# BAJAJ : New KFS+Agreement flow (with re-query)

: Ameya Aglawe
Created time: September 19, 2024 6:27 PM
Status: Pending Review
Last edited: October 11, 2024 12:42 PM
Owner: Ameya Aglawe

# **What problem are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload as well as results in customer drop-offs.

---

# **How do we measure success?**

- Number of customers who moved forward to sanction or disbursement/withdrawal
- Incremental number of customer who moved forward to sanction
- Reduction in man hours spent by Ops team for the re-generating agreement link/re-creating lender application.
- Reduction in number of users going through BAJAJ application with their CIBIL score impacted
- Reduction in #user stuck at Agreement step.
- **North star :** #applications completed per week with BAJAJ

---

# **How are others solving this problem?**

Currently, lenders who work with partners typically allow the LSP (partners) to retrigger the KFS through APIs. This could be either because customer asked for change in terms of if the lender changes the terms of the offer.

---

# **What is the solution?**

## Requirements overview (optional)

### User stories / User flow

**Existing Flow** 

1. User confirms pledging of funds by tapping on “confirm & get OTP” CTA on the Pledge step 
2. A modal with messaging “Rs xxxx unlocked successfully” opens up. 
3. User taps on continue 
4. A screens opens up with a loader & messaging “Generating agreement link” 
5. Once the loader is complete & we receive the callback of KFS link 
6. Agreement step anchor page opens up with state - 
    1. Review & accept key terms (highlighted) 
    2. Review & sign agreement (disabled) 
7. User taps on “Continue” CTA
8. KFS link opens up : User can scroll to the bottom of the documents and can see 2 CTA 
    - I agree
        1. If user taps on I agree KFS document shows messaging “Thanks for showing interest” 
        2. A modal opens up with messaging “Key terms accepted” with the CTA of “Continue”.  
        3. User taps on “Continue” and lands of Agreement step anchor page again with state 
            1. Review & accept key terms (marked completed) 
            2. Review & sign agreement  (highlighted) 
        4. User taps on “Continue to sign agreement” 
        5. Agreement link opens up : User can scroll to the bottom of the documents and can see 2 CTA
            - I Agree
                1. If user taps on I agree KFS document shows messaging “Thanks for showing interest” 
                2. A modal opens up with messaging “Agreement submitted” with the CTA of “Proceed”. 
                3. User taps on “Proceed” & goes to the auto-pay step. 
            - I disagree
                1. Initial state -
                    1. Our platform shows a generic loader
                    2. BAJAJ’s link shows “You have rejected the document”
                2. If user taps on back button → taps on continue application → taps “start” → Agreement anchor page opens up with CTA “Continue to sign agreement”
    - I disagree
        1. In app : We show BAJAJ’s link which has the messaging - “You have rejected the document” 
        2. In Web : 
            1. Initial state - 
                1. Our platform shows a generic loader
                2. BAJAJ’s link shows “You have rejected the document” 
            2. If user taps on back button →  taps on continue application → taps “start” → Agreement anchor page opens up with CTA “Continue to sign agreement” 

**New Flow** 

- User confirms pledging of funds by tapping on “confirm & get OTP” CTA on the Pledge step
    
    **Confirm pledge** 
    
    ![image.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/image.png)
    
    **Verifies OTP (CAMS & Kfin)** 
    
    ![image.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/image%201.png)
    
- A modal with messaging “Rs xxxx unlocked successfully” opens up.
    
    ![image.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/image%202.png)
    
- User taps on continue
    
    ![image.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/image%203.png)
    
- A screens opens up with a loader & messaging “Generating agreement link”
    
    ![image.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/image%204.png)
    
- Once the loader is complete [and we receive the callback of the Application, KFS, Agreement common link]
- Agreement step anchor page (new) opens up
    
    ![Screenshot 2024-09-30 at 3.22.09 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-09-30_at_3.22.09_PM.png)
    
