# Pledge error handling

: Ranjan kumar Singh
Created time: July 22, 2024 3:11 PM
Status: In progress
Last edited: February 19, 2026 7:14 PM
Owner: Lalit Bihani

# **What problem are we solving?**

Users are encountering difficulties when pledging folios due to the following error encountered during validation and authentication for CAMS and KFIN:

### User are getting below mentioned error at time of pledging with CAMS and KFIN

Note: Errors listed below are not exhaustive; users may encounter additional error types depending on specific cases from CAMS and KFIN.

Pledge error analysis DOC: [https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342)

- CAMS validation error

| RTA response | **count** |
| --- | --- |
| SUCCESS | 20058 |
| Lien Unit is greater than available Units | 6875 |
| Given Folio not match with given pan. | 459 |
| Given Mobile not match with given folio. | 295 |
| Given folio is invalid due to invalid mobile and email. | 114 |
- CAMS Auth error

| RTA response | **count** |
| --- | --- |
| Lien marked successfully. | 14600 |
| Invalid OTP. | 922 |
| FAILURE | 222 |
| Mark Unit is greater than available Units | 147 |
| Already lien marked against this pan  for this lien ref no | 100 |
| SUCCESS | 54 |
| Invalid OTP attempt maximum reached. | 36 |
| schemedetails parameter is missing in the request. | 26 |
| OTP Expired please regenerate again. | 12 |
| Invalid Reqrefno | 2 |
| Invalid otp value | 1 |
- KFIN validation error

| RTA response | **Count** |
| --- | --- |
| Success | 12899 |
| RequestID Cannot Process as Units are Not Available | 8191 |
| Request not Allowed as one of the Fund is not valid | 1403 |
| KYCStatus not verified | 950 |
| fatca not verified | 300 |
| Request not Allowed as one of the folio not belongs to the given Invpan | 259 |
| Data Doesnot Exists related to Mobile Number | 148 |
| Request not Allowed as one of the  folio is Under Cooling Period | 129 |
| PAN-aadhar seeding not completed | 84 |
| Request not Allowed as one of the folio is NRI | 59 |
| Request not Allowed as one of the folio is Under DEMAT | 57 |
| SEBI Debarred PAN are restricted for Lien Marking | 20 |
| Problem occured while saving | 19 |
| Please Enter valid LenderID | 12 |
|  | 9 |
| The request is currently in the process. | 4 |
| Please Enter valid ProviderID | 2 |
- KFIN Auth error

| RTA response | **count** |
| --- | --- |
| Success | 11703 |
| Invalid OTP Related to RequestID | 661 |
| Request Already Exists | 18 |
| Problem occured while saving | 4 |

---

# **How do we measure success?**

- Reduction in drop-offs at the pledge step due to errors.
- Decrease in customer support queries related to pledge errors.
- Lesser escalations/social/public feedback related to pledge errors.
- Improved conversion rate of successful pledge completions.
    - Higher auth success rates
    - Higher validation success rates
- Shorter resolution time for pledge-related errors.
- Fewer repeated attempts by users to complete the pledge.
- Reduced sanction TAT and disbursement TAT.

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

1. ~~Nudge user to refresh portfolio with both RTA when user lands on pledge landing page~~
    1. ~~Check last fetch date for both RTA, if current date and fetch date is greater then 72 hours.~~
        1. ~~Show notification to user saying that “Your portfolios are outdated, data may be inaccurate” with Refresh CTA~~
        2. ~~If user choose to refresh the folio, take user to fetch folio with both the RTA show updated limit and allow to edit limit.~~
            1. ~~Handle error if selected DP is less then 25K.~~
            2. ~~Latest fetched data to store along with fetch date and expiry for both RTA~~
        3. ~~If user do not choose to refresh folio, allow user to continue to pledge~~
