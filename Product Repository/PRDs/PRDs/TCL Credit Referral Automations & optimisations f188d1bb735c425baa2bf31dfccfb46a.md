# TCL Credit Referral Automations & optimisations

: Ameya Aglawe
Created time: October 22, 2024 2:49 PM
Status: In progress
Last edited: November 26, 2024 4:15 PM

# **What problem are we solving?**

Daily 20 credit referral tickets are being created and it is taking a lot of Ops bandwidth for reviewing each of these applications, approving it from their end and keeping a track over these application for lender approval. 

---

# **How do we measure success?**

- Man-hours spent in reviewing all credit referral application < 1 hour per day.
- TAT for application completion to reduce by ~20 minutes

---

# **How are others solving this problem?**

---

# **What is the solution?**

- Credit referral current handling
    
    
    | **Step**  | **Check**  | **Action** |
    | --- | --- | --- |
    | KYC_Documents | PAN-Aadhar name match score | - <70% : Credit referral
    - > 70% : User continues the application |
    | KYC_Documents | Match score between user’s live photo and KYC photo  | - <70% : Credit referral
    - > 70% : User continues the application |
    | CIBIL_Check | CIBIL score check  | - < 650 : Hard reject (Ops gets a mail) 
    - > 650 : User continues the application |
    |  | Posidex check  | - Negative : Credit referral
    - Positive (001) : User continues the application |
    | Bank verification  | PAN-Bank name match score  | - <70% : Credit referral 
    - > 70% : User continues the application 
     |
- Documents taken at each of the steps
    
    
    | **Check**  | **Document taken from the user** | **Ops check**  |
    | --- | --- | --- |
    | KYC Documents  | Passport, DL (name & picture), PAN, Voter Id  | Ops checks name in PAN with the supporting documents, and approve it unless there is a major name mis-match |
    | KYC Photo verification  | -  | Ops checks if the photo of the user is front facing and is authentic |
    | CIBIL_Check  | -  | Hard Reject, Ops changes lender  |
    | Posidex  | SOA of existing/previous loans (only if TATA Ops ask for it)  | If CIBIL > 650 they approve from their side, and pass the application to lender. If lender asks for SOA of existing loans : Ops provides the documents |
    | Bank verification  | Cancel cheque, Bank Statement, Passbook  | Ops check if PAN & bank name are roughly matching. and also if IFSC/Account number is matching with supporting documents |
- Credit referral new handling
    
    
    | **Check Step**  | Change in handling | **Check**  | **Threshold** | **Actions** |
    | --- | --- | --- | --- | --- |
    | KYC_Documents | Yes  | PAN-Aadhar name match score | match score < 70 | - Straight through process  |
    | KYC_Documents | Yes | Photo match score  | match score <70  | - Straight through process |
    | CIBIL_Check  | Yes  | CIBIL score  | 0 < CIBIL score < 650  | - Application blocked  |
    |  |  |  | CIBIL = -1 with limit > 20L  | - Straight through process |
    |  |  | Posidex code  | CIBIL > 650 (posidex negative) | - Straight through process  |
    | Bank Verification  | Yes  | PAN-bank name match score  | match score < 70 | - Straight through process |
