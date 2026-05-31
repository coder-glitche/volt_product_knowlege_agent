# Lodgement maker

: Vaibhav Arora
Created time: November 29, 2024 4:26 PM
Status: Pending Review
Last edited: November 29, 2024 4:43 PM

# **What problem are we solving?**

Users pledge securities before their loan account is created with the bank, users also pledge additional securities post origination. 

Scenarios can arise where the user has pledged securities, however the same have not been added to their loan account, ops team will need a capability through which they can manually lodge these securities into the user’s loan account via the command centre

---

# **How do we measure success?**

- Number of dangling securities pledged in the name of DSP but not lodged to an active loan
- Number of dangling securities as a percentage of total pledged securities in the name of DSP
- Number of days where securities were in a dangling state before they were either unpledged or mapped to a loan account

---

# **How are others solving this problem?**

Other lenders have operational processes, with regular reconciliation processes, they identify dangling securities and map it to the loan account. 

They have a maker checker process, where a person can make the request, and then the other person approves the request. They do not however have a dedupe logic at their end, as well as a lien validation check (which validates if the securities that are being lodged to the loan account are actually pledged in the name of the lender or not).

---

# **What is the solution?**

We will create a maker task, where the ops agent will be able to select an RTA and basis RTA add a lien reference number (unique to one pledging request). 

Against which we will hit the lien status API and get all the securities pledged in that particular session as well as their current status. Once we have the status, we will give the ops agent to select the desired securities which they want to map to the loan account, and give the user the respective drawing power.

CAMS → Lien reference number

KFIN → KFIN session number

For the sake of convenience, we can call them as a common identifier for easy communication between operations team.

<aside>
⚠️

Note: This process will have to be done at a RTA level, that is if a user has pledged securities with the two RTAs, we will be creating two corresponding lodgement requests to accurately track the status of the pledge and corresponding lodgement 

</aside>

High level flow:

- Ops agent identifies dangling securities (via reconciliation process or a customer/partner request)
- Ops agent then finds the request identifier (KFIN session number/ Lien reference number) and the PAN that holds the securities
- Ops agent then searches for the customer and goes to their loan account
- Upon reaching the loan account, they will be able to perform an action on the loan, which will be called as “Add collateral”.
- Once they select add collateral, ops agent will be able to select the RTA and then add the corresponding request identifier (KFIN session number/ Lien reference number)
- We will then hit the lien status API get the pledged securities and show the same to the ops agent
- Ops agent will then be able to select the securities that they want to add to the loan account. They should see the following details corresponding to each security
    - Scheme name
    - ISIN
    - Folio Number
    - Lien reference number
    - Lien marking number
    - Number of units
    - PAN number (security)
    - Mobile number
    - Email address
    - Lien status
- They should also see the following client/loan details:
    - Client PAN
    - Client email address
    - Client mobile number
    - Client held assets (current holding details)
- Once selected, they will reach a confirmation screen post which the assets will be requested for lodgement
- We will then send the request for internal collateral dedupe and if it is successful, the securities will be lodged against the loan account

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