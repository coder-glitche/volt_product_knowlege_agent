# Phase 1: LTV /Tenure Update_LOS

: Priyamvada S
Created time: May 13, 2026 4:23 PM
Status: Not started
Last edited: May 29, 2026 8:52 AM

# **What problem are we solving?**

DSP's LAMF product offers 45% LTV on equity and hybrid funds, compared to 70% LTV offered by banks — making it structurally uncompetitive. This gap limits DSP on three fronts:

- **Existing customers** are under-drawing against already-pledged assets, leaving loan book growth on the table
- **New customers** in lower-ticket segments have sufficient collateral at 70% LTV but fall below viable thresholds at 45%
- **Product parity** with banks cannot be achieved without closing this 25pp LTV gap

---

# **How do we measure success?**

1. % Increase in eligible (>10k)customer base 
2. % Increase in monthly disbursals from new customers 
3. % increase in ‘offer select’ completion rate 

---

# Scope

### In Scope

Product

- Support for both LTV45 & 70 product offers
- Support for  6-year tenure migration
- Partner-specific product config (LTV 45/70) for recommended offer
- Providing offer visibility to Sales/CS

Customer Scope

- New customers
- In journey users

Platform Scope

- DSP (Fenix)
- LSP integrations
- Volt & its partners

Product scope

- Term Loan
- LAMF

# **What is the solution?**

## Solution overview

- DSP to support multi offers ie both LTV45 & LTV70 offers for LSPs
- DSP to validate offers chosen by LSPs

## Detailed solution

## *Fenix Requirements*

### Primary Use cases

- Expose both LTV45/LTV70 offers and associated pricing grids
- Maintain LTV70/45 product preference of LSPs
- Validate offers chosen by LSPs
- New & in-journey customer provisions

### Detailed requirements

Offer Management APIs

a) Fetch Offer API

On invoking the Fetch Offer API, the LSP will receive:

- List of all available LTV-based offers with offer name (’contract ID=Offer50/’offer75’)
- A recommended offer determined using the predefined LSP preference configuration stored internally by DSP
    - LSP can share their preference for any of the below 3 :
        - Offer 50
        - Offer 75
        - All LTV offers (default)

Note:

- By  default, LSP’s would be enabled for the ‘all  LTV offers’ option
- List will contain only those offers with LTV higher than the recommended offer

The LSP may consume the required offer(s) to:

- Compute maximum eligible loan limit
- Determine applicable loan pricing terms using the shared pricing grids, including:
    - ROI :
    - Processing Fee (PF)
    - Annual Maintenance Charges (AMC)
    - Limit Enhancement Fee

b) Offer Generation API

This is an optional API for LSPs and follows the same structure as the Fetch Offer API.

c) Accept Offer API

Once the user selects an offer, the LSP must invoke the Accept Offer API with the selected offer details.

Mandatory Parameters

- ISIN(s)
- LTV
- LTV
- Tenure
- ROI
- PF
- Margin pledge fee
- Facility limit
- AMC : DSP to accept the shared AMC but no AMC  charge will be applied for the first year
- Limit Enhancement Fee : Value would be ‘0’ for all LOS users
    - LTV-70% & tenure=3 or 6 years >> Limit enhancement fee not applicable
    - LTV-45% &  tenure=3 or 6 years >> Limit enhancement fee will be surfaced in LMS KFS (in LTV upgrade flow)
    
    DSP Validation Logic
    
    Upon receiving the request, DSP will:
    
    1. Invoke Script Master using `Offer 50`
        - Retrieve all equity funds
        - Retrieve all debt/hybrid funds
    2. Validate each shared ISIN against the Script Master ‘Offer 45‘ ISIN ranges
        1. If validation succeeds under Offer 50:
            - DSP Offer Engine will assign `Offer 50 & validate next whetehr the pricing parameters shared by LSP are within the 'Offfer 50' range`
            - If pricing parameter validation is also successfull, DSP will return the generated `AcceptOfferID` to the LSP
    3. If validation failed under Offer 50,DSP will invoke Script Master using `Offer 70`
        - Validate whether the rejected ISINs falls within the LTV 70 min/max range
        - If validation succeeds under LTV 70:
            - DSP Offer Engine will assign `Offer 70  & validate next whetehr the pricing parameters shared are within the 'Offfer 70' range`
            - If validation successfull, DSP will return the generated `AcceptOfferID` to the LSP
        - If validation fails under LTV70
            - DSP to return ‘Incorrect LTV/Pricing paramter value’ error to LSP.
    
    Note: Since DSP allows offer modification until agreement signing, the user may complete pledge creation using Offer A, while the Agreement API may later receive an updated Offer B from the LSP. This can result in:
    
    - Insufficient pledged funds, or
    - Excess pledged funds compared to the final selected offer.