- Mail trigger/Zendesk ticketing system
    - Email trigger system
        
        
        | **Scenario**  | **Handling** |
        | --- | --- |
        | When a credit referral is raised and rejected at our end | Create zendesk ticket  |
        | When a credit referral is raised to lender | Create zendesk ticket  |
        | Lender approves | Top up on the same ticket notifying the approval of the case |
        | Lender rejects | Top up on the same ticket notifying the rejection of the case |
    - Email details (with template IDs)
        - Volt Rejected - CIBIL < 650 (d-9c3eae3916d0468c848d47bb69be5e81)
            - Header
                
                 [Rejected] Credit referral- {{application_id}} - {{full_name}}
                
            - Template
                
                <aside>
                💡
                
                We are rejecting the credit referral for this application application. Kindly contact the sales & ops team to take this forward. 
                
                Customer name :
                
                Customer PAN :
                
                Application ID :
                
                Application type :
                
                Credit referral reason : CIBIL Score < 650 
                
                Webtop ID :
                
                Opportunity ID :
                
                Credit referral ID :
                
                **Details -** 
                
                Posidex : 
                
                CIBIL score :
                
                {Attachments}
                
                </aside>
                
            - Send grid template ID :
        - Zendesk ticket creation in STP
            - Email header
                
                 Credit referral STP - {{application_id}} - {{full_name}}
                
            - Email template (with sendgrid template IDs)
                - General email template
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    Details:
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Match percentage :
                    
                    Name as per Bank Account :
                    
                    Name as per PAN (%) :
                    
                    Name as per AADHAR (%) :
                    
                    Photo match % :
                    
                    Posidex : negative 
                    
                    CIBIL :
                    
                    {Attachments}
                    
                    </aside>
                    
                - For PAN-Aadhar name mismatch(d-a189b549295f4befa44181052b3c30aa)
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : PAN-Aadhar match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    PAN-Aadhar match percentage : 
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For PAN-Bank name mismatch(d-f4aff836f96e412b97efca97862f3093)
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : PAN-Bank name match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Name as per Bank Account :
                    
                    PAN-Aadhar match percentage : 
                    
                    PAN-Bank match percentage : 
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For Photo verification (d-9aaa030926174b9ab34e309933697ab8)
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : Photo match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Photo match % :
                    
                    {Attachments - Customer’s Photo & Aadhar Photo}
                    
                    </aside>
                    
                - For Posidex negative (d-c25aeb511d1640d79f16dfeba9ccd618)
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : Posidex negative 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Posidex : negative
                    
                    CIBIL score :
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For NTC (d-a099acfaefb641669959dad77f06903a)
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : New to credit customer with limit > 20L
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    Posidex : 
                    
                    CIBIL score :
                    
                    Credit Limit : 
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
        - STP Lender approval (d-c2d069f72605472099408d8c24e1a847)
            
            <aside>
            💡
            
            Hi Team,
            
            The lender has rejected the credit referral. Please ask the sales & support team to contact the customer to take this forward.
            
            Regards
            Team Volt 
            
            </aside>
            
        - STP Lender rejection (d-1a0b2263db424a839f9d9d2e5a32275f)
            
            <aside>
            💡
            
            Hi Team,
            
            The lender has approved the credit referral. 
            
            Regards
            Team Volt 
            
            </aside>
            
- Credit referral request/response
    
    **Request :** 
    
    ```jsx
    {
        "LeadId": "226344635",
        "RefId": "2244940402952849110",
        "applSource": "LAS",
        "assignTo": "CM",
        "stage": "4",
        "stagedescription": "OKYC name mismatch",
        "webtopId": "291BZ8640463"
    }
    ```
    
    **Response :** 
    
    ```jsx
    {
        "Assign_Case_Response": {
            "Status": "Success",
            "Message": "Case has been assigned to CM",
            "LeadId": "226344635",
            "RefID": "2244940402952849110"
        },
        "RetStatus": "SUCCESS",
        "sysErrorMessage": "null",
        "sysErrorCode": "null"
    }
    ```
    
    **Callback :** 
    
    ```jsx
    {
      "applSource": "LAS",
      "leadId": "228204425",
      "managerDecision": "Rejected",
      "refId": "5688102400937952287",
      "stage": "3",
      "stageDescription": "Application has been recommended for Credit approval .Dedupe is negative",
      "webtopId": "291BZ8646200"
    }
    ```
    
