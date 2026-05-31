# Pre-fetch flow optimisation:Email entry/verification

: Priyamvada S
Created time: June 8, 2025 5:04 PM
Status: Not started
Last edited: June 9, 2025 11:10 AM

# **What problem are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

- 

---

# **What is the solution?**

### **A. Delay Email Capture Until After MFC Fetch & Remove email verification flow**

- Remove the ‘email entry + verification screen’ appearing before MFC fetch
- Instead take user directly to ‘Check eligibility’ screen post mob verification to initiate MFC fetch
    - **If email is available via MFC fetch:**
        - Use it as the default email ID for the user and pass it on for opportunity creation
        - Post opportunity creation & KYC completion, prefill it in the "Additional Details" screen ( post-KYC flow) for user review
        - Allow the user to edit if incorrect (no verification needed)
    - **If email is not available via MFC fetch:**
        - Show a simple email entry field after fetch but before KYC
        - The captured email ID is then passed on to DSP BE for opportunity creation
- Email verification will no longer be done and will be removed from the onboarding flow

**Proposed User Journey /Requirements**

**Category 1: B2C/B2B2C/ Applicable B2B partners**

These are flows where mob & email capture/verification happens before MFC fetch

New User flow

- After successful mobile OTP login user lands on the ‘Eligibility check initiation’ screen (ie ‘Check eligible credit limit’ screen)
- The user is prompted to enter their PAN number,DOB and review their pre-filled mobile number to trigger the MFC eligibility check.
- **User with Email in MFC Fetch**
    - Upon successful eligibility fetch, receives user’s email from MFC fetch response and passes on the same to DSP BE for opportunity ID creation
    - User shown the same email ID prefilled but editable format in ‘Additional details’ screen (post kYC) for review and update (if needed)
    - In case user updates the email ID, the same to be passed on to DSP BE to update the email ID associated with the opportunity ID
- **User without Email in MFC Fetch**
    - Upon successful eligibility fetch, if email ID is not present in MFC fetch response, surface the email entry screen post loan offer confirmation (ie pre KYC init)
    - The captured email ID is then passed on to DSP BE for opportunity creation

Note: Email verification is not done in either of these cases

**Category 2: B2B Platforms /B2C Web app**

These are platforms where users go through MFC fetch flow before email capture/verification

New User flow

- **User with Email in MFC Fetch**
    - Upon successful eligibility fetch, receives user’s email from MFC fetch response and passes on the same to DSP BE for opportunity ID creation
    - User shown the same email ID prefilled but editable format in ‘Additional details’ screen (post kYC) for review and update (if needed)
    - In case user updates the email ID, the same to be passed on to DSP BE to update the email ID associated with the opportunity ID
- **User without Email in MFC Fetch**
    - Upon successful eligibility fetch, if email ID is not present in MFC fetch response, surface the email entry screen post loan offer confirmation (ie pre KYC init)
    - The captured email ID is then passed on to DSP BE for opportunity creation

Note: Email verification is not done in either of these cases

### **Mitigating Risks from Dropping Email Verification**

### **A. Ensuring Document Delivery to Correct Email**

Since emails are not verified, there's a risk of users receiving loan documents at outdated or incorrect email IDs. To mitigate this:

- Loan documents will also be sent via SMS with a clickable link.
- SMS format:
    
    "Your loan documents have been sent to [email]. If this isn’t your email, click here to update it."
    
- Clicking the link opens the email update screen either in the app or mobile browser.
- Once the user updates their email, it is pushed to DSP backend to update the email linked to the opportunity.

### **B. Fallback Verification for Sensitive User Requests**

In cases where users initiate sensitive requests (e.g., unpledging or mobile number update):

- **If the user emails from an unverified ID:**
    - Trigger OTP to their registered mobile number.
    - If OTP is successfully validated, mark the email as verified and proceed.
- **If the user has lost mobile access and emails from an unverified email:**
    - Request the user to submit a selfie holding their Aadhaar card.
    - Ops team manually verifies the identity.
    - Upon successful verification, mark the email as verified and proceed with the request.

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