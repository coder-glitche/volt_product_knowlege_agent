# Un-pledge optimisations

: Ameya Aglawe
Created time: November 14, 2024 3:03 PM
Status: In progress
Last edited: December 3, 2024 3:13 PM

# **What problem are we solving?**

For BFL users, who make a withdrawal request of complete available amount while an un-pledge request is in-progress then the withdrawal requests gets processed first and un-pledge request gets rejected due to update in the value of net-payable due to the withdrawal processing  

---

# **How do we measure success?**

---

- Decrease un-pledge rejections for BFL by 1%

# **How are others solving this problem?**

---

# **What is the solution?**

When user is making a withdrawal is making a withdrawal while an un-pledge request is in “In progress” we will give a heads-up to the user that the withdrawal request might interfere with the un-pledge request if the outstanding is not zero. [This change only needs to be done for BFL] 

## Requirements overview (optional)

### User stories / User flow

1. User places an un-pledge request 
2. The un-pledge request is in-progress
3. User comes to the withdrawal screen and enters the withdrawal amount 
4. We show a callout to the user till the time the un-pledge requests status reaches the terminal state (SUCCESS, FAILED) 
- UI
    
    ![Screenshot 2024-11-25 at 7.24.33 PM.png](Unpledge%20and%20Disbursement%20Enhancement/Screenshot_2024-11-25_at_7.24.33_PM.png)
    
- BFL getDisbursementInfo response
    
    ```jsx
    (DisbursementDetails=[
      DisbursementInfo(drawingPower=117181.0000,
      availableAmountForDisbursement=0.0000,
      loanNo=V402ALAS00166463,
      chargesAmountDetails=[
        
      ],
      excessMargin=0.00,
      interestDue=0.00,
      chargesDue=0.00,
      loanAmount=82900.00,
      penalInterest=0.00,
      rateOfInterest=10.49,
      loanContractLimit=82900.00,
      loanAccountLimit=82900.00,
      loanMaturityDate=30-Jun-2027,
      loanAccount=185553,
      bankAccountDetails=[
        ClientBankAccountDetails(accountNo=004115000020355,
        ifscCode=TBSB0000004,
        bankName=THANEBHARATSAHAKARIBANKLTD)
      ])
    ])
    ```
    

# **Design**

---

https://www.figma.com/design/jYRvz34fgH47FywaqCrm25/Manage-Limit?node-id=305-853&node-type=canvas&t=mjbimHeN75aQ7hhc-0

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
    

- Update customer details
    - In our system
    - In TATA system