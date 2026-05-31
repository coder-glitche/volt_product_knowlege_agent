# Phase 0: LTV /Tenure Update_LOS

: Priyamvada S
Created time: April 20, 2026 3:35 PM
Status: Not started
Last edited: May 25, 2026 4:26 PM

# **What problem are we solving?**

Problem 1: LTV at 45

DSP's LAMF product offers 45% LTV on equity and hybrid funds, compared to 70% LTV offered by banks — making it structurally uncompetitive. This gap limits DSP on three fronts:

- **Existing customers** are under-drawing against already-pledged assets, leaving loan book growth on the table
- **New customers** in lower-ticket segments have sufficient collateral at 70% LTV but fall below viable thresholds at 45%
- **Product parity** with banks cannot be achieved without closing this 25pp LTV gap

Problem 2: Tenure at 3 years

RBI has recently mandated that repayments for credit line products must be completed within the approved line tenure. This effectively discontinues the existing line renewal construct currently used in the LAMF product.

Under the current 3-year tenure construct, customers have limited repayment flexibility, while the business loses the ability to extend customer relationships through renewals. Additionally, the shorter tenure limits the potential interest income and AMC revenue over the loan lifecycle.

---

# **How do we measure success?**

1. % Increase in eligible (>10k)customer base 
2. % Increase in monthly disbursals from new customers 
3. % increase in ‘offer select’ completion rate 

---

# Scope

### In Scope (Phase 0)

Product

- LTV increase from 45% → 70%
- 6-year tenure migration
- Partner-level LTV configuration
- Updated KFS/Agreement templates

Customer Scope

- New customers
- Existing users still within LOS flow

Platform Scope

- DSP (Fenix)
- LSP integrations
- Volt & its partners

### Out of Scope

Following are OOS for this PRD:

- Support for multiple loan offers to Volt customer
- Volt Frontend journey redesign

# **What is the solution?**

# Solution overview

- DSP to enable LSPs to onboard new customers on the LTV70 product construct.
- DSP to migrate all new customers across LSPs to a 6-year tenure construct for LTV45 & LTV70 products.
    
    

# Detailed solution

## *Fenix Requirements*

### Primary Use cases

- Maintain LTV70/45 product preference of LSPs
- Expose both LTV45/LTV70 offers and associated pricing grids
- Validate accepted offers (optional for Phase 0)
- Provide updated  agreement/KFS templates

### Detailed requirements

1. Partner-Level LTV Configuration

Fenix must maintain partner-level configuration indicating:

