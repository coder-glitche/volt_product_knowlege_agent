# Loan renewal for TCL customer’s

: Ranjan kumar Singh
Created time: October 3, 2024 4:25 PM
Status: Not started
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

### Loan renewal process summary:

- TCL has a negative consent-based loan renewal process, which means if a customer doesn't explicitly state they don't want to renew the loan, it will be automatically renewed.
- If a customer opts not to renew their loan, they must clear the due before the maturity date. Otherwise, 3% per month penal charges will be added to the POS amount.
    - If the user doesn't clear the foreclosure amount within 7 days of loan expiry, the TCL team will initiate a securities sell-off to recover the amount. Remaining securities will then be released by the TCL team.
    - The sell-off amount will be equal to the foreclosure amount.
- If a customer hasn't given negative consent, the TCL team will renew the loan on the loan maturity date.
    - New loan maturity date = Current maturity date + 365 days
    - Customers are not required to pay the outstanding amount
    - A renewal fee of 499 + GST will apply
    - Users are not required to go through the loan application process again (Re-KYC, mandate, and agreement are not required)

Renewal Modes:

- Manual Loan Renewal Process [V1]
    - Since the API for loan renewal is currently unavailable, we need to follow a manual process to renew loans.
    - Process/SOP:
        1. Collect renewal consent from customers
            1. Channel: Volt App only
            2. Maintain a config-based cut-off time for negative consent
        2. Send list of customers with negative consent to TCL on MD-2
        3. TCL to send list of customers whose renewals are completed
        4. Volt to post renewal fee for all customers shared by TCL
- API-based Loan Renewal Process [V2]
    - Although the loan renewal API is not currently available, we need to develop a solution that can seamlessly handle renewals once TCL makes the API available.
    - Process:
        1. Volt to call Miles API to update the loan maturity date
            1. Daily CRON-based API call to renew loans for customers who haven't given negative consent
            2. Renewal API will be called on the maturity date after 6 PM
        2. Once the maturity date is updated, Volt needs to post the renewal fee

### Handling of loan which are not allowed for renewal

As per TCL’s recent policy amendment on renewals, customers who do **not** meet the criteria listed below will **not** be allowed to renew their loans.

### **Latest Amended Policy Parameters for Renewals**

A customer is eligible **only if all** the below conditions are met:

1. No more than **2 instalment bounces** in the last 6 months
2. **No 30+ DPD** in the last 3 months
3. **No 90+ DPD** in the last 6 months
4. **CIBIL score > 650**

To handle this situation and to inform those customer who are not eligible to renew their loan with TCL, we have to do some Changes at our end.

**Required Changes**

- **TCL will share the list of ineligible customers** one month in advance in the below format:
    
    *(screenshot reference)*
    
    ![Screenshot 2025-12-12 at 2.52.29 PM.png](Loan%20renewal%20for%20TCL%20customer%E2%80%99s/Screenshot_2025-12-12_at_2.52.29_PM.png)
    

- **Volt Operations team will prepare a transformed file** based on the list received from TCL, in the format shown below:
    
    
    | **Credit Id** | **RenewalAllowed** |
    | --- | --- |
    | 8a80403e8b061b54018b0a63a7cd0993 | False |
    | 8a80403e8b061b54018b0a63a7cd0995 | False |
- **Operations team will upload the file** through the Admin Action panel to update the data in our database.
    - Ops will also handle customer communication (case-by-case calls + bulk communications where required).
- If a loan is marked as **RenewalAllowed = False**, the user **must not be allowed** to provide renewal consent.
    - In this scenario, the user should only be allowed to **repay the total outstanding amount** and proceed to **close the loan**.
- **UI Handling:**
    - Customers who are **not eligible for renewal** should be able to:
        - View their total outstanding amount
        - Repay the full amount
        - Raise a **foreclosure request**
- Communication handling: We will not send any renewal comms reminder to those customer who's renewal is not allowed. but will continue sending loan expiry comms to those customers.

**Important Note:**

This has been aligned with TCL: if they fail to provide the ineligible customer list at least one month in advance, and a customer has already provided renewal consent, then that case will remain eligible for renewal.
In such scenarios, we will not accept RenewalAllowed = False from the file uploaded by the Ops team.

