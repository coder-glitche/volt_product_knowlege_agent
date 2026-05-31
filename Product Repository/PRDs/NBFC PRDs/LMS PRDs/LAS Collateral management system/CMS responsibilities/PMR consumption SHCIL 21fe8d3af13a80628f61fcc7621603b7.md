# PMR consumption: SHCIL

Decription: SHCIL PMR consumption and pledged collateral management
Owner: Vaibhav Arora
Priority Level: High
Status: Done

# **What problem are we solving?**

In a Loan Against Securities (LAS) setup, collateral positions are dynamic — securities can be lien marked, revoked, confiscated, or impacted by corporate actions at any time. For the NBFC, accurate and timely tracking of these changes is critical to:

- **Maintain exposure** by ensuring only lien-marked securities are considered as collateral.
- **Protect against credit and operational risk** by reconciling collateral transactions with actual depository data.

Why is it important?

- **Detection of lien mismatches** (e.g., securities released or confiscated without a request).
- **Promptly act on corporate actions** that affect pledged securities.
- **Collateral lifecycle visibility to** manage releases, substitutions, and invocations.
- **Track unlinked holdings** from pending applications of customers

The **Pledge Master Report (PMR)**, received periodically from the depository, provides an authoritative and up-to-date view of the NBFCs lien marked holdings and pledge status. By systematically consuming and integrating PMR data, we can:

- Verify lien status
- Reconcile pledged holdings between NBFC records and the depository.
- Manage the full collateral transaction lifecycle, from pledge to release or invocation.
- Identify and manage unlinked collateral to avoid coverage gaps.
- Detect and act upon corporate actions impacting pledged securities.

---

# **How do we measure success?**

Success of PMR consumption will be measured by a combination of:

- **Lifecycle Tracking Accuracy** – % of collateral transactions (release, confiscation, substitution, lien marking) correctly captured and reflected in CMS.
- **Reconciliation Accuracy** – % match between NBFC’s lodged securities and PMR holdings in CMS.
- **Corporate Action Capture Rate** – % of pledged securities impacted by corporate actions correctly identified and updated.

---

# **How are others solving this problem?**

Currently, CDSL and NSDL do not provide lien verification APIs (unlike KFIN and CAMS for mutual funds). As a result, lenders depend on operational processes where PMRs are periodically consumed, and collateral transactions are manually approved or rejected based on this data.

Benchmarking with TCL indicates a similar approach — PMRs are ingested, and lodgement requests are approved or rejected through operational workflows using the report as the source of truth.

---

# **What is the solution?**

We will integrate **Pledge Master Report (PMR) consumption** into the Collateral Management System (CMS) to create a single, authoritative repository of all securities lien-marked in favour of the NBFC.

The PMR, received periodically from the depository, will be ingested into CMS and transformed into a structured collateral database. This will allow:

- **Automated lien verification** against depository records.
- **Accurate reconciliation** of pledged holdings between NBFC and depository data.
- **End-to-end collateral transaction lifecycle management** — tracking lien marking, revocation, substitution, and invocation.
- **NBFC-specific pledged collateral tracking** to maintain exposure accuracy.
- **Unlinked collateral identification and resolution** for pending customer applications.
- **Corporate action tracking** for pledged securities to manage risk and operational impact.

This approach ensures **real-time visibility, operational efficiency, and data integrity** across all pledged collateral, enabling faster decision-making and improved risk control.

## Requirements overview (optional)

## User stories / User flow

## Requirements

### Scope

Ingest CDSL and NSDL PMR CSVs (holding-style, full-position reports) into CMS to build a single authoritative collateral repository for all securities lien-marked in favour of the NBFC. The repository will be the source for **lien verification**, **collateral lifecycle management**, **reconciliation**, and **corporate action identification**.

### Source data:

- **Files:** CSV (one from CDSL, one from NSDL)
- **Delivery method:** Operations team will upload via CMS UI.
- **Frequency / Window:** Hourly files between **09:30 – 18:00**. Each file is a full holding-style report containing all pledges up to that timestamp (incremental in time, full in content).
- **Stability:** Columns / order are fixed per source (will not change). Two distinct schemas (CDSL vs NSDL).