- User taps on “Review Agreement”
    
    Application, KFS, Agreement common link opens. 
    
    1. Application form page shows up first 
        - User can scroll to bottom and see a single CTA “I agree”
            
            ![Screenshot 2024-09-30 at 3.18.51 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-09-30_at_3.18.51_PM.png)
            
        - User taps on “I agree”
    2. KFS page opens up as user taps on “I agree” on application form 
        - User can scroll to the bottom and see 2 CTAs “I agree” and “I disagree”
            
            ![Screenshot 2024-09-30 at 3.26.58 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-09-30_at_3.26.58_PM.png)
            
        - User taps on I agree
            - Agreement page opens up : User can scroll to the bottom and see 2 CTAs “I agree” & “I disagree”
                - UI
                    
                    ![Screenshot 2024-09-30 at 3.27.59 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-09-30_at_3.27.59_PM.png)
                    
                - User taps on I agree
                    - A modal would open with messaging “Agreement submitted” with CTA of “Proceed”
                    - User taps on “Proceed” & moves on to the auto-pay step
                - User taps on I disagree
                    1. We will show the UI 
                        1. Messaging : You have declined the Agreement 
                        2. CTA : Review Agreement 
                        3. User taps on “Review Agreement” CTA 
                            - UI
                                
                                ![Screenshot 2024-10-11 at 12.38.39 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-10-11_at_12.38.39_PM.png)
                                
                        4. A screens opens up with a loader & messaging “Generating agreement link” 
                        5. Once the loader is complete [and we receive the callback of the Application, KFS, Agreement common link]
                        6. Agreement step anchor page (new) opens up 
                        7. User taps on “Review Agreement” 
                        8. Application, KFS, Agreement common link opens.
                        9. User starts with the Application → KFS → Agreement flow again within the same link 
                        10. **Edge case :** 
                            - UI
                                
                                ![Screenshot 2024-09-30 at 5.58.37 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-09-30_at_5.58.37_PM.png)
                                
                            1. User confirms pledging of funds by tapping on “confirm & get OTP” CTA on the Pledge step → SFDC is generated → But we do not receive the callback of Agreement link 
                            2. Ops team can use the admin tool “Regenerate Agreement Link”. Here the input field will be application_id of the user. [Currently all ops team members don’t have access to this] 
        - User taps on I disagree
            1. We will show the UI 
                1. Messaging : You have declined the Agreement 
                2. CTA : Review Agreement 
                3. User taps on “Review Agreement” CTA 
                    - UI
                        
                        ![Screenshot 2024-10-11 at 12.41.56 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-10-11_at_12.41.56_PM.png)
                        
                4. A screens opens up with a loader & messaging “Generating agreement link” 
                5. Once the loader is complete [and we receive the callback of the Application, KFS, Agreement common link]
                6. Agreement step anchor page (new) opens up 
                7. User taps on “Review Agreement” 
                8. Application, KFS, Agreement common link opens.
                9. User starts with the Application → KFS → Agreement flow again within the same link 
                10. **Edge case :** 
                    - UI
                        
                        ![Screenshot 2024-09-30 at 5.58.37 PM.png](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/Screenshot_2024-09-30_at_5.58.37_PM.png)
                        
                    1. User confirms pledging of funds by tapping on “confirm & get OTP” CTA on the Pledge step → SFDC is generated → But we do not receive the callback of Agreement link 
                    2. Ops team can use the admin tool “Regenerate Agreement Link”. Here the input field will be application_id of the user. [Currently all ops team members don’t have access to this] 

[NewApplicationFormBAJAJ.pdf](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/NewApplicationFormBAJAJ.pdf)

[NewKFSFormatBAJAJ.pdf](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/NewKFSFormatBAJAJ.pdf)

[BAJAJAgreementNew.pdf](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/BAJAJAgreementNew.pdf)

## Technical Requirements

- The anchor page for agreement step with new copy
- Callbacks on different user actions -
    - Application accept - No callback
    - KFS accept - No callbacks
    - Agreement accept
        
        ```jsx
        {"loan_application_number":"62081719127547","KFSstatus":"116.73.243.197 || 2024-09-06 17:10:08 || SUCCESS","type":"esignature","status":"116.73.243.197 || 2024-09-06 17:11:01 || SUCCESS"}
        ```
        
    - KFS reject
        
        ```jsx
        {"loan_application_number":"62081719632112","KFSstatus":"116.73.243.197 || 2024-09-06 18:50:27 || REJECT","type":"esignature","status":"Acceptance Pending"} 
        ```
        
    - Agreement reject
        
        ```jsx
        {"loan_application_number":"62081719632112","KFSstatus":"Acceptance Pending","type":"esignature","status":"116.73.243.197 || REJECT"}
        ```
        
