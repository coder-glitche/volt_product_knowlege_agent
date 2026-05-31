# Unpledge and Disbursement Enhancement

: Surya Ganesh
Created time: April 14, 2025 4:59 PM
Status: In progress
Last edited: April 14, 2025 8:21 PM

# **What problem are we solving?**

Currently, customers with pending unlien (unpledge) requests see a general disclaimer: "Unlien request in progress, withdrawals may affect the approval of your on-going unpledge request." This creates uncertainty as customers cannot determine their exact available limit until their unlien request reaches a terminal status.

---

# **How do we measure success?**

Reduced number of rejections

---

# **How are others solving this problem?**

N/A

---

# **What is the solution?**

I. During Unliening in process:

1. Display Precise Information 
    - Show a specific message: "Unlien request in progress, withdrawals over ₹X,XXX will affect the approval of your on-going unpledge request"
    - The ₹X,XXX represents the calculated "recommended disbursement amount" that won't interfere with the pending unlien request
2. Calculation Method for Recommended Amount
    - Calculate the active loan amount of the pending unlien funds
    - Subtract this value from the customer's current available limit
    - Present this as the safe withdrawal threshold
3. User Experience Benefits
    - Guides customers to select realistic withdrawal amounts
    - Reduces confusion and prevents unexpected withdrawal rejections
    - Provides transparent information about current account limitations
4. Post-Unlien Resolution Notification
    - Once the unlien request reaches a terminal state (approved/rejected):
        - Send an immediate push notification
        - Inform customer that their available withdrawal limit has been updated
        - Clearly state they can now withdraw funds according to the new available amount

II. During Disbursement in process:

1. Reciprocal Warning System
    - Implement a similar disclaimer when customers have a pending withdrawal: "Withdrawal request in progress, unliening over ₹X,XXX may affect the approval of your on-going withdrawal request" on the fund selection page.
    - Calculate the maximum safe unlien amount by calculating (pending withdrawal request - available limit)

## Requirements overview (optional)

## User stories / User flow

II. During Unliening in process:

1. The customer initiates an upledging request.
2. Sighting the requirement of funds, goes to the withdrawal page for initiating a disbursement request.
3. Instead of wondering how much he might be able to withdraw, he is shown the exact possible amount in a disclaimer ensuring the requested amount is within the available limit even if the unliening request is a success.

II. During Disbursement in process: 

1. The customer has initiated a disbursement request of Rs. XXXX.
2. The customer also wants to un-lien some funds and thus heads to the un-liening page.
3. The customer selects the the funds of his choosing which he wants to unlien but also sees the disclaimer of the possible amount which he can unlien.

 

## Requirements

I. During Unliening in process :

1. Changing the the generic message to include the recommended disbursement amount which is calculated when the user goes on to the withdrawal page to enter the amount.
2. Implement push notification after the unpledging request reaches a terminal state.

II. During disbursement in process:

1. Adding a disclaimer to the end of the screen (after the values are showcased) with the message mentioned and the value.
2. Implementing the push when the disbursement reaches a terminal state. 

---

# **Design**

The following design has been implemented, the content needs to be updated.

![Screenshot 2024-11-25 at 7.24.33 PM.png](Unpledge%20and%20Disbursement%20Enhancement/Screenshot_2024-11-25_at_7.24.33_PM.png)

---

# **Analytics**

Number of Rejected Disbursement Request Lender-wise Distribution as well as Month-wise

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