d) Generate Loan Contract API

The LSP will invoke this API with the `AcceptOfferID` (optional).

Behaviour

- If `AcceptOfferID` is provided:
    - KFS will be generated using the corresponding accepted offer configuration
- If `AcceptOfferID` is not provided:
    - DSP will use the latest accepted offer stored in its configuration
- If no accepted offer exists in DSP configuration:
    - DSP will default to:
        - Recommended LTV ie  LSP LTV preference stored in internal config
        - Tenure received in the Loan Contract API request
    
    Note: If the tenure passed in the Loan Contract API differs from the tenure shared in the latest Accept Offer API, DSP must honor the tenure from the latest Accept Offer API
    
    e) Command Centre changes
    
    For ‘Loan creation approval’ request, following sections will reflect the value corresponding to respective LTV product construct.However Ops just need to review them to ensure they are within the regulatory limits  (same as existing)
    
    | CC section | Parameters | Values |
    | --- | --- | --- |
    | Interest tab | Interest rate | - |
    | Loan tab | Tenure  | 3 or 6 years |
    | Charges tab | -Processing Fee
    -Line enhancement fee
    -AMC charges | -
    -0 (new customers)
    - |
    | Loan Kit |  | KFS changes> ‘Line enhancement charge’ addition
    Agreement changes> Tenure limit options: 3/6 years
     |
    
    Note: For LOS CC requests (eg: loan creation NSTP request), no separate indicator is required to distinguish between LTV75/LTV40 products, since CC validations are based only on regulatory parameter limits, which are independent of the product construct
    

## *LSP Flow Enablement Requirements*

New customer (Phase1)

1. **Fetch / Generate Offer**
    - LSP invokes Fetch Offer or Generate Offer API
    - DSP returns:
        - All eligible offers
        - One recommended offer based on partner-specific internal configuration
2. **Offer Selection**
    - After user selects an offer, LSP invokes the `Accept Offer` API with the selected offer details
    - DSP validates the offer and returns an `AcceptOfferID`
3. **Loan Contract Generation**
    - LSP invokes the Loan Contract API with the `AcceptOfferID`
    - Loan contract / KFS by DSP is generated based on the accepted offer configuration ie tenure, ROI, Facility limit all are picked from

In-journey customer  (Phase 1)

### Pre-agreement signing

Definition:

- Phase -1 refers to customers whose latest activity in the LOS journey was before the Phase 0 launch
- Phase 0 refers to customers whose latest activity in the LOS journey was in the Phase 0  launch

