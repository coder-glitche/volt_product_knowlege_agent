# Term Loan: Foreclosure

# Overview

Loan/Tranche foreclosure refers to the early repayment and closure of a loan/tranche by the borrower before the scheduled loan/tranche tenure ends.

# **What problem are we solving?**

For Borrowers:

•	Interest burden: Reduces overall interest paid over the loan/tranche tenure.

•	Debt-free sooner: Achieves financial freedom earlier than planned.

•	Flexibility: Allows reallocation of capital or freeing up of credit limits.

For Lender/Business:

•	Reduces credit risk: Full repayment eliminates the risk of future defaults.

•	Recycling capital: Frees up capital for new disbursements, improving portfolio turnover.

---

# **How do we measure success?**

From a lender/fintech/product perspective, success is measured by:

Borrower-side metrics:

•	% of loans/tranche foreclosed early (segmented by loan type, tenure, customer cohort)

•	Average interest saved per borrower (customer benefit)

Lender-side metrics:

•	Reduction in default rates in foreclosed loan/tranche cohort

•	Operational efficiency of foreclosure process (TAT to process closure)

---

# **How are others solving this problem?**

Banks & Traditional Lenders

•	Foreclosure charges (especially on fixed-rate loans): A monetization mechanism to offset interest loss.

•	Offline, branch-heavy process: Requires physical visits, slow processing.

•	Limited transparency: Many borrowers don’t know the actual outstanding, charges, or procedure.

NBFCs & Fintech Lenders

•	Digital foreclosure calculators: Self-service tools for borrowers to assess foreclosure amount and component bifurcations.

•	App/portal-based foreclosure initiation: Simplifies the experience.

•	Pro-rata interest adjustment: Clear breakdown of interest saved and final amount due.

•	Incentivized early repayment: Some fintechs give interest rebates or lower charges on early closure.

•	Instant loan closure certificates/downloads via app.

---

# **What is the solution?**

## Requirements

### **Tranche Foreclosure**

Tranche Foreclosure enables users to foreclose individual tranches via the LSP app or by reaching out to support team. The foreclosure process is initiated by the user and processed manually by DSP through a non-STP flow. This section outlines the end-to-end flow, including eligibility, amount computation, validations, and post-foreclosure updates.

**Tranche Foreclosure/Net Payable Amount (NPA) Formula:**

Tranche Net Payable Amount=POS+IOS+Accrued Interest+Charges Outstanding−Excess

**Components:**

- **POS**: Tranche Principal Outstanding
- **IOS**: Tranche Interest Outstanding
- **Accrued Interest**: Based on business hours (see below)
- **Charges Outstanding**: Tranche-level unpaid charges
- **Excess**: Tranche level excess(Loan level excess not to be used here)

---

---

### **Flow of Events**

1. User will come to the LSP app to initiate a Tranche Foreclosure.
2. Once the user initiates the Foreclosure request from the LSP app for a Tranche, LSP app will get the Tranche Foreclosure details from DSP. For this they will call DSP’s Get foreclosure details API(Same as OD). 
3. DSP internally will do few validations to check if Foreclosure of the Tranche is allowed and also call Finflux’s API to get the Net Payable amount. Below are the Validations which DSP needs to perform:

| **Validations**  | **Tranche** | **OD Product** |
| --- | --- | --- |
| Loan account Exist | Required | Same as OD |
| Tranche account exist | Required | Not in OD |
| No Dues on any of the Tranches | Required | Not in OD |
| Non terminal foreclosure request of same Tranche | Required | Not in OD |
| Non terminal foreclosure request of Loan | Required(Not required in V0) | Same as OD |
| Non terminal collection request present | Required | Same as OD |
| Non terminal charge request present | Required(Not required in V0) | Same as OD |
| Non terminal repayment(non-foreclosure) request for Tranche/Loan | Required | Same as OD |
| Loan account Frozen | Required | Same as OD |

If any of the above check fails then in response to the LSP we will mention that “Foreclosure is not allowed”. If none of the above check fails then we provide LSPs with the Net payable amount for the Tranche.

