# Deferring email capture and verification during onboarding

: Devansh Kar
Created time: August 13, 2025 7:20 PM
Status: Not started
Last edited: September 26, 2025 7:05 PM

# **What problem are we solving?**

Currently we are observing a drop-off of 15% on average across Volt Channels at Email verification step in 30 day window (Apr ‘25). As email is asked from the user during initial part of onboarding process, the drop-offs are higher and needs to be reduced to <10% across Volt channels.

![image.png](Deferring%20email%20capture%20and%20verification%20during%20on/image.png)

---

# **How do we measure success?**

- x% increase in conversion at email verification step

---

# **How are others solving this problem?**

---

# Scope

The scope of the PRD is limited to all the Volt channels (B2C mobile, B2C web, B2B2C and B2B platforms)

---

# **What is the solution?**

- We are proposing to defer the email verification step to later stage in the funnel i.e. pre-agreement creation in order to reduce user drop-off at the initial stage.
- The idea for deferring the email verification to post pledge and pre-agreement is based on the intent of the user which would be high during the later stage of the funnel compared to asking for email verification at initial stage where the intent is usually low leading to higher drop-offs here.

## User stories / User flow

## Approach

High level approach.

- Remove email verification after mobile
- Place email verification after pledge and before agreement
- Any email received from MFC will be pre-filled on the email verification page
- Email verification itself will be allowed through Google SSO and OTP

### **Current flows:**

For Volt channels:

**Flow 1 (B2C mobile):**

Mobile login → Email entry (SSO + Manual)→ Email verification → ~~PAN verification (PAN + DoB input)~~ → Check eligibility page (Fetch)[PAN + phone number] → Eligible limit page → Loan offer page → KYC → Bank Verification → Mandate → Pledge → KFS and Agreement

**Flow 2.1 (B2B2C - Partner led journey):**

Customer registration [Phone no. + full name] → Email entry → Email OTP verification → ~~PAN verification (PAN + DoB input) (getting removed)~~ → Check eligibility page (Fetch)[PAN + phone number] →  Eligible limit page → Loan offer page → KYC → Bank Verification → Mandate → Pledge → KFS and Agreement

**Flow 2.2 (B2B2C - Partner led journey):**

Check eligibility page (Fetch)[PAN + phone number] → Customer registration [Phone no. + full name] → Email entry → Email verification →  Eligible limit page → Loan offer page → KYC → BAV → Mandate → Pledge → KFS and agreement

**Flow 3 (B2B - Platform SDK led journey):**

Fetch/ Check eligibility page (PAN + DoB) → Eligible limit page → SDK init → Email entry → Email verification → Unlock credit limit screen → Loan offer page  → KYC → BAV → Mandate → Pledge → KFS and agreement

## Requirements

**US1:** As a user, I should be shown email entry and verification page only after pledge completion and before agreement step.

**Success Criteria:**

**Frontend:**

- The email verification page wherever existing for partners/ users in Volt channel should be removed from pre-KYC onboarding step.
- User should be redirected directly to PAN verification page (if fetch has not happened initially for the user through check eligibility and user coming through mobile verification).
- User should be redirected directly to eligible limit page (if user is coming through check eligibility page where fetch has already happened).
- Email verification page shall be moved to post pledge step and before agreement step.

**Backend:**

- Email shall be an optional field for opportunity creation in DSP backend.

**US2:** As a user, I want to verify my email ID from any one of the available options provided by Volt.

**Success Criteria:**

**Frontend:**

- The user shall be shown pre-filled email fetched from MFC/ RTA in case email is not passed from platform or if the user is coming through B2C/ B2B2C flows.
- The above email (platform/ MFC) will be used to display the email to be verified by the customer. The customer, however can choose to verify any other email ID as well
- We will allow user to verify their email ID through Google SSO or email OTP. This might or might not be the email fetched from MFC/ RTA/ platform.

We will need to modify the existing email verification page with messaging around the fetched message and reasoning for email verification for sending important communications etc. 

**US3:** As a user, my loan agreement will contain the email ID updated on email verification page before agreement and welcome email will be triggered on the verified email id.

**Success Criteria:**

**Frontend:**

- Loan agreement will contain the email sent from backend based on final email verified by user before agreement.
- Welcome email will be sent to user on the latest mailID given by user.

**Backend:**

- Final email entered by user with OTP verification shall be stored and used for agreement creation and sending the welcome mail on the same.

**Edge case**

- **B2B Platform details passing:** If in case partner passes the emailID in CreateCustomer API this will be prioritized over MFC/RTA fetch email ID for prefilling and verification.
- For B2C platform, Google SSO option will also be there.
- In case of B2B and B2B2C, Google SSO option will not be provided.

---

# **Design**

Existing email verification page to be changed.
https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=7589-6620&t=8mYfH06xmgSoM6lK-11

---

# **Analytics**

- Number of customers who landed on email entry screen
- Number of customers with prefilled email
- Number of customers proceeding with prefilled email
- Number of customers who landed on the verification page
- Number of customers who verified
    - SSO
    - Email OTP

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
    - [ ]  Inform SDK partners about journey changes
    - [ ]  Write a 1 pager about the flow change (Release note)
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