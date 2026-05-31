# API flow for KFS and Agreement

Last Edited: June 5, 2025 10:48 AM
PRD ETA: May 6, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

As a platform, there are multiple ways through which LSPs can integrate with our platform, our current implementation offers a redirection flow for collecting KFS consent and Agreement signatures.

In the redirection flow, the customer’s IP and acknowledgement/ signing timestamps are consumed. However not all LSPs would be comfortable with redirecting the users to a different URL for the following reasons:

- They want to own the customer experience (having a different UI will impact their user journey).
- Redirection URLs often require internal approvals to whitelist domains that can be opened within the application which goes through an audit approval which will impact release timelines of integration efforts with LSPs

---

# **How do we measure success?**

- Go live TAT with future LSPs and integration with loan contract generation and acceptance flows

---

# **How are others solving this problem?**

- Other lenders offer APIs which can generate the KFS and Agreement as documents which are then rendered within the UI of the LSPs.
- Separate APIs are shared for collecting consent and signing based information separately (document generation and consent collection are decoupled processes).

---

# **What is the solution?**

We will be decoupling the existing sequential process of Key Fact Statement (KFS) and Agreement generation by building independent APIs. This will enable Loan Service Providers (LSPs) to:

- Generate KFS and Agreement documents separately.
- Collect KFS acknowledgements and Agreement signatures independently via APIs.

This modular approach enhances flexibility and improves integration capabilities for partner platforms.

Additional changes:

- **Validation Layer:** Implement robust validation mechanisms to ensure that all collected data and process flows remain compliant with regulatory guidelines and internal business rules.
- **Command centre changes:** Implement changes to enable operations team to identify, and accordingly handle different sign methodologies separately

## Requirements overview (optional)

## User stories / User flow

## Requirements

### Generate KFS and Agreement separately:

Currently, the KFS and Agreement generation are coupled and follow a sequential flow. We will be decoupling these processes by introducing independent APIs for each.

This change allows Loan Service Providers (LSPs) to generate and manage KFS and Agreement documents separately, enabling better control and integration flexibility.

```json
Existing request:
{
"kfsRequest": {
"creditLimit": 100000,
"sanctionLimit": 20000000,
"interestRate": 10.59,
"tenure": 36,
"feeDetails": {
"processingFee": 1599,
"enhanceLimitFee": 499,
"renewalFee": 1899,
"marginPledgeFee": 599
}
}
,
"agreementRequest": {
"kycReferenceId": "{{kycRefId}}",
"additionalUtilityReferenceId": "{{additionalDataRefId}}",
"photoUtilityReferenceId": "{{photoRefId}}",
"bankAccountReferenceId": "{{bankUtilityRefId}}"
}
,
"redirectionUrl": "https://www.voltmoney.in"
}

```

<aside>
⚠️

As per RBI guidelines, the KFS must be presented to the user before the Agreement is generated. Therefore, LSPs must first generate the KFS, and then include the kfsUtilityReferenceId when invoking the Agreement generation API. This ensures compliance and proper sequencing of user consent.

</aside>

POST Request: KFS Generation API

```json
POST /api/v2/generate-kfs
{
  "creditLimit": 100000,
  "sanctionLimit": 20000000,
  "interestRate": 10.59,
  "tenure": 36,
  "feeDetails": {
    "processingFee": 1599,
    "enhanceLimitFee": 499,
    "renewalFee": 1899,
    "marginPledgeFee": 599
  }
}
```

POST Request: Agreement Generation API

```json
POST /api/v1/generate-agreement

{
  "kfsUtilityReferenceId": "{{kfsRefId}}",
  "kycReferenceId": "{{kycRefId}}",
  "additionalUtilityReferenceId": "{{additionalDataRefId}}",
  "photoUtilityReferenceId": "{{photoRefId}}",
  "bankAccountReferenceId": "{{bankUtilityRefId}}",
}
```

