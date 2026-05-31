# Foreclosure lifecycle tracking + Tata EOD report

: Vaibhav Arora
Created time: March 5, 2024 8:32 AM
Status: Done
Last edited: March 23, 2025 6:31 PM
Due Date: 04/03/2024

# **What problem are we solving?**

- Users currently are not able to track the exact status of their request.
- Users do not get information and respective ETAs for the different steps involved in the process of their foreclosure request.
- Due to lack of clarity and involvement of 3P flows in the process, users feel that it is Volt that is causing delay in their application causing misinformation and instilling distrust in the minds of the user.

![User raises support ticket due to lack of clarity on status - tonality suggests that they feel that Volt is not doing anything to solve their issue](Foreclosure%20lifecycle%20tracking%20+%20Tata%20EOD%20report/Screenshot_2024-03-05_at_8.54.01_AM.png)

User raises support ticket due to lack of clarity on status - tonality suggests that they feel that Volt is not doing anything to solve their issue

![User has an urgency in mind, because they do not have a clear timeline in mind of the process](Foreclosure%20lifecycle%20tracking%20+%20Tata%20EOD%20report/Screenshot_2024-03-05_at_8.54.27_AM.png)

User has an urgency in mind, because they do not have a clear timeline in mind of the process

![Support team has to coordinate with tech team to get the status of the request? Why?](Foreclosure%20lifecycle%20tracking%20+%20Tata%20EOD%20report/Screenshot_2024-03-05_at_8.54.55_AM.png)

Support team has to coordinate with tech team to get the status of the request? Why?

![Users see this when they are awaiting status on their foreclosure request](Foreclosure%20lifecycle%20tracking%20+%20Tata%20EOD%20report/Screenshot_2024-03-05_at_5.54.20_PM.png)

Users see this when they are awaiting status on their foreclosure request

---

# **How do we measure success?**

- Number of tickets enquiring about the status of their foreclosure requests (zendesk) / total foreclosures
- Number of queries (multiple) per user on average
- Number of foreclosures automatically settled via our auto polling logic
- TAT for foreclosure settlement (Lender specific)

---

# **How are others solving this problem?**

Communicating external dependencies via UI:

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%202.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%203.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%204.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%205.png)

---

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%206.png)

![Untitled](Lien%20status%20lifecycle%20tracking/Untitled%207.png)

Other players communicating external dependencies via UI to communicate the steps involved to the customer and handle queries via product

---

# **What is the solution?**

We are solving this problem for the user by the following ways:

- Post making the foreclosure request, clearly describe the steps in the process to the user with accurate ETAs for each step.
- Descriptive UI screen describing the status along with steppers describing the journey of a foreclosure requests of the user
- Actively sharing the status of the request made by the user (foreclosure success/ foreclosure processed) on UI and via WhatsApp and Email to the user.
- Tata excess interest case handling - Foreclosure requests where we pay excess interest but it is not posted in the settlement account.
- Alerts
    - Flagging cases to Ops where requests are not automatically settled, so that they can be raised to BFL and Tata for settlement
    

## Requirements overview (optional)

### **Transaction status management**

- When we receive a foreclosure request from the user, we will be describing the state of their request in 3 steps:
    1. Request accepted for foreclosure
        1. Request accepted for closure
        2. Foreclosure request accepted
            1. Raised on 26th October 2024
    2. Foreclosure under processing
        1. Foreclosure request under process
            1. It may take up to 2 working days to process your request. Don’t worry, no additional interest will be charged from your account.
        2. Foreclosure processing
        3. Foreclosure is processing
            1. Final state - Foreclosure processed - Your loan was successfully closed, and a lien removal request has been raised with the RTA. 
    3. Lien removal under process with RTA
        1. Lien removal in process
        2. Lien removal request shared with RTA
            1. Volt has successfully shared the lien removal request against your pledged portfolio with the RTA(s). It may take them 4-5 business days to close this request.
    

### UI and cases that need to be handled

- Once the user has raised a foreclosure request, they will land on the foreclosure splash screen which will show the updated status of their request.
- Upon receiving confirmation of foreclosure (foreclosure request is open and we see loan update in the holdings statement) we will mark the second step as completed
- Once the loan is closed on the lender end, (polling the SOA API) we will see cases which have a closure transaction and a pending foreclosure request with us.
    - If validated, we will complete the second step and change its state to completed
- Third state will get updated on the next day automatically, and will be the closed state for the user. We will close this page after 3 business days and user will be redirected to an existing user page (Design pending) where user can reinitiate a loan request if needed.

### Accounting and Settlement

