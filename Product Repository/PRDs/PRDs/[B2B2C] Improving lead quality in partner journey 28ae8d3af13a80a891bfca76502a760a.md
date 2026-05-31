# [B2B2C] Improving lead quality in partner journey

: Ameya Aglawe
Created time: October 12, 2025 7:44 PM
Status: In progress
Last edited: December 29, 2025 2:56 PM
Owner: Ameya Aglawe
Assignee: Ameya Aglawe

# **What problem are we solving?**

---

- A large volume of junk leads are entering the **partner journey funnel**, primarily contributed by customers mistakenly starting the partner flow. As a result, the **sales team spends significant time manually validating ARNs on AMFII** and calling these users to verify details — consuming bandwidth that could otherwise be used for genuine partner outreach. This noise severely impacts sales efficiency and delays engagement with actual, high-quality partners.

# **How do we measure success?**

---

- Reduce junk leads in the partner journey by **30%**
- Reduce sales team bandwidth spent on junk leads by **~5 hours per week**

# **How are others solving this problem?**

---

- **Smallcase**: Keeps the partner onboarding journey **entirely offline** (via email or WhatsApp). They collect ARN and AMFII-registered name, then perform internal checks before granting access to the partner dashboard.
- **Groww** asks for ARN and only sends OTP for verification only to the mobile number linked with the ARN according to the AMFII database `
- **Neoble & AssetPlus**: Include **ARN validation** directly within their digital onboarding journeys.
- **DhanLAP & Liquify**: The onboarding journey **does not ask for ARN (ARN input field is not there) or mobile verification**, allowing users to enter the partner flow without any kind of validation.
- **Centricity, Wealthy, and AssetPlus**: Offer a digital onboarding journey without any ARN validation (though there is a nudge multiple times to enter valid ARN) but **don’t provide** instant dashboard access after completion of onboarding journey. After completion of onboarding journey they perform internal checks and share access post-validation.
- **Lark:** Offer a digital onboarding journey which asks whether the partner has an ARN or not and basis that the journey forward.
- [*Please find the video recording of the partner onboarding journey 7 competitors here*](https://drive.google.com/drive/folders/1VuaKLMjlgGSxrDViJ7zInH23LihqDk8l?usp=drive_link)

![Lark ](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/Screenshot_2025-10-13_at_2.46.31_PM.png)

Lark 

![Neoble](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/Screenshot_2025-10-13_at_2.49.41_PM.png)

Neoble

![Wealthy](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/Screenshot_2025-10-13_at_2.51.35_PM.png)

Wealthy

![Assetplus](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/Screenshot_2025-10-13_at_2.53.37_PM.png)

Assetplus

![Groww MF dashboard](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/Screenshot_2025-11-05_at_12.22.48_PM.png)

Groww MF dashboard

# **What is the solution?**

---

- **Analysis**
    - From a retrospective analysis of the ARNs and the name match scores between the ARN name and partner entered name in the dashboard, following were the insights -
        
        ![Screenshot 2025-10-13 at 10.12.16 AM.png](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/Screenshot_2025-10-13_at_10.12.16_AM.png)
        
        - Partners with valid ARNs and name match scores >50% generated 7x more business (average applications per partner) than those with invalid ARNs.
        - Within the valid ARN group, higher name match scores correlated strongly with higher business activity (avg. # of applications per partner)
        - To improve sales efficiency, our goal is to ensure that the sales team receives only validated and ranked leads, minimising time spent on filtering and prioritisation
- **Proposed Approach**
    - We will create **lead cohorts** based on ARN validity and name match score, defining tailored journeys for each:
        - **Invalid ARN cohort:**
            - Block users in the partner journey.
            - Prompt them to enter a valid ARN or proceed via the customer journey.
        - **Valid ARN cohort:**
            - Allow users to continue the partner journey.
            - Assign a **confidence score** in LSQ basis the name match score of name entered in the onboarded journey with name present in AMFII database for prioritisation by the sales team.
                - Note -
                    - We will fetch the AMFII registered name of the MFD using the AMFII API
                    - We will calculate the name match score using the Digio fuzzy match API

---

## Partner Empanelment Flow - Volt Platform

### Entry Points

- CTA: "Partner With Us" → "Empanel Now" button on Volt website homepage
- Direct URL access via marketing campaigns

### Authentication Flow

1. **Mobile Verification**
    - Input: 10-digit mobile number
    - System: Sends OTP to mobile
    - Validation: 6-digit OTP entry with 60-second timeout
    - Retry option if OTP expires/fails

### Partner Classification

1. **Partner Type Selection**
    - Drop-down menu with partner categories (MFD pre-selected)
    - Dynamic form fields based on selection
    - Drop down
        - MFD (Mutual Fund Distributor) - ARN
        - Broker - Registration number
        - RIA (Registered Individual Advisor) - Registration number
        - AP (Authorised Person) - Authorised Person Code
        - CA - Membership number
        - Others - [Collect what are they (text input) - DSA/Insurance agent/AMC]
2. **Credentials Validation**
    - **If MFD Selected:**
        - ARN input field with format validation
        - Real-time AMFI database verification (with a back up of AMFII database sheet)
            - Success → Empanelment complete
            - Failure → Error message with correction prompt + option to switch to customer journey → Customer lands on the email verification step
    - **For Non-MFD Partners:**
        - Unique identifier input based on partner type
        - No backend validation required
        - Direct progression to empanelment completion once the user fills the unique code and other details

### Confirmation

- Success screen with partner dashboard access
- Welcome email with login credentials

---

### Edge case and considerations

- A flag to instantly turn off the AMFII validation
- In case we receive the AMFII API failure we will fall back to the ARN present in the AMFII data base sheet

---

### API details & AMFII data

- Digio Fuzzy match API
    - Request
        
        ```jsx
        curl --location 'https://api.digio.in/v3/client/kyc/ ' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Basic QUlUSkxMNlhGNURHVDE3M0dVOEM4MzJDQlE2RzgyUkI6VjUxRUZGSThVQ0hSUkhVMk9FWjVXR1pUMlRLWkNaV1A=' \
        --data '{
            "context": "Name",
            "source": {
                "text": "Soham Sahajwani"
            },
            "target": {
                "text": "PARVESH GARG"
            },
            "confidence": 20,
            "reference_id" : "9cb2814fcbb34f12-b30752117c539a80",
            "unique_request_id": "9cb2814fcbb34f12-b30752117c539a80"
        }'
        ```
        
    - Response
        
        ```jsx
        {
            "matched": true,
            "match_score": 30
        }
        ```
        
- AMFII API
    - Request
        
        ```jsx
        curl --location 'https://www.amfiindia.com/api/distributor-agent?search=313105' \
        --header 'Accept: */*' \
        --header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
        --header 'Connection: keep-alive' \
        --header 'If-None-Match: W/"1ac-pdsVUhDJsuCaufGA6/1+5ueu/YI"' \
        --header 'Referer: https://www.amfiindia.com/locate-distributor' \
        --header 'Sec-Fetch-Dest: empty' \
        --header 'Sec-Fetch-Mode: cors' \
        --header 'Sec-Fetch-Site: same-origin' \
        --header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36' \
        --header 'sec-ch-ua: "Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"' \
        --header 'sec-ch-ua-mobile: ?0' \
        --header 'sec-ch-ua-platform: "macOS"' \
        --header 'Cookie: _ga=GA1.1.243036542.1757581195; _ga_DFEM9FQT5S=GS2.1.s1757584000$o2$g0$t1757584000$j60$l0$h0'
        ```
        
    - Response
        
        ```jsx
        {
            "data": [
                {
                    "id": 71609812,
                    "documentId": "Vq51unyIhIf0GQwgPij9Z",
                    "Sr_No": "865",
                    "ARN": "313105",
                    "ARNHolderName": "SHAILESH RAJU KELA",
                    "Pin": "431005",
                    "City": "AURANGABAD",
                    "LocationCity": null,
                    "ARNValidTill": "21-10-2027",
                    "ARNValidFrom": "09-11-2024",
                    "KYDCompliant": "Y",
                    "OptInForTransactionCharges": null,
                    "EUIN": "E592933",
                    "strOption": "Individual",
                    "SIF_Validity_From": null,
                    "SIF_Validity_to": null
                }
            ],
            "meta": {
                "page": 1,
                "pageSize": 12,
                "total": 1,
                "pageCount": 1
            }
        }
        ```
        
- AMFII database
    
    [AMFI database.xlsx](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/AMFI_database.xlsx)
    
- Admin action - To unblock MFDs with invalid ARN according to AMFII APIs
    - Mobile number will be an input for the admin action
    - For these mobile number the ARN validation will be skipped and partner can tap on the submit button on the partner onboarding journey and complete the onboarding flow

---

### LSQ handling

- If user continues the partner journey
    - Oppotunity activity : Partner Details Updated
        
        
        | Field  | Value  |
        | --- | --- |
        | Notes | Partner Details Updated |
        | Name  |  |
        | Email ID  |  |
        | City  |  |
        | Partner ID  |  |
        | Partner referrals link  |  |
        | Customer referrals link  |  |
        | ARN  |  |
        | Date  |  |
        | Status  |  |
        | Partner type  | {{parter_type}} |
        | Partner name match score  | {{name_match_score}} |
- If user redirects to customer journey from partner journey (incorrect ARN input)
    - Opportunity activity
        
        
        | Field  | Value  |
        | --- | --- |
        | Notes  | Lead type update from partner to customer |
        | Lead type  | User  |
        | Channel  | B2C |

# **Design**

---

https://www.figma.com/design/IFQ0S55xoZpghH2vOfEg4R/Partner-Dashboard-Onboarding?node-id=1-7898&t=loY6eKBGlwm5Lbhw-0

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

1. ARN registered name point - Not requried
2. Volt website changes - Not required 
- Partner type and ARN stitching
    - We won’t take any ARN number if the users select partner type other than MFD
        - Pros - Easier onboarding for different kinds of partners
        - Cons - MFDs might select random partner type to avoid putting ARN

- LSQ changes
    - Event - Bulk (which admin action do they use, what is the sheet format, is there any difference in the handling of event and webinars)
    - Webinar - Bulk
        - Details
        - Pre-filled details (name, phone number, customer/MFD, event name/webinar name)
    - Referral
        - Partner details update (when is it called?)
            - Name match score
            - Confidence score
        - Partner to customer
            - LT - customer
            - Channel - B2C2C
            - Tagging of the customer to that particular MFD
    - Web journey
        - Partner details update
            - Name match score
            - Confidence score
        - Partner to customer
            - LT - customer
            - Channel - B2
    - ARN input not input (LSQ changes)

- **Open point**
    - LSQ changes (confidence)
    - Admin action - To unblock MFDs with invalid ARN according to AMFII APIs
    - Clean Figma
    - Place designs sequentially
    - Continue as borrower
    - Animation button of “Continue as borrower”