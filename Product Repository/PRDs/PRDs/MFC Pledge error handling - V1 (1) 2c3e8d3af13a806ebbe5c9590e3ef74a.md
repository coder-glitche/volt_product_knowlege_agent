# MFC Pledge error handling - V1 (1)

: Devansh Kar
Created time: December 8, 2025 7:35 AM
Status: In progress
Last edited: May 4, 2026 5:20 PM

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
- This might not be the full list of errors we are handling. As we dial up and get new errors, we will handle those in the upcoming versions of error handling.

---

# Data

[https://docs.google.com/spreadsheets/d/1rUVHTYWTmSb6B9jVbLNBZ4Deoihq7s50_JO4T0Gp0tU/edit?gid=1170148963#gid=1170148963](https://docs.google.com/spreadsheets/d/1rUVHTYWTmSb6B9jVbLNBZ4Deoihq7s50_JO4T0Gp0tU/edit?gid=1170148963#gid=1170148963)

---

# **What is the solution?**

## User flow

[https://whimsical.com/mfc-fetch-copy-AoKatQpVDeRbFSjr3DqtME](https://whimsical.com/mfc-fetch-copy-AoKatQpVDeRbFSjr3DqtME)

## Requirements

1. **Hierarchy/ Priority order logic for error handling:**
- When a user enters the pledge step and clicks on Continue, Validate Lien API will be called first every time.
- Sample response body of Validate Lien API is attached below:

```jsx
{
	"reqId": "1315718962",
	"pan": "AYFPP3832Q",
	"pekrn": "",
	"mobile": "9998466665",
	"email": "",
	"clientId": "dspfinance",
	"lenderCode": "mfc_dspfinance",
	"pending": [],
	"errors": [
		{ 
			"rtaName": "CAMS",
			"lienRefNo": "",
			"techMessage": "",
			"message": "We are unable to process your request.Please try again later.",
			"code": "400",
			"schemeDetails": [
				{
					"amc": "G",
					"folio": "5649054",
					"schemeName": "",
					"isin": "INF194KB1AJ8",
					"itemNo": "",
					"lienUnits": "20.99",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "40636189",
					"schemeName": "",
					"isin": "INF109K01654",
					"itemNo": "",
					"lienUnits": "1638.47",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "G",
					"folio": "5649058",
					"schemeName": "",
					"isin": "INF194K01342",
					"itemNo": "",
					"lienUnits": "6.76",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "B",
					"folio": "1041735323",
					"schemeName": "",
					"isin": "INF209K01AJ8",
					"itemNo": "",
					"lienUnits": "0.5",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "L",
					"folio": "26310043",
					"schemeName": "",
					"isin": "INF200K01T28",
					"itemNo": "",
					"lienUnits": "210.13",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109KA14I5",
					"itemNo": "",
					"lienUnits": "3046.23",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "G",
					"folio": "5649058",
					"schemeName": "",
					"isin": "INF194KB1AJ8",
					"itemNo": "",
					"lienUnits": "106.06",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109K01852",
					"itemNo": "",
					"lienUnits": "78.79",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109KC1Q80",
					"itemNo": "",
					"lienUnits": "10461.08",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109K01837",
					"itemNo": "",
					"lienUnits": "277.58",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "L",
					"folio": "29435212",
					"schemeName": "",
					"isin": "INF200KA15E8",
					"itemNo": "",
					"lienUnits": "6616.35",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109K01BI0",
					"itemNo": "",
					"lienUnits": "123.99",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "L",
					"folio": "29283680",
					"schemeName": "",
					"isin": "INF200KA15E8",
					"itemNo": "",
					"lienUnits": "1747.69",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109KC1RE6",
					"itemNo": "",
					"lienUnits": "482.22",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109K01BL4",
					"itemNo": "",
					"lienUnits": "25.4",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "L",
					"folio": "28966975",
					"schemeName": "",
					"isin": "INF200KA15E8",
					"itemNo": "",
					"lienUnits": "510.33",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "15069429",
					"schemeName": "",
					"isin": "INF109K01AF8",
					"itemNo": "",
					"lienUnits": "10.29",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				},
				{
					"amc": "P",
					"folio": "37266916",
					"schemeName": "",
					"isin": "INF109K01BL4",
					"itemNo": "",
					"lienUnits": "9.58",
					"remarks": "Mobile number is not linked to the folio(s) of this PAN."
				}
			]
		}
	],
	"success": [
		{
			"rtaName": "KFIN",
			"lienRefNo": "6980959",
			"schemeDetails": [
				{
					"amc": "108",
					"folio": "577337029915",
					"schemeName": "UTI Flexi Cap Fund Regular Plan",
					"isin": "INF789F01513",
					"itemNo": "",
					"lienUnits": "113.71"
				}
			]
		}
	],
	"validateId": "1315718962"
}
```

- Basis on the response received from the API, the backend will trigger the error card and handling action as per the logic in BE config.
- The hierarchy/ priority order which needs to be followed for reading the response errors and trigger the corresponding next actions is mentioned as below:
    - The “remarks” keys for every fund under “schemedetails” subarray of “error” array is read first. The different **cases** and corresponding actions post reading “remarks” are:
        
        **Case-1:**
        
        - If “remarks” parameter have got one or more than one non-null values, and
            - **Case 1.1:** All the non-null “remarks” values belong to the list of fund remarks table mentioned below, then
                - enum is mapped to corresponding error remarks as per enums list.
                    - **Case 1.1.1:** If all enums are of same category, then corresponding header, messaging and CTA with actions are triggered as per config rules defined in exhaustive grid below.
                    - **Case 1.1.2:** If there is a mismatch of enum categories, then generic header and messaging is shown with **“Contact us”** CTA.
            - **Case 1.2:** If at least one of the “remarks” values of all the non-null remarks doesn’t belong to the list of fund remarks table mentioned below, then generic header and messaging is shown with **“Contact Us”** CTA.
        
        **Case-2:**
        
        - If all the “remarks” parameter has null values, then “message” parameter (Failure_Reasons) at an RTA level are checked
            - **Case 2.1:** All the “failure_reason”/ “message” belongs to the list of failure_reason in the table mentioned, then
                - enum is mapped to corresponding failure_reasons as per enums list and corresponding header, messaging, CTA with action is triggered as per config rules defined in the exhaustive grid below.
            - **Case 2.2:** If at least one of the “failure_reason” values doesn’t belong to the list of failure_reason in table mentioned below or value is **null**, then generic header and messaging is shown with **“Contact Us”** CTA.
            
    
    **Exhaustive table: (Subject to - Limit >10K available for pledging)**
    

|  **Error Details** |  |  |  |  |  |  |  | **Handling Details** |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Cases** | **RTA** | **Error Type 1** | **Error Type 2** | **Failure  reasons (RTA message)** | **Fund error remarks** | **Reason** | **enum** | **Handling** | **CTA names** | **Header** | **Messaging** | **Table (with updated details) required in UI?** |
| Case 1 | CAMS | Fund level |  |  | Scheme is not mapped to your client id. | Scheme is not in the approved list of MFC dashboard/id of DSP | SCHEME_NOT_MAPPED | H1 : A2 | Retry Pledging | Hd1: Looks like your fund details are not updated with MF Central | M1: We recommend pledging directly with CAMS and KFIN. | No |
| Case 2 | KFIN | Fund level |  |  | One of the Folio is Under Stop Payments | AMC has blocked the folio from transaction for any reason | STOP_PAYMENTS_FOLIO | H2: A1 | Pledge Remaining Funds | Hd2: AMC has blocked certain funds for pledging | M2: You can pledge remaining funds, your credit limit will change accordingly. Don’t worry you can enhance it later | Yes |
| Case 3 | KFIN | Fund level |  |  | DMAT Flag is not valid | Funds are in demat | INVALID_DMAT_FLAG | H2: A1 | Pledge Remaining Funds | Hd3: Some of your funds are Demat | M2: You can pledge remaining funds, your credit limit will change accordingly. Don’t worry you can enhance it later | Yes |
| Case 4 | CAMS+KFIN | Fund level | Lien mismatch error |  | CAMS:
a) Pass lien units less than or equal to available balance.
b) There is no available balance to the mark the lien in the given folio and scheme.
KFIN:
a) Free Units are less than Lien Units
b) No free units avaliable
c) Available units 0 are less than requested pledge units 380.5
 | Lien eligible units are 0/ less than requested units | LIEN_UNITS_MISMATCH | H3: A3 | Refetch Portfolio | Hd4: Requested fund units are not available for pledging | M3: Please refetch portfolio directly from CAMS & KFIN to get latest details and retry pledging | Yes (after refetch) |