1. **Business Hours Logic**
- If foreclosure amount is fetched **before 6 PM**, it includes **same-day accrued interest and same day penal charge**. Finflux’s API(Simulation API) will provide this based on the Transaction Date we pass in the API.
- If fetched **after 6 PM**, it includes **next day's accrued interest and penal charge**(Only applicable if tranche is in Overdue state)**.** Finflux’s API(Simulation API) will provide this based on the Transaction Date we pass in the API.
- If LSP sends the foreclosure request to DSP **before 6 PM**, repayment is posted the **same day**.
- If sent **after 6 PM**, posting happens **next day**.
1. **LSP** should be provided the below details in the Get foreclosure details API response:
    - Net Payable Amount: DSP gets this amount using Get Clear Dues Template API which is a simulation API provided by Finflux.
    - Loan ID and Tranche ID
    - Component-wise breakup will be provided. Below are the components(These components are the same as OD but here its the Tranche components):
        
        **Outstanding Principal**
        
        **Outstanding Interest**
        
        **Outstanding Charges**
        
        **Outstanding Penal Charges**
        
        **Total Due**
        
        **Excess Amount**
        
        **Net Payable**
        
        **Interest Accrued Not Due**
        
    - Remarks and other parameters which are passed in OD
2. **~~Rounding Logic for Net payable amount(Same as OD):** Net Payable Amount will be rounded to the nearest rupee using the **half-even rounding method** (same as the OD product). Finflux’s simulation API provides the foreclosure amount rounded to upto 2 decimal places as the decimal rounding configuration is at a currency level and changing it will result in rounding of the transaction amounts as well. We have to handle the half-even rounding on Fenix’s end to provide the LSP with an amount rounded off to the nearest rupee.~~
3. LSP shows the foreclosure details to the user on the app.
4. **User pays the Net Payable Amount and LSP sends the repayment details in the Create repayment order API.** 
5. **LSP then calls the initiate foreclosure request API and passes the repayment order ID to DSP(Same as OD)**
6. **Once the foreclosure request is raised by the LSP, DSP performs below mentioned validation(Above mentioned validations in point 3 will be done again):**

| **Validations**  | **Tranche** | **OD Product** |
| --- | --- | --- |
| Foreclosure amount greater than or equal as Net payable amount | Required | Same as OD |
1. **If validation fails**: Foreclosure request is rejected with error to LSP(Same as OD). Communication to be sent to the user(To be finalized)
    
    **If validation passes**: Foreclosure proceeds
    
2. Checker process is created for the Ops team with the Maker notes(Same as OD)
3. **Ops team (Command Centre)** approves foreclosure manually (non-STP process), same as OD product
4. Excess Settlement: Need to add
5. Finflux’s Foreclosure API is called.
6. **Apportionment** is done across all components by Finflux
7. **Tranche balances** are updated by Finflux
8. **Finflux makes all balances related to the Tranche as 0 along with the below action:** 
    - Finflux stops the Repayment Schedule (RPS) for the Tranche
    - Finflux marks the Tranche as **Closed**
9. LSP will be able to get the Foreclosure status through an API and the component wise details needs to be provided in the same. The components here will be the same as OD product with an addition of Tranche ID.
10. Communication is sent out to the user confirming the foreclosure of the Tranche. 
The template and responsibility on whether the Lender or LSP will send it is yet to be closed.

---

### **Important Notes**

- **Multiple tranches** can be foreclosed simultaneously, but not the **same tranche** in parallel.
- **No collateral unlodgement** will happen automatically on Tranche Foreclosure.
- **No STP process** will be followed for foreclosure.

## **Loan Foreclosure**

Loan Foreclosure allows users to foreclose the entire loan, which includes all open tranches, via the LSP app or by reaching out to support team. The process calculates the net payable amount, performs validations, collects repayment, and initiates manual foreclosure approval. Upon successful completion, all tranches and the loan itself are closed.

---

## V0 Scope

In the current scope we won’t be providing users with the ability to close the entire loan with a single payment. The user needs to close each active tranche first then only they will be able to close the loan. This process of events will pan out in the below described manner:
 

