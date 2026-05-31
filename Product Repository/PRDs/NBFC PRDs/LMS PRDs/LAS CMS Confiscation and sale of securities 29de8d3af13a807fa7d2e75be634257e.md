# LAS CMS: Confiscation and sale of securities

Last Edited: November 17, 2025 12:01 PM
PRD ETA: October 30, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

When securities are lien marked in favour of DSP Finance, it also gives the capability to the NBFC to invoke the lien to redeem the securities, this gives the proceeds from the sale of securities to the NBFC which is posted in the security holder’s loan account.

The following reasons are why there is a need for this capability:

- If the user goes into a shortfall, and is unable to regularise (DP>POS) their loan account within a stipulated time period (7 working days as defined by RBI), the NBFC is required to invoke securities to regularise the account
- If the user is overdue, and goes beyond a DPD of 20 days, the securities are invoked to recover all overdue amounts
- If the user, does not have capability to pay, their outstanding balance, they can raise a request to the NBFC to invoke the lien and recover all dues from the corresponding proceeds, this is called as a voluntary sell off.
- In case of a fraud, or an exposure breach, where TOS>Value of collaterals lodged in the loan account, the securities are sold off to recover all dues.

For collateral sale, DSP Finance needs to verify that securities selected for sale are successfully marked in its name.

Unlike non-demat holdings handled by RTAs (CAMS/KFIN), where lien invocation capabilities exists via APIs, depositories (CDSL/NSDL) do not provide a programmatic lien status check. This gap creates an operational dependency: DSP Finance cannot directly validate lien marking in real time.

Additionally, unlike RTAs, digital sale of securities via APIs is not available with depositories (NSDL and CDSL). The same will be managed operationally by raising requests on SHCIL dashboard. (Transnet)

Following is a PDF with screenshots from the Transnet dashboard

[Transnet_Demo_2.html (1).pdf](LAS%20CMS%20Confiscation%20and%20sale%20of%20securities/Transnet_Demo_2.html_(1).pdf)

To address this, DSP Finance will rely on ingestion of the PMR (Pledge Master Report) provided by depositories. The PMR will serve as the source of truth for lien confirmation, enabling reconciliation of sale collateral requests and we will be using SHCIL’s dashboard to sell collaterals.

Unlike non-Demat funds, where there is a direct API to invoke securities, invocation of lien for demat securities is a 2 step process.

- Confiscation: When confiscation is initiated for securities lien marked in favour of the NBFC, the units are transferred from the user’s demat account to the NBFC account.
- Sale of securities: Once securities are confiscated, they start reflecting in the NBFC’s demat account, and requests can be raised for the corresponding sale to the SHCIL terminal team.

Requests to SHCIL will be shared over email and at an account level, the settlement of proceeds of the collateral will be at an ISIN x Request level, that is if in one request there are 3 different ISINs, the NBFC bank account will get 3 corresponding credits in the bank account.

Core aspects for invocation of collaterals:

- **Eligibility check**: Ensuring that the user/NBFC is only able to confiscate securities of the amount equal to the eligible limit available for confiscation. The same will remain consistent with the existing implementation
Summation(Units*NAV*LTV)≤ **DP - AI**
- **Pledge status tracking**: Differentiating between “lien created,” “lien invoked,” and “released” statuses for proper lifecycle management.
- **Counterparty validation**: Verifying DP ID/Client ID to prevent cross-client or erroneous invocation.
- Blocking of DP: It will take one working day to process invocation of shares, and the corresponding settlement will be done at a T+1 basis. During this period, the securities should be blocked to ensure that there is no exposure breach for the user.
- Invocation charge: For now, we will keep the invocation charges for the securities the same as LAMF, the workflow of charge application will also remain consistent
- Reconciliation of proceeds with the corresponding collateral and shortfall request ID: Reconciliation of proceeds will be done at an amount level, since the settlement of the sale will be manually done and there are no data APIs through which requests can be triangulated to the corresponding settlement
- Posting of repayment and release of collateral from the loan account

