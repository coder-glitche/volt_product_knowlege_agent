# [CC] Showcase the reason for freezing on CC

: Surya Ganesh
Created time: January 24, 2025 3:17 PM
Status: Not started
Last edited: February 4, 2025 6:15 PM

# **What problem are we solving?**

Account freezing or suspension is a temporary restriction that prevents an account holder from accessing specific or all account features. This occurs for several reasons:

- Suspicious activity detection
- Policy violations
- Legal requirements
- Payment issues
- Security concerns

We have the operations team, risk team and the development team who can place an account under suspension or frozen state. 

The frozen state **also** occurs when an active account undergoes foreclosure procedure so as to prevent the user from initiating any debit transactions.

When an account gets frozen, teams can't easily see why it was frozen. This makes it harder and slower to solve the issue, which negatively affects our customer service.

The customer might face an issue as we will blocking certain actions when their account is frozen without any prior intimation. Thus, they might reach-out to the support, who will in-turn reach-out to the Ops team for more clarity of the case. 

As our account volume grows, manually tracking frozen accounts will become increasingly challenging. Since different freeze reasons require different standard operating procedures (SOPs), having a clear system to manage and resolve these cases is crucial to maintain efficient customer service.

---

# **Why are we solving this?**

For better alignment across the teams will help with quicker resolutions and better customer service. This solution is for all the members of the operations and risk teams.

---

# **How do we measure success?**

- Zero un-alignments between teams for customer problem resolutions in case of frozen accounts

---

# **How are others solving this problem?**

---

# **What is the solution?**

We allow the maker to add a reason to freezing of an account. This reason is taken as a service request and we will be storing this in our database.

When we fetch the reasons for the freezing of an account and showcase it as a separate column on the CC when a specific loan id if fetched.

Categorising the reasons for freezing into 2 major categories:

1. Suspicious Activity
2. Credit Risk includes (these individual options which can be selected):
    1. Invalid collateral addition or valuation
    2. Incorrect Repayment addition
    3. Invalid bank account
3. Foreclosure 

The Maker via the CC can select anyone of the above reasons for freezing (feature to select the reason is already available). The account will be immediately frozen and the reason should be visible to the the operations team. 

The bar showcasing the reason will be yellow in colour for the foreclosure and will be red in colour for the other reasons. This is to differentiate and create urgency for the accounts frozen for reasons apart from foreclosure.

There is no need for a history log to be maintained as the SOP takes care of reporting to the concerned stakeholders.

## Requirements overview (optional):

## User stories / User flow

---

1. If the operations team freezes an account, the initiator will need to add a reason for the same. On the system side, we will consider this as a service request to save the reason and log it in a table. 

2. When we change the status of an account from active to frozen, we should automatically update the reason for the same. When the operation’s team member searches for the customer ID/ Loan ID/ Name, they should be able to see the reason.

# **Design**

- Contributor: @Karuna Sankolli
- https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2804-82558&t=HRlEdptmrcs2AXa0-4

---

# **Analytics**

---

# **Timeline/Release Planning**

- To be picked in Feb A sprint
- Training to be scheduled in first week of Feb
- Get a query added for frozen accounts with reason distribution on CC
- 

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