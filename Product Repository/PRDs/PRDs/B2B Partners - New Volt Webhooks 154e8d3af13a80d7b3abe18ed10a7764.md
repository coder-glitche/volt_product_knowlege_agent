# B2B Partners - New Volt Webhooks

: Nihal Simha M S
Created time: December 6, 2024 8:48 AM
Status: Done
Last edited: January 6, 2025 6:45 PM

# **What problem are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their ability to manage customer interactions efficiently.

**Note:** 

1. While the requirement was initially raised by Zype, the proposed webhook solution will be available for the entire SDK, allowing all partners to opt in as needed.
2. Missing webhooks to develop. (Tech team to come back on this)

---

# **How do we measure success?**

1. **Reduced Support Tickets:** A decrease in the number of support tickets raised by B2B partners requesting the status of transactions such as loan account creation, margin shortfall, foreclosure, lien removal, and repayments. 
This will indicate that the new webhook system is providing the necessary updates and reducing the need for manual follow-ups.

---

# **How are others solving this problem?**

1. **Timely Callbacks:** Partners receive real-time updates for key events like loan creation, margin shortfall, foreclosure, lien removal, and repayments.
2. **Centralized Dashboards:** A few companies provide dashboards where partners can track all loan activities and updates in one place.

---

# **What is the solution?**

### Phase 1 - Enabling on Staging

1. **Enable Webhooks on Staging:**
    - Loan Account Created:
        - This is used to track customers with pending lodgment or disbursal cases. Support team intervention is required to collect the necessary documents from customers to complete the loan account creation process.
    - Lien Removal Status (Requested, Initiated, Rejected):
        - This status is required to be displayed in the partner app to inform users and enable the partner support team to track and manage lien removal requests effectively.
    - Margin Shortfall Occurred and Ageing:
        - This is necessary for white-labeled journeys on B2B platforms to notify customers who are experiencing margin shortfalls, ensuring timely communication and resolution.
    - Foreclosure (Initiated, Processed, Requested, Rejected):
        - Currently, only the foreclosure-processed webhook is available. This limitation prevents the partner support team from tracking the total number of customer requests, monitoring TAT, and identifying other request statuses effectively.
    - Repayment Initiated, Success:
        - Currently, only repayment success webhooks are provided. This restricts the partner's operations team from tracking when a customer initiated repayment and how long it has been pending, causing delays in addressing repayment-related queries.
2. **Monitor and Resolve Issues:** Monitor the callbacks for a week and fix any issues.
3. **Enable for All B2B Partners on Staging**

### Phase 2 - Enabling on Production (Next Sprint)

1. **Enable Webhooks for Zype on Production:** Monitor for a week and fix any known issues.
2. **Enable for All B2B Partners**

@keyur Lo to inform partners before enabling callbacks on staging and production.

### Webhooks Structure (Key Requirements)

- Loan Account Created
    - Loan account number
    - Lender name
    - application type(Primary/ Secondary)
    
    +
    
- Lien Removal
    - List of mutual funds
    - Lein removed units for each MF
    - Updated credit limits - only for success.
    - Status(Success/ Failure)
- Margin Shortfall
    - Shortfall amount
    Due amount
    - Aging
- Foreclosure
    - Status(success/ failure)
    - lender name
    - loan account id
- Repayment
    - Same as successful but status as “Initiated”

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