- whether LTV70 is enabled
- default recommended LTV product
- applicable pricing ranges

  Storing LTV Partner Preference:[Attached below is the finalised partner preferences:](https://docs.google.com/spreadsheets/d/1OCH_62HVvh51QKamYW37HFK5Sm_sLRx_RsCoLUNoGuQ/edit?gid=1027155293#gid=1027155293)

1. High level API/workflow requirements

2a. Fetch API Changes

Existing Flow

LSP → Fetch API → DSP fetches funds → DSP computes availble limits 

Proposed Enhancements

LSP→ Fetch API → DSP fetches funds → Internal Offer engine  runs→Computes Eligible LTV offers

ie Upon receiving the fetched funds, DSP will pass the ISIN, units, and applicable LTV into its internal offer engine to compute all eligible LTV offers for the user, along with the corresponding pricing parameter ranges, and return them in the Fetch API response. Additionally, DSP will mark the LSP’s preferred LTV product as the “recommended offer” in the response

| Parameter | Range | LTV45 | LTV70 |
| --- | --- | --- | --- |
| Processing Fee | Min/Max |  |  |
| Interest Rate | Min/Max |  |  |
| Margin Pledge Fee | Min/Max |  |  |
| Enhancement Fee | Min/Max |  |  |
| AMC | Min/Max |  |  |
| Tenure | 1–6 years |  |  |

Note: 

- Offer tagged as LTV70 if at least one pledged fund qualifies for 70% LTV.
- We’re introducing the additional fields to ‘fetch api’ so as to support quick go-live of LTV feature for partners who are not yet integrated with ‘Offer generation’ API

2b.Offer generation API  

    Same structure as fetch api

2c. Offer Acceptance API (optional for Phase 0)

LSP shares:

- ISIN
- selected LTV
- pricing  parameters chosen values

DSP will re-run its offer engine using the ISIN and units as inputs to compute the applicable offer. It will then validate the parameters shared by the LSP against the computed offer. If validation is successful, DSP will return the Offer ID; otherwise, it will reject the request with the error:

> “Shared offer pricing value is breaching lender accepted value.”
> 

2e. KFS/Agreement Changes

DSP to provide the updated KFS/Agreement for ‘LTV45/70 +6 year tenure’ product changes

Attached is the updated templates

2f. Submit Opportunity Changes

KFS parameter validation for STP/Non-STP routing will be performed against the fSTP ranges defined below.
Tenure: 72 years 
Interest Rate: 
Processing Fees:	
Margin Pledge Fees	
Annual Maintenance Fees

2g. Other stages

| Stage | Change |
| --- | --- |
| Opportunity Creation | No change |
| KYC | No change |
| Bank Verification | No change |
| Mandate | No change |
| Pledge | No change |
1. Command Centre changes

For ‘Loan creation approval’ request, following sections will reflect the value corresponding to 

| CC section | Parameters | Values |
| --- | --- | --- |
| Interest tab | Interest rate | To lie within the  supported range for the selected product construct (LTV45/LTV70) |
| Loan tab | Tenure | To reflect either 3 / 6 years |
| Charges tab | -Processing Fee-Enhancement fee-AMC charges | To reflect values within the  supported range for the selected product construct (LTV45/LTV70) |
| Loan Kit |  | KFS/Agreement template determined by:a)Selected LTV productb)Selected tenure (3 or 6 yrs) |

Note: For LOS CC requests (eg: loan creation NSTP request), no separate indicator is required to distinguish between LTV75/LTV40 products, since CC validations are based only on regulatory parameter limits, which are independent of the product construct

## *Volt Requirements*

### Primary use cases

- Configuring single LTV70 product for interested B2B ,B2B2C partners
- Rely on DSP to get single LTV70 loan offer (instead of internal config)
- App smith /LSQ to reflect LTV 70 product values
- Journey handling of users already in the LOS flow

### Detailed requirements

Volt will only be providing a single loan offer  (LTV45/70) to its users similar to the current behaviour & hence no journey changes are applicable for Phase 0.

1. *Storing Volt Partner <>LTV Preference* 

Volt to  maintain the following partner preference to determine whether or not LTV70 is to be enabled for particular partner or not.Attached below is the finalised partner preferences:

*b.Journey/API integration requirement :*

- In Phase 0, Volt will continue showing only a single loan offer to users (either LTV45 or LTV70 based on partner preference), similar to the current behaviour.
- Hence, no frontend journey changes are applicable for Phase 0.

b1. Fetch API

- Volt will consume the DSP Fetch API response containing following :
    - ISIN
    - Units
    - Applicable LTV
    - Eligible limit
- Volt will store both LTV45 and LTV70 offer data internally.
- Based on internal partner configuration, Volt will pick the maximum eligible limit corresponding to the “recommended” product construct (i.e. LTV70 if applicable; otherwise, default is set to LTV45), which will:
    - be displayed on the **Anchor Page** for Volt B2C users and partners using the Volt fetch journey
    - be shared downstream to partners handling eligible limit display on their own frontend (via fetch api). Note: Only a single product offer will be shared with the partner
- The “Fetched Funds” widget on this screen will display the funds with their maximum eligible limits determined by the applicable ‘recommended’ product construct(LTV70/45)

b2. Offer Generation — “Set Credit Limit” Screen

- Volt will invoke the DSP Offer Generation API to fetch the latest applicable:
    - ISINs
    - Units
    - LTV values for both: LTV45 & LTV70 products
- Volt will store this data and, based on internal partner configuration (ie r**ecommended product**), determine & display the max total eligible limit, along with the corresponding ISINs, units, and its eligible limits

Note: Volt should always display the max limit corresponding to recommended product on the slider