- SendGrid Templates
    - PAN Aadhar name mismatch
        
        ```jsx
        <p>Hi Team,</p>
                                    <p>The credit referral is raised to the lender.  </p>
                                    
                                    <ol style="margin: 20px 0 20px 20px; padding: 0;">
                                        <li>Customer's name: {{{full_name}}}</li>
                                        <li>Customer's PAN: {{{account_holderpan}}}</li>
                                        <li>Application ID: {{{application_id}}} </li>
                                        <li>Application type: {{{application_type}}} </li>
                                        <li>Credit referral reason: PAN-Aadhaar name mismatch</li>
                                        <li>Webtop ID: {{{webtop_id}}}</li>
                                         <li>Opportunity ID: {{{opporunity_id}}}</li>
                                        <li>Name as per PAN: {{{PAN_name}}}</li>
                                        <li>Name as per Aadhaar: {{{Aadhaar_name}}}</li>
                                        <li>PAN-Aadhar name match score: {{{PAN_Aadhaar_name_match_score}}}</li>
                                    </ol>
                                    
                                    <p>Please find the supporting documents and other reports of the customer in the "Get all documents" admin action.</p>
                                    <p>Regards,<br>Team Volt</p>
                                </td>
                            </tr>
        
        ```
        
    - PAN Bank name mismatch
        
        ```jsx
         <p>Hi Team,</p>
                                    <p>The credit referral is raised to the lender.   </p>
                                    
                                    <ol style="margin: 20px 0 20px 20px; padding: 0;">
                                        <li>Customer's name: {{{full_name}}}</li>
                                        <li>Customer's PAN: {{{account_holderpan}}}</li>
                                        <li>Application ID: {{{application_id}}} </li>
                                        <li>Application type: {{{application_type}}} </li>
                                        <li>Credit referral reason: PAN-Bank name mismatch</li>
                                        <li>Webtop ID: {{{webtop_id}}}</li>
                                         <li>Opportunity ID: {{{opporunity_id}}}</li>
                                        <li>Name as per PAN: {{{PAN_name}}}</li>
                                        <li>Name as per Bank: {{{Bank_name}}}</li>
                                        <li>PAN-Bank name match score: {{{PAN_Bank_name_match_score}}}</li>
                                    </ol>
                                    
                                    <p>Please find the supporting documents and other reports of the customer in the "Get all documents" admin action.</p>
                                    <p>Regards,<br>Team Volt</p>
                                </td>
                            </tr>
        
        ```
        
    - Live photo verification
        
        ```jsx
        <p>Hi Team,</p>
                                    <p>The credit referral is raised to the lender.   </p>
                                    
                                    <ol style="margin: 20px 0 20px 20px; padding: 0;">
                                        <li>Customer's name: {{{full_name}}}</li>
                                        <li>Customer's PAN: {{{account_holderpan}}}</li>
                                        <li>Application ID: {{{application_id}}} </li>
                                        <li>Application type: {{{application_type}}} </li>
                                        <li>Credit referral reason: Live photo mismatch</li>
                                        <li>Webtop ID: {{{webtop_id}}}</li>
                                         <li>Opportunity ID: {{{opporunity_id}}}</li>
                                        <li>Photo match score: {{{photo_match_score}}}</li>
                                    </ol>
                                    
                                    <p>Please find the supporting documents and other reports of the customer in the "Get all documents" admin action.</p>
                                    <p>Regards,<br>Team Volt</p>
                                </td>
                            </tr>
        ```
        
    - Posidex negative
        
        ```jsx
        <p>Hi Team,</p>
                                    <p>The credit referral is raised to the lender.</p>
                                    
                                    <ol style="margin: 20px 0 20px 20px; padding: 0;">
                                        <li>Customer's name: {{{full_name}}}</li>
                                        <li>Customer's PAN: {{{account_holderpan}}}</li>
                                        <li>Application ID: {{{application_id}}} </li>
                                        <li>Application type: {{{application_type}}} </li>
                                        <li>Credit referral reason: Posidex negative</li>
                                        <li>Webtop ID: {{{webtop_id}}}</li>
                                         <li>Opportunity ID: {{{opporunity_id}}}</li>
                                        <li>Posidex code: {{{posidex_code}}}</li>
                                        <li>CIBIL score: {{{CIBIL_score}}}</li>
                
                                    </ol>
                                    
                                    <p>Please find the supporting documents and other reports of the customer in the "Get all documents" admin action.</p>
                                    <p>Regards,<br>Team Volt</p>
                                </td>
                            </tr>
        ```
        
    - CIBIL < 650
        
        ```jsx
          <p>Hi Team,</p>
                                    <p> We have rejected the credit referral as CIBIL score of the customer is less than 650. Kindly ask the sales or support team to move ahead with alternate lender for this application.</p>
                                    
                                    <ol style="margin: 20px 0 20px 20px; padding: 0;">
                                        <li>Customer's name: {{{full_name}}}</li>
                                        <li>Customer's PAN: {{{account_holderpan}}}</li>
                                        <li>Application ID: {{{application_id}}} </li>
                                        <li>Application type: {{{application_type}}} </li>
                                        <li>Credit referral reason: CIBIL score < 650</li>
                                        <li>Webtop ID: {{{webtop_id}}}</li>
                                         <li>Opportunity ID: {{{opporunity_id}}}</li>
                                        <li>CIBIL score: {{{CIBIL_score}}}</li>
                                        <li>Credit referral rejection reason : CIBIL score < 650 </li>
                
                                    </ol>
                                    
                                    <p>Please find the attached supporting documents.</p>
                                    <p>Regards,<br>Team Volt</p>
                                </td>
                            </tr>
        ```
        
    - NTC with limit > 20L
        
        ```jsx
         <p>Hi Team,</p>
                                    <p> The credit referral is raised to the lender</p>
                                    
                                    <ol style="margin: 20px 0 20px 20px; padding: 0;">
                                        <li>Customer's name: {{{full_name}}}</li>
                                        <li>Customer's PAN: {{{account_holderpan}}}</li>
                                        <li>Application ID: {{{application_id}}} </li>
                                        <li>Application type: {{{application_type}}} </li>
                                        <li>Credit referral reason: New to credit customer with limit > 20L</li>
                                        <li>Webtop ID: {{{webtop_id}}}</li>
                                         <li>Opportunity ID: {{{opporunity_id}}}</li>
                                        <li>CIBIL score: {{{CIBIL_score}}}</li>
                                        <li>Credit limit : {{credit_limit}} </li>
                                        
                
                                    </ol>
                                    
                                    <p>Please find the attached supporting documents.</p>
                                    <p>Regards,<br>Team Volt</p>
        ```
        
    - Approval
        
        ```jsx
        p>Hi Team,</p>
                                    <p>The lender has approved the credit referral.   </p>
                                
                                
                                    <p>Regards,<br>Team Volt</p>
                                </td>
                            </tr>
        ```
        
    - Rejection
        
        ```jsx
         <tr>
                                <td style="padding: 30px 20px; font-size: 16px; line-height: 1.5; color: #000000;">
                                    <p>Hi Team,</p>
                                    <p>The lender has rejected the credit referral. Please ask the sales & support team to contact the customer to take this forward.   </p>
                                    <p>Credit referral rejection reason :</p>
                                
                                    <p>Regards,<br>Team Volt</p>
                                </td>
                            </tr>
        ```
        

