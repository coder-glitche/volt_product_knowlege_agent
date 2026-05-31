# Customer Lifecycle Tracking - Lien Unmarking → Repayment → Foreclosure

: Vaibhav Arora
Created time: February 22, 2024 9:37 AM
Status: In progress
Last edited: February 24, 2024 2:31 PM
Due Date: 23/02/2024

# **What problem are we solving?**

- 

---

# **How do we measure success?**

- Measure number of requests being raised related to update on pending states in user servicing journey (lender specific).
    - Lien removal requests (Tata and Bajaj)
    - Repayments (Bajaj)
    - Foreclosure requests (Tata and Bajaj)

---

# **How are others solving this problem?**

NA

---

# **What is the solution?**

- Actively communicating the stages of the respective request to the user on the app.
    - Using lender APIs to automatically capture status of the user’s request and breaking down the process into steps to reduce operational load as well as aligning the user on the development of their request.
- Making the request in progress banner less apparent in the user journey to avoid creating artificial urgency in the mid of the user. (Lien removal)
- End state for foreclosure requests when loan is closed (application closed → user should be able to initiate a new journey)

## Requirements overview (optional)

### Un-lien Requests (Tata and Bajaj):

Following are few lender agnostic steps that happen to complete the unpledge request for a user:

- Maker in lender LMS for unpledging of folios
    - Via email for Bajaj and collateral release API for Tata
- Verification and checker of the request (DP - POS > UL)
    - Drawing Power - Principal Outstanding should be greater than the limit of the folio requested for unmarking
- Unlodgement of folios by lender (Holding Statement is updated → Customer drawing power is updated → Folios visible to the user are updated)
- Sending communication (letters to RTA(s)) for unpledging of folio
- RTA(s) direct AMC(s) to process lien umarking request
- RTA confirmation to lender and lender confirmation to Volt on the status of request
- In case the request is rejected due to an outstanding amount pending at the user (DP - POS <UL) a new request has to be generated via (User/Ops) to reinitiate the process.

These steps can be diluted as 3 broad steps for the user:

1. Unpledge request approval (can be successful or rejected) - Primary text (Request raised to <lender>) 
    1. Please ensure you maintain equal or higher available credit line than <unpledge line amount> for a successful request.
2. Unlodgement - Unpledge request verification - Holding Statement Updated (once approved, unlodgement should be successful)  - Primary text (Request approved by <lender>) 
    1. Your request has been approved and funds have been unlodged from your loan account successfully.
3. Unpledging of folio(s) by RTA(s) (Can be successful and fail, if it fails, handled operationally between Volt and Lender)  - Primary text (Unpledging in progress by CAMS and KFintech) - Secondary Text: 
    1. Please note that RTA(s) may take 3-4 working days to unmark your funds. Don’t worry, this will not impact your funds in any way.

User communication:

User communication will be handled both passively and actively, upon each step advancement, we will update the status of the request on UI which the user can track passively, while we will automatically send WhatsApp messages to the user indicating the change in step.

Following updates need to be handled in UI and Comms:

- Request sent (Preliminary stage)

<aside>
💬 Your un-pledge request has been submitted!
Dear <name>,

Greetings from Volt Money.

Your un-pledge request of portfolio with limit ₹<limit of unpledge portfolio> has been successfully shared with <lender>.

Please maintain a credit limit higher than or equal to this amount to ensure your request is not rejected by the lender.

For any query or feedback, call us or WhatsApp us at +919611749097.

</aside>

- Request approved (Trigger: Disbursement info is updated and holding statement changes)

<aside>
💬 Your un-pledge request has been approved by <lender>!
Dear <name>,

Greetings from Volt Money.

Your un-pledge request of portfolio with limit ₹<limit of unpledge portfolio> has been successfully approved by <lender>.

Your updated credit limit amount is ₹<limit of unpledge portfolio>. (Please note that this amount has been adjusted from your credit line)

For any query or feedback, call us or WhatsApp us at +919611749097.

</aside>

- Request rejected (Trigger: Admin action)

<aside>
💬 Your un-pledge request has been rejected by <lender>.
Dear <name>,

Greetings from Volt Money.

Your un-pledge request of portfolio with limit ₹<limit of unpledge portfolio> has been rejected by <lender> due to insufficient credit line availability.

Please repay your outstanding balance, and maintain a credit limit higher than or equal to ₹<limit of unpledge portfolio> to try again.

