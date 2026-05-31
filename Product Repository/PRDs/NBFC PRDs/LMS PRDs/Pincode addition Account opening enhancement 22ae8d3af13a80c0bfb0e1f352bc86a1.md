# Pincode addition: Account opening enhancement

Last Edited: July 11, 2025 5:11 PM
PRD ETA: July 8, 2025
PRD Owner: Vaibhav Arora
Status: Pending review

# **What problem are we solving?’**

Every day, over 200 customers apply for a loan. For 4–5 of these customers, the pincode is missing in Finflux, our core lending platform. Currently, adding a missing pincode requires raising a support ticket to the Finflux team, which takes 3–4 working hours.

This manual dependency directly delays account opening, increases operational overhead, and negatively affects the customer experience and turnaround time (TAT).

Why do we need to store pin codes in Finflux?
User’s state is important as a context in the LMS (Accounting module) to ensure that the GST that is applied on charges is accordingly distributed between CGST/IGST/UTGST/SGST

---

# **How do we measure success?**

- Account opening TAT
- Number of account opening stuck due to pincode not being available in Finflux

---

# **How are others solving this problem?**

- Internal problem - Does not require benchmarking

---

# **What is the solution?**

We will be integrating with the Finflux add Pincode API, whenever a client creation is stuck due to a missing pin code exception, we will get details from the user’s KYC details (KYC utility) to push into the LMS and retry account opening

## Requirements overview (optional)

## User stories / User flow

- User completes application
- LOS initiates client creation in LMS
- If client creation is successful, loan is created for the customer
- If client creation fails due to pin code not existing in the LMS exception, we will get user KYC details and hit the add pin code API to add the pin code in the CLAW workflow.
- Post pin code addition, we will create client again, and post line creation loan will be created

![image.png](Pincode%20addition%20Account%20opening%20enhancement/image.png)

## Requirements

Add pincode API details:

```jsx
curl --location 'https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/masters/pincode' \
--header 'Accept: application/json, text/plain, */*' \
--header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'Authorization: Bearer eClwBKK6ukwBhuO4aYU9fShfc6M' \
--header 'Connection: keep-alive' \
--header 'Content-Security-Policy: default-src '\''self'\''' \
--header 'Content-Type: application/json' \
--data '{
    "areaName": "Kalyan Nagar",
    "pincode": "571449",
    "taluka": "Example Taluka",
    "district": "Bengaluru",
    "state": "Karnataka",
    "country": "India",
    "latitude": 12.345678,
    "longitude": 98.765432,
    "isServicible": "true"
}'

```

**Mandatory fields:**

- areaName
- pincode
- district
- state
- country
- isServicible

| Parameter name | Value | Source | Type |
| --- | --- | --- | --- |
| areaName | city | KYC utility | Free text field |
| pincode | pincode | KYC utility | pincode (6 digits) |
| district | city | KYC utility | Free text field |
| state | state | KYC utility | Fixed list (Finflux) |
| country | India | Static | Free text field |
| isServicible | true | Static | Free text field |

Finflux state and KYC state mapping

| **State** | **KYC mapping (Digilocker)** |
| --- | --- |
| ANDHRA PRADESH | Andhra Pradesh |
| BIHAR | Bihar |
| TELANGANA | Telangana |
| RAJASTHAN | Rajasthan |
| PUNJAB | Punjab |
| ASSAM | Assam |
| UTTAR PRADESH | Uttar Pradesh |
| KARNATAKA | Karnataka |
| MADHYA PRADESH | Madhya Pradesh |
| JHARKHAND | Jharkhand |
| ODISHA | Odisha, Orissa |
| MAHARASHTRA | Maharashtra |
| GUJARAT | Gujarat |
| CHHATTISGARH | Chhattisgarh |
| TAMIL NADU | Tamil Nadu |
| WEST BENGAL | West Bengal |
| HIMACHAL PRADESH | Himachal Pradesh |
| HARYANA | Haryana |
| KERALA | Kerala |
| DELHI | Delhi |
| JAMMU AND KASHMIR | Jammu and Kashmir, Jammu & Kashmir |
| MEGHALAYA | Meghalaya |
| THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU | Dadra and Nagar Haveli |
| LADAKH | Ladakh |
| TRIPURA | Tripura |
| NAGALAND | Nagaland |
| PUDUCHERRY | Pondicherry, Puducherry |
| CHANDIGARH | Chandigarh |
| GOA | Goa |
| UTTARAKHAND | Uttarakhand |
| ARUNACHAL PRADESH | Arunachal Pradesh |
| MIZORAM | Mizoram |
| LAKSHADWEEP | Lakshadweep |
| ANDAMAN AND NICOBAR ISLANDS | Andaman and Nicobar Islands |
| MANIPUR | Manipur |
| SIKKIM | Sikkim |

---

# **Design**

NA

---

# **Analytics**

- % of applications delayed due to pincode (Day on Day)
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