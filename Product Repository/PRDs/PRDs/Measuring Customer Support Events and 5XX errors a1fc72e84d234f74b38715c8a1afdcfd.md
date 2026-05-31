# Measuring Customer Support Events and 5XX errors

: Vaibhav Arora
Created time: February 16, 2024 12:03 PM
Status: Ready for Tech
Last edited: February 28, 2024 12:08 PM
Owner: Vaibhav Arora
Tasks: Amplitude events for support tickets + 500 (something went wrong) (https://app.notion.com/p/Amplitude-events-for-support-tickets-500-something-went-wrong-40981f5699fa44958ccb4ba6ed179054?pvs=21)
Due Date: 20/02/2024

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **CS Event Tracking - Loan Application**

# **What problem are we solving?**

- To accurately identify and measure user support issues in the loan application journey on a step by step level.
- To identify internal API errors and flow breakages in our flows and to be able to map them with respective flows to understand product and tech level issues
- Track assisted and non assisted journeys
- Identifying UX and copy issues

**Context:**

A lot of our users contact support (WA/Call/Email) while applying for a credit line and need assistance to complete the application. In most cases, our RMs end up assisting the customer in completing the application.

However it is imperative that users should be given the exact information and feedback while they are going through the application journey to be able to complete the application on their own. To correctly identify gaps, and accordingly make enhancements, we need to identify where and how our users are getting blocked in the application journey.

---

# **How do we measure success?**

- Build ability to correctly identify UX and product issues in the application journey
- Measure and attribute user query sources and plan improvements in the flow

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

Create a new amplitude event “CONTACT_SUPPORT_BUTTON_CLICKED” event 

Create a amplitude event “INTERNAL_VOLT_ERROR” event 

with event properties:

- current_screen (TBD with Tech)

Map child events once support bottom sheet is opened with following events (For Contact support event):

- CONTACT_VIA_WA_BUTTON_CLICKED
- CONTACT_VIA_CALL_BUTTON_CLICKED
- CONTACT_VIA_EMAIL_BUTTON_CLICKED

Screens where customer can initiate support flow or can face internal error:

| **Screen Name** | current_screen | **User Context** | **Product Context** | **Priority** | **Tech Alignment** |
| --- | --- | --- | --- | --- | --- |
| BORROWER_LANDING_PAGE | BORROWER_LANDING_SCREEN | User may have doubts about the product or may be unsure about |  |  |  |
| SIGNUP_OTP_PAGE | OTP_VERIFY | User may have some doubts related to the product | Understand how communication can be improved and measure success | P2 |  |
| VERIFY_EMAIL_PAGE | EMAIL_VERIFY |  |  | P2 |  |
| ENTER_PAN_PAGE | KYC_PAN_VERIFICATION | User may enquire about the details about the product before giving PAN | Measure communication effectiveness | P1 |  |
| CHECK_LIMIT_PAGE | MF_FETCH_PORTFOLIO | User may face errors in fetching their folios | Understand user errors and pinpoint issues | P0 |  |
| GET_PORTFOLIO_SUCCESS_PAGE | UNLOCK_LIMIT_LANDING | User may be confused about the assigned limit to their folio | Feedback on user communication | P0 |  |
| UNLOCK_CREDIT_LIMIT_PAGE | MF_PLEDGE_PORTFOLIO | Users may have issues with distinction between Kfintech and CAMS | Understand product awareness and communication effectiveness | P1 |  |
| SET_MF_LIMIT_AMOUNT_PAGE | SET_CREDIT_LIMIT | User may have doubts related overdraft | Understand product awareness and communication effectiveness | P1 |  |
| LOAN_SUMMARY_PAGE | PLEDGE_CONFIRMATION | User may have doubts related to specifics of the product | Understand frequent queries related to product | P2 |  |
| APPLICATION_STEPS_PAGE | KYC_STEPPER | User may have doubts with the required steps | Understand communication effectiveness and plan enhancements | P2 |  |
| KYC_START_PAGE | KYC_DOCUMENTS_DIGIO_BASE |  |  |  |  |
| KYC_ADDITIONAL_DETAILS | *Missing* |  |  |  |  |
| KYC_SUMMARY | KYC_SUMMARY |  |  |  |  |
| UPLOAD_SELFIE_PAGE | KYC_PHOTO_VERIFICATION | User may face difficulties with uploading selfie | Measure effective communication strategies and their effectiveness | P2 |  |
| CREDIT_REJECT_SCREEN | FAILED_SCREEN |  |  |  |  |
| VERIFY_BANK_START_PAGE | BANK_ACCOUNT_VERIFICATION | User may face issues with penny drop verification | Measure penny drop success and quality of error messaging | P1 |  |
| ADD_BANK_ACCOUNT_PAGE | BANK_ACCOUNT_ADD |  |  |  |  |
| AUTOPAY_PAGE |  DIGIO_MANDATE_SIGN | User may face errors with mandate set up/mandate amount limit | Measure mandate success and quality of error messaging | P0 |  |
| AUTOPAY_ERROR_BOTTOMSHEET | *Missing* to be added in Mandate error fix development | Post user receives an error | Is user able to understand the errors and respective context and act on it on their own | P0 |  |
| PLEDGE_FOLIO_PAGE | @Saksham Srivastava to get added event for this page (Add need help button currently missing on this screen) | User may face errors with pledging folio | Measure folio pledge success and assess quality of messaging and UX flows | P0 |  |
| AGREEMENT_PAGE | Independent pages for Bajaj and Tata 
BAJAJ_KFS (event missing) Check for Tata | User may have queries related to agreement | Understand frequent errors or queries related to agreement | P2 |  |
| MY_ACCOUNT_PAGE | DASHBOARD | User may have general queries once credit limit is unlocked | Measure user comfort with post loan booking UI and understanding of information architecture | P1 |  |

---

# Future Scope:

- Handle specific flow errors as event properties and measure flow specific errors within contact support
- Pass on errors to Wati and Admin tools for better handling by ops and support team to handle customer escalations

# **Design**

NA

---

# **Analytics**

Amplitude event tracking

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

- 
    
    [](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
    
    Product
    
    - Define Screen Names to be passed in event field “screen_name”
        
        [](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
        
    - Alignment and feasibility check if specific screen headers can be passed as event properties
        
        [](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
        
    - Build amplitude dashboards once implementation is complete
        
        [](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)
        

---

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes