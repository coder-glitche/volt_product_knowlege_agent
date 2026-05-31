# [Platform] Liveliness check

: Vaibhav Arora
Created time: December 15, 2024 11:40 PM
Status: In progress
Last edited: December 26, 2024 2:13 PM

# **What problem are we solving?**

Users can pledge their collateral using our platform and can get a loan within 5 minutes. The process is completely digital and can be done via just an application or website.

To ensure fair use of our product, there are certain checks that need to be in place to avoid frauds for un-willing / unaware users. 

The same is proposed by RBI in their guidelines:

<aside>
💡

The RE must ensure that the Live photograph of the customer is taken by the authorized officer and the same photograph is embedded in the Customer Application Form (CAF). Further, the system Application of the RE shall put a water-mark in readable form having CAF number, GPS coordinates, authorized official’s name, unique employee Code (assigned by REs) and Date (DD:MM:YYYY) and time stamp (HH:MM:SS) on the captured live photograph of the customer.

</aside>

How do we currently ensure the same:

- OTPs are exchanged at core steps in the journey
    - Mobile and email verification
    - KYC (getting access to digilocker data)
    - Fetch with CAMS and KFIN
- Photograph (face match with KYC document)
- Quality checks (Clicked pictures are verified manually).

However we have seen instances in the past, where photos of photo have been captured which passed our face match criteria later to be identified by the lender (BFL/TCL/DSP). 

For such scenarios, the loan application is blocked till a valid photograph is shared with the lender, which impacts user experience and also introduces fraud risk into the system.

---

# **How do we measure success?**

- TAT for getting a loan (origination to approval)
- QC rejections based on invalid photographs (photo of photo)
- Number of applications where an non live photo was captured followed by a new event with a valid photograph

---

# **How are others solving this problem?**

There are various ways through which other organisations solve for this problem:

- Video KYC (VKYC flows)
    - Pros:
    High accuracy
    Users can be classified as low risk post doing a V-CIP
    Widely accepted by regulatory bodies
    - Cons:
    High development effort - More time to GTM
    High user friction - Impacts conversion metrics
    Operationally heavy (requires manual effort) - correspondingly higher TAT for application approvals
- Live videos (users are asked to share a video while speaking a designated phrase)
    - Pros:
    High accuracy
    - Cons
    High user friction - Impacts conversion metrics
    Operationally heavy (requires manual effort) - correspondingly higher TAT for application approvals
- Custom photographs (Users are asked to write a random number on a piece of paper)
    - Pros:
    High accuracy
    Low effort
    - Cons:
    Introduces relatively lower but additional friction for the users
    Operationally heavy - each image needs to be verified by the operations team
- Active liveliness checks (Camera)
    - Pros:
    Low development effort (ready to use solutions in market)
    Relatively lower, but high accuracy
    - Cons:
    Performance issues in lower end devices
    Increases complexity for partners integrating with us as LSPs
- Passive liveliness checks (Photo processing)
    - Pros:
    Very low development effort
    No additional friction for the user 
    Little to no manual intervention
    - Cons:
    May not be as accurate as other alternatives

---

# **What is the solution?**

We will be integrating with Digio’s passive liveliness check API which uses a base64 to identify the following checks:

- If there is a person in the image
- If the shared photograph is a live photo

What is a live photo?
When a customer clicks there photograph while actually being there in front of the lens - it is considered as a live photo. 

What is not a live photo?

- Photograph of a passport size picture
- Photograph of a screen (picture of person)
- Photograph of a person on a video call

## User stories / User flow

![image.png](%5BPlatform%5D%20Liveliness%20check/image.png)

## Requirements

The following table provides information on the parameters used in the request body for the API.

| Parameter | Mandatory or Optional | Description |
| --- | --- | --- |
| `image`  | Mandatory | Base64 |
| unique_request_id | Mandatory | Unique request id  |

Sample request:

```json
curl -X POST "https://api.digio.in/v3/client/kyc/analyze/file/liveness" \
 -H "accept: application/json"\
 -H "x-session: SIDWQVGRJKVFRBSTPHROOUOASDXFKRSB" \
 -F "image=@blurcheck.png"\
 -F "unique_request_id=1212"

```

Sample response:

```json
{
  "score": 0,
  "result": "FAIL",
  "errors": [
    "Eyes not found, Closed/wearing glasses"
  ]
}

```

**Responses:**

Score:

Confidence of image being live or real/acceptable. Higher the better

<aside>
💡

We will be placing a threshold score of 90 (for launch) and can later relax the scores as and when required (Note score will be in percentage that is score should be greater than equal to 0.90)

</aside>

result:

Result for the validation check (UNKNOWN is from Gray-area where manual verification can be done if you don't want customers to reattempt). Ideally consider Unknown also as Fail and ask user to reattempt.

Allowed: PASS┃FAIL┃UNKNOWN

<aside>
💡

We will only be accepting images if they pass the test

</aside>

errors
[string]
In case there are errors, list of errors found in image

List of error messages:

| Error message | Error code | Volt error message | Description | Handling |
| --- | --- | --- | --- | --- |
| Eyes not found, Closed/wearing glasses | EYES_CLOSED_OR_UNAVAILABLE | We could not detect your eyes in the captured photo. Please try again with better lighting and without glasses.
 | Eyes were either closed or not visible in the images | Hard reject |
| Closed eyes/wearing glasses, Please open your eyes. | EYES_CLOSED_OR_UNAVAILABLE | We could not detect your eyes in the captured photo. Please try again with better lighting and without glasses.
 | Eyes were either closed or not visible in the images | Hard reject |
| Detected photo of photo/phone, Please capture a live selfie. | PHOTO_OF_PHOTO | It looks like you used a photo or a screen. Please capture a live photo and try again. | Photo of a photo | Hard reject |
| Mouth not found, remove mask/hand/other obstacle. | FACE_MASKED | We could not detect a face in the captured photo. Please remove anything covering your face and try again. | Face of the customer is hidden/ not completely visible | Hard reject |
| Blurred image. Please retake your selfie in clearer lighting conditions. | BLURRED_PHOTO | We could not capture a clear photo. Please capture a clear photo under good lighting conditions. | Image submitted by the user is blurry | Hard reject |
| Multiple people found in image, Please keep others away and capture again. | MUTLIPLE_FACES_DETECTED | We detected multiple faces in the captured photo. Please ensure a clear background and try again. | Multiple people found in the image | Hard reject 

(Can discuss with business as this is a live photo, should we make it a soft acceptance?) |
| Any other message | LIVELINESS_FAILED | We could not capture a clear photo. Please capture a clear photo under good lighting conditions. |  |  |

| Status Code | Summary | Description | Handling |
| --- | --- | --- | --- |
| 422 | Face not detected | The model failed to detect a face in the selfie. | Reject photo - Hard retry (if face is not detected) - No additional documents |
| 429 | Rate limit error | You have exceeded the configured rate limit for transactions per minute. | Do not block customer - Take application through non STP flow |
| 5xx | Server Error | Kindly check the request headers or contact the HyperVerge team for resolution. | Do not block customer - Take application through non STP flow |

**Command Centre:**

New section will be added in the customer photo log with the following parameters:

QC:

Title Photo liveliness:

Face match validation: Yes/No

Confidence: High/Medium/Low

Provider: Hyperverge/Digio

Liveliness status

Liveliness score

Remarks

Deviation task:

Review details:

1. Review aadhaar photo
2. Review photo on supporting document
3. Review liveliness check details
    1. Live face check: Yes/No
    2. Confidence score: High/Medium/Low
    3. Provider: Hyperverge
    4. 
    
    Liveliness status
    
    Liveliness score
    
    Remarks
    

---

# **Design**

NA

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