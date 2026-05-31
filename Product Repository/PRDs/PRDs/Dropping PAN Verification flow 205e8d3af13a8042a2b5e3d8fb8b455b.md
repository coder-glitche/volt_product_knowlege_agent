# Dropping PAN Verification flow

: Priyamvada S
Created time: June 1, 2025 2:11 PM
Status: Not started
Last edited: May 21, 2026 7:53 AM

# **What problem are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

---

# **How do we measure success?**

- **Mandate setup completion rate** increase by at least 600bps for customers
- **Overall funnel conversion rate** improvement of 450 additional conversions per month
- Reduction in **customer support queries** related to mandate amount
- Reduction in **customer and partner calls** related to mandate amount
- Decrease in **average time spent** at the mandate step

---

# **How are others solving this problem?**

Lenders broadly follow the below logic.

- Term Loan: 2-4X the EMI amount
- Credit Line: 10% of the credit line

There are some players like CRED who take mandate as the entire loan amount to avoid re-mandates.

---

# **What is the solution?**

## Requirements overview

Implement a **dynamic mandate limit** system that determines the mandate value based on the customer’s selected credit limit. The scope is strictly applicable for DSP across Volt and other LSPs.

**Minimum mandate amount requirement assumptions**

1. Mandate shall be registered only for the collection of interest and charges.
2. Max PF = max (5% of DP + GST, 499 + GST) = 5.9% of limit
3. Max 3 months of interest + penal charges = 3.75% (15%p.a. ROI) + 0.25% penal charges (@~3% annual rate) = 4% of the Pledge limit
4. Minimum mandate amount = 10k
5. Minimum mandate amount formula during onboarding = Max (5.9% of Pledge limit, 5 x 4% of Pledge limit, 10k)

**Enhancement cases:**

1. In enhancement cases, we will need to do a re-mandate in cases where the limit increases such that the mandate amount becomes < 4% of the DP.
2. In cases where DP increases due to market value such that the mandate amount becomes smaller than 4% of DP, there is currently no mechanism to cap the exposure. In such cases, we shall require the customer to do a re-mandate for a higher amount when requesting a withdrawal that increases the exposure.

## User stories / User flow

### Volt

B2C

Below is the new user flow for B2C: App journey

Customer lands on the PAN entry/verification screen post succesful user login/email verification

Customer is prompted to enter just their PAN no to check their MF eligiblity and complete the rest of the onboarding flow

Note: In CKYC, as the customer will be prompted to enter their Name

### 

Below is the enhancement flow for  B2C: Webapp journey

### B2B2C

Below is the user flow for LSPs.

- The customer fetches the funds and gets an offer on LSP UI
    - Customer lands on Volt website and clicks on ‘Check my eligibIlity’ CTA
- The customer chooses an offer which might be the same or lower than the eligible amount on LSP UI
- The customer reaches the mandate step on LSP UI
- DSP takes the amount received at an opportunity level from the customer through the offer generation API or through the fetch wrapper API
- DSP will not consider the mandate amount in the [Create Mandate API](https://documenter.getpostman.com/view/37292788/2sB2cVfNR4#ff86391a-7e03-4065-bc44-1a129b549934) for now
- The customer sees the mandate amount as below.
    - 20% of the selected offer with minimum of 10K AND maximum of 10L
- The amount decided is passed to Digio in registering the mandate
- The customer completes the mandate registration flow

Below is the enhancement flow for LSPs.

- The customer initiates enhancement on LSP through UI
- The customer fetches the funds and receives the offer
- The customer selects the offer on UI
- If the selected offer amount/original DP > 5, the customer needs to re-mandate for 20% of the selected offer with minimum of 10K AND maximum of 10L
- The customer is shown the option to undertake a new mandate registration
- The amount derived above is passed to Digio in registering the new mandate
- The customer completes the mandate registration flow
- DSP marks the older mandate as inactive and the new mandate as active

---

# **Design**

We will need to build the flow for registering a mandate post account opening for enhancement journeys.

---

# **Analytics**

Below are the metrics we will track on Volt side on a daily/weekly/monthly level at a customer and attempt level.

- Number of customers who reached the mandate step
- Number of customers who initiated mandate registration
- Number of customers who completed mandate registration
- Number of chats related to mandate amount.

Below are the metrics we will track on DSP side on a daily/weekly/monthly level at a customer and attempt level.

- Number of API calls to register mandate
- Number of customers who initiated mandate registration
- Number of customers who completed mandate registration

We will measure the L1 metric of mandate completion/mandate initiation as the overaching metric.

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
    - [ ]  Inform 3rd party LSPs that are live with DSP
    - [ ]  Inform 3rd party LSPs that are integrating with DSP
    - [ ]  Inform Volt sales & business teams on the amount change
- [ ]  Business
    - [ ]  

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