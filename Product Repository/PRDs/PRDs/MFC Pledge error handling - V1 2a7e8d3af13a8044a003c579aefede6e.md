# MFC Pledge error handling - V1

: Devansh Kar
Created time: November 10, 2025 9:06 AM
Status: Not started
Last edited: December 8, 2025 10:53 AM

# **What problem are we solving?**

- Currently, as we have made MFC Pledge live for B2B2C and B2C channels and plan to dial up for other channels as primary mode for pledging, we need to address and handle the top errors that have occurred until now.
- Currently, these errors are not handled: users see generic failure messages and raise tickets with customer support.
- This creates friction in the journey, increases TAT for resolution, and causes user drop-offs.

**Goal:** Show clear, actionable error messages for the most frequent pledge errors in frontend so users can self-resolve or know what to do next, reducing support load.

---

# **How do we measure success?**

- **% reduction in support tickets** raised for pledge-related failures (like limit updated)
- **% of users who retry & successfully complete pledge** after encountering an error.
- **NPS/CSAT uplift** for pledge flow experience.

---

# Scope

- Handle **Top pledge errors** from MFC (for CAMS and KFin funds) i~~n the last 1.5 months.~~
- Configure  **frontend error messages** mapped to each error.
- Add **retry action/ pledge remaining funds** where possible.
- Backend auto-retry orchestration wherever possible.
- This might not be the full list of errors we are handling. As we dial up and get new errors, we will handle those in the upcoming versions of error handling.

---

# Data

---

# **What is the solution?**

## Requirements

1. For errors associated to CAMS and KFin funds, which are not related to lien units mismatch, the following error handling can be done.

| Folio RTA | Error Type | Error Message | Reason for the error | Title | Error message to be shown | Action |
| --- | --- | --- | --- | --- | --- | --- |
| CAMS | Fund level | Scheme is not mapped to your client id. | Scheme is not in the approved list of CAMS/ MFC | Scheme code of the folio is absent | Scheme code of the folio is not in the approved list of CAMS. Please contact support. | **CTA:**
-’Pledge remaining funds’
‘Contact support’  |
| CAMS | Fund level | Mobile number is not linked to the folio(s) of this PAN. | Occurs when mobile number passed in request doesn’t match with mobile number for a given folio | Mobile number does not match for some of the folios | Mobile number is different for the given folio(s) - 
{{X}}
{{Y}}
{{Z}} Request you to update and use the same mobile number for all the folios and retry pledging | **CTA:**
-’Pledge remaining funds’
- ‘Contact support’ 

 |
| CAMS | Fund level | Given folio not match with given PAN. | If the folio details / any details( Scheme code / ISIN ) provided in the payload doesn’t match with the folio details in the DB/ PAN due to folio being archived, prospect folio, etc. | Some folio(s) don’t match with the given PAN | The given CAMS folios don’t belong to your PAN:

{{X}}
{{Y}}
{{Z}}

Please refresh portfolio and try again | **CTAs:
-** ’Refresh portfolio’
- ‘Contact support’ 
 |
| KFin | Fund level | Investor Information is not valid | Mobile number/ Email passed in request doesn’t match with the folio details mobile/ email | Details do not match for some of the folios | Mobile number/ Email is different for the given folio(s) - 
{{X}}
{{Y}}
{{Z}} Request you to update and use the same mobile number & email for all the folios and retry pledging | **CTAs:
-** ’Pledge with remaining funds’
- ‘Contact support’  |
| KFin | Fund level | Invalid Folio Details, Data not found | When the folio details (Scheme code / ISIN) provided in the payload doesn’t match with the folio details in the DB/ or doesn’t come under PAN | Some folio(s) don’t match with the given PAN | The given folios below don’t belong to your PAN:

{{X}}
{{Y}}
{{Z}}

Please refresh portfolio and try again | **CTAs:
-** ’Refresh portfolio’
- ‘Contact support’  |
| KFin | Fund level | One of the Folio is Under Stop Payments | AMC has blocked the folio from transaction for any reason | One of the Folio is restricted for transaction | AMC has restricted the following funds for transaction
{{X}}
{{Y}} | **CTAs**
‘Pledge with remaining funds’ |
| KFin | Fund level | DMAT Flag is not valid | Funds are in demat | Demat funds error | Some of your funds are demat and are not eligible for pledging | **CTAs**
‘Refresh portfolio’ |