2. Handle validation and Auth error received from CAMS and KFIN.
    1. Logic to decide which RTA to pledge first:
        1. RTA with Higher DP 
    2. Logic to decide which RTA to refresh if user encounter error with 1 RTA
        1. If user encounter error with 1st RTA, we need to check the latest last fetch date of the 2nd RTA or check if 2nd RTA is RTA fetch or MFC fetch
            1. If 2nd RTA is MFC fetch, then user should fetch both the RTA to avoid the pledge error 
            2. If 2nd RTA is RTA fetch and current date & fetch date is greater then 24 hours [Configurable from BE] than user should fetch both RTA
                1. Refer flow chart for more details: https://www.figma.com/board/eOSD0vbZEK2UcevWndsNm9/Pledge-error-handling?node-id=155-2278&t=mj4LQTv4b0b4Q7Fp-4
    3. We need to show error message to user based on error message we get from CAMS and KFIN and nudge user to take action based on error message.
        1. Error message displayed to the user and user action required on the UI should be dynamically provided by the backend based on the error message.
        2. BE should pass the Next step or action items for user to FE based on the error received. 
            1. Example: Let’s say user are facing KYC not verified at time of pledging and error count is >1 then BE should instruct FE that ask user to try pledging with other RTA if Available  DP is ≥25k
        3. BE should send folios to FE for which pledging was success and failed with error message received against each folio.
        4. We need to provide visibility to RM/ops/sales on service dashboard 
            1. Fetch response of both RTA [including error message]
            2. Pledge request and response including outcome of both RTA [Success and failure with reason] 
    4. If user are required to refresh the portfolio, ask user to refresh portfolio and fetch the latest folio and proceed for pledging. 
        1. We need to prompt user to refresh the folio specifically for the RTA for which they are encountering an error.
        2. Logic to refresh the portfolio as mentioned in 2.b
        3. Save latest fetched portfolio and its details and delete older one. [BE]
    5. Once portfolio is refreshed and limit is updated then show updated credit limit to user.
        1. Allow user to edit limit or allow user to continue for pledging.
            1. Handle error if DP selected is less then 25K at time of edit limit
        2. Handle cases when user has already pledged funds with one RTA and later refresh folio linked to other RTA and become ineligible for loan.
            1. To avoid this scenario, we are asking user to first pledge with RTA which has the highest DP
            2. If folio with 1 RTA is already pledged, we will give higher sanction limit to user, inform user about the margin pledge and allow user to proceed with loan application.
    6. If user encounter error at the time of fetch (refresh folio) the handling of fetch error has to be done as per current implementation.
        1. If user encountered fetch error with 1st RTA 
            1. Allow user to pledge RTA 2 and option to contact support
        2. If user encountered fetch error with both RTA
            1. Option to contact support
        3. If user has pledged with 1 RTA and getting fetch error with 2nd RTA
            1. Allow user to skip and continue to next step and option to contact support
            2. Flag like CAMS pledged, CAMS partially pledged need to maintain
    7. Logic to set sanction limit
        1. Sanction limit = DP selected (if not overridden): DP calculated based on the selected folio for pledging [DP selected can’t be less then 25K]
    8. Logic to show selected credit limit on pledge screen
        1. When user lands on pledge landing page for first time
            1. Show selected credit limit which user selected at set limit step
        2. When user refresh the folio
            1. If new limit after refresh is greater then previously selected limit then selected credit limit amount will be previously selected
                1. User can select “unselected funds” to get the higher limit [DP] by clicking on Edit button on pledge landing page
                2. We should show “Available limit” on pledge screen if new limit is greater then selected limit so that user can take inform decision. [Nudge user to select higher limit] 
            2. If new limit amount is less then previously selected then selected credit limit will be new limit
        3. Note: Need to store the Amount based on the last selected limit.
        4. If selected CL is less then 25K and SL is ≥25k then allow user to proceed with pledge [SL override case].
        
3. Handle drop-off cases: https://docs.google.com/spreadsheets/d/133xQB7T1p3tKJLXHAR1hqiR2G0RfmDj1psfhq4MhHrk/edit?usp=sharing

<aside>
💡

For now, we will not allow customers to change or fetch funds using a different PAN due to compliance & risk considerations

</aside>

### Error handling on UI based on error message received from CAMS and KFIN

### CAMS validation [INIT API] error cases

