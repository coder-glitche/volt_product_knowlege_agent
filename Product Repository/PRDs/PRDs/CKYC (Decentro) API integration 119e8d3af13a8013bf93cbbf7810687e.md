# CKYC (Decentro) API integration

: Vaibhav Arora
Created time: October 8, 2024 6:32 PM
Status: Done
Last edited: February 20, 2025 5:27 PM

# **What is CKYC?**

CKYC, or Central KYC (Know Your Customer), is a centralized registry in India where personal information related to identity verification is stored. When someone opens a new account with a bank or any financial institution, they typically need to submit documents to prove who they are (this process is called KYC).

Instead of submitting these documents every time, CKYC stores this information in one place. Once your details are registered with CKYC, any financial institution can access your information from the database, making the process faster and reducing the need for repetitive documentation. Essentially, CKYC streamlines the KYC process across different institutions.

[CKYC reporting master](https://docs.google.com/spreadsheets/d/1FWkdbFsAHewP_lmQTeG8_6wEPkQw0xW21__FBs1SifA/edit?gid=0#gid=0)

# **What problem are we solving?**

- Manual effort in retrieving and matching data
    - CKYC is a manual process for a lot of banks where KYC records are manually updated and then converted into consumable format by Cersai.
- Prone to errors which might result in borrowers’ records getting updated incorrectly
    - Due to the manual nature of flows, the process is error prone and has an impact on user’s KYC data saved with Cersai (which may be used by other lenders) and may impact user experience
- Upload involves processing/accessing a lot of PII & KYC data of borrowers
    - A lot of PII information and KYC data is consolidated and then posted into the CKYC registry.
- Delay in upload impacts our NBFC from a regulatory perspective
    - Meet regulatory requirements and be compliant with master regulations for KYC shared by the RBI

---

# **How do we measure success?**

- Man-hours per month to not exceed 10 MH (Management of upload processes)
- Success rate for CKYC upload > 95% (Accuracy of CKYC upload data)
- TAT for CKYC upload confirmation < 12 hours (Upload → Response → Reconciliation)
- Updating records to CKYC before the time period - 100% (CKYC upload coverage to meet guidelines within the designated TAT - 10 days)
(CKYC reporting for a new account must be completed within 10 days of account opening)

Success criteria we are looking to achieve in subsequent iterations.

- Error in updating records in < 1% of applications (Updating not in scope for V1)

---

# **How are others solving this problem?**

Most large REs are updating (uploading) records to CKYC in a manual manner through CKYC dashboard at a single record level or bulk upload. Some REs also use the SFTP flow to pass the records to CKYC. Most of this is manual and can result in errors.

Many REs use 3rd party vendors like Trackwizz, Digio, Decentro, Signzy, etc to process the upload flow through SFTP/APIs

- Review notes
    
    Ask decentro for the reconciliation flow (and how it can be handled)
    

---

# **What is the solution?**

We will be integrating with Decentro’s upload API to push CKYC data to Cersai.

[Documentation](https://docs.decentro.tech/reference/kyc-and-onboarding-api-reference-identities-ckyc-services-upload-individuals)

API request sections:

| **Parameter** | **Type** | **Number of entries per API call** | **Mandatory** | **Definition** |
| --- | --- | --- | --- | --- |
| `name` | String | One | Yes. Hardcoded | The name of the employee who has done the KYC verification and is performing the CKYC upload.  |
| `designation` | String | One | Yes. | The designation of the employee who is performing the CKYC upload. |
| `kyc_declaration_place` | String | One | Yes. Hardcoded | The place of declaration or verification of the KYC documents. |
| `employee_code` | String | One | Yes. Hardcoded | The employee code of the person performing the CKYC upload. |
| `individuals` | Array | (Multiple) | No | An array of individuals whose details are to be uploaded to CKYC. Refer the Individuals array |
| `legal_entities` | Array | (Not applicable) | No | An array of legal entities whose details are to be uploaded to CKYC. |

Individual array request parameters:

| **Parameter** | **Type** | **Mandatory** | **Definition** | **What needs to be passed** |
| --- | --- | --- | --- | --- |
| `identifier` | String | Yes | A unique reference ID of this user set by the RE. This is a mandatory field. | FX Client ID |
| `salutation` | String | Yes | The salutation of the user should be less than 5 characters. Examples are "MR", "MRS", "MS" and "MX" | Stored in Finflux (As per KYC) |
| `name` | String | Yes | The full name of the user. | Full name in customer as per KYC |
| `gender` | String | Yes | The gender of the user can be one of the following: `MALE`, `FEMALE` and `TRANSGENDER` | Gender of the customer stored in KYC |
| `date_of_birth` | String | Yes | The date of the birth of the user. Validation is done on the format. The date format needs to be “YYYY-MM-DD”. | DOB of the customer stored in KYC |
| `relative` | Object | Yes | The object contains the type (string) and name (string) of the relative. The type of the relative can be one `FATHER` or `SPOUSE` | FATHER (Static value)

Along with Father name (stored in Finflux) |
| `location` | Object | Yes | The object that denotes the full address of the individual. | Address object 
(Complete address in one string)
Pincode
State (as per masters)
City (as per masters) |
| `document_submission_type` | String | Yes | String denoting the types of documents submitted. Please refer to the Document Submission Type section. | EKYC (Static value) |
| `documents` | Array | Yes | Array representing the list of documents. Following documents are mandatory:• 1 document of type `PHOTOGRAPH`• 1 valid document that can be a Proof of AddressRefer to the Document Type section to learn more about the valid values for the type field in the members of documents array. | We need to pass two documents:

Photograph and Aadhaar 

(With base64 files for each)

- Aadhaar should be masked 

- Customer photograph should be passed  |
| `ids` | Array | Yes` | Array representing the list of IDs collected for the user.• 1 document ID of type `PAN` is mandatory.• 1 valid document ID that can be a Proof of AddressRefer to the ID type section to learn more about the valid values for the type field in the members of documents array. | PAN with complete PAN number, Eg: CLFPA9890J

Aadhaar with first 8 digits masked and last 4 digits to be passed 

XXXXXXXX1845 |

Sample Curl:

```json

{
  "reference_id": "11222323",
  "verifier": {
    "name": "Nishant Athmakoori",
    "designation": "Ops manager",
    "kyc_declaration_place": "Mumbai",
    "employee_code": "EMP001"
  },
  "purpose": "Registering a new user to CKYC",
  "consent": true,
  "individuals": [
    {
      "identifier": "12312312",
      "salutation": "MR",
      "name": "Vaibhav Arora",
      "gender": "MALE",
      "date_of_birth": "1999-04-14",
      "relative": {
        "type": "FATHER",
        "salutation": "Mr",
        "name": "Father Arora"
      },
      "document_submission_type": "EKYC",
      "location": {
        "address": "124/8A West Azad Nagar Delhi - 110051",
        "pincode": "110051",
        "state": "Delhi",
        "city": "Delhi"
      },
      "documents": [
        {
          "type": "AADHAAR",
          "base64": "bW92aW5nYWZ0ZXJub29ucGFzdHByb2JsZW1kZWNsYXJlZHdpZmVkZXRhaWxub2JvZHk="
        },
        {
          "type": "PHOTOGRAPH",
          "base64": "anVtcHNwaXRlZmlsbWJlY2F1c2V0YWxsZXN0YWJsaXNocG9zdG1lYW5zaGl0aGVhZGk="
        }
      ],
      "ids": [
        {
          "id_number": "XXXXXXXX1845",
          "type": "AADHAAR"
        },
        {
          "id_number": "CLFPA9890J",
          "type": "PAN"
        }
      ]
    }
  ]
}

```

Sample curl with multiple individuals:

```json
{
	"reference_id": "11222323",
	"verifier": {
		"name": "Nishant Athmakoori",
		"designation": "Ops manager",
		"kyc_declaration_place": "Mumbai",
		"employee_code": "EMP001"
	},
	"purpose": "Registering a new user to CKYC",
	"consent": true,
	"individuals": [
		{
			"identifier": "12312312",
			"salutation": "MR",
			"name": "Vaibhav Arora",
			"gender": "MALE",
			"date_of_birth": "1999-04-14",
			"relative": {
				"type": "FATHER",
				"salutation": "Mr",
				"name": "Father Arora"
			},
			"document_submission_type": "EKYC",
			"location": {
				"address": "124/8A West Azad Nagar Delhi - 110051",
				"pincode": "110051",
				"state": "Delhi",
				"city": "Delhi"
			},
			"documents": [
				{
					"type": "AADHAAR",
					"base64": "bW92aW5nYWZ0ZXJub29ucGFzdHByb2JsZW1kZWNsYXJlZHdpZmVkZXRhaWxub2JvZHk="
				},
				{
					"type": "PHOTOGRAPH",
					"base64": "anVtcHNwaXRlZmlsbWJlY2F1c2V0YWxsZXN0YWJsaXNocG9zdG1lYW5zaGl0aGVhZGk="
				}
			],
			"ids": [
				{
					"id_number": "XXXXXXXX1845",
					"type": "AADHAAR"
				},
				{
					"id_number": "CLFPA9890J",
					"type": "PAN"
				}
			]
		},
		{
			"identifier": "12312314",
			"salutation": "MR",
			"name": "Vaibhav Ramesh",
			"gender": "MALE",
			"date_of_birth": "1999-04-15",
			"relative": {
				"type": "FATHER",
				"salutation": "Mr",
				"name": "Father Ramesh"
			},
			"document_submission_type": "EKYC",
			"location": {
				"address": "124/8A West Azad Nagar Delhi - 110051",
				"pincode": "110051",
				"state": "Delhi",
				"city": "Delhi"
			},
			"documents": [
				{
					"type": "AADHAAR",
					"base64": "bW92aW5nYWZ0ZXJub29ucGFzdHByb2JsZW1kZWNsYXJlZHdpZmVkZXRhaWxub2JvZHk="
				},
				{
					"type": "PHOTOGRAPH",
					"base64": "anVtcHNwaXRlZmlsbWJlY2F1c2V0YWxsZXN0YWJsaXNocG9zdG1lYW5zaGl0aGVhZGk="
				}
			],
			"ids": [
				{
					"id_number": "XXXXXXXX1846",
					"type": "AADHAAR"
				},
				{
					"id_number": "CLFPA9891J",
					"type": "PAN"
				}
			]
		}
	]
}
```

Request response (Success):

```json
{
    "decentroTxnId": "DEC001",
    "status": "SUCCESS",
    "responseCode": "S00000",
    "message": "CKYC bulk upload has been initiated",
    "responseKey": "success_initiate_bulk_upload"
}
```

Request level (Failure):

```json
{
    "decentroTxnId": "97F82E27B6724020AC795CDE50D93189",
    "status": "FAILURE",
    "responseCode": "E00009",
    "message": "Issues detected with the request payload.",
    "data": {
        "verifier": [
            {
                "count": 1,
                "errors": [
                    {
                        "message": "Employee code cannot be null or empty. Hint: employee_code (str)",
                        "responseKey": "error_empty_employee_code"
                    }
                ]
            }
        ]
    },
    "responseKey": "error_invalid_payload"
}
```

Record level failure: (Identifier is present in request)

```json
{
    "decentroTxnId": "1763D6C9DB2947D4B4173940317E5925",
    "status": "FAILURE",
    "responseCode": "E00009",
    "message": "Issues detected with the request payload.",
    "data": {
        "individuals": [
            {
                "index": 0,
                "identifier": "12312312",
                "count": 1,
                "errors": [
                    {
                        "message": "Salutation cannot be null or empty. Hint: salutation (str)",
                        "responseKey": "error_empty_salutation"
                    }
                ]
            }
        ]
    },
    "responseKey": "error_invalid_payload"
}
```

Record level failure with multiple records:

```json
{
	"reference_id": "11222325",
	"verifier": {
		"name": "Nishant Athmakoori",
		"designation": "Ops manager",
		"kyc_declaration_place": "Mumbai",
		"employee_code": "EMP001"
	},
	"purpose": "Registering a new user to CKYC",
	"consent": true,
	"individuals": [
		{
			"identifier": "12312312",
			"salutation": "MR",
			"name": "",
			"gender": "MALE",
			"date_of_birth": "1999-04-14",
			"relative": {
				"type": "FATHER",
				"salutation": "Mr",
				"name": "Father Arora"
			},
			"document_submission_type": "EKYC",
			"location": {
				"address": "124/8A West Azad Nagar Delhi - 110051",
				"pincode": "110051",
				"state": "Delhi",
				"city": "Delhi"
			},
			"documents": [
				{
					"type": "AADHAAR",
					"base64": "bW92aW5nYWZ0ZXJub29ucGFzdHByb2JsZW1kZWNsYXJlZHdpZmVkZXRhaWxub2JvZHk="
				},
				{
					"type": "PHOTOGRAPH",
					"base64": "anVtcHNwaXRlZmlsbWJlY2F1c2V0YWxsZXN0YWJsaXNocG9zdG1lYW5zaGl0aGVhZGk="
				}
			],
			"ids": [
				{
					"id_number": "XXXXXXXX1845",
					"type": "AADHAAR"
				},
				{
					"id_number": "CLFPA9890J",
					"type": "PAN"
				}
			]
		},
		{
			"identifier": "12312314",
			"salutation": "MR",
			"name": "Vaibhav Ramesh",
			"gender": "MALE",
			"date_of_birth": "",
			"relative": {
				"type": "FATHER",
				"salutation": "Mr",
				"name": "Father Ramesh"
			},
			"document_submission_type": "EKYC",
			"location": {
				"address": "124/8A West Azad Nagar Delhi - 110051",
				"pincode": "110051",
				"state": "Delhi",
				"city": "Delhi"
			},
			"documents": [
				{
					"type": "AADHAAR",
					"base64": "bW92aW5nYWZ0ZXJub29ucGFzdHByb2JsZW1kZWNsYXJlZHdpZmVkZXRhaWxub2JvZHk="
				},
				{
					"type": "PHOTOGRAPH",
					"base64": "anVtcHNwaXRlZmlsbWJlY2F1c2V0YWxsZXN0YWJsaXNocG9zdG1lYW5zaGl0aGVhZGk="
				}
			],
			"ids": [
				{
					"id_number": "XXXXXXXX1846",
					"type": "AADHAAR"
				},
				{
					"id_number": "CLFPA9891J",
					"type": "PAN"
				}
			]
		}
	]
}
```

**Decentro response description and handling:**

| **Code** | **Description** | Handling |
| --- | --- | --- |
| error_invalid_relative_name | Invalid relative name passed in the request (String validation): Either the name is null or contains special characters  | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_relative_type | Error Invalid Relative Type Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_relative_type | Error Empty Relative Type Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_relative_name | Error Empty Relative Name Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message - N records out of M failed, email |
| error_empty_emp_code | Empty EMP Code Error | Fail batch upload and raise an alert (Log the error message) - Raise JIra (send email) |
| error_empty_branch | Empty Branch Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_id_number | Invalid ID Number Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_document_submission_type | Invalid Document Submission Type | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_pincode | Invalid Pincode Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_date_of_birth | Empty Date Of Birth Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_name | Invalid Name Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_name | Empty Name Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_city | Empty City Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_gender | Invalid Gender Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_verifier_name | Empty Verifier Name Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_city | Invalid City Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_individuals | Empty Individuals Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_address | Invalid Address Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_location | Empty Location Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_ids | Invalid IDs Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_document_submission_type | Empty Document Submission Type | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_verifier_designation | Invalid Verifier Designation | Fail batch upload and raise an alert (Log the error message) |
| error_empty_documents | Empty Documents Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_identifier | Empty Identifier Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_base64 | Empty base64 Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_branch | Invalid Branch Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_date_of_birth | Invalid Date of Birth Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_verifier_name | Invalid Verifier Name Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_salutation | Empty Salutation Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_address | Empty Address Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_verifier_designation | Empty Verifier Designation Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_document_type | Invalid Document Type Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_salutation | Invalid Salutation Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_individuals | Invalid Individuals Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_location | Invalid Location Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_batch_details | Invalid Batch Details Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_emp_code | Invalid EMP Code Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_state_code | Empty State Code Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_id_number | Empty ID Number Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| success_initiate_bulk_upload | Success Initiate Bulk Payload | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_ids | Empty IDs Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_base64 | Invalid Base64 Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_document_type | Empty Document Type Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_pincode | Empty Pincode Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error messageMark loan account CKYC upload as failed, remove from batch job and try again - Log the error messageMark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_batch_details | Empty Batch Details Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_gender | Empty Gender Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_state_code | Invalid State Code Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_documents | Invalid Documents Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_identifier | Invalid Identifiers Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_payload | Invalid Payload Error | Fail batch upload and raise an alert (Log the error message) |
| error_duplicate_identifier | Duplicate Identifier Error | Update request ID and try again  |
| error_empty_employee_code | Empty Employee Code Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_verifier | Empty Verifier Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_kyc_declaration_place | Invalid KYC Verification Place Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_employee_code | Invalid Employee Code Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_kyc_declaration_place | Empty KYC Declaration Place Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_verifier | Error Invalid Verifier | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_relative | Invalid Relative Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_relative | Empty Relative Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_upload_limit_exceeded |  | Fail batch upload and raise an alert (Log the error message) |
| success_bulk_upload_status_extracted | Success CKYC Upload Status Extracted | Fail batch upload and raise an alert (Log the error message) |
| success_bulk_upload_entity_status_extracted | Success CKYC Upload Entity Status Extracted | Not applicable |
| error_empty_incorporation_date | Empty Incorporation Date Error | Not applicable |
| error_empty_related_individual_ckyc_id | Empty Related Individual CKYC ID Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_entity_name | Empty Entity Name Error | Not applicable |
| error_empty_incorporation_country_code | Empty Incorporation Country Code Error | Not applicable |
| error_empty_related_individuals | Empty Related Individuals Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_related_individual_deletion_flag | Invalid Related Individual Deletion Flag Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_incorporation_place | Empty Incorporation Place Error | Not applicable |
| error_invalid_related_individuals | Invalid Related Individuals | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_related_individual_ckyc_id | Invalid Related Individual CKYC ID Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_commencement_date | Invalid Commencement Date Error | Not applicable |
| error_invalid_related_individual_name | Invalid Related Individual Name Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_commencement_date | Empty Commencement Date Error | Not applicable |
| error_invalid_incorporation | Invalid Incorporation Error | Not applicable |
| error_invalid_legal_entites | Invalid Legal Entities Error | Not applicable |
| error_invalid_incorporation_country_code | Invalid Incorporation Country Code Error | Not applicable |
| error_empty_related_individual_salutation | Empty Related Individual Salutation Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_constitution_type | Empty Constitution Type Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_entity_name | Invalid Entity Name Error | Not applicable |
| error_empty_legal_entites | Empty Legal Entities Error | Not applicable |
| error_empty_related_individual_type | Empty Related Individual Type | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_constitution_type | Invalid Constitution Type Error | Fail batch upload and raise an alert (Log the error message) |
| error_invalid_incorporation_date | Invalid Incorporation Date Error | Not applicable |
| error_empty_related_individual_deletion_flag | Empty Related Individual Deletion Flag Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_empty_incorporation | Empty Incorporation Error | Fail batch upload and raise an alert (Log the error message) |
| error_empty_related_individual_name | Empty Related Individual Name Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_document_submission_type | Invalid Document Submission Type | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |
| error_invalid_document_type | Invalid Document Type Error | Mark loan account CKYC upload as failed, remove from batch job and try again - Log the error message |

Sample response:

**Callbacks (post upload)**

We will be creating a callback URL and consuming the callbacks from Decentro to update status of records in our system:

| Callback enum | Sample response | Action |
| --- | --- | --- |
| BULK_CKYC_UPLOAD_RECORDS_UPLOADING_COMPLETED | { "attempt": 1, "referenceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "bulkDecentroTxnId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "callbackTxnId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "originalCallbackTxnId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "timestamp": "2024-06-13T10:36:32.604958", "creationTimestamp": "2024-06-13T10:34:06.597703", "lastModificationTimestamp": "2024-06-13T10:36:32.584826", "type": "BULK_CKYC_INDIVIDUALS_UPLOAD", "stage": "BULK_CKYC_UPLOAD_RECORDS_UPLOADING_COMPLETED", "status": "PROCESSING", "description": "Records Processing Completed" } | Mark request as successful and send email to Ops (First email) |
| BULK_CKYC_UPLOAD_RECORDS_UPLOAD_SUCCESSFUL | { "attempt": 1, "referenceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "bulkDecentroTxnId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "callbackTxnId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "originalCallbackTxnId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "timestamp": "2024-06-14T12:31:56.994998", "creationTimestamp": "2024-06-13T10:34:06.597703", "lastModificationTimestamp": "2024-06-14T12:31:56.971892", "type": "BULK_CKYC_INDIVIDUALS_UPLOAD", "stage": "BULK_CKYC_UPLOAD_RECORDS_UPLOAD_SUCCESSFUL", "status": "COMPLETED", "description": "Records Upload Success", "data": { "totalRecords": 93, "processedRecords": 93, "invalidRecords": 6, "approvedRecords": 75, "rejectedRecords": 12 } } | Hit GT Status API to get failed identifiers and update status of pending request |

GT Status API (Once request is processed (Callback is received): We will hit the status API to update the status of the identifiers in the system

```json
{
    "decentroTxnId": "XXXXXXX",
    "status": "SUCCESS",
    "responseCode": "S00000",
    "data": {
        "referenceId": "XXXXXX",
        "bulkDecentroTxnId": "XXXXXX",
        "individuals": {
            "requested": 10,
            "processed": 1,
            "successful": 9,
            "failed": 1,
            "pending": 0,
            "failedIdentifiers": [
                "123456789"
            ]
        },
        "stage": "BULK_CKYC_UPLOAD_RECORDS_UPLOADING_SUCCESSFUL",
        "status": "SUCCESS",
        "description": "Records Uploading Succeeded",
        "creationTimestamp": "XXXXXXXXX",
        "lastModificationTimestamp": "XXXXXXXXX"
    },
    "responseKey": "success_bulk_upload_status_extracted"
}
```

Once a request is initiated, CKYC status for the loans will change to processing, if we receive a failed status and the corresponding reference id, CKYC status for the respective loan should change to Failed. 

When pending becomes 0, and failed loans are marked as fails, it can be assumed that CKYC upload for all pending cases has been completed successfully

## Requirements overview (optional)

**High level flow:**

- N users completes loan application
- Scheduler runs at the end of the day (once in 3 days), for all account openings (client ID corresponding to loan ID) and checks status of CKYC reporting to identify loans where CKYC reporting has not been completed (Failed or not initiated)
- Scheduler then creates a batch, hits Decentro API (Decentro API batches the request as per rate limit) and schedules its own job to upload details to Cersai dashboard
- Once a batch is created, a summary email is sent to ops with an attachment:
    - Subject: CKYC upload initiated with request ID ______  (Date1) to (Date2)
    
    Dear team, 
    
    CKYC upload with request ID _________ has been initiated for loans booked from (Date1) to (Date2). Please review the attached file. 
    
    Additionally M records where CKYC reporting had failed have been included in the batch.
    
    Post review, approve the file on Cersai dashboard to initiate processing of upload.
    
    Team DSP Finance
    ([Attachment template](https://docs.google.com/spreadsheets/d/1kERer1GGEFoMuhnjK_DdJQDUWMUIbc1K_v0q_B16bes/edit?gid=0#gid=0))
- d-ecca353c1c954efc817846e6e28b9b3c (template ID)
Variables:

```json
{
    "date":"24-10-2024",
    "startDate":"21-10-2024",
    "endDate":"23-10-2024",
    "requestId":"1afsofjseofffffb",
    "numberOfFailedRecords":"34"
    
}
```

- We will poll the get status API every 3 hours, for 2 days to get the status of the upload request - API gives synchronous batch processing information (100 records, 20 successful 70 processing, 10 failed) along with failed reference ids
- Once a batch is successfully uploaded a response file will be generated and sent to ops via email
    - CKYC upload completed with request ID _______
    
    Dear team,
    
    CKYC upload with request ID ______ has been completed for loans booked from (Date1) to (Date2). Please review the attached response file. 
    
    Team DSP Finance
    ([Attachment template](https://docs.google.com/spreadsheets/d/1kERer1GGEFoMuhnjK_DdJQDUWMUIbc1K_v0q_B16bes/edit?gid=0#gid=0))
    - Template ID: d-ad34b2744ce441d9b1c0ae213fe0738c
    
    ```json
    {
        "date":"24-10-2024",
        "startDate":"21-10-2024",
        "endDate":"23-10-2024",
        "requestId":"1afsofjseofffffb"
        
    }
    ```
    
- Upon completion of upload, Ops agent will login on the Cersai dashboard to verify the upload and sign the upload file with DSC certificate
- Once uploaded CKYC reporting for the same will be completed. Fenix will track upload till it is uploaded to the Cersai dashboard, in case the uploaded details on Cersai are rejected by the ops agent, they will be able to reject the status of the CKYC upload for that particular customer (it will automatically be retried in the next job)

**Approval workflow on Cersai dashboard:**

Maker and Checker can view and download response of each uploaded batch after checker approval.
User needs to follow following steps to download bulk upload response file:

1. Click on “Bulk Upload Response” link under KYC Management.
2. Click on “SUBMIT” after providing start and end date.

![image.png](External%20reporting%20requirements/image%204.png)

**Response parameters and handling (Post approval):**

Broadly there are two types of errors, request level and record level error:

- In case of a record level error, we will update the CKYC status of the loan account as failed, and remove batch to report the remaining cases (we will have to store the record level error at a loan level, so that it can be corrected till the next batch upload)
- In case of a request level error, we will fail the batch and raise alert on the type of error

| **Status** | **Description** | **Action by** | **Remarks** |
| --- | --- | --- | --- |
| D | Draft | FI Maker | Maker will enter data, can save in draft mode. |
| PA | Pending Approval | FI Checker | Checker will verify the data with the image uploaded and submit it to the registry. |
| IH | Institutional Hold | FI Maker | Records with data/image discrepancies will be put on hold by the Checker. Maker will rectify and resubmit. |
| S | Submitted | FI Checker | Record is submitted to registry and pending de-duplication. |
| BA | Balance Available | Central KYC Registry | Balance available for record processing. |
| IB | Insufficient Balance | Central KYC Registry | Insufficient balance available in web wallet. |
| DM | Data Matching | Central KYC Registry | Record sent for de-duplication. |
| CM | Confirmed Match | Central KYC Registry | Based on data matching rules, record flagged as a confirmed match with another record. |
| FIR | FI Recon | FI | Probable match records pending resolution. |
| IDVP | ID Verification Pending | Central KYC Registry | Pending for ID verification. |
| IDC | ID Confirmed | Response of ID Issuer | If the name sent by the ID issuer matches with the name of the applicant, the status of the record will be changed to IDC. |
| IDNC | ID Not Confirmed | Response of ID Issuer | If the ID issuer flags the ID as either invalid, not available, or if the applicant name doesn’t match, the record is flagged as IDNC. |
| IDVS | ID Verification Sent | Central KYC Registry | Records where ID verification is sent to the issuing authority and awaiting response. |
| R | Reject | FI | Record rejected due to non-resolution of probable match by FI. |
| GK | Pending KYC Generation | Central KYC Registry | Interim status prior to KYC number getting generated. |
| KG | KYC Generated | Central KYC Registry | CKYC system will generate a unique KYC number. It can be generated after either ID confirmation or after the Data Matching Logic process for Low Risk. |

## User stories / User flow

Ops agent user flow:

- CKYC upload is completed by Decentro
- Ops agent visits Cersai dashboard (With role Institutional admin)
- Ops agent goes to Approval section under KYC
- Ops agent will be able to see all pending approvals for CKYC (They will pick the file with the latest date as per naming convention: (IN0531_11062018_RECON_1.2_00001_IA000763.txt)
- Once approved CKYC will be uploaded to Cersai

# **Design**

---

No design requirements

# **Analytics**

- CKYC status will be stored against each loan account and will have the following states:
    - Pending - When a loan account is created but CKYC upload is not initiated via CRON
    - Processing - When CKYC upload is initiated via CRON
    - Success - When GT status API is polled with zero pending cases and identifier is not recognised as failed
    - Failed - When GT status API returns individual identifier as failed
- Metrics to be tracked:
    - Total number of loans booked
    - Total number of loans booked and CKYC details uploaded
    - Number of loans with CKYC in process or pending
    - Number of loans with CKYC failed (Distributed with response keys as shared above)
- API hits to be logged covering request and response payloads including timestamps, error codes, response keys.
- Metrics to be tracked at a batch level.
    - Total number of records attempted
    - Total number of records updated successfully
    - Total number of records failed

Details to be tracked in the following windows:

(NBFC needs to report to CKYC within 10 days of account opening as per guidelines):

Number of loans booked in the last 3 days: N (Number of loans where CKYC upload is successful out of this cohort: M) M/N percentage

Number of loans booked in the last week: N2 (Number of loans where CKYC upload is successful out of this cohort M2) M2/N2 percentage

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

None

## Ops & Sales training

- Training for approving upload files on CERSAI
- Training for reviewing the logic

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

We will need to undertake the below activities post go-live.

- Analyze the error reasons
- Review the success rates
- Find corrective actions for major issues

---

# **Appendix**

## Meeting notes