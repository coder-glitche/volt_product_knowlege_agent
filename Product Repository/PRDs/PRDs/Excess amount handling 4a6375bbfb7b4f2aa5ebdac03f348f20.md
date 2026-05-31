# Excess amount handling

: Ameya Aglawe
Created time: July 27, 2024 4:12 PM
Status: On Hold
Last edited: November 8, 2024 1:55 PM

# **What problem are we solving?**

1. Users are not able to withdraw or utilise their complete limit in case their line goes in excess. 
2. Handling of storing of the excess amount data in our DB is not proper. 

---

# **How do we measure success?**

- Reduction in customer queries/complaints like available credit limit being shown less, not able to withdraw amount.
- Reduction in TAT of clearing the excess amount from users’ account

---

# **How are others solving this problem?**

---

# **What is the solution?**

- **Current handling :**
    - When user has excess amount in their line -
        - We show the available cash as excess amount itself
        - The DP gets reduced to excess amount amount itself. We also have a limitation of 1000 as minimum amount of withdrawal. In most cases excess is less than 1000 and hence the user is not able to make withdrawal & gets blocked.

![Untitled](Excess%20amount%20handling/Untitled.png)

- **Optimised handling :**
    - **1st approach**
        - We can show an alert to the user that shows the excess amount on the home screen itself.
        - Alert will say: “You have excess amount present in your loan account, click here to withdraw the excess amount”.
        - We will process the excess amounts which are greater than Rs 1 and less than Rs 1000
            - **Edge case : We can’t handle the cases where excess amount is less than Rs 1, since TATA does not allow the withdrawal of less than Rs 1.**
            - Check with Priyesh whether the Savedisbursment API is working for withdrawal less than Rs 1
            - We can run CRON on a daily basis in which we can waive of the excess amount less than Rs 1, or else we can automatically make the withdrawal request (if TATA Savedisbursment API is working for withdrawal requests less than Rs 1)
        - **Cons :**
            - Will require user’s effort each time there is an excess in their account.
    - **2nd approach**
        - Adding a CRON (in an interval of 6 hours), which will auto-process all the excess amount withdrawal request from the user
            - **Auto-disbursals approval from lender**
            - **Business hours**
        - **Cons :** User will be surprised to see a new withdrawal in the transactions, which was not requested by them

### Handling in backend for excess amount

Handling of excess amount in the backend is not proper. 

**BAJAJ handling**
Our DB (Athena)

![Screenshot 2024-07-29 at 7.33.38 PM.png](Excess%20amount%20handling/Screenshot_2024-07-29_at_7.33.38_PM.png)

**For TATA**

For TATA, in case of excess margin we the following response, we can see that we get Excess margin as 316.00, Available cash limit as 316.00 & Drawing power as 316.00. 

Response : 

```jsx
{
  "disbursementInfoResponse": {
    "disbursementDetails": [
      {
        "excessMargin": 316.00,
        "interestDue": 0.00,
        "thirdPartyBankAccount": [],
        "clientBankAccount": [
          {
            "clientBankName": "Punjab National Bank",
            "clientParyBankIFSC": "PUNB0360700",
            "clientBankAccountNo": "3607000102104918"
          }
        ],
        "loanAccount": 11748,
        "availableAmountForDisbursement": 316.00,
        "loanNo": 14196,
        "chargesAmountDetails": [],
        "chargesDue": 0.00,
        "loanAmount": 0.00,
        "rateOfInterest": 10.49,
        "loanAccountLimit": 42800.00,
        "drawingPower": 316.00,
        "penalInterest": 0.00,
        "loanContractLimit": 42800.00
      }
    ],
    "status": {
      "status": "Success",
      "code": "01",
      "remarks": ""
    }
  }
}
```

Storing in DB : 
But when it comes to storing the excess amount, we store the excess amount in POS as a negative value, and store total DP & excess margin as 0. 

![Screenshot 2024-07-29 at 7.28.33 PM.png](Excess%20amount%20handling/Screenshot_2024-07-29_at_7.28.33_PM.png)

We need to fix the mapping between the response which we receive in the API response and our backend, for the account with excess amount. 

## Requirements overview (optional)

## User stories / User flow

## Requirements

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

**Product issues scrum**

- Tickets -
    - WATI
        - Direct customer
        - MFD
    - Email
        - Users
        - Our raised
    - B2B
    - Product
    - Tech
    - Ops
- Tools
    - Zendesk
    - JIRA
    - Sheets (for bugs tracking)
- Solve
    - Channel + Reporting
    - Zendesk : JIRA integration - Has bugs
    - Sheets : JIRA integration
    - Sheets → JIRA → Zendesk
    - JIRA (For tracking & visiblity)
    - Zendesk (For Ticketing)
    - Stages
        - Backlog
        - Product sol.
        - PRD
        - Tech To-Do
        - Prod deployment (Scrum master required)
        - Ops training (Ops owner required)
    - Issues with tech
        - We are not able to keep a track of bugs in Tech stand-up
    - Add two owner in the JIRA tickets
        - Product owner
        - Tech owner
    - There should be a training after each bug fixes
    - All the on-call meeting action points should go through this
    - Metrics
        - L3, 0
        - Report
            - Incoming
            - Solved
            - Owners
            - Impact (high level)

3P Issues → Add an email zendesk email-id (add tagging) 

- Can we avoid excess money generating in the user’s account all the way?
    - Cases in which excess amount is generated :
        - A sell-off of units was made to clear the dues and the value of the units sold-off was a little higher than the due leading to excess
        - Multiple repayments - In case of BAJAJ, we give the list of repayments made by the customer to the lender, and lender updates it in their system and we hit the API to get updated POS, but till then the POS is not updated so customer makes another repayment to clear the due. [If in this case the has paid all the principal, then the extra repayment made will be stored as excess]
        - TATA, BAJAJ due & mandate process
            - TATA : The dues of all the users are listed on 1st of every month, and the dues are cleared through mandate itself but the mandate is updated in the list in the lender’s list by 3rd of the month, in the meanwhile, the user sees that the dues are still pending to be paid & thus the user makes the repayment through app to clear the dues. Thus double repayment is done for the same due leading to excess (if the POS=0)
            - BAJAJ : The dues of all the users are listed on 3rd of every month, and the dues are cleared through mandate itself but the mandate is updated in the lender’s list by 7th of the month, in the meanwhile, the user sees that the dues are still pending to be paid & thus the user makes the repayment through to clear the dues. Thus double repayment is done for the same due leading to excess (if the POS=0)
    - These cases are lender side process driven

1. Priyesh API hit 
2. Arpit doubt 
3. Priyesh raising 

**TATA**

![Screenshot 2024-07-29 at 7.45.36 PM.png](Excess%20amount%20handling/Screenshot_2024-07-29_at_7.45.36_PM.png)

In which cases do we get excess amount 

1. User did more amount of repayment than required. 

**getCredit API - Frontend**

available cash → available credit amount

Outstanding amount → Principle outstanding amount 

### List of excess margin with their SOA