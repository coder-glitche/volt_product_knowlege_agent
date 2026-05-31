# Pre-fetch flow Optimisation: Consolidating PAN flow

: Priyamvada S
Created time: June 3, 2025 2:04 PM
Status: Done
Last edited: February 19, 2026 9:43 AM

# **What problem are we solving?**

Currently, users have to go through multiple sequential screens : PAN & DOB entry screen, followed by a PAN validation pop-up, and then a separate eligibility initiation screen-ie a  lengthy pre-fetch flow which is adding friction & causing user drop-offs in top of funnel.

---

# **How do we measure success?**

- **% Increase in users initiating eligibility checks after successful email verification**, segmented by B2B2C and B2C channels
- **~~Total cost savings from dropped Decentro PAN validation API calls~~**

# **How are others solving this problem?**

NA

---

# **What is the solution?**

We propose streamlining the pre-fetch flow by removing non-essential inputs for fetch like DOB and consolidating the key fields—PAN and mobile number—along with the eligibility check into a single ‘Check Eligibility’ screen. This simplification is intended to reduce friction by shortening the journey and improve fetch initiation rates

## Proposed User Journey & BE  Requirements

### Applicable channels:

- B2C App  flow
- Applicable B2B partners
- B2C Web app flow via ‘Sign In” CTA entry point (ie fetch done post user details entry)
- B2B2C Flow via “Onboard a Customer” entry point (ie fetch done post user details entry)

### User journey

*MFC fetch flow*

- Upon successful mobile OTP verification and email confirmation, the user lands on the **‘Eligibility Check Initiation’** screen (i.e., the **‘Check Eligible Credit Limit’** screen).
- The user is prompted to enter their **PAN number** and confirm the **pre-filled mobile number** to initiate the **MFC eligibility check**.
- On submission of details:
    - First a backend call is triggered to Decentro API to get the PAN validity status, post which the MFC fetch api is hit
        - Note: In case the Decentro api is down, the flow will remain blocked—consistent with the current behavior.
    - If the **PAN + mobile number** combination is valid, an OTP is sent to the mobile number.
    - If “PAN + mobile number” combination is invalid, described below is the error handling:
        - Case 1: PAN invalid (ie PAN not in existence)
            - Identified by the following errors received in the backend:
                - Decentro response key: “error_invalid_pan”
                - ~~MFC Error message : "User has not invested in mutual funds”~~
            - Below error message to be shown to user with an option to **‘Edit Details’**, on hitting which the user is taken back to the Eligibility Check Initiation screen, where they can review and correct their PAN No
                - Message Header:No investments found for PAN USER_PAN_NUMBER
                - Message test: Please make sure investments are linked with the PAN USER_PAN_NUMBER
        - Case 2: Combination of ‘PAN & Mobile’ doesn’t exist/have no funds in MFC
            - Identified by the  following error code received in the backend:
                - MFC error code: MFCENTRAL.Fetch_Auth.INVALID_COMBINATION_FOR_MFC
            - Below error message to be shown to user with an option to **‘Edit Details’**, on hitting which the user is taken back to the Eligibility Check Initiation screen, where they can review and correct their PAN No/Mob no
                - Message Header:No investments found for PAN and mobile number combination
                - Message text: Please make sure investments are linked with mobile number USER_PHONE_NUMBER and PAN USER_PAN_NUMBER
        - Case 3: All other error scenarios will continue to be handled as per the existing logic.
    
    Note: There is no restriction on the number of PAN edits. However, once fetch is succesfully completed, it will become non-editable
    
- Once the user enters the received OTP, their **eligible credit limit is fetched from MFC**, and they proceed with the rest of the onboarding journey.

*KFin/Cams Flow (***Fallback Flow when MFC is Down or User actively choosing RTAs)**

