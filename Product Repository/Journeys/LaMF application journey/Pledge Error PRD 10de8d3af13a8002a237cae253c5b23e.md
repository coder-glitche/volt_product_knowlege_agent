# Pledge Error PRD

# Product Requirements Document (PRD)

## Title

**Volt Money Pledge Error Handling Enhancement**

---

## Table of Contents

---

## Introduction

The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries.

## Problem Statement

Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries.

### Common Errors Encountered:

- **CAMS Validation Errors**
- **CAMS Authentication Errors**
- **KFIN Validation Errors**
- **KFIN Authentication Errors**

A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342).

## Objectives

- **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors.
- **Enhance User Experience:** Provide clear, actionable error messages and guidance.
- **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors.
- **Improve Conversion Rates:** Increase the number of successful pledge completions.
- **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors.
- **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes.

## User Journey

The Volt Money loan process involves the following key steps:

1. **Login**
2. **PAN Verification**
3. **Fetch Folio**
4. **Eligibility Assessment and Lender Assignment**
5. **KYC Verification**
6. **Bank Account Verification**
7. **Mandate Setting**
8. **Asset Pledge**
9. **KFS and Documentation**
10. **Loan Agreement Execution**

## Success Metrics

- **Drop-off Reduction:** Decrease in user drop-offs at the pledge step.
- **Support Query Reduction:** Fewer customer support queries related to pledge errors.
- **Escalation Minimization:** Reduction in escalations and negative public feedback.
- **Conversion Rate Improvement:** Higher rates of successful pledge completions.
    - Increased authentication success rates.
    - Increased validation success rates.
- **Resolution Time:** Shorter time to resolve pledge-related errors.
- **Retry Attempts:** Fewer repeated user attempts to complete pledges.
- **Turnaround Time (TAT):** Reduced sanction and disbursement TAT.

## Competitive Analysis

*Currently, no specific competitors are detailed. This section can be expanded based on market research.*

## Solution

### Requirements Overview

### 1. Portfolio Refresh Prompt

- **Trigger:** User lands on the pledge landing page.
- **Condition:** Last fetch date for both RTAs is older than 72 hours.
- **Action:**
    - Display notification: “Your portfolios are outdated, data may be inaccurate” with a "Refresh" CTA.
    - If "Refresh" is selected:
        - Navigate to fetch folio for both RTAs.
        - Update limits and allow users to edit limits.
        - Handle errors if selected DP is less than ₹25K.
    - If "Refresh" is declined:
        - Allow the user to proceed with pledging.

### 2. Error Handling for CAMS and KFIN