### Flow of Events

1. User can have multiple Tranches against their Loan facility.
2. If users want to close their Loan in entirety and exit from the facility they will have to close all their Tranches individually.
3. In order to close each Tranche they will have to go through the exact process of Tranche Foreclosure as described in the above module of Tranche Foreclosure. 
4. The entire process of Tranche Foreclosure remains the same including all the validations and checks described in Tranche Foreclosure module.
5. Each Tranche Foreclosure will go through the non-STP flow of maker checker.
6. No unlodgement will happen when one/all Tranche/s is/are foreclosed. 
7. Once all the Tranches are closed successfully then only the user will be able to close the Loan.
8. When the user initiates the Loan foreclosure request LSP will call the Get Foreclosure Details API.
9. Once the Get Foreclosure Details API is called by the LSP, DSP will validate the below checks:

| **Validations**  | Loan | **OD Product** |
| --- | --- | --- |
| Loan account Exist | Required | Same as OD |
| All Tranches should be closed  | Required | Not in OD |
| Non terminal foreclosure request of any Tranche | Required | Not in OD |
| Non terminal foreclosure request of Loan | Required | Same as OD |
| Non terminal collection request present | Required | Same as OD |
| Non terminal charge request present | Required(Not required in V0) | Same as OD |
| Non terminal repayment(non-foreclosure) request for Tranche/Loan | Required | Same as OD |
| Loan account Frozen | Required | Same as OD |
| Non terminal disbursement request present | Required | Same as OD |
| Non terminal add collateral request present | Required | Same as OD |
| Non terminal remove collateral request present | Required | Same as OD |
1. If any of the above mentioned validations fail then the Foreclosure of Loan won’t be allowed and the same would be passed in response to the LSP along with the specific validation failure message.
2. If all of the above mentioned validations pass then Foreclosure of the Loan will be allowed and the Net Payable amount of the Loan will be passed in the Get Foreclosure Details API response along with the component bifurcations:
    
    **Outstanding Principal**
    
    **Outstanding Interest**
    
    **Outstanding Charges**
    
    **Total Due**
    
    **Excess Amount**
    
    **Net Payable**
    
    **Interest Accrued Not Due**
    
3. The API to be used by DSP, to get the Loan Foreclosure details, from Finflux would be the same Clear Dues Template API used in the OD product. This API is yet to be tested for Term Loan: Loan Foreclosure. This testing needs to be done by Product and Tech and if it does not work as per expectation then the same needs to be raised to Finflux.
4. **Rounding Logic for Net payable amount(Same as OD [Pre Clear Due step]):** Net Payable Amount will be rounded to the nearest rupee using the **half-even rounding method** (same as the OD product). Finflux’s simulation API provides the foreclosure amount rounded to upto 2 decimal places as the decimal rounding configuration is at a currency level and changing it will result in rounding of the transaction amounts as well. We have to handle the half-even rounding on Fenix’s end to provide the LSP with an amount rounded off to the nearest rupee.
5. Once the user completes the Loan Foreclosure payment through the LSP app then the LSP needs to raise a repayment request to DSP by passing the repayment details in the **Create repayment order API.** 
6. **LSP then calls the initiate foreclosure request API and passes the repayment order ID to DSP(Same as OD).**
7. **Once the foreclosure request is raised by the LSP, DSP performs below mentioned validation(Above mentioned validations in point 9 will be done again):**

| **Validations**  | **Tranche** | **OD Product** |
| --- | --- | --- |
| Foreclosure amount greater than or equal as Net payable amount | Required | Same as OD |
1. Any charge which is outstanding on the Loan level will be posted and if the excess is below Rs 0.50 then a transaction of this excess amount is posted but this amount is not collected from the user. If the excess is above Rs 0.5 then the foreclosure flow moves forward**(Same as OD [Post Clear Due step])**
2. The checker process for the foreclosure request should be created. Based on the checker approval the foreclosure request moves ahead(Same as OD).
3. Once checker approval happens we will refund any excess which is present i.e. greater than Rs 0.5(Same as OD).
4. Post the Excess settlement the unlodgement flow is also triggered. If the unlodgement flow completes successfully then the Foreclosure request moves ahead otherwise the foreclosure request gets rejected(Same as OD).
5. When unlodgement happens successfully then the Foreclosure API is called and the Loan will be closed with the Loan status updated as closed(Same as OD).
6. LSP will be able to get the Foreclosure status through an API and the component wise details needs to be provided in the same. The components here will be the same as OD product.
7. Communication is sent out to the user confirming the foreclosure of the Loan. 
The template and responsibility on whether the Lender or LSP will send it is yet to be closed.

