# External reporting requirements

: Vaibhav Arora
Created time: September 19, 2024 1:01 AM
Status: Done
Last edited: November 15, 2024 3:03 PM
Owner: Vaibhav Arora

# **Why are we doing this?**

RBI has mandated that all lenders report to entities  to maintain transparency, ensure accountability, and facilitate better credit management in the financial ecosystem.

CICs (like Experian, CIBIL, Equifax, etc.) collect and maintain credit information of individuals and businesses.

**Source of Reporting:**

- Credit Assessment: Reporting to **CICs** helps build credit histories, which are crucial for evaluating the creditworthiness of borrowers.
- **NeSL** is India's first Information Utility under the Insolvency and Bankruptcy Code (IBC) 2016. It stores financial information, primarily related to loan agreements and debt defaults.
- **CKYC** is a centralized repository for Know Your Customer (KYC) records, managed by the Central Registry of Securitisation Asset Reconstruction and Security Interest (CERSAI).

**Reason for Reporting**:

- **Regulatory Compliance**: NBFCs are required to report financial contracts and default information to NeSL as per IBC regulations.
- **Debt Resolution**: NeSL facilitates faster insolvency resolution by ensuring that loan agreements are readily available for legal proceedings if needed.
- **Customer Identification**: NBFCs must report customer identification details to the CKYC to prevent duplication of KYC records and maintain a unified KYC process across all financial institutions.

---

# **How do we measure success?**

- Man-Hours for CKYC Upload Process Management to not exceed more than 20 hours
- Success rate for CKYC upload/update > 95% (Accuracy of uploaded data)
- CKYC upload confirmation must be received within 12 hours (Upload → Response → Reconciliation)
- 100% of CKYC uploads should meet the regulatory deadline (10 days from account opening).
- Success rate for Bureau upload> 98%
- Bureau reporting should be completed within 5 days of the reporting period 

(Bureau reporting needs to be done within 7 days of the subsequent month) reporting period becomes last date of the effective month, success criteria becomes till the 5th of the next month (till January 2025) - Post which we will have to report bi- weekly and reporting dates would become 20th of existing month and 5th of next month)
- 100% of NeSL reporting should be completed within 30 days of issuance or 7 days of default (15th November)
- Monthly man-hours for managing NeSL submissions should be under 20 hours.
- Error rate for rejected NeSL submissions should be under 1%.

---

# **How are others solving this problem?**

- Integrating Loan Origination Systems (LOS) and Loan Management Systems (LMS) with CKYC, CICs, and NeSL through APIs
- Building middleware themselves to transform raw data from internal systems into formats that align with the specific requirements of CKYC, bureaus, and NeSL.
- Several NBFCs rely on third-party service providers specializing in regulatory compliance and reporting, such as Perfios or Karza Technologies. These vendors manage CKYC, bureau, and NeSL reporting by handling data transformation, submission, and error reconciliation on behalf of the NBFCs.

**Common challenges in the industry:**

1. **Error in Data Formats:**
    - **Solution:** Automated pre-validation tools to ensure that data aligns with required formats before submission.
2. **Manual Process Dependency:**
    - **Solution:** Automation of data collection and submission processes to reduce the need for manual intervention.
3. **High Rejection Rates:**
    - **Solution:** Error-handling mechanisms and robust reconciliation processes to quickly identify and rectify issues.

---

# **What is the solution?**

**CKYC update and upload**

We will be integrating with CKYC provider which will help us automate the [process of SFTP upload](CKYC%20Upload%20for%20DSP%201433e0160911411981171e2d7d788b91.md)  for the NBFC. 

**CIC**

We will get Finflux to create a pre-built report for us, which can be converted into TUDF format and directly uploaded to different SFTPs and ST clients of CICs for batch processing

**NeSL:**

We will get Finflux to create a custom report for us, which can be uploaded to NeSL’s website on a weekly and a monthly frequency