| Case 5 | CAMS+KFIN | Fund level | Contact details mismatch |  | CAMS: Mobile number is not linked to the folio(s) of this PAN.

KFIN: Investor Information is not valid | Mobile number for particular folios is different from the one passed in request body. | CONTACT_INFO_MISMATCH | H2: A1 | Pledge remaining funds | Hd5: Different contact information found for some funds | M5- You can pledge remaining funds. Don’t worry you can enhance it later by updating contact details with AMC | Yes |
| Case 6 | CAMS+KFIN | Fund level | PAN folio mismtach |  | CAMS: Given folio not match with given PAN.

KFIN: Invalid Folio Details, Data not found | Folios are not under the given PAN | PAN_FOLIO_MISMATCH | H2: A1 | Pledge remaining funds | Hd6: PAN is not linked to some funds | M2: You can pledge remaining funds, your credit limit will change accordingly. Don’t worry you can enhance it later | Yes |
| Case 7 |  | RTA level |  | CAMS: We're unable to process your request.Pls try again later |  |  | CAMS_PLEDGE_ISSUE | H2: A1 | Pledge remaining funds | Hd7: ~~Facing issue while processing your pledge request for some funds~~

- Unable to pledge a few funds due to technical issues with MF Central | M2: You can pledge remaining funds, your credit limit will change accordingly. Don’t worry you can enhance it later | Yes |
| Case 8 |  | RTA level |  | KFIN: Null |  |  | KFIN_NO_INFO | H2: A1 | Pledge remaining funds | Hd7: ~~Facing issue while processing your pledge request for some funds~~

