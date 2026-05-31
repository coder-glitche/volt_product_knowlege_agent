# Lodgement STP optimisations

: Ameya Aglawe
Created time: April 7, 2025 2:21 PM
Status: Pending Review
Last edited: May 20, 2025 4:16 PM

# **What problem are we solving?**

- Currently about 15% of the lodgements are flowing through non-STP flow requiring a lot DSP Ops bandwidth and keeps the customers blocked
- The top 2 reasons for the non-STP cases are -
    - Facility value threshold being 10L
    - Pledging and lodgement date mismatch

---

# **How do we measure success?**

- Increase in STP flows from 79% to 91% *(assuming SR of consolidated lien status to be 100%)*
- Decrease in 1st disbursal delay for customers
- Decrease in customer queries related to 1st disbursal to partner LSPs’ support team & DSP support team

---

# **How are others solving this problem?**

---

# **What is the solution?**

## User stories / User flow

## Requirements

---

### 1. Increase Threshold for FV-Based STP Eligibility

**Current Logic:**

Collateral additions with FV ≤ ₹10L qualify for the  STP route.

**Proposed Change:**

Increase this threshold from ₹10L to ₹30L.

**Expected Impact:**

This change is expected to reduce the volume of applications routed through the non-STP flow by ~30%, leading to faster processing and reduced ops bandwidth.

---

### 2. Skip Pledge Date vs. Lodgement Date Check

**Current Logic:**

Applications are flagged for manual review if the pledge date and lodgement date do not match.

**Proposed Change:**

If we receive a **successful** response from the consolidated lien status API, we will **bypass** the pledge date ≠ lodgement date check.

**Rationale:**

A successful consolidated lien status API response serves as a reliable confirmation of pledged_units=lodgement_units, rendering this additional check redundant.

---

### Following is the summary of the lodgement STP logic after the above two optimisations

| S.no | Checks | Condition  | Action |
| --- | --- | --- | --- |
| 1. | Maker initiated request | -  | Non-STP |
| 2. | LTV overridden lodgement for loan | -  | Non-STP |
| 3. | Consolidated lien API check  | API failed | Non-STP |
|  | Consolidated lien API check  | API executed | Do the 4th check (FV) |
| 4. | Facility value check  | 0<FV≤30L | STP  |
|  |  | FV>30 | Non-STP |

Note : The below checks are listed in the order of priority and must be executed in the same sequential order as mentioned in the table.

# **Design**

---

# **Analytics**

---

- Number of collateral additions flowing through the STP route
- Number of collateral additions flowing through the non-STP route
    - Bi-furcation of different reasons/checks due to which collateral additions are passing through non-STP route
- Consolidated lien API success & failure rate

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

- When we get LM hold from KFIN, we have to do manual lodgement
    - WHY: We do not get terminal state from the RTA
    - DSP ops team get consolidated data from the data and get it lodged
- Are we cancelling the lodgement request if we are getting any error ?
-