# DSP Consent Architecture (Oct25)

Last Edited: January 8, 2026 7:41 PM
PRD ETA: October 31, 2025
PRD Owner: Gautam Mahesh
Status: In progress

# **What problem are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

# **How do we measure success?**

Below is the success criteria.

- DSP is compliant with DPDP act and DLG from a consent framework perspective.
- DSP is able to capture the required customer consents as per DPDP and DLG.
- Customers should be able to revoke their consents as per DPDP.
- DSP is able to track the consents to be managed at a customer and version level.

---

# **How are others solving this problem?**

Below are the approaches taken by lenders in the industry.

- Consent framework: this is where new-age players design a detailed consent architecture across consent types
- Consent storage: this is where companies store all consents at an application level with basic versioning.

Most players are moving towards approach 1 due to upcoming DPDP guidelines.

Players to benchmark.

- BFL
- TCL
- Hero Fincorp

---

# **What is the solution?**

## Customer Journey

Below will be the end to end customer journey.

- The customer starts the journey on the LSP asset (web/app).
- The customer consents to the terms and conditions as a checkbox that incorporates the below items in the verbiage of DSP.
    - Privacy Policy of LSP
    - Privacy policy of DSP
    - T&C of DSP
    - Sharing data with 3P
    - The above documents will have the below items in scope. The LSP has the option to ask the customer to consent on all these points upfront or take consent at each stage.
        - Regulatory reporting
        - Promotional communication
        - Storage of data
        - SMS alerts & communication
        - Consent to download CKYC
        - Bureau pull
        - Camera access
        - Location access (when required in the future)
        - NRI confirmation
        - Any other conditions (Age > 18, Valid OVD, etc)
    - The LSP shares the customer acceptance consent of DSP of each item as separate item.
    - Only LSP privacy policy acceptance timestamp needs to be stored at DSP’s end.
- The customer verifies the mobile number if not done.
    - The LSP shares the timestamp of mobile verification with DSP via API.
    - This continues as it is and no change is required.
- The customer fetches the funds through RTAs or MFC and receives an offer.
    - No consent is required at this stage.
    - LSP needs to have text that explains to the customer that DSP will use the funds fetched will be used to generate an offer.
- The customer proceeds to the KYC step.
    - If the customer undertakes the journey through CKYC, the LSP takes explicit consent to download CKYC.
    - The LSP passes the consent details to DSP for CKYC if the consent isn’t incorporated at the start of the journey.
    - If the customer undertakes the journey through Digilocker, no additional consent is required as its taken on Digio and Digilocker pages.
- The customer undertakes a live photograph.
    - If the LSP has consent to access camera before the DSP LAMF journey starts, the consent details is passed to DSP either at the start of the journey OR
    - If the LSP takes consent through web/app (device) controls at this step, the same can be a proxy for consent.
    - The LSP passes the consent details to DSP.
- The customer completes the additional details page.
    - The customer explicitly consents to their permanent address = current address on the LSP UI.
    - The LSP passes the consent details to DSP for current address.
    - If the LSP has taken the consent from the customer not being an NRI at the start of the journey, the LSP can pass that timestamp to DSP OR
    - If the LSP takes consent on this page separately or with NRI, the LSP can pass that timestamp to DSP.
- The customer provides consent to receiving communication via SMS and/or Email.
    - If the customer wants an email based communication, no consent is required to be taken. The LSP only passes the email verification log to DSP.
    - If the customer wants an SMS based communication only and the LSP hasn’t taken any consent at the start of the journey, the LSP has to take an explicit consent.
    - If the customer wants an SMS based communication only and the LSP has taken  consent at the start of the journey, the LSP doesn’t have to take an explicit consent.
    - The LSP can pass the SMS consent details to DSP.
- The customer is redirected to the pledge step.
    - No consent is required at this stage if the LSP using its own APIs (CRED) or using wrapper APIs.
    - LSP needs to have text that explains to the customer that DSP will lien mark the funds in its favor.
