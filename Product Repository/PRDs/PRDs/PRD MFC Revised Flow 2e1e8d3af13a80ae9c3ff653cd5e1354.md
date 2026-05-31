# PRD: MFC Revised Flow

: Priyamvada S
Created time: January 7, 2026 1:31 PM
Status: Not started
Last edited: April 14, 2026 1:03 PM

## **Background and Context**

- 
    - Since MFC is going to deprecate the MFC fetch apis and moving to SDK based flow for fetching (concerns from AMFI around fintech platforms accessing investor data freely w/o explicit customer consent.)
    - This change is expected to go live by 31st January
    - Since all Volt channel flows (B2B,B2C & B2B2C) as well as LSP flows will be impacted by this change, figuring out how to tackle this transition to esnure business continuity in the near and long terms is critical

---

## **1. Problem scope**

### In scope

- 
    - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including::
        - Partners who have directly integrated with MFC  fetch flow (eg-Paytm)
        - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter)
        - Partners who are using Volt fetch journey

### Out of scope

- N~~ot covered as part of current scope:~~
    - ~~Loan journey changes ‘post fetch’ for Volt  channels~~
    - ~~B2C website journey changes wrt MFC SD~~K
- While the MFC SDK flow implementation is currently suboptimal from  tech/ UX POV, improving it by working with the MFC team is not feasible given our tight deadline.
    
    ---
    

## **2. Success Criteria**

- 
    - Overall fund fetch SR & first time SR
    - Overall Fetch TAT
    - MFC SDK  flow SR & TAT
    - MFC SDK & RTA flow stability /uptime

## **3. Solution Scope**

### [Detailed solution /Journey](https://whimsical.com/internal-mfc-fetch-updated-flow-copy-FDDhzqEJNzTbNnkUCW73b5)

### 1. Entry point (Volt/LSP channels)

Volt B2C

- Android/IOS app/Partner app: DSP SDK will be triggered on on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen
    
    ![Screenshot 2026-02-08 at 2.51.52 PM.png](PRD%20MFC%20Revised%20Flow/Screenshot_2026-02-08_at_2.51.52_PM.png)
    
- ‘Sign in’ entry point on Website : DSP SDK will be triggered on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen in the web app
- Check eligibility’ entry point on  VoltWebsite: DSP SDK will be triggered on submitting ‘PAN & mob no’ screen & will open in an iframe

Volt B2B2C/B2B partners

- Partners fetching in own UI:The ‘DSP SDK’ flow is triggered from the partner UI
- Partners using Volt UI for fetching: Flows  will be same as that mentioned under ‘B2C’ section

LSP

- The ‘DSP SDK’ flow is triggered from the partner UI

### 2.User journey (DSP SDK)

### *V0 SCOPE*

The VO version of DSP SDK will only be supporting MFC SDK flow (& not RTA flow).

Following would be the E2E user journey for the same:

1. User triggers ‘fetch’ from partner (LSP/Volt)UI.
2. Partner hits DSP /Volt ‘s ‘**Fetch Wrapper’ API** with ,user PAN & Mob no
    1. Required user details:  PAN, Mob no

Note: Every time this API is hit, a new redirection url will be generated

1. DSP checks if MFC server is up →if yes , route to MFC; If no, DSP returns a **technical error** to the partner, and the partner shows a technical error on their UI
2. DSP checks whether **user record exists in MFC**.
    - **If NO →** DSP returns corresponding error  to partner → partner shows error
        - Record might exist but can have others issues like KYC not verified etc, for which also the relevant error needs to be shared by DSP (see ‘error code’ section for details)
    - **If YES →** DSP shares **SDK redirection URL** in Volt /DSP Wrapper API response → user is redirected into DSP SDK
3. User lands on **MFC OTP screen** → enters OTP received on mobile → clicks **Authenticate**.
4. User lands on **AMC Selection** screen → views **AMC-wise portfolio holdings >**User selects desired **AMCs for LAMF** → clicks **Continue to Portfolio Import**.
5. User sees **MFC redirect-back (to DSP)confirmation** screen →DSP inturn redirects user back to Volt/LSP
    1. In case of Volt B2B/B2B2C partners initiating fetch from their own UI: MFC redirects to DSP>DSP redirects to Volt>Volt in turn redirects to partner uI
