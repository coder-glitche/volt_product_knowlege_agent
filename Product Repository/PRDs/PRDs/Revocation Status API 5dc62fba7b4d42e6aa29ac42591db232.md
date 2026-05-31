# Revocation Status API

: Ameya Aglawe
Created time: August 30, 2024 5:49 PM
Status: In progress
Last edited: March 24, 2025 6:08 PM
Owner: Ameya Aglawe

# **What problem are we solving?**

- Un-pledging requests are processed by polling the holding statement to check if the lender has released the funds. However, if the Drawing Power (DP) isn't updated within 4 days, the status remains "In-progress" rather than automatically resolving.
- Ops teams have to manually update the un-pledging status by referring to the Lien report when the DP isn't updated, adding manual effort.
- Dependence on the Lien report is inefficient since it is often delayed by the lender, causing further delays in updating the un-pledge status.
- The current method of indirectly tracking un-pledge status demands operational bandwidth and involved process in-efficiencies

---

# **How do we measure success?**

- Reduction in number of un-pledging requests at “Requested” state
- Man hours of Ops team updating the status of un-pledging requests using admin tool

---

# **How are others solving this problem?**

---

# **What is the solution?**

- Implement a direct integration with the GetReleaseStatus API to retrieve the un-pledging status without relying on the get holding statement or Lien report

[Release Status.docx](Revocation%20Status%20API/Release_Status.docx)

[RevocationRequestStatusAPI.docx](Revocation%20Status%20API/RevocationRequestStatusAPI.docx)

## Requirements overview (optional)

### User stories / User flow

## Requirements

- API Functionality
    - Poll the status API every hour for a duration of 4 days. Polling should commence **1 hour** after the user submits the un-pledge request.
    - Request block
        
        
        | **Request**  | **Where we will get this data from**  |
        | --- | --- |
        | ReleaseStagingID | Get it in the response of Collateral release API |
        | LoanAccountNo | We store it in our system |
        | UserName | Adminaf |
    - Response block
        
        ```jsx
        {
        "GetReleaseStatus": [
        {
        "LoanAccountNo": "1022",
        "RecordStatus": "Success",
        "DetailedReleaseStatus": " Lien Release Complete ",
        "CustomerId": "387",
        "ReleaseStagingID": "12321-214123-12321321-33123"
        }
        ],
        "status": {
        "Status": "Success",
        "Code": "01",
        "Remarks": ""
        }
        }
        ```
        
    - **Note**
        - We will get staging ID against each of the funds that are requested for un-pledging by the user.
        - We will pick the staging ID for each of the funds and keep checking the status
        - Save collateral release API response
            
            ```jsx
            {
                "retStatus": "SUCCESS",
                "SaveCollateralRelease_Response": {
                    "CollateralReleaseData": [
                        {
                            "RespRemarks": "Success",
                            "RecordStatusCode": "0",
                            "UniqueRecordID": "707862234421866",
                            "StagingID": "EFC27C51-1565-4B60-98ED-7FCC75616549"
                        },
                        {
                            "RespRemarks": "Success",
                            "RecordStatusCode": "0",
                            "UniqueRecordID": "387806909141199",
                            "StagingID": "393F0EB7-DC12-4B8D-BB48-2C0E774A0752"
                        }
                    ],
                    "status": {
                        "Status": "Success",
                        "Remarks": "",
                        "Code": "01"
                    }
                },
                "sysErrorMessage": "",
                "sysErrorCode": ""
            }
            ```
            
        - API URL
            
            GetReleaseStatus : [https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/GetReleaseStatus](https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/GetReleaseStatus)
            
            Auth Key:
            
            voltmoney = Basic dm9sdG1vbmV5cHJvZDp2b2x0bW9uZXlwcm9k
            
