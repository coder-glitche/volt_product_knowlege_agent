# MNRL Compliance Validation Integration

: Mohit Pareek
Created time: April 17, 2026 7:17 AM
Status: Not started
Last edited: April 29, 2026 5:11 PM

# **What problem are we solving?**

---

- Currently, our system does not have a standardized mechanism to validate mobile numbers against authoritative revocation and risk datasets.
- This creates a gap where deactivated or reassigned numbers can still be used within onboarding and auth flows, leading to potential exposure of sensitive information (like OTPs) to unintended users.
- Additionally, numbers flagged by Department of Telecommunications (DoT) and Law Enforcement Agencies (LEAs) for fraud or non-compliance may remain undetected, increasing the platform’s exposure to fraud risk and regulatory non-compliance.

# **Why Now ?**

---

With the mandate issued by the Reserve Bank of India (RBI) on January 17 2025. Refer [DOC](https://www.pdicai.org/Docs/RBI-2024-25-105_1812025145839888.pdf) financial institutions are now required to verify customer mobile numbers against the Mobile Number Revocation List (MNRL) and take necessary actions.

> The Mobile Number Revocation List (MNRL), published by the Department of Telecommunications, provides a centralized dataset of such deactivated or flagged numbers.
> 

# **How do we measure success?**

---

- % of High-Risk Mobile Numbers Blocked Before Loan Creation
- % of blocked cases successfully reported to C-DOT
- % of users blocked due to MNRL match (where disconnectionreason_id = 3, 4 or 5) who are later not found in MNRL after reactivation-sync
- % of correctly removed records vs expected removals

# **What is the solution?**

---

- We propose implementing MNRL validation at two critical touchpoints in the user journey to ensure early risk detection and strict compliance at the point of loan creation.
- Currently, mobile numbers appear in the MNRL dataset for multiple reasons. As part of the implementation, users will be blocked from loan account creation only for specific high-risk categories, based on compliance requirements.

| disconnectionreason_id | disconnection_reason | Action |
| --- | --- | --- |
| 1 | Subscriber Verification Non-compliant Cases | Don’t Block |
| 2 | Disconnection due to Zero Usage or Non-payment | Don’t Block |
| 3 | LEAs Reported Cybercrime | Block |
| 4 | DoT Reported Fake or Forged Cases | Block |
| 5 | TSP Internal Analysis | Block |
| 6 | Others  | Don’t Block |

### **High Level Flow :**

1. **Daily MNRL Data Sync**
    - On initial setup, we will manually fetch MNRL data for the last 90 days, filter out reactivation cases, and store the final records in DB . Post launch, data will be fetched daily.
    - Then Fetch MNRL data daily from C-DOT Fetch APIs at 3 AM
    - Store all fetched records in our internal database (`mnrl_blocklist`)
2. **User Validation during Journey**
    - When a user starts their loan journey, validate their mobile number against the MNRL dataset (stored in our DB)
    - Perform checks at two critical touchpoints:
        - Create Opportunity
        - Submit Opportunity
        - Rationale for Touchpoint Selection
            
            **1. Create Opportunity**
            
            - Enables early detection of high-risk numbers using MNRL data
            - Allows upfront blocking of users before journey entry
            - Avoids unnecessary costs (Pledge Cost, downstream API calls)
            - Improves overall risk control by filtering invalid users at entry
            
            **2. Submit Opportunity**
            
            - As this is the final step before loan account creation, making it a critical compliance checkpoint
            - Ensures that no user with a revoked mobile number is allowed to proceed to loan account creation
            - Handles late-flagged users
            
3. **Blocking Logic** 
    - If the user’s mobile number exists in MNRL and matches the following disconnection reasons:
        - LEAs Reported Cybercrime (3)
        - DoT Reported Fake or Forged Cases (4)
        - TSP Internal Analysis (5)
    - Then block the user from proceeding further (prevent OpportunityID / LoanID creation)
        - [Refer](https://www.notion.so/volt-money/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?source=copy_link#348e8d3af13a802c99a5d3177a71982e) for error handling for LSPs
        - [Refer](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) for error handling for Volt
    - If no match is found → user continues the journey.
4. **Reactivation Handling**
    - C-DOT provides a list of reactivated numbers (previously present in MNRL but later restored).
    - Fetch reactivation data on the last day of every month at 03:00 AM
    - Match these numbers with our `mnrl_blocklist`
        - Remove matching records from the database.
        - Log all removed records for audit and traceability. [ Refer [datapoints](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) to log ]
5. **ATR (Action Taken Report) Reporting**
    - As per compliance,we need to report actions taken on MNRL-flagged numbers to C-DOT.
    - Aggregate all records where `is_blocked = TRUE`
    - Send ATR reports on the first day of every month at 03:00 AM using C-DOT ATR APIs. [ [Refer](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) ]

### **User Segmentation & Handling Strategy** :

| User Type | Description | Where to handle | Handling Strategy  |
| --- | --- | --- | --- |
| Users in the Journey
(Loan Account Not Created ) | Users who have initiated the journey but loan account is not yet created | 2 Touch Points - Mentioned Above  |  Refer Above Flow  |
| Users with Existing Loan Account | Users with an active loan account |  | Capture Quantum → Further action to be taken will be decided by Compliance team |

## Implementation Scope

### For  LSPs

- MNRL check will be handled by DSP no checks required from LSPs
- They only need to do the error handling for the rejection cases
- Request at Create Opportunity
    
    
    ```csharp
    curl --location '[https://api.staging.dspfin.com/los/api/v1/opportunity](https://api.staging.dspfin.com/los/api/v1/opportunity)' \
    {
    "pan": "EVIPM1670K",
    "product": "LAS",
    "opportunityType": "LOAN_CREATION",
    "phoneNumber": "9032390555",
    "email": "[vamshi8053@gmail.com](mailto:vamshi8053@gmail.com)"
    }'
    ```
    
- Response for failure
    
    ```csharp
    {
    "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK",
    "message": "User blacklisted due to MNRL check",
    "statusCode": "400"
    }
    ```
    
- Request at Submit Opportunity
    
    ```csharp
    curl --location '[https://api.staging.dspfin.com/los/api/v1/opportunity/OPP8724213445/submit](https://api.staging.dspfin.com/los/api/v1/opportunity/OPP8724213445/submit)' \
    {
    "submittedDataList": [
    {
    "dataType": "BANK_ACCOUNT",
    "referenceId": "URBANK4674555244"
    },
    {
    "dataType": "AGREEMENT",
    "referenceId": "URAGR5525242915"
    },
    {
    "dataType": "KFS",
    "referenceId": "URKFS1311438232"
    },
    {
    "dataType": "MANDATE",
    "referenceId": "URMNDT1155573314"
    },
    {
    "dataType": "ADDITIONAL_DATA",
    "referenceId": "URADDDATA4113361315"
    },
    {
    "dataType": "KYC",
    "referenceId": "URKYC3689753934"
    },
    {
    "dataType": "PHOTO_VERIFICATION",
    "referenceId": "URPHV1829553398"
    },
    {
    "dataType": "MOBILE_VERIFICATION_LOG",
    "referenceId": "URVERLOG4219785652"
    },
    {
    "dataType": "EMAIL_VERIFICATION_LOG",
    "referenceId": ""
    }
    ]
    }'
    ```
    
- Response for failure
    
    ```csharp
    {
    "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK",
    "message": "User blacklisted due to MNRL check",
    "statusCode": "400"
    }
    ```
    
- Updating LSQ
    
    We would need to create a new activity for LSQ events to handle MNRL rejected cases by adding 
    
    ```csharp
    {
    "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK",
    "message": "User blacklisted due to MNRL check",
    }
    ```
    

**~~User Experience**~~ 

- ~~Display a generic error message to the end user~~
- ~~Maintain consistent messaging across touchpoints~~

### Technical Implementation

#### 1. Setup with C-DOT

- We’ll share our server's public IP → C-DOT whitelists it
- C-DOT RSA public key : Get key [here](https://drive.google.com/drive/folders/1GIyQMkm7ZzkUIhsmozVXCnXKVQql8pxW?usp=sharing)
- We generate our own RSA key pair and share our public key with C-DOT (they use it to encrypt MNRL data responses)

#### 2. Fetching Data from C-DOT APIs

Scheduled at 03:00 AM daily to populate the internal DB

***NOTE** : C-DOT allows data to be fetched only for the last 90 days*

**1.  Authenticate to → Get Token

API :** [https://mnrlbankapitestgateway.sancharsaathi.gov.in/mnrlbankapi/v2/auth](https://mnrlbankapitestgateway.sancharsaathi.gov.in/mnrlbankapi/v2/auth)

- Encrypt {email, password} using AES-256-GCM + RSA-OAEP (using C-DOT's RSA public key)
- POST to `/mnrlbankapi/v2/auth`
- After creds verification a token will be provided will be used for fetching
    - Response :  `{"token": "token_value"}` - valid for **120 minutes**

```
Request:  POST /mnrlbankapi/v2/auth
Body After Encryption : { encryptedKey, encryptedData, authTag, nonce }
Response: { token: "abc123" }
```

**2. Get Count for any date** 

- POST to `/mnrlbankapi/v2/count`
- Response tells us total entries available for that date
- This will be a plaintext request (no encryption needed)

```
Request:  POST /mnrlbankapi/v2/count
Body:     { "date": "2025-04-15" }
Response: { "date": "2025-04-15", "count": 41630 }
```

- Response for failure cases
    
    ```
    HTTP/1.1 xxx
    {
      "response_code": "xxx",
      "message": "Reason for failure"
    }
    ```
    
    Refer : [Table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) for response_code Mapping 
    

**3. Fetch MNRL Data in Batches :**

- POST to `/mnrlbankapi/v2/mnrldata`
- Max 3000 entries per request, max 120 requests per 10 minutes
- Each response is encrypted - we need to decrypt it

```
Request 1:  { date, BankId, offset: 0,count: 3000 }
Request 2:  { date, BankId, offset: 3000, count: 3000 }
Request 3:  { date, BankId, offset: 6000, count: 3000 }
```

- The date (in `YYYY-MM-DD` format) - specifies the day for which data is to be fetched
- Count : # of records to be fetched in a single request.

**4. Decrypt Each Response**

```
Step A: Our RSA private key → decrypt encryptedKey → get decrypted AES key
Step B: Use AES key + nonce + authTag → decrypt encryptedData → get MNRL records
```

- Decrypted data response : Refer this [table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) for parameters understanding
    
    ```json
    {
      "data": [
        {
          "mobile_no": "9858578541",
          "lsa_id": "9",
          "tsp_id": "4",
          "date_of_disconnection": "2025-04-14",
          "disconnectionreason_id": "3"
        },
      ]
    }
    ```
    
- **5. Store in our DB [ mnrl_blocklist ]**
    
    
    | Field Name | Description | Logic to Store in DB |  |
    | --- | --- | --- | --- |
    | mobile_number | User’s mobile number (Primary Identifier) | Take from `/mnrlbankapi/v2/mnrldata`  endpoint response  |  |
    | pan  | User’s PAN number  |  |  |
    | lsa_name | Licensed Service Area ID | Map lsa_id from response with this [table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) and store lsa_name [ Ex : Assam ] |  |
    | tsp_name | Telecom Service Provider ID | Map tsp_id from response with this [table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) and store tsp_name |  |
    | date_of_disconnection | Date when number was disconnected | Take from `/mnrlbankapi/v2/mnrldata`  endpoint response  |  |
    | disconnection_reason_id | Reason code for disconnection | Take from `/mnrlbankapi/v2/mnrldata`  endpoint response  |  |
    | disconnection_reason | Reason for disconnection | Map disconnectionreason_idfrom response with this [table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21) and store disconnection_reason |  |
    | sourcing_channel  |  |  |  |
    | created_at | Record creation timestamp |  |  |
    | is_blocked  | This will help us know did we blocked a user due to MNRL check [ where disconnectionreason_id   = 3, 4 or 5] | True if Match Found else False  |  |
    | investigation_details | Remark
    on action  | We can mention Blacklisted User |  |
    | action_taken_id | ID against taken action | Will be kept constant as 4 (Others).
    
    As it is the closest matching action from the defined mapping [table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21). |  |
    | grievance_received | Yes or No  | Yes or No |  |

### **3. Reactivation Handling**

**What is Reactivation ?**

Reactivation refers to mobile numbers that were previously marked as deactivated (present in MNRL) but are later restored by telecom operators before the 90-day window due to customer requests or grievance resolution. 

- Possible Reasons for reactivating numbers
    
    
    | Reactivation ID | Reactivation Reason |
    | --- | --- |
    | 1 | Reactivation to same customer due to late reverification |
    | 2 | Activation after returning from MNP |
    | 3 | Reactivation to same customer due to grievance |
    | 4 | Reactivation to same customer due to request from LEA/DoT |
    | 5 | Reactivation to other customer due to other reason |

**Why Reactivation Handling is Required ?**

- Prevents false positives (blocking genuine users)
- Aligns with regulatory expectations of maintaining updated user status

Without this, users whose numbers are removed from MNRL Revoked List may continue to be incorrectly blocked.

### **Flow -**

```
Cron Runs Monthly [ Last Day of Month at 3 AM ] 
        ↓
Fetch Reactivated Numbers from C-DOT API for the month
        ↓
Decrypt Response
        ↓
Match with mnrl_blocklist [ Our DB ]
        ↓
Remove matching numbers from our DB
        ↓
Log removed entries for audit / traceability 
        ↓
Updated DB reflects only valid blocked numbers
```

**Rationale for Monthly Reactivation Sync** 

- Reactivation is a **l**ow-frequency event compared to MNRL additions
- Reduces unnecessary API calls and processing overhead

#### **Reactivation API Integration**

**Endpoint Details**

| API | Endpoint | Purpose | Encryption |
| --- | --- | --- | --- |
| Count API | `/mnrlbankreactivatedapi/v2/count` | Get total reactivated records for a date | No |
| Fetch API | `/mnrlbankreactivatedapi/v2/reactivated` | Fetch reactivated numbers | Response: Yes |
|  |  |  |  |

#### **1. Get Reactivated Count**

**Request**

```json
{
  "date": "2025-04-15"
}
```

**Response**

```json
{
  "date": "2025-04-15",
  "count": 1200
}
```

#### **2. Fetch Reactivated Numbers**

- **Request**
    
    ```json
    POST /mnrlbankreactivatedapi/v2/reactivated
    
    {
      "date": "2025-04-15",
      "BankId": "BANK123",
      "offset": 0,
      "count": 3000 
    }
    ```
    
- **Response (Encrypted)**
    
    ```json
    {
      "encryptedKey": " ",
      "encryptedData": " ",
      "authTag": " ",
      "nonce": " "
    }
    ```
    
- **Decrypted Output**
    
    ```json
    
    {
      "data": [
        {
          "mobile_no": "1234567890",
          "date_of_reactivation": "2025-02-03",
          "reactivation_id": "1"
        }
      ]
    }
    ```
    
- **Response Parameter Deatils**
    
    
    | S. No. | Key | Sample | Length & Format |
    | --- | --- | --- | --- |
    | 1 | mobile_no | "1234567890" | 10-character numeric string (digits only) |
    | 2 | date_of_reactivation | "2025-02-03" | Format: YYYY-MM-DD |
    | 3 | reactivation_id | "1" | 1-digit string (mapped to reactivation reason [table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21)) |

### **4. ATR Reporting Strategy**

**What is ATR?**

ATR (Action Taken Report) is a mandatory requirement where financial institutions report actions taken on MNRL-flagged numbers to Centre for Development of Telematics.

**Approach**

- ATR will be batched and reported on the first day of every month at 3 AM, covering only those cases where an action has been taken on MNRL-flagged numbers.
- For our use case, we will only be reporting `action_id = 4 (Others)` as it is the only applicable category in our integration scope.
- Refer Action Taken Mapping [table](https://app.notion.com/p/PRD-Mobile-Number-Revocation-List-343e8d3af13a80749df1c66cac2d83af?pvs=21)

#### **ATR Implementation**

### **Flow**

```
User Blocked Due to ( disconnectionreason_id = 3, 4 or 5 )
        ↓
Aggregate all blocked cases ( where is_blocked = TRUE )
        ↓
Monthly Job Trigger
        ↓
Encrypt ATR payload
        ↓
Send to C-DOT ATR API
```

- **ATR API Request**
    - **Note:** `bank_id` is mandatory and provided by C-DOT. Keep it configurable (not hardcoded), it is expected to remain static but may change in future.
    
    **Endpoint :** `POST /mnrlbankapiatr/v2/atr`
    
    **Request Body (Before Encryption)**
    
    ```json
    {
      "bank_id": "1234567890",
      "atr_data": [
        {
          "mobile_no": "1234567890",
          "action_taken": "1",
          "investigation_details": "Profile made inactive",
          "date_of_action": "yyyy-mm-dd hh:mm:ss",
          "disconnection_reason_id": "4",
          "grievance_received": "No"
        }
      ]
    }
    ```
    
    This request needs to be encrypted and shared. 
    
    - **Refer ATR Request Parameters**
        
        
        | S.No | Key | Data Type | Sample Value | Length / Format | Description |
        | --- | --- | --- | --- | --- | --- |
        | 1 | mobile_no | String | "1234567890" / "911234567890" | 10 or 12 chars | Numeric string only. Can be 10-digit or 12-digit with `91` country prefix |
        | 2 | date_of_action | String | "2025-02-03 11:43:56" | YYYY-MM-DD HH:MM:SS | Timestamp of the action performed |
        | 3 | action_taken | String | "1" | 1-digit string | Code representing action taken (mapped in reference table) |
        | 4 | investigation_details | String | "Profile made Inactive" | Max 250 chars | Remarks or explanation for the action taken |
        | 5 | grievance_received | String | "Yes" / "No" | ("Yes","No") | Indicates whether grievance was received |
        | 6 | disconnection_reason_id | String | "3" | 1-digit string | Reason code for disconnection (mapped in reference table ) |
        | 7 | bank_id | String  |  |  | C-DOT has provided this |
- **ATR Response Handling**
    - Sample Response
        
        {
        "response_code": "422",
        "RequestId": "1234567890",
        "message": "Partial Success, some entries are rejected",
        "ErrorIn": {
        "12345678x0": "invalid mobile_no format (must be 10 digits)",
        "1234567891": "invalid action_taken code"
        }
        }
        
    - We would need to persist all partial failure cases against the corresponding RequestId for traceability, and audit purposes.
    - HTTP 200 can still contain:
        - Success
        - Partial success (validation-level rejection)
    - ErrorIn contains:
        - Key = input identifier ( like - mobile number)
        - Value = validation error message
    - Non-200 HTTP status indicates system-level failure

### For VOLT

#### **Volt-Specific User Journey Handling**

From Volt’s perspective, only error handling is required. MNRL validation is handled by DSP.

- If DSP returns a rejection in `Create Opportunity` or `Submit Opportunity` with `ErrorCode": "USER_BLACKLISTED_MNRL_CHECK"`
- Display a blocking card with message displayed to user [ Figma Link Added Below ]

> *We are unable to process your application as it does not meet the lender’s eligibility criteria*
> 
- AppsSmith Task
    - Update AppsSmith Remarks Field : User Blacklisted due to MNRL check [{{ disconnection_reason}}]
1. **~~At Create Opportunity~~**
    - ~~Perform MNRL check~~
    - ~~If match found:~~
        - ~~Block user immediately - prevent OpportunityID creation~~
        - ~~Display a blocking card post validation~~
2. **~~At Submit Opportunity~~**
    - ~~Perform final MNRL check~~
    - ~~If match found:~~
        - ~~Prevent LoanID creation~~
        - ~~Display the same blocking card~~

### **Design**

---

Figma [Link](https://www.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-Ad-Hoc-tasks?node-id=1278-317&t=6ivOTRkv8vVSgazs-11)

# Tables :

### Error Code Table

| S. No. | response_code  | HTTP Code | Message |
| --- | --- | --- | --- |
| 1 | 442 | 200 | Date format incorrect / Missing |
| 2 | 402 | 422 | Date is older than 90 days from current date |
| 3 | 422 | 200 | INVALID JSON INPUT / PARAMETER MISSING / DECRYPTION FAILED / NO ACCOUNT FOUND / INCORRECT PASSWORD |
| 4 | 401 | 200 | Bank ID mismatch |
| 5 | 403 | - | Unauthorized / Expired / Invalid Token |
| 6 | 422 | 200 | Partial Success in ATR |
| 7 | 429 | 429 | Too Many Attempts |
| 9 | 405  | 405 | Method Not Allowed |

### Response Parameters Detail Table

| S. No. | Key | Data Type | Sample | Length and Format |
| --- | --- | --- | --- | --- |
| 1 | mobile_no | String | "1234567890" | 10-character numeric string (digits only) |
| 2 | lsa_id | String | "3" | 1 or 2 character numeric string |
| 3 | tsp_id | String | "4" | 1 or 2 character numeric string |
| 4 | date_of_disconnection | String | "2025-02-03" | Date format (YYYY-MM-DD) |
| 5 | disconnection_reason_id | String | "1" | 1-digit string (reason mapping provided in another table) |

### LSA Mapping

| lsa_id | lsa_code  | lsa_name |
| --- | --- | --- |
| 1 | AP | Andhra Pradesh |
| 2 | AS | Assam |
| 3 | BR | Bihar |
| 4 | DL | Delhi |
| 5 | GJ | Gujarat |
| 6 | HP | Himachal Pradesh |
| 7 | HR | Haryana |
| 8 | JK | Jammu & Kashmir |
| 9 | KA | Karnataka |
| 10 | KL | Kerala |
| 11 | KO | Kolkata |
| 12 | MH | Maharashtra |
| 13 | MP | Madhya Pradesh |
| 14 | MU | Mumbai |
| 15 | NE | Northeast |
| 16 | OR | Orissa |
| 17 | PB | Punjab |
| 18 | RJ | Rajasthan |
| 19 | TN | Tamil Nadu |
| 20 | UE | Uttar Pradesh (East) |
| 21 | UW | Uttar Pradesh (West) |
| 22 | WB | West Bengal |

### TSP Mapping

| tsp_id | tsp_name |
| --- | --- |
| 1 | TTL |
| 2 | BSNL |
| 3 | RCOM |
| 4 | RJIL |
| 5 | VMIPL |
| 6 | QTL |
| 7 | VIL |
| 8 | BAL |
| 9 | MTNL |

### Disconnection Mapping

| disconnectionreason_id | disconnection_reason |
| --- | --- |
| 1 | Subscriber Verification Non-compliant Cases |
| 2 | Disconnection due to Zero Usage or Non-payment |
| 3 | LEAs Reported Cybercrime |
| 4 | DoT Reported Fake or Forged Cases |
| 5 | TSP Internal Analysis |
| 6 | Others  |

### Reactivation Mapping

| reactivation_id | reactivation_reason |
| --- | --- |
| 1 | Reactivation to same customer due to late reverification |
| 2 | Activation after returning from MNP |
| 3 | Reactivation to same customer due to grievance |
| 4 | Reactivation to same customer due to request from LEA/DoT |
| 5 | Reactivation to other customer due to other reason |

### Action taken Reason Mapping

| Code | Action Reason |
| --- | --- |
| 1 | Bank/Wallet Account Frozen |
| 2 | Debit/Credit Restrictions on Account |
| 3 | Bank/Wallet Account found Compliant |
| 4 | Others |

# **Analytics**

---

# **Timeline/Release Planning**

**NOTE** : 

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

How we’ll monitor that error is not leading to support tickets ?

1. Show general error at create opp and submit opp
2. Monitor Blocked Cases
3. If Blocked Cases -> leads to support tickets 
    1. and if support ticket/ blocked cases > 50%  - Optimize Error Handling