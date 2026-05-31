# [Lending stack] Agreement execution flow

: Lalit Bihani
Created time: February 29, 2024 2:44 PM
Status: In progress
Last edited: November 12, 2025 1:01 PM
Owner: Saksham Srivastava

# **What problem are we solving?**

- Customer signing through platforms like Leegality and Digio has their own disadvantages. They don’t support clickwrap agreement making it hard for customers to sign on agreement.
- These vendors don’t provide the ideal flow which balances for regulation and cost of stamping.

---

# **How do we measure success?**

Below are the ways to measure success.

## Functional Metrics

- At least 95% of customers who complete the KFS step complete agreement
- Not more than 5% of customers reach out to us for queries

## Performance Metrics

- 95th percentile TAT for loading the agreement to be <5s including front-end
- Success rate for generating the agreement to be at least 99%
- Performance metrics to be maintained for at least 3 TPS
- All API hits to Leegality to be logged with request & response payloads
- All API hits to BE to be logged with request & response payloads
- Success rate for email sending to be at least 99%

## Guardrail Metrics

- 100% of stamped documents to be executed successfully
- 100% of signed agreements to capture IP and timestamp

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

1. On LSP, post customer completes pledge step. “Continue to review KFS” should be the CTA on pledge completion. 
2. Agreement document should be visible in the same webview where we showed KFS to the customer. Design: https://www.figma.com/design/Rez1MdgXywVoHo9ucwPimp/KFS?node-id=577-12321&node-type=section&t=9lEAfrfvMnmSC7sg-11
    1. Error modal designs have been shared in the design.
3. When the agreement is signed by the customer successfully. Fenix should send a webhook/response to LSP that the agreement is signed successfully.

## User stories / User flow

High level flow:

![Screenshot 2024-09-23 at 8.03.57 PM.png](%5BLending%20stack%5D%20Agreement%20execution%20flow/Screenshot_2024-09-23_at_8.03.57_PM.png)

**Note:** The min(3 days, customer placing a withdrawal req) logic from above flow is deprioritized for CUG launch. 

Detailed flow: 

| Flow | Tech implimentation | Notes |
| --- | --- | --- |
| Fenix will share a link that will be openend in webview on the LSP side. Customer will acknowledge on KFS first through clickwrap on this link. |  |  |
| - Before customer views the agreement, check for stamp inventory. If there are less than X unused stamps, give an error that customer can not sign the agreement right now.   | API to check stamp inventory: [https://docs.leegality.com/v3#tag/Stamp-Details-API/paths/~1v3.0~1series~1list/get](https://docs.leegality.com/v3#tag/Stamp-Details-API/paths/~1v3.0~1series~1list/get) 

**Response:**
- Check for state of Delhi there should be X unused stamps from any series. 
- If for the state of Delhi there are less than X unsused stamps, throw an error that customer can not sign the agreement for now. |  |
| - Loan kit will be opened in a document viewer in the same webview
- Customer will sign the agreement through clickwrap- Customer sign and timestamp to be affixed on bottom left of each page of the loan kit. Example:
Signed by Saksham Srivastava17 Sep 2024 23:04:05 IST |  | - FE design for agreement document viewer is pending. 
- Final template that will be used for agreement is pending.  |
| - Store this copy (Copy #1) of document. |  |  |
| - From Leegality, use "Customer copy of agreement” workflow. Another copy of the filled template (Copy #2) of the agreement must be used. The workflow will create a docsigner sign request. | API to create e-Sign request: [https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1request/post](https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1request/post) 

**Request:**
- Pass name of file: {{OPPID}}_LAS_customer_copy
- Pass profile ID of the "customer copy of agreement" workflow
- Pass base64 of the filled template (without customer/NBFC sign)
- Pass ____ for name in invitees object. [Open point on Leegality]
- Pass ____ for email in invitees object. [Open point on Leegality]
- We should pass an internal reference number in the irn field for internal tracking of document. This can be {{OPPID}}_LAMF_customer_copy. [Discuss with engineering]

**Response:**
- If status is 1, the workflow was successfully executed. Store the document ID. This will be used to download the completed document.- If status is 0, their was an error. Retry the flow and trigger an alert with the IRN and messages array on mail. - Store the signUrl from the invitees array, this will be used for esigning the request. | - Final name and email on invitees is blocked on class 2 docsigner procurement. |
| - NBFC to Sign on the above docsigner request. | API to sign on the docsigner sign request: [https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1docSigner~1invitation/post](https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1docSigner~1invitation/post) 

**Request:**
- send the signURL from above.
- send ____ profileId of the docsigner saved on Leegallity [Pending on DocSigner procurement and setup]
- In consent field send this exact string "By using this authenticated API and the ProfileID associated with this Document Signer Certificate, I agree that the Document Signer Certificate saved in this Account will be used to eSign documents for me. I also understand that recipients of such electronic documents will be able to see my signing details."

**Response:**
- If status is 1, the doc was signed successfully.
- If status is 0, their was an error. Retry the flow and trigger an alert with the messages array on mail. | - Profile ID of the docsigner is blocked on class 2 docsigner procurement |
| - Download above document from leegality and send it to the customer. | API to download document: [https://docs.leegality.com/v3#tag/API-3.3/paths/~1v3.3~1document~1fetchDocument/get](https://docs.leegality.com/v3#tag/API-3.1/paths/~1v3.1~1document~1details/get)

**Request:** 
- Pass document ID of the previous document in documentID parameter. 
- Pass true in the file parameter. 

**Response:**
- base64 of the document | - The document will be sent in a welcome email. Design and template setup for email is pending.  |
| - Convert the customer signed copy of agreement (Copy #1) to base64
- Send the base64 version for workflow "Stamp and DSP sign"

- The above flow will be triggered only when,
    - QC for the application is approved
    - ~~Customer places a withdrawal request, or 3 days after customer signed the agreement, whichever happens first.~~  This has been deprioritised for CUG testing. 

**- PLEASE NOTE
1. The agreement will not be stamped or countersigned before QC approval.
2. Customer will be able to place a withdrawal request but the request will be processed only after agreement is stamped and countersigned.**
 | API to create e-Sign request: [https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1request/post](https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1request/post) 

**Request:**
- Pass name of file: {{OPPID}}_LAS_executed_copy
- Pass profile ID of the "stamp and DSP sign" workflow
- Pass base64 of the customer signed copy of agreement from 4th event
- Pass ____ for stampSeries. [Open point on Leegality]
- Pass ____ for name in invitees object. [Open point on Leegality]
- Pass ____ for email in invitees object. [Open point on Leegality]
- We should pass an internal reference number in the irn field for internal tracking of document. This can be {{OPPID}}_LAMF_executed_copy. [Discuss with engineering]

**Response:**
- If status is 1, the workflow was successfully executed. Store the document ID. This will be used to download the completed document.- If status is 0, their was an error. Retry the flow and trigger an alert with the IRN and messages array on mail. - Store the signUrl from the invitees array, this will be used for esigning the request. |  |
| - NBFC to sign on above docsigner request | API to sign on the docsigner sign request: [https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1docSigner~1invitation/post](https://docs.leegality.com/v3#tag/Document-Execution-Platform/paths/~1v3.0~1sign~1docSigner~1invitation/post) 

Request:
- send the signURL from above.
- send ____ profileId of the docsigner saved on Leegallity [Pending on DocSigner procurement and setup]- In consent field send this exact string "By using this authenticated API and the ProfileID associated with this Document Signer Certificate, I agree that the Document Signer Certificate saved in this Account will be used to eSign documents for me. I also understand that recipients of such electronic documents will be able to see my signing details."

**Response:**
- If status is 1, the doc was signed successfully.- If status is 0, their was an error. Retry the flow and trigger an alert with the messages array on mail. |  |
| - Store this copy(copy #2) of document. | API to download document: [https://docs.leegality.com/v3#tag/API-3.3/paths/~1v3.3~1document~1fetchDocument/get](https://docs.leegality.com/v3#tag/API-3.1/paths/~1v3.1~1document~1details/get)

**Request:** 
- Pass document ID of the previous document in documentID parameter. 
- Pass true in the file parameter. 

**Response:**
- base64 of the document | - Confirm with Gautam for data redundancy
- Storage in RDS instead of S3: Both to be added to the roadmap.  |

Other notes:

1. Stamp inventory management will be an operational process. SOP for the same will be prepared. Alerts on inventory will be added in the roadmap. 

[Postman collection](%5BLending%20stack%5D%20Agreement%20execution%20flow/Postman%20collection%2010de8d3af13a804dac1fecc93067b0ab.md)

## Requirements

Audit trail requirement-

Capture the following when customer is signing the the agreement for audit trail:

1. Opp ID of the customer 
2. Agreement utility ID
3. IP of the customer 
4. Method of signing: Clickwrap
5. Device of the customer 
6. OS of the customer device
7. LSP: Volt Money

Performance requirement- 

1. Time taken to generate the loan kit should not exceed 5 seconds. 

---

# **Design**

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

Not needed at this moment stand-alone. To be done as an integrated stack post go-live.

## Ops & Sales training

- Training to be setup for sales & ops before CUG phase 1 go-live

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Setup training with Sales pre CUG go-live
    - [ ]  Setup training with operations pre CUG go-live
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  

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