- The customer is redirected to the mandate step.
    - No consent is required at this stage if the LSP using its own APIs (CRED, Smallcase) or using wrapper APIs.
    - LSP needs to have text that explains to the customer that DSP will setup a recurring debit to process towards EMIs/interest dues.
- The customer is redirected to the KFS step.
    - If the LSP is using the redirection link of DSP, DSP takes the required consent on its UI. The LSP doesn’t need to pass any consent to DSP.
    - If the LSP is using the PDF flow of DSP, the LSP takes the required consent on its UI. The LSP needs to pass this consent to DSP.
- The customer is redirected to the Agreement step.
    - If the LSP is using the redirection link of DSP, DSP takes the required consent on its UI. The LSP doesn’t need to pass any consent to DSP.
    - If the LSP is using the PDF flow of DSP, the LSP takes the required consent on its UI. The LSP needs to pass this consent to DSP.

Below is tabular format of when all the consents can be captured.

| **Consent Type** | **Journey Stage** | **Consent** |
| --- | --- | --- |
| Privacy Policy of LSP | Start of the Journey | Yes |
| Privacy Policy and Terms & Conditions of DSP | - Start of the Journey OR 
- Selection of DSP as Lender OR 
(T&C’s may be removed post discussion or finalization with Legal) | Yes |
| Sharing data with Third parties | - Start of the Journey or 
- On selection of DSP as Lender | Yes |
| CKYC Consent for downloading KYC records from CKYC registry | - Start of the Journey OR 
- Fetch stage or 
- KYC stage | Yes |
| Digilocker Consent for fetching KYC records from Digilocker | Digilocker page | Yes |
| Camera Consent – Photo | - Pre-captured by LSP OR 
- Google/Apple prompts audit trail on the Image capturing screen | Yes |
| Current Address confirmation | - KYC stage OR
- Additional details page | Yes |
| Consent – Indian resident | - Start of the journey (if captured in T&C’s)OR
- The final application stage (where all the details are captured) | Yes |
| Email-id Validation or receiving comms. on mobile number | - At the email id verification stage OR
- The final application stage | Yes |
| Bureau Fetch consent | - Start of the journey OR 
- Any pre-bureau page | Yes |
| KFS Acceptance consent | At the KFS stage | Yes |
| Agreement Acceptance consent | At the Agreement stage | Yes |

## Flow : Consent  Capture

### Journey Start

Below is how the consent would be captured for multiple consents that are captured in DSP T&Cs, privacy policy and LSP privacy policy.

- LSP initiates DSP flow by initiating APIs or fetching funds on their UI.
- Customer consent to be captured by LSP on the LSP T&Cs and privacy policy.
    - This will be passed by the LSP to DSP via API
- Customer consent to be captured by LSP on the LSP T&Cs and privacy policy.
    - This will be passed by the LSP to DSP via API
- The scope of consents being captured will be one or more.
    - 3P data sharing
    - Regulatory reporting
    - Promotional communication
    - Storage of data
    - SMS alerts & communication
    - Consent to download CKYC
    - Bureau pull
    - Camera access
    - Location access (when required in the future)
    - NRI confirmation
    - Any other conditions (Age > 18, Valid OVD, etc)
- The LSP can choose the pass the consent timestamp immediately or later in the journey.

### Camera Access

Below is how the consent would be captured for camera access.

- LSP initiates DSP liveliness check by initiating APIs.
- LSP can leverage the device prompts as explicit consent for access OR
    - This will be passed by the LSP to DSP via API
- LSP can leverage any other consent taken as part of generic onboarding.
    - This will be passed by the LSP to DSP via API

Validation.

- Consent timestamp has to be passed before KYC initiation is called

### KYC Processing

Below is how the consent would be captured for the KYC step.

- LSP initiates KYC flow by initiating KYC APIs.
- Customer consent to be captured by LSP only for CKYC flow.
    - This will be passed by the LSP to DSP via API
