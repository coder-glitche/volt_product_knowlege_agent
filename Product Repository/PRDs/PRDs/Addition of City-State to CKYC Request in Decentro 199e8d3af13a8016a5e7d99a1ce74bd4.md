# Addition of City-State to CKYC Request in Decentro API

: Surya Ganesh
Created time: February 13, 2025 11:34 AM
Status: In progress
Last edited: June 18, 2025 6:10 PM

# **What problem are we solving?**

The Central Registry of Securitisation Asset Reconstruction and Security Interest (CERSAI) manages the centralized CKYC database. 

CKYCRR (CKYC Registry) maintains a master pincode list that works differently from the standard India Post directory. Here's how:

Source and Updates

- CKYCRR sources its pincode data from India Post (.csv file)
- Updates occur every 6 months
- Requires 3 weeks notice to Reporting Entities for implementation

Note: city and district are used through out the PRD inter-changeably. 

How the Master List Works

The CKYC Master List follows a specific logic for handling pincodes:

1. **Single District-State Pincodes:**
    - If a pincode has only one district-state combination, it's included in the master list
    - Example: Pincode 400051 → Mumbai Suburban, Maharashtra
    - In this case, we can send this pincode and CERSAI will populate the state and city referring to the CKYC Master Pincode List
2. **Multiple District-State Pincodes:**
    - If a pincode has multiple valid district-state combinations, it's intentionally EXCLUDED from the master list
    - Example: Pincode 247775 can be used with either:
        - SHAMLI, UTTAR PRADESH
        - MUZAFFARNAGAR, UTTAR PRADESH
    - In this case, CERSAI won’t be able to populate the city-state combination and the CKYC application fails.

Our 3rd Party vendor responsible for the CKYC upload (Decentro) does the validation by comparing the pincode to its own pincode directory which is exactly same as the CKYC Master Pincode List before the upload commences. This ensures reduced number of failures after uploading.

Currently, we send only the pincode in the request body while calling the Decentro API and this causes a validation failure (Decentro rejects it before it reached CERSAI).

## Core Issue

Applications from Financial Institutions are getting rejected when they contain valid pincodes that are not reflected in the  CKYC Master Pincode List. This occurs because:

1. The CKYC Master Pincode List does not store pincodes with more than one city-state pair
2. There is no mechanism to handle changes when CKYC Master Pincode List updates and possibly, some of the pincodes get updated

---

# **How do we measure success?**

Zero Missing Pincode Errors

---

# **How are others solving this problem?**

N.A

---

# **What is the solution?**

The solution has been presented in the notice provided by CERSAI published on 31st Jan 2025:
[**Notice by CERSAI](https://www.ckycindia.in/ckyc/assets/doc/4838-Rejection_in_upload_of_KYC_records_due_to_mismatch_of_PIN.pdf)**
The notice recognised the problem and gave the solution of passing the state and the city (which have been part of the request body but was not added before as they were optional). CERSAI will accept the city-state pair and process the documents if the pincode is missing.

This ensures no rejection from CERSAI’s  as well as 3rd Party Service Provider’s side due to the pincode missing with the CKYC Master Pincode List.

## Requirements overview (optional)

## User stories / User flow

## Requirements

**I.** We will be doing a two step implementation:

1. We will be uploading all the CKYC applications, as we do right now, with only the pincode. 
2. If the CKYC gets rejected by the 3rd Party (Decentro) due to the pincode error “RECORD_VALIDATION_FAILED” with the response:

3. We store this error. We retry that specific application along with the city-state pair from the customer’s KYC details in the next batch we upload.

```json
{
    "decentroTxnId": "EEB679CE926C4E5A9FC4EE157552913D",
    "status": "FAILURE",
    "responseCode": "E00009",
    "message": "Issues detected with the request payload.",
    "data": {
        "individuals": [
            {
                "index": 0,
                "identifier": "12312ssdfsdf",
                "count": 1,
                "errors": [
                    {
                        "message": "Pincode is not valid. Hint: pincode (str)",
                        "responseKey": "error_invalid_pincode"
                    }
                ]
            }
        ]
    },
    "responseKey": "error_invalid_payload"
```

**II.** We also need to make sure the **state and city are visible in the review file generated** which is checked and approved by the Risk Ops team. We can add the column regardless if there are any cases being handled for the pincode issue.

Passing City and State in the JSON code when running the Decentro API. The following is the syntax for the same highlighted in brown:

```json
import requests

url = "https://in.staging.decentro.tech/v2/kyc/ckyc/bulk/individuals/upload"

payload = {
    "reference_id": "123456789",
    "consent": True,
    "purpose": "For bank account purpose",
    "verifier": {
        "name": "Example Name",
        "designation": "Example Designation",
        "employee_code": "1234",
        "kyc_declaration_place": "Bangalore"
    },
    "individuals": [
        {
            "identifier": "123456789",
            "salutation": "MR",
            "name": "John Doe",
            "gender": "MALE",
            "date_of_birth": "YYYY-MM-DD",
            "location": {
						"address": "124/8A West Azad Nagar Delhi - 110051",
						"pincode": "110051",
						"state": "Delhi",
						"city": "Delhi"
				},

            "document_submission_type": "OFFLINE_VERIFICATION",
            "relative": {
                "salutation": "MR",
                "type": "FATHER",
                "name": "Johnathan Doe"
            },
            "documents": [
                {
                    "base64": "<base64>",
                    "type": "AADHAAR"
                },
                {
                    "base64": "<base64>",
                    "type": "PHOTOGRAPH"
                }
            ],
            "ids": [
                {
                    "id_number": "4720",
                    "type": "AADHAAR"
                }
            ]
        }
    ]
}
headers = {
    "accept": "application/json",
    "client_id": "example_client_id",
    "client_secret": "example_client_secret",
    "module_secret": "example_module_secret",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

**The sample request:** 

https://docs.google.com/document/d/1EPl5vTNro56E905R9F2uxqZjLCARZVAeSIISIFBNvIU/edit?usp=sharing

There are no specific casing requirements for the city and state. We will pass the city and state in Pascal Casing. Example: “city” : “Mumbai”, “state” : “Maharashtra”.  We need to make sure no special characters should be part of the city and state except spaces between words. If present, brackets should be removed and in case of full-stops and hyphens, they should be replaced with a space.

We have already tested with 1 CKYC upload where we uploaded the city and state pair along with the pincode which worked successfully. 

### Sourcing the Data

We will be sourcing the City and State from the KYC details of the customer where the “city”:”XXXXXX” and “state”:”XXXXXXX” is present.

Incases of city or state being null, the accounts will not be created so we will be able to handle such cases during the account opening journey itself. Additionally, because we are retrieving this data from Aadhaar, it will always have the city and state mentioned.

### Error Handling

Any case of any error occurring for applications with City-State mentioned, log the error and retry in the next batch

---

# **Design**

N.A

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

N.A

## Marketing

N.A

## Ops & Sales training

N.A

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