**Sample (CSV row) — CDSL**

```json

PledgeSeqNo,PledgeStatus,ISIN,ISINDescription,PledgeQuantity,TotalUnpledgeAccQty,TotalConfiscationAccQty,ParentPSN,AgreementNumber,PledgeAcceptVerifiedDt,PledgeCloseDt,PledgeExpiryDt,LockinExpDate,LockinReason,PledgorDP,PledgorClientID,PledgeeDP,PledgeeClientID
337932324,Accepted,INE163A01018,NOCCL LI EQTY SHARES,2500,200,2300,0,2037,21082023:162142,01082025:165210,20082024,, ,INxxxxxx,12345678,INxxxxxx,87654321

```

**Sample (CSV row) — NSDL**

```json

PledgeInstructionNo,UniqueID,ISIN,ISINDescription,PledgeQuantity,ClosedQuantity,InvokedQuantity,Status,ClosureDate,AgreementNo,PledgeType,ExecutionDate,PledgorDP,PledgorClientID,PledgeeDP,PledgeeClientID
10000013414521,ABC123,INE009A01021,INFOSYS LIMITED EQ FV RS 5,117,117,0,Closed,31-03-2025,A9080910006632,Pledge,27-09-2022,IN300214,26844899,21714715,21714715

```

### Collateral mapping

| CMS Key | NSDL Key | CDSL Key | Logic to Compute | Trigger (populate/update) |
| --- | --- | --- | --- | --- |
| pledge_id | N/A | N/A | Generate UUID at first ingestion | On first detection of pledge record (Uniqueness will be defined basis PSN) |
| Depository | Static = "NSDL" | Static = "CDSL" | Based on file being parsed | Always |
| pledge_seq_no / unique_id | `UniqueID` | `PledgeSeqNo` | Direct mapping | Always |
| pledge_instruction_no / parent_psn | `PledgeInstructionNo` | `ParentPSN` | Direct mapping | Always |
| agreement_number | `AgreementNo` | `AgreementNumber` | Direct mapping | Always |
| isin | `ISIN` | `ISIN` | Direct mapping | Always |
| isin_description | `ISINDescription` | `ISINDescription` | Direct mapping | Always |
| pledgor_dp | `PledgorDP` | `PledgorDP` | Direct mapping | Always |
| pledgor_client_id | `PledgorClientID` | `PledgorClientID` | Direct mapping | Always |
| pledgee_dp | `PledgeeDP` | `PledgeeDP` | Direct mapping | Always |
| pledgee_client_id | `PledgeeClientID` | `PledgeeClientID` | Direct mapping | Always |
| units_lien_marked | `PledgeQuantity` | `PledgeQuantity` | Direct mapping | Always |
| units_revoked | `ClosedQuantity` | `TotalUnpledgeAccQty` | Direct mapping | Always; if value increases, create Revocation txn |
| units_invoked | `InvokedQuantity` | `TotalConfiscationAccQty` | Direct mapping | Always; if value increases, create Invocation txn |
| available_units | N/A | N/A | `units_lien_marked - units_revoked - units_invoked` | On each ingestion/update |
| status | `Status` → Canonical Map | `PledgeStatus` → Canonical Map | Use status mapping table | Always |
| pledge_created_on | `ExecutionDate` | `PledgeAcceptVerifiedDt` | Parse date from source | On first detection |
| pledge_closed_on | `ClosureDate` | `PledgeCloseDt` | Parse date if provided | When source provides close date |
| lockin_reason | (NSDL: no direct field) | `LockinReason` | Direct mapping (CDSL only) | If present |
| lockin_expiry_date | (NSDL: no direct field) | `LockinExpDate` | Parse date if present | If present |
| last_pmr_received_on | N/A | N/A | System timestamp of ingestion | On every ingestion |
| raw_row | Entire CSV row | Entire CSV row | Store raw | Always |

### Collateral transactions:

