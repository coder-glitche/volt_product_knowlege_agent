# MFC fetch in Volt Journey

: Ranjan kumar Singh
Created time: July 31, 2024 5:59 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

- Allow users to fetch their folio using the MFC API to calculate the eligible credit limit during loan applications, limit increases, and loan renewals.
    - Streamline the process by requiring users to enter only one OTP to fetch the entire folio.
    - This reduces cognitive load, as they currently need to enter two OTPs when fetching or refreshing folios from both CAMS and KFIN.
    - Allow user to continue loan application journey without requiring to fetch again with CAMS and KFIN if user has already fetched folio with MFC on other platform like Volt landing page, partner dashboard, and other B2B platform.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

| Scenarios | Questions |  |
| --- | --- | --- |
| MFC fetch on landing page and user continue on app to select limit | - How to validate PAN, so that we can skip PAN validation
****PAN is used to create lead 
****Name as per PAN is used for KYC
- How lead and borrower account creation will work
- How attribution will work |  |
| How to handle MFC fetch with combination of phone number | - Which number to use to register customer |  |
| We get email id in MFC fetch response | - Which email to choose and how to validate and use as registered email |  |
| If MFC is down | - How we will get to know that MFC is down
- How to switch user to fetch from KFIN and CAMS if MFC is down
- What if MFC and other two RTA are also down |  |
| User fetched with MFC but not able to pledge with MFC | - Switch user to Pledge through CAMS and KFIN
- What if user are not able to pledge with CAMS and KFIN also |  |
| How fetch will work using MFC | - Borrower account is already created after fetching the MFC
- User again fetch on landing page or on any other platform
- Will eligible limit get change for borrower account based on latest MFC fetch on landing page? |  |
| Lender credentials for Fetch and pledge | How it will work in case of switch |  |
| Visibility for Sales and Ops | - Funds fetched from MFC
- Funds linked with different phone
- CAMS and KFIN funds
- Eligible and non eligible Funds
- Lien eligible units for both RTA |  |
| Handle refetch and refresh | - Pledge units not available when user are trying to pledge  |  |
| Credit Limit, portfolio and units selection | How to handle if user want to pledge selected funds or units |  |
| Create a list of platform for which we can integrate MFC fetch | - Flag to decide on which platform MFC fetch journey will be Shown |  |
| Update portfolio of user when they refetch MFD on any platform, Volt website or partner dashboard |  |  |

Data Validation:

| Criteria | Comments |
| --- | --- |
| Data coming in CAS summary and CAS detailed |  |
| Lien eligible units for both RTA | - Check eligible units accuracy 
***Check before and after pledge response |
| Locked and eligible units for ELSS funds |  |
| Funds which are not eligible for pledge [DMAT, child, retirement] |  |
| Available unit against AMC |  |
| Detailed and summary CAS pull with one user consent working or Not | KFIN is Doing UAT on 5 Aug to provide units available for pledge |
| How pledge will work if user fetch MFC from multiple phone number | OTP will be sent on all number to pledge funds? |

## User flow

### **MFC fetch on Volt landing page**

**Fetch and pledge with MFC: [Happy flow]**

User fetched MFC on landing page > User are eligible for loan > User continue loan application > borrower account is created > User verify email > User verify PAN > Unlock credit limit page is shown to user [user can refresh folio, Change phone to fetch folio from MFC] > user continue > Lender is assigned > User  select limit and folio > loan offer > KYC > Lien validation API is called [refresh and select limit flow triggered in case of unit mismatch] > Proceed to MFC pledge or pledge with CAMS/KFIN

**MFC <> CAMS/KFIN Fetch Switch: [Fetch with CAMS/KFIN flag is TRUE and Pledge with MFC is FALSE]**

User fetched MFC on landing page > User are eligible for loan > User continue loan application > borrower account is created > User verify email > User verify PAN > User fetch using cams and KFIN > Unlock credit limit > Lender is assigned > Edit limit > Verify interest and charges > KYC > Lien validate using MFC API [refresh and select limit flow triggered in case of unit mismatch] > Pledge using CAMS/KFIN 

**MFC <> CAMS/KFIN Pledge switch: [Fetch with MFC is TRUE and Pledge with MFC is FALSE]**

ser fetched MFC on landing page > User are eligible for loan > User continue loan application > borrower account is created > User verify email > User verify PAN > User fetch using MFC > Unlock credit limit > Lender is assigned > Edit limit > Verify interest and charges > KYC > Lien validate using MFC API [refresh and select limit flow triggered in case of unit mismatch] > Pledge using CAMS/KFIN 

### MFC fetch on partner dashboard

MFD fetch user folio using MFC > Customer are eligible > MFD click on continue > Borrower account is created > [Journey continue same as Volt journey]

### MFC fetch on Volt Web/Android/iOS app

User sign up using phone > Validate email > validate pan > Fetch using MFC > Credit limit is shown to user > User continue to unlock limit or change phone number to fetch again > Unlock limit > set limit > verify charges > KYC > Validate lien > Pledge using MFC [If Pledge with MFC flag is TRUE]

