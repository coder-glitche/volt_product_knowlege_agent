# Reducing Limit on DSP from 25K

: Gautam Mahesh
Created time: November 22, 2024 5:32 PM
Status: In progress
Last edited: December 6, 2024 3:39 PM
Owner: Saksham Srivastava

# **What problem are we solving?**

Currently, a lot of customers, especially in the B2B channels are dropping off due to the limit fetched being < 25,000. 

- ~5000 customers/month across channels (B2B, B2C) aren’t being serviced for having a limit b/w 10K and 25K
- ~4000 customers/month across channels (B2B, B2C) aren’t being serviced for having a limit b/w 5K and 10K
- Loss of customers to competitors like Fibe and Abhiloans who are servicing customers with limits of 15K and 7.5K respective
- Loss of revenue from PF and interest fee due to customers not taking a loan from DSP

These customers aren’t serviceable by other lenders and currently, we are processing loans with a lower limit of 25K.

Below is the breakup of the funnel and the expected impact.

| Funnel | 10K - 25K | 5K - 10K |
| --- | --- | --- |
| Monthly post-fetch | 5000 | 4000 |
| Account opening at 20% | 1000 | 800 |
| Avg. limit fetched | 16K | 7K |
| Total limit sanctioned | 1.6CR | 56L |
| Avg. PF | 999 | 499 |
| PF collected | 9,99,000 (assuming 999) | 4,99,000 (assuming 499) |
| Interest income @ 12% at 75% utilization/month | 1.2L | 42K |

**Note**: the above analysis doesn’t factor the re-marketing on existing customers or any new acquisitions in the MFD channels.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?//.**

## Requirements Overview

### Phase 1

- For customers fetching an eligible limit of higher than 10k and below 25k, assign lender to be DSP.
    - DSP lender should only be assigned for whitelisted platforms/partners. We should have ability to whitelist platforms and partners through a config (No release should be needed). The config should have the following parameters configurable:
        - Lender
        - Main application: Min eligbile credit limit
        - Margin pledge: Min eligible credit limit
        - Renewal: Min eligible credit limit
        - Processing fees for Main application, margin pledge, and renewal as basis credit limit slabs. Maintain PF and stamp duty breakup for lenders and platforms.
    - ~~The feature should also have an enable/disable flag.~~  This will be handled from the config itself.
- If DSP lender is assigned to a customer, he/she should be able to select a credit limit between the range of ₹10k to his/her eligible credit limit.
- Minimum eligible credit limit for margin pledge for DSP lender should be reduced to ₹10k as well. We should have the same whitelisted platforms/partners checks as the main application. The value of min margin pledge/enhancement should be read from the previously discussed config as well.
- Run lender assignment BRE on the MFC Check eligibility page. If the eligible credit limit for the customer is below 25k, assign DSP lender to the customer. When customer enters the application the same lender should reflect in the app.
    - No change in the MFC CAS fetch API (provided to partners)
    - Partners who are using the MFC redirection journey should be able to give credit limits lower than ₹25k to customers post this change.

### Phase 2

- FE changes across FAQs.
- Partners using CAS API will be required to make changes in their journey. They will be covered in subsequent phases.

## User stories / User flow

## Requirements

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