| CMS Key | NSDL Key | CDSL Key | Logic to Compute | Trigger (populate/update) |
| --- | --- | --- | --- | --- |
| transaction_id | N/A | N/A | Generate UUID | On transaction creation |
| pledge_id (FK) | Derived from matching pledge_seq_no/unique_id | Derived from matching pledge_seq_no/unique_id | Link to `pledged_collateral` | On transaction creation |
| txn_type | Derived from status change or quantity delta | Derived from status change or quantity delta | - If `ClosedQuantity` ↑ → Revocation- If `InvokedQuantity` ↑ → Invocation- If status = Pledged-CI → Corporate Invocation marker- If ISIN change with same ParentPSN/PIN → Substitution | On detection of event |
| txn_units_delta | Difference between new and previous values of relevant quantity | Difference between new and previous values of relevant quantity | For Revocation: ΔClosedQuantity / ΔTotalUnpledgeAccQtyFor Invocation: ΔInvokedQuantity / ΔTotalConfiscationAccQtyFor Substitution: units difference in CA event | On transaction creation |
| txn_isin | `ISIN` (for CA/Substitution) | `ISIN` (for CA/Substitution) | Direct mapping from CA row | Only for Substitution or CA event |
| parent_psn / pledge_instruction_no | `PledgeInstructionNo` | `ParentPSN` | Direct mapping | Always |
| detected_on | N/A | N/A | System timestamp when delta detected | On transaction creation |
| reconciliation_status | N/A | N/A | Default = Open; updated when matched to request | On transaction creation; updated on reconciliation |
| mapped_request_id | N/A | N/A | Set when matched to a LMS lodge/release/invocation request | On reconciliation |
| raw_pmr_reference | N/A | N/A | Store file timestamp + row ID from ingestion | On transaction creation |

### Processing rules (ingest → detect → persist)

### Ingestion & validation

- Only consume rows marked **Verified** where applicable (CDSL: Initiated/Verified = Verified). If verified flag is absent, ignore the transaction.
- Update/Insert into `pledged_collateral` keyed by `source` + `pledge_seq_no/unique_id`. If record exists, treat as updated state (full-position semantics).

### Lien identification (new pledge detection)

- **CDSL:** treat new lien when `PledgeStatus = Accepted` AND `PSN` (pledge agreement) does not already exist in CMS. Create a `pledged_collateral` entry with status = `Open / Lodgement Pending` until LMS lodgement occurs.
- **NSDL:** treat new lien when `Status = Pledged` AND `UniqueID` (or AgreementNo) does not already exist in CMS. Create entry status = `Open / Lodgement Pending` until LMS lodgement occurs.

> Lodgement status: the collateral remains open in CMS until a corresponding lodgement record in LMS matches the pledge (matching on demat account = pledgor_dp+client and pledge identifiers). This is a separate integration.
> 

MF: Lien ref number+ ISIN + Folio

Shares: DEMAT account number + ISIN + Pledge agreement number

### Transaction identification rules (PMR derived rules)

- For an incoming PMR row mapped to an existing `pledged_collateral`:
    - If `TotalUnpledgeAccQty` (CDSL) or `ClosedQuantity` (NSDL) **increased** from last stored value → create **Revocation / Release** transaction with `txn_units_delta = new_closed - prev_closed`.
    - If `TotalConfiscationAccQty` (CDSL) or `InvokedQuantity` (NSDL Invoked) **increased** → create **Invocation / Confiscation** transaction with delta = new_invoked - prev_invoked.
    - **Substitution detection**
        - **Unit substitution (same ISIN):** New PMR row Pledge-CI (status/txn type) with same PSN/ParentPSN and same ISIN and units increased in a correlated way → create `Substitution` transaction capturing ratio (units added : units existing).
        - **ISIN substitution (isin swap):** New Pledge-CI row with same PSN/ParentPSN but **different ISIN** → create `Substitution` transaction flagged as ISIN-swap. Create internal CA-substitution feed requiring ratio input to finalize.
    - **Corporate Action marker:** If incoming row `Status` = `Pledged-CI` (CDSL) or equivalent NSDL marker, treat it as a corporate action event and create + queue a `corporate_action` feed for ratio / resolution.