- In cases where we get the callback of KFS & Agreement rejection
    - We will show a UI with
        - Messaging : You have declined the Agreement
        - CTA : Review Agreement
    - Once user taps on “Review Agreement” CTA
        - We will hit the re-query API & get new agreement link.
        - Generating agreement link loader will be shown
        - Take the user back to the Agreement anchor page
        - User taps on review agreement & link opens up
        - Poll status of the Agreement link
            - User accepts all documents
                - We get the SUCCESS callbacks
                    
                    ```jsx
                    {"loan_application_number":"62081719127547","KFSstatus":"116.73.243.197 || 2024-09-06 17:10:08 || SUCCESS","type":"esignature","status":"116.73.243.197 || 2024-09-06 17:11:01 || SUCCESS"}
                    ```
                    
                - Take user to next step (Auto-pay)
            - User rejects KFS/Agreement
                - We get the REJECT callback
                - We will show a UI with
                    - Messaging : You have declined the Agreement
                    - CTA : Review Agreement

---

# **Design**

---

Figma : https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=9837-59660&t=pVjivWu47PjJD9K3-1

# **Analytics**

Below are the metrics to be logged and tracked.

- Number of customers for whom KFS bundle was created.
- Number of customers for whom KFS was actioned by the customer.
- Number of customers for whom KFS was accepted by the customer.
- Number of customers for whom KFS was rejected by the customer.
- Number of customers who accepted the KFS after rejection
- TAT for customers to accept the KFS bundle

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

Training to be done with the sales & ops team.

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Training for sales & ops
- [ ]  Business
    - [ ]  
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
        1. User accepts agreement : We show users CTA of “proceed” with modal of Agreement submitted message
        2. User rejects agreement : App is just stuck at the generic loader in our app, with no button/CTA available for the user to move back or ahead in the flow. **User is blocked**
    2. User rejects KFS : App is just stuck at a modal with message “Waiting for response - Please wait while we process your request”.  with no button/CTA available for the user to move back or ahead in the flow. **User is blocked.** 

[LoanApplicationJourney_KFS_Agreement.mov](BAJAJ%20New%20KFS+Agreement%20flow%20(with%20re-query)/LoanApplicationJourney_KFS_Agreement.mov)

### New Flow

**Pop up option** 

1. At KFS step 
    1. If user REJECTS the KFS → We can show a pop-up to the user saying
        1. “You REJECTED the KFS. If you wish to continue ahead with the load application, please select Regenerate KFS”
        CTA → Regenerate KFS : CANCEL 
        2. “You REJECTED the KFS. In order to proceed with application please select Regenerate KFS”
        CTA → Regenerate KFS : CANCEL 
        3. “You REJECTED the KFS. You wish to generate the KFS again?”
        CTA → YES: NO
2. If user drops-off 
    1. Re-create SFDC 

You have declined your loan terms. 

**Screen option** 

### User stories

- User completes the post-pledge step by tapping on “Confirm pledge” button → Agreement link loader screen shows up → Agreement anchor screen opens up → User taps on “Continue” button → Application+KFS+Agreement link opens up :
    - User accepts all the documents → User proceeds to Auto-Pay screen → User sets up the mandate
    - User rejects KFS or agreement → We show “You have rejected the agreement” callout & give a CTA to “Review Agreement” to the user → User taps on “Review Agreement” button → Agreement link loader screen shows up → Agreement anchor screen opens up → User taps on “Continue” button → Application+KFS+Agreement link opens up

## BAJAJ Go Live test plan

1. Test for new application 
2. Test for enhancement 
3. Test for renewal applications 
    1. Callbacks for - 
        1. KFS reject 
        2. KFS accept 
        3. Agreement reject 
        4. Agreement accept 
    2. For Agreement accept, are we moving the application to Auto-pay 
    3. If we are re-generating the agreement link then what are the callbacks for - 
        1. KFS reject 
        2. KFS accept 
        3. Agreement reject 
        4. Agreement accept 

We can’t directly open the KFS links because - 

1. In BAJAJ’s loan terms document the document type is not very clear
2. In our flow we show in the bottom drawer 

No bottom stick & does not clearly call out what the document