Desing link: https://www.figma.com/design/YtIrrCHwQmfyc6DmZnw1Tq/Loan-renewal?node-id=10524-6178&t=NjlbBYCDmJx14bMC-4 

## User stories / User flow

**Scenario 1: Maturity date (MD) - Current Date ≤ 30 days && negative consent is FALSE or not set**

- User should see a notification on the Volt app
    - Data points:
        1. Header: "Loan renewal scheduled on {{MaturityDate}}" or "Loan renewal due in 30 days"
        2. Display credit limit if TOS ≤ 0; otherwise, show TOS
        3. Highlight benefits of loan renewal
        4. "View more details" CTA
- User should receive reminder communications
    - Message should state that the loan account is scheduled for renewal on the maturity date
        - Data points:
            1. POS/Credit limit
            2. Benefits of loan renewal
            3. Instructions for users who don't want to renew
            4. CTA/link to Volt app

**Scenario 2: Maturity date (MD) - Current Date ≤ 30 days && negative consent is TRUE**

**[From MD-30 to MD-2]**

- User should see a notification on the Volt app
    - Data points:
        1. Header: "Your loan will expire in 15 days"
        2. Display credit limit if TOS ≤ 0; otherwise, show TOS
        3. Highlight benefits of loan renewal
        4. "Renew now" CTA
        5. Update renewal consent if user confirms renewal before cut-off date
        6. Inform user they can change negative consent before MD-2
- User should receive reminder communications if TOS > 0
    - Message should state that the loan account will expire in X days, advising to repay outstanding amount or renew loan to avoid repayment
        - Data points:
            1. POS/Credit limit
            2. Benefits of loan renewal
            3. Instructions for users who don't want to renew
            4. Renewal consent change cut-off date
            5. CTA/link to Volt app
- **[From MD-1 to MD]**
    - Requests for withdrawal, foreclosure, lien removal, and line enhancement will not be allowed
    - User should see a notification on the Volt app
        - Data points:
            1. Header: "Your loan will expire tomorrow/today"
            2. Display credit limit if TOS ≤ 0; otherwise, show TOS
            3. "View details" or "Pay now" CTA (based on TOS)
    - User should receive reminder communications if TOS > 0
        - Message should state that the loan account will expire in X days, advising to repay outstanding amount to avoid penal charges
            - Data points:
                1. POS/Credit limit
                2. CTA/link to Volt app

**Scenario 3: Current Date > Maturity date (MD) && no renewal request is raised**

- Requests for withdrawal, lien removal, and line enhancement will not be allowed
- User should see a notification on the Volt app
    - Data points:
        1. Header: "Your loan expired on {{date}}"
        2. Display credit limit if TOS ≤ 0; otherwise, show TOS
        3. Prompt to repay if TOS > 0
        4. Use foreclosure API to calculate the TOS
        5. Take user to the repayment flow the show the break-up of the TOS amount
            1. Remove Nudge from the repayment page “This amount might not be correct, contact support….”
        6. When TOS <0 then allow user to raise the loan closure request [if not raised automatically]
            1. Take user to foreclosure flow > user should directly land on loan details page, confirm closure with OTP and than show loan closure status page [No option to cancel request on status page in this case]
            2. Foreclosure request will be sent to lender in MIS
            3. lien removal request will be raised once foreclosure is raised
- User should receive reminder communications if TOS > 0
    - Message should state that the loan account has expired and the outstanding amount needs to be repaid
        - Data points:
            1. TOS
            2. Information about last due date, penal charges, and sell-off date
            3. CTA/link to Volt app

**Scenario 4: Current Date > Maturity date (MD) &&  renewal request is raised**

- User should see a notification on the Volt app
    - Data points:
        1. Header: "Loan renewal is in progress"
        2. ETA for renewal completion

## Requirements

---

# **Design**

https://www.figma.com/design/YtIrrCHwQmfyc6DmZnw1Tq/Loan-renewal?node-id=9018-8830&p=f&t=XWIhqFTt3VD6HLTJ-0

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