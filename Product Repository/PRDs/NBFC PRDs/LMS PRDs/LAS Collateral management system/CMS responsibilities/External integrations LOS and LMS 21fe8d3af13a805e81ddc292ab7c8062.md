# External integrations: LOS and LMS

Decription: - LOS integration
Status: Done

# **What problem are we solving?**

There is no dedicated system to centrally manage the lifecycle of collateral for Loan Against Securities (LAS). Currently, lien requests, revocations, and monitoring are either partially tracked in LMS or manually handled by operations. This leads to operational risk, poor scalability, and delayed exception handling.

---

# **How do we measure success?**

- Management of 100% collateral transactions through CMS
- 100% accuracy in lien verification processes

---

# **How are others solving this problem?**

Some lenders use an all-in-one platform where CMS is built into the LMS, but it limits flexibility and DP integrations. Most others rely on operations teams with spreadsheets and LMS-linked flags to track collateral status. This creates reconciliation debt and operational overhead.

---

# **What is the solution?**

Build a standalone CMS with tight integrations to both LOS and LMS. CMS will be the source of truth for lien status and collateral health, while LOS and LMS remain the system of record for application and loan lifecycle.

## Requirements overview (optional)

| System | Integration Purpose |
| --- | --- |
| LOS | Accept and validate user-submitted collateral information, generates offer based on approved list and configured margins at an ISIN level, deduplicate pledged assets, and generate a pledge request reference (PRF generation) |
| LMS | Keep lien status, revocation, and LTV updated throughout the lifecycle of the loan. Enable real-time updates on enhancements, margin calls, and release. |

## User stories / User flow

## Requirements

### LOS Integration Flow:

1. LSP LOS submits pledge reference request with BOID, folio, and ISINs.
2. LSP requests for a generated offer: generate offer will have the following values:
    1. 
    
    ```json
    {
    "dedupeResponse": {
    "isDuplicateClient": false,
    "message": "Client is not duplicate"
    }
    ,
    "assets": [
    {
    "isin": "INF0GCD01032",
    "folioNumber": "12345434",
    "dpId": "13424",
    "dematAccountNumber": "IN34242313424",
    "depository": "CDSL/NSDL/CAMS/KFIN",
    "isEligibleFund": true,
    "assetUnits": 4499.999,
    "assetLtv": 0.8,
    "assetValue": 4815673.92985,
    "assetCurrentLimit": 3852539.14388,
    "assetCurrentMarketPrice": 1070.15
    }
    ,
    {
    "isin": "INF277K01Z51",
    "folioNumber": "12345434",
    "dpId": "13424",
    "dematAccountNumber": "IN34242313424",
    "depository": "CDSL/NSDL/CAMS/KFIN",
    "isEligibleFund": true,
    "assetUnits": 4499.999,
    "assetLtv": 0.5,
    "assetValue": 232244.94839,
    "assetCurrentLimit": 116122.474195,
    "assetCurrentMarketPrice": 51.61
    }
    ,
    {
    "isin": "123",
    "folioNumber": "12345434",
    "dpId": "13424",
    "dematAccountNumber": "IN34242313424",
    "depository": "CDSL/NSDL/CAMS/KFIN",
    "isEligibleFund": false,
    "assetUnits": 4499.999,
    "assetLtv": 0,
    "assetValue": 0,
    "assetCurrentLimit": 0,
    "assetCurrentMarketPrice": 0
    }
    ]
    ,
    "totalAssetValue": 5047918.87824,
    "totalAssetLtv": 3968661.618075,
    "feeConfig": {
    "processingFee": {
    "minFee": 499,
    "maxFee": 400000
    }
    ,
    "renewalFee": {
    "minFee": 499,
    "maxFee": 400000
    }
    ,
    "enhanceLimitFee": {
    "minFee": 25000,
    "maxFee": 20000000
    }
    ,
    "marginPledgeFee": {
    "minFee": 0,
    "maxFee": 400000
    }
    }
    ,
    "interestConfig": {
    "minInterestRate": 8,
    "maxInterestRate": 20
    }
    ,
    "tenureConfig": {
    "minTenureMonths": 12,
    "maxTenureMonths": 37
    }
    }
    ```
    
