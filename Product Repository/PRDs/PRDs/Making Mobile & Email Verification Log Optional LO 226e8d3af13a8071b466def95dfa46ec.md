# Making Mobile & Email Verification Log Optional: LOS & CC Changes

: Priyamvada S
Created time: July 4, 2025 9:43 AM
Status: Not started
Last edited: July 18, 2025 12:17 PM

# **What problem are we solving?**

As per RBI’s CDD guidelines, verifying ~~either~~ the customer’s ~~mobile number or~~ email is mandatory. Currently, LSPs must verify ~~the mobile number and submit mobile verification &~~ email and pass the verification logs via the `mobile_verification_log`/`email_verification_log` APIs respectively. The resulting utility IDs are required in the `Submit Opportunity` API to create the loan application at DSP’s end.

However, some LSPs have highlighted friction in integrating these additional API, noting that both mobile number & email are already verified on their end and can be shared with DSP on demand when required.

---

# **How do we measure success?**

Adoption of Optional Log Flow:  % of LSPs skipping the email verification_log/ `~~mobile_verification_log`~~ API

---

# **How are others solving this problem?**

NA

---

# **What is the solution?**

To reduce integration friction while maintaining regulatory compliance, we propose making the ~~mobile verification log API &~~ email verification log API optional. Instead, DSP will include a clause in the LSP agreement mandating that LSPs verify the ~~mobile number/~~email  shared with DSP during opportunity creation and ensure that ~~mobile &~~ email verification logs can be furnished offline, on demand, whenever requested by DSP to meet audit and compliance requirements

~~This exemption is **not applicable** if:~~

- ~~The LSP does **not** use DSP’s fund fetch or lien marking APIs, or~~
- ~~The LSP allows the user to update/change the mobile number before initiating DSP’s fund fetch or pledge flow.’~~

# PRD Scope

Due to certain compliance/legal constraints, this feature scope is limited to sourcing channel=’PhonePe” and for its Phase 1 launch only (Tentative ETA: Sept 30)

## Requirements

### 1. LOS Onboarding Flow Changes

**Objective:**

Simplify LSP integration by making the ~~mobile verification log  &~~ email  verification log  APIs optional

**Requirements:**

- ~~Mobile &~~ Email verification Log API
    - LSP can skip integrating this  ‘Email verification log’ API .
- **Submit Opportunity API:**
    - The `~~mobile_verification_log`~~ /`email_verification_log` utilities should be made optional for the LSP

---

### 2. Command Centre Dashboard Enhancements

Requirement:

The ‘Non-STP account opening’ cases to carry ‘email delivery status logs’ instead of the ‘email verification status logs’

**Scope of Change:**

### a. Task Type: `Loan Creation Approval`

- **Current data:**
    - Loan creation approval request contains ‘email verification’ logs under the ‘email verification’ section
- **Updated Behavior:**
    - ~~Mobile verification &~~ Email verification log to be replaced with ‘email delivery’ logs

### b. UI Changes – Verification Log Section

- **Within ‘Email verification’ section :**
    - Verified status to contain ‘email delivery logs’ .
    - Sample delivery log copy :
        - ”Delivered by DSP Finance at 21-Sept-2025,11:07:25
        - Customer IP:10.83.70.70
- **Fi~~eld Tagging:~~**
    - ~~Within the `Phone No Verification` & Email Verification subsections:~~
        - ~~Tag both `Verification Status` and `Customer IP` fields with ‘**Optional’ tag**~~
- **~~Approval Logic:~~**
    - ~~If `Verification Status` and `Customer IP` are **empty**, Ops **can still approve** the case.~~
    - ~~If values are **present**, Ops can review and consider them before approval.~~
    
    ![image.png](Making%20Mobile%20&%20Email%20Verification%20Log%20Optional%20LO/image.png)
    

### c.Ops Training & Communication

Need to ensure the Ops team is aware of the updated data format that will come  in the ‘email verification’ log section

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