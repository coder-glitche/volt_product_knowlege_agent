# KYC & Mandate Workflow PRD

: Nihal Simha M S
Created time: November 27, 2024 4:20 PM
Status: Done
Last edited: April 14, 2025 7:17 PM

# **What problem are we solving?**

1. LSPs currently need to integrate with third-party SDKs to complete the KYC and mandate steps. Integrating two separate SDKs is cumbersome, fails to establish a high standard for DSP, and raises compliance concerns when DSP credentials are shared with LSPs for SDK invocation.
2. Alternatively, LSPs can initiate the Digilocker/mandate step via a web URL, which opens in a web view belonging to a third-party provider. DSP has no control over the session, screens, or analytics on what step user dropped.
3. The go-live TAT for LSPs increases due to third-party SDK integrations, multiple API integrations for steps like KYC, photo verification, and additional data, along with building the UI and handling various cases.
4. As a regulated entity, the Digital Service Provider (DSP) currently lacks complete control over user-submitted data (e.g., photos, additional details) and the associated screens. This compromises compliance, data accuracy, and the ability to deliver a seamless and secure user experience.

---

# **How do we measure success?**

1. **Application Drop-Off Rate**: Percentage of users who drop off at each step.
2. **Selfie Step Completion Rate**: Percentage of users who successfully complete the selfie step.
3. **Session Duration**: Time spent on the application(KYC journey & Mandate journey) by users.
4. **Retry Attempts**: Number of retries per step (e.g., failed selfie attempts, digilocker, mandates).
5. **Successful Mandate Registration:** Percentage of users who successfully complete the mandate step.

---

# **How are others solving this problem?**

1. Some NBFCs bundle KYC, selfie, and other verification processes into a single integration, managed through a redirection journey. However, these platforms often lack flexibility and do not provide end-to-end control over screens and the user journey.
2. Others offer individual SDKs to LSPs to manage multiple verification processes separately, providing a native experience. However, using multiple SDKs increases application size and might affect user experience.
3. Similarly, some NBFCs provide standalone APIs, allowing LSPs to build their own UI and retain full control over the screens and user journey.

---

# **What is the solution?**

We are introducing fully customizable, DSP-managed user screens to deliver a seamless, compliant, and consistent user experience. These screens will allow LSPs to customize themes and branding to align with their specific requirements.

This solution eliminates the reliance on third-party SDKs, reduces integration complexity, and accelerates the go-live process.

Additionally, LSPs can enable or disable specific modules, or manage them independently through backend APIs:

1. **KYC Module**:
    - Mandatory for all LSPs and cannot be skipped or disabled.
2. **Photo Verification**:
    - Optional module; LSPs can choose to disable it and handle verification via backend APIs.
3. **Additional Data Collection**:
    - Optional module; LSPs can disable it and manage the data collection process independently using backend APIs.

## User stories / User flow

1. The user initiates the LAMF journey from the LSP application.
2. The user fetches mutual funds from RTAs and sets a credit limit on LSP-managed screens.
3. The user completes the KYC, photo verification, and additional data steps on DSP-managed screens via the web.
4. After completing the KYC step, the user verifies their bank account on LSP-managed screens.
5. Once the account is verified, the LSP initiates DSP screens via a web URL for the user to complete the mandate setup.
6. The user pledges their funds through LSP-managed screens.
7. The user accepts the KFS and signs the agreement via DSP screens initiated through a web URL.
8. A loan account is created at DSP upon completion.

## Requirements

1. KYC Session Initiation API
2. GET KYC Status API
3. Callbacks