| **Customer stage** | **Phase** | **What happens** | **Offer terms** |
| --- | --- | --- | --- |
| Pre-pledge | Phase -1 or Phase 0 | LSP shows revised offer to all customers and hits 'Accept Offer' API with new offer ID in Contract API | LTV & tenure per revised offer config |
| Pledge in progress / completed | Phase -1 | LSP either shows revised offer and hits Accept Offer, OR shares tenure = 3 yrs in Loan Contract — we pick LTV from partner config | LTV 45% or 70% (from config) · 3 yrs |
|  | Phase 0 | LSP shares terms as accepted in Phase 0 | LTV 70% · 6 yrs OR LTV 45% · 6 yrs |
| KFS initiated & within validity | Phase -1 | LSP shares LTV 45% and tenure = 3 yrs. KFS is cached at our end — we don't regenerate or recheck config. Loan created on cached KFS terms | LTV 45% · 3 yrs |
|  | Phase 0 | LSP shares terms as initiated in Phase 0 | LTV 70% · 6 yrs OR LTV 45% · 6 yrs |
| KFS initiated & now expired | Phase -1 | LSP shares tenure = 3 yrs. We recheck config and regenerate KFS | LTV 45% or 70% (from config) · 3 yrs |
|  | Phase 0 | LSP re-hits API with their tenure (3 or 6 yrs). We honour that tenure and pick LTV from internal config | LTV per config · tenure as shared by LSP |

### Post-agreement signing

| Customer stage | What happens | Offer terms |
| --- | --- | --- |
| **Agreement signed** | Loan account opened on the terms in the signed agreement. No changes. | As per signed agreement |

**Note:** 

For LTV-70 offers, configured partner-specific ROI & PF will be applicable.

## *Volt Requirements*

### Primary use cases

In addition to the Phase 0 use cases, the following additional requirements need to be addressed:

- Support both LTV45/70 loan product offers  in Volt UI for customer selection
- App smith /LSQ visibility wrt selected product construct (LTV45/70)
- Journey handling of existing users who are still in the LOS flow

### Detailed requirements

*a.Journey/API integration requirement :*

a1.Fetch (Anchor page)

- Volt will hit DSP fetch API to receive all the applicable offers with recommended offer as ‘Offer45’
- Volt checks ‘internal config’ to determine the offer & in-turn the max eligible limit to be shown on Anchor page wrt Volt partner preference (ie recommended product)
    - Note: For partners doing fetch on their own, Volt to pass only single offer based on partner preference & partner to show max limit accordingly
- Need to introduce a new flow wherein a customer can either proceed with the max limit directly or can choose to update the limit by going via ‘Set credit limit’ flow

a2. Offer Generation — “Set Credit Limit” Screen

On user landing on ‘Set Credit limit’ screen, for cases where the LTV70 product construct is applicable, Volt will support displaying both LTV product offers within the UI, enabling users to choose between the available product constructs.

On the “Set Credit Limit” screen:

- Volt will support both LTV45 and LTV70 loan amount ranges.
- If the user selects a loan amount within the LTV45 range:
    - funds will be mapped using the LTV45 construct, and
    - the corresponding interest construct will apply.
- As the user moves the slider beyond the LTV45 range into the LTV70 range:
    - funds will progressively start switching to the LTV70 construct,
    - and at the maximum eligible limit, all applicable funds will reflect LTV70.
- Volt will abstract the selected funds list within an ‘Edit selected funds’ L2 flow which will dynamically update based on the slider selection

Note:

- Interest rate variation between LTV45 and LTV70 constructs will not be surfaced on the “Set Credit Limit” screen (to be closed based on A/B results)
- The applicable pricing variation will only be shown on the subsequent “Loan Offer” page.
- For cases where LTV45 product is chosen by partner, Volt shouldn’t show LTV70 product  even if eligible

a3. Loan offer screen

- Based on the selected limit, user will be shown the applicable ROI, Tenure & charges.
    - Tenure: This will be set to ‘6 year’ by default. User can choose to update the tenure to ‘3 years’ by clicking on ‘edit button’
    - Fallback to LTV45 entry point: If a user selects an LTV70 loan offer but prefers a lower interest rate, they can use the supported fallback entry point to navigate back to the “Set Credit Limit” page, where the loan amount range will be snapped to the LTV45 construct for selection.
    - Following are the pricing parameter values to be configured at Volts end for LTV45 & 70 product:
        
        
        | Parameter | Range | LTV45 | LTV70 |
        | --- | --- | --- | --- |
        | Processing Fee | Min/Max |  |  |
        | Interest Rate | Min/Max |  |  |
        | Margin Pledge Fee | Min/Max |  |  |
        | Enhancement Fee | Min/Max |  |  |
        | AMC | Min/Max |  |  |
        | Tenure | 1–6 years |  |  |

