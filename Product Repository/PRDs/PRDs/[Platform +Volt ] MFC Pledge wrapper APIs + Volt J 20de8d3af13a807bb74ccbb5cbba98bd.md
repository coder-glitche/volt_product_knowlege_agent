# [Platform +Volt ] MFC Pledge wrapper APIs + Volt Journey

: Saksham Srivastava
Created time: June 9, 2025 2:02 PM
Status: In progress
Last edited: July 30, 2025 3:55 PM

# **What problem are we solving?**

Currently LSPs pledge funds through RTA wrapper APIs. This means that for end customer to pledge mutual funds, customer requires to provide 2 separate OTPs one for each RTA. 

This can be solved by providing LSPs an option to pledge mutual funds via MFC with single OTP.

Pledging through two RTA also has a cost implication, pledging via MFC will reduce the pledging cost to half of the current cost. 

---

# **How do we measure success?**

1. Speed and ease of integration for LSPs.
2. Bugs, issues, or errors while LSPs integrate the pledge wrapper API. 

---

# **How are others solving this problem?**

 

---

# **What is the solution?**

## Requirements overview

## User stories / User flow

LSPs will be able to pledge mutual funds of customers in two ways:

1. Using pledge Wrapper APIs.
2. Using DSP child credentials to call MFC APIs independently. 

For method #1 -  Pledge wrapper APIs, following would be the flow: 

1. Call the pledge wrapper APIs with necessary details and MFC as the “provider”.
2. In the response of Trigger OTP API, LSP will get a UtilityRefId. 
3. This UtilityRefId can be used to get the status of pledging request. 
4. For collateral addition, the same UtilityRefId can be passed in the submitOpportunity v2 API to get the collaterals mapped to customer loan account. Through this LSP can skip calling the add collateral API separately. 
5. In case LSP does not send pledge utility ref ID in the submit opportunity, LSPs can still call the add collateral v1 or v2 APIs to add collateral to customers loan account. In v1 API they will be required to send complete body with mutual fund details, and in v2 API they can call the API with just the utility ref id to get the collateral added. The add collateral API should be called post submit opportunity is successful. 
6. In cases of errors, DSP will send adequate error messages to the LSP. We will create a map of what are the errors that we send LSP in case we receive particular error messages from MFC. In case, we receive an error message that is not accounted for in the map we will send the exact error message received from MFC to LSP. Error mapping given here. 

For method #2 - DSP child credentials, following would be the flow:

1. LSP to call the MFC APIs (submitLien, verifyLien, investorConsent) independently using DSP child credentials. 
2. All encryption, decryption and error handling will be managed directly by the LSP. 
3. LSP will have to call v1 add collateral API post submit opportunity to get the collateral added to customer’s loan account. 

### MFC error messages and mapping

Following are the error messages and their expected handling that we can receive in from the validateLien API. 

| Error Type | Error Message from MFC | Reason for the error | Error message to be given to LSP | Step |
| --- | --- | --- | --- | --- |
| Fund-level | No free units available | Customer has no lien eligible units for the given scheme | No units available for pledging under the selected scheme. | Pledge |
| Root-level | Unable to verify KYC Status | KYC status of the customer is not “KYC validated” | Investor KYC is not updated. Please update investor KYC.  |  |
| Root-level | Fatca Not Verified | FATCA is not verified; user needs to get their FATCA verified with RTAs/ AMCs | FATCA compliance is pending.  |  |
| Fund-level | Status Description is not valid | **To be understood.**  | The status of the folio could not be verified.  |  |
| Fund-level | Invalid Folio Details, Data not found | Folio details of the customer not found or are incorrect.  | The folio details provided are incorrect or do not exist. |  |
| Fund-level | Request not Allowed as one of the folio is NRI | Customer is not an Indian resident.  | This folio belongs to a non-resident (NRI) customer and cannot be pledged. |  |
| Fund-level | Investor Information is not valid | Mobile number does not match the given folio | The mobile number provided does not match the one linked to the folio. |  |
| Fund-level | Request not Allowed as the folio is Under Cooling Period | Mobile number/Email or other KYC change done recently by the customer. Example, mobile number change in Nippon AMC means that the particular funds can not be pledged for a cooling period of 6 months | This folio is under a mandatory cooling period due to recent KYC detail changes. |  |
| Fund-level | Given folio not match with given PAN | PAN passed in request and folio do not match | The PAN provided does not match the PAN linked to the folio. |  |
| Fund-level | Pass lien units less than or equal to available balance | Units passed in the request are higher than lien eligible units available for the customer.  | The requested units exceed the number of units available for lien marking |  |
| Fund-level | Mobile number is not linked to the folio(s) of this PAN | A different mobile number is linked to PAN’s folios | The mobile number provided is not linked to any folio under this PAN.  |  |
| Fund-level | There is no available balance to the mark the lien in the given folio and scheme | User has no units for the given folio | The customer has no units in the selected folio and scheme pledge. |  |
| Fund-level | ISIN is not applicable for lien marking | Lien is not allowed by AMC for this particular ISIN | The AMC does not allow lien marking for the selected mutual fund.  |  |
| Fund-level | Scheme is not mapped to your clientid | Scheme is not whitelisted for the ClientID shared in the request | The scheme is not whitelisted for lien marking by the lender.  |  |
- LSPs should be provide with root level and fund level errors. All the fund level errors should be provided in the response body of “Trigger OTP for Pledge” APIs.
- The error mapping should be kept flexible and easy to update/add new error messages as our understanding of error messages improves.