Unable to pledge a few funds due to technical issues with MF Central | M2: You can pledge remaining funds, your credit limit will change accordingly. Don’t worry you can enhance it later | Yes |
| Case 9 |  | RTA level |  | Some folios not found in trigger OTP response |  |  | FOLIO_OTP_RESPONSE_ERROR | H3: A3 | Refetch Portfolio | Hd8: F~~acing issue while processing your pledge request for some funds~~
Few of your funds are not available with MF Central for pledging | M3: Please refetch portfolio directly from CAMS & KFIN to get latest details and retry pledging | Yes (after refetch) |
| Case 10 |  | RTA level |  | KFIN: Error occurred while validating PAN or KYC. Try again later. |  |  | KFIN_KYC_PAN_ERROR | H2: A1 | Pledge remaining funds | Hd7: ~~Facing issue while processing your pledge request for some funds~~

Unable to pledge a few funds due to technical issues with MF Central | M2: You can continue pledging with remaining funds, your credit limit will change accordingly. Don’t worry you can enhance it later | Yes |
| Case 11 |  | RTA level |  | KFIN: Invalid Folios |  |  | KFIN_INVALID_FOLIOS | H3: A3 | Refetch Portfolio | Hd8: Few of your funds are not available with MF Central for pledging | M3: Please refetch portfolio directly from CAMS & KFIN to get latest details and retry pledging | Yes (after refetch) |
| Case 12 |  | RTA level |  | CAMS: We are unable to process your request.Please try again later., KFIN: Invalid Folios |  |  | CAMS_KFIN_PLEDGE_ISSUE | H3: A3 | Refetch Portfolio | Hd8: Few of your funds are not available with MF Central for pledging | M3: Please refetch portfolio directly from CAMS & KFIN to get latest details and retry pledging | Yes (after refetch) |
| Case 13 |  | RTA/ Fund level |  | ^ Any other error apart from above errors/ NULL | ^ Any other error apart from above errors |  | OTHER_ERRORs | H4:A4 (Generic handling) | Contact Support | Hd9: Unable to pledge a few funds due to technical issues with MF Central | M4: Please contact support to know more | No |

