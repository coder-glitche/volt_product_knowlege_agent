# LAS CMS: Lodgement

Last Edited: October 30, 2025 7:51 PM
PRD ETA: August 20, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

For collateral lodgement, DSP Finance needs to verify that pledged securities have been successfully marked in its name before associating them with user loan accounts and extending drawing power.

Unlike non-demat holdings handled by RTAs (CAMS/KFIN), where lien verification capabilities exist, depositories (CDSL/NSDL) do not provide a programmatic lien status check. This gap creates an operational dependency: DSP Finance cannot directly validate lien marking in real time.

To address this, DSP Finance will rely on ingestion of the PMR (Pledge Master Report) provided by depositories. The PMR will serve as the source of truth for lien confirmation, enabling reconciliation of pledging requests with actual pledging transactions before lodgement approval.

Core use cases of lodgement:

- **Eligibility check**: Ensuring only securities that meet lender’s eligibility criteria (e.g., allowed ISINs, AMC whitelist/blacklist, minimum NAV thresholds) are lodged.
- **Pledge status tracking**: Differentiating between “lien created,” “lien invoked,” and “released” statuses for proper lifecycle management.
- **Loan exposure alignment**: Verifying that lodged securities are mapped to the correct loan account, ensuring accurate LTV computation and exposure tracking.
- **Counterparty validation**: Verifying DP ID/Client ID to prevent cross-client or erroneous lodgement.

---

# **How do we measure success?**

The success of lodgement transaction handling in CMS will be measured across accuracy, timeliness, reconciliation fidelity, and process efficiency.

- **Accuracy of Lifecycle Tracking**
    - Every collateral lodgement request should move through clearly defined states — pending verification, verified, associated to loan account, checker validation.
- **Reconciliation Fidelity**
    - Derived pledging requests from PMR must match to actual pledging transactions without exceptions (or with a defined SLA for resolution).
- **Timeliness of Lodgement**
    - Average turnaround time from pledge identification (via PMR) to lodgement completion should be measurable.
    - SLA adherence for ingestion, verification, and DP update steps. (SLAs to be defined)
- **Operational Efficiency**
    - Reduction in manual interventions needed to validate pledges.
    - Automated ingestion and reconciliation reduces dependency on ops bandwidth.

---

# **How are others solving this problem?**

- Industry practice today is largely **manual reconciliation** due to the absence of a depository-provided API or system for lien verification.
- **Example**: **TCL** – Their operations team downloads the PMR reports from depositories and compares them with internal collateral records. They manually deduplicate entries and verify lien status before confirming lodgement.
- This approach is **time-consuming, error-prone, and operationally intensive**, but remains the default fallback for most players in the LAS ecosystem.
- The opportunity lies in **automating ingestion, mapping, and reconciliation of PMR data** to replicate this manual verification flow at scale, reducing both turnaround time (TAT) and error rates.

---

# **What is the solution?**

- **PMR-based validation** – Since no lien verification API is available, lodgement will rely on accurate and timely ingestion of PMR data.
- **Derived pledging requests** – The system will generate internal pledging requests from PMR entries and reconcile them against originator-reported transactions.
- **Reconciliation-first approval** – Lodgement will only be approved once reconciliation confirms DSP’s lien.
- **Exception handling** – Any mismatches between pledged securities and PMR entries will be flagged for manual resolution.
- **Lifecycle management**: Management of add collateral request via CMS (Lodgement)

## User stories / User flow

![image.png](LAS%20CMS%20Lodgement/image.png)

## Requirements

### Pledging of Securities (Process Overview – for information only)

1. **Initiation**
    - Users complete **Pledge Request Forms (PRFs)** with wet signatures.
    - Forms are submitted to their **Depository Participant (DP)**, typically via physical letters routed through brokers/DPs.
2. **DP Validation**
    - The DP validates the PRF details.
    - Upon successful validation, the request is forwarded to the relevant depository (**CDSL/NSDL**).
3. **Lien Marking**
    - Depositories lock the pledged securities and confirm **lien marking in favour of DSP Finance**.
4. **PMR Reflection**
    - Once lien is confirmed, pledged securities are reported in the **Pledge Master Report (PMR)**.
    - **Identifiers for tracking:**
        - *Pledge Agreement Number*
        - *Pledge Sequence Number (PSN)*
5. **Uniqueness Key**
    - A new pledge request is uniquely identified by:
        
        **Depository + PSN**
        

### Deriving Open Pledge Transactions from PMR

Since there is no direct API available to fetch lien status, the **PMR (Pledge Master Report)** becomes the single source of truth for identifying pledges. To create internal records of new pledges, we apply a **deduplication logic** based on:

- **Depository (CSDL/NSDL)**
- **Pledge Sequence Number (PSN)**

