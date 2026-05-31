# Bank-PAN Name Mismatch in BAJAJ

: Ayush Kumar
Created time: October 7, 2024 11:28 AM
Status: In progress
Last edited: May 12, 2026 4:07 PM
Owner: Ayush Kumar

# **What problem are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

# **How do we measure success?**

---

# **How are the changes?**

**CURRENTLY:**

- The Bank-PAN Name validation is only for B2C and B2B customers and Name match threshold ≥ 65 and the customer were not allowed to upload supporting document
- The Bank-PAN Name validation is not for B2B2C customers

**CHANGES:**

- The Bank-PAN Name validation will be for all customers and Name match threshold should be ≥ 75
- If the Name match threshold < 75, the customer will be allowed to upload supporting document

---

# **What is the solution?**

## Requirements overview

- In the Bank verification step in BAJAJ: During penny drop, Digio verifies the Bank Account Holder Name with the Aadhaar Name and the PAN name
- If the match score ≥ 75, then we can allow the customer to complete the loan application
- If the match score < 75, then we will navigate the customer to a screen

![Untitled](Bank-PAN%20Name%20Mismatch%20in%20BAJAJ/Untitled.png)

- The screen would display a error message “We found a mismatch in your name as per PAN and Bank Account” and will give two options:
1. “No, I added wrong Bank Account”. 

This option will allow customer to add a new Bank Account and proceed the loan application

1. “Yes, it’s my Bank Account”. 

![Untitled](Bank-PAN%20Name%20Mismatch%20in%20BAJAJ/Untitled%201.png)

This option will allow the customer to upload supporting documents and complete the pending loan application as per the above screen

- The details of the mismatch along with the supporting documents will be sent to BAJAJ with the account opening mail in the following format:
    
    Bank name vs PAN name match result : {result percentage}
    Name as per PAN :
    Name as per bank account :
    PFA the supporting document shared by the customer(Passbook, Cancelled Cheque, Bank Statement)
    
    Format of the Account opening mail to BAJAJ:
    
    ![Untitled](Bank-PAN%20Name%20Mismatch%20in%20BAJAJ/Untitled%202.png)
    
    After the Account opening email content, leave a line space and attach the details of mismatch with the supporting document.
    
    > **Email Format:**
    > 
    > 
    > Hi,
    > 
    > Please refer to the below details for account creation and attached file for lodgment of MF.
    > 
    > Expecting confirmation with IVR file (PDF), Miles LAN number and Miles Account number.
    > 
    > PAN no – FRYPK2091F
    > 
    > Mandate-Callback :
    > 
    > {
    > 
    > "applicationId" : "0db22bfb-95d6-4e11-a551-7ff943e6ebfb",
    > 
    > "data" : {
    > 
    > "account_number" : "77770100689617",
    > 
    > "bank_name" : "Federal Bank",
    > 
    > "ref_no" : "BFL200843563231823",
    > 
    > "customer_name" : "KAPTAAN"
    > 
    > },
    > 
    > "error" : null,
    > 
    > "lanNo" : "63193054018519",
    > 
    > "link" : null,
    > 
    > "status" : "Finished"
    > 
    > }
    > 
    > Agreement-Callback :
    > 
    > {
    > 
    > "acceptanceIPAddress" : null,
    > 
    > "acceptanceTimestamp" : null,
    > 
    > "applicationId" : "0db22bfb-95d6-4e11-a551-7ff943e6ebfb",
    > 
    > "link" : null,
    > 
    > "status" : "223.228.95.183 || 2024-07-29 17:26:25 || SUCCESS"
    > 
    > }
    > 
    > We have encountered a mismatch in the BANK-PAN Name and the details are as follows:
    > 
    > Bank name vs PAN name match result : {result percentage}
    > Name as per PAN :
    > Name as per bank account :
    > 
    > PFA the supporting documents as proof of Bank account holding.
    > 
    > MF_Pledged_Portfolio.csv, (Passbook, Cancelled Cheque, Bank Statement).jpeg/pdf/png
    > 
    
    - If BAJAJ rejects the application after referring the supporting documents, then it is to be handled operationally by Ops team.
    

## User stories / User flow

## Requirements

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

VERIFY BANK ACCOUNT admin tool validation

If there is some unapproved IFSC from the BAJAJ side, the IFSC is not picked in our system. So, the customer is stuck at the Bank step and he is not able to proceed through the loan application flow.
In this case, we require the admin tool VERIFY_BANK_ACCOUNT
The unapproved IFSC is not allowed in the BAJAJ Bank Mandate as well
So, physical mandate is required in this step also.

UPDATE BANK ACCOUNT AFTER CREDIT CREATION 

- Validation of Bank from Digio
- Bank Name - PAN name score check occurs

Redirection Journey:

JS SDK

Android SDK

IOS SDK

React Native SDK