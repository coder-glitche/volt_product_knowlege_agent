# [Lending stack] KYC Flow

: Saksham Srivastava
Created time: August 21, 2024 12:59 PM
Status: Not started
Last edited: October 11, 2024 4:17 PM

# **What problem are we solving?**

Complete KYC of the customer for DSP lender. For completing a successful CDD, following are the requirements as per regulations.

1. Proof of possession of Aadhaar number.
2. Verified E-document of Aadhaar (to be used as proof of address)
3. PAN should be verified fro mt hte issuing authority. 
4. PAN details/document (to be used as proof of identity). 

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

![Screenshot 2024-08-21 at 2.08.39 PM.png](%5BLending%20stack%5D%20KYC%20Flow/Screenshot_2024-08-21_at_2.08.39_PM.png)

If both PAN and Aadhaar are fetched from digilocker, all KYC requirements are met directly.

If PAN is not fetched from digilocker, we need the following to be completed.

1. PAN verification
2. PAN-Aadhaar seeding check

This will be done by using the signzy PAN extensive API. 

## Requirements

1. Pass PAN number for Digio digilocker init. Pick this from the PAN verification utility.
2. In case PAN is not fetched from digilocker, digio SDK should be exited. This can be achieved by using the “AADHAAR_PAN_KYC” workflow in digio.
3. In case PAN is not fetched from digilocker, call the PAN extensive API.
    1. Request: 
    
    ```
    {
        "panNumber": "KHUPS6329M", // PAN number of the customer
        "getStatusInfo": "true" //This should be sent true to get PAN verification status
    ```
    
    b. Response: 
    
    ```
    {
        "name": "Saksham Srivastava", // This should be stored as Name as per PAN
        "number": "KHUPS6329M",
        "firstName": "Saksham",
        "middleName": "",
        "lastName": "Srivastava",
        "typeOfHolder": "Individual or Person",
        "gender": "Male", 
        "isIndividual": true,
        "category": "person",
        "dateOfBirth": "11-06-1999", //This should be stored as Date of birth of the customer
        "maskedAadhaarNumber": "XXXXXXXX4049", // This will be used to check PAN-Aadhaar seeding status
        "emailId": "hss.harsh@gmail.com",
        "mobileNumber": "7376971700",
        "aadhaarLinked": true, // This will be checked while checking for PAN-Aadhaar seeding
        "address": {
            "fullAddress": "24 KANOONGOPURA, CHHOTI BAZAAR, QANOONGOPURA S.O, BAHRAICH, UTTAR PRADESH, - 271801",
            "addressLineOne": "24",
            "addressLineTwo": "Kanoongopura, Chhoti Bazaar",
            "street": "BAHRAICH",
            "city": "BAHRAICH",
            "state": "UTTAR PRADESH",
            "pincode": "271801",
            "country": "India"
        },
        "isValid": true,
        "panStatus": "VALID",
        "panStatusCode": "E" // This will be used for PAN verification status
    }
    ```
    
    c. cURL(staging) of the to test the API:
    
    curl --location '[https://api-preproduction.signzy.app/api/v3/panextensive](https://api-preproduction.signzy.app/api/v3/panextensive)' \
    --header 'Authorization: mJeBkv8NpCivJGiRsWYtpWiEb8I86YCG' \
    --header 'x-client-unique-id: [gautam.mahesh@voltmoney.in](mailto:gautam.mahesh@voltmoney.in)' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "panNumber": "KHUPS6329M",
    "getStatusInfo": "true"
    }'
    
4. Check for panStatusCode in the response,
    1. If panStatusCode==E: PAN of the customer is existing and valid
    2. If panStatusCode!=E: Consider PAN of the customer to be not verified. 
    
    User will be shown an error here.
    
5. Check the aadhaarLinked status,
    1. If aadhaarLinked==true: The PAN is linked to an aadhaar
    2. If aadhaarLinked!=true: The PAN is not linked to an aadhaar. 
    
    User will be shown an error here. 
    
6. Match maskedAadhaarNumber received from PAN extensive with the Aadhaar id_number received from Digilocker
    1. If match is true: KYC is success
    2. If match is false: Use will be shown an error. 
7. KYC Logs (This will be used in QC as well) **{This will be picked along with other logs and consent}**
    1. OVD:
        1. OVD type: Aadhaar
        2. OVD number: XXXXXXXX4049
        3. Document source: Digilocker
        4. Verification status: Verified
        5. Verification source: Digilocker
        6. Verified on: Timestamp of when was it verified (completedAt value from Digio)
    2. PAN:
        1. PAN details: PAN of the customer
        2. Document source: Digilocker/ NA
        3. Verification source: Digilocker/ Verification API
        4. Verification status: Verified
        5. PAN-Aadhaar seeding status: True
        6. PAN-Aadhaar seeding status source: Digilocker/ ITD API
        7. Verified on: Timestamp of verification

## Salutation and third gender handling:

1. For gender in 

---

# **Design**

1. Loader screen when Digio SDK is exited and PAN extensive API is called. 
~~Green hour glass lottie will be used.~~   The existing handling for Digio latency will work here as well. This will be an in line loader. @Bhavna Haritsa to update on this. 
2. Error modals: https://www.figma.com/design/4Jw8te9DVzKQbb6GovyCK2/Wireframes?node-id=1224-9138&node-type=FRAME&t=X3ME2uPDBP67NczV-11

| **Error case** | **Fenix error** | **Error to LSP** | **Modal to show** |
| --- | --- | --- | --- |
| **Aadhaar not seeded with PAN in signzy** | PAN_NOT_SEEDED | MISMATCH_DETECTED | 2 |
| **PAN is not verified** | INVALID_PAN | INVALID_PAN | 1 |
| **Aadhaar mismatch between digilocker and signzy** | PAN_AADHAAR_MISMATCH | MISMATCH_DETECTED | 2 |
| **PAN mismatch between digilocker and lead** | PAN_MISMATCH | MISMATCH_DETECTED | 2 |
| Age is below 18 years | AGE_BELOW_LIMIT | AGE_BELOW_LIMIT | 4 |
| Age is more than 70 years | AGE_ABOVE_LIMIT | AGE_ABOVE_LIMIT | 5 |

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