This **Depository + PSN** combination forms a **uniqueness key**.

### Process:

1. **Scan PMR Entries:** The system ingests each fresh PMR file received from the depository.
2. **Check for Uniqueness:** For each line item in the PMR, the system checks whether the combination of *Depository + PSN* already exists in our database.
3. **Create Derived Transaction:**
    - If the combination is **not found**, it is treated as a **new pledge**, and an **internal open pledge transaction** is created.
    - If the combination is **already present**, it is ignored (as it has already been recorded earlier).
4. **Linking Information** – The derived transaction carries essential details like pledge agreement number, folio, ISIN, quantity, and lien date to enable reconciliation and tracking.

### Originator shared pledge information:

**Step 1: Input from originator**

- The originator initiates the lodgement process by calling the **Add Collateral API**.
- API payload (V1):
    - DEMAT account number (holder / end user / Pledgor)
    - DEMAT account number (Pledgee: Securities in favour of)
    - Loan account number / Opportunity ID (where securities should be lodged)
    - ISIN of security pledged
    - Units of security pledged
    - Depository of units pledged (NSDL/CDSL)
    - Pledge agreement number (same as PRF request reference)

In **V1**, only **one DEMAT account** can be processed per request. This simplifies reconciliation and reduces the risk of mismatches.

**Step 2: Pre-lien verification validation**

Before lien verification is attempted, the following validations are performed:

1. **Approved script validation:** Ensures the ISIN belongs to the approved list of securities.
2. **Deduplication check:** Ensures the same ISIN + DEMAT + Pledge agreement number combination is not already lodged.

Only if these validations succeed does the process proceed to lien verification, and a sync fail response is given to the originator

**Step 3: Open pledge creation**

- Once the request is created, it will look for an open for reconciliation pledged derive transaction
- The system attempts to match the details (DEMAT + ISIN + Depository + Agreement number) with existing pledge transactions.
- If a matching derived transaction is found, the status of that derived transaction is updated to **“Reconciled”** so that it cannot be re-used in reconciliation with any other request.

**Step 4: Lien verification (first pass)**

- System verifies that the securities being pledged are indeed **lien marked** in the depository system.
- At this stage, lien is validated against depository data to confirm that pledged units exist and are not released or invoked.

**Step 5: Checker decision (manual review)**

- After initial lien verification, the request passes through a **choice state** to decide whether manual checker approval is required.
- For **launch (V1)**: This will be **globally enforced** → all requests must pass through checker review.
- For **future versions**: This may be conditional, based on parameters such as:
    - **LTV value threshold** (e.g., if above a certain exposure amount)
    - **Depository type** (e.g., certain depositories requiring stricter control)
    - **Originator profile** (some partners might be fully trusted, others partially controlled)
    - **Exposure concentration** (if too much of a single ISIN is being pledged)
    
    Checker will be performing the following checks manually:
    
    - Approved script check: They will have a separate sheet/dashboard where approved scripts can be verified
    - Dedupe check: Checker will be able to track pledged securities using the Pledge agreement number and the corresponding lodgement status in the collateral tracking section of CC
    - Lien verification: Checker will go through the latest PMR to ensure that the securities are pledged

**Step 6: Post-checker lien verification (second pass)**

- Once checker approves, the system re-verifies lien with the depository to ensure securities are still intact:
    - Total **revoked securities = 0**
    - Total **invoked securities = 0**
    - Units available for pledge match request
    
    If this fails (Lodgement request will fail with status post lien status verification failure)
    

**Step 7: Lodgement in loan account**

- On successful re-verification, securities are **lodged** into the borrower’s loan account.
- Lodgement ensures:
    - Securities are tagged against the correct loan account.
    - Exposure and collateral value are updated in RMS.
    - A unique add collateral request ID is generated for traceability.

```json
[Start]
   |
   v
[Input from Originator]
   |
   v
[Pre-Lien Verification Validation]
   |---(Fail: Invalid ISIN / Duplicate Lodgement)--> [Rejected: Validation Failure]
   |
   v
[Open Pledge Creation]
   |---(Fail: No matching derived transaction)--> [Rejected: No Derived Match]
   |
   v
[Lien Verification - First Pass]
   |---(Fail: Lien not found / Units mismatch)--> [Rejected: Lien Verification Failure]
   |
   v
[Checker Review Required?]
   |---(V1: Always Yes)--->
          [Manual Checker Review]
             |---(Fail: Rejected by Checker)--> [Rejected: Checker Failure]
             |---(Pass)--> [Post-Checker Lien Verification]
   |
   v
[Post-Checker Lien Verification]
   |---(Fail: Revoked / Invoked / Units mismatch)--> [Rejected: Post-Lien Verification Failure]
   |
   v
[Lodged in Loan Account]
   |
   v
[End: Lodgement Successful]

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