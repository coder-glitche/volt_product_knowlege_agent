# Withdrawal issues enhancement

: Vaibhav Arora
Created time: June 19, 2024 7:09 AM
Status: Not started
Last edited: March 23, 2025 6:43 PM
Assignee: Vaibhav Arora

# **What problem are we solving?**

- **Users are not able to track and are not notified on failed withdrawal requests**
- Users are not clear that amount disbursed in their account is after deducting the processing fee or other outstanding charges against their line
- Users are not able to track other charges deducted from their withdrawal amount
- Users are sent triggers of processing of withdrawals at incorrect triggers (State management)
- Users are not shown accurate ETAs of their withdrawal requests

For the scope of this PRD we will be covering failed withdrawal handling for the users

- Future scope
    
    Withdrawal issues can be broadly defined into the following themes:
    
    1. Withdrawal request tracking (Status and TAT)
    2. Charges deduction against withdrawal
    
    ### Withdrawal TAT tracking
    
    - Users are not able to track the status of their withdrawal requests accurately
        - **Lack of handling of failed state of withdrawal**
            - User story: User places a request, request is cancelled by lender, user is not prompted or informed via touch points (comms/UI)
            - How is the issue currently handled: Currently this is solved by either retrying withdrawal requests by on call or by ops manually informing the customer that their request has failed and asking them to make the request again.
        - Users are not able to know by when their withdrawal amount will reach their bank account. This case is more frequent for cases where the user makes the withdrawal request in off business hours i.e. on weekends/bank holidays or after 6 PM (banking hours) this further divided into two cases, one where its the first withdrawal of the user that is credit has to be created before placing the withdrawal and second where the credit has been created and then the user has placed an nth withdrawal.
            - User story: User wants money and decides to make a withdrawal request on Volt money app. Most withdrawals against a line are not pre-emptive but for a specific use case for which the user needs money for. Accordingly the user has an urgency for receiving the withdrawal amount.
            - How is the issue currently handled: User is shown an expected ETA by when the withdrawal amount would be deposited to the user account
            - Hypothesis: Withdrawal TAT being shown to the user is not very apparent while making the request, there are no signalling callouts telling the user that the request being placed is outside of business hours which might extend the TAT for settlement
            
            Withdrawal TAT being shown to the user is not accurate, we are not able to meet the expectations that we are showcasing to the user which is leading to escalations
        - User is not able to track the status of their request (navigation from payment success to where the user can track the status of their transaction)
        - When user places their request and it is under credit approval (non business hours) credit is not created, message is sent to the user when the lender API is called and not when the request is raised by the customer (trigger is incorrect for processing)
        - For a few cases, withdrawal processing message is not triggered (919030855990) - Need an RCA
    - Users are not able to track the charges deducted against their withdrawal requests,
        - For first withdrawals, it is not intuitive for the user that the stamping duty and processing fee will be deducted from their withdrawal amount
            - User story: User opens a line with a limit of 50,000. A processing fee and stamping duty of 999 and 199 is charged to the user’s account. User then places a withdrawal of Rs 10,000. As per our product, the amount is deducted from the user’s withdrawal amount and the remaining amount is disbursed to the user’s bank account. The user however is not able to identify their withdrawal transaction since they are expecting a credit of Rs 10,000 and not Rs 8802
            - How the issue is currently being handled: User escalates on consumer interface and is told by the ops agent that the amount received by the user is Rs 8802 and not 10,000
    
    ### Charges deduction against withdrawal
    
    - For subsequent withdrawals, if there are any outstanding charges, they are deducted against the withdrawal however that is currently not handled on UI. User is shown the complete amount as withdrawal however amount after deduction is disbursed to the user.
        - User story: User had a line of Rs 50,000 and outstanding principle of Rs 10,000 and outstanding interest of Rs 1000. Mandate was presented against the outstanding interest however the user did not have enough funds in their bank account. A bounce charge of Rs 600 was placed against the user’s line 
        
        For first withdrawals processing fee and stamping duty are deducted by default, the copy however is not intuitive for the user and they are not able to understand that the charge is deducted from their withdrawal (Deductions are communicated in UI as well as communication but it is not intuitive) 
        Other contingent charges like bounce fee are also deducted from the user’s withdrawal request however they are not handled on UI.
        
        ![Untitled](Withdrawal%20issues%20enhancement/Untitled.png)
        
        ![Untitled](Withdrawal%20issues%20enhancement/Untitled%201.png)
        
        ![Screenshot 2024-06-21 at 8.42.38 AM.png](Withdrawal%20issues%20enhancement/Screenshot_2024-06-21_at_8.42.38_AM.png)
        
        ![Screenshot 2024-06-21 at 8.42.48 AM.png](Withdrawal%20issues%20enhancement/Screenshot_2024-06-21_at_8.42.48_AM.png)
        
        ![Screenshot 2024-06-19 at 8.39.55 AM.png](Withdrawal%20issues%20enhancement/Screenshot_2024-06-19_at_8.39.55_AM.png)
        
        ![Untitled](Withdrawal%20issues%20enhancement/Untitled%202.png)
        
        ![Untitled](Withdrawal%20issues%20enhancement/Untitled%203.png)
        

---

# **How do we measure success?**

- Performance metrics
    - Identify how many withdrawal requests are retried post notification
    - Failed on (last updated on) and retried on timestamp to be maintained by the user
    - Retry TAT post failure confirmation by the user