## Requirements

### Data requirements

**DSP Pledge wrapper Data requirement:**

To track success rates of pledging through pledge wrapper APIs, we should store the following data in a table that the data team can build insights upon: 

1. Success/failure status of each pledge request.
2. Success/failure status of each add collateral request.
3. No of folios being pledged in each pledge request.
4. No of folios where validateLien was successful. 
5. No of folios where validateLien was unsuccessful.
6. Root/Request level error message. 
7. Folio level error messages in a request. 

**Volt pledge flow amplitude requirement [WIP]:**

Will be filled post design finalisation of MFC pledge flow on Volt side. 

### Leadsquared requirements [WIP]

Currently, the events passed to LSQ for pledge are as follows:

1. Portfolio Pledge Started
2. MF Pledged via CAMS
3. MF Pledged via KFintech

With the introduction of MFC Pledge, this will become the default pledge method. As a result, a significant number of pledges will now be initiated via MFC by default. Subsequently, if required, users may opt for alternate pledge methods (CAMS/KFintech).

With the introduction of MFC Pledge as the default method, the updated event flow to be passed to LSQ should be as follows:

**Primary Flow:**

- `Portfolio Pledge Started`   → `MF Pledge via MF Central` → `Portfolio Pledge Complete`

**Fallback Flow (in case of MFC failure):**

- `Portfolio Pledge Started`   → `MF Pledge via MF Central` → *Error* → `MF Pledged via CAMS` → `MF Pledged via KFintech` → `Portfolio Pledge Complete`

This ensures that pledge completion is tracked accurately regardless of the route taken and appropriate CRM activities are triggered at each step.

### Design requirements

For MFC pledging on Volt.

- On the **Pledge step**, the user must choose the source platform for pledging.
- Present this selection **similar to the MF fetch step** (source selection UI pattern).
- Scenarios for pledge sources option shown to the customer:

| Customer's Eligible Fund Sources | Options Shown in UI |
| --- | --- |
| CAMS + KFin | Pledge via MFC (default), Pledge via CAMS & KFin |
| Only CAMS | Pledge via MFC (default), Pledge via CAMS |
| Only KFin | Pledge via MFC (default), Pledge via KFin |
- **MFC should be the default option** for pledging.
- Customers and MFDs can **explicitly switch** to CAMS/KFin if preferred.
- CAMS OTP trigger animation is outdated and incorrectly implies OTP is sent via email. We should correct and standardise it across MFC, CAMS and KFin pledge.
- The MFC pledge flow will be same as current RTA pledging.
    - Customer initiated MFC pledge.
    - OTP is triggered
    - Customer enters OTP
    - Pledge is completed
- Currently, we refetch customer’s portfolio is case customer encounters any error on the pledge step. Similarly for MFC pledge, in case there are any fund level errors in the validateLien API, the customer will refetch holdings and try to pledge again. Check the current handling in the attached [video](https://drive.google.com/file/d/1tQc7gQQQ29HQRj0BAEAnVR9vYVNwT__t/view?usp=sharing). Will have to improve the messaging and standardise this across MFC, CAMS and KFin refetch.
- If the user is facing error, the user should be able to try pledge via RTA as well.

### GTM requirements

GTM requirements are [here](https://docs.google.com/spreadsheets/d/1b9eGxjoxCzmOx7ku6KFRcZ-4sWtyksfml9F6HZvX2Dg/edit?usp=sharing). 

### Volt requirements [WIP]

Volt BE requirements.

- Flag to switch to RTA pledge in case of MFC pledge failure.
- Support CAMS, KFin fetch → MFC pledge

Volt FE requirements. 

- 

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

Updated API documentation: 

[LAMF_Updated 4.docx](%5BPlatform%20+Volt%20%5D%20MFC%20Pledge%20wrapper%20APIs%20+%20Volt%20J/LAMF_Updated_4.docx)