# Skip Email verification

: Priyamvada S
Created time: November 12, 2025 11:08 AM
Status: Not started
Last edited: December 29, 2025 11:59 AM

# **What problem are we solving?**

Email verification is currently mandatory for loan application creation. However, we’re seeing around 15% **user drop-off** at this step. To reduce friction, we propose letting users **choose their preferred primary communication channel — SMS or Email** — and **skip email verification** for those who select SMS. This allows users who rely on SMS to continue without being blocked by email OTP verification.

---

# **How do we measure success?**

- **Increase in users reaching the agreement step**
- **Improvement in overall loan application completions:**

---

# **What is the solution?**

### Overview

Volt channels ([flow diagram](https://whimsical.com/volt-lsp-skip-email-verification-Q2qUcFeG7cQofGFLsKhw9k))

[](https://imgr.whimsical.com/object/AxGvwsXHVg3XGBVgVAwArg)

LSP ([flow diagram](https://whimsical.com/volt-lsp-skip-email-verification-Q2qUcFeG7cQofGFLsKhw9k))

[](https://imgr.whimsical.com/object/RbZwpT2Y3YjUdTnjK2E4HZ)

### **Details**

*Section 1: Capturing/Storing  primary communication mode*

A) All Volt channels (OD/LAS)

- User enters the loan application flow & reaches the ‘email id’ capture screen
- On the email capture screen, in addition to the email input field, we have the additional  consent checkbox (unchecked) with the following language:
    - By checking this option, you authorise the use of SMS as the primary communication channel instead of  email
- If user checks the above,  ‘email verification’ flow will be skipped in UI and Volt to pass the following info to DSP BE in the ‘loan contract’ api
    - ‘SMS’ as the primary communication channel  for the user
    - Timestamp and IP address of the consent provided
    - Captured ‘email id’
- On receiving this info, DSP to set ‘email verification status’ as ‘unverified’ for the user &  trigger all LOS/LMS communications to the user going forward through ‘S**MS ‘** only(‘containing DSP web app links  for viewing relevant document wherever applicable)
    - See ‘section.2’ for the complete list of LOS/LMS communications to be handled  and their respective templates
    - ~~Note: Here since the confidential loan documents will be triggered to an unverified email, the docs will be password protected to restrict unauthorised access~~
- If user doesn’t check the above box, Volt to continue with the current flow of capturing email id as well as verifying them via OTP and pass the following info to DSP BE in the ‘loan contract’ api
    - ‘Email’ as the primary communication channel for the user
    - Captured ‘email id’ to be passed  along with the verification logs
- On receiving this info, DSP to set ‘email verification status’ as ‘verified’ for the user &  trigger all LOS/LMS communications to the user going forward through **both ‘Email’ &  ‘SMS ‘**(containing DSP web app links  for viewing relevant document wherever applicable)
    - See ‘section.2’ for the complete list of LOS/LMS communication templates for email  & SMS

B) LSPs

- Here LSPs will capture the primary communication mode choice (SMS/Email) and  the ‘email id’ in their own UI and pass these details along with consent (of primary mode) timestamp& IP  to DSP first. Based on these shared details,
    - In case ‘email’ is chosen as the primary communication mode, LSPs will also need to pass the ‘email verification log’ utility ID in the ‘loan contract’ stage
    - In case ‘sms’ is chosen as the primary communication mode, ‘email verification log utility ID in the ‘loan contract’ api will be optional
        - Note: In this case, if email log
        
        Note: In both cases, email ID needs to be captured mandatorily (either via ‘Create opportunity or ‘Update opportunity)
        
- Based on the info receiving above, DSP to set  the primary mode to either ‘SMS/Email’ ‘, update ‘email verification status’ (verified or unverified) and trigger LOS/LMS communication channel to either ‘SMS’ (in case SMS chosen as primary mode) and both  ‘Email’ & ‘SMS’ in case ‘email’ is chosen as the primary mode
    - See ‘section.2’ for the complete list of LOS/LMS communication templates for email  & SMS

Section 2: LOS Communication trigger (SMS / Email)

Following are the list of LOS communications that needs to be triggered to users:

1. Welcome docs:
    
    Email template : Same as current
    
    SMS template
    
    - Body:
        
        Congratulations {{name}}! Your Loan Against Securities account with DSP Finance is now active.
        
        Client ID: {{client_id}}
        Loan A/c No.: {{loan_account_number}}
        Credit Limit: ₹{{credit_limit}}
        
        Your welcome letter (KFS, and signed agreement) are available here: {{documents_link}}
        
        For support: 022-414-84529 | [support@dspfin.com](mailto:support@dspfin.com)
        
    - Variable Definitions
        - **{{name}}** — Customer’s name
        - **{{client_id}}** — DSP Client ID
        - **{{loan_account_number}}** — DSP Loan Account Number
        - **{{credit_limit}}** — Sanctioned credit limit
        - **{{documents_link}}** — Link to DSP’s web app where all files can be downloaded
    - Template ID
        - 
    

2.KFS

Email template : Same as current

SMS template

- Body:
    
    Hi {{name}},  we’ve received and recorded your acceptance of the KFS for your LAMF application (Ref: {{opportunity_id}}  with DSP Finance at  {{ack_timestamp}}.
    
    You can view/download your KFS here: {{kfs_link}}
    
    For help: 022-414-84529 | [support@dspfin.com](mailto:support@dspfin.com)
    
- Variable Definitions
    - **{{name}}** — Customer’s name
    - {opportunity_id}} - Opp ID
    - {{ack_timestamp}} - Timestamp of KFS acknowledgement
    - {{kfs_link}} - Link to DSP’s web app where KFS can be downloaded
- Template ID
    - 

3.’Opportunity creation email

Email template : Same as current

SMS template

- Body:
    
    Hi {{name}}, we’ve received your Loan Against Mutual Funds application (Ref: {{opportunity_id}}) on {{application_timestamp}}.
    
    Our team will review it and keep you updated.
    
    For help: 022-414-84529 | [support@dspfin.com](mailto:support@dspfin.com)
    
- Variable Definitions
    - {{name}}	- Customer’s name
    - {{opportunity_id}} - Opp ID
    - {{application_timestamp}}- Timestamp when the application was received
- Template ID
    - 

Section 3: Nudges for email verification  post loan a/c creation

For cases where ‘SMS’ was chosen as the primary communication mode, DSP will trigger nudges (post successful loan a/c creation)to captured (un-verified) emails of the user prompting them to verify their email. 

The nudge email will carry a verification link which on clicking will auto verify that email id and the ‘email verification status’ will get updated to ’verified’ in DSP BE.The expiry of this email will be 30 days

Attached below is the ‘email verification’ nudge template:

Subject: **“Verify Your Email to Receive Important Loan Updates”**

Body:

Hi,

To ensure you continue receiving important updates and statements for your Loan against Mutual Funds account, please verify your email by clicking {{verificationLink}}

Regards,

Team DSP

---

**Variables:**

- **date:** {{triggerDate}}
- **verificationLink:** {{email_verification_link}}
- **supportEmail:** support@dspfin.com
- **phone:** 022-414-84529

---

**Template ID:**

- d-2ac0956492cf49ae98b3b4d62ecb3c67

Nudge framework:

Nudge Trigger

- **Event:** Successful loan account creation
- **Condition:** `primary_comm_channel = SMS` and `email_status = unverified`
- **Action:** Start nudge sequence until verification OR stop condition is met.

Nudge Cadence

**WEEK 1**

- Nudge 1 — Immediate (T = 0 hours) ie Triggered right after loan a/c creation
- Nudge 2 — Day 4

WEEK 2

- Nudge 3 — Day 11

WEEK 3&4

- Nudge 4 — Week 3 (Day 18)
- Nudge 5 — Week 4 (Day 25)

Next 3 months

- Nudges 6, 7, 8 — Monthly (1 per month) on 1st

Section 4: Command centre changes

With this new feature, there will be a new subsection under ‘Verification logs’ tab  in ‘Loan approval’ task  called “Communication mode” under which we will have  an **additional parameter of “***Primary Communication Mode”*

- **If the user selects ‘SMS’ as the primary communication mode:**
    - **‘Primary Communication Mode’ field will carry ‘SMS’**
    - **Verified Status** and **Customer IP** fields under Email Verification becomes optional, since email verification is not required
- **If the user selects Email as the primary communication mode:**
    - **‘Primary Communication Mode’ field will carry ‘Email’**
    - **Verified Status** and **Customer IP** must continue to be **mandatory**, as per current behaviour.

If the user completes email verification later through DSP’s post-creation nudges, then the ‘Verified Status’ and ‘Customer IP’ fields under the ‘Email Verification’ section must be updated with the corresponding verification details

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