**Handling types:**

|  | Pledge |  |  |
| --- | --- | --- | --- |
| Fetch |  | MFC=1 | RTA=1 |
|  | MFC/RTA=0 | A1(Remove funds & Re-pledge via MFC) | A2 (Only RTA repledge) |
|  | RTA=1 | A3(Fetch via RTA & MFC Pledge) [Contextual RTA fetch basis on funds rta mapping] |  |

 

Priority of errors

**Updated Credit Limit:**

- **H2:A1-** After the funds are removed, BE will keep the context of earlier requested credit limit and calculate new credit limit post removing funds.
    - The updated credit limit is reflected in a table in the error card with old and new credit limit, if credit limit > 0
    - The distribution of updated credit limit with final total portfolio value, eligible portfolio value and non-eligible portfolio value is calculated from BE and sent to FE which a user can read on clicking the “info” icon.
    - **Limit check handling errors**
    1. Pledge remaining funds limit handling
    
    **0 credit limit**: When pledgable credit limit calculated after removing funds are 0, then instead of error card as per enum error card with the following components need to be shown:
    
    **Header** - ~~You don’t have any units to pledge as some of your funds are facing issues.~~ We are unable to process your request as funds are not available for pledging
    
    **Messaging**: Please contact support to know more
    
    **CTA**: Contact Us
    
    b. **10k credit limit**: When pledgable credit limit calculated after removing funds > 0 and <10,000, then instead of error card as per enum error card with the following components need to be shown:
    
    **Header:** We are unable to process your request as funds are not available for pledging
    
    **Messaging:** A minimum credit limit of Rs. 10000 is required to continue with this loan application.
    
    CTA: Contact Us
    
    - When credit limit after removing funds = 0
- **H3:A3:** On refetching portfolio, the updated limit is calculated in the backend and reflected in a table in a bottom sheet in the FE.
- Fetch failure error: If fetch is failed an enum: FETCH_FAILED is mapped and error card is shown instead.
- **Limit check handling errors:** Cases Same as handling same as mentioned in first error handling case.

**Generic messages (Null error, errors not in list, mismatch of errors):**

The below details are passed when null error remarks/ message is received, or any unknown error not mentioned in the table list above or mismatch of error happens.

**Header** - Unable to pledge a few funds due to technical issues with MF Central

**Messaging**: Please contact support to know more

**CTA**: Contact Us

**User Flow**

**A) Single error type handling - Fund level error remarks are received:**

**Error Handling type 1:** Reattempt pledging by switching over to RTA (CAMS and KFin Pledge)

**Error type(s) addressed**: 

**a) Fund level remarks:** CAMS - Scheme is not mapped to your client id. — MFC_ERR_01

b) Request level (Failure reason without fund remarks): CAMS: We're unable to process your request.Pls try again later

- The “Validate Lien” API [Init] is called as soon as the user enters the Pledge step after user clicking on continue. The corresponding error message will be shown upfront to the user in the error card with CTA to “Retry pledging”
- On clicking on “Retry pledging”, BE switches the pledge provider from MFC to RTA and user can complete pledging with 2 OTPs.
- In case, error still persists due to CAMS/ KFin, pledging the error will be handled as it is being handled currently for RTAs. [Something went wrong with Refetch and repledge flow]. (4OTPs)
- If the limit changes, the new updated limit is shown to the user.

**Error Handling type 2:** Remove funds and reattempt pledging via MFC

**Error type(s) addressed**: Fund level: 

KFin - One of the Folio is Under Stop Payments 

KFin - DMAT Flag is not valid — MFC_ERR_03

Type 1 - **Contact details mismatch against funds/ folio**

Fund level: 

1. CAMS: Mobile number is not linked to the folio(s) of this PAN. — MFC_ERR_05
2. KFin: Investor Information is not valid. — MFC_ERR_05

Type 2 - **PAN folio mismatch**

