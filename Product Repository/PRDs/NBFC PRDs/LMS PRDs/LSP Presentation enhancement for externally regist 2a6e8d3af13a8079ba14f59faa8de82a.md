# LSP: Presentation enhancement for externally registered mandates

Last Edited: November 21, 2025 2:07 PM
PRD ETA: November 10, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

Currently, all mandate registrations for DSP Finance are done internally through our TSP (Digio) integration. As we onboard LSP partners like Smallcase, there is a need for them to independently initiate mandate registration flows while still maintaining DSP Finance’s sponsor bank credentials.

This enhancement allows Smallcase to register mandates on behalf of DSP Finance, improving the customer experience by reducing redirects and enabling a native flow within the LSP app.

However, since mandates will be registered from the partner’s Digio account, DSP will not have direct access to those Digio mandates and must handle downstream flows (like presentation) differently.

---

# **How do we measure success?**

- Accurate tagging of internal vs. external mandates in LMS
- No breakage in downstream presentation flow for externally registered mandates

---

# **How are others solving this problem?**

Other TSP-integrated NBFCs (like RazorpayX, Cashfree, or PayU) enable LSP-managed mandate registration by extending API credentials with credential management on the LSPs end.

---

# **What is the solution?**

We will extend mandate registration capability to Smallcase via Digio by sharing DSP’s sponsor bank configuration. Smallcase will have restricted access — limited only to mandate registration (not cancellation or presentation).

Post successful registration, Smallcase will call submitMandateDetails API to push the mandate details to DSP for internal record-keeping and tagging.

During future mandate presentations, if the mandate is tagged as external, DSP will additionally pass bank_account and ifsc in the presentation request since these details are unavailable within DSP’s Digio account context.

## Requirements overview (optional)

- Extend DSP’s sponsor bank access to Smallcase’s Digio account
- Introduce tagging for **mandate registration type** (`internal` or `external`)
- Modify mandate presentation logic to include bank details for `external` mandates
- Restrict LSP permissions to registration only - Managed outside implementation
- Update internal dashboards and reconciliation processes to recognize external mandates

## User stories / User flow

**User Story 1:**

As an LSP (Smallcase), I should be able to register a mandate on behalf of DSP using DSP’s sponsor bank configuration via my Digio account.

**User Story 2:**

As DSP, I should be able to receive mandate details via API post-registration to store and tag the mandate as `external`.

**User Story 3:**

As DSP, I should be able to correctly present external mandates by including `bank_account` and `ifsc` fields in the presentation request.

**User Flow:**

1. User initiates mandate registration on Smallcase app
2. Smallcase registers mandate with Digio (DSP sponsor bank config)
3. Upon success, Smallcase calls DSP’s `/submitMandateDetails` API with mandate reference details
4. DSP stores the mandate with tag = `external`
5. During presentation, DSP includes `bank_account` and `ifsc` in the Digio presentation API request

## Requirements

- **Mandate Registration Extension:**
    
    Enable Smallcase to register mandates using DSP’s sponsor bank configuration on Digio. DSP will provide the necessary sponsor bank details and configuration setup.
    
- **API enhancement- `/submitMandateDetails`:**
    
    Enhance submit mandate API Smallcase to submit mandate registration details post successful registration. This will include fields such as mandate reference number, customer ID, registration date, account details, and mandate registration type.
    
    - Mandate type
    - UMRN
    - Mandate initiated date
    - Mandate expiry date
    - Mandate expiry amount
    - Bank account number
    - IFSC code
    - mandate_registration_type - LSP will have to pass ‘EXTERNAL’ here
- **Mandate Tagging:**
    
    Introduce a new attribute — `mandate_registration_type` — in the internal mandate schema to identify whether a mandate is registered internally or externally. This tag will be used across downstream systems (presentation, reconciliation, and reporting) - This will be powered by a sourcing channel level configuration, only certain LSPs should be allowed to register external mandates
    
- **Presentation Logic Update:**
    
    Update the presentation logic to handle externally registered mandates. For mandates tagged as `external`, DSP must pass `bank_account` and `ifsc` in the presentation API call to Digio since these are not available within DSP’s Digio account context.
    
- **Access Control:**
    
    Restrict permissions for LSP partners like Smallcase to mandate registration only. Cancellation and presentation APIs will remain accessible exclusively to DSP’s internal system.
    
- Mandate re-registration (Bank account update):
Mandate re-registration should be supported by the LSP, extendability via the submit mandate details API should support mandate registration post loan account opening (Like current implementation)
- **Dashboard and Reporting Updates:**
    
    Update internal dashboards, monitoring, and reconciliation tools to reflect mandate registration type (`internal` / `external`) for better traceability and operational visibility.
    

---

# **Design**

Command Centre design enhancements

- Show mandate registration type in CC at a loan account level
- Show mandate registration type during loan account creation process (Approval task)

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

- No direct marketing activity required.
- Internal communication to highlight improved LSP mandate registration flow.

## Ops & Sales training

- Training deck for Ops team on identifying and reconciling external mandates
- FAQs and troubleshooting guide for common issues in external registration

## Frequently asked questions (FAQs)

**Q1:** Can Smallcase cancel or present mandates?

→ No, only registration access is provided.

**Q2:** How do we differentiate internal vs. external mandates?

→ Based on the `mandate_registration_type` tag stored against each record.

**Q3:** What changes for DSP while presenting mandates?

→ For external mandates, bank account and IFSC are passed explicitly.

**Q4:** Will this flow extend to other LSPs?

→ Yes, design supports scaling to other LSPs with similar configuration.

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