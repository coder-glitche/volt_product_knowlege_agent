# White-labelled Redirection Journey for B2B Partners v2

: Gautam Mahesh
Created time: October 3, 2024 6:37 PM
Status: In progress
Last edited: November 14, 2024 7:27 PM

# **What problem are we solving?**

Smaller B2B partners want to go live with Volt’s offering but don’t to spend a lot of bandwidth in validating the demand. Hence, they choose to opt for the redirection based offering.

The current redirection based offering presents the below challenges.

- Customers sourced from partners not having trust as they don’t know Volt
- Partners not being comfortable in bringing Volt to the flow
- Customers dropping off on Volt’s homepage
- Partners not opting to go-live with Volt
- Time taken to go-live for partners increase impacting adoption

The above challenges can be attributed to the below reasons.

- Lack of partner’s branding (logo/name)
- Lack of partner’s color theme on Volt
- Lack of dedicated landing page/flows for partners

While incorporating the above points will consume considerable bandwidth, we want to validate the adoption of a white-labelled journey where no logo or branding of Volt is visible. 

---

# **How do we measure success?**

We can measure the success of this feature through the below metrics.

- Number of partners who go live increase by at least 10
- Number of redirection journeys from partners increase by at least 1000/month.
- Number of applications received from partners increase by at least 500/month.
- Time required for partners to reduce by at least 90% to 3 days.

Below are the guardrail metrics.

- Ability to track application by partners.
- Non-branded pages render better or same (TAT) than branded pages (<3s).

---

# **How are others solving this problem?**

This problem is being solve by different players in multiple approaches.

- **Approach 1**: redirection based flow with specific partner themed journey
- **Approach 2**: redirection based flow with Volt themed journey
- **Approach 3**: redirection based flow with a non-themed journey

Below are the considerations for each of the approaches.

|  | **Approach 1** | **Approach 2** | **Approach 3** |
| --- | --- | --- | --- |
| Customer trust | High | Low | Medium |
| Conversion* | High | Medium | Medium |
| Effort | Low^ | Medium | Very Low |
| Partner comfort | Very High | High | Medium |

Considering that we want to validate the adoption of redirection flows, Approach 3 is considered the most appropriate at this stage. 

*the premise here is that customers value the flow that is closest to the customer’s context.

^ we have already built the capability to handle UI schemes basis 

---

# **What is the solution?**

## Requirements overview

Below are the key requirements.

- This journey will not have mobile verification through OTP which is the case currently.
- This journey will be implemented for MFC fetch based journeys to start with.
- This journey will not have any Volt logo or branding on any of its page
- All the pages that are external like Digilocker, NACH will continue with existing UI theme
- We will maintain different UTM parameters for each partner as this journey will be rolled out to multiple partners
- We will need to maintain UTM parameters on each page to ensure we are able to track the application.
- We will need to render the pages as per the asset type (mobile/laptop) to ensure customer experience is maintained.
- Partner will pass us a dynamic application ID for each application in the URL which can be used by us to map and intimate the partner through webhooks or show on dashboard.

## User stories / User flow

Below are the user stories.

- Customer views the banner created by Volt/partner on the native asset (eg. Phonepe) of the partner’s domain
- Customer clicks on the banner and is redirected to the Volt homepage. On this page, there’s no logo of volt. Also, we need to host this on a separate page
- Customer won’t have to enter their mobile number and OTP
- Customer enters the PAN number and completes the MFC fetch. On this page, there’s no logo of volt.
- Customer fetches the funds after entering the OTP or faces an error. On this page, there’s no logo of volt.
- Customer views the offer on the Set Credit Limit page which is a function of the funds fetched. On this page, there’s no logo of volt.

## Requirements

---

# **Design**

While there’s no complete design intervention needed, it does require design sanity and sign-off.

---

# **Analytics**

Below are the analytics/metrics that need to be tracked.

- Number of redirections that need to be captured on Amplitude
- Number of MFD fetches that were started by entering PAN.
- Number of MFD fetches that were completed by entering OTP.
- Number of customers who reached the sanction stage.
- Number of applications by partners at each stage.

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
    - [ ]  Build a variant of the product note for redirection flow
- [ ]  Business
    - [ ]  Get feedback on the redirection flow and drive adoption
    - [ ]  @Keyur Lo to share the pipeline for this customer flow
- [ ]  Design
    - [ ]  

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# Feature Roadmap

Below are the subsequent features we plan to consider in the roadmap.

- Dedicated landing page for each partner in their native theme for medium/large partners
- Dedicated configuration based journeys for medium/large partners
- Reduction in the number of fields in the journey for conversion %age

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes