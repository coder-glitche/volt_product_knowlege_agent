# [Platform] Mandate collection enhancement

Last Edited: September 18, 2025 12:41 PM
PRD ETA: March 20, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

Our LAMF credit line product follows a balloon repayment model, which essentially means that the customer is only obligated to pay the interest as per their principal outstanding (which is accrued daily and posted monthly). 

There are multiple ways through which a user can pay this amount:

- Making a repayment on their lo ch the NBFC automatically deducts the amount from the user’s bank account)

What amount is collected from the user’s account?

- Charges due + Penal charges due + Interest due are collected on the 7th via mandate presentation

As we are a platform, there can come across use cases, where an LSP may want to control the repayment experience from the user (if they have capability to register as well as present mandates). The same scenario is with one of the LSPs (PhonePe).

Problem statement: Our platform should have a capability where the LSP can get what amount needs to be presented at a loan account level, present the mandate using their own capabilities and accordingly pass the details to the NBFC within the timeframe so that there is no penal charge implication for the user

---

# **How do we measure success?**

- Number of presentations / Total customers eligible for presentation
- Presentation success rate (Out of all the presentations, how many were successful)
- Number of loan accounts where mandate was presented, but details were shared late due to which there was an arrear and penal implication for the user (as a percentage of total successful presentations)

---

# **How are others solving this problem?**

- TCL and BFL control the mandate presentation for all users and does not offer the capability to the LSP to do mandate presentation

---

# **What is the solution?**

We will be enhancing our current mandate presentation workflow to support the use case where an LSP will control the mandate presentation for the users and will have the following capabilities:

- Get mandate collection file: Mandate collection file which is generated every month and then approved by the operations team will be available as a file (csv) through a get API (for all eligible loan accounts for presentation) to the LSP with approval status
- Mandate collection posting API: LSP will have the capability to pass the mandate collection response to the user (broadly there can be the following scenarios)
    - Mandate was presented and collected successfully (Success)
    - Mandate was presented but failed (Fail)
    - Mandate was not presented (Pending) - LSP will not call the API here
- Operations team should be able to track the progress of the presentation by the LSP in real time (Make response file in sync instead of post completion)
- Sourcing channel level handling for mandate collection file generation (+ CC support) @Karuna Sankolli will need design assistance here so that the operations team can distinguish between files for different sourcing channels.

## Requirements overview (optional)

NA

## User stories / User flow

Mandate file generation:

We will be using the current mandate file generation flow, however now a different file will be generated for customers sourced via sourcing channel “PhonePe”.

<aside>
🚨

Mandate files will get generated automatically on the first of the month at 10:00 AM

</aside>

Please note that these customers should not come in the generic mandate collection file generated for other LSPs (Groww/Volt/Indmoney)

<aside>
🚨

Mandate type for PhonePe will be “UPI_Mandate”

</aside>

Mandate file generation format (Sanitisation of parameters)

| Current value | Updated value |
| --- | --- |
| monthlyMandateCollectionBatchItemId | Mandate collection batch item ID |
| monthlyMandateCollectionBatchId | Mandate collection batch ID |
| loanAccountId | Loan account ID |
| amount | Total presentation amount |
| interestAmount | Interest amount |
| chargesAmount | Charge amount |
| penaltyChargesAmount | Penal charge amount |
| remarks | Remarks |
| umrn | Presentation UMRN |
| bankAccountNumber | Bank account number |
| bankAccountIFSC | Bank account IFSC code |
| mandateType | Mandate type (Will be UPI for PhonePe) |
| collectionSkipReason | Collection skip reason |
| mandateCollectionRequestId | Mandate collection request ID |
| utrNumber | UTR Number |
| mandateCollectionRequestStatus | Mandate collection request status |
| mandateCollectionRequestSubStatus | Mandate collection request sub status |
| statusNotes | Status notes |
| collectionRequestedOn | Collection requested on |
| completedOn | Completed on |
| isCollectionWaviedOff | Is collection waived off flag |
| collectionSkipped | Collection skipped flag |

PhonePe will be able to hit an API to get the collection request file:

- Only customers with sourcing channel of PhonePe should be a part of this file
- Mandate eligibility criteria to be same as currently configured
- Mandate collection amount criteria to be same as currently configured
- PhonePe will only get details of the presentation when the filed is approved by the operations team
- (PhonePe will hit the API on 5th to do a pre-debit for UPI mandates)

```json
GET /api/v1/{sourcing_channel}/collection-file

sourcing_channel (required): Identifies the sourcing channel for the collection data
collection_month (required): Month for which collection data is requested (format: 1-12)
collection_year (required): Year for which collection data is requested (format: YYYY)
```

### Error Responses

1. **400 Bad Request**
    - When required parameters are missing or invalid
    
    ```json
    json
    Copy
    {
      "status": "error",
      "code": "INVALID_PARAMETERS",
      "message": "Invalid or missing required parameters",
      "details": [
        {
          "param": "collection_month",
          "message": "Collection month must be between 1 and 12"
        }
      ]
    }
    
    ```
    

**404 Not Found**

- When the specified sourcing channel doesn't exist

```json
json
Copy
{
  "status": "error",
  "code": "SOURCING_CHANNEL_NOT_FOUND",
  "message": "The specified sourcing channel was not found"
}

```

**500 Internal Server Error**

- When the server encounters an unexpected error

```json
json
{
  "status": "error",
  "code": "INTERNAL_ERROR",
  "message": "An unexpected error occurred while processing your request"
}

```

**204 No Content**

- When no data is available for the specified parameters

```json
json

{
  "status": "success",
  "code": "NO_DATA",
  "message": "No collection data available for the specified parameters"
}

```

---

# **Design**

@Karuna Sankolli (CC enhancements to support multiple mandate files)

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