- For any detected transaction, create a `collateral_transactions` row with `reconciliation_status = Open` until matched to an operational request.

### Reconciliation mapping

- For PMR-derived release/invocation transactions, attempt auto-match to existing LMS requests (release / invocation) by matching: demat account, pledge identifiers, units, and timestamps. (Logic to be closed separately)
- If no match found, reconciliation_status remains `Open` and the transaction stays in the queue for ops/manual mapping (store indefinitely).

### Status mapping

Map source statuses to CMS canonical ones:

- **Pledged** (NSDL) → `Pledged`
- **Accepted** (CDSL) → `Accepted` (may be partial)
- **Partially Closed** → `Partially Closed`
- **Partially Invoked** → `Partially Invoked`
- **Partial Closed/Invoked** → `Partially Closed/Invoked`
- **Closed** → `Closed`

Status semantics:

- `Pledged` / `Accepted` → collateral still active (available_units > 0).
- `Partially Closed` / `Partially Invoked` → mixture; available_units adjusted.
- `Closed` → available_units = 0; pledge_closed_on should be set.

### Business rules

- **Available units formula**
    
    ```
    
    available_units = units_lien_marked - units_revoked - units_invoked
    
    ```
    
- **Uniqueness:** pledge agreement number / pledge_seq_no / unique_id must be unique per source. On duplicate incoming IDs, verify if truly duplicate or a stale file;
- **Parent key for CA:** use CDSL.ParentPSN or NSDL.PledgeInstructionNo (PIN) to associate corporate action records to existing pledge entries. New `Pledged-CI` rows referencing those association keys denote CA events.
- **Store raw rows and file timestamp** for audit and rollback.
- **Do not delete** open transactions automatically—store indefinitely until mapped/closed by ops or request mapping.
- **Consumption validation:** only rows with Verified (where present) should be consumed; others stored in a `pending` bucket for ops review. (For rows which failed parsing, create a checker task for the operations team to review)

### Edge cases and error handling:

- **Duplicate agreement numbers across different pledgor DPs**: treat as conflict; raise for manual resolution.
- **ParentPSN/PIN absent on Corporate actions rows**: store CA as `orphan` and flag ops. (Pledge type should be Pledged-CI / Accepted-CI)
- **Partial / stale files**: detect file timestamp regression (older file uploaded after newer); discard unless ops confirms reprocessing. - If existing pledge transactions do not exist in the new file that is being procesed, mark file as stale and create approval task)

### Detection (Sample)

1. **Revocation**
    - Prev: units_revoked = 100; incoming PMR: TotalUnpledgeAccQty = 150 → create Revocation txn with delta = 50; reconciliation_status = Open.
2. **Invocation**
    - Prev: units_invoked = 0; incoming PMR: TotalConfiscationAccQty = 10 → create Invocation txn with delta = 10; reconciliation_status = Open.
3. **ISIN substitution (CA)**
    - Existing pledge PSN = 1001, ISIN = X, units = 100. Incoming `Pledged-CI` with PSN = 1001, ISIN = Y, units = 200 → create `corporate_action` (ISIN swap), expect ratio input to compute mapping, then create substitution transaction.

**CDSL parameters:**