[

{

"TransactionID": **null**,

"UniqueRecordID": "1000835165",

"FirstName": "MANISH",

"MiddleName": "SUDHIR",

"LastName": "PATIL",

"BOCodeSecurity": "",

"FatherOrHusbandName": "SUDHIR",

"HeadOfFamily": "No",

"BOCodeMF": "",

"FamilyID": "1298",

"FamilyName": "LAS_DIGITAL",

"GroupID": "1210",

"GroupName": "LAS_DIGITAL",

"CommenceOn": "2023-09-09",

"BOCodeDebt": "",

"TaxStatusCode": "01",

"TaxStatus": "Individual",

"TaxPercent": "0",

"PoolAccount": "Yes",

"UCC": "",

"BOCodeNBFC": "",

"CategoryCode": "20",

"Category": "Platinum",

**"CommonClientCode": null,**

"BorrowerIndustryID": "",

"BorrowerIndustryName": "",

"TaxIdOrPAN": "APLPP8042S",

"TAN_No": "",

"GIR_No": "",

"TaxWaiverInFile": "",

"CircleOrWardOrDist": "",

"AadharCardNo": "XXXXXXXX4655",

"RBIApprovalNo": "",

"RBIApprovalDate": "",

"TaxDeductionStatus": "",

"SEBIRegistrationNo": "",

"Address1": "K-2601 RUSTAMJEE AZZIANO MUMBAI NASIK ",

"Address2": "HIGHWAY MAJIWADA THANE NEXT TO RUSTAMJEE ",

"Address3": "CAMBRIDGE SCHOOL Thane Thane Thane Thane ",

"City": "Thane",

"PinCode": "400601",

"StateID": "27",

"State": "Maharashtra",

"CountryID": "5",

"Country": "India",

"ResTelNo": "",

"MobileNo": "9820652320",

"Fax": "",

"Email": "mpatil3084@gmail.com",

"OffAddress1": "",

"OffAddress2": "",

"OffAddress3": "",

"OffCity": "",

"OffPinCode": "",

"OffStateID": "",

"OffState": "",

"OffCountryID": "",

"OffCountry": "",

"OffTelNo": "",

"OffMobileNo": "",

"OffFax": "",

"OffEmail": **null**,

"DefaultMailing": "Home",

"DeciderName": **null**,

"DeciderTelNo": **null**,

"DeciderFax": **null**,

"OperationPersonName": **null**,

"OperationPersonTelNo": **null**,

"OperationPersonFax": **null**,

"Designation": **null**,

"OtherAddress1": **null**,

"OtherAddress2": **null**,

"OtherAddress3": **null**,

"OtherCity": **null**,

"OtherPinCode": **null**,

"LoanRequests": "Investments In Securities",

"DOB": "30-Oct-1984",

"GuardianName": **null**,

"PlaceOfBirth": **null**,

"Salutation": **null**,

"Gender": "Male",

"MaritalStatus": "Married",

"SpouseName": **null**,

"WeddingDate": **null**,

"SpouseDOB": **null**,

"OccupationCode": "7",

"ProfessionalCode": **null**,

"SalariedCode": **null**,

"OtherOccupation": **null**,

"OccupationType": **null**,

"GrossAnnualIncome_InLakhs": **null**,

"EstFinancialWealth_InLakhs": **null**,

"NameOfEmployer": **null**,

"YearsOfEmploymentOrBusiness": **null**,

"EducationalQualification": **null**,

"PersonalAddress1": **null**,

"PersonalAddress2": **null**,

"PersonalAddress3": **null**,

"Nationality": "Indian Citizen",

"NationalityIfOther": **null**,

"NatureOfBusiness": **null**,

"VoterID": **null**,

"PassportNo": **null**,

"PlaceOfIssue": **null**,

"PassportIssueDate": **null**,

"PassportExpiryDate": **null**,

"InterCompany": "No",

"Jurisdiction": **null**,

"DateOfIncoporation": "01-01-1990",

"DateOfCommencement": **null**,

"CorporateNatureOfBusiness": **null**,

"LegalConstitutionID": **null**,

"LegalConstitution": **null**,

"RegisteredOfficeDUNSNumber": **null**,

"BorrowerDUNSNumber": **null**,

"EstFinancialWealth_InMillion": **null**,

"CorporateGrossAnnualIncome_InLakhs": **null**,

"FGIInterCompanyCode": "",

"Email_YesNo": "mpatil3084@gmail.com",

"Fax_YesNo": "",

"Mail_YesNo": **null**,

"Hand_YesNo": **null**,

"AlertEmail_YesNo": "",

"AlertFax_YesNo": "",

"AlertSMS_YesNo": "",

"EmailOnDeactivationofAccount": **null**,

"EmailOnCorporateAction": **null**,

"PromotionalMaterial": **null**,

"EmailOnCloseOfAccount": **null**,

"EmailOnFreezeOfAccount": **null**,

"SharePhoneOrEmail": **null**,

"Statement": **null**,

"ChangeInClientInformation": **null**,

"InternetID": **null**,

"ClientBankDetailsUpdate": [

{

"Action": **null**,

"BankId": "0",

"BankName": "HDFC Bank",

"BankBranch": "MUMBAI - POWAI",

"MICR": "400240039",

"IFSC": "HDFC0000239",

"AccountNo": "02391140093584",

"FirstHolderName": "Manish Sudhir Patil",

"SecondHolderName": **null**,

"ThirdHolderName": **null**,

"AcctOpeningDt": "12-09-2018",

"DefaultAccount": "Yes",

"Accounttype": "Savings",

"BankDtl_CCY": "INR",

"PaymentMode": "Account/Fund Transfer",

"PaymentCode": "I",

"LocationCode": **null**

},

{

"Action": **null**,

"BankId": "0",

"BankName": "STATE BANK OF INDIA",

"BankBranch": "MUMBAI - POWAI",

"MICR": "110002006",

"IFSC": "SBIN0000745",

"AccountNo": "02391140093589",

"FirstHolderName": "Manish Sudhir Patil",

"SecondHolderName": **null**,

"ThirdHolderName": **null**,

"AcctOpeningDt": "12-09-2018",

"DefaultAccount": "No",

"Accounttype": "Savings",

"BankDtl_CCY": "INR",

"PaymentMode": "Account/Fund Transfer",

"PaymentCode": "I",

"LocationCode": **null**

}

],

"ClientBrokerDetailsUpdate": [

{

"Action": **null**,

"ExchangeId": "",

"ExchangeName": "",

"BrokerId": "",

"BrokerName": "",

"Address": **null**,

"AccountNo": "",

"FirstHolderName": "",

"AccountOpeningDt": ""

}

],

"ClientDPDetailsUpdate": [

{

"Action": **null**,

"Depository": "NSDL",

"DPName": "IN303116",

"DPMainCode": "268",

"DPAccountNo": "13742676",

"DpId": "IN303116",

"FirstHolderName": "MANISH SUDHIR PATIL",

"SecondHolderName": **null**,

"ThirdHolderName": **null**,

"AcctOpeningDt": "12-06-2018",

"POAYN": "Yes",

"DefaultDp": "No",

"AccountType": "1",

"AccountTypeName": "Equity",

"PrimaryHolderYN": "Yes"

}

],

"ClientKeyManagementPersonnelUpdate": [

{

"Action": **null**,

"Designation": "NA",

"Address": "NA",

"DUNSNo": **null**,

"NamePrefix": **null**,

"FullName": "NA",

"Relation": "",

"RelatedType": "",

"Gender": "NA",

"PANNo": **null**,

"PassportNo": **null**,

"VoterId": **null**,

"Address2": **null**,

"Address3": **null**,

"City": "",

"StateCode": "27",

"CountryId": "5",

"PinCode": **null**,

"AadharCardNo": **null**,

"Contactno": **null**

}

],

"ClientCreditFacilityUpdate": [

{

"Action": **null**,

"BankOrInstitutionOrCompanyName": "",

"AccountNo": "",

"AmountOfLoan": **null**,

"TenureOfLoan": **null**,

"EMIAmount": **null**

}

],

"ClientCreditCardUpdate": [

{

"Action": **null**,

"CCBankOrInstitutionOrCompanyName": "",

"CreditCardNo": "",

"DateOfExpiry": "",

"TypeOfCard": ""

}

],

"ClientRelatedCompaniesUpdate": [

{

"Action": **null**,

"RelatedCompanyID": "",

"RelatedCompanyName": "",

"RelationWithCompany": "",

"RelationID": "",

"Received": "",

"DateOfIntimation": ""

}

],

"ClientIntroducerUpdate": [

{

"ExistingClient": "",

"IntroducerName": "",

"AddressOfIntroducer1": **null**,

"AddressOfIntroducer2": **null**,

"AddressOfIntroducer3": **null**,

"MappinID": **null**,

"IntroducerClientCode": **null**,

"NameOfEmployeeInterviewed": **null**,

"DesginationOfEmployeeInterviewed": **null**

}

],

"ClientBranchDetailsUpdate": [

{

"Action": **null**,

"BranchCode": "386",

"BranchName": "DELHI RAJENDRA PLACE",

"LocationID": "02",

"LocationName": "New Delhi",

"RegionName": **null**,

"WefDate": "21-Sep-2023"

}

],

"ClientSubBrokerDetailsUpdate": [

{

"Action": **null**,

"SubBrokerID": **null**,

"SubBrokerName": **null**,

"WefDate": "21-Sep-2023"

}

],

"ClientPrimaryRMUpdate": [

{

"Action": **null**,

"ManagerCode": "11",

"ManagerName": "JALINDAR AVHAD",

"ManagerEmailID": "Jalindar.Avhad@tatacapital.com",

"ManagerMobileNo.": "9870003436",

"WefDate": "21-Sep-2023"

}

],

"ClientSecondaryRMUpdate": [

{

"Action": **null**,

"ManagerCode": "",

"ManagerName": "",

"ManagerEmailID": **null**,

"ManagerMobileNo.": **null**,

"WefDate": ""

}

],

"ClientGSTDetailsUpdate": [

{

"Action": **null**,

"StateCode": "22",

"State": "Maharashtra",

"GSTIN": "",

"DefaultLocation": "yes",

"IsGSTExempted": "no",

"GSTExemptionDesc": **null**,

"IsRelatedParty": "no",

"RelatedPartyDesc": **null**

}

],

"OtherDetails": [

{

"Employee": **null**,

"Employee Code": **null**,

"Remarks 1": **null**,

"Remarks 2": **null**

}

]

}

]