Operations team will have the capability to upload bulk settlement files corresponding to the invocations that they have to do. Since these operations are usually done for multiple customers at a time, we will be enhancing the bulk sell off functionality to support confiscation and sale of securities.

---

# **How do we measure success?**

The success of invocation transaction handling in CMS will be measured across accuracy, timeliness, reconciliation completion, and process efficiency.

- **Accuracy of Lifecycle Tracking**
    - Every collateral invocation request should move through clearly defined states:
    - Request accepted
    - Blocking of collaterals (To ensure DP is reduced)
    - Verification of lien using PMR consumed data (existing)
    - Confiscation task (This is different from a checker task, has here the ops agent will be confiscating the securities and confirming if the securities have been confiscated) (This will enable the operations team to raise request using the Transnet dashboard with SHCIL) once confirmed they will complete the task
    - Operations team will be able to verify the confiscated securities on the CDSL/NSDL dashboard via Transnet using the holding statement report via the Transnet dashboard and can accordingly mark the task as completed, in case they were unable to confiscate the securities they can fail the request, or reject the request (in case of validation failure)
        - Confirm confiscation (This will signify that they have confiscated securities using Transnet dashboard with SHCHIL)
        - Cancel and unblock securities (This will cancel the request, and also ensure that the user gets the corresponding drawing power against the blocked securities)
        - Fail request: This is an option where the securities will not be unblocked, but the request will be marked failed (So that exposure can be controlled, while keeping the securities as blocked)
    - Once the task is completed, we will take the request in a pending reconciliation state, here we will be consuming the PMR for the respective PSNs to confirm if the securities have been confiscated. (NBFC will be able to raise a sell off request even if there is an existing incomplete sell off request for the user’s loan account.)
    - Once the reconciliation is completed, and PMR (logic shared below) confirms confiscation, we will release the securities from the LMS and close the request
- **Reconciliation Fidelity**
    - Derived pledging requests from PMR must match to actual confiscation transactions without exceptions (or with a defined SLA for resolution).
- **Timeliness of confiscation**
    - Average turnaround time from lien verification (via PMR) to confiscation completion should be measurable.
    - SLA adherence for ingestion, verification, and DP update steps. (SLAs to be defined)
- **Operational Efficiency**
    - Reduction in manual interventions needed to confiscate pledges.
    - Automated ingestion and reconciliation reduces dependency on ops bandwidth.

---

# **How are others solving this problem?**

- Industry practice today is largely **manual intervention** due to the absence of a depository-provided API or system for lien release.
- **Example**: **TCL** – Their operations team downloads the PMR reports from depositories and compares them with internal collateral records. They manually deduplicate entries and verify lien status before confirming confiscation.
- This approach is **time-consuming, error-prone, and operationally intensive**, but remains the default fallback for most players in the LAS ecosystem.
- The opportunity lies in **automating ingestion, mapping, and reconciliation of PMR data** to replicate this manual verification flow at scale, reducing both turnaround time (TAT) and error rates.

---

# **What is the solution?**

- **PMR-based validation** – Since no lien verification API is available, removal will rely on accurate and timely ingestion of PMR data.
- **Derived removal requests** – The system will generate internal removal requests from PMR entries and reconcile them against originator-reported transactions.
- **Reconciliation-first approval** – confiscation will only be approved once checker confirms task on Command centre
- **Exception handling** – Any mismatches between pledged securities and PMR entries will be flagged for manual resolution.
- **Lifecycle management**: Management of add collateral request via CMS (Removal)

## User stories / User flow

![image.png](LAS%20CMS%20Confiscation%20and%20sale%20of%20securities/image.png)

## Requirements

### Sell off of Securities (Process Overview – for information only)

1. **Initiation**
    - Lender gets request from LSP/Customer for voluntary sell off of Demat securities
