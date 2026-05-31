# Volt - DSP LSP Integration Flow

: Gautam Mahesh
Created time: September 9, 2024 1:17 PM
Status: Not started
Last edited: October 7, 2024 11:14 AM

# **What problem are we solving?**

---

# **How do we measure success?**

Below are the metrics we want to maintain.

## Functional Metrics

- 

## Performance Metrics

- Penny drop validation TAT (90th) to be <2s
- KYC completion TAT (90th) to be <s
- Mandate completion TAT (90th) to be <s
- 

## Technical Metrics

- DSP API uptime to be at least 99%
- DSP API responses to behave as documented for at least 95%
- TAT for generating agreement (90th) to be < 5s

## Guardrail Metrics

- Volt’s side of metrics till x stage to be maintained

---

# **How are others solving this problem?**

Below are broadly the 2 approaches taken by lending fintechs.

- 

---

# **What is the solution?**

## Customer Journey

Below is the user journey for B2C.

1. Screen 1 - customer logs into Volt app after entering the OTP. This OTP is triggered and maintained by Volt.
2. 
3. Screen 2 - 
4. 

## Internal Journey

## Journey Mapping

Below are the customer journey and its components.

| **Step** | **Description** | **Volt** | **DSP** | **External** | Pending items |
| --- | --- | --- | --- | --- | --- |
| Landing page | Customer lands on Volt app | Yes | No | No |  |
|  | Customer enters the mobile and OTP is triggered | Yes | No | API call to Gupshup happens for triggering the OTP |  |
|  | Customer enters the OTP | Yes | No | API call to Gupshup happens for validating the OTP |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| Customer lands on the KYC page | KYC completion using Digilocker | Yes | Yes | DSP makes a call to Digio for creating a digilocker request |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | Customer views the detailed KFS on the page | Volt calls DSP’s backend to generate the UI on app.dspfin.com | Yes | None |  |
|  |  |  |  |  |  |
| Customer’s profile deviates from our policy | Customer sees a   | Volt shows the customer that their application is on hold  | Operations team reviews the application and signs-off on command center | None |  |
| Customer completes the application till the agreement step | Customer sees what? | Volt shows the customer that their application is on complete | Operations team reviews the application (QC/Ops) and signs-off on command center. Withdrawal is placed if requested |  |  |
|  |  | Volt shows the customer that their application is on complete and withdrawal is placed  | Operations team reviews the application (QC/Ops) and signs-off on command center. Withdrawal is placed if requested | Request placed with Cashfree for a disbursement |  |

---

# Out of Scope

---

# Roadmap

---

- Integration with DSP for MFD channel to be picked up
- Integration with DSP for B2B partners to be picked up

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

- To do
    - QA needs to comeback on load testing for Agreements
    -