1. KYC Session Initiation API
    1. **Mandatory Parameters**:
        1. Opportunity ID
        2. Redirection URL
    2. **Optional Parameters**:
        1. Employment status
        2. Income range
        3. End-use
        4. Marital status
        5. Mother’s name
        6. Father’s name
    3. **WebUrl Usage**:
        1. The session will be initiated at DSP using the provided webUrl.
    4. **Additional Data Handling**:
        1. If LSPs provide optional parameters, corresponding input fields will not appear on the additional data collection screen or will be prefilled.
        2. DSP will only request missing details from the user.
    5. **Unified WebUrl Functionality**:
    
              This API enables the completion of three steps in a single flow:
    
    1. Digilocker KYC
    2. Additional Data Collection
    3. Selfie (Photo Verification)
    
    Request Body
    
    ```json
    {
        "opportunityId":"{{opportunityId}}",
        "redirectionUrl": "https://www.voltmoney.in",
        "additionalData": {
            "endUse": "",
            "qualification": "",
            "incomeRange": "",
            "maritalStatus": "",
            "mothersFirstName": "",
            "mothersMiddleName": "",
            "mothersLastName": "",
            "fathersFirstName": "",
            "fathersMiddleName": "",
            "fathersLastName": "",
            "employmentStatus": "",
        }
    }
    ```
    
    Response Body
    
    ```json
    {
        "opportunityId": "OPP9726566149",
        "fenixLoanAccountId": null,
        "utilityReferenceId": "URKYC5344634384",
        "status": "IN_PROGRESS",
        "subStatus": "VALIDATION_PENDING",
        "webUrl": "https://www.voltmoney.in/KYC"
    }
    ```
    
    1. GET KYC Status API
        1. Request Body. —> Utility reference ID
        2. Response Body
        
        ```json
        {
          "opportunityId": "OPP3297739554",
          "fenixLoanAccountId": null,
          "utilityReferenceId": "URKYC6417594683",
          "stage": "Digilocker/ Additional Data/ Selfie",
          "status": "APPROVED",
          "subStatus": "VALIDATION_SUCCESSFUL"
        }
        ```
        
    2. Callbacks
        1. In callbacks, we need to have -
            1. Stage- Digilocker/ Additional Data/ Selfie
            2. Status- Status of the stage.
            3. Sub-status- Status of the stage.
    
2. KYC Wireframes

![image.png](KYC%20&%20Mandate%20Workflow%20PRD/image.png)

1. Digilocker KYC
    1. User lands on the DSP-controlled screen with a progress bar displayed.
    2. DSP invokes Digio’s JS SDK to initiate the session.
    3. User completes the Digilocker journey on the Meripehchan website.
    4. Digio displays success or failure, handing control back to DSP.
    5. User returns to the progress bar screen, with KYC marked as completed, and proceeds to the additional data step.
2. Additional Data
    1. After completing Digilocker KYC, the user lands on the progress bar screen showing KYC as completed.
    2. If optional parameters are sent by LSPs, corresponding fields will be pre-filled or hidden.
    3. Once the user submits the data, the "Save Additional Data" API is invoked.
3. Photo Verification
    1. Next, the user completes photo verification using the existing API or a third-party SDK for passive liveness/face match.
    2. The user grants camera access to take a selfie.
    3. The captured image is converted to base64 and uploaded via the photo verification API.
    4. DSP performs a photo match between the Digilocker Aadhaar photo and the uploaded selfie.
        1. The user cannot proceed to the next step until the photo is approved.

### KYC State Management

| **Step Name/ Stage** | **API Sub-Status** | **Scenario** | **Expectations** |
| --- | --- | --- | --- |
| KYC | Validation_Pending | Every new request, user lands on Digio screen directly. | User lands on the Digio screen. This is the default status & expectations. |
| KYC | Validation_success | Once user completes the KYC, can move to next step | Next step |
| KYC | Validity_expired | User dropped mid-journey & came back to the LSP platform & status is | Re-initiate the KYC step, user needs to start the journey from digilocker. |
| KYC | Internal_failure | Due to technical reasons, DSP have not received the callbacks/ GET API gave some other status. | Re-initiate the KYC step, user needs to start the journey from digilocker. |
| KYC | pan_mismatch | User completed the digilocker journey but pan number given by user & available in digilocker is not matching then | Re-initiate the KYC step, user needs to start the journey from digilocker. |
| KYC | pan_aadhaar_mismatch | User completed the digilocker journey but pan & aadhaar both the data not matching then | Re-initiate the KYC step, user needs to start the journey from digilocker. |
| Selfie | checker_approved | User uploaded the selfie but captured image & aadhaar image is not matching. Deviation flow triggered. User also uploaded one of the document & got approved from checker. | Next step |
| Selfie | checker_rejected | User uploaded the selfie but captured image & aadhaar image is not matching. Deviation flow triggered. User also uploaded one of the document & checker rejected. | Re-initiate the selfie step. |
| Selfie | photo_verification_failed | User captured image & aadhaar image not matching. | Trigger the deviation screens. Where user will select the document type & uploads the doc. Checker will verify it later. |
| Selfie | photo_verification_success | User captured image & aadhaar image is matching. | Next step |
| Additional data | Approved | It is default status & no deviation flow. | Next step |

