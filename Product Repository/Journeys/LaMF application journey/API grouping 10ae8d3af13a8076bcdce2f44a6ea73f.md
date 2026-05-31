# API grouping

Sure! Below is a comprehensive list of all the APIs you've provided, organized into logical steps involved in the credit application process. I've included their descriptions and organized them into a table format that can be easily transferred to an Excel sheet. The total count of APIs is **112**.

### Step 1: Application Retrieval and Management

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 1 | `/app/borrower/application/{applicationId}` | GET | Retrieves application data using the application ID. |
| 1 | `/app/borrower/application/change/state/progress/{applicationId}/{currentStepId}` | GET | Updates the step state to 'in progress' for the given application. |
| 1 | `/app/borrower/application/override` | POST | Overrides application rules for exceptional cases. |
| 1 | `/app/borrower/application/stepper` | POST | Retrieves stepper data for the given application. |

### Step 2: KYC Additional Details

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 2 | `/app/borrower/application/additionalDetails/{applicationId}` | GET | Retrieves the list of additional KYC details present in the system. |
| 2 | `/app/borrower/application/additionalDetails/{applicationId}` | POST | Adds additional KYC details to the application. |

### Step 3: Agreement Processing

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 3 | `/app/borrower/application/agreement/link/{applicationId}` | GET | Retrieves the e-agreement setup link. |
| 3 | `/app/borrower/application/agreement/status/{applicationId}` | GET | Retrieves the agreement acceptance status. |
| 3 | `/app/borrower/application/agreement/stepper/{applicationId}` | GET | Retrieves agreement stepper information. |
| 3 | `/app/borrower/application/doc/digio/init/{applicationId}` | GET | Initiates a Digio e-sign request for the agreement. |
| 3 | `/app/borrower/application/doc/digio/status/{applicationId}` | GET | Checks the status of the Digio e-sign request. |
| 3 | `/app/borrower/application/doc/digio/status/deep/{applicationId}` | GET | Performs a deep status check of the Digio e-sign request. |
| 3 | `/app/borrower/application/signdesk/esign/init/{applicationId}` | GET | Initiates e-sign via SignDesk. |
| 3 | `/app/borrower/application/signdesk/esign/status/deep/{applicationId}` | GET | Checks SignDesk e-sign status in depth. |
| 3 | `/app/borrower/application/signdesk/esign/validate` | POST | Validates the SignDesk token. |

### Step 4: Loan Approval and Eligibility

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 4 | `/app/borrower/application/approval/check/{applicationId}` | GET | Retrieves loan approval status. |
| 4 | `/app/borrower/application/check/shallow/creditApproval/{applicationId}` | GET | Checks credit approval status for an application. |
| 4 | `/app/borrower/application/check/shallow/creditApproval/creditApproval/{applicationId}` | POST | Performs a shallow credit approval check. |
| 4 | `/app/borrower/application/checkCustomerEligibility/{applicationId}` | GET | Checks customer eligibility for the loan. |
| 4 | `/app/borrower/application/cibilCheck/{applicationId}` | GET | Checks the CIBIL score for the borrower. |
| 4 | `/app/borrower/application/ckyc/{applicationId}` | GET | Initiates CKYC for the application. |
| 4 | `/app/borrower/application/credit/profile/evaluate` | POST | Assigns a lender to the credit application. |
| 4 | `/app/borrower/application/find/credit/withoutCompletedApplication` | GET | Retrieves all credit applications without a completed application. |

### Step 5: KYC Verification

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 5 | `/app/borrower/application/kyc/pan/panVerify` | POST | Verifies the PAN with NSDL and retrieves the full name linked with PAN. |
| 5 | `/app/borrower/application/kyc/pan/panVerify/coborrower` | POST | Verifies the co-borrower's PAN with NSDL. |
| 5 | `/app/borrower/application/kyc/aadhaar/init` | POST | Initiates Aadhaar verification and sends OTP to the linked mobile number. |
| 5 | `/app/borrower/application/kyc/aadhaar/verify` | POST | Completes Aadhaar verification using the provided OTP. |
| 5 | `/app/borrower/application/kyc/photo/init` | POST | Generates a pre-signed link for uploading the borrower's photo. |
| 5 | `/app/borrower/application/kyc/photo/verify` | POST | Verifies the uploaded photo with KYC details. |
| 5 | `/app/borrower/application/kyc/summary/init/{applicationId}` | GET | Retrieves the KYC summary for the application. |
| 5 | `/app/borrower/application/kyc/summary/verify/{applicationId}` | GET | Confirms the KYC summary. |