- Stability metrics
    - No. of withdrawal failures/Total withdrawal requests
    - Number of users who do not place a withdrawal request post failure in a 3 day timeframe (business loss they arranged money from elsewhere)
    - Number of users who close their loan account immediately after a failed withdrawal transaction (business loss)

---

# **How are others solving this problem?**

![Untitled](Withdrawal%20issues%20enhancement/Untitled%204.png)

![Untitled](Withdrawal%20issues%20enhancement/Untitled%205.png)

![Untitled](Withdrawal%20issues%20enhancement/Untitled%206.png)

![Untitled](Withdrawal%20issues%20enhancement/Untitled%207.png)

---

# **What is the solution?**

### Failed withdrawal handling:

User story: User places a request, request is cancelled/rejected/failed by the lender, user is not prompted or informed via touch points (comms/UI)

![Untitled](Withdrawal%20issues%20enhancement/Untitled%202.png)

Failed withdrawal analysis:

[https://docs.google.com/spreadsheets/d/16ZAzvFp60zzlFkid9dqpHzRXrfnN6R1HxK1HHbFRSe0/edit?gid=1316381149#gid=1316381149](https://docs.google.com/spreadsheets/d/16ZAzvFp60zzlFkid9dqpHzRXrfnN6R1HxK1HHbFRSe0/edit?gid=1316381149#gid=1316381149)

- Failed withdrawal API response: Bajaj (Rejected / Failed)
    
    97CCDE0-ViI02sTrRTyP
    @logStream	
    CreditManagementServicev2/volt-creditmanagementservice/e9689d28e8b04e638b603c00b10149a2
    @message	
    INFO NonStaticHttpUtility RRId= RId=0b823d5b-3e41-4a7b-a7d3-b6547d8d932f, CreditId=8a80037c90b5b5580190b71c52111f33, UId= - got a response with status 200, and body {"DisbursementStatus":[],"status":{"Status":"Fail","Code":"02","Remarks":"No Data Found"}}
    
- Failed withdrawal API response: Tata (Rejected / Failed)
    
    INFO NonStaticHttpUtility RRId= RId=8d74ab5a-7cbf-4733-a830-c3e90bc1ae10, CreditId=8a801fa78ee1ad38018ee1f436c10014, UId= - got a response with status 200, and body {"retStatus":"SUCCESS","GetDisbursementStatus_Response":{"DisbursementStatus":[{"LoanAccount":"8946","LoanNo":"11117","DisburseDate":"16-Jul-2024","CustomerId":"10658","RecordStatus":"Rejected"}],"status":{"Status":"Success","Remarks":"","Code":"01"}},"sysErrorMessage":"","sysErrorCode":""}
    

To solve this problem we will be handling rejected transactions in the transaction tab, and will be prompting the user on their failed request with communications so that the user can place another request without ops intervention.

### Withdrawal failure notification

- User will be notified with a failed withdrawal notification on their dashboard and will be able to retry with the same amount from the dashboard itself.
- Clicking on retry will take the user to the withdraw amount screen with the amount pre-filled
- Notification will only be visible to the user till 48 hours of the request being rejected or if another withdrawal request is placed (new request in progress) by the user.
- Validations:
    - Notification will not be visible to the user if there is an already pending withdrawal request in progress (user cannot retry): Is disbursement available flag
    
    ![Untitled](Withdrawal%20issues%20enhancement/Untitled%208.png)
    

### Failed transactions in transaction tab

- User will be able to track failed transactions in the transaction tab
- Transactions should be sorted from latest to last for the user (outside of scope)
- Transactions in case more than 100 should be trimmed to the latest 100 transactions (outside of scope)
- Failed transactions will be visible in the completed transactions tab for the user

![Untitled](Withdrawal%20issues%20enhancement/Untitled%209.png)

### Withdrawal failure notification:

User will be notified from customer communications platforms (Whatsapp and Email) when their request is rejected by the lender

![Untitled](Withdrawal%20issues%20enhancement/Untitled%2010.png)

![Untitled](Withdrawal%20issues%20enhancement/Untitled%2011.png)

![Screenshot 2024-07-16 at 8.10.32 AM.png](Withdrawal%20issues%20enhancement/Screenshot_2024-07-16_at_8.10.32_AM.png)

Template(s):

[https://docs.google.com/document/d/1prSrc895F6eD-hQNS2j4NW2f0JrfyPbpFj4ygVhBrZ4/edit](https://docs.google.com/document/d/1prSrc895F6eD-hQNS2j4NW2f0JrfyPbpFj4ygVhBrZ4/edit)

<aside>
💡

Important: Withdrawal of Rs.{withdrawal_amount} failed

Dear {customername},

Your withdrawal request of ₹{withdrawal_amount} was failed due to a technical issue with the lender. Our team is actively working to resolve this issue as quickly as possible.

Withdrawal amount: **₹{withdrawal_amount}**

Requested date: **{created_on}**

Don’t worry, you can retry placing a request by clicking below.

For any query, feedback or support, call us or whatsapp us at {contactnumber}.

Regards,

Team Volt Money

</aside>

## Requirements

---

# **Design**

[https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=9764-19657&t=xzBfzzxQL8Ga74dj-0](https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=9764-19657&t=xzBfzzxQL8Ga74dj-0)

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
    - Report is required as per the analysis done for impact measurement
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