# BAJAJ : New KFS+Agreement flow

: Ameya Aglawe
Created time: September 12, 2024 4:42 PM
Status: Done
Last edited: October 8, 2024 1:04 PM
Owner: Ameya Aglawe

# **What problem are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload

---

# **How do we measure success?**

- Reduction in #user stuck at Agreement step.
- **North star :** #applications completed per week with BAJAJ

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

### User stories / User flow

**Existing Flow** 

1. User confirms pledging of funds 
2. Agreement link generation loader shows up 
3. Agreement step anchor page shows with the state 
    1. Review Key terms (marked completed)  
    2. Review agreement 
4. User taps on “Review KFS” → KFS link opens 
    1. I agree : Handled 
    1. I disagree : **Getting callback but not handled in backend & UI** 

**New Flow** 

1. User confirms pledging of funds 
2. Agreement link generation loader shows up 
3. Agreement step anchor page shows with the state 
    1. Review Key terms (marked completed)  
    2. Review agreement 
4. User taps on “Review Agreement” CTA 
5. Application, KFS, Agreement common link opens up 
    1. Application 
    1. KFS 
    1. Agreement 

### New Flow with screens

**Confirm pledge** 

![Screenshot 2024-09-27 at 10.02.35 AM.png](BAJAJ%20New%20KFS+Agreement%20flow/Screenshot_2024-09-27_at_10.02.35_AM.png)

**Enters & verifies OTP (CAMS & Kfin)** 

![Screenshot 2024-09-27 at 10.04.01 AM.png](BAJAJ%20New%20KFS+Agreement%20flow/Screenshot_2024-09-27_at_10.04.01_AM.png)

**Taps on continue and comes to the anchor page** 

![Screenshot 2024-09-27 at 10.04.51 AM.png](BAJAJ%20New%20KFS+Agreement%20flow/Screenshot_2024-09-27_at_10.04.51_AM.png)

- Agreement step anchor page shows up with the state
    1. Review & accept key terms (marked completed)  
    2. Review & sign agreement 

**User taps on “Continue to sign agreement”**

Then BAJAJ’s link opens up with following document in sequential manner 

1. Page 1 - application form opens up, users can scroll down and tap on the “I accept” option. There will only be one option in application form & that is to accept the document 
2. Page 2 - Once user accepts application form, KFS document opens up where users can scroll down and tap on the “I accept” or “I disagree” option. 
    1. If user taps on I accept : User will move to next page (Agreement page) 
    2. If user taps on I disagree : A new page will open up showing “Our sales representative will contact you shortly” this state will update to “You have rejected the document” within a minute. This will be the terminal state of the link. 
        - On app : If users taps on back button they’ll land of the agreement anchor page
            
            ![image.png](BAJAJ%20New%20KFS+Agreement%20flow/image.png)
            
        - On web : If user closes the agreement link & refreshes our web app they’ll land at the agreement anchor page
            
            ![image.png](BAJAJ%20New%20KFS+Agreement%20flow/image%201.png)
            
3. Page 3 - Once user accepts the KFS, Agreement document opens up where users can scroll down and tap on the “I accept” or “I disagree” option. 
    1. If user taps on I accept : A new page will open up showing “Thanks for showing your interest” and the link will close, a bottom drawer would open up in our app saying “Agreement submitted” with the CTA “Proceed”, tapping on the CTA user moves to the Auto-pay step 
    2. If user taps on I disagree : A new page will open up showing “Our sales representative will contact you shortly” this state will update to “You have rejected the document” within a minute. This will be the terminal state of the link. The terminal state of our app/web will be the agreement anchor page. 
        - On app : If users taps on back button they’ll land of the agreement anchor page
            
            ![image.png](BAJAJ%20New%20KFS+Agreement%20flow/image.png)
            
        - On web : If user closes the agreement link & refreshes our web app they’ll land at the agreement anchor page
            
            ![image.png](BAJAJ%20New%20KFS+Agreement%20flow/image%201.png)
            
        

BAJAJ’s new loan documents 

[NewApplicationFormBAJAJ.pdf](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/NewApplicationFormBAJAJ.pdf)

[NewKFSFormatBAJAJ.pdf](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/NewKFSFormatBAJAJ.pdf)

[BAJAJAgreementNew.pdf](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/BAJAJAgreementNew.pdf)

**User accepts all the 3 documents** 

User lands on the Setup AutoPay screen. 

![Screenshot 2024-09-27 at 11.54.55 AM.png](BAJAJ%20New%20KFS+Agreement%20flow/Screenshot_2024-09-27_at_11.54.55_AM.png)

- From here user can setup the mandate and proceed with the application journey.

## Requirements

- The anchor page for agreement step, will briefly mention the documents that users needs to review & the stepper will be removed completely

---

# **Design**

---

Figma : https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=9837-59660&t=pVjivWu47PjJD9K3-1

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
    - [x]  Training to be setup for Ops & sales
    - [ ]  Metrics to be setup to review the funnel
- [x]  Business
- [x]  Design

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

- **Cases of KFS Reject**
    - `INFO NonStaticHttpUtility RRId= RId=3e34d36c-d0b3-47e6-9580-e559bae44857, AppId=, UId= - Creating post request for uri http://internal-Beta-Credi-14BGMJPDTBX1M-996195882.ap-south-1.elb.amazonaws.com/review/kfs/review/kfs/status/update with body {"applicationId":"688f6127-ebfb-45dc-b649-687be8ea5e74","link":null,"status":"2401:4900:8648:90cd::359d:448e || 2024-09-01 19:59:16 || REJECT"}`
    - `INFO NonStaticHttpUtility RRId= RId=3737eaf9-1fc8-4790-8418-d4dcb242fc1e, AppId=, UId= - Creating post request for uri http://internal-Beta-Credi-14BGMJPDTBX1M-996195882.ap-south-1.elb.amazonaws.com/review/kfs/review/kfs/status/update with body {"applicationId":"ff3d4f9b-3bec-4c11-b00f-cd868ecbe189","link":null,"status":"223.190.84.123 || 2024-09-01 14:22:59 || REJECT"}`
    - `INFO NonStaticHttpUtility RRId= RId=681760ce-70f5-41f2-ba39-d15568cdbee4, AppId=, UId= - Creating post request for uri http://internal-Beta-Credi-14BGMJPDTBX1M-996195882.ap-south-1.elb.amazonaws.com/review/kfs/review/kfs/status/update with body {"applicationId":"d85cd4b0-8aeb-4877-b98d-00c20ec58be4","link":null,"status":"2401:4900:8556:8d3a::44a4:53a8 || 2024-08-31 17:37:52 || REJECT"}`
    - `INFO NonStaticHttpUtility RRId= RId=3441a5db-33fa-4bcc-ac75-33cb58ac294a, AppId=, UId= - Creating post request for uri http://internal-Beta-Credi-14BGMJPDTBX1M-996195882.ap-south-1.elb.amazonaws.com/review/kfs/review/kfs/status/update with body {"applicationId":"60160997-36cc-4278-a655-bc1f432d1ab7","link":null,"status":"180.188.224.243 || 2024-08-30 19:19:13 || REJECT"}`
- **Cases of Agreement Reject**
    - We don’t get REJECT in case of Agreement as of now, this is at UAT stage in BAJAJ
    - So we can’t do the handling of the same right now.

- Ask to Sagar Dhede
    - Will agreement re-query work only case of single KFS + Agreement link
    - Will agreement re-query work when KFS is REJECTED by the user

# Single link of KFS & Agreement

Reasons why customer Rejects KFS - 

- We show EMI in the KFS which goes against our pitch of over draft
- Total interest amount to be charged is mentioned as fixed interest, which goes against our pitch of falling interest rate

**Difference log statuses (Happy flow) -** 
**Initial status** 
1.{"loan_application_number":"62081719127547","type":"status","status":"approved"}
2. {"loan_application_number":"62081719127547","link":"[https://emandate-staging.bajajfinserv.in/DocumentPOD/DocPod/Index/h1TTB7tY4VsOfBm8k1q~V3U7n0JjwhACNkgot5YEVIlEz4WTRXFJAYJIIXfX3nOH_cwBQPKChYhHkhcjHHCK3g==","KFSstatus":"Acceptance](https://emandate-staging.bajajfinserv.in/DocumentPOD/DocPod/Index/h1TTB7tY4VsOfBm8k1q~V3U7n0JjwhACNkgot5YEVIlEz4WTRXFJAYJIIXfX3nOH_cwBQPKChYhHkhcjHHCK3g==%22,%22KFSstatus%22:%22Acceptance) Pending","type":"esignature","status":"Acceptance Pending"}

