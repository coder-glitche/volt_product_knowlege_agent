# Pledge error handling v1

: Devansh Kar
Created time: September 12, 2025 9:06 AM
Status: Not started
Last edited: October 1, 2025 9:19 AM

# **What problem are we solving?**

- In the last 3 months, majority of user escalations to support are related to pledge failures from **CAMS and KFin RTAs**. (For instance 41 tickets in last 2 weeks of Aug)
- Currently, these errors are not handled: users see generic failure messages and raise tickets with customer support.
- This creates friction in the journey, increases TAT for resolution, and causes user drop-offs.

**Goal:** Show clear, actionable error messages for the most frequent pledge errors in frontend so users can self-resolve or know what to do next, reducing support load.

---

# **How do we measure success?**

- **% reduction in support tickets** raised for pledge-related failures (baseline = last 3 months avg).
- **% of users who retry & successfully complete pledge** after encountering an error.
- **NPS/CSAT uplift** for pledge flow experience.

---

# Scope

- Handle **Top 5–7 pledge errors** from CAMS & KFin that cover >80% of escalations.
- Configure  **frontend error messages** mapped to each error.
- Add **retry action** where possible.
- Backend auto-retry orchestration wherever possible

---

# **What is the solution?**

## Requirements

1. For KYC errors from KFin/ CAMS the error card can be shown to user.

| Error Type | Error Message | Reason for the error | Title | Error message to be shown | Action |
| --- | --- | --- | --- | --- | --- |
| Root-level(KFin) | Error occurred while validating PAN or KYC. Try again later. | Occurs when there is no response from the KYC API or some unknown error occurs while API call made. Advised to retry | Details could not be verified, | KYC or PAN validation failed due to a temporary issue. Please retry after ‘X’ hours | KFin Pledge: ‘Retry’ CTA |
| Root-level | Unable to verify KYC Status | Sent when the status code is not (200) from the API. Advised to retry |  | KYC/ PAN validation failed due to a temporary issue. Please try again in sometime. | KFin Pledge: ‘Retry’ CTA |
| Root-level | KYC API error while validating KYC Status. Try again later | Some unexpected error occurs in the process , so to handle the error we send this response.Advised to retry |  | KYC/ PAN validation failed due to a temporary issue. Please try again in sometime. | KFin Pledge: ‘Retry’ CTA |
| Root-level | Investor KYC is On-hold, please complete the KYC to proceed forward. | When there is a KYC block and is on hold we pass this message. (Terminal) |  | Unable to proceed with application as your KYC is on hold with CAMS/KFIN | Contact us |
| Root-level | KYC Rejected | Not in our codebase , it comes as a message from the KYC API. |  | KYC/ PAN validation failed due to a temporary issue. Please try again in sometime. | KFin Pledge: ‘Retry’ CTA |

For errors where KYC status 

b. Error message in KFin Pledge: “Request not Allowed as one of the folio is Under Cooling Period”.

**Case 1:** If the user has done **fetch** through **MFC,** and no. of funds received from Karvy > 1 and one of the funds fetched is ~~Nippon fund~~ under cooling period.

1. When the user tries to pledge via CAMS and KFin and gets the **above** error from KFin in BE, then user should be shown the error message “Request not Allowed as one of the folios is Under Cooling Period due to updated contact details” with CTA to “Refetch” via KFin.
2. If funds received post KFin refetch >1 (apart from Nippon funds after cooling period) the user can pledge the remaining funds through KFin and move forward CTA. (Updated limit to be shown to user)

**Case 2:** If the user has done **fetch** through **MFC,** and no. of funds received from Karvy = 1 and the fund is Nippon Mutual fund.

1. When the user tries to pledge via CAMS and KFin and get the above error from KFin in BE, then user should be shown the error message “Request not Allowed as one of the folios is Under Cooling Period due to updated contact details” with CTA to “Refetch” via KFin.
2. If refetching through KFin still fails due to availability of fund in KFin which is under cooling period then user should be shown the ~~“Fetch failed due to funds in cooling period. Please proceed by pledging the remaining funds” and user should be given CTA to Proceed.~~then updated limit from CAMS and be made to proceed forward.

**Case 3:** If the user has done fetch though RTA and the number of funds from KFin > 1 (including Nippon funds which are initially not under cooling period.)  Let’s assume the user updates the contact details for Nippon fund before pledging.

1. In the above case while pledging through KFin, the BE will get the above error message from KFin and the user should be shown the error message “Request not Allowed as one of the folios is Under Cooling Period due to updated contact details” with CTA to refetch via KFin.
2. If funds received post KFin refetch >1 (apart from Nippon funds after cooling period) the user can pledge the remaining funds through KFin and move forward. (Updated limit to be shown to user)

**Case 4:** If the user has done **fetch** through **RTA,** and no. of funds received from Karvy = 1 and the fund is ~~Nippon Mutual fund~~ under cooling period. Let’s assume the user updates the contact details for Nippon fund before pledging.

1. When the user tries to pledge via CAMS and KFin and get the above error from KFin in BE, then user should be shown the error message “Request not Allowed as one of the folios is Under Cooling Period due to updated contact details” with CTA to “Refetch” via KFin.
2. If refetching through  KFin still fails due to availability of fund in KFin which is under cooling period then user should be shown the ~~“Fetch failed due to funds in cooling period. Please proceed by pledging the remaining funds” and user should be given CTA to Proceed.~~then updated limit from CAMS and be made to proceed forward.
3. If refetched funds from KFin > 1 (apart from cooling period funds) the user can pledge the remaining funds through KFin and move forward.

c. Error message in KFin Pledge (Validate API): “RequestID Cannot Process as Units are Not Available” or CAMS (Validate API): “Pass lien units less than or equalto available balance”

---

# **Design**

[https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=8070-17560&t=6RQDFEmd51LM9wbL-0#1429436552](https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=8070-17560&t=6RQDFEmd51LM9wbL-0#1429436552)

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