{

"ClientMasterUpdateData": [

{

"UniqueRecordID": "1000835165",

"RecordStatusCode": "0",

"Remarks": "Success"

}

],

"status": {

"Status": "Success",

"Code": "01",

"Remarks": ""

}

}

Test cases for the API 

1. Happy flow 
2. KFS Reject
3. Agreement Reject 
4. Re-query
    1. KFS Reject 
    2. Agreement Reject 
    3. Happy flow  

1. I agree
2. I disagree
    1. Show to the user that they have rejected the KFS/Agreement & gives CTA which re-generates agreement(both app & web) 
    2. Callback format
        1. {"loan_application_number":"62081719632112","KFSstatus":"116.73.243.197 || 2024-09-06 18:50:27 || REJECT","type":"esignature","status":"Acceptance Pending"} 
3. Agreement 
    1. I agree : Handled, will move the user to “Auto-Pay” step 
        1. callback format : 
        {"loan_application_number":"62081719127547","KFSstatus":"116.73.243.197 || 2024-09-06 17:10:08 || SUCCESS","type":"esignature","status":"116.73.243.197 || 2024-09-06 17:11:01 || SUCCESS"}
    2. I disagree : Getting a callback (both app & web) 
        1. Show to the user that they have rejected the KFS/Agreement & gives CTA which re-generates agreement (UI)
            1. callback format : {"loan_application_number":"62081719632112","KFSstatus":"Acceptance Pending","type":"esignature","status":"116.73.243.197 || REJECT"} 
4. KFS/Agreement regenerated (this is still not working as expected) 
    1. KFS & Agreement accepted 
        1. {"loan_application_number":"62081783992771","KFSstatus":"2401:4900:16eb:4837:7547:a442:45da:3337 || 2024-09-25 15:22:27 || SUCCESS","type":"esignature","status":"2401:4900:16eb:4837:7547:a442:45da:3337 || 2024-09-25 15:23:03 || SUCCESS"}
    2. KFS rejected 
        1. {"loan_application_number":"62081719632112","KFSstatus":"116.73.243.197 || 2024-09-06 18:50:27 || REJECT","type":"esignature","status":"Acceptance Pending"} 
    3. KFS accepted & Agreement rejected 
        1. {"loan_application_number":"62081719632112","KFSstatus":"Acceptance Pending","type":"esignature","status":"116.73.243.197 || REJECT"}

- If user rejects the KFS or agreement, we show a callout in the UI and give a
    - Primary CTA : Review Agreement
    - Secondary CTA : Contact Support