3. LOS sends collateral details to CMS for validation and generating a pledge request reference (Pledge request reference gives them a unique ID which will be the pledge utility reference number
    1. There are two ways through which LSPs can operate in this flow:
        1. Get a generated PRF (will be handled at a DP ID level for top X DP providers)
        2. Use the pledge reference ID to lien mark securities (They will use this as the pledge agreement number (PAN))
4. LOS sends pledged collateral for lien verification to CMS
5. CMS:
    - Verifies collateral eligibility. (Approved list validation based on ISIN)
    - Deduplicates based on DP account number + ISIN + Pledge agreement number (Pledge utility reference number)
    - Generates pledge utility reference number (Pledge Request Form) with unique pledge agreement ID.
6. CMS verifies lien marking of securities and lodges securities in the collateral

### LMS Integration Flow:

1. Once loan is created, CMS pushes collaterals for lodgement to LMS
2. CMS pushes:
    - Lien confirmation
    - Asset data
    - Daily NAV values at an ISIN level
3. User raises a collateral release request, LMS validates the request in terms of DP validation, post validation raises to CMS, CMS verifies lien, creates a release task for the operations team (Currently lien revocation will be an operational process)

Once request is processed, CMS confirms the final status (Lifecycle management of collateral request is managed by CMS) and confirms to LMS: LMS releases collateral from the user’s loan account.
4. User/Ops raises a collateral invocation request, LMS validates the request in terms of DP validation, post validation raises to CMS, CMS verifies lien, creates a invocation task for the operations team (Currently lien invocation will be an operational process)

When units are invoked, they will be available as units in the DP account of the NBFC, Operational team then raises a sell request to the broker.  (Need to understand association of units to invocation request)

Broker initiates sale of collateral, once sold off, proceeds of the transaction are posted into the user’s account as a repayment

Once request is processed, CMS confirms the final status (Lifecycle management of collateral request is managed by CMS) and confirms to LMS: LMS releases collateral from the user’s loan account.

### LOS Integration

| Requirement | Description |
| --- | --- |
| Offer generation API enhancements | Offer generation API enhancement to consume LAS specific parameters:
- BO ID
- Depository
- DP ID
 |
| Approved list enhancements | Support LAS as collateral in the script NAV master 

Consuming depository at an ISIN level

Storing sub type of security (EQUITY_SHARE
EQUITY_MF
DEBT_MF
LIQUID_MF)

(NAV exchange will happen at an ISIN level) |
| Collateral Intake API | CMS exposes API for LOS to submit BOID, folio, and ISINs for collateral addition

Consuming pledge source at an ISIN level basis pledge source conditional handling will be done for lien verification processes (STP/non STP logic)

- CDSL / NSDL (Physical lien verification) if approved lodge via NSTP flows (Task is created with DSP operations team)

- MFC (Digital lien verification) if success lodge while following STP thresholds

- CAMS (Digital lien verification) if success lodge while following STP thresholds

- KFIN (Digital lien verification) if success lodge while following STP thresholds
 |
| Dedupe Logic | CMS checks whether the same ISIN is already pledged by borrower across loans (Shares) |
| PRF Generation | CMS returns a unique pledge request number + PRF to LOS after successful validation for top X DPs |
| Enhancements in current flow to support manual lien verification | Design support for enhancement of add collateral workflow to support loan against shares @Karuna Sankolli 

Collateral management system section where DSP operations team will be able to track all holdings lien marked against the NBFC (Will cover in detail in operations tooling) |
| Sync Validation Status | CMS updates LOS with per-ISIN eligibility and reason for rejection (Offer generation support) |
| Await Lien Confirmation | LMS must await successful lien confirmation from CMS before lodging collateral. |

---

# **Design**

NA

---

# **Analytics**

Loans with Collateral at Origination

Track the number and percentage of loans that had a pledged security (Loan Against Shares) at the time of disbursal.

## 2. **Lifecycle TAT Monitoring**

The system should measure time taken (Turnaround Time - TAT) across and within the following stages of the collateral lifecycle:

### A.  **Collateral Addition Flow**

| Step | Metric |
| --- | --- |
| Pledge Request Created | Time from loan sanction to pledge request initiation |
| PRF (Pledge Reference Form) Generated | Time from pledge request to PRF generation |
| Pledge Confirmation | Time from PRF to confirmation from SHCIL/DP |
| Final Lodgement | Time from confirmation to CMS marking collateral as active and eligible |

---

### B.  **Collateral Release Flow**

| Step | Metric |
| --- | --- |
| Release Request Created | Triggered on prepayment or loan closure |
| Task Created | Internal task generated for review |
| Task Approved | Time taken for Ops to approve release |
| Release Executed (LMS + DP) | Time from approval to actual revocation and confirmation in LMS and DP |

---

### C.  **Collateral Invocation Flow**

| Step | Metric |
| --- | --- |
| Invocation Request Created | Triggered by default or margin shortfall |
| Task Created | Internal task generated for risk/Ops |
| Task Approved | Time taken to approve invocation |
| Holding Transfer Confirmed | Time from approval to confirmation of holding transfer (via PMR or Ops input) |

---

### D.  **Collateral Sale & Recovery Flow**

| Step | Metric |
| --- | --- |
| Broker Sale Initiated | Time from holding transfer to sale trigger |
| Broker Sale Confirmed | Confirmation received from broker platform |
| Repayment Reconciliation | Time from confirmation to mapping proceeds to loan account |
| Repayment Posting | Time from reconciliation to repayment ledger update |

---

# **Timeline/Release Planning**

---

# **Go to market**

NA - Internal workflow

## Marketing

NA - Internal workflow

## Ops & Sales training

NA - Internal workflow

## Frequently asked questions (FAQs)

NA - Internal workflow

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