# [CC] Lodgement Enhancement

: Surya Ganesh
Created time: January 30, 2025 6:30 PM
Status: Not started
Last edited: February 7, 2025 6:19 PM

# **What problem are we solving?**

The operations team needs to verify loan collateral before lodgement for the following conditions:

1. Loan Value over 10L: To ensure we are not in credit risk in cases with large amounts
2. Date mismatch (more than a day): To ensure the funds which are up for lodgements are still pledged and no un-pledging request for those funds have been raised.

These ensure that we minimise credit risk (assign accurate credit limit to right loan accounts).

- **Current steps to approve a lodgement considering there are two folios, one for CAMS and another for Kfintech**
    1. Login to CC:
    - Check maker name
    - Look at lien reference number
    1. Then for KFINTECH RTAs:
    - Log into Kfintech dashboard
    - Search using user’s PAN number
    - Navigate to pledge portfolio section
    - Manually match: (between Lodgement request and KFIN dashboard)
        - IH number
        - Lien reference
        - Folio number
        - ISIN number
        - Units pledged
    
    ii. For CAMS RTAs:
    
    - Switch to email (agent’s inbox) and search for the specific lien reference number for the lodgement. We are doing this for checking if there have been any un-pledging requests raised by the user for the collaterals we are looking to lodge.
    - Look for confirmation emails using the lien reference number which will give the lien status details to cross-verify the Name, ISIN, Folio and the Units pledged against DSP

Current challenges in this process:

1. Manual Verification Overhead
    1. Operations team must verify 8+ fields (ISIN, Folio, Units, etc.) manually across different platforms:
        - CC (Core system)
        - Kfintech Dashboard (RTA verification)
        - Email inbox for CAMS Verification
    2. Manual verification of several parameters introduces high risk of human error during cross-checking
2. Fragmented Data Sources and Process Differences:
    1. Different workflows for KFINTECH and CAMS RTAs:
        - KFINTECH requires dashboard login and manual field matching
        - CAMS requires email verification and multiple email searches
3. Non-terminal status cases of Kfintech aren’t re-checked:
    1. LM hold and LM pending case are polled for 30mins with the Status API being called every 5mins. After which, the status API isn’t called to re-check the status.
    2. LM hold and LM pending cases are showcased to the Ops team but aren’t differentiated from other LM success cases
    3. The time between when the task is made and when it is picked for approval by the Ops personnel, there are significant chances of these cases having their status changed to a Terminal Status i.e LM Success or LM Fail, thus loosing out on potential DP for the user.
4. Non-terminal Kfintech lodgements are not visible:
    1. In cases where the LM pending lodgements were auto-rejected but they get LM success later-on (when the Ops team starts checking the details) they are not able to approve that lodgement as it is not available to the Ops team to lodge.

---

# **How do we measure success?**

1. Approval of the lodgement process within 30 seconds for cases with equal to or less than 10 folios and less than 3 minutes for cases less than or equal to 50 lodgement.

---

# **How are others solving this problem?**

NA

---

# What is the solution?

Following are the solutions we will be implementing to increase the efficiency of the Ops team and reduce the time taken to approve lodgements:

## Requirements Overview

1. Addition of De-dupe status in the “request details” (system generated)
2. Renaming and addition of the tabs:
    1. Client details, unchanged
    2. Loan details, minor change
    3. “Transactions “ to be changed to→ “Statements”
3. Re-ordering and addition of the Details within a lodgement to the following: 
    1. RTA
    2. Lien reference /IH number
    3. Folio
    4. ISIN
    5. Quantity→ **Requested Units (to be renamed)**
    6. **Pledged Units (Additional Parameter, to be fetched from the Pledged Portfolio Request API for Kfintech and Final Status Checking for CAMS)**
    7. Mode of Holding
    8. Collateral Sub Type
    9. LTV
    10. Market value
    11. Limit
    12. **Time-stamp for Last Refresh**
    13. **Last Status Update**
4. Showcase the status tag as “Will Be Rejected” on the lodgement header in case the specific collateral is on LM pending or LM hold. Additionally, provide a **Refresh Button** for the collaterals which are on LM pending or LM hold that will enable the ops personnel to refresh that specific lodgement. 
If the refresh is successful, the Time-stamp for the Last Refresh should be updated as well as if the status is terminal, subsequent changes should be made to the Lodgement:
    1. In case of the pledging status updating to a success, “Will Be Rejected” should be changed to “Success” and the “Last Status Update” parameter should get updated to success
    2. In case of the pledging status updating to a failure, the lodgement action buttons should be disabled as well as the “Will be rejected” tag should be changed to “Failed” along with the “Last Status Update” getting updated to failed 

## User stories / User flow

1. The Ops personnel starts by checking the maker of the lodgements 
2. Then, opening the first case, checks:
    1. **Pledged Units**
    2. **Requested Units**  (should be ≥ Pledged units to approve)
3. Then, completes all the lodgements which have had “success” pledging status.
4. Coming to the lodgements which do not have a terminal status (LM pending or LM hold),
    1. Refreshes the lodgements
    2. Checks for the status update
        1. Incase of the status update to a terminal success, approves the lodgement after checking for the pledged and requested units
        2. Incase of the NO status update (still being on LM pending or LM hold), Ops personnel can login to Kfintech dashboard to double check the status.
            1. If it is still pending, they should reject the lodgement.
            2. If it is a success, check the units and approve.
            3. If it is a failure, reject the lodgement.

---

# **Design**

Problem understanding 

---

# **Analytics**

---

# **Timeline/Release Planning**

To be picked up in the Sprint Feb B

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