**Final status** 
{"loan_application_number":"62081719127547","KFSstatus":"116.73.243.197 || 2024-09-06 17:10:08 || SUCCESS","type":"esignature","status":"116.73.243.197 || 2024-09-06 17:11:01 || SUCCESS"}

**Difference log statuses (Rejection flow) -
1. KFS Rejected** 

Not getting a callback 

**2. Agreement Rejected**  

{"loan_application_number":"62081719632112","KFSstatus":"116.73.243.197 || 2024-09-06 18:50:27 || SUCCESS","type":"esignature","status":"116.73.243.197 || REJECT"}

"stepStatusMap": {
"MF_FETCH_PORTFOLIO": "COMPLETED",
"KYC_SUMMARY": "COMPLETED",
"KYC_PAN_VERIFICATION": "COMPLETED",
"BANK_ACCOUNT_VERIFICATION": "COMPLETED",
"MF_PLEDGE_PORTFOLIO": "SKIPPED",
"KYC_DOCUMENTS": "COMPLETED",
"KYC_ADDITIONAL_DETAILS": "COMPLETED",
"ASSET_PLEDGE": "COMPLETED",
"CREDIT_APPROVAL": "COMPLETED",
"KYC_PHOTO_VERIFICATION": "COMPLETED",
"KYC_CKYC": "SKIPPED",
"REVIEW_KFS": "NOT_STARTED",
"AGREEMENT_SIGN": "NOT_STARTED",
"DIGIO_MANDATE_SIGN": "SKIPPED",
"BAJAJ_CKYC": "SKIPPED",
"MANDATE_SETUP": "NOT_STARTED"
},

### **Final Analysis**

**Existing Flow** 

1. User confirms pledging of funds 
2. KFS link opens 
    1. I agree : Handled 
    2. I disagree : **Getting callback but not handled in backend & UI** 
        1. In app : We show BAJAJ’s link (Document Rejected) 
        2. In Web : We show a generic loader 
3. Agreement link opens 
    1. I agree : Handled 
    2. I disagree : **Getting callback but not handled in backend & UI**
        1. In app : We show BAJAJ’s link (Document Rejected) 
        2. In Web : We show a generic loader 

**New Flow** 

1. User confirms pledging of funds 
2. Application, KFS, Agreement common link 
    1. Application 
        1. I agree 
    2. KFS 
        1. I agree : Will not get a callback 
        2. I disagree : **Not getting a callback (raised)** 
    3. Agreement 
        1. I agree : Handled 
        2. I disagree : Getting a callback, will be handled 

**Issues** 

1. Not getting KFS reject callback 
2. Should we give an option to re-generate KFS? 
    1. BAJAJ do a hardpull, though there is a dedupe check at CIBIL’s end. 
3. What should be the copy of screen KFS Reject handling screen 
    1. Current copy “Contact our team to proceed or to un-pledge your mutual funds” 
    2. https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=9837-59660&t=fNlH40ueC2ZGfHZW-1

---

1. User taps on “Confirm & get OTP” at the pledge step 
2. We hit the request for SFDC creation
3. We get get SFDC response
4. We get KFS link callback 
    1. User accepts KFS : We show the CTA of “continue to sign agreement step” to the user 
    1. User rejects KFS : App is just stuck at a modal with message “Waiting for response - Please wait while we process your request”.  with no button/CTA available for the user to move back or ahead in the flow. **User is blocked.** 

[LoanApplicationJourney_KFS_Agreement.mov](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/LoanApplicationJourney_KFS_Agreement.mov)

### New Flow

**Pop up option** 

1. At KFS step 
    1. If user REJECTS the KFS → We can show a pop-up to the user saying
2. If user drops-off 
    1. Re-create SFDC 

**Screen option** 

**Re-query** 

![Screenshot 2024-10-04 at 1.51.53 PM.png](BAJAJ%20New%20KFS+Agreement%20flow/Screenshot_2024-10-04_at_1.51.53_PM.png)

![Screenshot 2024-10-04 at 1.52.15 PM.png](BAJAJ%20New%20KFS+Agreement%20flow/Screenshot_2024-10-04_at_1.52.15_PM.png)