b3. Offer Selection Flow — “Loan Offer” Screen

- On user landing on the Loan Offer screen, Volt will invoke the DSP Offer Generation API again to fetch:
    - latest LTV45/LTV70 offers
    - pricing parameter ranges including:
        - ROI
        - Processing Fee
        - applicable charges
- Volt will use its internal offer engine to determine the final pricing values (ROI, PF, charges, etc.) from the ranges shared by DSP API.
- Volt will display the applicable offer to the user based on:
    - applicable LTV product
    - selected loan amount
    - internal partner configuration
- On clicking “Continue”:
    - Volt will invoke the DSP Accept Offer API (optional for Phase 0)
    - Volt will share the selected offer with DSP
    - DSP will internally validate the offer and return:
        - success + Offer ID, or
        - failure response

b4.Loan Amount Modification Behaviour

- Until pledge completion, users can modify the selected loan amount.
- On modification:
    - user will be redirected back to the “Set Credit Limit” screen
    - Volt will recompute/update the offer
    - updated offer will again be shared to DSP via Accept Offer API
- Even during modification flows, users will continue seeing only the single applicable product construct (either LTV45 or LTV70).

b5.Remaining flows

| Stage | Volt |
| --- | --- |
| Client dedupe | No change |
| Opportunity creation | No change |
| KYC & Photo verification | No change |
| Additional details | No change |
| Bank a/c verification | No change |
| Mandate set up | No change |
| Pledge | No change |
| KFS/Agreement | No change. |
| Submit opp | No change |

c*. Existing In-Progress LOS User Handling*

For users who are already in the LOS journey during rollout, the following handling will apply:

- Users who have already crossed the Loan Offer stage will continue on the existing product construct:
    - LTV: 45%
    - Tenure: 3 years
    This will remain unchanged even if the user edits the loan offer subsequently.
- Users who are still before the Loan Offer selection stage will be migrated to the updated product construct and shown:
    - LTV: 70%
    - Tenure: 6 years
    similar to the new customer journey.

*d. App smith changes*

![Screenshot 2026-05-13 at 3.25.48 PM.png](Phase%200%20LTV%20Tenure%20Update_LOS/Screenshot_2026-05-13_at_3.25.48_PM.png)

‘LOS Application’ will carry the following sections will reflect the value corresponding to chosen ‘LTV45/70’ product :

| Application tab | Parameters | Values |
| --- | --- | --- |
| Details | Interest rate | Will reflect ROI corresponding to LTV45/70 product |
| Approved funds | LTV | Reflect 45%/70% depending on chosen fund LTV  |
| Unapproved funds | LTV | Reflect 45%/70% depending on chosen fund LTV  |
|  |  |  |

*e. LSQ changes:*

Open points:

Partner on 70 shared a offer that isnot 70 in the contract api?

Ensuring tenue=6 years where ?

Are we sending both offers to Volt partners in phase 0 also;If so how do we validate if they are showig max limit corresspoindg tyo LTV70 and not 45

---

# **Design**

Phase 0 introduces:

- no frontend journey redesign
- no new screens
- no customer flow changes

Only backend product construct changes are introduced.

---

# **Analytics**

PFA the requirements [here](https://docs.google.com/spreadsheets/d/1POA-6Ei420RvyeDxFg02L9BaPrKX0CA_7YhZP7uroB8/edit?userstoinvite=mohit.pareek%40voltmoney.in&sharingaction=manageaccess&role=writer&gid=1061167390#gid=1061167390)

---

# **Timeline/Release Planning**

---

# **Go to market**

-

-

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

| CC section | Parameters | Values |
| --- | --- | --- |
| Interest tab | Interest rate | To lie within the  supported range for the selected product construct (LTV45/LTV70) |
| Loan tab | Tenure | To reflect either 3 / 6 years |
| Charges tab | -Processing Fee-Enhancement fee-AMC charges | To reflect values within the  supported range for the selected product construct (LTV45/LTV70) |
| Loan Kit |  | KFS/Agreement template determined by:a)Selected LTV productb)Selected tenure (3 or 6 yrs) |