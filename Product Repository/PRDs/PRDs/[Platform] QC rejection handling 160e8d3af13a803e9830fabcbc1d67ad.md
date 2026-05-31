# [Platform] QC rejection handling

: Vaibhav Arora
Created time: December 18, 2024 9:00 AM
Status: Ready for Tech
Last edited: January 21, 2025 2:16 PM

# **What problem are we solving?**

To ensure a valid application, we have developed a quality check flow on the command centre through which operations team can verify core aspects of an application and decide to either approve or reject it.

If a discrepancy is found in the QC application, the operations team is supposed to reject the QC, however the corresponding outflow of information to the customer and the LSP is not handled. 

This impacts the user’s application experience  (as by then the securities are pledged by the user) and increases TAT for an application to get processed. It also consumes significant operational bandwidth of the team.

---

# **How do we measure success?**

- Completion rate of applications post rejection as a ratio of average completion rate (Should be close to 0.9-1)
- Man hours spent from operations and tech to handle QC rejections
- TAT to complete an application post rejection as a ratio of average completion TAT (should be close to 0.6-0.8)

---

# **How are others solving this problem?**

- BFL and TCL had not handled programmatic responses if the applications in the non STP flow were rejected. Information was passed between operations team of BFL/TCL and Volt money and applications were then reversed
- Mirae blocks the customer post application and sends it to review, (user is not able to make requests or access their loan while their application is processed) - Once processed they get shifted back to the corresponding step to handle the same

---

# **What is the solution?**

We will be sending callbacks to the LSP for the corresponding rejections on the application. LSPs basis the callback will handle the corresponding orchestration to handle the user’s application.

Send backs can occur due to the following broad scenarios (in one or multiple sections):

- Value mismatch / Discrepancy (Eg: Photo of the customer and OVD does not match) - Soft reject
- Policy breach (Eg: Policy allows applicants aged 21–60, but the customer is 19 or 65) - Soft reject
- Other (Remarks) (Eg: There are issues with document uploads or system errors during processing.) - Soft reject

It will be the LSPs decision and responsibility to handle the corresponding orchestration. 

Following are the scenarios that we will be handling in V1:

| **Section** | **Subsection** | **Details** | **Mismatch** | **Mismatch Scenario** | **Policy Breach** | **PB Scenario** | **Other Potential Scenarios** | Affected Utility |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Application Section | Applicant Details | Customer Name | Yes | Name does not match the customer name in the agreement | Yes | Customer name does not match with OVD document | Salutation does not match marital status | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Applicant Details | Date of Birth | Yes | Date of birth does not match in the agreement | Yes | Below 18 or over 70 | Inconsistent DOB across different documents | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Applicant Details | Gender | Yes | Gender does not match salutation/agreement | Yes | Gender apart from what is accepted by the NBFC |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Applicant Details | POI Type | Yes | POI type mismatch (type was different from populated values) | Yes | Invalid POI type |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Applicant Details | POI Number | Yes | POI number mismatch with provided document | No |  |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Applicant Details | POI Verification Status | No |  | Yes | POI document verification failed |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Applicant Details | PAN and Aadhaar Seeding | No |  | Yes | PAN and Aadhaar are not linked |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Proof of Address | POA Name | Yes | POA name does not match with the provided proof | No |  |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Proof of Address | POA Number | Yes | POA number mismatch with provided document | No |  |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Proof of Address | POA Verification Status | No |  | Yes | Verification status failure |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Proof of Address | Customer Address | Yes | Address mismatch with provided document | Yes | Address outside the whitelisted pincodes |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Proof of Address | Pincode | Yes | Pincode mismatch with address | Yes | Pincode not serviced by NBFC |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Proof of Address | City | Yes | City does not match provided address proof | Yes | City not under serviceable area |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Proof of Address | State | Yes | State does not match provided address proof | Yes | State not under serviceable area |  | KYC, KFS, PHOTO &
Agreement |  |
| Application Section | Customer Declarations | Father’s Name | Yes | Incorrect father's name | Yes | Missing father's name |  | Additional details
Agreement |  |
| Application Section | Customer Declarations | Educational Qualifications | Yes | Education details mismatch with agreement | No |  |  | Additional details
Agreement |  |
| Application Section | Customer Declarations | Marital Status | Yes | Marital status mismatch with provided documents | No |  | Salutation not matching marital status | Additional details
Agreement |  |
| Application Section | Customer Declarations | Income Range | Yes | Income does not match declared or verified range | Yes | Income declared below NBFC's acceptable range |  | Additional details
Agreement |  |
| Application Section | Customer Declarations | Employment Status | Yes | Employment status mismatch with documents provided | No |  |  | Additional details
Agreement |  |
| Application Section | Customer Declarations | End Use of Loan | Yes | Missing / Invalid end use | Yes | Loan purpose does not align with allowed criteria |  | Additional details
Agreement |  |
| Application Section | Customer Declarations | Current and Permanent Address Declaration | Yes | Missing / Invalid declaration | No |  |  | Additional details
Agreement |  |
| Application Section | Customer Photo | Photo Verification Status | Yes | Photo mismatch with uploaded image | No |  |  | Photo verification
Agreement |  |
| Application Section | Customer Photo | Photo Liveliness Status | No |  | Yes | Photo failed liveliness check |  | Photo verification
Agreement |  |
| Application Section | Customer Photo | Match Percentage | No |  | Yes | Match percentage below acceptable threshold |  | Photo verification
Agreement |  |
| Application Section | Customer Photo | Liveliness Percentage | No |  | Yes | Liveliness percentage below acceptable threshold |  | Photo verification
Agreement |  |
| Application Section | Verification Logs | Phone Number | Yes | Phone number mismatch / Invalid | No |  |  | Mobile verification log
Agreement |  |
| Application Section | Verification Logs | Verification Status (Phone) | Yes | Invalid verification method or timestamp | Yes | Phone verification method not allowed |  | Mobile verification log
Agreement |  |
| Application Section | Verification Logs | Customer IP (Phone) | Yes | Customer IP mismatch during phone verification | No |  | VPN detected during check | Mobile verification log
Agreement |  |
| Application Section | Verification Logs | Email Address | Yes | Email address invalid | No |  |  | Email verification log
Agreement |  |
| Application Section | Verification Logs | Verification Status (Email) | Yes | Email verification failed or missing | Yes | Email verification method not allowed |  | Email verification log
Agreement |  |
| Application Section | Verification Logs | Customer IP (Email) | Yes | Customer IP mismatch during email verification | No |  | VPN detected during check | Email verification log
Agreement |  |
| Bank and Mandate Details | Bank Details | Bank Name | Yes | Bank name mismatch with documents provided | Yes | Bank name and IFSC do not match |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Bank Details | Bank Account Number | Yes | Bank account number mismatch with loan kit or invalid | No |  |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Bank Details | IFSC | Yes | Invalid or inactive IFSC code | No |  |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Bank Details | Name as per Bank Account | Yes | Name mismatch with OVD details | No |  |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Bank Details | Bank Verification Status | Yes | Invalid verification method or timestamp | Yes | Bank verification failed |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Mandate Details | Mandate Status | Yes | Invalid mandate status | No |  |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Mandate Details | Registration Method | Yes | Invalid registration method | No |  |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Mandate Details | UMRN | Yes | Invalid UMRN / Missing UMRN | No |  |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Mandate Details | Maximum Amount | Yes | Amount invalid or missing | Yes | Amount is not as per policy limits |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Mandate Details | Frequency | Yes | Frequency invalid or missing | Yes | Frequency not allowed as per NBFC policy |  | Bank account
Mandate
Agreement |  |
| Bank and Mandate Details | Mandate Details | Expiry Date | Yes | Expiry date invalid or missing | Yes | Date is not as per policy limits |  | Bank account
Mandate
Agreement |  |
| Loan Details Section | Loan Terms | Product Type | Yes | Product type invalid or missing | Yes | Product not allowed by NBFC |  | Bank account
Mandate
Agreement |  |
| Loan Details Section | Loan Terms | Maximum Sanctioned Limit | Yes | Sanctioned limit invalid or missing | Yes | Sanctioned limit does not meet policy limits |  | Agreement |  |
| Loan Details Section | Loan Terms | Facility Value Limit | Yes | Facility value invalid or missing | No |  |  | Agreement |  |
| Loan Details Section | Loan Terms | Tenure | Yes | Tenure invalid or missing | Yes | Tenure is not as per policy limits |  | Agreement |  |
| Loan Details Section | Loan Terms | Maturity Date | Yes | Maturity date invalid or missing or does not correspond to the tenure | Yes | Maturity is not as per policy limits |  | Agreement |  |
| Loan Details Section | Loan Terms | Allowed Collaterals | Yes | Collateral type invalid or missing | Yes | Collateral not permissible under NBFC policy |  | Agreement |  |
| Loan Details Section | Interest Details | Interest Type | Yes | Interest type invalid or missing | Yes | Interest type not allowed |  | Agreement |  |
| Loan Details Section | Interest Details | Interest Rate | Yes | Interest rate missing or does not match with loan kit | Yes | Rate outside permissible limits |  | Agreement |  |
| Loan Details Section | Interest Details | Interest Due Date | Yes | Due date missing or invalid | Yes | Interest due date not as per policy limits |  | Agreement |  |
| Loan Details Section | Charges | Processing Fee | Yes | Processing fee missing or invalid | Yes | Fee does not meet policy limits |  | Agreement |  |
| Loan Details Section | Charges | Margin Pledge Fee | Yes | Margin pledge fee missing or invalid | Yes | Fee does not meet policy limits |  | Agreement |  |
| Loan Details Section | Charges | Renewal Fee | Yes | Renewal fee missing or invalid | Yes | Fee does not meet policy limits |  | Agreement |  |
| Loan Details Section | Charges | Foreclosure Fee | Yes | Foreclosure fee missing or invalid | Yes | Fee does not meet policy limits |  | Agreement |  |
| Loan Details Section | Charges | Annual Maintenance | Yes | Maintenance fee missing or invalid | Yes | Fee does not meet policy limits |  | Agreement |  |
| Loan Details Section | Loan Kit Details | Application Number | Yes | Application number missing or invalid or does not match with loan kit | No |  |  | Agreement |  |
| Loan Details Section | Loan Kit Details | Acknowledgement Status | Yes | Status invalid or missing | Yes | Status is not as per policy |  | Agreement |  |
| Loan Details Section | Loan Kit Details | KFS Customer IP | Yes | Customer IP mismatch or missing | No |  | VPN detected | Agreement |  |
| Loan Details Section | Loan Kit Details | Customer Sign Status | Yes | Sign status missing or invalid | No |  |  | Agreement |  |
| Loan Details Section | Loan Kit Details | Agreement Customer IP | Yes | Agreement IP mismatch or missing | No |  | VPN detected | Agreement |  |
| Risk Section | Credit Details | Risk Category | Yes | Risk category mismatch or missing | Yes | Customer flagged in AML watchlist |  | Agreement |  |
| Risk Section | Credit Details | Credit Score | Yes | Credit score mismatch or missing | Yes | Score below acceptable threshold |  | Agreement |  |
| Risk Section | AML/PEP Details | AML/PEP Risk Category | Yes | Status invalid or missing | Yes | Customer listed under high-risk category |  | Agreement |  |
| Risk Section | AML/PEP Details | India PEP Match Status | Yes | Status invalid or missing | Yes | Customer listed in PEP records |  | Agreement |  |
| Risk Section | AML/PEP Details | UNSC Match Status | Yes | Status invalid or missing | Yes | Customer flagged in UNSC sanctions list |  | Agreement |  |
| Risk Section | AML/PEP Details | India MHA Match Status | Yes | Status invalid or missing | Yes | Customer flagged in MHA list |  | Agreement |  |
| Risk Section | KYC Risk | KYC Risk Category | Yes | Category invalid or missing | Yes | KYC category not as per policy |  | Agreement |  |
| Risk Section | KYC Risk | Reason | Yes | Reason missing or invalid | No |  |  | Agreement |  |

