# NBFC NACH: Mandate Limit Change

: Gautam Mahesh
Created time: May 29, 2025 3:20 PM
Status: Ready for Tech
Last edited: August 13, 2025 6:31 PM
Owner: Parikshit Kumar

# **What problem are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

---

# **How do we measure success?**

- **Mandate setup completion rate** increase by at least 600bps for customers
- **Overall funnel conversion rate** improvement of 450 additional conversions per month
- Reduction in **customer support queries** related to mandate amount
- Reduction in **customer and partner calls** related to mandate amount
- Reduction in **average time spent** at the mandate step

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

Below is the new user flow for Volt.

- The customer fetches the funds and gets an offer
- The customer chooses an offer which might be the same or lower than the eligible amount
- The customer completes the flow till bank account verification
- The customer reaches the mandate step
- The customer sees the mandate amount as below.
    - 20% of the selected offer with minimum of 10K AND maximum of 10 Lacs
- The amount decided is passed to Digio in registering the mandate
- The customer completes the mandate registration flow

Below is the enhancement flow for Volt.

- The customer initiates enhancement on Volt through UI
- The customer fetches the funds and receives the offer
- The customer selects the offer on UI
- If the selected offer amount/original DP > 5, the customer needs to do re-mandate for 20% of the selected offer with minimum of 10K AND maximum of 10 Lacs
- The customer is shown the option to undertake a new mandate registration
- The amount derived above is passed to Digio in registering the new mandate
- The customer completes the mandate registration flow
- DSP marks the older mandate as inactive and the new mandate as active. The same is communicated to the customer on the UI and through SMS/PN.

### LSP

Below is the user flow for LSPs.

- The customer fetches the funds and gets an offer on LSP UI
- The customer chooses an offer which might be the same or lower than the eligible amount on LSP UI
- The customer reaches the mandate step on LSP UI
- DSP takes the amount received at an opportunity level from the customer through the offer generation API or through the fetch wrapper API
- DSP will not consider the mandate amount in the [Create Mandate API](https://documenter.getpostman.com/view/37292788/2sB2cVfNR4#ff86391a-7e03-4065-bc44-1a129b549934) for now
- The customer sees the mandate amount as below.
    - 20% of the selected offer with minimum of 10K AND maximum of 10 Lacs
- The amount decided is passed to Digio in registering the mandate
- The customer completes the mandate registration flow

Below is the enhancement flow for LSPs.

- The customer initiates enhancement on LSP through UI
- The customer fetches the funds and receives the offer
- The customer selects the offer on UI
- If the selected offer amount/original DP > 5, the customer needs to do re-mandate for 20% of the selected offer with minimum of 10K AND maximum of 10 Lacs
- The customer is shown the option to undertake a new mandate registration
- The amount derived above is passed to Digio in registering the new mandate
- The customer completes the mandate registration flow
- DSP marks the older mandate as inactive and the new mandate as active. The same is communicated to the customer on the UI and through SMS/PN.

### Presentation

- DSP will use the latest mandate to present the dues

# **Design**

We will need to build the flow for registering a mandate post account opening for enhancement journeys.

---

# **Analytics**

Below are the metrics we will track on Volt side on a daily/weekly/monthly level at a customer(Unique) and attempt level.

- Number of customers who reached the mandate step
- Number of customers who initiated mandate registration
- Number of customers who completed mandate registration
- Number of chats related to mandate amount.

Below are the metrics we will track on DSP side on a daily/weekly/monthly level at a customer(Unique) and attempt level.

- Number of API calls to register mandate
- Number of customers who initiated mandate registration
- Number of customers who completed mandate registration

We will measure the L1 metric of mandate completion/mandate initiation as the overaching metric.

---

# **Timeline/Release Planning**

---

# **Go to market**

### Roll Out Plan

The current Mandate Limit of 10 Lacs is a high amount for users with much lower credit lines which in turn impact the Mandate conversions. In order to improve the conversions we are considering lowering the Mandate limit. For deciding the amount to which the mandate limit should be lowered to, we will be testing the conversion rates for two different mandate amounts. One amount which is equal to the selected offer and the other amount which is equal to 20% of the selected offer.

- We would be rolling out this Mandate Limit change feature in an A/B Test manner over a Control group and two Test groups.
- The Control group users would have the Mandate limit as 10 Lacs, which is the current setup, and the Test groups will have the Mandate limit as:- Test Group 1: 20% of the Selected Offer, Test Group 2: Selected Offer.
- We would be going ahead with this A/B implementation on all Volt Channels(Excluding Groww and INDMoney)

- The roll out will be in the following manner:
- Day 1 - Control: 80%, Test 1: 10%, Test 2: 10%
- Day 2 to Day 3 - Control: 50%, Test 1: 25%, Test 2: 25%
- Day 4 to Day 5 - Control: 20%, Test 1: 40%, Test 2: 40%
- Day 6 to Day 7 - Control: 0%, Test 1: 50%, Test 2: 50%
- Post Day 7, based on the A/B test data we will be increasing the roll out for the Test group which performs better i.e. Mandate completion rate is better.
- [Proposal]If the mandate completion rate is comparable for both the test groups then we will go ahead with the test group which gives the business an option to debit a higher amount from the customer(in this case Test group 2) in case we want to debit the Principal or to file for a recourse.
- If the mandate completion rate is comparable for all three groups then we can decide with the larger audience if we want to go ahead with the 10 lacs mandate limit amount.
- In case of limit Enhancement, the re-mandate flow won’t be available to the customers during this launch even if the following condition: mandate amount becomes < 4% of the DP, is met.
- Once we have observed the impact on the Mandate conversion rate for Groww we will be planning to roll this out for other LSPs as well.

[**Mandate Limit Change for LSPs**](NBFC%20NACH%20Mandate%20Limit%20Change/Mandate%20Limit%20Change%20for%20LSPs%2024ee8d3af13a803d8ff9e8518ba6e4c5.md)

### Timeline

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Inform Groww about the change
    - [ ]  Conduct a VOC parallely with the customers to understand the reason behind dropping off from the Mandate setup flow
    - [ ]  Train Sales and Ops about the change
    - [ ]  Provide Analytics team with the metrics we need to track related to this change
    - [ ]  Plan the re-mandate flow for Groww and other LSPs(Which are live with the enhancement flow)
    - [ ]  Inform 3rd party LSPs that are live with DSP
    - [ ]  Inform 3rd party LSPs that are integrating with DSP
- [ ]  Business
    - [ ]  
- [ ]  Design
    - [ ]  Design for enhancement flow

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