For any query or feedback, call us or WhatsApp us at +919611749097.

</aside>

- Folio(s) unpledged (Trigger: Admin action)

<aside>
💬 Unpledge request completed
Dear <name>,

Greetings from Volt Money.

Your un-pledge request of portfolio with limit ₹<limit of unpledge portfolio> is completed.

For any query or feedback, call us or WhatsApp us at +919611749097.

</aside>

### Repayments (Bajaj):

Currently users after making repayments once made on our platform till it is settled with the bank. All payments are sent to Bajaj and are settled on the same day till 6 PM

Post 6 PM they are processed on the next working day

We will create a pending state for payments on UI for user to track and keep polling SOA from Bajaj. In case there are multiple repayments, user will see multiple pending transactions on UI.

On receiving entries in SOA, we will check pending repayments state, and mark them settled in our DB, only pending payments will be visible on UI. 

Logic:
Read all credit transactions on loan account (poll at 6 PM everyday) with pending repayments excluding interest payments (Charges + Interest repayment)

- If POS>0 and Sum(Credit Transactions) = Sum (Pending Repayments) → Mark pending payments as settled remove from UI and show settled transactions in status
- If POS<0 and Sum(Credit Transactions - POS) = Sum(Pending Repayments) → Mark pending payments as settled remove from UI and show settled transactions in status
- If POS>0 and Sum(Credit Transactions) < Sum (Pending Repayments) → Check if Sum(Credit Transactions + Interest repayments) = Sum(Pending Repayments) then mark pending payments as settled remove from UI and show settled transactions in status if that is not the case raise to ops
- If POS>0 and Sum(Credit Transactions) > Sum (Pending Repayments) → Raise to ops
- If POS<0 and Sum(Credit Transactions - POS) = Sum(Pending Repayments) → Mark pending payments as settled remove from UI and show settled transactions in status if Sum(Credit Transactions - POS) = Sum(Pending Repayments) raise to ops

Design pending

<aside>
💬

Your repayment was successful!
Dear <customer name>,

Greetings from Volt Money.

Your payment of ₹25,000 was received successfully. ✅

Note: It may take 1-2 business hours for payment to reflect in the account statement.

For any query or feedback, call us or whatsapp us at +919611749097

</aside>

### Foreclosure (Tata + Bajaj):

Day end operation check all loans that are closed, see which accounts have foreclosure requests pending, close their accounts and application.

Create a loan closed state for them, with a stepper showcasing that their loan has been closed with the bank.

Steps:

- Loan foreclosure request received - Initial State
    - We have received the foreclosure request for your successfully. It should get processed by <lender> in 1-2 business days.
- Loan foreclosed (Trigger day end job loan closed status)
    - Lender has approved your foreclosure request and closed your loan successfully.
- Unpledging of folios in progress by RTA(s)
    - Please note that RTA(s) may take 3-4 working days to unmark your funds. Don’t worry, you will not be charged any additional interest till this request is closed.

## User stories / User flow

![Screenshot 2024-02-23 at 12.42.36 PM.png](Customer%20Lifecycle%20Tracking%20-%20Lien%20Unmarking%20%E2%86%92%20Rep/Screenshot_2024-02-23_at_12.42.36_PM.png)

## Requirements

- UI upgrade to show pending request under pledged portfolio (Not actively remind the user of unpledge request) - Design pending
- Communication in steps within unpledge request on the status of the application - Design pending
- Comms set up on 4 aforementioned states of request (Coordination with Labdhi required)
- 

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

[Sameer Minde <> Vaibhav](Customer%20Lifecycle%20Tracking%20-%20Lien%20Unmarking%20%E2%86%92%20Rep/Sameer%20Minde%20Vaibhav%20de95cc867b5b4dffbb017ec07a51d6a1.md)

# Action Items:

Foreclose loan close status - Day end job

Day end job check which loans are closed and close their loan and application with active foreclosure screen

Create a foreclosure state for such users where they see a welcome back screen and can initiate a new application on consent

Repayment:

Multiple payments (how will they be reconciled and handled on UI)

On principal repayment - 

Create reporting for Ops for cases where cases where repayment due will not be covered and reconciliation is incomplete will be raised to ops

Payments after 6 are settled on the other day - how will this be handled?

Handle working days for each lender cases

Make changes for design on a component level