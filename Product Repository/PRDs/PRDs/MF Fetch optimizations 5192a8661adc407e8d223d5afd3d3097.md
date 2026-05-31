# MF Fetch optimizations

: Saksham Srivastava
Created time: February 22, 2024 8:33 AM
Status: Ready for Tech
Last edited: December 15, 2025 4:53 PM
Owner: Saksham Srivastava
Tasks: CAMS & KFin Fetch issues (https://app.notion.com/p/CAMS-KFin-Fetch-issues-efa17b2d2a1049a5a5fd815046376f05?pvs=21)
Due Date: 22/02/2024

# **What problem are we solving?**

The aim is to improve MF fetch flow, to solve for this we will solve the following problems:

1. Show users contextual errors that convey what exactly went wrong for the user in fetch.
    
    Users should have better understanding of the fetch errors, the construct of LAMF, what investments can be used for LAMF, and actionable to rectify errors (for errors that can be rectified).
    
    For users downloading our app from app stores without understanding that this is not a traditional unsecured loan, these errors should handle their disappointment with grace and make them understand that the error that they are facing are because of unavailability of eligible funds. 
    
2. Flow and UI optimisations to make improve fetch success. 
    
    Users generally have limited understanding of what CAMS/ KFin are and how they operate. Making certain changes in the flow will help ease user’s cognitive overload when trying to fetch funds from both RTA
    
3. Tracking, reporting, and alerts for fetch.
    
    This will help us better track error occurrences and will significantly reduce TAT in cases of any system failure on RTA’s or volt’s end.
    
4. Improve our understanding of the different errors users face while MF fetch from CAMS and KFintech.
    
    Will reduce current ambiguity that the team has in error understanding, this will help us better handle user queries and should help us resolve these queries better. 
    

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

1. User should see contextual errors whenever MF fetch fails.
2. Next RTA should automatically be triggered for users in certain error cases to ensure higher MF fetch completion rate

## User stories / User flow

## Requirements

1. Error code mapping:
    - Error mapping for each RTA error is given is this [sheet](https://docs.google.com/spreadsheets/d/1pOOii9EQmGyJYJ2g4XOD5p2fCgbNx_gb52D1ZO75rvg/edit#gid=712598614).
        - Error screen UI: https://www.figma.com/file/PhZVp9NC4i9Nv4fnhJHI4r/Fetch-and-pledge-error-messages?type=design&node-id=35-7355&mode=design&t=drLSWQ8uLS5b2qIQ-11 (Refer only the modals, ignore the background screens)
            1. Need help CTAs will open the Need help bottom sheet.
            2. Edit details CTA will close the error bottom sheet and bring the user back to check limit page.
2. Flow/ UI improvements: 
    - Currently we retry fetch from 2nd RTA in certain auth errors. We will be expanding on that functionality to include few validation errors as well. Refer this [sheet](https://docs.google.com/spreadsheets/d/1qFkxjos_xa1pUZm98kFGV3dEEJ7KTTiw78znFAtKJbs/edit#gid=128051023) for mechanism details.
        1. This retry mechanism will be triggered only in two flows, once when the user is fetching for the first time and another when the user is doing an enhancement request. 
        2. For auth error cases we will skip directly to next RTA without showing any UI. 
        3. For validation errors (error where OTP was triggered successfully by one RTA) we will show an intermediate error screen. Figma: https://www.figma.com/file/PhZVp9NC4i9Nv4fnhJHI4r/Fetch-and-pledge-error-messages?type=design&node-id=35-7356&mode=design&t=drLSWQ8uLS5b2qIQ-4
            - Next RTA fetch OTP will be triggered when the user is on this loader screen.
            - The loader will have a load time of 3 seconds.
            - The loader text will be “Fetching your portfolio from” + {next_RTA}
    - Default order of RTA for fetch remains: CAMS → KFintech
    - Need a feature flag to hide email from check limit page UI.
3. Tracking, reporting, and alerts:
    - Amplitude: For already instrumented events-
        
        GET_MF_PORTFOLIO_AUTH_RESULT: 
        
        1. **error_type**: This will have the error FE will show to the user. (From the sheet shared only pass the heading of the error).
        2. **add new event property rta_error_type:** This will have whatever error RTA is sending us, verbatim. 
        
        **GET_MF_PORTFOLIO_OTP_RESULT:**
        
        1. **error_type**: This will have the error FE will show to the user. (From the sheet shared only pass the heading of the error)
        2. **add new event property rta_error_type**: This will have whatever error RTA is sending us, verbatim. 
    - [UPDATED Amplitude requirements]
        - BE event
            - GET_MF_PORTFOLIO_AUTH_RTA
                - result: true/false
                - rta: CAMS/Karvy
                - rta_error_type: whatever error RTA is sending us.
            - GET_MF_PORTFOLIO_OTP_RTA
                - result: true/false
                - rta: CAMS/Karvy
                - rta_error_type: whatever error RTA is sending us.
        - FE event
            - GET_MF_PORTFOLIO_AUTH_USER
                - result: true/false
                - rta: CAMS/Karvy
                - error_type: Heading of the error we are showing to the user.
            - GET_MF_PORTFOLIO_OTP_USER
                - result: true/false
                - rta: CAMS/Karvy
                - error_type: Heading of the error we are showing to the user.
    - Slack: in #mfd-customer-mf-fetch and #non-mfd-customer-fetch pass the exact error that RTAs are sending volt.
        
        {user_name} + “tried” {generating /validating} + “OTP for Fetching CAS in” + {CAMS/KFin} +  “and received error” + {header} + “due to” + {rta_error} + “PAN:” + {user_pan} + “Email” + {user_email} + “Phone” + {user_phone} 
        
    

---

# **Design**

---

# **Analytics**

---

# Future scope

1. Next RTA should automatically be triggered when the user has successfully fetched holdings from one RTA. (Users actually read the holdings that are fetched from one RTA before fetching another, the flow should not negatively impact this user behaviour) **[To discuss]**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Understanding need for training material from Ops
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

Error understanding is this [sheet.](https://docs.google.com/spreadsheets/d/1_v_BUv1i0jUb5AUZh2gFbAoFaVsli6T5xxZmF9XA8_8/edit#gid=1265241962) 

---

# **Appendix**

## Meeting notes