1. The validate lien API will be called as soon as the user enters the Pledge step before clicking on continue. The error message as per the table above will be shown upfront to the user.
2. In all the above cases mentioned in the table, when user gets error for CAMS funds only, then refreshing the portfolio will only do a CAMS refetch and pledge with MFC. (2 OTPs). [error message: “Given folio not match with given PAN”.]
3. If post refetching the portfolio with CAMS and pledging with MFC, the error still persists, then the same error messaging will appear on the UI as mentioned in the table above with CTA to either “Pledge with remaining folios” or “Contact support”.
4. If user clicks on “Pledge with remaining folios”, then from BE, it should remove the funds for which the specific error message appears and try repledging with MFC (1 OTP). [Total 4 OTPs]
5. The updated pledge limit after removing the funds with error messages should be shown to the user on UI.
6. If the user clicks on “Contact support”, then email popup can appear for users to raise a ticket on the same.
7. In all the above cases, when user gets error for KFin funds, then refreshing the portfolio will only do a KFin refetch and pledge with MFC. (2 OTPs). [error message: a) “Invalid Folio Details, Data not found”. b) “DMAT Flag is not valid”]
8. If post refetching the portfolio with KFin and repledging with MFC, the error still persists, then the same error messaging will appear on the UI as mentioned in the table above with CTA to either “Pledge with remaining folios” or “Contact support”
9. For the KFin funds error (”One of the Folio is Under Stop Payments”), the BE should remove the funds and show the updated pledge limit to the user when user clicks on “Pledge with remaining funds” CTA.
10. For cases where the error remarks come for both CAMS and KFin, then refetching from both CAMS and KFin will be done (except when KFin error remarks is “One of the Folio is Under Stop Payments”).

b. For units mismatch error remarks:

| Folio RTA type | Error Type | Error Message | Reason for the error | Title | Error message to be shown | Action |
| --- | --- | --- | --- | --- | --- | --- |
| CAMS | Fund level | Pass lien units less than or equal to available balance. | Lien eligible units are less than requested units | Requested Lien units unavailable | Lien eligible units are less than requested units. Please refresh portfolio | **CTA:** ‘Refresh portfolio’ |
| CAMS | Fund level | There is no available balance to the mark the lien in the given folio and scheme. | Lien eligible units are 0/ less than requested units | Requested Lien units unavailable | Lien eligible units are less than requested units. Please refresh portfolio | **CTA:** ‘Refresh portfolio’ |
| KFin | Fund level | Free Units are less than Lien Units | Lien eligible units are less than requested units | Requested Lien units unavailable | Lien eligible units are less than requested units. Please refresh portfolio | **CTA:** ‘Refresh portfolio’ |
| KFin | Fund level | No free units avaliable | Lien eligible units are 0/ less than requested units | Requested Lien units unavailable | Lien eligible units are less than requested units. Please refresh portfolio | **CTA:** ‘Refresh portfolio’ |
| KFin | Fund level | Available units 0 are less than requested pledge units 380.5 | Lien eligible units are 0/ less than requested units | Requested Lien units unavailable | Lien eligible units are less than requested units. Please refresh portfolio | **CTA:** ‘Refresh portfolio’ |
| KFin | Fund level | Available units 0 are less than requested pledge units 65.95 | Lien eligible units are 0/ less than requested units | Requested Lien units unavailable | Lien eligible units are less than requested units. Please refresh portfolio | **CTA:** ‘Refresh portfolio’ |

1. For unavailable requested lien units errors, if we only receive them corresponding to CAMS, then only CAMS refetch will happen, with notifying new limit to the user. Post which MFC repledge needs to be done by the user. (3 OTPs)
2. For unavailable requested lien units errors, if we only receive them corresponding to KFin, then only KFin refetch will happen, with notifying new limit to the user. Post which MFC repledge needs to be done by the user. (3 OTPs)
3. If limit mismatch errors come for both CAMS and KFin, then refetching will be done for both CAMS and KFin, with notifying the new limit to the user. Post this MFC repledging CTA will happen. (4 OTPs)

**Error Handling type 1:** 

---

# **Design**

[https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=4-13&p=f&t=kdJe8c9ZBfMQbHA4-0](https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=4-13&p=f&t=kdJe8c9ZBfMQbHA4-0)

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