- We will poll holding statement for the user, once a foreclosure payment is made by the user. We will start polling it for every hour and as soon as the holding statement is updated and account is settled we will update the status of the request.
- For cases where foreclosure request is not automatically settled, we will let ops team to settle them/update status using our admin action.
- For TATA, we will build an end of day report which will identify all cases where excess money is equal to interest accrued and pass that to Tata so that their ops team can create closure maker requests on respective loans.
    - On maker, accrued interest will get posted in the account and the user’s account will get settled post which the account can be closed with Tata.

### User Comms

Repayment confirmation

<aside>
💬 Foreclosure under process!

Dear <customer name>,

Your foreclosure request was received successfully. ✅

Note: It may take 2-3 business days for your request to get processed.  

You can track the status of your request on the Volt Money app <app link>

For any query or feedback, call us or whatsapp us at +919611749097

Template ID: repayment_processing_v1

</aside>

Repayment settled:

<aside>
💬 Foreclosure processed!

Dear <customer name>,

Your foreclosure request against your loan account has been processed and a request has been raised with the RTA(s) to un-pledge your portfolio. ✅

Note: RTA(s) may take 4-5 business days to complete the un-pledge request on your portfolio.

For any query or feedback, call us or whatsapp us at +919611749097

Template ID: repayment_processing_v1

</aside>

### Reporting (Internal analytics + Ops flags and ticket creation)

- Admin action to close foreclosure request (change on UI) manually coordinated with Volt and lender (BFL and Tata)
- End of day report to be created for Tata (Ops requirement)
    - Loan accounts at end of day tracker needs to be shared with Tata team as per the following logic:
        - If foreclosure request is made (POS=0) and interest accrued = excess amount in SOA (add the report)
        - Values that need to be shared with Tata team:
            - Tata loan account number
            - Customer name
            - Customer mobile number
        - Needs to be sent to Tata ops while also marking our operations team
            - Get contact details (get added in daily ops sync with Tata, get our support email whitelisted) discuss report requirements tomorrow.
- DB entries of cases where requests were raised but were not settled (Ledger) with following metrics (Stored once a day at 6 PM)
    - Application ID
    - Request Status
    - Request closure status (Unsettled/Settled) - Basis which we will control pending requests on UI
    - request date and time (User payment timestamp)
    - Auto-closure date and time (Internal API settling timestamp) - measure TAT
    - Manual Settlement Flag (true/false if request was settled manually by ops team using admin action)
- Automated Emails to Zendesk (T+Nth Business day) to create unclosed request ticket IDs for operations team to identify and follow up on cases with BFL and Tata.
- Backfill task (See all requests completed before) and backfill them as closed.
- Close application ID once a loan is closed and map it to existing user stage on dashboard sign up
- Automated Report to be sent daily indicating pending settlements for measuring product efficiency and raising outliers to ops.

[https://docs.google.com/spreadsheets/d/10gK_rXJ2PbsF3pZ1kUc4Xz_tMSsBu8szAh02rCbxN8M/edit#gid=0](https://docs.google.com/spreadsheets/d/10gK_rXJ2PbsF3pZ1kUc4Xz_tMSsBu8szAh02rCbxN8M/edit#gid=0)

|  | **T0** | **T-1** | **T-2** | **T-3** | **T-4** | **Remaining** |
| --- | --- | --- | --- | --- | --- | --- |
| Number of foreclosure requests |  |  |  |  |  |  |
| Number of requests automatically closed |  |  |  |  |  |  |
| Number of requests pending closure |  |  |  |  |  |  |
|  | **Today** | **This week** | **This month** |  |  | **Remaining** |
| Average closure TAT |  |  |  |  |  |  |
| % Requests closed automatically |  |  |  |  |  |  |

|  | **T0** | **T-1** | **T-2** | Rest |
| --- | --- | --- | --- | --- |
| Number of requests |  |  |  |  |
| Number of transactions automatically settled |  |  |  |  |
| Number of transactions pending settlement |  |  |  |  |
|  | **Today** | **This week** | **This month** |  |
| Average settlement TAT |  |  |  |  |
| % repayments settled automatically |  |  |  |  |

## User stories / User flow:x`

![Screenshot 2024-03-05 at 2.02.49 PM.png](Foreclosure%20lifecycle%20tracking%20+%20Tata%20EOD%20report/Screenshot_2024-03-05_at_2.02.49_PM.png)

## Requirements:

---

# **Design:**

https://figma.com/file/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?type=design&node-id=6691-14831&mode=design&t=QCOcE1xjyECCNwu7-0

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

- [ ]  Product Tasks
    - Create queries to measure impact metrics
    - Connect with Labdi for template approval and setting up trigger along with backend
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - Design overlook pending

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

### Analytics requirement:

[Analytics requirement: Foreclosure](Repayment%20Lifecycle%20Tracking/Analytics%20requirement%20Foreclosure%208e4d1f5d1a7d4b259dc52600e961084b.md)