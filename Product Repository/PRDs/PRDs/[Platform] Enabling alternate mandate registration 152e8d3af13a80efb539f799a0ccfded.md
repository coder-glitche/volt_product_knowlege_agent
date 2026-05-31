# [Platform] Enabling alternate mandate registration methods

: Vaibhav Arora
Created time: December 4, 2024 9:38 AM
Status: Done
Last edited: February 1, 2025 7:49 PM

# **What problem are we solving?**

As a part of the application flow, users have to register a mandate. While it is not mandatory, it is convenient for both the lender as well as the user to do so.

- **Convenient EMI Payments**: A mandate ensures automatic deduction of EMIs from the borrower's account, reducing the risk of missed payments.
- **Assurance for the Lender**: It provides the lender a reliable mechanism for repayment.

The mandate registration process requires the user to authenticate the registration on their bank account, NPCI allows the user to do so via three methods:

1. E-NACH 
    1. Debit card
    2. Net banking
    3. Aadhaar OTP
2. Aadhaar (E-sign)
3. Physical NACH form

Currently we support e-NACH capabilities to set up a mandate, within e-mandate there are certain banks who support specific authorisation methods (Debit card/NB/A-OTP). 

However a lot of users do not have access to, a debit card or a net banking account to authorise their mandate.

To support flows where the user is able to register a mandate, we will enable LSPs to register a mandate with the NBFC via other authorization methods:

1. Aadhaar (E-sign)
2. Physical NACH form

https://www.npci.org.in/PDF/nach/live-members-e-mandates/Live_Banks_in_eSign_26thOct20.pdf - Live bank list for E-NACH

https://www.npci.org.in/PDF/nach/live-members-e-mandates/Live-Banks-in-API-E-Mandate.pdf - Live bank list for Aadhaar e-sign

---

# **Why are we solving this?**

For more than 10% applications month on month (E-mandate set up has to be skipped for BFL)

| # | Month (2024) | Total Bajaj credits | Where mandate was skipped | % |
| --- | --- | --- | --- | --- |
| 1 | 1 | 794 | 82 | 10.33% |
| 2 | 2 | 735 | 60 | 8.16% |
| 3 | 3 | 939 | 181 | 19.28% |
| 4 | 4 | 206 | 62 | 30.10% |
| 5 | 5 | 332 | 81 | 24.40% |
| 6 | 6 | 991 | 169 | 17.05% |
| 7 | 7 | 1603 | 158 | 9.86% |
| 8 | 8 | 1462 | 112 | 7.66% |
| 9 | 9 | 1411 | 116 | 8.22% |
| 10 | 10 | 1852 | 164 | 8.86% |
| 11 | 11 | 1746 | 163 | 9.34% |
|  |  |  |  |  |
|  | **Total** | 12071 | 1348 | 11.17% |

Users then set up their mandate physically which is a cumbersome process:

[https://docs.google.com/spreadsheets/d/1E-7SYqBmzdik56l1CWxAzcnzofY0ejFDAUW1JsxbbAo/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1E-7SYqBmzdik56l1CWxAzcnzofY0ejFDAUW1JsxbbAo/edit?gid=0#gid=0)

---

# **How do we measure success?**

- Number of mandates registered via Aadhaar (E-sign) or Physical NACH as a percentage of total applications
- Success rate of mandate registration (E-sign/Physical NACH)
- Number of applications where E-NACH set up failed and the user was able to register a mandate via (Aadhaar E-sign / Physical NACH)

---

# **How are others solving this problem?**

- (BFL and TCL) have a stack to register mandate via their platform, and currently only support E-NACH capabilities to register a mandate
- LSPs offer mandate registration via physical mandate flow

---

# **What is the solution?**

We will be utilising Digio’s flow to initiate mandate registration flow for the user/LSP. LSP will be able to control which registration method is to be used in the mandate registration request.

LSP be able to pass the preferred method of mandate set up to the request post which the request will go through a whitelist. 

Each LSP will have the methods of mandate registration whitelisted for them (If they can use E-NACH/ Aadhaar E-sign/ Physical NACH) for the user mapping with source code.

Fenix will also share a bank whitelist with the LSPs for them to able to gauge which bank account is activated and available for the corresponding registration method.

Basis the selection, Fenix will invoke the specfic flow for the LSP by modifying a request parameter for Digio

<aside>
💡

Important note: E-NACH flows are synchronous which means that destination bank confirms immediately if the mandate can be set up or not.

Aadhaar e-sign and Physical NACH form set up on the other hand are a-synchronous and have a TAT of 2-5 days of completion and a relatively higher rate of failure. 

Scenarios can arise where a mandate registration was completed successfully but the registration in itself failed. 

We will not be blocking the user journey, instead we will allow users to set up mandate post origination. This will serve three use cases:

- Mandate set up failure (initiated in the application journey)
- Mandates marked inactive due to presentation failure
- Mandates expired (post expiry)
</aside>

We will be passing mandate status changes via callback to the LSP for the following events: 

- Mandate registered successfully
- Mandate confirmation (Important for Aadhaar e-sign and Physical NACH)
- Mandate registration failed (Important for Aadhaar e-sign and Physical NACH)
- Mandate expired
- Mandate marked as failed (due to erroneous presentation attempt)

LSP will be managing the respective status and accordingly will nudge the user to set up mandates again (Business alignment required).

## Requirements overview (optional):

## User stories / User flow

[https://claude.site/artifacts/3ee64537-2100-456e-a6ef-017e9c7a77c4](https://claude.site/artifacts/3ee64537-2100-456e-a6ef-017e9c7a77c4)

![image.png](%5BPlatform%5D%20Enabling%20alternate%20mandate%20registration/image.png)

## Requirements

### Bank whitelist:

Fenix will maintain a list of all banks and their corresponding availability across registration methods with NPCI (for mandates) this will be synced every day at EOD and the same will be used by partner LSPs (post bank verification) to pass a preferred mandate method while creating the request.

API integration with Digio (Documentation: [Link](https://documentation.digio.in/digicollect/nach/nach_registration/live_banks/))

**Sample request and response:**

```json
Type: Get
Endpoint:  /v3/client/mandate/banks

Response:
[
{
"id": "BNI190205133107279IW29M2B4TZ7PAJ",
"name": "510 Army Base W/s Credit Coop Primary Bank Ltd.",
"ifsc_prefix": "ICIC",
"active": true,
"primary_bank": false,
"routing_code": "ARMX",
"esign_mandate": false,
"api_mandate": false,
"physical_mandate": true,
"penny_less": false
},
{
"id": "BNI190205153036123F6UIBWCVOFSTSK",
"name": "Abhinandan Urban Coop Bank Amravati",
"ifsc_prefix": "HDFC",
"active": true,
"primary_bank": false,
"routing_code": "ABUX",
"esign_mandate": false,
"api_mandate": false,
"physical_mandate": true,
"penny_less": true
},
{
"id": "BNI1812040345269602CUEACAFX9R7JC",
"name": "Abhyudaya Co Op Bank",
"ifsc_prefix": "ABHY",
"active": true,
"primary_bank": false,
"routing_code": "ABHY",
"esign_mandate": true,
"api_mandate": false,
"physical_mandate": true,
"penny_less": true
},
{
"id": "BNI1902051331072707IKYF5BTXXG3YP",
"name": "Abu Dhabi Commercial Bank",
"ifsc_prefix": "ADCB",
"active": true,
"primary_bank": false,
"routing_code": "ADCB",
"esign_mandate": false,
"api_mandate": false,
"physical_mandate": true,
"penny_less": false
}]
```

LSPs will be using the IFSC code submitted by the user (and then verified via penny drop) to check the corresponding methods of registration in the mandate request.

**Sample request for mandate (Fenix):**

```json
{
    "opportunityId": "{{opportunityId}}",
    fenixLoanAccountId
    "bankAccountVerificationId": "{{bankUtilityRefId}}",
    "endDate": "2039-09-20",
    "**preferredMandateType**": "API_MANDATE/ ESIGN/ PHYSICAL",
    "mandateAmount": "50000000",
    "redirectionUrl": "https://www.voltmoney.in"
}
```

<aside>
💡

Important note: We will have to allow the LSP to create mandate creation requests post origination (use fenixLoanAccountId instead of opportunity ID)

</aside>

### LSP whitelist:

We will control which LSP can use which mandate registration method as an internal configuration. While LSPs can send a preferred registration method, Fenix will decide the mandate type based on the following logic.

- If passed method whitelisted (for LSP), accept the same and create corresponding request
- If passed method not whitelisted (for LSP), select the mandate type in the following order of availability (based on internally synced live bank list):
    - E-mandate
    - Aadhaar e-sign
    - Physical mandate

Fenix will share the selected mandate type in the corresponding response to the LSP:

```json
{
    "opportunityId": "OPP9726566149",
    "fenixLoanAccountId": null,
    "utilityReferenceId": "URMNDT4945818111",
    "status": "IN_PROGRESS",
    "subStatus": "IN_PROGRESS",
    "data": {
        "bankAccountDetails": {
            "nameAsPerBankAccount": "John Doe",
            "accountNumber": "02629180000",
            "ifscCode": "YESB0000300",
            "accountType": "SAVINGS_ACCOUNT",
            "bankName": "YES BANK"
        },
        "selectedMandateType": "API_MANDATE",
        "maxAmount": 50,
        "startDate": 1732200163700,
        "expiryDate": 2200156199999,
        "mandateFrequency": "ADHOC",
        "mandateStatus": null,
        "mobileNumber": "8494901798",
        "failureReason": null,
        "redirectionUrl": "https://www.google.com"
    },
    "verifierData": {
        "verifier": "DIGIO",
        "verifierReferenceId": "ENA241121201247204TR2F2O8WEBO9AP",
        "verifierTokenId": "GWT241121201247279RYQZBYB8DY64PS"
    },
    "webUrl": "https://ext.digio.in/#/gateway/login/ENA241121201247204TR2F2O8WEBO9AP/ENA241121201247204TR2F2O8WEBO9AP/8494901798?token_id=GWT241121201247279RYQZBYB8DY64PS&redirect_url=https://www.google.com"
}
```

### Callbacks to be consumed via Digio (Mandate registration):

| Webhook | Description | Handling (Pre-origination) | Handling (post-origination) |
| --- | --- | --- | --- |
| Mandate auth success | Mandate was successfully authenticated by the user | Let user move ahead to the next step of the application journey | Keep mandate status for loan account inactive |
| Mandate auth failed | Mandate authentication failed for the user | Ask user to retry auth set up | Keep mandate status for loan account inactive |
| Mandate transfer failed | Mandate transfer to sponsor bank failed for the user | Ask user to retry auth set up | Keep mandate status for loan account inactive |
| Mandate transfer succesful |  | Let user move ahead to the next step of the application journey | Keep mandate status for loan account inactive |
| Mandate accepted by sponsor bank |  | Let user move ahead to the next step of the application journey | Keep mandate status for loan account inactive |
| Mandate accepted by NPCI |  | Let user move ahead to the next step of the application journey | Keep mandate status for loan account inactive |
| Mandate rejected by NPCI |  | Ask user to retry auth set up | Keep mandate status for loan account inactive |
| Destination bank accepted | Mandate registered with destination bank | Mark mandate status as successful | Mark mandate status as successful |
| Destination bank rejected | Mandate registration failed with destination bank | Ask user to retry auth set up | Keep mandate status for loan account inactive |
| Mandate cancelled | Mandate was cancelled by the user or the bank | NA | Mark manadate as inactive (ask user to register a new mandate) |

**Possible statuses for mandate registration:**

created┃ready┃downloaded┃failed┃auth_success┃successful┃partial┃sign_pending┃signed┃transfer_failed┃transfer_success┃reject_spo_bank┃accepted_spo_bank┃awaiting_ack┃nack_received┃ack_received┃awaiting_res┃register_failed┃register_success┃revoked

### Callbacks to be triggered to LSP:

- Mandate registered successfully
- Mandate confirmation (Important for Aadhaar e-sign and Physical NACH)
- Mandate registration failed (Important for Aadhaar e-sign and Physical NACH)
- Mandate expired
- Mandate marked as failed (due to erroneous presentation attempt)

```json
// 1. Mandate Registered Successfully
{
  "event": "MANDATE_REGISTERED",
  "mandate_id": "string",
  "customer_ref_number": "string",
  "status": {
    "code": "SUCCESS",
    "message": "Mandate registered successfully"
  },
  "mandate_details": {
    "umrn": "string",
    "customer_name": "string",
    "customer_account_number": "string",
    "bank_name": "string",
    "maximum_amount": "number",
    "frequency": "Monthly|Quarterly|Yearly",
    "start_date": "date-time",
    "end_date": "date-time",
    "auth_type": "API|ESIGN|PHYSICAL"
  },
  "timestamp": "date-time"
}

// 2. Mandate Confirmation (For Aadhaar e-sign and Physical NACH)
{
  "event": "MANDATE_CONFIRMED",
  "mandate_id": "string",
  "customer_ref_number": "string",
  "status": {
    "code": "CONFIRMED",
    "message": "Mandate confirmed by bank"
  },
  "confirmation_details": {
    "ack_report": {
      "umrn": "string",
      "accepted": true,
      "generated_at": "date-time"
    },
    "bank_state": "ack_received"
  },
  "timestamp": "date-time"
}

// 3. Mandate Registration Failed
{
  "event": "MANDATE_REGISTRATION_FAILED",
  "mandate_id": "string",
  "customer_ref_number": "string",
  "status": {
    "code": "FAILED",
    "message": "Mandate registration failed"
  },
  "failure_details": {
    "reject_code": "string",
    "reject_reason": "string",
    "bank_state": "register_failed"
  },
  "timestamp": "date-time"
}

// 4. Mandate Expired
{
  "event": "MANDATE_EXPIRED",
  "mandate_id": "string",
  "customer_ref_number": "string",
  "status": {
    "code": "EXPIRED",
    "message": "Mandate has expired"
  },
  "expiry_details": {
    "expired_at": "date-time",
    "final_collection_date": "date-time"
  },
  "timestamp": "date-time"
}

// 5. Mandate Failed (Presentation Failure)
{
  "event": "MANDATE_PRESENTATION_FAILED",
  "mandate_id": "string",
  "customer_ref_number": "string",
  "status": {
    "code": "PRESENTATION_FAILED",
    "message": "Mandate presentation attempt failed"
  },
  "failure_details": {
    "presentation_date": "date-time",
    "reject_code": "string",
    "reject_reason": "string",
    "attempt_number": "number"
  },
  "timestamp": "date-time"
}

// 6. Mandate Cancelled by User
{
  "event": "MANDATE_CANCELLED",
  "mandate_id": "string",
  "customer_ref_number": "string",
  "status": {
    "code": "CANCELLED",
    "message": "Mandate cancelled by user"
  },
  "cancellation_details": {
    "cancelled_at": "date-time",
    "reason": "string"
  },
  "timestamp": "date-time"
}
```

---

# **Design**

- Interface to track mandate registration attempts and respective status (instead of just the current mandate details (active/inactive)) for ops team to coordinate with LSP/Users

---

# **Analytics**

@Vihari Kandian 

- Number of mandates registered via Aadhaar (E-sign) or Physical NACH as a percentage of total applications
- Success rate of mandate registration (E-sign/Physical NACH)
- Number of applications where E-NACH set up failed and the user was able to register a mandate via (Aadhaar E-sign / Physical NACH)

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