### MFC fetch on platform[SDK]

Borrower account is created? [Yes] > User verify Email? [Yes/No]>User verify PAN? [Yes/No]> user fetch with MFC > Credit limit is shown to user > User continue to unlock limit or change phone number to fetch again > Unlock limit > set limit > verify charges > KYC > Validate lien > Pledge using MFC [If Pledge with MFC flag is TRUE]

### MFC fetch on platform[Redirection journey]

User fetch MFC > Borrower account do not exists? [No] > Credit limit is shown to user > User are asked to download Volt App > User continue on Volt platform > user verify email > User verify PAN > User unlock the limit > lender is assigned > Set limit > Verify charges > KYC > Pledge using MFC [If Pledge with MFC flag is TRUE]

## Requirements

### 1. Flow Configuration Flags

- **Fetch Flow Flag**:
    - Determine whether to fetch data using MFC or CAMS/KFIN once borrower account is created.
    - If the user has already fetched their folio with MFC and then come to the app, the MFC limit will be displayed. The user can choose to refresh the folio with MFC or proceed to unlock the limit, unless the "Fetch with CAMS/KFIN" flag is enabled.
        - If the "Fetch with CAMS/KFIN" flag is overridden, the user must fetch the folio with CAMS/KFIN. In this scenario, the MFC portfolio will still be retained.
- **Pledge Flow Flag**:
    - Determine whether to pledge using MFC or CAMS/KFIN.

### 2. Platform-Specific Fetch/Pledge Configurations

- **Platform-Based Flag Settings**:
    - Configuration should allow setting specific fetch/pledge flows for different platforms.
    - **Example**: For the Jupiter platform, if the fetch flag is set to "MFC" and the pledge flag is set to "CAMS/KFIN," all Jupiter users will fetch folios using MFC and pledge them using CAMS/KFIN.

### 3. Portfolio Management

- **MFC Portfolio Persistence**:
    - Ensure that portfolios fetched using MFC are retained if the fetch process is switched from MFC to CAMS/KFIN.
- **Portfolio Refresh/Update**:
    - Automatically refresh or update the portfolio if a borrower account is created and the user refetches the portfolio via MFC on the Volt Website, Partner Dashboard, or any associated platform.

### 4. Automated Switching via BRE

- **Business Rule Engine (BRE) Switching**:
    - Implement BRE to automatically switch between MFC and CAMS/KFIN for both fetching and pledging, depending on service availability.
    - **Scenario**: The BRE should automatically switch to CAMS/KFIN if MFC is down and vice versa.

### 5. Step ID Assignments

- Assign distinct Step IDs for the following processes:
    - MFC Fetch
    - CAMS/KFIN Fetch
    - MFC Pledge
    - CAMS/KFIN Pledge

---

# **Design requirement**

### When user has not fetched the MFC and user starting loan application journey on Volt app:

- Fetch with MFC on loan application journey, line enhancement and renewal flow
    - Check credit limit using PAN and phone
        - Single consent to fetch MFC detailed and summary API [Lien eligible units are not coming in summary API]
    - Fetch success page if user are eligible for loan [limit >25K]
        - Option to refetch folio [If multiple phone number linked with folio for same PAN]
    - Error handling if folio not found with given phone and PAN
        - Option to change Phone and PAN to refetch
    - Option to refresh the folio with MFC
    - Option to refresh the folio with CAMS/KFIN in case of fetch flag override

### When MFC is fetched and then user are coming on Volt loan application journey:

- Show home page with Eligible credit limit [This page already exists]
- Unlock credit limit page with folio refresh option with MFC
    - Data to show on Unlock credit limit page:
        - Fetched Folio total limit
        - Eligible limit
        - Break up of cams and KFIN folio value [This is required when user need to pledge folio with CAMS and KFIN]
    - Show error message to user if user are not eligible for loan

### Fetch with MFC in increase limit and loan renewal flow:

- Fetch experience for user will be same as fresh loan application journey in increase limit and loan renewal flow.

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

- Understand jupiter and phonepe journey
- Journey Scope: Phonepe, jupiter, Partner dashbaord, Volt MFC journey

Expection:

- Architecture discussion with Tech -> PRD
- How refetch or refresh will work
- How we are going to decide for whcih platform will work and for not work - Flag for Platform
- What if MFC is down - Flag
- Portfolio to persist for MFC in case of Switch
- Grid: Data is not coming [Lien eligible data is inaccurate in CAS summary] - check mail frwd by Lalit
- Available unit against AMC is not coming
- KFIN AMC [Locked and lien marked is not included] - Follow up LAlit
- Call both API CAS details and CAS summary
- Consent with KFIN and CAMS to use both API
- If MFC fetch dosent work - check for which platform we can use
- Connect with saksham to unblock

- What if MFC is down
- Different step id for MFC fetch
- Sales use CAS detailed doc, → Two MFC pull, cas summary and details with one invester consent