### Step 6: KYC Document Upload and Validation

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 6 | `/app/borrower/application/kyc/document/{applicationId}` | POST | Retrieves URL to upload documents securely. |
| 6 | `/app/borrower/application/kyc/document/poa/{applicationId}` | POST | Retrieves URL to upload Proof of Address (PoA) documents. |
| 6 | `/app/borrower/application/kyc/document/poa/validate/{applicationId}` | GET | Validates uploaded PoA documents. |
| 6 | `/app/borrower/application/kyc/document/poi/{applicationId}` | POST | Retrieves URL to upload Proof of Identity (PoI) documents. |
| 6 | `/app/borrower/application/kyc/document/poi/validate/{applicationId}` | GET | Validates uploaded PoI documents. |
| 6 | `/app/borrower/application/kyc/document/validate/{applicationId}` | GET | Validates all uploaded documents. |
| 6 | `/app/borrower/application/kyc/documents/digilocker/init/{applicationId}` | POST | Initiates Digilocker KYC. |
| 6 | `/app/borrower/application/kyc/documents/digilocker/status/{applicationId}` | GET | Checks Digilocker KYC status. |
| 6 | `/app/borrower/application/kyc/documents/digio/init/{applicationId}` | GET | Initiates Digio KYC. |
| 6 | `/app/borrower/application/kyc/documents/digio/status/{applicationId}` | GET | Checks Digio KYC status. |

### Step 7: Bank Account Verification (BAV)

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 7 | `/app/borrower/application/bav/{applicationId}` | GET | Retrieves pre-fetched bank account details. |
| 7 | `/app/borrower/application/bav/add` | POST | Adds bank account details to the application. |
| 7 | `/app/borrower/application/bav/status/{applicationId}` | GET | Checks the status of a pending bank account verification. |
| 7 | `/app/borrower/application/bav/verify` | POST | Verifies bank account details. |

### Step 8: Asset Pledge Initiation and Verification

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 8 | `/app/borrower/application/asset/fetch/credentials` | POST | Retrieves credentials required for asset fetching. |
| 8 | `/app/borrower/application/asset/pledge/init/otp` | POST | Initiates OTP for asset pledge. |
| 8 | `/app/borrower/application/asset/pledge/v2/init/otp` | POST | Initiates OTP for asset pledge (Version 2). |
| 8 | `/app/borrower/application/asset/pledge/verify/otp` | POST | Verifies the OTP for asset pledge. |
| 8 | `/app/borrower/application/asset/pledge/activate/{applicationId}` | GET | Activates the asset pledge for the application. |
| 8 | `/app/borrower/application/asset/pledge/details/{applicationId}` | GET | Retrieves details of the pledged assets. |

### Step 9: Offer Selection

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 9 | `/app/borrower/application/offer/selection/init/{applicationId}` | GET | Retrieves the offer selection page for the application. |
| 9 | `/app/borrower/application/offer/selection/verify/{applicationId}` | GET | Confirms the selected offer for the application. |

### Step 10: Mandate Setup and Status

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 10 | `/app/borrower/application/mandate/link/{applicationId}` | GET | Retrieves the e-mandate setup link. |
| 10 | `/app/borrower/application/mandate/status/{applicationId}` | GET | Retrieves the e-mandate setup status. |
| 10 | `/app/borrower/application/mandate/digio/init/{applicationId}` | GET | Initiates a Digio mandate request. |
| 10 | `/app/borrower/application/mandate/digio/status/{applicationId}` | GET | Checks the status of the Digio mandate request. |
| 10 | `/app/borrower/application/mandate/digio/status/deep/{applicationId}` | GET | Performs a deep status check of the Digio mandate request. |
| 10 | `/app/borrower/application/mandate/digio/status/deep/v2/{applicationId}` | GET | Deep status check for Digio mandate (Version 2). |

### Step 11: Portfolio Fetch and Authentication

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 11 | `/app/borrower/application/fetch/init/otp/v3` | POST | Initiates portfolio fetch request and sends OTP for authentication. |
| 11 | `/app/borrower/application/fetch/authCAS/v2` | POST | Verifies the OTP and returns the mutual fund portfolio. |
| 11 | `/app/borrower/application/refreshPortfolioRequired/{applicationId}` | GET | Checks if a portfolio refresh is required. |