The success responses of the respective APIs, will have the documents respectively. (We will be passing a pre-signed URL of the generated document in the response.

### KFS acknowledgement and Agreement signature

Separate APIs will be provided to LSPs to:

- Record the customer's **KFS acknowledgement**, and
- Capture the **Agreement signature**.

<aside>
⚠️

Please note: The LSP should not be able to hit the sign agreement API call if the KFS is not consented by the user and should throw a validation error with the corresponding ENUM and error message

</aside>

We will be collecting the following parameters in the KFS acknowledgement API:

- KFS utility reference ID
- Customer IP
- KFS acknowledgement timestamp

KFS acknowledgement API 

```json
POST /api/v2/acknowledge-kfs

{
  "kfsUtilityReferenceId": "{{kfsRefId}}",
  "customerIp": "203.0.113.42",
  "acknowledgementTimestamp": "2025-05-06T10:45:00Z"
}
```

Agreement sign API

```json
{
  "agreementUtilityReferenceId": "{{agreementRefId}}",
  "kfsUtilityReferenceId": "{{kfsRefId}}",
  "customerIp": "203.0.113.42",
  "signatureTimestamp": "2025-05-06T11:15:00Z"
}
```

### **Validations**

The following validations must be enforced to ensure compliance, data integrity, and a secure consent flow:

1. **Sequential Consent Enforcement**
    - The Agreement **must not** be signed before the KFS is acknowledged.
    - If attempted, the API should return a validation error with a clear ENUM indicating `KFS_NOT_ACKNOWLEDGED`.
2. **KFS Expiry Validation**
    - KFS acknowledgement **must occur within 3 working days** of its generation.
    - If the KFS is older than 3 working days, the API should reject the acknowledgement and return an ENUM such as `KFS_EXPIRED`, along with a message prompting the LSP to regenerate the KFS.
3. **IP Consistency Check**
    - The **customer IP address** captured during KFS acknowledgement and Agreement signature **must match**.
    - Update (We will not place this validation, instead we will be collecting two different IPs in each API request for acknowledgement and sign).
    - A mismatch should raise an error with ENUM `IP_MISMATCH`, indicating possible session tampering or user switch.
4. **Timestamp Order Validation**
    - The Agreement **signature timestamp** must be **after** the KFS acknowledgement timestamp.
    - If violated, return ENUM `INVALID_SIGNATURE_TIMESTAMP.`
5. **Reference ID Validation**
    - All incoming utility reference IDs (for KFS or Agreement) must be:
        - Present in the system.
        - Active (not expired).
        - Mapped to the same user session or customer entity.
    - Violations should raise a `INVALID_OR_STALE_REFERENCE_ID` error.
6. **Mandatory Field Validation**
    - All required fields in the payload (reference IDs, IP address, timestamp) must be non-null and correctly formatted.
    - Violations should return `MISSING_OR_INVALID_FIELDS`.
7. **Redirection URL Whitelisting (Optional)**
    - If a redirection URL is passed during agreement generation, it must be from a whitelisted domain to avoid phishing attempts.
- **Opportunity Status Validation**
- The provided `opportunityId` must:
    - Exist in the system.
    - Be in an **active** state.
    - Not be **suspended**
- If invalid, return ENUM: `SUSPENDED_OPPORTUNITY`.

### Command centre:

![image.png](API%20flow%20for%20KFS%20and%20Agreement/image.png)

We will be changing the KFS acknowledgement status and customer sign status for agreement (only for API based flows) as follows:

- KFS acknowledgement status: Approved through {Sourcing channel}  on timestamp
- Customer sign status: Verified through {Sourcing channel} via Click wrap at timestamp

---

# **Design**

NA

---

# **Analytics**

- There should be any changes in the way we consume data across utiltiies and KFS and agreement signature
- KFS acknowledgement failures and Agreement signing failures should be identifiable via status and sub statuses
- 

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