## Requirements overview (optional)

### User stories / User flow

1. User starts application with TATA as lender
2. Comes at KYC verification step (match score < 70%) 
3. Application goes into Credit referral 
4. Application is forwarded to TATA for credit referral 
    1. We directly send a mail to [tata.operations@voltmoney.in](mailto:tata.operations@voltmoney.in) to create a zendesk ticket 
    2. TATA Ops approves : We get success callback → We top-up in the same ticket/mail to inform the ops about the approval of the credit referral 
    3. TATA Ops rejects : We get reject callback (will send an email/zendesk ticket to Ops) → We top-up in the same ticket/mail to inform the ops about the rejection of the credit referral 

# **Design**

---

# **Analytics**

- Number of applications where the system is sending referral per day
- Split of application status
    - Blocked
    - Volt Ops approved
        - Lender Ops approved
        - Lender Ops rejected
    - Volt Ops rejected
    - TAT for Volt Ops approval/rejection
    - TAT for Lender approval/rejection

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

- Aadhar-PAN mismatch : Less than 70% then pass to credit referral
- KYC Photo verification : 70%
- CIBIL
    - CIBIL < 650
        - Hard reject
    - CIBIL > 650 ; Posidex negative
        - 002,
- PAN-Bank name : Less than 70% then pass to credit referral

BAJAJ : 90%

TATA : 70%, CIBIL < 650 

