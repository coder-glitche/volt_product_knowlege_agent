# Tata Video KYC Integration V0

: Surya Ganesh
Created time: May 21, 2025 4:32 PM
Status: In progress
Last edited: July 3, 2025 10:08 AM

# **What problem are we solving?**

Tata Capital mandated the VKYC process to be completed for each new customer from 1st April 2025. With larger vision and deeper potential partnerships in the horizon, restarting the business with Tata Capital is required.

To do so, we need to implement Tata  Capital’s VKYC in our journey flow.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

Implementation of VKYC will cause significant rise in the drop-offs. With alignment from Tata, we can open the account without the customer completing the VKYC but it is mandatory for the customer to complete VKYC before raising a disbursement request.

For the initial launch (and till we observe stabilized funnels) we would be involving our Support team to help customers before and after (in cases of rejection/incomplete VKYC) with clear instructions and hand holding.

This is for the V0 launch only.

 

Note:

Tata’s Business Hour: 9AM - 6pm

[Activation: LSQ Task Creation](Tata%20Video%20KYC%20Integration%20V0/Activation%20LSQ%20Task%20Creation%20224e8d3af13a80c982dacebab3d9b6b0.md)

## Scope:

1.  Static VKYC CTA Banner on the Dashboard (similar to Elevate banner)
2. Admin action: Link generation + active link
3. LSQ task creation for follow-up calls
4. Disabling the withdraw button OR opening the VKYC instruction page (if in business hours) 
5. In-App iframe Implementation  - Open item
6. In-app VKYC Status Handling via bottom sheet (Back-End powered content) 

Out of scope for V0:

1. Pre-SDK launch device permission check: to be done on TCL’s end 
2. Redirection to settings page for device permissions
3. Whatsapp Reminders: In batches to the MFD and customer
4. Push Notifications
5. Redirection to setting page to enable device permissions (OS Depended)

## User stories / User flow

Following is the flow of the customer after completing the agreement step and Tata Capital account is opened (Miles APIs is are called)

1. After the agreement step, the customer is redirected to the dashboard if there is less than 15 mins left in business hour. If more than 15mins left in business hour, the customer continues to the VKYC Instructions Page
    1. Support: If 1 hour left in business hours, customer support connects with the customer/MFD and provides instructions and flow of the VKYC.
    2. Tech:
        1. The customer receives the VKYC completion link via WhatsApp along with instructions to follow after 15mins of completing account opening.  
            1. A banner with a CTA to complete the VKYC must appear on the dashboard. 
            2. Additionally, if the customer is redirected from the agreement step or clicks on the “Withdraw” or VKYC banner CTA outside of business hour, we display a bottom sheet explaining the business hour with a CTA button that reads "OK, I understand."
            
2. VKYC CTA opens the page with the instructions to be followed (our interface)
    
    Contents of Instruction Page:
    
    1. CTA to initiate the VKYC 
    2. Have device permission check which are required (mic, camera, speaker and location) and requesting the customer to have their original PAN card ready. CTA is only accessible if all device permissions are given.
    3. FAQs below the CTA with questions about W’s of VKYC, how to enable device permissions, and what Documents are required.
    
    Support: Will have access to the link incase the customer calls for support (not able to open link, redirection issue, etc). Link generation in case of rejection.
    
    Tech: 
    
    1. Empower support with the generated link which 
        1. will open the volt app to the permissions page
        2. when the customer clicks on the permissions page CTA, the new VKYC session should begin
    2. Allow link generation through admin action (required in the case where the customer is rejected). View and copy the link generated. Also, replace the VKYC link in-app for situations where the customer continues the journey in-app (does not use the link provided by the support). 
    
3. The customer continues to the iframe.
    
    This is the start of the TCL journey:
    
    Customer needs to gives the consent by clicking on the checkboxes and needs to pass all the device permission (mic, camera, location and speaker test). 
    

3a. The customer faces error:

- Agent not available
- Queue beyond permissible limit
- Out of business hours

1. Support: Support calls the customer on priority to request a re-try in business hour
2. Tech: 
    1. Send whatsapp message along with the CTA to the Volt app (opening the instructions page) requesting a retry in business hour
    2. On the application: Error bottom sheet with message to Retry again in business hour, CTA “Ok, I understand”. 