6. Meanwhile DSP BE  polls MFC to get the fetched portfolio data.Following are the key data points available in the response
    1. PAN, Mob no & Email
    2. Array containing scheme-level portfolio details  including
        - amc code
        - amc Name
        - folio
        - taxStatus
        - modeOfHolding
        - schemeCode
        - schemeName
        - assetType
        - schemeType
        - lienEligibleUnits
        - isDemat
        - decimalUnits
        - isin
        - rtaName
        - kycStatus

7. On getting the data, DSP provides a callback to the partner /can hit the ‘status api’ and shares the fetched portfolio data along with eligible credit limit. Following details need to be shared along:

1. PAN, Mob no, Status, Substatus, Provider, error code (enum) & message,Email id (if available)
    1. ‘Failure’ enums to be same as that of MFC wrapper API enums (pls refer error handling section for exact errors); Enums for additional errors coming in the MFC redirection flow to be shared
2. ‘Eligible funds’ array with scheme details provided by RTA/MFC
3. Ineligible funds array
4. Summary object: Total fund value (if available), Eligbile fund value, Credit limit

Note: 

All errors handling (UI)including pre-OTP & post OTP-trigger will be handled by the LSPs/partner 

### ***V1 SCOPE***

1. User triggers ‘fetch’ from partner (LSP/Volt)UI.
2. Partner hits DSP /Volt ‘s ‘**Fetch Wrapper’ API** with ,user PAN & Mob no
    1. Required user details:  PAN, Mob no

Note: Everytime this API is hit, a new redirection url will be generated

3. DSP BRE <>Partner customisations

DSP then runs a BRE to apply partner-specific customisations/preferences to apply in the DSP SDK journey

*What are the supported customisations (scope)* 

a) ‘MFC/RTA provider’ customisations

| Provider customisation | Comments |
| --- | --- |
| MFC (primary)+ RTA | If RTA is down (can be identified only manually), we need to switch to MFC |
| RTA (primary) +MFC | If MFC is down (can be identified only manually), we need to switch to RTA |
| Only MFC | No manual switch /fallback possible for this |

b) DSP SDK flow customisations (theme, flow)

- UI (V1): Primary & Secondary colors,font,  Dark/Light theme
- ~~BE: Skippable portfolio/credit limit screen (& associated error handling)~~
- ~~Copy customisations~~

*Where are they stored?*

a) MFC/RTA routing

Partner’s provider preference is pre-defined /stored either in DSP config (for LSPs) or in Volt config (for Volt &n Volt partners, passed in the DSP API request).

b) DSP SDK flow customisations (theme, flow)

Partner preference is stored either in DSP config (for LSPs) or in Volt config (for Volt & Volt partners, passed in the DSP API request)).

*How are they activated?*

In order to determine whether to read ‘partner pref’ from  Volt or DSP config, BRE first checks if:

- If “override custom pref” = ‘yes’ in DSP config → pick SDK customisations from DSP API request (derived from Volt config) Else → pick SDK customisations from DSP config
- If “override provider pref” = ‘yes’ in DSP config → pick provider preference from in theDSP init api  (derived from Volt config); Else → pick provider preference from DSP config

4.Core Fetch Flow (RTA/MFC)

*RTA Flow*

If the selected provider is **‘RTA+MFC’**, the flow is:

1.DSP checks **RTA availability:**

- If **at least one RTA server is up**, route via **RTA**
- If **no RTA servers are up:**
    - Check if MFC server is up →if yes , route to MFC; If no, DSP returns corresponding **error** to the partner, and the partner shows a technical error on their UI
        - For Volt B2B/B2B2C partners triggering fetch from their own uI, DSP will pass the error to Volt and Volt in turn passes it to the partner via the Volt wrapper API