(Note: We will create automated emails to Ops, with the reports so that they a respective ticket is created for them to complete the task for V1

We will automate the complete uploading of files to the external agencies in v2 (Post we have confidence in data generation and upload across workflows and systems)

## Requirements overview (optional)

## User stories / User flow

High level CKYC upload flow:

![image.png](External%20reporting%20requirements/image.png)

[https://claude.site/artifacts/209abfa0-a0b6-43cb-b8c1-b77726a4cb27](https://claude.site/artifacts/209abfa0-a0b6-43cb-b8c1-b77726a4cb27)

Bureau reporting workflow:

![image.png](External%20reporting%20requirements/image%201.png)

NeSL reporting workflow:

![image.png](External%20reporting%20requirements/image%202.png)

## Requirements:

### CKYC reporting

CKYC, or Central KYC (Know Your Customer), is a centralized registry in India where personal information related to identity verification is stored. When someone opens a new account with a bank or any financial institution, they typically need to submit documents to prove who they are (this process is called KYC)

Instead of submitting these documents every time, CKYC stores this information in one place. Once your details are registered with CKYC, any financial institution can access your information from the database, making the process faster and reducing the need for repetitive documentation. Essentially, CKYC streamlines the KYC process across different institutions.

**Given our CKYC requirements we can use the following ways to achieve CKYC reporting:**

| **Consideration** | **Description** | **Manual upload via Cersai dashboard** | **Bulk upload via CKYC** | **Third party integration** |
| --- | --- | --- | --- | --- |
| Frequency | CKYC upload needs to be done within 10 days of account opening for every customer onboarded | Easier if count of transactions are less but would become a bottleneck as we scale | Harder to do on a set frequency however easier if number of applications are high per cycle in setfrequency | **Easiest once set up, does not require recurring effort** |
| Set up | Effort to set up the requirements to handle upload and update capabilities | **Low** | High | Medium |
| Cost | Cost per upload | **Low (10 paisa)** | **Low (10 paisa)** | High (2-3 Rs per upload/ update) |
| Accuracy | Accuracy of upload | Low (Required individual effort for each account) | Medium (Processes can be sent to bulk upload reducing the error proneness marginally) | **High ((Automated processes where data is passed via system directly)** |
| Operational effort per transaction | - | High (Requires effort for each account - Upload + Approval) | Medium (Requires effort for each batch - Upload + Approval) | **Low (Requires effort for each batch - Approval)** |
| Scalability | - | Low | Medium | **High (Cost may become a factor as we scale, can build own systems to subside the same)** |

**Quick comparison of different vendors for CKYC:**

| **Consideration** | **Description** | **Decentro** | **HyperVerge** | **Syntizen** | **Judgment** |
| --- | --- | --- | --- | --- | --- |
| Coverage of Use Cases | The range of CKYC operations supported by the API | CKYC Search, Download, Upload (individuals), Bulk upload | CKYC PreUpload (configuration), Upload (individuals), Bulk upload | CKYC Search, Upload (Create Customer), Customer file upload, 
**Reconcilation flows via dashboard** | Syntizen |
| API Design | The structure and design principles of the API | **RESTful API with standard HTTP methods, JSON format** | **RESTful API with standard HTTP methods, JSON format** | RESTful API with POST method only, JSON format | Tie: Decentro & HyperVerge |
| Ease of Integration | How easily the API can be integrated into existing systems | Clean API design, query parameters for options, OCR support | Detailed input parameters, webhook support for async processing | **Existing integration between Finflux and Syntizen** | Syntizen |
| Error Handling | How errors are communicated and managed | Detailed response keys and descriptions | Detailed error codes and messages, callback request body samples | Detailed error codes and messages | Tie: All three |
| Additional Features | Unique or standout features offered by each vendor | **OCR support for CKYC documents, utility APIs (e.g., Form 60 handling)** | Configuration setup via PreUpload API, detailed callback mechanisms | **Separate API for document upload, detailed input validation rules** | Tie: Decentro & Syntizen |
| Input Validation | How the API validates and handles input data | Standard input validation (implied from docs) | Comprehensive input validation rules | **Detailed special character and input validation rules** | Syntizen |
| API Versioning | How different versions of the API are handled | Not explicitly mentioned in provided docs | Not explicitly mentioned in provided docs | Not explicitly mentioned in provided docs | Tie: No clear winner |
| **Cost** | **-** | **To be checked** | **To be checked** | **To be checked** | **To be checked** |
| Implementation effort | - | Low | Low | NA - Existing integration | Syntizen |

**Documentations:**

[CKYC DOCUMENTATION – Syntizen Technologies.pdf](External%20reporting%20requirements/CKYC_DOCUMENTATION__Syntizen_Technologies.pdf)

[CKYC Download.pdf](External%20reporting%20requirements/CKYC_Download.pdf)

[CKYC PreUpload API _ HyperVerge.pdf](External%20reporting%20requirements/CKYC_PreUpload_API___HyperVerge.pdf)

[CKYC Search.pdf](External%20reporting%20requirements/CKYC_Search.pdf)

[CKYC Upload (Individuals).pdf](External%20reporting%20requirements/CKYC_Upload_(Individuals).pdf)

[Create Customer – Syntizen Technologies.pdf](External%20reporting%20requirements/Create_Customer__Syntizen_Technologies.pdf)

[Customer reconcilation – Syntizen Technologies.pdf](External%20reporting%20requirements/Customer_reconcilation__Syntizen_Technologies.pdf)

[Hyperverge CKYC documentation.pdf](External%20reporting%20requirements/Hyperverge_CKYC_documentation.pdf)

[Login – Syntizen Technologies.pdf](External%20reporting%20requirements/Login__Syntizen_Technologies.pdf)

Syntizen is a clear winner since it involves no effort from a integration POV and all details which are already being stored in Finflux can be directly utilised by Syntizen to process batch upload for CKYC reporting

**High level flow:**

![image.png](External%20reporting%20requirements/image%203.png)

**Parameters to be saved in passed in CKYC and their respective storage in Finflux (only mandatory fields for individual reporting):**

| **Parameter** | **Mandatory (Yes/No)** | **Value** | **Value type** | **To be passed** | **In finflux** |
| --- | --- | --- | --- | --- | --- |
| Constitution Type | M | For Individuals we can hard code if Type is not avilable in NEO DB | Static | Yes | NA |
| Account type | M | 01-Normal,04 - OTP Based E-KYC ,05 - Minor--- | Static | Yes | NA |
| Applicant Name Prefix | M | Mr,Mrs,Mis,Dr,Minor | Dynamic | Yes | Yes |
| Applicant First Name | M |  | Dynamic | Yes | Yes |
| **Flag indicating Father or Spouse Name** | **M/O** | Any of the father,Spouse or Mother's name is manadatory | Static | Yes | No |
| Applicant Father/Spouse Name Prefix | M/O |  | Dynamic | Yes | Yes |
| Father / Spouse First Name | M/O |  | Dynamic | Yes | Yes |
| Gender | M | ‘M’ – Male, ‘F’ – Female, 'T'- Transgender | Dynamic | Yes | Yes |
| Date of Birth | M | DD-MM-YYYY | Dynamic | Yes | Yes |
| PAN or form 60 | M | PAN Number(5alphabets+4numbers+1alphabet) | Dynamic | Yes | Yes |
| Address  Line 1 | M |  | Dynamic | Yes | Yes |
| Address -  District | M | api wil retrun failure of cusotmer insertion if the value givne is not part of the master | Dynamic | Yes | Yes |
| Address - State/ U.T | M | Refer the state master for codes | Dynamic | Yes | Yes |
| Address  - Country | M | Refere country master for codes | Dynamic | Yes | Yes |
| Address -  PIN Code | M | api wil retrun failure of cusotmer insertion if the value givne is not part of the master | Dynamic | Yes | Yes |
| Proof of Address submitted for Proof of Identity and Address | M | Refere proof of Address master for passing code(should eb able to pass more than one code) | Dynamic | Yes | Yes |
| **POI & POA ID number** | **M** | **should be able to pass more than one ID number** | **Dynamic** | **Yes** | **Not sure (Aadhaar last 4 digits)** |
| Flag indicating if Proof of Identity and Address is same as current Address | M | Y/N | Static | Yes | NA |
| Current Address Line 1 | M |  | Dynamic | Yes | Yes |
| Current Address -  City / Town / Village | M |  | Dynamic | Yes | Yes |
| Current Address -  District | M |  | Dynamic | Yes | Yes |
| Current Address - Country | M |  | Dynamic | Yes | Yes |
| Current Address -  PIN Code Local Address Pin code | M |  | Dynamic | Yes | Yes |
| Proof of address submitted for Current Address | M |  | Dynamic | Yes | Yes |
| Mobile No. (ISD Code) | M |  | Dynamic | Yes | Yes |
| Mobile No. | M |  | Dynamic | Yes | Yes |
| Date of Declaration | M | DD-MM-YYYY | Dynamic | Yes | Yes |
| Place of Declaration | M |  | Dynamic | Yes | Yes |
| KYC Verification Date | M | DD-MM-YYYY | Dynamic | Yes | Yes |
| Type of Document Submitted | M | 01- Certified Copies02 - E-KYC data received from UIDAI03 - Data received from offline verification04 - Digital KYC process05 - Equivalent e-document06- Video-based KYC | Static | Yes | Yes |
| KYC Verification Name | M | Details for Employeed who performed KYC | Static | Yes | Yes |
| KYC Verification Designation | M | Details for Employeed who performed KYC | Static | Yes | Yes |
| KYC Verification Branch | M | Veriifcation Brach Code assigned by CKYCR | Static | Yes | Yes |
| KYC Verification EMP code | M | Details for Employeed who performed KYC | Static | Yes | Yes |
| Organisation Name | M | Name of the organisation | Static | Yes | Yes |
| Organisation Code | M | Institution Code assigned by CKYCR | Static | Yes | Yes |
| ID Documents code | M | Refer Document codes master for code, shoud be able to pass more than one code | Dynamic | Yes | Yes |
| ID Documents | M | pdf,tiff,JPG,JPEG and less than or equal to 350 KB. Shoudl be able to able to pass more than one document | Dynamic | Yes | Yes |
| Aadhaar photo |  |  |  |  |  |

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

**Cersai dashboard approval workflow:**

Maker and Checker can view and download response of each uploaded batch after checker approval.
User needs to follow following steps to download bulk upload response file:

1. Click on “Bulk Upload Response” link under KYC Management.
2. Click on “SUBMIT” after providing start and end date.

![image.png](External%20reporting%20requirements/image%204.png)

**Response parameters and handling (Post approval):**

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

### CIC reporting

CIC, or Credit Information Company, is an organization that collects and maintains records of an individual's or company's credit information. In India, 

there are four main CICs to which reporting is mandated:

- CIBIL TU
- Equifax
- Experian
- CRIF High Mark

CICs gather credit-related data from various financial institutions and create comprehensive credit reports and scores. These reports are used by lenders to assess the creditworthiness of potential borrowers.

| **Consideration** | **Description** | **Bulk upload via to SFTP and ST clients** | **Third party integration** |
| --- | --- | --- | --- |
| Frequency | CIC reporting needs to be done on a bi-monthly level for all loan accounts  | Easier to implement and since the frequency is fixed, can be achieve | Automated by the vendor (Directly consumes information) |
| Set up | Effort to set up the requirements to handle upload and update capabilities (OML) | **Low** | Medium |
| Cost | Cost per upload | NA | **Set up and AMC:**
 ₹5,000 - ₹15,000 per month
**Per-record fee:** ₹2 - ₹10 per record |
| Accuracy | Accuracy of upload | Low (Required individual effort for each bulk upload) | High ((Automated processes where data is passed via system directly) |
| Operational effort per transaction | - | Medium (Requires effort for each bulk upload | Low (Requires effort for each batch - Approval) |
| Scalability | - | **Medium** | Low (Cost may become a factor as we scale, can build own systems to subside the same) |

There are no strong contenders that support CIC reporting and since the cyclical nature of reporting for CICs, can be handled via bulk uploads to different CICs.

 

### **Steps to upload to CRIF**

- Generate the reporting Excel file from the LMS.
- Fill in all mandatory fields in the Excel file (highlighted in red).
- Convert the Excel file to the required text format:
a. Copy specific columns (first 3 and last) from each sheet to the sorting sheet.
b. Sort the data in the sorting sheet by Account Number and Flag.
c. Add Header (HD) and Trailer (TS) segment data.
d. Copy the sorted data into a notepad file.
- Save the notepad file with an appropriate name (e.g., member ID).
- Log in to the CRIF SFTP portal.
- Navigate to the correct folder for upload (Bureau Data Submission > Prod Data > Consumer/MFI/Commercial).
- Select the submission frequency (Daily, Weekly, or Monthly).
- Upload the file using the File > Upload option or drag and drop.
- Send an intimation email to the appropriate CRIF support email.

Guide document:

[MFI TRAINING STEPS TO UPLOAD DATA.docx](External%20reporting%20requirements/MFI_TRAINING_STEPS_TO_UPLOAD_DATA.docx)

[steps to convert excel to text.docx](External%20reporting%20requirements/steps_to_convert_excel_to_text.docx)

[CONSUMER TRAINING STEPS TO UPLOAD DATA.docx](External%20reporting%20requirements/CONSUMER_TRAINING_STEPS_TO_UPLOAD_DATA.docx)

### **Steps to upload to Experian**

- Obtain STS ID from Experian (one-time setup):
a. Provide a company domain email address to Experian.
b. Receive 3 automated emails from [Expadmin@experian.com](mailto:Expadmin@experian.com).
c. Click on the registration link (accessible only once in a browser).
d. Set up a new password and security questions.
e. Agree to terms and conditions and complete registration.
- Generate the reporting file from the LMS.
- Log in to the Experian STS portal:
a. Access [https://data.experian.in](https://data.experian.in/).
b. Enter STS ID and password.
c. Answer one of the security questions set during registration.
- Navigate to the correct folder for upload:
a. Select the "To_xpn" folder for sharing data with Experian.
- Set the correct transfer mode:
a. For text, ASC, PRN, and CSV files: Select ASCII Mode.
b. For ZIP, PGP, GPG, Excel, MDB, DBF, and TRS files: Select Binary Mode.
- Upload the file.
- Verify successful upload in the Upload monitor.
    
    [Experian_Bureau_Guide_STS-ID-Creation_Usage_22.pdf](External%20reporting%20requirements/Experian_Bureau_Guide_STS-ID-Creation_Usage_22.pdf)
    

### **Steps to upload to CIBIL**

- Generate the reporting file from the LMS.
- Set up SFTP access (one-time setup):
a. Whitelist CIBIL's SFTP URL ([https://tuftp.cibil.com](https://tuftp.cibil.com/)) or IP (103.225.112.95).
b. Provide your source server's public IP to CIBIL.
c. Generate and share your public SSH key with CIBIL.
d. Receive SFTP credentials from CIBIL.
- Configure environment variables:
a. Set CIBIL_SFTP_USER and CIBIL_SFTP_HOST in your system environment.
- Prepare the upload script:
a. Use the provided script or create your own based on the sample.
b. Ensure the script handles file tracking and logging.
- Upload process:
a. Place files in the designated source directory.
b. Run the upload script, which will:
    - Connect to CIBIL's SFTP server.
    - Upload new files to the appropriate directory.
    - Track uploaded files to prevent duplicates.
    - Log the upload process.
- Verify upload:
a. Check the log file for upload status.
b. Verify files in CIBIL's SFTP server.
- Handle rejections and re-uploads (if necessary):
a. Check the outbox folder on SFTP for reject (RFCU) files.
b. Process rejections and prepare corrected files.
c. Re-upload corrected files using the same process.

[UAT Process Guidebook.pdf](External%20reporting%20requirements/UAT_Process_Guidebook.pdf)

### NeSL reporting

NeSL, or National E-Governance Services Limited, is India's first Information Utility (IU) established under the Insolvency and Bankruptcy Code, 2016. It serves as a centralized platform for storing financial information about debtors.

NeSL acts as a repository of financial and credit information. It collects, collates, authenticates, and disseminates financial information to facilitate insolvency resolution processes. Banks, financial institutions, and other creditors report loan details and defaults to NeSL.

<aside>
⚠️

Reporting to NeSL is manual by design on their website and there are no vendors currently supporting this at the moment, hence we would have to set up an operational process to handle NeSL report (the format generation however can be automated via Finflux)

</aside>

**NeSL reporting format**

| Parameters | VERSION | TYP | NOOFREC | GSTIN | BILLADD | BUSSDT | UIN | FULNM | RELTOCNTRCT | DOI | COMADDR | PIN | TELNO | MOBNO | EMLID | EMLID2 | EMLID3 | PANNO | CIN | KIN | OTHID | OTHIDTYPE | CUSTID | LGLCNSTN | MSMEFLAG | MSMESTYP | INDUSTRY | CNTRPRTYADDR | REGOFFPIN | CNTRPRTYCNTNM | CNTRPRTYCNTMOBNO | ALTMOBNO | ALTEMLID | PRTYSNCTCCY | PRTYSNCTAMT | LOANNO | OLDACCNO | LOC | BU | RMEMAIL | DTOFSNCTN | DTOFDBRS | SANCREFNO | CURROFSANC | SNCTNAMT | DP | NTROFCRDT | CRDTSUBTYP | FCLTYNM | FUNDTYP | SECURITY | RPYFRQ | TENURE | DTOFEXP | EMIAMT | RTOFINT | LNDNGARRG | CURROFLOAN | TOUTSTNDAMT | PRIAMT | INTAMT | CHGAMT | AMTOVRDUE | DPD | ASSETCLASS | SMACAT | ISACCTCLOSED | REMARKPARTA | DTOFCRTN | TYPOFCHRG | ASSTYP | SECTYP | SECCATGRY | ASSETID | DSCOFSCRTY | VLOFSCRTY | CURROFSEC | DTOFVLTN | SCRTYIDROC | SCRTYIDCERSAI | REMARKPARTB | DEFLTDT | DEFLTAMT | LASTPAYAMT | LASTPAYDT | SUITFILEDT | REMARKPARTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sample value 1 | V2.5 | loan | 1 | 12AAACS1010D12Z | ROYAL BLDG 1ST FLOOR  LT ROAD BKC Mumbai 400051 | 21032018 | AAACS1010D | ABC BANK | Creditor | 1071955 | ARC BLDG 1ST FLOORJC ROAD BENGALURU | 560001 | 8022000000 | 9731208261 | creditor@abc.com | creditor@abc.com | creditor@abc.com |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sample value 2 | V2.5IND | loan | N |  |  | {DDMMYYYY} | DSP PAN | {User name} | {Debtor} |  |  |  |  |  | {user email} |  |  | {User PAN} |  |  |  |  |  | RESI |  |  |  |  |  |  |  |  |  |  |  | {Loan account number} |  |  |  |  |  | {Loan account creation date} |  | INR | {Sanction limit} |  | Financial | DLON | Loan against securities | Funded | Secured |  |  |  |  |  |  | INR | {TOS} |  |  |  | {Total overdue} | {DPD} |  |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  | { if DPD>0 then Current date - DPD in DDMMYYYY format} | {Amount overdue} |  |  |  |  |
| Value type | Static value | Static value | Static value | Null | Null | Date of report generation (business date) | Static value | DSP Finance Pvt Ltd (Static value) | Debtor - Static value | Null | Null | Null | Null | Null | Customer email | Null | Null | Customer PAN | Null | Null | Null | Null | Null | Static value "RESI" | Null | Null | Null | Null | Null | Null | Null | Null | Null | Null | Null | Customer loan account number | Null | Null | Null | Null | Null | Customer loan account opening date | Null | INR - Static value | Sanction limit of loan | Null | Financial - static value | DLON - static value | Static value | Funded - static value | Secured - static value | Null | Null | Null | Null | Null | Null | INR - Static value | Total outstanding of the loan account | Null | Null | Null | Total overdue of the loan account | DPD of the loan account (Has to be null if TOS is zero) | Null | Null | Acccount status (Yes if closed No if active or frozen) | Null | Null | Null | Null | Null | Null | Null | Null | Null | Null | Null | Null | Null | Null | { if DPD>0 then Current date - DPD in DDMMYYYY format} - First default date | Amount overdue (Total interest plus charges plus principal) | Null | Null | Null | Null |

**High level workflow:**

![image.png](External%20reporting%20requirements/image%205.png)

**Steps to upload on NeSL dashboard**

- Generate the reporting CSV file from the LMS.
- Prepare the CSV file:
a. Remove all commas (,) from the file.
b. Format "LOANNO" column cells as Number with no decimals.
c. Ensure no commas in "Amount" or "Address" cells.
d. Verify the number of records (NOOFREC) matches unique records in the file.
e. Save the file as .CSV with the format: PAN_ddmmyyyy_001.csv (e.g., AAAAA1234A_27052019_001.csv)
- Convert CSV to JSON:
a. Use the NeSL CSV to JSON Conversion Utility ([https://iu.nesl.co.in/JSONConversionUtility/](https://iu.nesl.co.in/JSONConversionUtility/)).
b. Enter the provided API Key and upload the CSV file.
c. Click "Convert to JSON" and download the resulting JSON file.
- Validate the JSON file:
a. Use the NeSL JSON Validation Utility ([https://iu.nesl.co.in/JSONValidationUtility/](https://iu.nesl.co.in/JSONValidationUtility/)).
b. Enter the API Key and upload the JSON file.
c. Click "Validate JSON".
d. If errors are found, download the error file, correct issues, and repeat the process.
- Sign the JSON file:
Option A: Using PFX file
a. Use the NeSL JSON Signature Utility ([https://iu.nesl.co.in/JSONSignatureUtility/](https://iu.nesl.co.in/JSONSignatureUtility/)).
b. Select "PFX based" option.
c. Enter the API Key, choose the JSON file and PFX file.
d. Enter the PFX passcode and click "Sign JSON".
e. Download the signed JSON file.
Option B: Using PKI Dongle
a. Install nCodePKIComponent_Setup.
b. Run nCodePkiComponenetV4.jar from the command prompt.
c. Insert the dongle and choose the JSON file.
d. Select the digital signature and enter the PIN.
e. Download the signed JSON file.
- Upload to NeSL Portal:
a. Log in to the NeSL Portal.
b. Navigate to "Bulk Upload" > "Form C Bulk Upload".
c. Choose the signed JSON file and click "Submit".
- Verify upload:
a. Check "Bulk Upload" > "Form C Bulk Status" for acknowledgement.
b. Download and review the acknowledgement file.

---

# **Design**

NA

---

# **Analytics**

Below are the metrics we need to monitor at a transaction/monthly/quarterly level.

- Number of records uploaded (CKYC / NeSL / CIC)
- Number of records that need to be created  (CKYC / NeSL / CIC)
- Number of records that need to be updated  (CKYC)
- Success rate for creation of a record  (CKYC / NeSL / CIC)
- Success rate for updating a record  (CKYC)

---

# **Timeline/Release Planning**

To be discussed

---

# **Go to market**

- CKYC: Within a week of go-live (Expected date: October 21st)
- CIC: Within a month of go live (Expected date: November 15th)
- NeSL: Within a month of go live (Expected date: November 15th)

## Marketing

NA

## Ops & Sales training

- Meeting with Ops to be setup to align on the process
- Close on solutioning for sending emails to create tickets

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Vendor confirmation discuss pricing
    - [ ]  Email copies for zendesk automation and triggering logic
- [ ]  Business
    - [ ]  Setting up Zendesk for DSP ops
    - [ ]  Setting up process to handle automatic email and create tasks for ops to upload data to CICs and NeSL
    - [ ]  Training for ops (Support manual to handle uploads)
    - [ ]  Sign-off on the requirements
    - [ ]  Formalise the SOP
- [ ]  Program
    - [ ]  Setup CKYC account for DSP
    - [ ]  Configure FI code for DSP
    - [ ]  Onboard CKYC vendor
    - [x]  Set up NeSL account
    - [x]  Setup CIBIL account
    - [ ]  Setup CRIF account
    - [ ]  Setup Experian account
    - [ ]  Setup Equifax account
    - [ ]  Set up NeSL reporting and UAT requirements
    - [ ]  Set up SFTPs with Experian
    - [ ]  Set up SFTPs with CIBIL
    - [ ]  Set up SFTPs with Equifax
    - [ ]  Set up SFTPs with CRIF

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