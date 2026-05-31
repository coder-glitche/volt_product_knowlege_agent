# Lien removal SLA tracking report

: Vaibhav Arora
Created time: July 11, 2024 3:30 PM
Status: Ready for Tech
Last edited: November 7, 2024 8:13 AM
Owner: Vaibhav Arora

# **What problem are we solving?**

Users raise lien removal requests via Volt app and web app which are raised directly with the lenders. 

Lien removal requests have broadly three steps:

1. Lien removal request validation
2. Unlodgement of funds
3. Unpledging of funds

The process for the first two steps is done digitally via API however unpledging is done operationally via letters send to the RTAs (CAMS and Kfintech).

Volt and lenders have an operational workflow set between the teams of the two organisations and they need a report to manage SLAs.

**Problem statements:**

1. Volt ops agents should be able to track requests raised by the customers in a defined period which is shared with the lender.
2. Volt ops agent should be able to get status remarks from lender ops team against each request.
3. Lender ops agent should be able to identify the unpledge request of the customer and map it to the unique user entity in their system.
4. Lender ops agent should be able to validate the request raised by the customer via the report itself and approve the same directly in their collateral management system.

---

# **How do we measure success?**

With an improved operational workflow and SLA tracking following metrics should be improved against unpledge requests raised by the customers:

1. TAT to complete request (status is marked success)
2. Escalations raised by customers on delays on their unpledging request should reduce

---

# **How are others solving this problem?**

— Internal use case— 

---

# **What is the solution?**

Two reports (Revocation request level and ISIN level will be created which will be sent to the lender

**Report 1:**

Created_on

Loan account number - Lender loan account number (Credits)
Loan contract number - Lender credit ID (Credits)
Customer name - Borrower name (Borroweraccounts)
VOLT request ID - Revocation request ID (revocation requests)
Customer PAN - AccountholderPAN (Borroweraccounts)
Total outstanding amount - Netpayable (Credits) - 

Update (07-17) - At the time of making request (Needs to be stored while making the request)
DP before un-pledging - Assetlimitbeforepledging (Revocationrequests)

Update (07-17) - At the time of making request (Needs to be stored while making the request)
DP after un-pledging - Assetlimitbeforepledging (Update (07-17) - At the time of making request (Needs to be stored while making the request)) - Sum of all securities(Assets to be unpledged*LTV*NAV) - Needs to be taken from revocation request
Request status - Revocationrequeststatus 
Comments - To be sent blank for lender ops agent to fill

**Report 2:**

Created_on

Loan account number - Same as above
Loan contract number - Same as above
Customer name - Same as above
VOLT request ID - Same as above
Customer PAN - Same as above
Folio No. - FolioNo (Revocationrequest)
ISIN - ISIN (Revocationrequest)
Scheme name - Assetname (Revocationrequest)
AMC name - AMCname (Revocationrequest)
Units to be un-pledged - Units to be unpledged (security level) (Revocationrequest)
Asset repository - Asset repository (Revocationrequest)

## Requirements overview (optional)

Template ID: d-e81d65b641f94be3b2d0917fb1257503

*Emails: 
Email will be sent at 6 PM everyday with the list of lien removal requests raised after 6PM T-1 till 6PM T0.*

*BFL:*

*To: [las.crm@bajajfinserv.in](mailto:las.crm@bajajfinserv.in) , [las.collateral@bajajfinserv.in](mailto:las.collateral@bajajfinserv.in), [operations@voltmoney.in](mailto:operations@voltmoney.in)* 

*BCC: vaibhav.arora@voltmoney.in*

*Tata:
To: [tata.operations@voltmoney.in](mailto:tata.operations@voltmoney.in)*

*BCC: [vaibhav.arora@voltmoney.in](mailto:vaibhav.arora@voltmoney.in)*

## User stories / User flow

## Requirements

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