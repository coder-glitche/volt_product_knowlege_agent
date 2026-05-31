# [Platform] Photo verification and liveliness check

: Vaibhav Arora
Created time: December 2, 2024 9:18 AM
Status: Done
Last edited: January 21, 2025 7:21 AM

# **What problem are we solving?**

It is important to ensure that the user who is going through the application journey submits there own verification documents and details (POA, POI and bank account). 

There are multiple checks in place currently in the system that ensure that:

- Customer Aadhaar PAN seeding check
- Selfie/Photo verification (not liveliness check) with their Aadhaar
- Name verification with bank account (Aadhaar/PAN)

Despite these checks, we have seen cases in the past when operating as an LSP where users were able to bypass this check by clicking a screenshot/someone else’s photograph in the photo verification flow and getting a loan (these were later reported by the lenders to the LSP).

We have also noticed limitations in Digio’s photo verification stack where the photo match operation was not very accurate

---

# **How do we measure success?**

- Number of cases where photo mismatch was incorrect (photo did not match) as a percentage of top of the line applications
- Number of cases where photo was correct but not of the user (screenshot/physical photograph) instead of a live user as a percentage of top of the line applications

---

# **How are others solving this problem?**

- Various NBFCs and LSPs use multiple checks to avoid such scenarios:
    - Photo liveliness check (physical - Slice): User is shown a text/number which they have to record or say out loud during the application process
        - Pros: Very accurate and difficult to game by fraudsters
        - Cons: Increases friction in the application journey / Manual checks (increases operational load internally to verify each application)
    - Custom photo verification (Physical - Zerodha): Users have to write a text (I consent that I am Vaibhav Arora or just their name) on a blank sheet of paper and click a photograph which is later verified by the operations/onboarding team
        - Pros: Very accurate and difficult to game by fraudsters
        - Cons: Increases friction in the application journey / Manual checks (increases operational load internally to verify each application)

---

# **What is the solution?**

We will be integrating with Hyperverge’s photo verification and liveliness check stack where the photo will be first matched and then will be checked by a model which verifies if it was a live photograph or a picture of a picture

## Requirements overview (optional)

Following are core requirements:

- Hyperverge integration
    - Authentication: Two ways through which it can be done
        - API key and secret (High risk / Low effort / Not configurable)
        - Auth token: Preferred (Lower risk / Higher effort / Configurable)
            - Can be beneficial for future LSP integrations if they have directly integrated with Hyperverge

## User stories / User flow

Consumer flow (corresponding LSP flow is defined separately)

![image.png](%5BPlatform%5D%20Photo%20verification%20and%20liveliness%20check/image.png)

## Requirements

![image.png](%5BPlatform%5D%20Photo%20verification%20and%20liveliness%20check/image%201.png)

Lifecycle of an application with Hyperverge

The result webhook is triggered whenever the application moves between the statuses as described above in the workflow:

### API to Subscribe to webhooks:

```json
Sample request:
curl --location POST 'https://review-api.idv.hyperverge.co/api/v1/config' \
--header 'appid:<Enter_the_HyperVerge_appId>' \
--header 'appkey:<Enter_the_HyperVerge_appKey>' \
--header 'transactionId: <Enter_the_HyperVerge_transactionID>' \
--header 'Content-Type: application/json' \
--data '{
    "webhookUrl": "https://webhook.site/dd42bf33-3b0d-4095-8953-b0e91ad312345",
    "events": [<Events Array>]
}'

Response:
{
    "statusCode": 200,
    "status": "success",
    "result": {
        "appId": "123456",
        "webhookUrl": "https://webhook.site/dd42bf33-3b0d-4095-8953-b0e91ad3191e",
        "created_at": "2022-01-09T12:50:34.544Z",
        "updated_at": "2022-01-09T12:50:34.544Z",
        "id": "1"
    }

```

Sample webhook payload:

```json
{
  "transactionId": "<Transaction_Identifier>",
  "applicationStatus": "manually_approved",
  "eventId": "<Event_Identifier>",
  "eventVersion": "1.0.0",
  "eventTime": "2023-01-30T1722.102Z",
  "eventType": "MANUAL_REVIEW_STATUS_UPDATE",
  "reviewerEmail": "<Sample_Email>"
}
```

UAT Credentials:

<aside>
💡

App ID: fyr7wn

App key: nntitne6i1drmlhiyk3e

</aside>

Request:

```json
curl -X POST https://sgp.idv.hyperverge.co/v1/checkLiveness \ 
   -H 'appId: xxx' \   
   -H 'appKey: yyyy' \ 
   -H 'transactionId: zzzz' \ 
   -H 'content-type: multipart/form-data;' \ 
   -F 'image=@image_path.png \ - base64 image needs to be passed (KYC image: Aadhaar)
```

Success response:

```json
{
  "status": "success", 
  "statusCode": "200", 
  "result": { 
 "details": { 
    "liveFace": { 
       "value": "yes"/"no", 
       "confidence": "high"/"low", 
        }, 
    "qualityChecks": { 
       "eyesClosed": { 
       "confidence": "high"/"low", 
       "value": "yes"/"no", 
         }, 
    "maskPresent": { 
       "confidence": "high"/"low", 
       "value": "yes"/"no", 
         }, 
    "multipleFaces": { 
       "confidence": "high"/"low", 
       "value": "yes"/"no", 
         }, 
    "blur": { 
       "confidence": "high"/"low", 
       "value": "yes"/"no", 
         } 
    } (optional), 
         }, 
    "summary" : { 
       "action" : "pass/fail/manualReview", 
       "details : [], 
         } 
}, 
"metaData": { 
       "requestId": "xxx", 
       "transactionId": "yyy", 
   }
}
```

Scenarios and respective handling:

| **Parameter** | **Confidence** | **Value** | **Description** | **Handling** |
| --- | --- | --- | --- | --- |
| liveFace | high/low | yes/no | Specifies if a live face is detected. | Value: Yes
Confidence: HIgh

Allow else disallow |
| eyesClosed | high/low | yes/no | Specifies if the subject's eyes are closed. | Value: Yes
Confidence: HIgh

Allow else disallow |
| maskPresent | high/low | yes/no | Specifies if a mask is detected on the face. | Value: Yes
Confidence: HIgh

Allow else disallow |
| multipleFaces | high/low | yes/no | Specifies if multiple faces are detected. | Value: Yes
Confidence: HIgh

Allow else disallow |
| blur | high/low | yes/no | Specifies if the image is blurry. | Ignore |
| summary.action | - | pass/fail/manualReview | Specifies the final action recommended based on the checks. | Pass: Allow
Fail: Retry
Manual Review: Not applicable  |
| summary.details | - | [] | Contains additional details about the summary (optional, currently unused). | Ignore |
| metaData.requestId | - | xxx | Unique identifier for the API request. | Request ID |
| metaData.transactionId | - | yyy | Unique identifier for the transaction associated with the API call. | Tranasction ID |

Sample error response:

```json
Face not detected:
{
  "status": "failure", 
  "statusCode": "422", 
  "metadata": { 
    "requestId": "xxx", 
    "transactionId": "yyyyy" 
  }, 
  "result": { 
    "error": "Face not detected" 
  } 
}

Rate limit error:
{
  "status": "failure", 
  "statusCode": 429, 
  "error": "Rate limit error"
}
Server error:
{
  "status": "failure", 
  "statusCode": "5xx", 
  "error": "Server Error"
}

```

| Status Code | Summary | Description |
| --- | --- | --- |
| 422 | Face not detected | The model failed to detect a face in the selfie. |
| 429 | Rate limit error | You have exceeded the configured rate limit for transactions per minute. |
| 5xx | Server Error | Kindly check the request headers or contact the HyperVerge team for resolution. |

Hyperverge also gives quality check responses in the image: (Discuss if this needs to be enabled for DSP):

| Quality Check | Description | Key in Response |
| --- | --- | --- |
| Eyes Closed Check | Check if eyes are closed | eyesClosed |
| Mask Check | Check if face in selfie is wearing a mask | maskPresent |
| Multiple Faces Check | Check if multiple faces are present in the selfie | multipleFaces |
| Blur Check | Check if face in selfie is blurred | blur |
| Hat Check | Check if face in selfie is wearing a hat | hat |
| Sunglasses Check | Check if face in selfie is wearing sunglasses | sunglasses |
| Reading Glasses Check | Check if face in selfie is wearing reading glasses | readingGlasses |
| Over Exposure Check | Check if face in selfie is over exposed | bright |
| Under Exposure Check | Check if face in selfie is under exposed | dull |
| Head Turned Check | Check if face in selfie is misaligned | headTurned |
| Low Quality Check | Check if quality of image is low | lowQuality |

---

# **Design**

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