4. TCL journey continues:

1. Cx in queue (status updates to “waiting”), 
2. Agents gets assigned (Status updates to “agent-assigned”) 
3. Agent gets connected (No status update)

4a. If the Customer dropped-off after getting in the queue (Status: “waiting”)

4b. If the Customer dropped-off after connecting with the agent (Status: “agent-assigned”)

If the customer status remains “waiting“ or “agent-assigned” for 1 hour and there is 1 hour left in business hour, then:

1. Support: Calls up the MFD to understand the drop-off reason and request retry 
2. Tech: Whatsapp message requesting the customer to retry again in 

4b. If the agent logged off

If the customer status remains “agent-assigned” for 1 hour and there is 1 hour left in the business hour, then:

1. Support: Calls up the customer to understand the drop-off reason and request retry 
2. Tech: Error Bottom sheet requesting the customer to try again in business hour

5. Agent Actions:

5a. Unable: 

1. Support: Understands the reason and helps the customer retry solving the issue
2. Tech: Bottom sheet requesting the customer to retry.

5b.  Rejected:

1. Support: Requesting customer to retry and avoid the mistake last time
2. Tech: 
    1. Generate a new link using a new “tracking ID”. Whatsapp communications to request the customer to retry along with the VKYC link and try again message
    2. Push Notifications 

5c. Successful:

1. Support: Requests the customer to be patient and wait for auditor approval
2. Tech: 

6. Auditor Actions:

6a. Reopen:

1. Support: Requesting customer to retry and avoid the mistake made last time
2. Tech: Whatsapp communications to request the customer to retry along with the VKYC link. 

6b. Not Approved:

1. Support: Requesting customer to retry and avoid the mistake last time
2. Tech: Generate a new link using a new “tracking ID”. Whatsapp communications to request the customer to retry along with the VKYC link. 

6c. Approved:

1. Support: Inform the MFD
2. Tech: 

## Requirements:

### Tech:

Customer Handshake API: Used for generating the link

cURL:

```json
curl --location 'https://workappsoauth-uat-apicast.apps.tclnprdservices.tatacapital.com/rest/Workappsfe/v1.0/CustomerData' \
--header 'Content-Type: application/json' \
--header 'ConversationID: QWERT213' \
--header 'SourceName: VoltMoney' \
--header 'Cookie: 1b0d639f33ed2984e457a4bc1ce15058=7024ff2a1adff13a7ce2085adefd5539; 1b0d639f33ed2984e457a4bc1ce15058=7024ff2a1adff13a7ce2085adefd5539' \
--header 'OAuth: Basic OTY2OGMzY2E6NmJmZDFhODgwOTU3YTlmZmY0ZmJiYmMyMzgwZTU4M2Y=' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0aGRoU2xLc0cwajhkUGRoNHRtMlYtMHhoWnNMTUVEY3M2YTBpLXpPVmdZIn0.eyJleHAiOjE3NDkxMjYwMjcsImlhdCI6MTc0OTEyNTcyNywianRpIjoiZjFiNmYxYWEtYTMzYy00NTZkLWJkZWYtODE1M2IwYzE2MmE5IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5hcHBzLnRjbG5wcmRzZXJ2aWNlcy50YXRhY2FwaXRhbC5jb20vcmVhbG1zLzNzY2FsZS1zc28iLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiNzY4NjBkOWYtYjEwZS00YWE0LWEzOTctNTUxYTU5NTBhMDBlIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiOTY2OGMzY2EiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtM3NjYWxlLXNzbyIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxMC4xMjguMi4yIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LTk2NjhjM2NhIiwiY2xpZW50QWRkcmVzcyI6IjEwLjEyOC4yLjIiLCJjbGllbnRfaWQiOiI5NjY4YzNjYSJ9.rshVMf8Hw79S0Qsjy3ZfnKW-s88cpe6L7MBH8NdE4ZvfDGU_xWSWI1crlHQU85t84PNqKUxrPpkEPaTU44gM7XRwLLaSrcfcqhS9oaF2eBeNJbhqf2y8DRCKqGIbkvdNtJ10p0TxWPpAH_H7d5TrbG-IFTH1SEWmAlhpTR9fO8HDK9Sbbmj5q8mdwkQztfxxlBDJKzyXCn1iB8viP9MqiEPUfC0lKppHMJOLhmp-V32v7mje7zqcFP9SNdhDUjNUTi_j8oK8Xnv_JugpndHKeKDarc66hoaDSEDyweDzjWLMMI3ktcpmMqMuCiSqX2RXTK_III8VHT4FdzmASKCfpw' \
--data-raw '{
  "trackingId": "ABCD1234",
  "displayName": "Surya Ganesh",
  "welcomeMessage": "Hi... \nWelcome to the KYC process for Tata Capital. \nI recommend you to ensure a good network connection and keep your ID proofs ready before you proceed for video KYC as I will verify your documents over a video call. \nAlso, I request you to keep a pen and blank white paper ready with you for signature purpose.",
  "groupId": 100015,
  "flow": "Continuous",
  "product": "Loan Against Share/Loan Against Mutual Fund",
  "subProduct": "Loan Against Mutual Fund",
  "priority": 1,
  "userPhoto": "/BASE64",
  "data": [
    {
      "name": "WebTopId",
      "value": "291TZ0007250"
    },
    {
      "name": "OpportunityId",
      "value": "240134354925"
    },
    {
      "name": "OriginatingSystem",
      "value": "LAS_VoltMoney"
    },
    {
      "name": "KycType",
      "value": "DIGI"
    },
    {
      "name": "StatusEndpoint",
      "value": "342211"
    },
    {
      "name": "RedirectUrl",
      "value": "https://www.google.com"
    },
    {
      "name": "KYCDateTime",
      "value": "2025-06-05 13:22:23"
    },
    {
      "name": "JourneyType",
      "value": "Digi"
    },
    {
      "name": "NameAsPerPanCard",
      "value": "Surya Ganesh"
    },
    {
      "name": "DateOfBirth",
      "value": "2002-11-12"
    },
    {
      "name": "PANNumber",
      "value": "DKQPG8603E"
    },
    {
      "name": "FathersName",
      "value": "Ganesh Sankaraman"
    },
    {
      "name": "MothersName",
      "value": "Uttara Ganesh"
    },
    {
      "name": "DOBAsPerPanCard",
      "value": "2002-11-12"
    },
    {
      "name": "EmailID",
      "value": "suryaganeshdc@gmail.com"
    },
    {
      "name": "CustomerMobileNumber",
      "value": "9223427245"
    },
    {
      "name": "Gender",
      "value": "Male"
    },
    {
      "name": "CommunicationAddressFlag",
      "value": "true"
    },
    {
      "name": "CommunicationAddressLine1",
      "value": "D/O: Suryakant Purandare....."
    },
    {
      "name": "CommunicationAddressLine2",
      "value": "Hari Om Nagar"
    },
    {
      "name": "CommunicationAddressLine3",
      "value": "Mulund East"
    },
    {
      "name": "CommunicationAddressCity",
      "value": "Mumbai"
    },
    {
      "name": "CommunicationAddressState",
      "value": "Maharashtra"
    },
    {
      "name": "CommunicationAddressPinCode",
      "value": "400081"
    },
    {
      "name": "CommunicationAddressCountry",
      "value": "India"
    }
  ]
}
'
```

The CH API is the API used for generating the link of the VKYC. The request body needs the following details (mandatory fields):

