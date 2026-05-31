# LAS CMS: Unlodgement

Last Edited: March 19, 2026 9:44 PM
PRD ETA: October 30, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

For collateral removal, DSP Finance needs to verify that requested securities for removal are successfully marked in its name before removing them from user loan accounts to ensure that no financial exposure is created for the NBFC.

Unlike non-demat holdings handled by RTAs (CAMS/KFIN), where lien verification capabilities exist, depositories (CDSL/NSDL) do not provide a programmatic lien status check. This gap creates an operational dependency: DSP Finance cannot directly validate lien marking in real time.

Additionally, unlike RTAs, digital removal of securities via APIs is not available with depositories (NSDL and CDSL). The same will be managed operationally by raising requests on SHCIL dashboard.

To address this, DSP Finance will rely on ingestion of the PMR (Pledge Master Report) provided by depositories. The PMR will serve as the source of truth for lien confirmation, enabling reconciliation of remove collateral requests and we will be using SHCIL’s dashboard to remove collaterals.

Core use cases of removal of collaterals:

- **Eligibility check**: Ensuring that the user is only able to revoke securities of the amount equal to the eligible limit available for revocation. The same will remain consistent with the existing implementation
Summation(Units*NAV*LTV)≤ DP - TOS - AI
- **Pledge status tracking**: Differentiating between “lien created,” “lien invoked,” and “released” statuses for proper lifecycle management.
- **Counterparty validation**: Verifying DP ID/Client ID to prevent cross-client or erroneous revocation.

---

# **How do we measure success?**

The success of revocation transaction handling in CMS will be measured across accuracy, timeliness, reconciliation fidelity, and process efficiency.