- **Validation and Authentication Errors:**
    - **Pledge Priority:** Pledge with the RTA having a higher DP first.
    - **Error Encounter Handling:**
        - If error occurs with the first RTA, determine whether to refresh the second RTA based on the last fetch date or fetch type.
        - Refer to the [Flow Chart](https://www.figma.com/board/eOSD0vbZEK2UcevWndsNm9/Pledge-error-handling?node-id=155-2278&t=mj4LQTv4b0b4Q7Fp-4) for detailed logic.
    - **User Messaging:**
        - Display error messages based on RTA responses.
        - Backend should provide actionable steps for the frontend to display.
        - Example: For KYC not verified, prompt to pledge with another RTA if available DP is ≥ ₹25K.
    - **Dashboard Visibility:**
        - Provide visibility to RM/Ops/Sales on service dashboards, including RTA responses and pledge outcomes.

### 3. Sanction Limit Logic

- **Basis:** Business logic to determine sanction limits based on pledged DP.
- **Scenarios:**
    1. **DP Selected = DP Pledged:** Sanction limit equals DP pledged.
    2. **DP Pledged > Threshold:** Sanction limit equals DP pledged.
    3. **DP Selected > DP Pledged > Threshold:** Sanction limit equals DP selected.
    4. **DP Pledged < Threshold:** Sanction limit equals DP selected.

**Definitions:**

- **DP Selected:** DP based on selected folios for pledging (minimum ₹25K).
- **DP Pledged:** DP based on successfully pledged folios.
- **Threshold:** ₹12.5K, used to determine sanction limits in partial pledging scenarios.

### Error Handling

### CAMS Validation Errors

| RTA Response | Count | Comment | Next Step | RCA Doc | UI Heading | UI Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *Empty* | 31,230 | Missing schemedetails parameter | Internal bug resolution | [Link](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) | Error Occurred | An unexpected error occurred. Please try again later. | Contact Support |
| SUCCESS | 20,058 |  | None |  |  |  |  |
| Lien Unit is greater than available Units | 6,875 | Unit mismatch | Ask user to refresh folio |  | Your portfolio details are outdated! | Please refresh your mutual fund portfolio to get the latest details & try again. | Refresh Portfolio <br> Need Help? Contact us. |
| Given Folio not match with given PAN | 459 | Incorrect folio or PAN | Ask user to refresh folio | [Link](https://docs.google.com/document/d/1nB1N7W6FzPTCMjlzg1weagR_5qp1FiMc3RCnqae0G14/edit?usp=sharing) | Given PAN <PAN> is not linked with all of the portfolios | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Given Mobile not match with given folio | 295 | Incorrect folio or mobile | Ask user to refresh folio | [Link](https://docs.google.com/document/d/10dUXoI6NBD54DXQ1hLi-cCYU0YwPpJzOZOzfFLSzozs/edit?usp=sharing) | Given Mobile 7980565882 is not linked with all of the portfolios | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Given folio is invalid due to invalid mobile and email | 114 | Incorrect folio or mobile | Resolved issue | [Link](https://docs.google.com/document/d/10dUXoI6NBD54DXQ1hLi-cCYU0YwPpJzOZOzfFLSzozs/edit?usp=sharing) | Given Mobile 7980565882 is not linked with all of the portfolios | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Default error | N/A | Unhandled errors | Generic error message |  | Error occurred while validating your portfolio with {{RTA name}} | Refresh your portfolio and try again. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |

### CAMS Authentication Errors

| RTA Response | Count | Comment | Next Step | RCA Doc | UI Heading | UI Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lien marked successfully | 14,600 |  | None |  |  |  |  |
| Invalid OTP | 922 |  | Prompt for valid OTP |  |  |  |  |
| FAILURE | 222 | Possible KYC not verified | Inform technical issue |  | Partial Portfolio Pledged | Error occurred while pledging some portfolios with {{RTA name}}; however, {{countofportfoliowithsuccess}} portfolios were successfully pledged. | Continue to pledge {{RTA name}} <br> Need Help? Contact us. |
| Mark Unit is greater than available Units | 147 | Duplicate request | Add backend validation | [Link](https://docs.google.com/document/d/1m84M_Rq6Rg_NsGooamj_2SVfhmbF0exi44zS9pKRTOQ/edit?usp=sharing) | Error Occurred | Please refresh your portfolio and try again. | Refresh Portfolio |
| Already lien marked against this PAN for this lien ref no | 100 | Duplicate request | Add backend validation | [Link](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) | Error Occurred | Please refresh your portfolio and try again. | Refresh Portfolio |
| SUCCESS | 54 |  | None |  |  |  |  |
| Invalid OTP attempt maximum reached | 36 |  | Inform user to regenerate OTP |  |  |  |  |
| schemedetails parameter is missing in the request | 26 | Duplicate request | Add backend validation | [Link](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) | Error Occurred | Please refresh your portfolio and try again. | Refresh Portfolio |
| OTP Expired please regenerate again | 12 |  | Prompt to regenerate OTP |  |  |  |  |
| Invalid Reqrefno | 2 | Duplicate request | Add backend validation | [Link](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) | Error Occurred | Please refresh your portfolio and try again. | Refresh Portfolio |
| Invalid otp value | 1 |  | Prompt for valid OTP |  |  |  |  |
| Default error | N/A | Unhandled errors | Generic error message |  | Error occurred while pledging your portfolio with {{RTA name}} | Refresh your portfolio and try again. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |

### KFIN Validation Errors

*Note: Currently using KFIN LAMF V1 API, which provides request-level errors. LAMF V2 will offer folio-level errors.*

| RTA Response | Count | Comment | Next Step | RCA Doc | UI Heading | UI Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Success | 12,899 |  | None |  |  |  |  |
| RequestID Cannot Process as Units are Not Available | 8,191 | Unit mismatch | Refresh KFIN folio |  | Your portfolio details are outdated! | Please refresh your mutual fund portfolio to get the latest details & try again. | Refresh Portfolio |
| Request not Allowed as one of the Fund is not valid | 1,403 | Internal issue | Internal bug resolution |  | One of your mutual fund portfolio is not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| KYCStatus not verified | 950 | KYC not verified | Prompt to refresh with KFIN |  | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| fatca not verified | 300 | FATCA not verified | Prompt to refresh with KFIN & fix internal issues | [Link](https://docs.google.com/document/d/1C8KxUVPUSUho_Fq63_Vn7l9X2bA0tQcb1K6Hq1uTwfc/edit?usp=sharing) | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Request not Allowed as one of the folio not belongs to the given Invpan | 259 | Internal issue | Internal bug resolution | [Link](https://docs.google.com/document/d/1q3OR66efbWOIWmyQNQc8mkIqSJy-qw7glPSYmy_JNXQ/edit?usp=sharing) | Given PAN EXBPS7155E is not linked with all of the portfolios | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Data Doesnot Exists related to Mobile Number | 148 | Internal issue | Internal bug resolution | [Link](https://docs.google.com/document/d/1fpUkbAUdI1MXdvGByGq4ejsLOsHNqcAjZi1OeuQlWkc/edit?usp=sharing) | Error Occurred | Please refresh your portfolio and try again. If the issue persists, reach out to support for assistance. | Refresh Portfolio |
| Request not Allowed as one of the folio is Under Cooling Period | 129 | Limited pledging period | Refresh KFIN folio |  | One of your mutual fund portfolio is not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| PAN-aadhar seeding not completed | 84 | KFIN fixed the issue | N/A | [Link](https://docs.google.com/document/d/1w5Tp_tJFkKM4f_xmwuwK2STI-8irsuvkEwnz-ZKXrE0/edit?usp=sharing) | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Request not Allowed as one of the folio is NRI | 59 | Only 1 user affected | Refresh KFIN folio |  | One of your mutual fund portfolio is not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Request not Allowed as one of the folio is Under DEMAT | 57 | DEMAT folio issue | Raise with KFIN | [Link](https://docs.google.com/document/d/1WCfemmSNMFHW_UZBo0ev_pRrohQY8Q6RvEQFOoh5n4I/edit?usp=sharing) | One of your mutual fund portfolio is not eligible for pledging | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| SEBI Debarred PAN are restricted for Lien Marking | 20 | PAN blacklisted | Prompt to refresh |  | Portfolio validation failed at KFIN end | Refresh your portfolio to get updated mutual fund. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |
| Problem occured while saving | 19 | API failure | Inform technical issue & retry |  | Facing technical issues with {{RTA name}} in pledging mutual fund investments. | Please try again. If the issue persists, reach out to support for assistance. | Retry <br> Need Help? Contact us. |
| Please Enter valid LenderID | 12 | Internal issue | Internal bug resolution | [Link](https://docs.google.com/document/d/1F_zJpKm75TPTfSwDE4iOdlHjZHF2n6bC63W7uR666j4/edit?usp=sharing) | Error Occurred | Please refresh your portfolio and try again. | Refresh Portfolio |
| *Empty* | 9 | Missing schemedetails parameter | Internal bug resolution | [Link](https://docs.google.com/document/d/1uVPa_xgT7sCgWWQz3pN0BtWXcGuBLQ6M_pf4RYZ9eZ0/edit?usp=sharing) | Error Occurred | Please refresh your portfolio and try again. | Refresh Portfolio |
| The request is currently in the process. | 4 | Duplicate API call | Inform user to wait |  | Pledging with {{RTA name}} already in progress | Please wait while we complete the pledging process. Reach out to support for assistance. | Ok, got it! <br> Need Help? Contact us. |
| Please Enter valid ProviderID | 2 | Invalid provider | N/A |  |  |  |  |
| Default error | N/A | Unhandled errors | Generic error message |  | Error occurred while validating your portfolio with {{RTA name}} | Refresh your portfolio and try again. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |

### KFIN Authentication Errors

| RTA Response | Count | Comment | Next Step | RCA Doc | UI Heading | UI Sub-text | CTA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Success | 11,703 |  | None |  |  |  |  |
| Invalid OTP Related to RequestID | 661 |  | Prompt for valid OTP |  |  |  |  |
| Request Already Exists | 18 | Duplicate request | Internal bug resolution | [Link](https://docs.google.com/document/d/1US8ItOhJj9Ppqmps48LLSak7upS_0iUzrC9j7tOp0YI/edit?usp=sharing) | Pledging with {{RTA name}} already in progress | Please wait while we complete the pledging process. Reach out to support for assistance. | Ok, got it! <br> Need Help? Contact us. |
| Problem occured while saving | 4 | API failure | Inform technical issue & retry |  | Facing technical issues with {{RTA name}} in pledging mutual fund investments. | Please try again. If the issue persists, reach out to support for assistance. | Retry <br> Need Help? Contact us. |
| Default error | N/A | Unhandled errors | Generic error message |  | Error occurred while pledging your portfolio with {{RTA name}} | Refresh your portfolio and try again. If the issue persists, reach out to support for assistance. | Refresh Portfolio <br> Need Help? Contact us. |

### User Flow

Refer to the detailed [User Flow Diagram](https://www.figma.com/board/eOSD0vbZEK2UcevWndsNm9/Pledge-error-handling?node-id=155-2278&t=mj4LQTv4b0b4Q7Fp-4).

### Requirements

### Backend (BE) Requirements:

- **Issue Resolution:** Fix all internal issues causing pledge errors.
- **Data Management:** Maintain the latest fetch date and expiry date for both RTAs.
- **Pledging Logic:**
    - Determine the order of RTAs based on higher DP.
    - Decide which RTA to refresh upon encountering errors.
- **Error Messaging:** Configure backend to send appropriate error messages and next steps to the frontend based on RTA responses.
- **Dashboard Integration:** Provide request-level RTA responses and pledge outcomes on the service dashboard.
- **Reporting Data:** Ensure data required for reporting is available.
- **Analytics Integration:** Push validation and authentication errors to Amplitude.

### Frontend (FE) Requirements:

- **UI Design:** Implement error handling UI based on backend messages.
- **User Prompts:** Display actionable prompts (e.g., refresh portfolio, contact support) based on error types.
- **Limit Editing:** Allow users to edit credit limits post-refresh.
- **Error Modals:** Show specific modals for different error scenarios as per design specifications.

## Design

Refer to the comprehensive [Design Requirements](https://www.figma.com/board/eOSD0vbZEK2UcevWndsNm9/Pledge-error-handling?node-id=0-1&t=8vPXs7icvlrd3WSI-1).

### Key Design Components:

1. **Folio Mismatch Modal**
    - **Heading**
    - **Subheading**
    - **CTAs:** "Refresh Portfolio"
2. **Updated Eligible Limit Modal**
    - **Eligible Limit Amount**
    - **Nudge to Select Unselected Funds**
    - **Edit Limit CTA**
    - **Proceed to Pledge with RTA CTA**
3. **Edit Limit Pop-up**
    - **Select Credit Limit**
    - **List of Selected Folios**
    - **List of Available Folios**
    - **Select Folio CTA**
    - **Proceed to Pledge with RTA CTA**

## Analytics

### Amplitude Events:

- **Pending**

### Reporting Metrics:

- Number and percentage of pledge errors reduced due to KFIN portfolio refresh.
- Success rate of pledge step post-release for CAMS.
- Distribution of pledge success rate by folio for CAMS.
- Number of pledge errors reduced due to CAMS portfolio refresh.
- Success rate of pledge step post-release for KFIN.
- Overall pledge step success rate post-release.
- Fallback error report for unhandled errors.

## Timeline & Release Planning

*Details to be determined based on project scope and resource availability.*

## Roadmap

### Future Enhancements:

1. **Integration of KFIN LAMF V2:** To enable folio-level error handling for better user experience.
2. **MFC Lien Validation API:** To improve validation accuracy and reduce pledge errors.

## Go to Market

### Marketing

*Details to be developed based on the final solution and target audience.*

### Ops & Sales Training

*Training modules to be created to educate ops and sales teams on new error handling processes and user support protocols.*

### Frequently Asked Questions (FAQs)

*Develop a comprehensive FAQ section addressing common pledge errors and user actions.*

## Action Items / Checklist

- [ ]  **Product**
    - [ ]  Finalize PRD
    - [ ]  Align with stakeholders
- [ ]  **Business**
    - [ ]  Obtain sign-off on requirements
- [ ]  **Design**
    - [ ]  Complete all scenario handling
    - [ ]  Finalize UI components
- [ ]  **Engineering**
    - [ ]  Resolve backend issues causing pledge errors
    - [ ]  Implement logic for RTA prioritization and refresh
    - [ ]  Configure error messaging to frontend
    - [ ]  Integrate reporting and analytics
    - [ ]  Share backend-related RCAs for pledge errors
    - [ ]  Share frontend-related RCAs for pledge errors

## Feedback

*Placeholder for ongoing feedback from stakeholders and users post-implementation.*

## Learnings & Next Steps

*To be updated based on project progression and post-launch insights.*

## Appendix

### Limitations

- **KFIN Error Granularity:** KFIN LAMF V1 API does not provide folio-level errors, limiting specific error handling. This will be addressed with LAMF V2 integration.

### Meeting Notes

- **Primary Focus:** Address unit mismatch errors through portfolio refresh prompts and API enhancements.
- **Strategies:**
    1. **Pre-Pledging Validation:** Utilize MFC lien validation API to check available units before pledging.
    2. **Post-Error Handling:** Enable users to refresh portfolios upon encountering errors.

### API Details

### Lien Validation API Request

```json
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

### Lien Validation API Response

```json
{
    "reqId": "2451478",
    "pan": "AZHPR1374G",
    "pekrn": "",
    "mobile": "7904530323",
    "email": "",
    "clientId": "sampleClientId",
    "lenderCode": "123",
    "pending": [],
    "errors": [],
    "success": [
        {
            "rtaName": "CAMS",
            "lienRefNo": "18409",
            "schemeDetails": [
                {
                    "amc": "T",
                    "folio": "3591684",
                    "schemeName": "",
                    "isin": "INF277K014C0",
                    "itemNo": "",
                    "lienUnits": "3"
                }
            ]
        }
    ],
    "validateId": "2451478"
}

```

### Lien Validation API Documentation

[MFCentral LAMF API Document](https://prod-files-secure.s3.us-west-2.amazonaws.com/7dffccbf-7070-46c0-8cf4-47741d25871e/bb5f1468-3ace-435b-b9fe-cda4c834c104/MFCentral_LAMF_API_document_for_1.7_(2).pdf)

### Lien Validation Criteria

| Criteria | Result | If Fails |
| --- | --- | --- |
| Number of folios in request matches response | - | Refresh Portfolio |
| Unit quantity per folio matches response | - | Refresh Portfolio |
| Success response with given PAN and mobile | - | - |
| Success response with single lender code | - | - |
| Details in `errors[]` and `pending[]` | - | - |
| Validate already pledged units for both lenders | - | - |
| Validate locked units for both RTAs | - | - |
| Validation for AE/CS funds for both RTAs | - | - |
| Response for pre-pledging and post-pledging scenarios | - | - |

### Lien Validation API Scenarios

### Scenario 1:

1. User lands on pledge screen.
2. Lien validation API is called to validate folios.
3. Loading screen displayed: "Verifying your portfolio available for pledging."

**Case 1:** Mismatch in units found

- **Action:** Show "Folio changed" message and prompt to refresh both RTAs.

**Case 2:** Folio mismatch (e.g., ISIN mismatch)

- **Action:** Show "Folio changed" message and prompt to refresh both RTAs.

**Case 3:** MFC API success but empty response

- **Action:** Allow pledging → Trigger OTP for RTA 1 → If error occurs, prompt to refresh folio with RTA → Handle user drop-off appropriately.

**Case 4:** API failure

- **Action:** Allow pledging → If RTA error occurs, prompt to refresh portfolio.

### Scenario 2:

1. User lands on pledge screen.
2. Lien validation API validates folios.
3. Loading screen displayed: "Verifying your portfolio available for pledging."
4. No mismatch found.

**Case 1:** No mismatch but RTA returns auth or validation error

- **Action:** Prompt user to refresh portfolios with both RTAs.

### Handling on UI if Errors Occur

- **General Approach:** For any errors, prompt users with a generic message to refresh their folio. Specific error details are not displayed to avoid confusion due to multiple possible errors in a single request.
- **Post-Refresh Scenarios:**
    - **CAMS:**
        - If updated limit is ₹0, prompt to proceed with KFIN if available.
        - If updated limit ≥ ₹25K, allow pledging with CAMS.
        - If updated limit < ₹25K, check KFIN limits and guide accordingly.
    - **KFIN:**
        - Similar prompts based on updated limits and availability of funds.

## Feedback

*Feedback mechanisms to be established post-implementation to gather user insights and identify areas for further improvement.*

## Learnings & Next Steps

*Document learnings from the implementation and outline subsequent steps to enhance the pledge process further.*

## Appendix

### Limitations

- **KFIN API Granularity:** KFIN LAMF V1 API lacks folio-level error reporting, limiting precise error handling. This limitation will be mitigated with the integration of KFIN LAMF V2 API.

### Meeting Notes

**Primary Focus:**

- Addressing unit mismatch errors by prompting users to refresh portfolios and enhancing API validation.

**Strategies:**

1. **Pre-Pledging Validation:** Utilize MFC lien validation API to verify available units before pledging.
2. **Post-Error Handling:** Enable portfolio refresh prompts upon encountering errors during pledging.

**Error Handling Insights:**

- CAMS provides folio-level errors, enabling specific user prompts.
- KFIN currently offers request-level errors; folio-level error handling will be enhanced with LAMF V2 integration.

### API Details

**Lien Validation API Request Example:**

```json
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

**Lien Validation API Response Example:**

```json
{
    "reqId": "2451478",
    "pan": "AZHPR1374G",
    "pekrn": "",
    "mobile": "7904530323",
    "email": "",
    "clientId": "sampleClientId",
    "lenderCode": "123",
    "pending": [],
    "errors": [],
    "success": [
        {
            "rtaName": "CAMS",
            "lienRefNo": "18409",
            "schemeDetails": [
                {
                    "amc": "T",
                    "folio": "3591684",
                    "schemeName": "",
                    "isin": "INF277K014C0",
                    "itemNo": "",
                    "lienUnits": "3"
                }
            ]
        }
    ],
    "validateId": "2451478"
}

```

**Lien Validation API Documentation:**[MFCentral LAMF API Document](https://prod-files-secure.s3.us-west-2.amazonaws.com/7dffccbf-7070-46c0-8cf4-47741d25871e/bb5f1468-3ace-435b-b9fe-cda4c834c104/MFCentral_LAMF_API_document_for_1.7_(2).pdf)

### Lien Validation API Criteria

| Criteria | Result | If Fails |
| --- | --- | --- |
| Number of folios in request matches response | - | Refresh Portfolio |
| Unit quantity per folio matches response | - | Refresh Portfolio |
| Success response with given PAN and mobile | - | - |
| Single lender code success response | - | - |
| Details in `errors[]` and `pending[]` | - | - |
| Validate already pledged units for both lenders | - | - |
| Validate locked units for both RTAs | - | - |
| Validation for AE/CS funds for both RTAs | - | - |
| Response for pre-pledging and post-pledging scenarios | - | - |

### Lien Validation API Scenarios

### Scenario 1:

1. User navigates to the pledge screen.
2. Lien validation API is triggered.
3. Loading screen displays: "Verifying your portfolio available for pledging."

**Case 1:** Unit mismatch detected

- **Action:** Display "Folio changed" message and prompt to refresh both RTAs.

**Case 2:** Folio mismatch (e.g., ISIN mismatch)

- **Action:** Display "Folio changed" message and prompt to refresh both RTAs.

**Case 3:** MFC API success but empty response

- **Action:** Allow pledging → Trigger OTP for RTA 1 → If error, prompt to refresh folio with RTA → Handle user drop-off.

**Case 4:** API failure

- **Action:** Allow pledging → If RTA error occurs, prompt to refresh portfolio.

### Scenario 2:

1. User navigates to the pledge screen.
2. Lien validation API confirms folio validity.
3. Loading screen displays: "Verifying your portfolio available for pledging."
4. No mismatches detected.

**Case 1:** No mismatches but RTA returns auth or validation error

- **Action:** Prompt user to refresh portfolios with both RTAs.

---

## questions

- Do these list cover all the Error codes form KFIN , CAMS,
- After error identification , can we  or are we passing the information ot Support in case ticket creation is needed .
-