- Digilocker captures customer consent on behalf of the customer on their UI.
    - DSP will consider this timestamp for consent

Validation.

- KYC consent timestamp has to be passed before Submit Opportunity is called

### SMS Alerts

Below is how the consent would be captured for the SMS alerts.

- Customer completes fetching of funds.
- Customer consent to be captured by LSP to receive only SMS alerts if email isn’t verified.
    - This will be passed by the LSP to DSP via API

Validation.

- Consent timestamp has to be passed before Submit Opportunity is called

### Citizenship Declaration

Below is how the consent for citizenship declaration (not an NRI) will be captured.

- LSP initiates the additional details step.
- Customer completes the additional details.
- Customer consents to the declaration that he/she is an Indian citizen through a checkbox if the LSP hasn’t captured this at the onboarding stage.
    - LSP passes this consent timestamp to DSP.

Validation.

- Consent timestamp has to be passed before Submit Opportunity is called

### Address Declaration

Below is how the consent for current address declaration will be captured.

- LSP initiates the additional details step.
- Customer completes the additional details.
- Customer consents to the declaration that current address is the same as current address through an explicit consent (checkbox).
    - LSP passes this consent timestamp to DSP.

Validation.

- Consent timestamp has to be passed before Submit Opportunity is called

### Credit Bureau

Below is how the consent for credit bureau pull will be captured.

- LSP can choose to inform the customer about credit bureau pull at any stage once DSP is assigned as the lending partner including at the onboarding stage.
- Customer consents to their credit report being pulled.
    - LSP passes this timestamp to DSP for consent.

Validation.

- Consent timestamp has to be passed before Submit Opportunity is called

### KFS Acceptance

Below is how the consent for KFS acceptance will be captured.

- LSP initiates the KFS step via APIs
- Customer accepts the KFS PDF on LSP UI.
    - LSP passes this consent timestamp to DSP.
- Customer accepts the KFS on DSP UI.
    - The timestamp when the customer has accepted the KFS needs to be stored.

Validation.

- Consent timestamp has to be passed before Submit Opportunity is called for PDF based flows.
- Consent timestamp has to be before the agreement acceptance timestamp.

### Agreement Acceptance

Below is how the consent for agreement acceptance will be captured.

- LSP initiates the Agreement step via APIs
- Customer accepts the KFS PDF on LSP UI.
    - LSP passes this consent timestamp to DSP.
- Customer accepts the KFS on DSP UI.
    - The timestamp when the customer has accepted the KFS needs to be stored.

Validation.

- Consent timestamp has to be passed before Submit Opportunity is called for PDF based flows.
- Consent timestamp has to be after the KFS acceptance timestamp.

## Flow : Consent Revocation

Below is the user flow for consent revocation for a customer.

- The customer reaches out to DSP directly or through an LSP to delete data and its consent.
- The LSP hits DSP’s APIs or the operations team accesses the command center.
- DSP checks if a customer is an active customer or not.
- Basis the consent type and the relationship with DSP, we delete the consent and data.
- Operations team will use the command center to delete the consent and data.
- Application has to be suspended - this approach is from a simplicity perspective.
    - This will result in a scenario that a customer will have to redo the application in case of opportunity suspension.
- Data associated with the consent cannot be used.

| **Consent Required** | **Revokable (Active Loan)** | **Revokable (Application)** |
| --- | --- | --- |
| Sharing of data with 3rd parties | No | No |
| Consent for collection, storage, and use of KYC documents (CKYC) | No | Yes |
| Consent to confirm borrower is not NRI | No | No |
| Consent to confirm present and permanent address so as to not carry out specific KYC for amended address | No | Yes |
| Consent for accessing credit report | No | Yes |
| Consent for storage/destruction of personal/financial data | No | Yes |
| KFS acceptance | No | Yes. |
| Consent for communication via SMS | Yes | Yes |
| Consent for promotional communication | Yes | Yes |
| Consent for reporting under STR/CTR/Fraud reporting | No | No |
| Agreement acceptance | No | No |