a4. Offer Acceptance API (mandatory)

On clicking ‘Continue’ on loan offer screen, Volt will hit DSP’s accept offer api & share chosen:

- ISINs , units & LTV
- Tenure
- Pricing  parameters value (ROI, PF, Charges)

Volt will receive either a success with offerID from DSP or a reject with relevant failure reason on which Volt can correct the values /display to customer and on acceptance of the offer re-hit the accept offer API with the corrected values 

Note: Volt can invoke the “Offer Accept” API multiple times throughout the journey until the Agreement stage. However, the final Offer ID must be passed in the Agreement API, post which the loan offer can no longer be modified.

2e. KFS/Agreement Changes

Volt to provide the DSP ‘accepted offer ID’ in the loan contract api for generation of KFS/Agreement .DSP will validate the offer ID and return the DSP redirection url.

a4.Remaining flows

| Stage | Volt |
| --- | --- |
| Client dedupe | No change |
| Opportunity creation | No change |
| Offer page | Migrate to DSP offer generation API.  To be invoked on  user landing on ‘Set credit limit’ screen. Received offers to then be stored on Volt end such that on loan amount slider movements, Volt computes and updates the data based on the cached ISIN/LTV values |
| Accept offer | Accept offer to be called on ‘Continue’ click on loan offer page. 
Until before pledging since user can edit the loan amount, on user edit they will be taken back to loan offer page and they can  update the loan offer and post it to DSP with ‘accept offer’ api. |
| KYC & Photo verification | No change |
| Additional details | No change |
| Bank a/c verification | No change |
| Mandate set up | No change |
| Pledge | No change |
| KFS/Agreement | No change |
| Submit opp | No change |

App smith changes

![Screenshot 2026-05-13 at 3.25.48 PM.png](Phase%200%20LTV%20Tenure%20Update_LOS/Screenshot_2026-05-13_at_3.25.48_PM.png)

‘LOS Application’ will carry the following sections will reflect the value corresponding to ‘LTV70’ product :

| Application tab | Parameters | Values |
| --- | --- | --- |
| Details | Interest rate | Will reflect ROI corresponding to LTV45/70 product |
| Approved funds | LTV | Reflect 45%/70% depending on chosen fund LTV  |
| Unapproved funds | LTV | Reflect 45%/70% depending on chosen fund LTV  |
|  |  |  |

LSQ changes:

Note: For users who are still in the LOS flow:

- User crossed the loan offer screen: If user clicks the ‘credit limit’ edit option from any of the screens till pledge stage,user to be shown a revised offer screen reflecting increased limit with LTV70 & tenure=6 yrs
- User in the pre-loan offer selection flow: User on resuming the flow will land on the ‘anchor page’ and will be shown the updated ‘credit limit’corespinding to LTV70 prodcut construct.On moving ahead to loan offer page, tenure will be updated to show 6 years

---

# **Design**

PFA the [design](https://www.figma.com/design/uztYv9y1Rzk6AAHpKWVB3L/Multi-loan-offer?node-id=4859-2351&t=TSlHOYlbquDvSCP1-0) here

---

# **Analytics**

PFA the [requirement here](https://docs.google.com/spreadsheets/d/1POA-6Ei420RvyeDxFg02L9BaPrKX0CA_7YhZP7uroB8/edit?userstoinvite=mohit.pareek%40voltmoney.in&sharingaction=manageaccess&role=writer&gid=1189711996#gid=1189711996)

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