Fund level:

- CAMS: Given folio not match with given PAN. — MFC_ERR_06
- KFin: Invalid Folio Details, Data not found — MFC_ERR_06
- The “Validate Lien” API [Init] is called as soon as the user enters the Pledge step after user clicking on continue. The corresponding error message will be shown upfront to the user in the error card with CTA to “Pledge with remaining funds”.
- In the above error card, FE would consume and show the — old limit and the new updated limit calculated from backend after removing the funds.
- On clicking “Pledge with remaining funds”, again Init (Validate lien) will be called with MFC as provider and 1 MFC pledge OTP will be triggered completing the pledge process.

**Error Handling type 3:** Refetch via CAMS/ KFin (RTA) and repledge via MFC

**Error type(s) addressed**: 

1. Fund level: CAMS + KFin Lien mismatch error — MFC_ERR_04
2. Request level errors

- The “Validate Lien” API [Init] is called as soon as the user enters the Pledge step after clicking on continue. The corresponding error message will be shown upfront to the user in the error card with CTA to “Refetch portfolio”.
- Fetching will be done either only from CAMS or KFin or both CAMS and KFin based on the funds of the specific RTA against which error(s) is/ are incurred. (1 or 2 OTPs)
- After refetching portfolio, BE would calculate the new limit and FE would show the old as well as the updated limit via a bottom sheet with CTA to “Continue pledging”
- When user continues, pledging will happen via MFC as provider. (1 OTP).
- If still any kind of error is encountered irrespective of the type on calling “Validate lien” at this step - provider will be switched to RTA for pledging with showing the user with corresponding error message received at fund level or generic error if no fund level/ known request level error is received from MFC.

**~~Error Handling type 4:** Giving both the options to user as action -~~ 

1. ~~Remove funds and reattempt pledging via MFC (Primary CTA)~~
2. ~~Refetch via CAMS and KFin and repledge via MFC~~
- ~~The “Validate Lien” API [Init] is called as soon as the user enters the Pledge step before clicking on continue. The corresponding error message will be shown upfront to the user in the error card with 2 CTAs:~~
    - ~~Primary CTA: “Pledge with remaining funds”~~
    - ~~Secondary CTA: Updated contact details? “Refetch portfolio”~~
- ~~FE would consume and render the old and new calculated limit after BE sends the new calculated limit after removing the funds.~~
- ~~If user clicks on “Pledge with remaining funds”, again Init (Validate lien) will be called with MFC as provider and 1 MFC pledge OTP will be triggered completing the pledge process.~~
- ~~If user clicks on 2nd CTA “Refetch portfolio”, then CAMS and KFin fetch will happen and new calculated limit will be shown to the user from the BE (conditional that old limit and new limit are different) with option to continue pledge.~~
    - ~~Happy scenario: MFC pledge will be success after OTP triggers.~~
    - ~~If same error still persists, then the whole flow will start again with same error card which the flow started with.~~

- **Amplittude events**
    - BE event
        - MF_PLEDGE_INIT
            - result: true/false
            - provider: MFC
            - rta: CAMS/Karvy
            - rta_error_type: enum passed.
        - MF_PLEDGE_OTP_RTA
            - result: true/false
            - rta: CAMS/Karvy
            - rta_error_type: enum passed

**AppSmith Requirements:**

- The latest pledgingremarks reasons are populated for error funds under pledged funds
- Failure reason at a request level is populated in case there is no fund level remarks

~~MUTLIPLE ERRORHANDLING~~

~~SAME TYPE MULTIPLE ERROR~~

~~DIFFERENT. TYPE MULTIPLE ERROR~~

---

# **Design**

[https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=4-13&p=f&t=kdJe8c9ZBfMQbHA4-0](https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=4-13&p=f&t=kdJe8c9ZBfMQbHA4-0)

---

# **Analytics**

---

# **Reference**

Error and corresponding handling sheet: https://docs.google.com/spreadsheets/d/1dXBrV4Oy1w14up_SzzkOMyML_2LQ8bkw1IaLqBv2LLQ/edit?gid=0#gid=0

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