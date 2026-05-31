# DSP: PhonePe LSP Integration

: Gautam Mahesh
Created time: January 29, 2025 1:35 PM
Status: In progress
Last edited: January 30, 2025 1:26 PM

# Context

# Journey

## Application

### KYC

- Customer initiates the KYC flow through DL on the PhonePe TPAP
- PhonePe calls their internal DL KYC API managed by their KYC platform team
- The PhonePe internal KYC API calls Signzy DL integration
- The customer is shown the UI of DL on the TPAP
- The customer is redirected to the DL page and completes the journey
- PhonePe KYC team receives the KYC datapoints from DL through Signzy
- PhonePe lending team receives the KYC datapoints from their KYC team
- PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md).
- DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure

### Mandate

## Servicing

# Integration

## KYC

- PhonePe’s DL account is at PhonePe level (parent entity)
- DSP finance can get a sub-account under the above account

Open points.

- Can Signzy trigger an independent webhook to DSP’s endpoint?
- Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity?

| Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory |
| --- | --- | --- | --- | --- |
| { |  |  |  |  |
| "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory |
| "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory |
| "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory |
| "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory |
| "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory |
| "AddressLine1P": "Bhayander", |  | 255 | Varchar | Mandatory |
| "AddressLine2P": "Thane", |  | 255 | Varchar | Non Mandatory |
| "PincodeP": "400033", |  | 6 | Numeric | Mandatory |
| "kycType": "Digilocker", | Digilocker |  |  | Mandatory |
| "ekycId": "K13656433547667", | Digilocker id |  |  | Non Mandatory |
| "applicantFirstName": "Shankar", |  |  |  | Mandatory |
| "applicantLastName": "Paradkar", |  |  |  | Mandatory |
| "applicantMiddleName": "Ramesh", |  |  |  | Non Mandatory |
| "applicantDOB": "1994-02-11" |  | yyyy-mm-dd |  | Mandatory |
| } |  |  |  |  |
| } |  |  |  |  |

## Mandate

# Conversations

## KYC

On the KYC piece, please see below typical draft language in our LSP agreements with other lenders.

1. **Know your customer’ (“KYC”) Document collection services:**
The LSP shall provide the Lender with details of the Leads it has identified, along with all the required consent & customer background check data including collecting KYC Documents as per RBI regulated cKYC, Digilocker and Offline KYC [(O-KYC) and any other mode as allowed under Applicable Laws based on the Lender’s KYC policy. Lender shall ensure that their KYC policies are in compliance with the Applicable Law and regulations set out by the RBI. Lender hereby agrees that in the event there are any changes, amendments or modifications to its KYC policy, then it shall promptly inform the LSP to enable the LSP to comply with the revised KYC policy for providing the Services. LSP hereby agrees that it shall assist Lender, as an agent of Lender, with carrying out all necessary actions (excluding CKYC verification) in relation to the KYC checks of the Leads by collecting KYC Documents from the Leads. The Lender shall do its independent credit, background & KYC check and communicate its decision to the Lead through the LSP.

1. 1. **Know your customer’ (“KYC”) Document collection services:**

This is in line with the below clause of Sep'22 RBI guidelines on DLG, [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12382&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12382&Mode=0)

***2.5. Lending Service Provider (LSP):** An agent of a Regulated Entity who carries out one or more of lender’s functions or part thereof in customer acquisition, underwriting support, pricing support, servicing, monitoring, recovery of specific loan or loan portfolio on behalf of REs in conformity with extant outsourcing guidelines issued by the Reserve Bank.*

The below language in the DLG guidelines is as below.

**10.1.** REs shall ensure that any collection of data by their DLAs and DLAs of their LSPs is need-based and with prior and explicit consent of the borrower having audit trail. In any case, REs shall also ensure that DLAs desist from accessing mobile phone resources like file and media, contact list, call logs, telephony functions, *etc.* A one-time access can be taken for camera, microphone, location or any other facility necessary for the purpose of on-boarding/ KYC requirements only, with the explicit consent of the borrower.

### Interpretation

- DSP can accept KYC but the onus of verification is on us as an RE
- LSP can pass KYC data to us (not forbidden or a grey area)
-