- 

<aside>
💡

Ops agent will be able to raise rejections at a sub section and a section level, and the complete rejection of the QC will entail rejections at a section, task and sub-task level

There can be multiple rejection reasons within one rejection, the same will be passed to the LSP in the corresponding response/callback

</aside>

## Requirements overview (optional)

Post QC rejection, Fenix will send a callback as well as give a status API which the LSP can use to get the status of the loan application. 

Sample Callback / Status response:

```json
{
  "application_id": "1234567890",
  "status": "Rejected",
  "rejection_reasons": [
    {
      "section": "Application",
      "task": "Applicant Details",
      "sub_tasks": [
        {
          "field": "Customer name",
          "reason": "Mismatch",
          "details": "Name in application does not match name in PAN document."
        },
        {
          "field": "Date of birth",
          "reason": "Policy breach",
          "details": "Applicant's age is below the minimum allowed age of 21."
        }
      ]
    },
    {
      "section": "Proof of Address",
      "task": "Address Details",
      "sub_tasks": [
        {
          "field": "Pincode",
          "reason": "Mismatch",
          "details": "Pincode in proof of address does not match the application form."
        }
      ]
    },
    {
      "section": "Bank and Mandate Details",
      "task": "Mandate Details",
      "sub_tasks": [
        {
          "field": "Mandate status",
          "reason": "Other",
          "details": "Mandate registration failed due to insufficient account balance."
        }
      ]
    },
    {
      "section": "Loan Details",
      "task": "Loan Terms",
      "sub_tasks": [
        {
          "field": "Tenure",
          "reason": "Policy breach",
          "details": "Requested loan tenure exceeds the allowed maximum of 60 months."
        }
      ]
    },
    {
      "section": "Risk",
      "task": "AML/PEP Details",
      "sub_tasks": [
        {
          "field": "UNSC match status",
          "reason": "Other",
          "details": "Applicant appears on the UNSC sanctions list."
        }
      ]
    }
  ]
}
```