### Step 12: Pledge Processing

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 12 | `/app/borrower/application/pledge/init` | POST | Initiates the pledge process and sends OTP. |
| 12 | `/app/borrower/application/pledge/init/v3` | POST | Initiates the pledge process (Version 3). |
| 12 | `/app/borrower/application/pledge/create` | POST | Creates a pledge by accepting the portfolio and triggers OTP. |
| 12 | `/app/borrower/application/pledge/v2/create` | POST | Creates a pledge (Version 2). |
| 12 | `/app/borrower/application/pledge/authCAS` | POST | Verifies OTP and returns the mutual fund portfolio. |
| 12 | `/app/borrower/application/pledge/authPledge` | POST | Finalizes the pledge after OTP verification. |
| 12 | `/app/borrower/application/pledge/limit/{applicationId}` | GET | Retrieves eligibility based on selected portfolios. |
| 12 | `/app/borrower/application/pledge/processingCharges` | POST | Provides processing charges for selected portfolios. |
| 12 | `/app/borrower/application/pledge/save` | POST | Saves the portfolio preferences made by the user. |

### Step 13: Error Handling and Miscellaneous

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 13 | `/app/borrower/application/persist/mismatch/issue/{applicationId}` | GET | Persists name mismatch issues. |
| 13 | `/app/borrower/application/restart/failed/step/{applicationId}/{currentStepId}` | GET | Restarts a step after a failed review. |
| 13 | `/app/borrower/application/creditApplication/mismatch/appeal` | POST | Saves customer appeal for mismatch issues. |
| 13 | `/app/borrower/application/creditApplication/should/show/kycEdit/{applicationId}` | GET | Determines whether to show KYC edit option. |
| 13 | `/app/borrower/application/creditApplication/test/loan/create` | POST | Creates a test loan application. |
| 13 | `/app/borrower/application/review/kfs/init/{applicationId}` | GET | Initializes the Key Fact Statement (KFS) step. |
| 13 | `/app/borrower/application/review/kfs/link/{applicationId}` | GET | Retrieves the KFS link. |
| 13 | `/app/borrower/application/review/kfs/status/{applicationId}` | GET | Retrieves the KFS status. |
| 13 | `/app/borrower/application/review/kfs/accept` | POST | Accepts the KFS details. |
| 13 | `/app/borrower/application/routeConfig` | POST | Retrieves route configuration. |

### Step 14: Limit Management

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 14 | `/app/borrower/application/edit/limit/{applicationId}` | GET | Edits the limit for the application. |
| 14 | `/app/borrower/application/enable/edit/limit/{accountId}` | GET | Checks if limit editing is enabled for the account. |
| 14 | `/app/borrower/application/update/limit/{applicationId}` | GET | Initiates limit update for the application. |
| 14 | `/app/borrower/application/update/limit/allowed/{applicationId}` | GET | Checks if limit update is allowed for the application. |

### Step 15: Document Upload

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 15 | `/app/borrower/application/uploadDocuments/init` | POST | Initiates document upload process. |
| 15 | `/app/borrower/application/uploadDocuments/upload/{applicationId}` | POST | Uploads a document for the application. |
| 15 | `/app/borrower/application/uploadDocuments/verify/{applicationId}` | POST | Verifies the uploaded document. |
| 15 | `/app/borrower/application/uploadDocuments/submit` | POST | Submits all uploaded documents. |

### Step 16: Tata Mandate and Merger

| Step | API Endpoint | Method | Description |
| --- | --- | --- | --- |
| 16 | `/app/borrower/application/tata/mandate/link/` | POST | Retrieves the Tata mandate link. |
| 16 | `/app/borrower/application/tata/mandate/status/{applicationId}` | GET | Retrieves the Tata mandate status. |
| 16 | `/app/borrower/application/tata/mandate/status/v2/{applicationId}` | GET | Retrieves the Tata mandate status (Version 2). |
| 16 | `/app/borrower/application/tata/merger/enabled/{accountId}` | GET | Checks if the Tata merger is enabled for the account. |

---

**Total Count of APIs:** **112**

---

**Note:** You can transfer this table into an Excel spreadsheet by copying each section and pasting it into your Excel file. Each step corresponds to a logical grouping in the credit application process, helping to streamline development and integration efforts.