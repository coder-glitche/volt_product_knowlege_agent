# Phone and Email validation on PLJ

: Ranjan kumar Singh
Created time: June 6, 2024 12:05 PM
Status: In progress
Last edited: February 19, 2026 7:14 PM
Owner: Lalit Bihani
Tasks: Phone and Email validation on PLJ (https://app.notion.com/p/Phone-and-Email-validation-on-PLJ-aa32b5007a9b4d8c8d557f1d079bee93?pvs=21)
Due Date: 06/06/2024

# **What problem are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

### **Issues Faced When MFDs Enter Incorrect Information:**

### **Customer Issues:**

- Transaction communications are not sent to the actual customer.
- The customer is unable to withdraw funds.

### **Risks for Volt Money:**

- Lender compliance risk due to incorrect contact information.

---

# **How do we measure success?**

- Reduced phone and email change requests from customers/MFDs.
- Currently we are getting 3-4 phone change request per week

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

- When user click on register customer CTA , Open register customer side drawer on Desktop and full screen modal on Mobile device
    - Remove all current input field and keep only Mobile number and Customer name input field
        - Customer name and Mobile number field will be required field
    - Nudge to user that OTP will be sent to verify mobile
    - After entering customer name and mobile number user should be able to proceed and OTP will be triggered on provided mobile number
- When user click on get OTP CTA, Verify if customer exist? if yes show Customer exist modal else Open enter OTP modal
    - If OTP is verified, Create customer in DB, link with partner and take user to Customer registered successfully
        - Show name of customer on drawer header, entered by partner
        - Handle OTP validation as per current implementation
        - Once pan is  validated, replace Customer name as per PAN
- When user click on Edit mobile number CTA on  OTP Modal
    - Close modal and Allow Partner to go back on Register customer screen/modal where user should be able to edit mobile number and name and trigger OTP again
- When user are registering the customer after MFC fetch
    - Pre-fill Mobile number on Register customer drawer
    - Pre-fill PAN on PAN validation step
    - Reset of the behaviour as mentioned above.
- For PLJ Journey, Skip home screen “Screen on which we show Benefits, Blog link and FAQ”
- Show “Share application link with client” on header with Copy link and share via WA

## User stories / User flow

## Requirements

---

# **Design**

[https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/Partner-flow?node-id=4328-72184&t=ViZZkeuhUXc8eRhc-4](https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/Partner-flow?node-id=4328-72184&t=ViZZkeuhUXc8eRhc-4)

---

# **Analytics**

**New registration**

User journey: User click on Register customer > user enters phone and name >user enters OTP > Success or failed page > User click on continue journey > API call to load bundle > API call to load customer > user land on current step

### PLJ INSTRUMENTATION

| User action/API Events | Event name | Event attribute | Comment |
| --- | --- | --- | --- |
| User click on “continue loan application” After registration is completed

OR

User click on “Complete application” on pending application table

OR

User click on “View as client” CTA on completed application table | **PLJ_LOAD_INITIATED** | TRACKING_ID  | TRACKING_ID  = {6 Digit random character} - Generated for each PLJ session start

- We need to generate and pass unique id to and events attributes for the events PLJ are initiated
-  Same unique id we need to pass to the subsequent events to track the events fired against the unique id |
| Short token api called | PLJ_SHORT_TOKEN_GENERATION_INITIATED | TRACKING_ID 
INITIATED_AT |  |
| Short token api success | PLJ_SHORT_TOKEN_GENERATION_COMPLETED | TRACKING_ID  |  |
| Short token api failure | PLJ_SHORT_TOKEN_GENERATION_FAILED | TRACKING_ID  |  |
| App bundle download start | PLJ_APP_BUNDLE_LOADING_INITIATED | TRACKING_ID 
 |  |
| App bundle download completed | PLJ_APP_BUNDLE_LOADING_COMPLETED | TRACKING_ID 
 |  |
| App bundle download failed | PLJ_APP_BUNDLE_LOADING_FAILED | TRACKING_ID 
 |  |
| Send the short token as message to borrower app. | PLJ_SEND_SHORT_TOKEN_TO_APP_BUNDLE | TRACKING_ID 
 |  |
| Api for the refresh token called  | PLJ_SHORT_TOKEN_TO_LONG_TOKEN_GENERATION_INITIATED | TRACKING_ID 
 |  |
| Api for the refresh token completed  | PLJ_SHORT_TOKEN_TO_LONG_TOKEN_GENERATION_COMPLETED | TRACKING_ID 
 |  |
| Api for the refresh token failed  | PLJ_SHORT_TOKEN_TO_LONG_TOKEN_GENERATION_FAILED | TRACKING_ID  |  |
| reload app on receiving the access token | PLJ_REDIRECT_USER_TO_APP | TRACKING_ID  |  |
|  |  |  |  |

**Pending application**

User journey: Partner click on complete application on table > API call to load bundle > API call to load customer > user land on current step

**Completed application**

User journey: Partner click on view as client on table > API call to load bundle > API call to load customer > user land on my account page

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

Events:

| User action | Event name | Event attribute | Event exist |
| --- | --- | --- | --- |
| User clicked on Register customer | **ASSISTED_JOURNEY_BUTTON_CLICKED** |  | Yes |
| User Enters Name, Phone and click on get OTP | OTP_REQUESTED_TO_REGISTER_CUSTOMER | - name
- phone | No |
| OTP result | OTP_VERIFICATION_RESULT | TRUE/FALSE | No |
| User clicked on continue journey, and API called to loan iframe/Bundle | BUNDLE_LOAD_INITIATED | internet_strength | No |
| User clicked on PLJ close button | PLJ_CLOSE_BUTTON_CLICKED | current_page | No |
| Bundle/iframe loaded successfully | BUNDLE_LOAD_SUCCESS |  | No |
|  |  |  |  |