## Requirements Overview

### Customer Level

DSP will have to capture the below consents from customers (applicants).

- **Consent ENUM**: this will the consent version ID that will be provided by the customer.
- **Consent name**: this will be name of the consent. Eg - KYC Processing, e-KYC.
- **Consent capture timestamp**: this will be the timestamp when the consent was accepted by the customer. This could be through Volt or any other LSP
- **Consent status**: this will be the status of the current consent at a consent and customer level. This can have one of the below values.
    - **Active**: this is the scenario where the customer consent
    - **Revoked**: this is the scenario where the customer hasn’t revoked the consent provided earlier.
    - **Expired**: this is the scenario where the consent has expired because its past the timeframe.
- **Consent revocation timestamp**: this will be the timestamp when the consent was revoked by the customer. This could be through Volt or any other LSP.
- **Consent version**: this will be the version of the consent that the customer has provided consent to.
- **Consent channel**: this will be the channel through which the consent has been captured or revoked by the customer.
- **Consent end timestamp**: this will be the timestamp when the customer revoked the consent explicitly or when the consent expired automatically.

All consents will be captured by LSPs including Volt in one of the 2 forms.

- **Policies**: This will be a page like T&C which will be referenced during the journey. DSP will maintain any verbiage changes to each policy.
- **Journey**: This will be a journey text that the customer can see before consenting to the terms. This will be captured on the UI.

### Consent Level

Each consent will have the below attributes that is mapped to a consent ID.

- **Consent ID**: A unique identifier to identify the consent.
    - Each ID will be used to identify a unique consent like CKYC, CIC, SMS, etc.
    - Each ID can have multiple versions due to journey variants.
- **Consent name**: this will be name of the consent. Eg - KYC Processing, e-KYC. This will be a more descriptive version of the consent ID.
- **Consent version**: this will be the version of the consent that the customer has provided consent to.
    - Language changes to consent will result in a new version.
    - We will have multiple versions at any time for the same to support backward compatibility for LSPs to make changes.
    - Each version will have its own version ID.
- **Consent text**: this will be the actual consent text that the customer has provided consent to.
    - There can be multiple variations of the text depending on the product, variants and even LSPs
    - Text needs to be maintained at the version.
- **Consent timeperiod**: this will be the time period for which a consent will be captured by DSP.
    - This will be defined by DSP at a consent level.
    - LSP will not pass this to DSP.
- **Consent capture type**: this will have to be the type of consent captured.
    - Explicit
    - Implicit

DSP will have to maintain the consent list at the below level to uniquely identify consent granted or revoked.

- **Opportunity**: each consent and its attributes will need to be mapped to an opportunity at DSP’s end.
- **LSP**: each consent and its attributes will need to be mapped to the LSP who’s taking consent from the customer.

## LSP Flow

### Pre-Requisites

DSP team shares the list of consents with the points of capture with the LSP or B2B partners.

- Partner adds the consent verbiage or a variant in their journey.
- Partner embeds the consents at different touchpoints of the journey.
- Partner integrates to pass the consent timestamps to DSP.

### Consent Capture

Below is the user journey for capturing consent.

- The customer starts the journey on the partner UI.
- The partner captures the required consent from the customer.
- The partner creates an opportunity with DSP.
- The partner passes the required consent details to DSP.
    - Opportunity ID
    - Consent type (CKYC, CIC, etc)
    - Consent timestamp
    - Consent channel (UI/SMS/WA/Email)
- DSP maps the consent provided from its partners as per its template.
    - Consent period
    - Consent start time
    - Consent end time
    - Consent version
- Partner passes the consent details via APIs before submitting an opportunity.
- DSP validates the consents at the time of opportunity submission.
- DSP puts account opening on hold in case of insufficient consents being passed.

### Consent Revocation

Below is the user journey for revoking consent.