- Status
    - The mapping will be done on the basis of recordStatus & DetailedRecordStatus
    - Status Mapping:
        
        
        | **Recordstatus**  | **DetailedRecordStatus** | **Action** | **Fund level status** |
        | --- | --- | --- | --- |
        | Rejected | -  | Stored Failed status | FAILED |
        | Pending | -  | Store Approval Pending status and keep polling  | APPROVAL_PENDING |
        | Success | Lien Release approval Pending | Keep polling | APPROVAL_PENDING |
        | Success | Lien Release Request Rejected by Lender | Store Failed status | FAILED |
        | Success | Lien Release Request in process | Store Approval Pending status and keep polling | APPROVAL_PENDING |
        | Success | Lien Release Failed  | Store Failed status | FAILED |
        | Success | Lien Release Complete | Store Success status | SUCCESS |
    - Terminal statuses are at fund level are SUCCESS, FAILED.
    - We will keep polling the status until we get the terminal statuses of each of the funds
    - Un-pledge level status
        - If any one the funds’ status is SUCCESS, we mark the status of un-pledge as SUCCESS
        - If status of all the funds are SUCESS then we store status as SUCCESS
        - If status of all the funds are FAILED then we store status as FAILED.
        - If we keep polling the API for 4 days every hour until we get the status of all the fund
    - In case all the fund status do not reach the terminal state at the end of the polling period then we store the status of un-pledge request as APPROVAL_PENDING
- DB storing
    - We will add one more column in the revocation request table which will store the combined status of all the funds in JSON format against each funds
    - Column name : revocationFolioDetails
        - ISIN
        - staging_ID
        - uniqueRecordID
        - status
    - Logging the partial success cases
        - We will log for the cases in which status of all the funds are not SUCCESS
            
            
            | Status of funds not with SUCCESS status | **Log**  |
            | --- | --- |
            | Other funds REJECT | The status of un-pledge request is PARTIAL_SUCCESS  |
            | Other funds with APPROVAL_PENDING (and polling period is over)  | The status of un-pledge request is APPROVAL_PENDING as few funds’ status is APPROVAL_PENDING and polling period is over |

Comment

---

# **Design**

---

# **Analytics**

---

- DB storing
    - We will add one more column in the revocation request table which will store the combined status of all the funds in JSON format against each funds
    - Column name : revocationFolioDetails
        - ISIN
        - staging_ID
        - uniqueRecordID
        - status
    - Logging the partial success cases
        - We will log for the cases in which status of all the funds are not SUCCESS
            
            
            | Status of funds not with SUCCESS status | **Log**  |
            | --- | --- |
            | Other funds REJECT | The status of un-pledge request is PARTIAL_SUCCESS  |
            | Other funds with APPROVAL_PENDING | The status of un-pledge request is PARTIAL_SUCCESS with few funds with APPROVAL_PENDING status |
            | Other funds with both REJECT & APPROVAL_PENDING status | The status of un-pledge request is PARTIAL_SUCCESS with few funds with APPROVAL_PENDING status |

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

- Understand the frequency of poll and the time of poll?
    - We start the polling one day later, poll in every 1 hour till next 4 days
- What happens if we don’t get the get the desired fund value within the polling timeframe
    - Then the un-pledging is kept an requested state, Ops team keeps a track of un-pledging request, they mark it as success & failed from admin action.

1st handling : 

- API Functionality
    - Poll the status API every hour for a duration of 4 days.
    - Given that the P90 time for status update is 78.63 hours, polling should commence 12 hours after the user submits the un-pledge request.
    - Request block
        
        
        | **Request**  | **Where we will get this data from**  |
        | --- | --- |
        | ReleaseStagingID | Get it in the response of Collateral release API |
        | LoanAccountNo | We store it in our system |
        | UserName | Adminaf |
    - **Note**
        - We will get staging ID against each of the funds that are requested for un-pledging by the user, we will just pick one of the staging IDs and check the status of the un-pledging.
        - As we get the status against this staging id we we mark the same status against all the other funds in the un-pledge request.
- Status and Failure Handling
    - Status Mapping:
        - Success – When the API call is successful, the un-pledge status in the database should be updated to "Success."
        - Rejected – If the API call fails due to validation issues, the status should be recorded as "FAILED" in the database.
        - Pending – If the API request is queued for execution, the status should be marked as "Approval Pending" in the database.
        In the case of a "Pending" status, polling should continue for up to 4 days.
    - API Failure Handling ***(De-prioritised)***:
        - End-of-day (EOD) checks on the holding data can serve as a fallback mechanism for updating the un-pledging status if the RevocationRequestStatus API fails.
        - This fallback has been ***de-prioritised*** following discussions with the tech team because:
            - Admin actions already serve as an adequate fallback for API failures, and introducing an additional fallback would result in unnecessary redundancy.
            - The implementation of this fallback would add technical complexity without any significant benefit.
- Given that the P90 time for status update is 78.63 hours