## V1 Scope(To be Closed/Pending)

### **Loan Foreclosure/Net Payable Amount (NPA) Formula**

Loan Net Payable Amount=Loan POS+Loan IOS+Loan Accrued Interest+Loan Charges Outstanding−Loan Excess

**Components:**

- **Loan POS**: Principal Outstanding across all open tranches
- **Loan IOS**: Interest Outstanding across all open tranches
- **Loan Accrued Interest**: Sum of accrued interest of all open tranches(Based on business hours described below)
- **Loan Charges Outstanding**: Charges across tranches and loan level
- **Loan Excess**: Total excess tagged to the loan

**Rounding Logic:**

Final Net Payable Amount will be rounded to the nearest rupee using the **half-even rounding** method (as used in the OD product).

---

### **Business Hours Logic**

- If fetched **before 6 PM**, it includes **same-day accrued interest and same day penal charge**
- If fetched **after 6 PM**, it includes **next day's accrued interest and penal charge**(Only applicable if account is in Overdue state)
- If the request is sent to DSP **before 6 PM**, posting happens **same day**
- If the request is sent **after 6 PM**, posting happens **next day**

---

### **Flow of Events**

1. **User** initiates Loan Foreclosure via **LSP app**
2. **LSP** calls the **Loan Foreclosure API**, receiving:
    - Net Payable Amount using foreclosure details API
    - Component-wise breakup will be provided in the same
3. **User pays the Net Payable Amount and LSP sends the repayment details in the repayment order API.** 
4. **LSP then calls the initiate foreclosure request API and passes the repayment order ID to DSP**
5. **Post accrued interest and charges**
6. Collateral based checks are performed and if the checks pass. The collaterals are then blocked and a checker process is created. The checker process is then approved and the securities are unlodged and unpledged then the foreclosure request proceeds.(Will add the collateral validation)
7. **DSP performs validations**:
    
    
    | **Validations**  | Loan | **Validation Step** |
    | --- | --- | --- |
    | Loan account Exist | Required |  |
    | Non terminal foreclosure request of any Tranche | Required |  |
    | Non terminal foreclosure request of Loan | Required |  |
    | Non terminal disbursement request | Required |  |
    | Non terminal add collateral request | Required |  |
    | Non terminal sell off collateral request | Required |  |
    | Non terminal excess settlement request | Required |  |
    | Non terminal mandate request present | Required |  |
    | Non terminal charge request present | Required |  |
    | Non terminal repayment(non-foreclosure) request | Required |  |
    | Non terminal remove collateral request | Required |  |
8. **If validation fails**: Foreclosure is rejected, error returned to LSP. Communication to be sent to user(To be finalized)
    
    **If validation passes**: Proceed to foreclosure
    
9. **Ops team** (Command Centre) **approves manually** (non-STP)
10. **Apportionment** occurs across all components of tranches and loan
11. **Update balances** for each tranche and loan
12. **If all tranche balances = 0**:
    - RPS of all tranches is stopped
    - Tranches are closed
13. **If all tranches closed and loan balance = 0**:
    - Loan is marked **closed**
14. **DSP sends confirmation** to LSP with updated balances and component-wise settlement breakdown. 
15. Communication and NOC is sent out to the user confirming the foreclosure of the Tranche. 
The template and responsibility on whether the Lender or LSP will send it is yet to be closed.

---

### **Important Notes**

- All open tranches are foreclosed in this process
- Multiple loan foreclosure requests **cannot run in parallel**
- No STP process is involved, similar to the OD product

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