- The customer reaches out to DSP or partner for closing an application or dropping off.
- DSP captures the revocation timestamp at its end and closes the application/loan.
- If the customer asks for a specific consent to be revoked, the partner captures the consent request and passes it to DSP.
- DSP validates if the consent can be revoked and responds to the partner.
- DSP marks the consent as ‘Revoked’ with the timestamp or rejects the request.
- DSP will not delete the data even if the consent is revoked for active loans.

## Command Center

Below are the requirements that need to be made available on CC.

- Ability to see the consents captured at an opportunity level.
- Ability to see the consents captured at a loan level.
- Ability to initiate consent revocation at an opportunity level.
- Ability to initiate consent revocation at an application level.

## Integration

### Integration Approach

Below are the integration approaches.

- **Consolidated**: LSPs share the consent timestamps in a single API call that covers all the consents. This will be before the opportunity is submitted to DSP.
- **Individual**: LSPs share the consent timestamps for each consent through individual API calls. This will be after each step is called.

Individual APIs provide the flexibility for the LSP to build their own journey and pass the consent at each stage. This also allows DSP to validate each consent and avoids post-facto audit challenges. It also avoids a very large API call at the submit opportunity where already a lot of processing happens at DSP’s end.

Consolidated API provides the flexibility for the LSP to complete the journey and pass all consents in a single shot to DSP. This has the flip-side of not able to validate consents and will result in a bad customer experience in case of any validations failing. It also adds additional processing at the submit opportunity stage.

<aside>
💡

More details to be added post solutioning with tech

</aside>

### LSP Integration

DSP needs to provide LSPs the below capabilities.

- Ability to pass the consent acceptance details to DSP at an opportunity or loan level.
    - Consent type
    - Consent acceptance timestamp
    - Consent acceptance channel
- Ability to pass the consent revocation request to DSP at an opportunity or loan level.
    - Consent type
    - Consent revocation timestamp
    - Consent revocation channel
- DSP needs to inform the partner in case a request is accepted or rejected.
- DSP will inform the LSP in case of customer consent revocation offline for now.

## Consent List

[Here](https://docs.google.com/spreadsheets/d/1aHVJR7Zrhjqk-ynrQW1yULSRZjCTerJNNWsbfo_xdXo/edit?usp=sharing) is the list of consents to be captured and its status. The list needs to be finalized post discussion with compliance.

---

# **Analytics**

Below are the metrics that will be tracked.

- Number of consents captured at customer/partner level.
- Number of consents revoked at customer/partner level.
- Number of consents inactive at customer/partner level.
- Number of consents not given at customer/partner level.

---

# **Timeline/Release Planning**

Below are the milestones that are part of this PRD.

| **Item** | **Description** | **Status** |
| --- | --- | --- |
| Consent List | Finalize the list of consents that needs to be captured by LSPs in the journey or in T&C | In Progress |
| Language Changes | Finalize the list of consents that need language changes | In Progress |
| Partner Intimation | Intimate partners (LSPs) about the consent changes across journey and T&Cs | Not Started |
| Partner Solutioning | Solution any consent changes basis the variations in integrations | In Progress |
| Dev Closure | Development closure for APIs to be made ready for partner consumption | Not Started |
| Volt Launch | Make consent changes and API integration across Volt channels before LSP launch | Not Started |
| LSP Launch v1 | Launch with LSPs who are on a standard integration format (Groww, ETMoney, Indmoney, Smallcase) | Not Started |
| LSP Launch v2 | Launch with LSPs who are on a bespoke integration format (PhonePe, PayTm, CRED) | Not Started |

---

# **Go to market**

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [x]  Take PRD sign-off from Compliance
    - [ ]  Inform LSPs about changes
    - [ ]  Prepare 1 pager for LSPs
    - [ ]  Train Ops once the feature is developed
- [ ]  Business
    - [ ]  Align LSPs about consent capture
- [ ]  Tech
    - [ ]  PRD walkthrough with tech
    - [ ]  PRD kick-off with tech

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