- Discussion with Nishant
1. Excess Margin during unpledging & Full closure unpledging issue at BAJAJ's end
2. All cases automate (with data) as suggested by tech about 10 tickets per day.
3. Seperate ticket for rejection in case there is a rejection after SLA breach? Or the same mail thread only
    1. Seperate ticket for rejection/approval 
4. Seperate SLA mail thread for credit referral at each step?
5. **Business hour rule?**
    1. TATA Ops business hours? 
        1. Time : (1st and 2nd Saturday leave,) 9-6
        2. Days 
    2. Holidays? - Arpit 
    3. Logic 
        1. Simple handling 
            1. If current time (when credit referral created) is within business hours → Send the credit referral case to TATA & initial the scheduler for SLA breach check right then 
            2. If current time outside business hours → Send the credit referral case to TATA & initial the scheduler for SLA breach check once the business hour starts 
        2. Extra handling 
            1. If current time + 2 hours is within business hours → then send the credit referral case to TATA initiate the scheduler 
            2. If current time is outside business hours → Send the credit referral cases when next business hour starts 
            3. If current time + 2 hours is outside business hours → Send the credit referral case to TATA, but start the scheduler when the next business hour starts 

- Deprioritised handling

| **Check Step**  | Change in handling | **Check**  | **Threshold** | **Actions** |  |
| --- | --- | --- | --- | --- | --- |
| KYC_Documents | Yes  | PAN-Aadhar name match score | 20 ≤match score ≤ 70 | - Straight through process  |  |
|  |  |  | match score <20 | - Through Volt Ops |  |
| KYC_Documents | No  | Photo match score  | match score <70  | - Through Volt Ops  |  |
| CIBIL_Check  | Yes  | CIBIL score  | < 650  | - Application blocked  |  |
|  |  | Posidex code  | Negative (CIBIL > 650)  | - Straight through process  |  |
| Bank Verification  | Yes  | PAN-bank name match score  | 20 ≤match score ≤ 70 | - Straight through process |  |
|  |  |  | match score < 20 | - Through Volt Ops  |  |
- Mail trigger/Zendesk ticketing system
    - Email trigger system
        - Logic
            
            
            | **Handling** | **Scenario**  | **Action**  |
            | --- | --- | --- |
            | STP  | Success | No mail zendesk ticket  |
            |  | Rejection Create zendesk ticket |  |
            |  | SLA breach (> 2 hours) & no callback [with business hour logic] | Create zendesk ticket |
            |  | SLA breached & approved later | Create zendesk ticket/Add top with “Success” in the same mail thread |
            |  | SLA breached & rejected later | Create zendesk ticket/Add top with “Rejected” in the same mail thread |
            | Through Volt Ops  | - | Create zendesk ticket, Ops will check & approve |
            |  | Approved | Create zendesk ticket/Add top with “Success” in the same mail thread |
            |  | Rejected | Create zendesk ticket/Add top with “Rejected” in the same mail thread |
        - Business hour logic
            - Business hours
                - Usual ⇒ Mon-Fri (9AM-6PM) with 2nd, 4th Saturday working
                - Holiday sheet to be shared by Arpit
            
            | **Time**  | **Action**  | SLA  |
            | --- | --- | --- |
            | If time at which credit referral created (T) is  within business hour  | Pass the credit referral to the lender  | T+2 hours  |
            | If time at which credit referral created (T) is outside business hour  | Pass the credit referral to the lender  | Time at which next business hour starts + 2 hours |
    - Email details
        - STP Success
            
            Email/Ticket is not required
            
        - STP SLA breach
            - Email header
                
                Credit referral SLA Breach - {Application ID} - {Customer Name}
                
            - Email template
                - For PAN-Aadhar name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    PAN-Aadhar name match percentage :
                    
                    Please follow up from the lender’s team to take this forward. 
                    
                    **{Attachments}**
                    
                    </aside>
                    
                - For PAN-Bank name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    **Details -** 
                    
                    Name as per Bank Account :
                    
                    Name as per PAN :
                    
                    PAN-Bank name match percentage : 
                    
                    Please follow up from the lender’s team to take this forward. 
                    
                    {Attachments}
                    
                    </aside>
                    
                - For Photo verification
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    **Details -** 
                    
                    Photo match % : 
                    
                    {Attachments - Customer’s Photo & Aadhar Photo}
                    
                    </aside>
                    
                - For CIBIL/Posidex
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Details:
                    
                    Posidex negative : 
                    
                    CIBIL :
                    
                    **{Attachments}**
                    
                    </aside>
                    
        - STP rejections
            - Email header
                
                Credit referral rejected - {Application ID} - {Customer Name}
                
            - Email template
                - General email template
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Match percentage :
                    
                    Name as per Bank Account :
                    
                    Name as per PAN (%) :
                    
                    Name as per AADHAR (%) :
                    
                    Photo match % :
                    
                    Posidex : negative 
                    
                    CIBIL :
                    
                    {Attachments}
                    
                    </aside>
                    
                - For PAN-Aadhar name mismatch
                    
                    <aside>
                    💡
                    
                    The credit referral is rejected from the lender’s end.  
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    PAN-Aadhar name match percentage :
                    
                    {Attachments}
                    
                    </aside>
                    
                - For PAN-Bank name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    **Details -** 
                    
                    Name as per Bank Account :
                    
                    Name as per PAN :
                    
                    PAN-Bank name match percentage : 
                    
                    Please follow up from the lender’s team to take this forward. 
                    
                    {Attachments}
                    
                    </aside>
                    
                - For Photo verification
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    **Details -** 
                    
                    Photo match % : 
                    
                    **{Attachments - Customer’s Photo & Aadhar Photo}**
                    
                    </aside>
                    
                - For CIBIL/Posidex
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    **Details -** 
                    
                    Posidex negative : 
                    
                    CIBIL :
                    
                    {Attachments}
                    
                    </aside>
                    
        - Through Ops : Zendesk ticket
            - Email header
                
                 Credit referral Pending Manual Review - {Application ID} - {Customer Name}
                
            - Email template
                - General email template
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    Details:
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Match percentage :
                    
                    Name as per Bank Account :
                    
                    Name as per PAN (%) :
                    
                    Name as per AADHAR (%) :
                    
                    Photo match % :
                    
                    Posidex : negative 
                    
                    CIBIL :
                    
                    {Attachments}
                    
                    </aside>
                    
                - For PAN-Aadhar name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : PAN-Aadhar match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    PAN-Aadhar match percentage : 
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For PAN-Bank name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : PAN-Bank name match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Name as per Bank Account :
                    
                    PAN-Aadhar match percentage : 
                    
                    PAN-Bank match percentage : 
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For Photo verification
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : Photo match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Photo match % :
                    
                    {Attachments - Customer’s Photo & Aadhar Photo}
                    
                    </aside>
                    
                - For Posidex negative
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : Posidex negative 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Posidex : negative
                    
                    CIBIL score :
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For CIBIL < 650
                    
                    <aside>
                    💡
                    
                    We are rejecting this application. 
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : CIBIL Score < 650 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Posidex : 
                    
                    CIBIL score :
                    
                    {Attachments}
                    
                    </aside>
                    
- Credit referral request/response
    
    **Request :** 
    
    ```jsx
    {
        "LeadId": "226344635",
        "RefId": "2244940402952849110",
        "applSource": "LAS",
        "assignTo": "CM",
        "stage": "4",
        "stagedescription": "OKYC name mismatch",
        "webtopId": "291BZ8640463"
    }
    ```
    
    **Response :** 
    
    ```jsx
    {
        "Assign_Case_Response": {
            "Status": "Success",
            "Message": "Case has been assigned to CM",
            "LeadId": "226344635",
            "RefID": "2244940402952849110"
        },
        "RetStatus": "SUCCESS",
        "sysErrorMessage": "null",
        "sysErrorCode": "null"
    }
    ```
    
    **Callback :** 
    
    ```jsx
    {
      "applSource": "LAS",
      "leadId": "228204425",
      "managerDecision": "Rejected",
      "refId": "5688102400937952287",
      "stage": "3",
      "stageDescription": "Application has been recommended for Credit approval .Dedupe is negative",
      "webtopId": "291BZ8646200"
    }
    ```