| **Parameter** | **Value** | Description | To be consumed |
| --- | --- | --- | --- |
| Pledge Seq. No. | 337932324 | Unique collateral lien marking reference number, similar to lien marking number | Yes |
| Pledge Status | Closed | Current status of collateral, possible values:
- Accepted
- Closed | Yes |
| Pledge Value | 561875.000 | Total value of collateral lien marked in the transaction | No |
| ISIN | INE163A01018 | International Securities Identification Number | Yes |
| ISIN Description | NOCCL LI EQTY SHARES | Name of the security / Scrip name | Yes |
| Pledge Quantity | 2500.000 | Total number of units lien marked in the transaction | Yes |
| Total Unpledge Acc Qty | 200.000 | Total number of units released since the security was lien marked | Yes |
| Total Confiscation Acc Qty | 2300.000 | Total number of units confiscated (step 1 of invocation) since the security was lien marked | Yes |
| Initiated/Verified | Verified | Verification status, we will only place a validation to consume verified row items | No |
| Parent PSN | 0 | Association key, used for corporate actions, in corporate action transaction, parent PSN is same as PSN | Yes |
| Agreement Number | 2037 | Pledge agreement number, unique request ID for the request | Yes |
| Pledge Setup Initiated Dt. | 21082023:162142 | Pledge initiated on | No |
| Pledge Setup Verified Dt. | 21082023:162142 | Pledge setup confirmed at | No |
| Pledge Accept Initiated Dt. | 21082023:162142 | Pledge accepted initiated at | No |
| Pledge Accept Verified Dt. | 21082023:162142 | Pledge accepted confirmed at | Yes |
| Pledge Reversal Dt. | — | NA |  |
| Pledge Close Dt. | 01082025:165210 | Pledge closure date (date of release of all securities) | Yes |
| Pledge Expiry Dt. | 20082024 | Date of expiry of pledge (has to be closed what date will be this, has to be more than tenure date)  | Yes |
| Pledge for | FREE | NA | No |
| Lockin ID | — | NA |  |
| Lockin Exp. Date | — | Reason if securities are locked - Not sure on what scenarios this would arise, will only consume for now | Yes |
| Lockin Reason | — | Reason if securities are locked - Not sure on what scenarios this would arise, will only consume for now | Yes |
| Pledgor DP |  | DP ID for the customer | Yes |
| Pledgor Client ID |  | Client ID for the user, pledgor DP and client ID combine to form the DEMAT account number | Yes |
| Pledgee client ID |  | DP ID for the NBFC (DSP FInance) | Yes |
| Pledgee client ID |  | Client ID for the NBFC (DSP Finance), pledgor DP and client ID combine to form the DEMAT account number | Yes |

NSDL parameters

| **Parameter** | **Value** | Description | To be consumed |
| --- | --- | --- | --- |
| Pledgor DP | IN300214 | DP ID for the customer | Yes |
| Pledgor DP Name | KOTAK SECURITIES LIMITED | DP name for the user | No |
| Pledgee Client | 21714715 | DP ID for the NBFC (DSP FInance) | Yes |
| Pledgee Client Name | TATA CAPITAL LIMITED | DP name for the client | No |
| Pledgor Client | 26844899 | Client ID for the user, pledgor DP and client ID combine to form the DEMAT account number | Yes |
| Pledgor Client Name | ANUJ KUMAR SINGHANIA HUF | User name | No |
| Pledge Instruction No.  | 10000013414521 | Association key, similar to Parent PSN (CDSL) | Yes |
| Unique ID |  | Unique collateral lien marking reference number, similar to lien marking number similar to PSN | Yes |
| ISIN (1st row) | INE009A01021 | International Securities Identification Number | Yes |
| ISIN Description (1st row) | INFOSYS LIMITED EQ FV RS 5 | Name of the security / Scrip name | Yes |
| Pledge Quantity (1st row) | 117 | Total number of units lien marked in the transaction | Yes |
| Closed Quantity (1st row) | 117 | Total number of units released since the security was lien marked | Yes |
| Status  | Closed | Current status of collateral, possible values:
- Pledged
- Closed
- Partially closed
- Partially invoked
- Partially closed/invoked | Yes |
| Closure Date  | 31-Mar-2025 | Pledge closure date (date of release of all securities) | Yes |
| Agreement No.  | A9080910006632 | Pledge agreement number, unique request ID for the request | Yes |
| Pledge Type (1st row) | Pledge | Type of transaction (Pledge) | Yes |
| Execution Date (1st row) | 27-09-2022 | Date of execution of pledge | Yes |

Images:

![CDSL sample PMR](PMR%20consumption%20SHCIL/image_(9).png)

CDSL sample PMR

![NSDL sample PMR](PMR%20consumption%20SHCIL/image_(10).png)

NSDL sample PMR

---

# Workflow

![image.png](PMR%20consumption%20SHCIL/image.png)

---

# **Analytics**

Na

---

# **Timeline/Release Planning**

NA

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