**Examples-**

1. Dropped-off user
    1. User completed the Digilocker KYC on 10th November & dropped off.
    2. Now, the user came back on 12th November to complete the journey.
    3. The redirection URL will take the user to the 2nd step in the flow. As KYC(1st step) is completed by the user.
2. Deviation- Checker approval required
    1. User will be taken to a separate screen that says “Processing your request”. Terminal screen.
3. LSPs have passed all optional data
    1. In this case, the user will be taken to the screen that shows the address fetched from Aadhaar & 2 required consents. 
    2. Resident of India & current address is same as permanent address.

## Mandate User Flow

![image.png](KYC%20&%20Mandate%20Workflow%20PRD/image%201.png)

**Flow Chart**

This flowchart helps us to understand the mandate flow in detail & also handling of the errors/ failure.

Error Handling Excel Sheet - [Link](https://docs.google.com/spreadsheets/d/1KN3VFNOq2g3P6u4kC8RsrjCZ0PX5ulh4n2pK1EEMmQU/edit?usp=sharing). (Navigate to DSP named sheet)

![image.png](KYC%20&%20Mandate%20Workflow%20PRD/image%202.png)

- **Mandate Initiation by LSPs:**
    - After bank account validation, LSPs can invoke the mandate initiation API with their preferred mandate modes.
    - LSPs can choose to include or exclude eNach, eSign, and Physical mandates in their request array.
- **Business Rule Engine (BRE):**
    - The system will verify the mandate modes specified by the LSPs.
    - Based on the LSP request, the bank name, and the available mandate modes, only applicable options will be enabled, with others disabled.
    - *eNach* will always remain the default and first-preference mode.
    - The operations team can override all mandate modes to *Physical* if necessary.
- **Digio SDK Integration:**
    - Based on the selected mandate mode, Digio’s SDK will be initiated.
- **Loader and SDK Invocation:**
    - The DSP will display a 2-second loader before showing a message while the SDK is being invoked.
- **Handling eNach Failures:**
    - If eNach mandate registration fails, the user will be presented with two options:
        - Reinitiate the journey.
        - Switch to *eSign*.
- **Handling eSign Failures:**
    - If eSign fails, the user will have two options:
        - Reinitiate the journey.
        - Switch to *Physical* mandate.
- **Fallback for eNach Failure Post eSign Attempt: // do not refer to this point.**
    - If eSign fails after attempting eNach, users will have the option to:
        - Reinitiate the journey.
        - Retry with eNach.
- **Post-Mandate Completion:**
    - After completing the mandate, Digio will redirect the user back to the DSP screen.
    - The DSP will display a “Redirecting…” message before routing the user back to the LSP.
- **Note:**
    - The DSP will not display success or failure screens for mandate registration.

**Mandate init API Request Body (Exposed to LSPs) (Just for reference)**

```json
{
    "opportunityId": "{{opportunityId}}",
    "bankAccountVerificationId": "{{bankUtilityRefId}}",
    "endDate": "2039-09-20", // Not required
    "preferredMandateMode": [ "API_MANDATE" , "ESIGN" , "PHYSICAL" ],
    "mandateAmount": "5000000",  // Not required
    "redirectionUrl": "https://www.voltmoney.in"
}
```

**Mandate init API Response Body**

```json
{
  "opportunityId": "OPP9726566149",
  "fenixLoanAccountId": null,
  "utilityReferenceId": "URMNDT4945818111",
  "status": "IN_PROGRESS",
  "subStatus": "IN_PROGRESS",
  "data": {
    "bankAccountDetails": {
      "nameAsPerBankAccount": "John Doe",
      "accountNumber": "02629180000",
      "ifscCode": "YESB0000300",
      "accountType": "SAVINGS_ACCOUNT",
      "bankName": "YES BANK"
    }
  },
  "webUrl": "https://dsp.finance.com/redirect?"
}

```

**Mandate Create Request Body(To be called in SDK)**

```json
{
    "opportunityId": "{{opportunityId}}",
    "bankAccountVerificationId": "{{bankUtilityRefId}}",
    "endDate": "2039-09-20",
    "mandateType": "API_MANDATE/ ESIGN/ PHYSICAL",
    "mandateAmount": "50000000",
    "redirectionUrl": "https://www.voltmoney.in"
}
```

1. API_MANDATE - This will initiate the API Mandates. This will take the user to NPCI.
2. ESIGN - This will initiate the eSign mandates. This will take the user to NDSL/ CDSL.
3. Physical - This will initiate the physical mandate flow. User have to upload the signed copy.

**Mandate Create Response Body**

```json
{
    "opportunityId": "OPP9726566149",
    "fenixLoanAccountId": null,
    "utilityReferenceId": "URMNDT4945818111",
    "status": "IN_PROGRESS",
    "subStatus": "IN_PROGRESS",
    "data": {
        "bankAccountDetails": {
            "nameAsPerBankAccount": "John Doe",
            "accountNumber": "02629180000",
            "ifscCode": "YESB0000300",
            "accountType": "SAVINGS_ACCOUNT",
            "bankName": "YES BANK"
        },
        "mandateType": "API_MANDATE",
        "maxAmount": 50,
        "startDate": 1732200163700,
        "expiryDate": 2200156199999,
        "mandateFrequency": "ADHOC",
        "mandateStatus": null,
        "mobileNumber": "8494901798",
        "failureReason": null,
        "redirectionUrl": "https://www.google.com"
    },
    "verifierData": {
        "verifier": "DIGIO",
        "verifierReferenceId": "ENA241121201247204TR2F2O8WEBO9AP",
        "verifierTokenId": "GWT241121201247279RYQZBYB8DY64PS"
    },
    "webUrl": "https://ext.digio.in/#/gateway/login/ENA241121201247204TR2F2O8WEBO9AP/ENA241121201247204TR2F2O8WEBO9AP/8494901798?token_id=GWT241121201247279RYQZBYB8DY64PS&redirect_url=https://www.google.com"
}
```

### General Requirement

- **Customizability**:
    - All components, UI elements, and themes must be customizable at the LSP level to align with their branding and preferences.
- **LSP Logo**:
    - Including the LSP logo on the interface should be optional and configurable through the backend.
- **"Need Help" CTA**:
    - The "Need Help" button should display the support email, phone number, or both, based on the LSP’s configuration.
- **User Journey Continuity** *(Excluding mandates)*:
    - Users should resume their journey seamlessly from where they left off:
        - If a user completes the KYC process but drops off, they should resume from the progression screen.
        - The progression screen must clearly indicate that the KYC step has been completed.
        - The backend should propagate a consistent URL to facilitate user continuity.

---

# **Design**

[Figma Designs](https://www.figma.com/design/SPIVBN2sXOAXmrn89jkhtE/DSP-SDK?node-id=152-24&node-type=section&t=wh5t287LlBZopDbf-0)

[Mandate Prototype](https://www.figma.com/proto/SPIVBN2sXOAXmrn89jkhtE/DSP-SDK?page-id=1%3A3&node-id=306-1329&node-type=frame&viewport=-2467%2C958%2C0.49&t=C3Rwcxvoj9LYWwmQ-1&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=76%3A16&show-proto-sidebar=1)

---

# **Analytics**

- Track events for **KYC step** and **Mandate step**, including:
    - KYC initiation
    - KYC completion (success/failure)
    - Drop-off points during KYC
    - Errors during KYC session
- Track events for **Mandate setup**, including:
    - Mandate initiation
    - Mandate completion (success/failure)
    - Drop-off points during mandate setup(If possible)
    - Errors during mandate SDK invocation
- **User Journey Tracking**:
    - Progress through all steps (KYC, additional data, photo verification, mandate).
    - Time spent on each step.
    - Steps where users drop off most frequently.
- **Optional Data Analytics**:
    - Frequency of optional fields being prefilled by LSPs.
    - User interaction with prefilled fields (edits made).
- **User Behavior Insights**:
    - Device and browser details.
    - User interactions (button clicks, page transitions).
- **Error Analysis**:
    - Common errors and failure reasons for APIs and SDKs.
    - Frequency and type of errors encountered by users.
- **Conversion Metrics**:
    - Percentage of users successfully completing the journey.
    - Percentage of users progressing to the next step after each stage.
- **Customizability Metrics**:
    - Usage and effectiveness of LSP-specific themes or logos.
    - Engagement with "Need Help" support options.
- **Redirection Events**:
    - Tracking user redirection back to LSP screens post-DSP flow.
    - Success rate of redirection processes.

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