- If the MFC system is unavailable, the eligibility check is  routed through **CAMS(or KFin)**
- After successful mobile OTP login and email verification, the user lands on the **‘Eligibility Check Initiation’** screen (i.e., the **‘Check Eligible Credit Limit’** screen).
- The user is prompted to enter their **PAN number** and confirm the **pre-filled mobile number** to initiate the **CAMS(or KFin) eligibility check**.
- On submission:
    - If the ‘**PAN + mobile number’** combination is valid, an OTP is sent to the mobile number.
    - If “PAN + mobile number” combination is invalid, described below is the error handling:
        - Case 1: PAN invalid (ie PAN not in existence)
            - Identified by combination of the following errors received in the backend:
                - Decentro response key: “error_invalid_pan”
                - CAMS /KFin Error message :
                    - CAMS: PAN entered ABCDE1234F is not KYC verified
                    - KFin: KFIN.Fetch_Auth.NO_INVESTMENTS_KFIN
            - Below error message to be shown to user with an option to **‘Edit Details’**, on hitting which the user is taken back to the Eligibility Check Initiation screen, where they can review and correct their PAN No
                - Message Header:No investments found for PAN USER_PAN_NUMBER
                - Message test: Please make sure investments are linked with the PAN USER_PAN_NUMBER
        - Case 2: Combination of ‘PAN & Mobile’ doesn’t exist/have no funds in CAMS(or KFIn)
            - Identified by the  following error code received in the backend:
                - CAMS error code:  CAMS.Fetch_Auth.NO_INVESTMENTS_CAMS
                - KFIN.Fetch_Auth.NO_INVESTMENTS_KFIN
            - Below error message to be shown to user with an option to **‘Edit Details’**, on hitting which the user is taken back to the Eligibility Check Initiation screen, where they can review and correct their PAN No
                - Message Header:No investments found for PAN and mobile number combination
                - Message text: Please make sure investments are linked with mobile number USER_PHONE_NUMBER and PAN USER_PAN_NUMBER
            
            Note:  There is no restriction on the number of PAN edits. However, once fetch is succesfully completed, it will become non-editable
            
        - Case 3: All other error scenarios will continue to be handled as per the existing logic.
    
      Note: here is no restriction on the number of PAN edits. However, once fetch is succesfully completed, it will become non-editable
    

- After entering the OTP, the user sees their **eligible limit** on the **‘Unlock Credit Limit’** screen.
- The user may either:
    - Proceed directly to the **‘Set Credit Limit’** step, or
    - Tap **‘Get  more Portfolio’** to view their investment holdings.
        - On tapping **‘Get Portfolio’**, a bottom sheet titled **‘Check Eligible Credit Limit’** is displayed, with **PAN and mobile number pre-filled**.
        - **PAN remains non-editable** (as it was successfully validated in the earlier fetch flow & hence non editable ), while the **mobile number remains editable**.

   Note:

- ~~The following journeys **do not involve PAN/DOB entry or PAN verification**, and are excluded from this PRD scope:~~
    - **~~B2C Web App~~**
    - **~~B2B2C flows** initiated via the **‘Check Eligibility in 15s’** CTA~~
- Might see an uptick in eligibility check failures due to missing PAN name confirmation pop-up, leading users to proceed with incorrect PAN entries for fetch

### BE Requirements

As PAN and DOB entry are now part of the **‘Check Eligibility’** screen, the **Decentro API** call for PAN validation must be triggered **before** initiating the MFC/RTA eligibility fetch (i.e., before OTP trigger).

 This call is intended to **capture the user's name in the backend**, which will continue to be used in downstream processes~~.~~

**Note:**

- We are **not deferring the Decentro API call** to post-OTP verification or post-eligibility fetch due to limited clarity on downstream dependencies on the **‘name’ field**, which is currently derived from the Decentro response.
- Trigger Decentro API call only if the entered PAN has changed since the last successful API hit.

# **Design**

[https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=5638-9400&t=03gKrKQglxA6lcmF-11](https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=5638-9400&t=03gKrKQglxA6lcmF-11)

---

# **Analytics**

FE

- Page view of new ‘Check eligible credit limit’ screen
- Field level analytics of ‘Check eligible credit limit’ screen
    - PAN i/p field clicks
    - Mob input field clicks
- Submit clicks on ‘eligibility check’ initiation screen ie: ‘Continue CTA’ clicks
- Page view of ‘Unlock credit limit’ screen
- CTA clicks on error bottomsheet (Invalid PAN, Invalid mob no,Invalid combination of PAN/Mob no) including
    - ‘Edit PAN’ /’Edit details’/’Edit mob no’ CTA
    - ’Contact us’ CTA

BE

- Total #MFC fetch initiate calls
- Total #MFC fetch failures with error code distribution( Incorrect PAN, mob no )
- Total #MFC fetch success calls
- Total #PAN edits made (ie edited & submitted)
- Total # Mob edits made

Note: Include **user/session identifiers** in the event payload for both FE & BE events including:

- `user_id`
- `session_id`
- `event_name`
- `timestamp`
- `error_code`

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