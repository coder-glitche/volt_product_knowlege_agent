# API details

This API documentation outlines various attributes in both the **Request Header** and **Request Body** sections. Below, I will explain each attribute in both sections for a better understanding.

### Request Header Attributes

1. **Ocp-Apim-Subscription-Key** (String, Mandatory):
    - A unique subscription key required for accessing the API. This is a static key that needs to be obtained from the APIM Gateway authority.
2. **MOAuthorization** (String, Mandatory):
    - A dynamic authorization token (Mauth Token) that must be obtained and passed. This is managed by the respective authority and is not required if the request is initiated from an SFDC channel.
3. **Content-Type** (String, Mandatory):
    - Default value is `"application/json"`. It specifies the format of the data being sent.
4. **Authorization** (String, Mandatory):
    - An authorization token, typically OAuth2, used for accessing the API securely.

### Request Body Attributes

1. **XML_PACKET** (String, Optional):
    - Specifies whether CKYC XML Data will be included in the response. Default value is 'Y'. Possible values:
        - `'Y'`: XML Data will be included.
        - `'N'`: Only extracted fields will be returned.
2. **BITLY** (String, Optional):
    - Indicates whether a URL will be sent in the response or through SMS. Default value is 'N'. Possible values:
        - `'N'`: URL will be included in the response.
        - `'Y'`: URL will be sent via SMS.
3. **SOURCE_REQUEST_TIME** (String, Mandatory):
    - The timestamp of the request in the format `YYYY-MM-DD HH:MM:SS`.
4. **PROCESS_MODE** (String, Mandatory):
    - Indicates the mode of the process. Possible values:
        - `'UI'`: For user interface modes such as CKYC, OKYC.
        - `'API'`: Applicable when KYC Mode is CKYC.
5. **SOURCE_REQUEST_ID** (String, Mandatory):
    - A unique ID to identify the source channel request.
6. **APPLICATION_ID** (String, Optional):
    - A unique Application ID of the sourcing channel.
7. **CHANNEL_KEY** (String, Mandatory):
    - A static key that identifies the sourcing channel, obtained during the initial setup.
8. **CUSTOMER_ID** (String, Optional):
    - The customer identifier.
9. **POI_TYPE** (String, Optional):
    - Proof of Identity Type. Possible values include PAN, PASSPORT, UID, etc.
10. **POI_NO** (String, Optional):
    - The corresponding number for the specified POI type.
11. **DOB** (String, Mandatory):
    - Customer's Date of Birth in the format `YYYY-MM-DD`.
12. **CUSTOMER_TYPE** (String, Optional):
    - Customer type for reporting purposes. Possible values: New, Existing.
13. **FORCE_REFRESH_FLAG** (String, Optional):
    - Indicates whether to bypass the KYC search for an existing customer. Possible values: 'Y', 'N'.
14. **GENDER** (String, Optional):
    - Customer gender. Mandatory for Process Mode `'API'` and POI Type `'UID'`. Possible values:
        - `'M'`: Male
        - `'F'`: Female
        - `'T'`: Transgender
15. **SUBSCRIPTIONKEY** (String, Mandatory):
    - The subscription key value, required for accessing specific features.
16. **MOBILE** (String, Mandatory):
    - The 10-digit mobile number of the customer.
17. **FIRST_NAME, MIDDLE_NAME, LAST_NAME** (Strings, Optional):
    - First, middle, and last names of the customer. Mandatory only for Process Mode `'API'` and POI Type `'UID'`.
18. **SOURCE_IP_ADDRESS** (String, Mandatory):
    - The IP address from which the request is initiated.
19. **SESSION_TOKEN** (String, Optional):
    - An internal field for session tracking. No value expected from the sourcing channel.
20. **KYC_MODE** (String, Optional):
    - Specifies which KYC mode is used. Possible values: CKYC, OKYC, BIOMETRIC, FACEID.
21. **Form_DATA** (String, Optional):
    - Internal use, no value expected from the sourcing channel.
22. **Expiry_Date** (String, Optional):
    - Expiry date of the POI, mandatory for PASSPORT and DRIVING LICENSE types. Format is `YYYY-MM-DD`.
23. **BUSINESS, PRODUCT_CODE, CALLBACK** (Strings, Optional):
    - Attributes used to provide callback-related functionality. CALLBACK default value is 'N'.
24. **UPLOAD_OPTION** (String, Mandatory):
    - Indicates the type of document to be uploaded. Possible values:
        - `'All'`, `'POA'`, `'Photo'`, `'NA'`.
25. **LATITUDE, LONGITUDE** (Strings, Mandatory):
    - Latitude and longitude of the request.
26. **DEVICE_ID** (String, Mandatory):
    - Identifier for the device from which the request is sent.
27. **SOURCE_URI** (String, Mandatory):
    - URL of the source channel initiating the request.
28. **RETURN_URL** (String, Optional):
    - URL to which the KYC reference ID will be posted in UI mode.
29. **CONSENT_FLAG, CONSENT_DATE_TIME, CONSENT_IP_ADDRESS** (Strings, Optional):
    - Consent-related fields required if subscription key implies EKYC.
30. **BIOMETRIC_AADHAAR_NUMBER, BIOMETRIC_DATA** (Strings, Optional):
    - Used for biometric-based EKYC process. Includes Aadhaar number and biometric data in encrypted form.
31. **CLEVERTAP_CONFIG** (JSON Object, Optional):
    - Configurations for consuming clickstream information. This is passed to clevertap events.
32. **VERSION** (String, Optional):
    - The version of the response format. Used by certain subscriptions.
33. **RE_KYC** (String, Optional):
    - Indicates if EKYC OTP should be an option. Default is 'N'.
34. **USER_PHOTO, USER_PHOTO_ID1, USER_PHOTO_ID2** (Strings, Optional):
    - Attributes for sending photos in different formats for verification.
35. **LE_POI_TYPE, LE_POI_NO** (Strings, Optional/Conditional Mandatory):
    - Proof of Identity Type and Number for legal entities.
36. **AADHAAR_LAST_FOUR** (String, Optional):
    - Last four digits of Aadhaar for VID.
37. **LANGUAGE_CODE** (String, Optional):
    - Language for SMS communication. Default is English.
38. **VCIP** (JSON Object, Optional):
    - Attributes for initiating a Video KYC journey.
39. **AGENTID, ORGNAME, CHANNEL_URL** (Strings, Optional/Conditional Mandatory):
    - Fields for specifying the agent handling the journey and the channel's webhook URL for status updates.
40. **PRIORITY** (String, Optional):
    - Indicates priority of the journey: `'queue'` or `'standard'`.
41. **PNL** (String, Optional):
    - Product group for profit and loss for billing purposes.
42. **BRANCH** (String, Optional):
    - Name of the branch from which the request is made.
43. **TITLE** (String, Optional/Conditional Mandatory):
    - Mandatory for legal entities.
44. **PRODUCT_NAME** (String, Optional):
    - Name of the product involved in the Video KYC journey.
45. **NAME** (String, Optional):
    - Name of the customer who will perform the Video KYC journey.

These attributes provide a detailed description of the data that needs to be passed in the API request for the specific KYC process being performed.