- **Accuracy of Lifecycle Tracking**
    - Every collateral revocation request should move through clearly defined states:
    - Request accepted
    - Blocking of collaterals (To ensure DP is reduced)
    - Verification of lien using PMR consumed data (existing)
    - Release task (This is different from checker task, has here the ops agent will be releasing the securities and confirming if the securities have been released) (This will enable the operations team to raise request using the Transnet dashboard with SHCIL) once confirmed they will complete the task
    - Once the task is completed, we will take the request in a pending reconciliation state, here we will be consuming the PMR for the respective PSNs to confirm if the securities have been released. (User should not be able to raise any subsequent release requests till this request is taken to closure for the respective loan account)
    - The operations agent will be able to perform 3 actions on the task:
        - Confirm release (This will signify that they have confirmed release using Transnet dashboard with SHCHIL)
        - Cancel and unblock securities (This will cancel the request, and also ensure that the user gets the corresponding drawing power against the blocked securities
        - Fail request: This is an option where the securities will not be unblocked, but the request will be marked failed (So that exposure can be controlled, while keeping the securities as blocked)
    - Once the reconciliation is completed, and PMR (logic shared below) confirms revocation, we will release the securities from the LMS and close the request
- **Reconciliation Fidelity**
    - Derived pledging requests from PMR must match to actual removal transactions without exceptions (or with a defined SLA for resolution).
- **Timeliness of revocation**
    - Average turnaround time from lien verification (via PMR) to revocation completion should be measurable.
    - SLA adherence for ingestion, verification, and DP update steps. (SLAs to be defined)
- **Operational Efficiency**
    - Reduction in manual interventions needed to revoke pledges.
    - Automated ingestion and reconciliation reduces dependency on ops bandwidth.

---

# **How are others solving this problem?**

- Industry practice today is largely **manual intervention** due to the absence of a depository-provided API or system for lien release.
- **Example**: **TCL** – Their operations team downloads the PMR reports from depositories and compares them with internal collateral records. They manually deduplicate entries and verify lien status before confirming revocation.
- This approach is **time-consuming, error-prone, and operationally intensive**, but remains the default fallback for most players in the LAS ecosystem.
- The opportunity lies in **automating ingestion, mapping, and reconciliation of PMR data** to replicate this manual verification flow at scale, reducing both turnaround time (TAT) and error rates.

---

# **What is the solution?**

- **PMR-based validation** – Since no lien verification API is available, removal will rely on accurate and timely ingestion of PMR data.
- **Derived removal requests** – The system will generate internal removal requests from PMR entries and reconcile them against originator-reported transactions.
- **Reconciliation-first approval** – Revocation will only be approved once checker confirms task on Command centre
- **Exception handling** – Any mismatches between pledged securities and PMR entries will be flagged for manual resolution.
- **Lifecycle management**: Management of add collateral request via CMS (Removal)

## User stories / User flow

![image.png](LAS%20CMS%20Unlodgement/image.png)

## Requirements

### Unpledging of Securities (Process Overview – for information only)

1. **Initiation**
    - Lender gets request from LSP/Customer for removal of lien of Demat securities
2. **DP Validation**
    - DP validation is done to ensure that the request for removal of collaterals is valid as per aforementioned validation
    - Upon successful validation, the request is forwarded the operations team via a removal task with the expectation of removal of those securities using Transnet (SHCIL dashboard)
3. **Lien unmarking**
    - Once the PSNs for the corresponding entries are entered on the dashboard (bulk is also available with Transnet)
4. **PMR Reflection**
    - **Released securities will reflect in the PMR transaction as revoked units and the status will change to partially closed for CDSL and NSDL**
    - **Identifiers for tracking:**
        - *Pledge Agreement Number*
        - *Pledge Sequence Number (PSN)*

### Deriving Release Pledge Transactions from PMR

Since there is no direct API available to fetch lien removal status, the **PMR (Pledge Master Report)** becomes the single source of truth for identifying revocation completion. To create internal records of new pledges, we apply a **deduplication logic** based on:

- **Depository (CSDL/NSDL)**
- **Pledge Sequence Number (PSN)**
- Status + Released units

Please note that this is only applicable for already lodged securities, that is these PSNs should already be lodged in the corresponding loan accounts

There may also arise multiple release requests against the same PSN, in this case, we should reconcile it at an PSN level 

Scenario:

Lodgement: PSN1 with units 100

Release 1: 10 units are released, PSN1 will remain same, total units will remain 100 and released units will change to 10 making total available units as 90

Release 2: 10 units are released, PSN1 will remain same, total units will remain as 100, and released units will change to 20, the tracking accordingly has to be incremental

### Process:

1. **Scan PMR Entries:** The system ingests each fresh PMR file received from the depository.
2. **Check for change in units for lodged PSNs:** For each line item in the PMR, the system checks total units, released units and confiscated/invoked units
3. **Create Derived Transaction:**
    - If a change in available units  is identified, it is treated as a **new transaction**, and an **internal open remove pledge transaction** is created.
    - If the combination is **already present and units are changed**, it is ignored (as it has already been recorded earlier).
4. **Linking Information** – The derived transaction carries essential details like pledge agreement number, folio, ISIN, quantity, and lien date to enable reconciliation and tracking.

### Originator shared pledge information:

**Step 1: Input from originator**

- The originator initiates the removal process by calling the **Remove Collateral API**.
- API payload (V1):
    - Loan account number / Opportunity ID (where securities should be lodged)
    - DEMAT account number (holder / end user / Pledgor)
    - DEMAT account number (Pledgee: Securities in favour of)
    - ISIN of security pledged
    - Units of security pledged (Number of units that have to be released)
    - Depository of units pledged against (NSDL/CDSL)

**Step 2: Pre-lien verification validation**

Before lien removal is attempted, the following validations are performed:

1. **Lodgement validation:** Ensures the ISIN and units are lodged against the loan.
2. **Deduplication check:** Ensures the same ISIN + DEMAT + Pledge agreement number combination is not already raised for removal.

Only if these validations succeed does the process proceed to lien removal, and a sync fail response is given to the originator

**Step 3: Open pledge removal transaction creation**

- Once the request is created, it will look for an open for reconciliation pledge removal derive transaction
- The system attempts to match the details (DEMAT + ISIN + Depository + Agreement number + Sequence number + Units) with existing pledge transactions.
- If a matching derived transaction is found, the status of that derived transaction is updated to **“Reconciled”** so that it cannot be re-used in reconciliation with any other request.

**Step 4: Checker decision (manual review)**

- After initial lien verification, the request passes through a **choice state** to decide whether manual checker approval is required.
- For **launch (V1)**: This will be **globally enforced** → all requests must pass through checker review.
- For **future versions**: This may be conditional, based on parameters such as:
    - **LTV value threshold** (e.g., if above a certain exposure amount)
    - **Depository type** (e.g., certain depositories requiring stricter control)
    - **Originator profile** (some partners might be fully trusted, others partially controlled)
    
    Checker will be performing the following checks manually:
    
    - Lodgement verification: They will be able to track lodged securities and verify if the same are blocked for revocation
    - Dedupe check: Checker will be able to track collateral transactions and ensure that a similar request for same PSN does not exist
    - Lien verification: Checker will go through the latest PMR to ensure that the securities are pledged
    - DP Validation: Checker will validate if the limit available for account is enough to remove the securities from the account

**Step 5: Post-checker lien verification (second pass)**

- Once checker approves, they will release the units against the corresponding PSNs using Transnet (SHCIL dashboard)

**Step 6: Reconcilation and lifecycle tracking**

- On successful confirmation, securities are removed from the borrower’s loan account.
- Remvoval ensures:
    - Securities are tagged against the correct loan account.
    - Exposure and collateral value are updated in RMS.
    - A unique remove collateral request ID is generated for traceability.

```json
[Start: User Removal Request]
|
v
[Eligibility Check]
|---(Fail: Sum(Units*NAV*LTV) > DP-TOS-AI)--> [Rejected: Insufficient Eligible Limit]
|
v
[Request Accepted & Securities Blocked]
|
v
[PMR Lien Status Verification]
|---(Fail: Lien not found in PMR / Status mismatch)--> [Rejected: PMR Verification Failure]
|
v
[Release Task Creation]
|
v
[Operations Team Action Required]
|---(Cancel & Unblock)--> [Request Cancelled: Securities Unblocked]
|---(Fail Request)--> [Request Failed: Securities Remain Blocked]
|---(Confirm Release)--> [Release Confirmed via SHCIL/Transnet]
|
v
[Pending Reconciliation State]
|---(Block: New requests for same loan account)--> [Subsequent Requests Blocked]
|
v
[PMR Reconciliation Check]
|---(Fail: PSN not released in PMR)--> [Exception Handling: Manual Resolution Required]
|
v
[Release Securities from LMS]
|
v
[End: Removal Successful & Request Closed]
```

---

# **Design**

https://docs.google.com/spreadsheets/d/1jVKAnJZUNI8VeihT4B6Wdtbletytx-wrLQOE8Dor3XM/edit?gid=571501479#gid=571501479

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