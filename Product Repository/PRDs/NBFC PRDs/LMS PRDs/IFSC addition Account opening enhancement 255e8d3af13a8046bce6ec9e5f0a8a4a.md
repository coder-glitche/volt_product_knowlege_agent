# IFSC addition: Account opening enhancement

Last Edited: September 1, 2025 10:22 PM
PRD ETA: August 20, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?’**

Every day, over 200 customers apply for a loan. For 1–3 of these customers, the IFSC is missing in Finflux, our core lending platform. Currently, adding a missing IFSC requires raising a support ticket to the Finflux team, which takes 3–4 working hours.

This manual dependency directly delays account opening, increases operational overhead, and negatively affects the customer experience and turnaround time (TAT).

---

# **How do we measure success?**

- Account opening TAT
- Number of account opening stuck due to IFSC not being available in Finflux

---

# **How are others solving this problem?**

- Internal problem - Does not require benchmarking

---

# **What is the solution?**

We will be integrating with the Finflux add IFSC insert API, whenever a client creation is stuck due to a missing pin code exception, we will get details from Digio’s IFSC detail API to update into the LMS

## Requirements overview (optional)

## User stories / User flow

- User completes application
- LOS initiates client creation in LMS
- If client creation is successful, loan is created for the customer
- If client creation fails due to IFSC not existing in the LMS exception, we will get IFSC details using Digio’s IFSC API and hit the add IFSC API to add the IFSC code in the CLAW workflow.
- Post IFSC addition, we will create client again, and post line creation loan will be created

![image.png](IFSC%20addition%20Account%20opening%20enhancement/image.png)

## Requirements

Add IFSC API details:

```jsx
curl --location 'https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/ifsc' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eClwBKK6ukwBhuO4aYU9fShfc6M' \
--data '{
    "ifsc": "SBI1234119",
    "bankName": "Bank ABC",
    "branchName": "Branch XYZ",
    "bankAddress": "123 Street Name",
    "bankCity": "City Name",
    "micrCode": "MICR1234"
    
}'
```

Get IFSC details (Digio)

```json
curl --location 'https://api.digio.in/v3/client/kyc/verify/IFSC' \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'x-session: SIDDIHSKLFRLUVCEHTDFTRFLRFYJAZSB' \
--data '{"identifier":"SBIN0000813"}'
```

Response from Digio:

```json
{
  "verified": true,
  "data": {
    "ifsc": "SBIN0000813",
    "bank": "State Bank of India",
    "micr": "560002057",
    "branch": "BANGALORE",
    "centre": "BANGALORE URBAN",
    "address": "POST BAG NO.5310, STATE BANK ROAD, BANGLORE 560001",
    "district": "BANGALORE URBAN",
    "city": "BANGLORE",
    "state": "KARNATAKA",
    "neft": "true",
    "imps": "true",
    "rtgs": "true",
    "upi": "true",
    "penny_drop_bank": false,
    "iso3166": "IN-KA",
    "swift": "SBININBB169",
    "contact": "",
    "updated_at": "2022-07-11 13:03:28"
  }
}
```

**Mandatory fields:**

- ifsc
- bankName
- branchName
- bankAddress
- bankCity
- micrCode

| Parameter name | Value | Source | Type |
| --- | --- | --- | --- |
| ifsc | IFSC code | Bank verification utility | IFSC |
| bankName | Name of the bank | Digio API, key: bank | Free text field |
| branchName | Name of the branch | Digio API, key: centre | Free text field |
| bankAddress | Address of the bank branch | Digio API, key: address | Free text field |
| bankCity | City of the bank | Digio API, key: city | Free text field |
| micrCode | MICR code | Static | Free text field |

---

# **Design**

NA

---

# **Analytics**

- % of applications delayed due to IFSC (Day on Day)
- Account opening TAT

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

![image.png](IFSC%20addition%20Account%20opening%20enhancement/image%201.png)