Basis this LSP will be able to identify the response and orchestrate the next steps accordingly. 

Fenix handling:
Post getting callback, LSP can re-submit the corresponding details at an opportunity level into the respective utilities. 

Once re-submitted, LSP should be able to retrigger application submission to DSP which should create a new QC task for the operations team to verify.

This new task will have context of the older task at a sub task level.

Ops team should also be able to identify that this is not a new application but an older re-submission.

We will handle this via the task name: Loan creation approval (Re-submission)

and the page header (Quality check: Re-submission) - @Karuna Sankolli to solve in terms of design

Live deviation, there will be a section called rejection details which will have the following parameters at a sub task level:

Rejection details:

Rejected on: Timestamp

Rejected by: Checker Name
Rejection parameter: Which parameter was rejected in the sub task
Rejection reason: Mismatch / Policy breach / Others
Rejection remarks: (If others) corresponding remarks

## User stories / User flow

![image.png](%5BPlatform%5D%20QC%20rejection%20handling/image.png)

---

# **Design**

**@Karuna Sankolli to make designs**

---

# **Analytics**

- Number of QC rejections as a percentage of total applications (Daily/Weekly/Monthly)
- Completion rate of applications post rejection as a ratio of average completion rate (Should be close to 0.9-1)
- TAT to complete an application post rejection as a ratio of average completion TAT (should be close to 0.6-0.8)

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