2. **DP Validation**
    - DP validation is done to ensure that the request for sale of collaterals is valid as per aforementioned validation
    - Upon successful validation, the request is forwarded the operations team via a sell off task with the expectation of confiscating of those securities using Transnet (SHCIL dashboard)
3. **Lien invocation**
    - Once the PSNs for the corresponding entries are entered on the dashboard (bulk is also available with Transnet)
4. **PMR and holding statement reflection**
    - **Invoked securities will reflect in the PMR transaction as confiscated units and the status will change to partially invoked for CDSL and NSDL**
    - Once invoked the securities will start reflecting in the holding statement of the NBFC’s Demat account with the corresponding depository.
    - **Identifiers for tracking:**
        - *Pledge Agreement Number*
        - *Pledge Sequence Number (PSN)*
5. **Sale of securities**
    - Once the securities are confiscated and available as units in the NBFC demat account number, requests will be raised to SHCIL for selling the securities.
    - These requests will be raised at a loan request level, the corresponding settlement to the account will be done at an ISIN + Request level.
    - Post settlement of transactions in the NBFC account (T+1) the corresponding proceeds from the sale of collateral will be posted, and the corresponding units will be released from the loan account

<aside>
💡

(Same as LAMF): Existing bulk sell off workflow and repayment posting workflow has to be enhanced here

</aside>

### Deriving Release Pledge Transactions from PMR

Since there is no direct API available to fetch lien confiscation status, the **PMR (Pledge Master Report)** becomes the single source of truth for identifying confiscation completion. To create internal records of new pledges, we apply a **deduplication logic** based on:

- **Depository (CSDL/NSDL)**
- **Pledge Sequence Number (PSN)**
- Status + Confiscated/Invoked units

Please note that this is only applicable for already lodged securities, that is these PSNs should already be lodged in the corresponding loan accounts

There may also arise multiple sell off requests against the same PSN, in this case, we should reconcile it at an PSN level 

Scenario:

Lodgement: PSN1 with units 100

Release 1: 10 units are confiscated, PSN1 will remain same, total units will remain 100 and confiscated units will change to 10 making total available units as 90

Release 2: 10 units are released, PSN1 will remain same, total units will remain as 100, and confiscated units will change to 20, the tracking accordingly has to be incremental

### Process:

1. **Scan PMR Entries:** The system ingests each fresh PMR file received from the depository.
2. **Check for change in units for lodged PSNs:** For each line item in the PMR, the system checks total units, released units and confiscated/invoked units
3. **Create Derived Transaction:**
    - If a change in available units  is identified, it is treated as a **new transaction**, and an **internal open sell off transaction** is created.
    - If the combination is **already present and units are changed**, it is ignored (as it has already been recorded earlier).
4. **Linking Information** – The derived transaction carries essential details like pledge agreement number, folio, ISIN, quantity, and lien date to enable reconciliation and tracking.

### Originator shared pledge information:

**Step 1: Input from originator**

- The originator initiates the sell off process by using the bulk sell off removal
- File format (V1):
    - Loan account number (where securities should be lodged)
    - ISIN of security pledged
    - Units of security pledged (Number of units that have to be released)
    - Depository of units pledged against (NSDL/CDSL)
    - DEMAT account number

**Step 2: Response File**

- The originator in return will get a response file, which will be used to reconcile proceeds from sale and post in the respective loan account
- File format (V1):
    - Loan account number (where securities should be lodged)
    - ISIN of security pledged
    - Units of security pledged (Number of units that have to be released)
    - Depository of units pledged against (NSDL/CDSL)
    - Sell off request ID (SCRID)
    - Collateral detail ID (CDID)
    - PSN
    - Pledge agreement number
    - NAV
    - DEMAT account number

Repayments will be posted at a CDID level in the respective loan accounts.

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
    
    - Lodgement verification: They will be able to track lodged securities and verify if the same are blocked for confiscation
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

![image.png](LAS%20CMS%20Confiscation%20and%20sale%20of%20securities/image%201.png)