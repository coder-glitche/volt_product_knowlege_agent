# [Platform] Wrapper APIs for RTAs

: Vaibhav Arora
Created time: March 5, 2025 6:59 AM
Status: Not started
Last edited: March 24, 2025 5:17 PM

# **What problem are we solving?**

AMCs are divided between two RTAs CAMS and KFIN, both CAMS and KFIN have a common initiative called MFC. All CAMS, KFIN and MFC have different APIs and corresponding features like:

- Session management
- Error handling
- Encryption/Decryption
- Authorisation

While KFIN has session management and credential based authorisation, CAMS has a signature along with encryption and decryption of requests and response packets.

MFC on the other hand, has session management (via JWT tokens), encryption and decryption along with signatures which makes it very hard for an LSP to integrate with each of the entities independently.

There are also edge cases and internal learnings that we have implemented over the years to handle errors from the RTAs for fetch and pledge that will be handled (RTA error messages keep on changing and are not consistent between KFIN/CAMS/MFC) we will be making a consistent set of error messaging to allow LSPs to handle corresponding scenarios and messaging to the user for fetch and pledge

Certain AMCs support pledging upto 3 decimals, while most AMCs have a support of 2 decimals, this introduces two issues:

- KFIN allows pledging upto 3 decimals however pledging above 3 decimals have a relatively higher failure rate (20%) than normal pledging due to limited AMC support and internal reconciliation issues
- Post pledging as we do computation in amount and convert it back to units upto 2 decimals, trailing units (in 3 decimals) are left behind which cannot be unlien marked digitally (due to the limits placed by the RTAs) and have to be manually unlien marked.

Currently we have no visibility on the units pledged against the NBFC via LSPs and only get to know of the number when we get the corresponding request, getting pledge data across customers will be essential for us for the following reasons:

- Getting visibility of collaterals pledged (across ISINs) against the NBFC
- Building a collateral management system which will track all collateral holdings, and corresponding metrics like concentration risk, total DP
- Management of unlinked (not lodged) collaterals and compliance requirement to un lien mark within 30 days of pledging if not lodged against a loan

As a regulated entity, we get credentials from respective RTA which we are not supposed to integrate, with wrapper APIs we will be able to maintain single credentials at NBFCs disposal, and will be able to give access based control to LSPs integrating with us on our wrapper APIs.

---

# **How do we measure success?**

- Days taken to integrate with RTA APIs with LSPs (Subjective)

---

# **How are others solving this problem?**

NA

---

# **What is the solution?**

We will be building wrapper V2 APIs for the following workflows:

- Investor consent API (MFC) (OTP generation)
- Get CAS Document API - Summary (MFC)
- Lien status API (KFIN V2)
- Lien status API (CAMS)
- Lien marking API (KFIN V2)
- Lien marking API (CAMS)

We will also be simplifying multiple processes which are to be done to ensure that the integration is seamless for our LSPs:

- MFC token generation and management
- MFC signature generation
- MFC encryption and decryption (Sanitisation of LSP request to MFC encrypted format and response sanitisation in decrypted format to LSP)
- KFIN session management for lien marking and status
- CAMS signature generation for lien marking and status
- CAMS encryption and decryption for lien marking and status

There will be three wrapper APIs (DSP) which the LSPs will be expected to integrate (two are essential and one is optional):

- Fetch (Support for MFC fetch / CAMS fetch / KFIN fetch) - Essential
- Pledge (Support for CAMS pledge and KFIN pledge) - Essential
- Lien status (Support for transaction level lien marking status get) - Optional

## Requirements

MFC fetch:

### Initiate Consent API (gets user consent for fetch and triggers OTP to the customer)

```

POST /api/v2/mfcentral/consent

POST /api/v2/cams/consent

POST /api/v2/kfintech/consent

```

Request parameters:

```json
{
  "pan": "string", // User's PAN number
  "mobile": "string", // Registered mobile number for the user
}
```

We will be doing validations at source before passing on the request to MFC, and then will be raising the request to MFC:

```json
Sample response from MFC:

{
"reqId": 2469810,
"otpRef": "c4558eff-aae1-42c9-b913-f85d3c90c9d7", //Needs to be passed in the OTP validation API
"userSubjectReference": "",
"clientRefNo": "0206ranjani0108_0417" // Passed in the request
}
```

Fenix validations:

- Regex validation on PAN
- Regex validation on Mobile (MFC expects mobile appended with the country code (+91) we will be also expecting the same from the LSP)

Response from DSP wrapper API:

```json
{
  "status": "string", // "success" or "error"
  "requestId": "string", // Generated request ID for subsequent calls (This will be the clientrefID which will be generated by Fenix and passed to LSP in response)
  "otpSent": "boolean", // Indicates if OTP was successfully sent
  "otpReference": "string", // Reference ID for OTP validation
  "error": {
    "code": "string", // Error code if applicable
    "message": "string" // Error description if applicable
    "thirdpartyerror": "string" // Error description if applicable
  }
}
```

Error messages:

| Scenario | Code | Validator | Message | Third party error |
| --- | --- | --- | --- | --- |
| Fenix PAN validation | INVALID_PAN | Fenix | Please enter a valid PAN and try again | NA |
| Fenix Mobile validation | INVALID_MOBILE | Fenix | Please enter a valid mobile number (Country code + 10 digits) and try again | NA |
| Unhandled error from MFC  | SYSTEM_ERROR | MFC | An unknown error occurred | Pass MFC error message response |

MFC OTP Validation:

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