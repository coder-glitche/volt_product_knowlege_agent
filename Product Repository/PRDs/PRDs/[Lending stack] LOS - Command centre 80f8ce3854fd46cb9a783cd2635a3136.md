# [Lending stack] LOS - Command centre

: Saksham Srivastava
Created time: August 9, 2024 10:35 AM
Status: Not started
Last edited: September 18, 2024 3:52 PM

# **What problem are we solving?**

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

LOS Deviations

| Deviation | Prioritised for V1 |
| --- | --- |
| Sanction limit more than 2Cr | No |
| Sanction limit less than 10k | No |
| Age is more than 70 yrs | No |
| Bank-PAN/Aadhaar name mismatch | Yes |
| Photo match percentage | Yes |
| AML/PEP check | Yes |

### **Photo mismatch:**

JTBD: 

1. Match the photo that customer took with the photo on supporting document and 
2. Match the photo that customer took with the photo on Aadhaar. 

Primary details: 

1. LSP provided photo of the customer.
2. Additional supporting document uploaded by the customer, there will be front and back photos of these. (Voter ID, Passport, Driver’s license)
3. Photo on Aadhaar where match failed.
4. Photo match percentage. 

### **Bank name mismatch:**

JTBD: 
1. Match the name from Bank verification utility with name on supporting document. 
2. Match the same with name on aadhaar and PAN. 

Primary details:

1. Name from the BAV utility.
2. Match percentage with PAN and aadhaar names.
3. Name on the supporting document (Cancelled cheque, bank statement, passbook)

### AML/PEP match:

JTBD: Go through the trackwizz report and take a call if the customer’s application should be approved or not. 

Primary details:

1. Match score in AML/PEP lists. Currently there are three. India MHA, UNSC, India PEP.
2. Trackwizz report
3. Details of the custome:
    
    pan
    aadhaarNumber
    mobileNumber
    email
    address
    address-country-code (IND - India)
    Zipcode
    State - code (address)
    gender mapped to integer (01, 02, 03) from KYC data
    DOB (DD-MMM-YYY) from KYC / PAN (later when we do PAN Verification)
    Father Name from additional documents ( + prefix)
    First Name : Pass entire name | No validations from TW
    
- Old requirements
    
    Handle the following use cases: 
    
    1. Deviations: Approve/reject deviation from STP 
        1. Deviations created during the journey (created by different utils) before LSP submits opportunity
            1. Sanction limit > maxSanctionAmount for STP. 
                1. Required document: CAS document of the customer.
            2. Sanction limit is < minSanctionAmount for STP: Before pledging
                1. Required document: CAS docuement of te customer. 
            3. Customer age > maxAge for STP
                1. Required document: None
            4. Photo match percentage < photoMatchThreshold for STP
                1. Required document: Photo match details, Aadhaar document
            5. Bank name - PAN/ Aadhaar name mismatch < (bankPanNameMatchThreshold, bankAadhaarNameMatchThreshold) for STP
                1. Required document: Cancelled cheque, Bank stament of the customer
        2. Deviations created post LSP submits opportunity
            1. AML score of the customer is > maxAmlScore in any of the lists (MHA designated, UNSC Consolidated list, India PEP)
                1. Required document: None
    2. Ops review/Application review/Quality check: Final check and review of the complete application steps and details.
        1. Applicant details: 
        Documents: Customer application form
            
            
            | OpportunityID | Opportunity ID  |
            | --- | --- |
            | CAF number | Unique number of the CAF |
            | Customer photo | Live photo captured of the user |
            | Name | Name as per PAN |
            | Date of birth: | DOB as per PAN |
            | Gender: | Gender as per Aadhaar |
            | Father's Name: | As entered by user |
            | Mother's Name: | As entered by user |
            | Marital Status: | As entered by user |
            | Address line 1: | From proof of address (Aadhaar) |
            | Address line 2: | From proof of address (Aadhaar) |
            | State: | From proof of address (Aadhaar) |
            | District/City: | From proof of address (Aadhaar) |
            | Pincode: | From proof of address (Aadhaar) |
            | PAN: | PAN of the customer from KYC |
            | OVD type: | Aadhaar |
            | OVD number: | Masked Aadhaar number of the customer from KYC |
            | Mobile number:  | Mobile number of the customer |
            | Email address: | Email address of the customer  |
            | Education qualification: | Upto 12th pass/Graduate/Post graduate/Others |
            | Income range: |  |
            | Profession: |  |
        2. KYC documents: 
            1. KYC ref no. 
            2. OVD:
                1. OVD type: Aadhaar
                2. OVD number:
                3. Source:
                4. Verification status:
                5. Verified on:
                6. View document:
            3. PAN:
                1. PAN details:
                2. Source:
                3. Verification source/status:
                4. Aadhaar link source/status: 
                5. Verified on:
                6. View document:
        3. Bank details: BAV reference number 
            1. Bank account number:
            2. IFSC: 
            3. Name as per bank account:
            4. Name match wtih Aadhaar:
            5. Name match with PAN:
            6. Provider:
        4. Mandate details: Mandate utility reference number
            1. Mandate status:
            2. Mandate type
            3. Mandate amount:
            4. UMRN number:
            5. Frequency:
            6. End date:
        5. Loan terms:
            
            
            |  | **Fields** | **Go-live value** |
            | --- | --- | --- |
            | Terms | Product Name | Loan against securities |
            |  | Max sanctioned limit | ₹2,00,00,000 |
            |  | Collateral linked credit limit | - Drawing power of the customer in accordance with pledged mutual funds |
            |  | Tenure | 36 months |
            |  | Details of securities | Pledge of securites, mutual funds, Exchange Traded Funds (ETFs) shares and any other securites as will be pledged from tme to tme |
            |  | Interest type | Floating |
            |  | Interest rate |  |
            |  | Due date of interest payment | 7th of every month |
            | Charges | Processing charges | Rs 1,499 + GST |
            |  | Margin pledge charges | 499 + GST |
            |  | Sanction limit update charges | Rs. 999 + GST |
            |  | Renewal charges | Rs. 1,499 + GST |
        6. Loan kit details
            1. Loan kit status:
            2. Customer sign type:
            3. Customer signed on:
            4. View loan kit:
        7. Risk assessment
            1. Risk category:
            2. Credit score:
            3. View credit report:
            4. View risk report:
        
        Deviation information will be contextualised in the OC step check.
        

## User stories / User flow

## Requirements

---

# **Design**

Design requirements : 16th Aug

- **Scope of work**: Create wireframes for the following
    - Task list view screen
    - Deviations screens
    - Application view screens (including the QC screen)
- 

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