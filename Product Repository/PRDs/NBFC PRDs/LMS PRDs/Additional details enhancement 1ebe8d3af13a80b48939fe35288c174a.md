# Additional details enhancement

Last Edited: June 27, 2025 8:43 AM
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

To support underwriting and assess the end use of funds, we currently collect the following additional user details:

- Marital status
- Educational qualification
- Mother's first and last name
- Father's first and last name
- Loan purpose
- Income range
- Employment status

While this information is essential, requiring users to fill seven separate fields has contributed to a noticeable drop-off rate—ranging from **1% to 5% across different LSPs**—which negatively impacts the top of the funnel.

---

# **How do we measure success?**

- Conversion rate post the additional details step across LSPs as a %
- Conversion rate from KYC to loan completion as a %

---

# **How are others solving this problem?**

| Field | Public Sector Banks | Private Banks | NBFCs | Fintech Lenders |
| --- | --- | --- | --- | --- |
| **Marital Status** | ✅ | ✅ | ✅ | ✅ |
| **Educational Qualification** | ❌ (often skipped) | ✅ (selectively) | ✅ (optional) | ✅ (in underwriting) |
| **Mother’s Name** | ❌ | ❌ | ❌ | ❌ |
| **Father’s Name** | ✅ (for KYC match) | ✅ | ✅ | ✅ (if PAN mismatch) |
| **Loan Purpose** | ✅ (drop-down) | ✅ | ✅ | ✅ |
| **Income Range** | ✅ (salary slips, ITRs) | ✅ | ✅ | ✅ |
| **Employment Status** | ✅ | ✅ | ✅ | ✅ |

---

# **What is the solution?**

- V2 API with optional and mandatory fields
    - Mandatory fields:
        - Employment details
        - Income range
        - Father’s name
        - Loan purpose
    - Optional fields
        - Educational qualification
        - Mother’s name
- Handling UI changes on Command centre to make it intuitive for the operations team

## User stories / User flow

- Details will be collected via LSP in the loan application flow for DSP.
- LSP will pass the additional details to DSP Finance via the additional details utility.

## Requirements

### Making details optional

As described above following details will be made optional as additional details, please note the details will be made optional for all LSPs and will be LSP agnostic

Command centre design changes: @Karuna Sankolli 

- Operations team should have clear visibility on mandatory and non mandatory fields
- LSPs can still pass non mandatory fields, we will have to ensure, even if they are not mandatory, details are available to view in the checker task as well as on the client details screen when passed or available

### Agreement and KFS changes:

We will retain the fields in the loan kit and will not be updating the templates, these fields will be printed when available for the user, and will be null when not passed.

---

# **Design**

**Objective:**

Enhance the Command Centre to provide clear visibility of both mandatory and non-mandatory fields submitted by LSPs, ensuring data transparency for the operations team.

**Requirements:**

1. **Field Visibility Differentiation:**
    - Clearly distinguish between **mandatory** and **non-mandatory** fields in both the **checker task view** and the **client details screen**.
2. **Non-Mandatory Field Handling:**
    - If LSPs pass non-mandatory fields, these should be displayed **without omission** in both views.
    - Ensure non-mandatory fields are **visibly marked** (e.g., tag, icon, or style differentiation) to aid quick recognition.
3. **Data Integrity:**
    - Ensure no loss of field data, even if non-mandatory, during internal processing or UI rendering.

**Outcome:**

Operations team can view all submitted data (mandatory or otherwise) clearly, enabling accurate verification and decision-making.

@Vaibhav Arora 
**Figma designs**

[https://embed.figma.com/design/KBCUs2Ea5SO2rhTOoZb8Oj/LOS--Command-center?node-id=1768-10075&t=1DwCH0S2wlavEwXQ-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/KBCUs2Ea5SO2rhTOoZb8Oj/LOS--Command-center?node-id=1768-10075&t=1DwCH0S2wlavEwXQ-11&embed-host=notion&footer=false&theme=system)

---

# **Analytics**

- Drop-off rate at additional details step

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