# DSP: PhonePe PG Integration for PhonePe

: Gautam Mahesh
Created time: February 4, 2025 1:08 PM
Status: In progress
Last edited: March 8, 2025 1:25 PM

# **What problem are we solving?**

- Recording PG repayments from PhonePe offline will take considerable time and effort for our operations team
- Reconciling PG repayments from PhonePe will take time and will impact the SLAs from a customer experience perspective
- Delay in posting transactions will impact our accounting and result in backdated transactions, opening up a backdoor for a lot of issues

---

# **How do we measure success?**

- Transaction Success Rate – Percentage of transactions which are accepted by DSP
- Turnaround Time (TAT) for transaction – Time taken to complete the PG repayment.

---

# **What is the solution?**

DSP will expose an API to accept payments through PG on PhonePe UI.

---

## User stories / User flow

### Transaction

- The user intending to take a loan against mutual funds enters through the PhonePe application.
- The user completes all necessary KYC steps, uploads a selfie, and provides additional data for the DSP lender on the PhonePe UI.
- PhonePe prompts the user to set up the UPI mandate on their verified bank accounts, with the data later to be shared with DSP.
- The user sets up the mandate via the PhonePe app and proceeds to open the DSP loan account.

### Reconciliation

### Accounting

---

## Requirements

The flow is broken into 2 parts-

1. Transaction
2. Reconciliation

### Transaction

- The user intending to take a loan against mutual funds enters through the PhonePe application.
- The user completes all necessary KYC steps, uploads a selfie, and provides additional data for the DSP lender on the PhonePe UI.
- PhonePe will not call DSP’s bank verification or mandate setup APIs. Instead, it will interact with PhonePe PG APIs to set up UPI autopay.
- Once the UPI mandate is successfully registered, the PhonePe lending team will call the mandate posting API exposed by DSP to share all mandate details. The attributes include:
    - Opportunity ID
    - UMN
    - Status
    - Timestamp
    - Bank Account Number
    - IFSC, etc.
- The mandate posting API will accept data only if the status is “Success.”
- In the DSP database, an entry will be created against the Opportunity ID and marked as completed. DSP will also generate the “Bank Utility Reference ID” and “Mandate Reference ID.”
- In the same mandate posting API response, DSP will share 2 utility reference IDs.
    - Bank Utility Reference ID
    - Mandate Utility Reference ID
- Using these utility reference IDs, the PhonePe lending team will call the Generate Loan Contract API.
- The Generate Loan Contract API will function only if all utility reference IDs are in a successful state. For mandate verification, DSP will rely on PhonePe PG APIs, and for bank verification, DSP will rely on mandate posting done by PhonePe lending.
- PhonePe PG team will share a registration summary report(MIS) on a T+1 basis which will include all the successful and failed registrations.
- DSP will reconcile the list of mandates registered using the UMN field from the PhonePe PG MIS against the DSP database.
- Two possible ways for going wrong-
    - Mandate data missing in PhonePe PG MIS report
    - Data is available in PhonePe PG MIS but mandate posting is not done by PhonePe Lending.
    
    In both the above cases, there should be a SOP to address the issues.
    
- DSP to rely on PhonePe PG MIS reports as the first source of truth.

Below are the fields DSP wants from PhonePe at a transaction level.

| Field | Description | Mandatory |
| --- | --- | --- |
| Acc ID | PhonePe ref ID | Yes |
| LAN | Fenxi LAN | Yes |
| Req ID | API request ID for reconciliation | Yes |
| Amount | Gross Payment amount | Yes |
| UTR | Transaction | Yes |
| Timestamp | Transaction timestamp | Yes |
| Method | DC, NB, UPI | Yes |
| Network | Master, VISA, Rupay | Yes |
| Bank | Bank name - DC/NB | Yes |
| Status | Success, Failure | Yes |
| Name | Payer name | No |

### SFTP Setup

This SFTP is for MIS reports exchange between PhonePe PG & DSP. PhonePe PG to share the SFTP setup guide.

### LMS Posting

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