- Tracking ID (webtop ID): Dynamic
- Webtop ID: Dynamic
- Opportunity ID: Dynamic
- welcomeMessage: Static
- Display name: Dynamic
- Originating system
- Product: Static (Loan Against Share/Loan Against Mutual Fund)
- Subproduct: Static(Loan Against Mutual Fund)
- flow: Static (Continuous)
- groupId: Static (100015)
- priority: Static (1)
- CommunicationAddressFlag: Static (True)
- CommunicationAddressLine1: Dynamic
- CommunicationAddressLine2: Dynamic
- CommunicationAddressLine3 (Can be “.” as well): Dynamic
- CommunicationAddressCity: Dynamic
- CommunicationAddressState: Dynamic
- CommunicationAddressPinCode: Dynamic
- CommunicationAddressCountry: Dynamic
- KYCTYPE: Static (DIGI)
- KYCDateTime: Dynamic
- Journeytype: Static (Digi)
- NameAsPerPanCard: Dynamic
- DateOfBirth: Dynamic
- PANNumber: Dynamic
- Fathersname: Dynamic
- DOBasperPAN: Dynamic
- EmailID: Dynamic
- CustomerMobileNumber: Dynamic
- userPhoto: Dynamic
- STATUSENDPOINT: Dynamic
- RedirectUrl: Static (Volt App link, to be made)
- Gender: Dynamic

**Sample RR logs:** 

[https://docs.google.com/document/d/1P6a1awis3gqqQtpdxaANvwvSiOitnF5aKIE7L91OMSg/edit?usp=sharing](https://docs.google.com/document/d/1P6a1awis3gqqQtpdxaANvwvSiOitnF5aKIE7L91OMSg/edit?usp=sharing)

Status API:

Used for getting the status of a VKYC application.

cURL:

```json
curl --location 'https://workappsoauth-uat-apicast.apps.tclnprdservices.tatacapital.com/rest/Workappsfe/v1.0/TrackingId' \
--header 'Content-Type: application/json' \
--header 'ConversationID: 123456789_16' \
--header 'SourceName: TrackingId' \
--header 'Cookie: 1b0d639f33ed2984e457a4bc1ce15058=7024ff2a1adff13a7ce2085adefd5539; 1b0d639f33ed2984e457a4bc1ce15058=7024ff2a1adff13a7ce2085adefd5539' \
--header 'Authorization: Bearer  eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0aGRoU2xLc0cwajhkUGRoNHRtMlYtMHhoWnNMTUVEY3M2YTBpLXpPVmdZIn0.eyJleHAiOjE3NDkxODg1NTAsImlhdCI6MTc0OTE4ODI1MCwianRpIjoiOTkwN2FlM2MtYzZiYS00OGZlLTg3ZmEtOTY5NGE5OTMyNTE1IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5hcHBzLnRjbG5wcmRzZXJ2aWNlcy50YXRhY2FwaXRhbC5jb20vcmVhbG1zLzNzY2FsZS1zc28iLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiNzY4NjBkOWYtYjEwZS00YWE0LWEzOTctNTUxYTU5NTBhMDBlIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiOTY2OGMzY2EiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtM3NjYWxlLXNzbyIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNsaWVudEhvc3QiOiIxMC4xMjguMi4yIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LTk2NjhjM2NhIiwiY2xpZW50QWRkcmVzcyI6IjEwLjEyOC4yLjIiLCJjbGllbnRfaWQiOiI5NjY4YzNjYSJ9.jhtnkFfUmNy6ESLC8nKrfJAXGWFMU3VG_ags-fM1MOiaYc04jh3Z0gd8u5ihptcwDlnB6IGoazust_LJTF7MPkg_x5L81Aw5Kwj1e4VLtwSwvLv5BXcuk9LGZbcAkJ8w_YWPbwu5WgCToEHVSea3oLDTtwPWTcCtR3KM1HYuGj2TqalZT9s7dM8X_qSNsE3pehB9_fwP2uVxl-3-f2lrdK7yrGmkFW9GJe8Op3KHHCjro0HfPV33b8U8eaD5zW-6-g_wyjJf2hj3sG_9R5tya3qxRD9GblpvxoZPYsu08LFGVLVuVqzoK1L60uHrWw-BqR8BU1PwQCQRhT3Te8TWIg' \
--data '{
    "trackingID":"ABCD1234"
}'
```

Sample RR Logs:

[https://docs.google.com/document/d/1Q4IA4l38TL9WbpLfaFXvdPffmrMNqaPML_rB6lCZgko/edit?usp=sharing](https://docs.google.com/document/d/1Q4IA4l38TL9WbpLfaFXvdPffmrMNqaPML_rB6lCZgko/edit?usp=sharing)

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