| RTA response | **count** | **Comment** | **Next step** | RCA Doc | Heading | Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SUCCESS | 20058 |  | NA |  |  |  |  |
| Lien Unit is greater than available Units | 6875 | Unit mismatch | Ask user to refresh folio |  | Your portfolio details are outdated! | Refresh portfolio to get latest mutual fund portfolios and retry pledging. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |
| Given Folio not match with given pan. | 459 | Wrong folio or PAN sent in request | Internal bug, Tech need to provide RCA and resolution | [https://docs.google.com/document/d/1nB1N7W6FzPTCMjlzg1weagR_5qp1FiMc3RCnqae0G14/edit?usp=sharing](https://docs.google.com/document/d/1nB1N7W6FzPTCMjlzg1weagR_5qp1FiMc3RCnqae0G14/edit?usp=sharing) | Given PAN EXBPS7155E is not linked to some of the selected portfolios | Refresh portfolio to get portfolio linked to the PAN EXBPS7155E and retry pledging. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |
| Given Mobile not match with given folio. | 295 | Wrong folio or mobile sent in request | Internal bug, Tech need to provide RCA and resolution | [https://docs.google.com/document/d/10dUXoI6NBD54DXQ1hLi-cCYU0YwPpJzOZOzfFLSzozs/edit?usp=sharing](https://docs.google.com/document/d/10dUXoI6NBD54DXQ1hLi-cCYU0YwPpJzOZOzfFLSzozs/edit?usp=sharing) | Given Mobile 7980565882 is not linked with all of the portfolios | Refresh portfolio to get mutual fund portfolios linked to the mobile 7980565882 and retry pledging. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |
| Given folio is invalid due to invalid mobile and email. | 114 | Wrong folio or mobile sent in request | Internal bug, Tech need to provide RCA and resolution - Resolved | This is resolved in May 2024 | Given Mobile 7980565882 is not linked with all of the portfolios | Refresh portfolio to get mutual fund portfolios linked to the mobile 7980565882 and retry pledging. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |
| Default error |  | Any other error which are not handled |  |  | Error occurred while validating your portfolio with {{RTA}} | Refresh portfolio and retry pledging. If the issue persists, reach out to support for assistance. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |

### CAMS Auth[OTP verification API] error cases

| RTA response | **count** | **Comment** | **Next step** | RCA DOc | Heading | Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lien marked successfully. | 14600 |  | Already handled |  |  |  |  |
| Invalid OTP. | 922 |  | Already handled |  |  |  |  |
| FAILURE | 222 | - We are not getting exact failure reason: Issue at CAMS end, This is happening for ICICI funds- Error at folio level: KYC not verified with AMC [CAMS to answer why this is coming at time of OTP verification] | CAMS needs to share RCA |  | **Case 1: Partial pledging**

Heading: {{pledgedAmount}} unlocked successfully

—————————
**Case 2: Pledging failed for all portfolio**

Heading: Error occurred while pledging your portfolio with CAMS | **Case 1: Partial pledging**

Sub-text: Partial funds were pledged as some portfolios were ineligible. You can increase your limit by pledging additional funds later.

————————
**Case 2: Pledging failed for all portfolio**

Sub-text: Refresh portfolio and retry pledging. If the issue persists, reach out to support for assistance. | **Case 1: Partial pledging

CTA 1: Continue to pledge {{RTA name}}

CTA 2:** CTA 2: Need help? Contact us.

—————————-
**Case 2: Pledging failed for all portfolio**

CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |
| Mark Unit is greater than available Units | 147 | Caused due to duplicate request | - Tech need to check why this is coming at OTP verification this should have came at time of INIT
- Tech team need to add validation in BE to avoid the duplicate request | [https://docs.google.com/document/d/1m84M_Rq6Rg_NsGooamj_2SVfhmbF0exi44zS9pKRTOQ/edit?usp=sharing](https://docs.google.com/document/d/1m84M_Rq6Rg_NsGooamj_2SVfhmbF0exi44zS9pKRTOQ/edit?usp=sharing) | Your portfolio details are outdated! | Please refresh your mutual fund portfolio to get the latest details & try again. |  |
| Already lien marked against this pan  for this lien ref no | 100 | Caused due to duplicate request | - Internal bug, Tech need to provide RCA and resolution

- Tech team need to add validation in BE to avoid the duplicate request | [https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) |  |  |  |
| SUCCESS | 54 |  | Already handled |  |  |  |  |
| Invalid OTP attempt maximum reached. | 36 | Need to check if we are sending new ref number in this case | Already handled |  |  |  |  |
| schemedetails parameter is missing in the request. | 26 | - Empty request sent

- Caused due to duplicate request
 | Internal bug, Tech need to provide RCA and resolution | [https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) |  |  |  |
| OTP Expired please regenerate again. | 12 |  | Already handled |  |  |  |  |
| Invalid Reqrefno | 2 | - Invalid reference number sent

- Caused due to duplicate request | Internal bug, Tech need to provide RCA and resolution | [https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) |  |  |  |
| Invalid otp value | 1 |  | Already handled |  |  |  |  |
| Default error |  | Any other error which are not handled |  |  | Error occurred while pledging your portfolio with {{RTA}} | Refresh portfolio and retry pledging. If the issue persists, reach out to support for assistance. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |

### KFIN Validation error cases

<aside>
💡

- Currently we are using KFIN LAMF V1 API and with this API we get error at request level but not at the folio level
- In LAMF V2 we will get error at folio level [Handling of error has to done post LAMF V2 API is integrated]
</aside>

| RTA response | **Count** | **Comment** | **Next step** | RCA Doc | Heading | Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Success | 12899 | OK | Already handled |  |  |  |  |
| RequestID Cannot Process as Units are Not Available | 8191 | Unit mismatch | Refresh KFIN folio |  | Your portfolio details are outdated! | Please refresh your mutual fund portfolio to get the latest details & try again. |  |
| Request not Allowed as one of the Fund is not valid | 1403 | Volt internal issue | Internal bug, Tech need to provide RCA and resolution |  | One of your mutual fund portfolio are not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |
| KYCStatus not verified | 950 | Two possible reason:- User fetching MFC but not with KFIN [PhonePe and other platform]- User has fetched with KFIN but still getting this issue, might be a case where we are not updating the value | If KFIN has been not fetched then ask user to refresh with KFIN |  | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| fatca not verified | 300 | Three possible reason:- User fetching MFC but not with KFIN [PhonePe and other platform]- Issue at KFIN end- 

Issue at Volt end: sent empty object in validate pledge API- Need to check if we get "FATCA not verified" in MFC CAS | - If KFIN has been not fetched then ask user to refresh with KFIN- Tech need to fix issue which happened due to internal issue | [https://docs.google.com/document/d/1C8KxUVPUSUho_Fq63_Vn7l9X2bA0tQcb1K6Hq1uTwfc/edit?usp=sharing](https://docs.google.com/document/d/1C8KxUVPUSUho_Fq63_Vn7l9X2bA0tQcb1K6Hq1uTwfc/edit?usp=sharing) | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| Request not Allowed as one of the folio not belongs to the given Invpan | 259 | Volt internal issue | Internal bug, Tech need to provide RCA and resolution | [https://docs.google.com/document/d/1q3OR66efbWOIWmyQNQc8mkIqSJy-qw7glPSYmy_JNXQ/edit?usp=sharing](https://docs.google.com/document/d/1q3OR66efbWOIWmyQNQc8mkIqSJy-qw7glPSYmy_JNXQ/edit?usp=sharing) | Given PAN EXBPS7155E is not linked with all of the portfolios | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| Data Doesnot Exists related to Mobile Number | 148 | Volt internal issue | Internal bug, Tech need to provide RCA and resolution | [https://docs.google.com/document/d/1fpUkbAUdI1MXdvGByGq4ejsLOsHNqcAjZi1OeuQlWkc/edit?usp=sharing](https://docs.google.com/document/d/1fpUkbAUdI1MXdvGByGq4ejsLOsHNqcAjZi1OeuQlWkc/edit?usp=sharing) | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| Request not Allowed as one of the  folio is Under Cooling Period | 129 | - This happens only for Nippon folio- Need to check time gap b/w fetch and pledge | - Refresh KFIN folio |  | One of your mutual fund portfolio are not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| PAN-aadhar seeding not completed | 84 | This issue will not come, as KFIN has fixed the issue | NA | [https://docs.google.com/document/d/1w5Tp_tJFkKM4f_xmwuwK2STI-8irsuvkEwnz-ZKXrE0/edit?usp=sharing](https://docs.google.com/document/d/1w5Tp_tJFkKM4f_xmwuwK2STI-8irsuvkEwnz-ZKXrE0/edit?usp=sharing) | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| Request not Allowed as one of the folio is NRI | 59 | Came for only 1 user in last 4 month, this is also becasue he did not fetched KFIN | Refresh KFIN folio |  | One of your mutual fund portfolio are not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| Request not Allowed as one of the folio is Under DEMAT | 57 | Need to raise this with KFIN to understand why DEMAT folio was fetched | Refresh KFIN folio | [https://docs.google.com/document/d/1WCfemmSNMFHW_UZBo0ev_pRrohQY8Q6RvEQFOoh5n4I/edit?usp=sharing](https://docs.google.com/document/d/1WCfemmSNMFHW_UZBo0ev_pRrohQY8Q6RvEQFOoh5n4I/edit?usp=sharing) | One of your mutual fund portfolio are not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| SEBI Debarred PAN are restricted for Lien Marking | 20 | - PAN blacklisted for Pledging- This happend for only one user who did not fetched with KFIN | Ask user to refresh, non eligible funds will be removed |  | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
| Problem occured while saving | 19 | API failure at KFIN end | - Inform user about the technical issue and ask user to retry - Retry validation with same request and reference number |  | Facing technical issues with {{RTA name}} in pledging mutual fund investments. | Please try again.If the issue persists, reach out to support for assistance. | CTA 1: Retry

CTA 2: Need help? Contact us. |
| Please Enter valid LenderID | 12 | This is due to Volt internal issue | Tech need to check and fix this | [https://docs.google.com/document/d/1F_zJpKm75TPTfSwDE4iOdlHjZHF2n6bC63W7uR666j4/edit?usp=sharing](https://docs.google.com/document/d/1F_zJpKm75TPTfSwDE4iOdlHjZHF2n6bC63W7uR666j4/edit?usp=sharing) | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. |  |
|  | 9 | No remarks due to "schemedetails parameter is missing in the request" issue | Tech need to check and fix this | Didn't get for KFIN |  |  |  |
| The request is currently in the process. | 4 | Need to check if we are calling API multiple time | Tech need to check and fix this |  | Pledging with {{RTA name}} already in progress | Please wait while we complete the pledging process. reach out to support for assistance. | CTA 1: Ok, got it!

CTA 2: Need help? Contact us. |
| Please Enter valid ProviderID | 2 | Invalid - this happened only for Saksham account | NA |  |  |  |  |
| Default error |  | Any other error which are not handled |  |  | Error occurred while validating your portfolio with {{RTA name}} | Refresh your portfolio and try again. If the issue persists, reach out to support for assistance. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |

### KFIN Auth error cases

| RTA response | **count** | **Comment** | **Next step** | RCA Doc | Heading | Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Success | 11703 | OK | NA |  |  |  |  |
| Invalid OTP Related to RequestID | 661 | OK | NA |  |  |  |  |
| Request Already Exists | 18 | Duplicate request | Internal bug, Tech need to provide RCA and resolution | [https://docs.google.com/document/d/1US8ItOhJj9Ppqmps48LLSak7upS_0iUzrC9j7tOp0YI/edit?usp=sharing](https://docs.google.com/document/d/1US8ItOhJj9Ppqmps48LLSak7upS_0iUzrC9j7tOp0YI/edit?usp=sharing) | Pledging with {{RTA name}} already in progress | Please wait while we complete the pledging process. reach out to support for assistance. | CTA 1: Ok, got it!

CTA 2: Need help? Contact us. |
| Problem occured while saving | 4 | KFIN API failure | - Inform user about the technical issue and ask user to retry - Retry validation with same request and reference number |  | Facing technical issues with {{RTA name}} in pledging mutual fund investments. | Please try again. If the issue persists, reach out to support for assistance. | CTA 1: Retry

CTA 2: Need help? Contact us. |
| Default error |  | Any other error which are not handled |  |  | Error occurred while pledging your portfolio with {{RTA name}} | Refresh your portfolio and try again. If the issue persists, reach out to support for assistance. | CTA 1: Refresh portfolio

CTA 2: Need help? Contact us. |

## User flow

https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/[New]-Loan-application-journey?node-id=31-40687&node-type=section&t=Eyj4bUrEutCZViHt-11

## Requirements

BE Requirement checklist:

- Fix all issue caused at our end [P0]
- Maintain latest fetch date for both RTA and expiry date for same [P0]
    - Expiry date for both RTA should be configurable from the BE
- Logic to decide which RTA to pledge first [P0]
- Logic to decide which RTA to refresh if pledge error occurs [P0]
- BE Config to send error message to FE based on error message received from RTA [P0]
- Push Validation and Auth error on Amplitude [P0]
- Handle if call back doesn’t received from RTA [P0]
- Show request level RTA response on service dashboard [P1]
    - Along with timestamp of fetch and pledge at RTA level
- Data required for reporting [P0]
- Handle when RTA is down: BE need to share solution based on cloudwatch alarm [P1]

FE requirement checklist:

- Provide root cause analysis for issues originating from the front-end
    - For error analysis and next step refer: https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?usp=sharing
- Pledge landing page
    - Nudge user to refresh folio based on last fetch date
    - Allow user to edit their limit on pledge landing page
    - Handle drop-off
- Pledge error handling
- Refresh portfolio flow
- Handle calculation of selected CL based on above mentioned logic [refer: 2.h]

---

# **Design**

Design requirement: https://www.figma.com/board/eOSD0vbZEK2UcevWndsNm9/Pledge-error-handling?node-id=0-1&t=8vPXs7icvlrd3WSI-1

UI screens link: 

[https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Fdesign%2Fu5fpymb6jC6ubzT9YUXFgb%2FLoan-application-flow%3Fnode-id%3D9720-35718](https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Fdesign%2Fu5fpymb6jC6ubzT9YUXFgb%2FLoan-application-flow%3Fnode-id%3D9720-35718)

1. Folio mismatch modal
    1. Heading
    2. Subheading
    3. CTA [Refresh portfolio]
        1. Fetch folio at pledge step based on user action
2. Updated eligible limit modal
    1. Eligible limit amount
    2. Nudge to select unselected funds if updated credit limit becomes <25k
    3. Edit limit CTA
    4.  CTA [Proceed to pledge with RTA]
3. Edit limit pop up
    1. Select credit limit
    2. List of selected folio
    3. List of available folio 
    4. CTA on popup [Select folio] 
    5. CTA [Proceed to pledge with RTA]

---

# **Analytics**

List of amplitude events [FE+BE]:

| User flow | User action | Event name | Trigger from | Event property  | ExpectedValue |
| --- | --- | --- | --- | --- | --- |
| AssetPledge | User lands on Asset pledge landing page | MF_PLEDGE_FUNDS_LANDING_PAGE_VIEWED | Frontend |  |  |
|  | When user click on “Pledge funds” or “Pledge remaining funds” | MF_PLEDGE_FUNDS_BUTTON_CLICKED | Frontend | RTA | cams/kfin |
|  | User clicks on edit limit button on pledge funds landing page | EDIT_LIMIT_BUTTON_CLICKED | Frontend | page | pledge landing page |
|  | RTA API is called to validate the CAS data for pledging | MF_CAS_VALIDATION_FOR_PLEDGE_RESULT | Backend | RTA | cams/kfin |
|  |  |  |  | status | TRUE/FALSE |
|  |  |  |  | message | {{remarks received from RTA}} |
|  |  |  |  | rta_error_type |  |
|  | when user enters otp received by CAMS or KFIN to pledge asset | MF_PLEDGE_OTP_VERIFICATION_TRIGGERED | Backend | source | cams/kfin |
|  | when user click on resend otp to confirm pledge through CAMS or KFIN | MF_PLEDGE_OTP_RESEND | Frontend | RTA | cams/kfin |
|  |  |  |  | attempt_count | 1 |
|  | asset pledge result after otp verification from CAMS or KFIN | MF_PLEDGE_RESULT | Backend | pledge_status | Success/failed/partially pledged |
|  |  |  |  | RTA | cams/kfin |
|  |  |  |  | Message | {{remarks received from RTA}} |
|  |  |  |  | rta_error_type | 100/400/1 |
|  |  |  |  | total_pledge_count | 1 |
|  |  |  |  | total_pledge_amount | 100000 |
|  | - User click on refresh CTA after pledge error 
- Refresh button on modal or pledge funds landing page | MF_REFRESH_PORTFOLIO_BUTTON_CLICKED | FRONTEND |  |  |
|  | Event already exist in fetch flow, just add at time of fetching at pledge step | GET_MF_PORTFOLIO_REQUESTED | Backend | email | santanu.mldt@gmail.com |
|  |  |  |  | get_folio_from | CAMS |
|  |  |  |  | mobile | +917384637254 |
|  | Event already exist in fetch flow, just add at time of fetching at pledge step | GET_MF_PORTFOLIO_AUTH_RTA | Backend | **email** |  |
|  |  |  |  | **mobile** |  |
|  |  |  |  | **result** |  |
|  |  |  |  | **rta** |  |
|  |  |  |  | rta_error_type |  |
|  | Event already exist in fetch flow, just add at time of fetching at pledge step | GET_MF_PORTFOLIO_AUTH_RESULT |  | **get_folio_from** |  |
|  |  |  |  | **mobile** |  |
|  |  |  |  | **result** |  |
|  | Event already exist in fetch flow, just add at time of fetching at pledge step | GET_MF_PORTFOLIO_OTP_RTA |  | **result** |  |
|  |  |  |  | **rta** |  |
|  |  |  |  | **rta_error_type** |  |
|  | Event already exist in fetch flow, just add at time of fetching at pledge step | GET_MF_PORTFOLIO_OTP_RESULT |  | Same as current |  |
|  |  |  |  |  |  |

Below are the metrics we would want to measure. [Reporting requirement]

- Number and %age of pledge errors reduced due to refresh of KFin portfolio
- Success rate of pledge step post this release for CAMS
- Distribution of the pledge success rate by folio for CAMS
- Number of pledge errors reduced due to refresh of CAMS portfolio
- Success rate of pledge step post this release for KFIN
- Success rate of pledge step post this release overall
- Fallback error report: error which we have not handled

---

# **Timeline/Release Planning**

---

# Roadmap

@Ranjan kumar Singh - we can mention that the roadmap will include using KFin LAMF v2 post go live for better conversions.

1. Integration of KFIN LAMF V2
2. MFC lien validation API
3. Handle PF on offer page [PF based on Credit limit]

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  
- [ ]  Business
    - [ ]  Sign-off on the
- [ ]  Design
    - [ ]  Handle all scenarios
- [ ]  Engineering
    - [ ]  Share BE related RCAs related for pledge errors
    - [ ]  Share FE related RCAs related for pledge errors

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

Limitations:

- For KFIN we do not get error folio wise but for CAMS we get folio wise error

## Meeting notes

As per above error data, we primarily need to solve for Unit mismatch cases:

For this case we can solve this in two way:

1. Use MFC lien validation API to check available units before user start the pledging -  MFC POC needs to be done
2. Enable user to refresh the portfolio after user gets the error from RTA.

1. Nudge user to refresh the folio if user drop-off and come back after 24 hours on pledge landing page.
    - If user do not refresh and trigger OTP for RTA 1, and unit mismatch error is thrown. then ask user to refresh the folio of RTA 1.
    - Or, user can trigger OTP for RTA 2.
    - If pledge with RTA 2 is completed, then user should have option to refresh 1 RTA.
    - If SL is > 25k and pledging with 1 RTA is completed, then allow user to skip the pledge step and calculation of SL should be inclusive of CL of RTA 1 and RTA 2 so that user can pledge the rest of funds after loan application completion and user should not have to sign the agreement again.
- For CAMS, we can display the specific folio encountering an error along with the corresponding error message of pledge landing page.
- After the refresh if CL become ineligible and funds are unselected for pledging, then nudge user to select the unselected funds to get eligible

- 

**KFIN AUTH - 1 week logs**

| Error | Count | Cause | Handling on UI | RCA required |
| --- | --- | --- | --- | --- |
| RequestID Cannot Process as Units are Not Available | 78 | Available units for pledging is less then requested units | Ask user to refresh for CAMS and KFIN |  |
| Data Does not Exists related to Mobile Number | 1 | User might have changed the mobile number for folio | Ask user to refresh for CAMS and KFIN |  |
|  Request not Allowed as one of the folio is Under DEMAT | 4 | This should not have to come at pledge Step | Refresh | Yes |
| PAN-aadhar seeding not completed  | 4 | - User PAN and Aadhaar not linked
- This error should not come at pledge step
- This should have caught at fetch step
- Happening for MFC fetch
 | Refresh | Yes |
| KYCStatus not verified | 4 | Should not come at pledge step | Refresh | Yes |
| Request not Allowed as one of the  folio is Under Cooling Period | 2 | If any details changed for folio, Nippon do not allow the pledge for 6 month | Refresh |  |
|  Request not Allowed as one of the folio not belongs to the given Invpan  | 4 | - This should have caught at fetch step
- Might be happening Because, Joint holder funds are not getting filtered out
 | Refresh | Yes |
|  Request not Allowed as one of the folio is NRI | 1 | Need to check if we get tax status in CAMS / KFIN fetch / MFC fetch | Refresh | Yes |

**KFIN Validation - 1 week logs**

| Error | Count | Cause | RCA required |
| --- | --- | --- | --- |
| Invalid OTP Related to RequestID  | 144 | Wrong OTP entered by user |  |
| Problem occurred while saving | 1 | ? | Yes |
| Request Already Exists | 2 | ? | Yes |

**CAMS AUTH - 1 week logs**

*Note: We get  folio wise error in CAMS*

| Error | Cause | UI handling | Backend | RCA required |
| --- | --- | --- | --- | --- |
| Unit is greater than available Units | Requested Unit is greater then available unit | Refresh |  |  |
| Given Mobile not match with given folio | Mobile number for folio might have changed | Refresh | We need to show  folio wise error on service desk |  |
| Given Folio not match with given pan | Might be passing joint-holder funds for pledging | Refresh | We need to show  folio wise error on service desk | Yes |
| Given folio is invalid due to mobile and email | Mobile and email not linked with Folio | Refresh | We need to show folio wise error on service desk | Yes |
| null | ? | ? | ? | Yes |

**CAMS Validation - 1 week logs**

| Error | count | UI handling |
| --- | --- | --- |
| Invalid OTP | 133 | Enter valid OTP |
| OTP Expired please regenerate again | 1 | Trigger OTP again |
| schemedetails parameter is missing in the request | 6 | Refresh |
| Mark Unit is greater than available Units | 13 | Refresh |
| Invalid OTP attempt maximum reached | 1 | 5 time allowed, regenerate after 10 min, trigger OTP again and resend request |

| User Action | Scenario | Reasons | Handling on UI |
| --- | --- | --- | --- |
| User tigger OTP for RTA 1 | Auth error occurred for RTA 1 | Unit is greater than available Units | Refresh portfolio |
|  |  | Given Mobile not match with given folio | Refresh portfolio |
|  |  | Given Folio not match with given pan | Refresh portfolio |
|  |  | Given folio is invalid due to mobile and email | Refresh portfolio |
|  | If not Auth error -Validation error occurred for RTA 1 | Invalid OTP | Error: Enter valid OTP |
|  |  | schemedetails parameter is missing in the request | Refresh portfolio |
|  |  | OTP Expired  |  |
|  |  | Mark Unit is greater than available Units | Refresh portfolio |
|  |  | Invalid OTP attempt maximum reached |  |
|  | If not Auth and pledge error - Pledge is completed with RTA 1 |  |  |
| **In case of Auth and validation error:** 
User refresh the portfolio | Limit decreased after refresh but limit ≥25 |  |  |
|  | Limit increased after refresh |  | **If funds belongs to only 1 RTA :** 
- Show Updated limit after refresh
- Edit limit option 

**If funds belongs to both the RTAs:**
- Show updated limit after refreshing both RTA |
|  | Limit decreased after refresh and new limit < 25 |  | **If user has fetched both RTA:**
Case 1: Fetched both but no funds found with 1 RTA
Case 2: Fetched both but not all funds selected for pledging

**User fetched 1 RTA and proceeded for pledging:**
- If user become ineligible after refreshing 1 RTA, ask user to fetch with other RTA
- If user become ineligible after fetching the both RTA, show not eligible message to user
**** |
| User tigger OTP for RTA 1 after refresh | Auth error occurred for RTA 1 |  |  |
|  | If not Auth error - Validation error occurred for RTA 1 |  |  |
|  | If not Auth and pledge error - Pledge is completed with RTA 1 |  |  |
| User tigger OTP for RTA 2 | Auth error occurred for RTA 2 |  |  |
| User refresh the portfolio and folio with RTA 1 is pledged | Limit decreased after refresh [RTA 1(already pledged) + RTA 2 limit ≥25] |  |  |
|  | Limit increased after refresh [No new folio fetched for RTA 1] |  |  |
|  | Limit increased after refresh [New folio fetched for RTA 1] |  |  |
|  | Limit decreased after refresh [RTA 1(already pledged) + RTA 2 limit < 25] |  |  |
| User refreshed the portfolio for RTA 2 and folio with RTA 1 is not pledged | This case will not arise as per current implementation |  |  |
|  |  |  |  |
|  | User facing issue with Pledging due to error from RTA even after refresh |  | - Currently we do allow user to Skip Pledging with one RTA on UI
- OPS team request backend team to skip the pledging of 1 RTA |

### Lien validation request API request and response

```jsx
Lien validation API Request
{ 
    "reqId": "2048269", 
    "pan": "AZHPR1374G", 
    "pekrn": "", 
    "mobile": "7904530323", 
    "email": "", 
    "clientId": "sampleClientId", 
    "clientRefNo": "sample123", 
    "lenderCode": "123", 
    "data": [ 
        { 
            "schemeDetails": [ 
                { 
                    "amc": "T", 
                    "amcname": "Tata Mutual Fund", 
                    "folio": "3591684", 
                    "isin": "INF277K014C0", 
                    "itemNo": "", 
                    "schemeCode": "LSD01", 
                    "schemeName": "", 
                    "schemeType": "", 
                    "lienUnits": "5"  
                } 
            ] 
        } 
    ] 
} 
```

```jsx
Lien validation API Response
{ 
"reqId":"2451478", 
"pan":"AZHPR1374G", 
"pekrn":"", 
"mobile":"7904530323", 
"email":"", 
"clientId":"sampleClientId", 
"lenderCode":"123", 
"pending":[], 
"errors":[], 
"success":[ 
{ 
"rtaName":"CAMS", 
"lienRefNo":"18409", 
"schemeDetails":[ 
{ 
"amc":"T", 
"folio":"3591684", 
"schemeName":"", 
"isin":"INF277K014C0", 
"itemNo":"", 
"lienUnits":"3" 
} 
] 
} 
], 
"validateId":"2451478"
```

### Lien validation API DOC

[MFCentral LAMF API document for 1.7 (2).pdf](Pledge%20error%20handling/MFCentral_LAMF_API_document_for_1.7_(2).pdf)

### Lien validation criteria

| Criteria  | Result | If fails |
| --- | --- | --- |
| No. of folio we send in request should match with the no of folio we get in response |  | Refresh |
| Unit qty of each folio in request should match with the Unit qty of each folio we get in response |  | Refresh |
| We should be get success response with Given PAN and mobile |  |  |
| We need to check if we are getting success response with one lender code i.e if we send only lender code of BAJAJ then API will work or not |  |  |
| We need to check what exactly we are getting in “errors[]” |  |  |
| We need to check what exactly we are getting in “pending[]” |  |  |
| Validate for already pledged unit for both lender |  |  |
| Validate for Locked unit for both RTA |  |  |
| Validation working for AE/CS funds for both RTA |  |  |
| Check response for pre-pledging and Post pledging scenario |  |  |

### Lien validation API scenarios

Scenario 1: 

User lands on pledge screen -> Lien validation API is called to validate the folio available for pledging -> Loading screen will be shown to user [Verifying your portfolio available for pledging]

Case 1 : Mismatch in units found

Action: Show “Folio changed” message to User and ask to refresh both RTA 

Case 2 : Folio mismatch found [Mismatch in ISIN]

Action: Show “Folio changed” message to User and ask to refresh both RTA

Case 3 : MFC API returned success but empty response

Action: Allow user to proceed for pledge → User started pledging →OTP triggered for RTA 1 → If error occurred → Ask user to refresh → User need to Refresh folio with RTA → if user dropped → show refresh option on Pledge screen

Case 4 : API failure

Action: Allow user to proceed pledge -> In case of RTA error -> Ask user to refresh portfolio

Scenario 2: 

User lands on pledge screen -> Lien validation API is called to validate the folio available for pledging -> Loading screen will be shown to user [Verifying your portfolio available for pledging] -> No mismatch found

Case 1: No mismatch found with lien validation but RTA returned the Auth or validation error

Action: Ask user to refresh the portfolio with both the RTA

- KFIN validation error cases [1-31st AUG]
    - Note:
        - We do not get folio level error in KFIN LAMF API V1, but we will get folio level error in LAMF V2
        - We won’t be able to identify for which folio error has occurred.

| *Error message* | Cause | Handling on UI | Modal Heading text | Modal Sub-heading text | CTA |
| --- | --- | --- | --- | --- | --- |
| Request not Allowed as one of the folio not belongs to the given Invpan |  | Open a modal to display the specific error message to the user, clearly explaining the issue. Prompt the user to refresh the portfolio linked to the relevant RTA to resolve the error. | Request not allowed! | One of your folio is not linked to the provided PAN [PAN Number]. Please refresh now to get latest portfolio. |  |
| Data Doesnot Exists related to Mobile Number | User might have updated the mobile linked with folio |  | Request not allowed! | One of your folio is not linked to the provided Mobile [ Mobile Number]. Please refresh now to get latest portfolio. |  |
| fatca not verified | - FATCA is not verified for given folio for pledging
- We have seen some cases where user got this error and after retry this issue got resolved
- Connect with KFIN and understand how to FIX | TBD 

Should we ask user to verify FATCA using NCT API |  |  |  |
| KYCStatus not verified | User KYC status is not verified, need to get this resolved with KFIN
- This issue should not come in KFIN LAMF V2 | TBD |  |  |  |
| Request not Allowed as one of the  folio is Under Cooling Period | This only happens for Nippon folio. when user change and folio details |  | Request not allowed! | It seems your portfolio details has been changed after your last fetch, please refresh now to get latest portfolio. |  |
| Request not Allowed as one of the Fund is not valid |  |  | Request not allowed! | It seems your portfolio details has been changed after your last fetch, please refresh now to get latest portfolio. |  |
| RequestID Cannot Process as Units are Not Available |  |  | Portfolio mismatch found! | It seems your portfolio details has been changed after your last fetch, please refresh now to get latest portfolio. |  |
| Default [Any other error] | We need to understand the error on regular basis and handle UX accordingly  | Generic message on modal and ask user to refresh folio | Portfolio mismatch found! | It seems your portfolio details has been changed after your last fetch, please refresh now to get latest portfolio. |  |
- KFIN Auth error cases [1-31st AUG]

| *Error* | Cause | Handling on UI | Modal Heading text | Modal Sub-heading text |
| --- | --- | --- | --- | --- |
| Data Doesnot Exists | Folio not found with given phone/email/Pan |  | Request not allowed! | It seems your portfolio details has been changed after your last fetch, please refresh now to get latest portfolio. |
| Data Doesnot Exists related to Mobile Number/EmailID | Folio not found with given phone/email/Pan |  | Request not allowed! | It seems your portfolio details has been changed after your last fetch, please refresh now to get latest portfolio. |
| fatca not verified |  |  |  |  |
| KYC Status not verified |  |  |  |  |
| SEBI Debarred PAN are restricted for Lien Marking | User blacklisted for pledging MF | TBD |  |  |
| Default [Any other error] | We need to understand the error on regular basis and handle UX accordingly  | Generic message on modal and ask user to refresh folio | Portfolio mismatch found! | It seems your portfolio details has been changed after your last fetch, please refresh now to get latest portfolio. |

1. **Handling on UI if error occurs:**
    - For any of the errors listed below, we should prompt the user to refresh the folio by displaying a generic message. Since a basket of folios can generate multiple type of errors in a single request, it is not feasible to show a contextual message for each error.
    - If user refresh the folio with CAMS
        - **Case 1: Updated limit with CAMS is = 0**
            - Ask user to proceed pledging with KFIN if KFIN funds are available for pledging
            - If KFIN funds are not available for pledging [KFIN Funds may not available due to below scenario]
                - Scenario 1: User had fetched with KFIN but no funds was found
                    - Ask user to fetch with KFIN again along with option to reach out to support
                        - Hypothesis: User may have done new investment
                    - If no funds found after re-fetch then inform user the they are not eligible for loan along with contact support option.
                - Scenario 2: User had fetched with KFIN but no funds was selected for pledging
                    - Ask user to select the unselected funds and if credit limit for selected funds is >10k then given option to proceed for pledging
                - Scenario 3: User did not fetched folio with KFIN
                    - Ask user to fetch folio with KFIN and if credit limit is >10K then give option to proceed for pledging else inform user that they are not eligible for loan along with contact support option
        
        - **Case 2: Updated limit with CAMS is > 0**
            - Scenario 1: Updated credit limit with CAMS is ≥ 10K
                - Allow user to proceed for pledging with CAMS along with edit limit option.
            - Scenario 2: Updated credit limit with CAMS is < 10K [when all CAMS funds are selected for pledging]
                - Check if KFIN funds are available and SUM of Credit limit with both the RTA is ≥10k
                    - If yes, allow user to proceed for pledging with CAMS
                    - If no, inform user that their limit is not sufficient to proceed for pledging and nudge user to fetch with KFIN
        
        b. **Handle user drop-off if CAMS error occurred and user dropped-off without refreshing or without pledging**
        
        - CAMS error occurred and user drop-off and return back on app and lands on pledge landing page
            - Show message on UI to user: Your credit limit has expired, refetch you portfolio to continue
            - User has to refresh folio only with CAMS if error has only came for CAMS
            - If user refresh the folio → Allow user to pledge with CAMS

Callouts:

- Meeting notes:
    -