1. DSP checks whether the user has an RTA record (by PAN)
    
    **A. Check CAMS**
    
    - **If record exists in CAMS →** DSP returns the **DSP SDK redirection URL** in the DSP Wrapper API response → user is redirected to DSP SDK
        - For Volt B2B/B2B2C partners triggering fetch from their own uI, DSP will pass its url directly to partner
    - **If record does not exist in CAMS →** move to KFin check
    
    **B. Check KFin**
    
    - **If record exists in KFin →** DSP returns the **DSP SDK redirection URL** in the DSP Wrapper API response → user is redirected to DSP SDK and lands directly on ‘KFIN’ otp screen
    - **If record does not exist in KFin →** DSP returns **“No investments found for the PAN”** to the partner → partner shows the error in their UI
        - For Volt B2B/B2B2C partners triggering fetch from their own uI, DSP will pass the error to Volt and Volt in turn passes it to the partner via the Volt wrapper API
2. User redirected to DSP url 
3. User lands on **CAMS OTP** screen (if  applicable)→ enters OTP 
    1. If there is an error  happening post CAMS OTP validation , user not to be shown the error and instead to be taken directly to step 5
4. User sees a ‘Checking for more funds’ loader screen 
5. User lands on **KFIN OTP** screen (if applicable) → enters OTP 
6. User is then redirected back to Volt partner/LSP
7.  DSP  BE receives the ‘fetched fund’ data in  ‘validate api’ response.Following are the data points available in the response
    1. CAMS response
        
        amccode
        
        amcname
        
        closingBalance (ie total available units)
        
        email
        
        folio
        
        isinno
        
        modeofholding
        
        schemecode
        
        schemename
        
        schemetype
        
    2. KFIN response
        
        AmcCode
        
        AssetClass
        
        CostValue
        
        FolioNo
        
        ISIN
        
        InvName
        
        InvPan
        
        Lenderid
        
        MOH
        
        MOHDesc
        
        MarketValue
        
        Mobile
        
        Providerid
        
        RequestID
        
        SchemeCode
        
        SchemeName
        
        Units
        
        usertype
        
