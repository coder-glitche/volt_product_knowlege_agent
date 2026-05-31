# Email Validation Approach: PhonePe

: Priyamvada S
Created time: July 17, 2025 9:46 AM
Status: Not started
Last edited: October 22, 2025 1:32 PM

# **What problem are we solving?**

PhonePe captures user email IDs without verification, posing compliance and communication risks. To avoid delaying go-live, an interim solution is needed to ensure basic email validity without enforcing strict verification.

---

# **How do we measure success?**

NA

---

# **How are others solving this problem?**

NA

---

# **What is the solution?**

- **Phase 1 (pre-Sept 30):** Use email delivery status as a proxy for verification. Undelivered cases follow a manual Ops-led validation via alternate email + OTP or fallback checks.
- **Phase 2 (post-Sept 30):** PhonePe to implement OTP-based or other standard email verification mechanisms within their frontend journey.

## **User Flow (Detailed)**

### **1. Email Capture & Trigger**

- **User enters email ID (E1)** on the PhonePe pre-KYC screen.
- **E1 is shared with DSP via Submit opportunity API (**Email logs are not shared as its optional)
    - DSP triggers email to E1 and monitors delivery status
        - Template:
            - Subject: Congratulations on Starting Your Loan Application !
            - Body:
                
                Hi,
                
                Thank you for initiating your Loan Against Mutual Funds (LAMF) application with DSP via PhonePe.
                
                Regards,
                
                Team DSP
                
            - Variables
                - date: {Trigger date}
                - ~~Phone: 022-414-84529~~
                - supportEmail: support@dspfin.com
        - Template ID: d-2e4f9bad098b49ecb4b4672569fc5748
- Opportunity gets submitted by LSP & ‘submit opportunity’ workflow is initiated
- In the workflow, a check is introduced for ‘email delivery’ status
    - If email delivery is success (ie status= Clicked/Delivered/Open), workflow continues
    - If email delivery ‘failed/delayed’ (ie status= Blocked/Bounced/Failed/Marked spam/Sent/Triggered), system triggers 2 emails concurrently as described below
    
     b)A email is triggered to user’s captured mail ID ‘E1’
    
    - Subject: “Urgent: Verify Your Email to Continue Your Loan Application”
    - Body
        
        Hi,
        
        Thank you for starting your Loan against Mutual Fund application with us.
        
        To proceed further, please verify your email address by clicking {verificationLink}
        
        This link will be valid for the next 48 hours.
        
        Regards,
        
        Team DSP
        
    - Variables
        - date: {Trigger date}
        - verificationLink: Email verification link
        - ~~Phone: 022-414-84529~~
        - supportEmail: support@dspfin.com
    - Template iD:  d-9bc1b36bde1d4db79c9c25b71c8d3ea7
    
    a)A second email is triggered to  ‘support@dspfin.com’  
    
    - Subject: “Email delivery failed”
    - Body: Email delivery failed for the following user:
        - Opportunity ID
        - Customer name
        - Email id
        - Mob no
    - Variables:
        - date
        - opportunityId
        - customerName
        - emailId
        - mobileNo
        - supportEmail
    - Template ID: d-d1c36e69addb44068064c39d6509b2d9
    - Above email auto creates a Zoho ticket with the above captured fields
    - Agent then triggers a call to the user  using the captured mobile number

### **2. Support agent Intervention & Verification tracking**

A)Agent outreach: User has access to E1

- Agent confirms email id E1 with customer
- On user confirmation , agent guides user to check the email received from ‘dspfin’ and click on the verification link.

System tracking & handling 

- Once the system receives a **successful email verification response**, it:
    - Marks the email ID (E1) as verified
    - Captures the **verification timestamp**
    - Unblocks the **opportunity submission workflow**
- If the email is not verified within ~~30 days of~~ the verification link being generated, the link expires

A~~gent tracking & ticket closure~~

- ~~Agent tracks the status of ‘email verification’ by looking up the opportunity ID’ in ‘CC dashboard’ and checking the ‘email verification’ field status to close the ticket~~
    - ~~If successfully verified, agent marks the ticket as ‘closed’~~
    - ~~If verification failed (eg: link expiry after 48 hours), agent marks the ticket as ‘closed’ with remarks “email unverified”~~

B)Agent outreach:  **User does NOT have access to E1 or is not receiving emails  from DSP**

- Agent ask  for an alternate email id (while on call)
    - In this case, we need a maker/checker flow as original email is getting updated
- **If user does not have an alternate email ID (Out of Scope for initial release)**
    - ~~Agent instructs user to **send an email from E1** to a specified DSP email ID (TBD)~~
    - ~~On receiving email from E1, a support ticket is auto-created in Command Centre~~
    - ~~Ticket is processed manually for validation~~
- **If user provides alternate email ID (E2)**
    - Agent clicks **‘Update Email’** in UI
        - Replaces E1 with E2 in the email field
        - On updating, **‘Approve’ CTA is disabled**
        - Only **‘Reject’** or **‘Move to Checker’** options are available now
    - Agent clicks **‘Trigger Link’** → Verification link is sent to E2
    - Agent guides user to verify using that link
    - **If user clicks verification link instantly:**
        - System updates:
            - Email delivery/verification status → **Verified**
            - Email delivery/verification timestamp → **current time**
        - On successful verification, agent ends the cal & logs the Zoho ticket number in the dashboard; this ticket includes the call recording.
        - Agent clicks **‘Move to Checker’** CTA
            - Request is escalated to internal Ops agent for checker verification/approval
    - **If user doesn’t verify instantly**
        - User has up to **48 hours** before link expiry
        - If not verified within 48 hrs (indicated by ‘verification link’ status field), agent clicks **‘Reject’**CTA → Opportunity is rejected, user cannot proceed further

**Note**: If the user forwards the verification link from E2 to E3 and verifies via E3, it will still be accepted. DSP will not enforce checks on this; user bears responsibility.

 **Command Centre Ticket Auto-Creation**

- **A ticket gets auto-created in DSP Command Centre with following details**
    - Task type: *“Email validation approval”*
    - Opportunity ID
    - Task ID
    - Customer name
    - Checker name
    - Created on
    - ‘Review’ CTA
        - On clicking review, page opens up with the following details:
            - Email id
            - Email delivery/verification status: Failed
            - Email delivery/Verification Timestamp:
            - Name
            - Mob
            - PAN
            - Opportunity ID
            - Zoho ticket no
            - Verification link status: Expired/Active
            - CTAs:
                - Approve/Reject/Move to checker
                - Trigger link
                - Update email id (this CTA comes against the ‘email id’ field)

**Support Agent  Workflow**

- Agent clicks **‘Review’** CTA and  views detailed customer information
- Agent creates a Zoho ticket and triggers a call to the user  using the captured mobile number
    - Zoho ticket creation is required to ensure  the call recording is captured for later review

- **Final Approval – Checker** [Applicable only in cases where user updates their mail id to E2]
    - Checker (internal Ops agent) receives the **email validation request** in the Command Centre.
    - Opens corresponding **Zoho ticket &  reviews the c**all recording
    - Ops agent will then either reject or approve it by hitting ‘Reject’ or ‘Approve’ CTA resp.
        - If approved, the opportunity workflow resumes with the rest of the steps
        - If rejected, the opportunity is rejected and user can’t move ahead with account creation

### **5. Post-Validation Sync with PhonePe**

- **If email ID was updated from E1 → E2**, then:
    - DSP Ops team compiles a **daily offline file, which is s**hared with PhonePe to support **backend email ID updates** at their end

## Requirements

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