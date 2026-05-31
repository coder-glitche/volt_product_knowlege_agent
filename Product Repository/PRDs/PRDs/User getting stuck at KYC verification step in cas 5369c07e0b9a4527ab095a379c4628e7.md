# User getting stuck at KYC verification step in case of PAN-Aadhar name mismatch

: Ameya Aglawe
Created time: July 27, 2024 12:00 PM
Status: On Hold
Last edited: October 7, 2024 5:01 PM

# **What problem are we solving?**

In the applications in which we are not able to fetch PAN details, the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

# **How do we measure success?**

- Number of application with Aadhar-PAN name mismatch completed successfully
- Loan application TAT for applications with Aadhar-PAN name mismatch

---

# **How are others solving this problem?**

---

# **What is the solution?**

- User completes the KYC screen :
    - We get “POV=null” in the getkycdetails response.
    - Then we will not keep the user stuck at this step, and allow them to move to the next “bank account” step.
    - Then we will enable the user to add supporting documents in the documents section
- When the issue is of mis-match, we will enable the 1st applicant to the add additional documents screen, where we will make the user attach the :
    - PAN signed document
- Once the user has uploaded the document, these documents will be sent in BAJAJ account creation mail, **(with remarks)**
    - **Remarks : “PAN for the customer was not fetched from Digilocker, hence attaching the self attested PAN of the user”**
    - Add Pratik, Sheetal & Parul in cc
        - Pratik :  [pratik.bagul@bajajfinserv.in](mailto:pratik.bagul@bajajfinserv.in)
        - Sheetal : [shital.mahale@bajajfinserv.in](mailto:shital.mahale@bajajfinserv.in)
        - Parul : [parul.rajas@bizsupporta.com](mailto:parul.rajas@bizsupporta.com)
- Once the account creation mail is sent to BAJAJ
    - BAJAJ approves → User’s loan account will be created
    - BAJAJ rejects → Ask customer whether they are okay with going with different lender/starting new application again → Change lender through admin action & ask user to create a new application

## Requirements overview (optional)

## User stories / User flow

User completes the KYC verification step → KYC verification failed → We let the user continue the journey → User adds supporting documents (Signed PAN) at the document step→ User completes the application → If the application is approved from BAJAJ side → User’s loan account will created in BAJAJ 

## Requirements

---

1. If we get POV=”null”, add 2 more section in the Document step, for the first applicant to upload supporting document
    1. Other section will for signed PAN document upload 
    2. **Note** : It will be mandatory for the first applicant to attach these documents 
2. Edge cases : 
    1. Document size exceeded
    2. Document type unsupported 
    3. Technical error 
3. Please refer to the designs here: [https://www.figma.com/design/9EhyO2MFVGvrCrjgsFvsGj/Aadhar-PAN-Mismatch?node-id=0-1&t=77D8Xu74By4BV7VH-1](https://www.figma.com/design/9EhyO2MFVGvrCrjgsFvsGj/Aadhar-PAN-Mismatch?node-id=0-1&t=77D8Xu74By4BV7VH-1)

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

**Doubts -** 

1. Why is this kind of document sign required in the first place? Considering the user has already done complete KYC verification process. 
    1. Addendum if fine 
    2. Why are only co-applicants PAN & Aadhar are required?  - This is a lender side requirement 
    3. Co-applicants PAN & Aadhar card required from lender side itself? 
2. If there is a name mis-match issue, then we don’t allow the user to move forward in the application then how come the user will arrive at the step of document step - That’s the PRD for, we need to re-direct the user to “add documents” screen. 

- KYC detail entered, allow
- We got webhook
- We use webhook to hit getkycdetails
    - We get the POV details
- And then we validate here if we

- **Doubts :**
1. BAJAJ application sending, at what time, how? Can I see the email?

**KYC_POD -** 
1. POV - Details from PAN 
2. POI, POA - Details from Aadhar (state etc.) 

**PAN-AADHAR MISMATCH CASES -** 
1. Aadhar not present 
2. PAN not present
3. POV=null 

- Account creation mail
    - PAN-aadhar name mismatch :

**Discussion :** 

1. How were we able to fetch the Aadhar details if we were not able to fetch the PAN details? 
2. Is PAN & Aadhar both mandatory as supporting documents? Only PAN
3. **What happens if BAJAJ rejects the application after sending the supporting documents?** 
    1. We change the lender & start a new application (after informing the user) 
    2. What do we show to the user in the app? 
        1. Till the time account creation is pending → We land the user to the dashboard screen & also allow the user to make the withdrawal 
        2. **When the application is rejected by the lender???? We don’t have handling for this, the withdrawal request just stays at requested** 
4. There could be two approaches 
    1. Adding documents screen post KYC verification itself in case of mis-match 
        1. Pros 
            1. User’s effort will be saved in case BAJAJ rejects their application 
            2. If BAJAJ rejects this application at this stage, we can still move back the user to previous step and ask user to resume the application from the there. 
        2. Cons 
            1. The TAT for BAJAJ response for the application is very high 
            2. Will have to establish a system with BAJAJ in order to process these PAN-Aadhar name mismatch cases separately 
    2. Adding section for uploading first applicants signed PAN-Aadhar in the documents screen itself 
        1. Pros 
            1. Since user have already spent a lot of effort till the time they reach this step, so they will make the extra to upload document at this step, but asking user to upload documents at the initial stages of the application itself might lead to user dropping off. 
        2. Cons 
            1. If the user’s application gets rejected at this stage (after completing the application) then a lot of user effort will be wasted.
            2. A new application will have to be created, and user will have be required to do the application again (with TATA)