8. On getting the data, DSP provides a callback to the partner /can hit the ‘status api’ and shares the fetched portfolio data along with eligible credit limit. Following details need to be shared along:
    1. PAN, Mob no, Status, Substatus, Provider, failure reason,remark,Email id (if available)
        1. Potential values for API status are as follows
        
        | API status | Scenario | Error codes to be shared in API response? | Fetched data sharing |
        | --- | --- | --- | --- |
        | Success | If atleast one of CAMS/KFIN fetch (validate api) is success | Error codes of the failed single  RTA | Yes; If any one RTA succeeds, share the retrieved data in response |
        | Failed | If both CAMS/KIFN faced error (init/validate) | Error codes of both the failed RTA | NA |
        | In progress | If atleast one of CAMS/KFIN has init api success but no terminal staus for 'validate' api | Error code of the failed single RTA, if applicable | Yes; If any one RTA succeeds, share the retrieved data in response |
    2. ‘Eligible funds’ array with scheme details provided by RTA/MFC
    3. ~~Ineligible funds array~~
    4. Summary object: Total eligible fund value, Credit limit
    5. Failure reasons handling: The full list of errors and the corresponding fenxi error code/enum & fenix error message to be shared are [here](https://docs.google.com/spreadsheets/d/12ltk9HJ2vhmbZAi1zAHKCTHtjMwtkVh6KauxF1sh_uM/edit?gid=1600083765#gid=1600083765)

Note: 

All error UI handling—except core-flow cases (e.g., OTP retries or attempt-limit exhausted)—including both pre-OTP and post OTP-trigger scenarios, will be handled by the LSPs/partners.

### OR

*MFC  Flow* 

If the provider preference is **‘Only MFC’**, the flow is:

1. Check if MFC server is up →if yes , route to MFC; If no, DSP returns a **technical error** to the partner, and the partner shows a technical error on their UI
2. DSP checks whether **user record exists in MFC**.
    - **If NO →** DSP returns **“**No investments found for the PAN**”** to partner → partner shows error
    - **If YES →** DSP shares **SDK redirection URL** in DSP Wrapper API response → user is redirected into DSP SDK
3. User lands on **MFC OTP screen** → enters OTP received on mobile → clicks **Authenticate**.
4. User lands on **AMC Selection** screen → views **AMC-wise portfolio holdings >**User selects desired **AMCs for LAMF** → clicks **Continue to Portfolio Import**.
5. User sees **MFC redirect-back confirmation** screen → user is redirected back to DSP →DSP inturn redirects user back to Volt/LSP
    1. In case of Volt B2B/B2B2C partners initiating fetch from their own UI: MFC redirects to DSP>DSP redirects to Volt>Volt inturn redirects to partner uI
6. Meanwhile DSP BE  polls MFC to get the fetched portfolio data.Following are the key data points available in the response
    1. PAN, Mob no & Email
    2. Array containing scheme-level portfolio details  including
        - amc code
        - amc Name
        - folio
        - taxStatus
        - modeOfHolding
        - schemeCode
        - schemeName
        - assetType
        - schemeType
        - lienEligibleUnits
        - isDemat
        - decimalUnits
        - isin
        - rtaName
        - kycStatus

7. On getting the data, DSP provides a callback to the partner /can hit the ‘status api’ and shares the fetched portfolio data along with eligible credit limit. Following details need to be shared along:

1. PAN, Mob no, Status, Substatus, Provider, failure reason,remark,Email id (if available)
    1. ‘Failure reason’ enums to be same as that of MFC wrapper API enums; Enums for additional errors coming in the MFC redirection flow to be shared
    2. Potential values for API status are as follows
2. ‘Eligible funds’ array with scheme details provided by RTA/MFC
3. Ineligible funds array
4. Summary object: Total fund value (if available), Eligbile fund value, Credit limit

Note: All error handling—except core-flow cases (e.g., OTP retries or attempt-limit exhausted)—including both pre-OTP and post OTP-trigger scenarios, will be handled by the LSPs/partners.

---

### 2.User journey (Volt)

Following section describes the ‘fetch’ user journey changes for Volt across: 

- B2C android/IOS  & Web app
    
    [1.Post](http://1.Post) DSP SDK redirection back to Volt asset (app/webapp/website), Volt will display ‘Evaluating your mutual funds’ screen while it is awaiting the fetch status from DSP
    
    [2.I](http://2.In)f the fetch status is success, then Volt will check if the total eligible credit limit>10k.
    
    - **If YES →** Volt proceeds to show the ‘anchor page’ (credit limit)’ >>’Set credit limit’ screen
    - **If No →** Volt proceeds to show the error screen for ineligiblity
    
    3.If fetch status is ‘failed’, then Volt will show the corresponding error screen. Full list of errors to be handled is attached [here](https://docs.google.com/spreadsheets/d/12ltk9HJ2vhmbZAi1zAHKCTHtjMwtkVh6KauxF1sh_uM/edit?gid=1586955728#gid=1586955728)
    

- Volt website
    
    [1.Post](http://1.Post) DSP SDK redirection back to Volt website, Volt will display ‘Evaluating your mutual funds’ screen while it is awaiting the fetch status from DSP
    
    [2.I](http://2.In)f the fetch status is success, then Volt will check if the total eligible credit limit>10k.
    
    - **If YES →** Volt proceeds to show the ‘Available credit limit’ screen
        - ‘Available credit limit’ screen  will carry total eligible credit limit  & its breakup across both RTAs
    - **If No →** Volt proceeds to show the error screen for ineligiblity
    
    3.If fetch status is ‘failed’, then Volt will show the corresponding error screen. Full list of errors to be handled is attached [here](https://docs.google.com/spreadsheets/d/12ltk9HJ2vhmbZAi1zAHKCTHtjMwtkVh6KauxF1sh_uM/edit?gid=1586955728#gid=1586955728)
    

Design:

[https://www.figma.com/design/qKWikWbliBjOYpJ81DF2Pr/MFC-Cas?node-id=18-168&p=f&t=z7gAZTf4MiQPbT6g-0](https://www.figma.com/design/qKWikWbliBjOYpJ81DF2Pr/MFC-Cas?node-id=18-168&p=f&t=z7gAZTf4MiQPbT6g-0)

### Analytics

[FE events](https://docs.google.com/spreadsheets/d/1eZiOG4lnSelVgtZdYDCMJiQ87lxbxNofeB6cGQwzM44/edit?gid=433351868#gid=433351868)

[BE Data](https://docs.google.com/spreadsheets/d/1EnqgWTD-T-GWkGOmydGz4CdNZAfTS40K0XEkBan6ubg/edit?gid=1232653340#gid=1232653340)

Following data to be available in the DB:

---

##