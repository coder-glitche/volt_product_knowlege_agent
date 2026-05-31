# PMR consumption

Last Edited: May 19, 2026 5:45 PM
PRD ETA: May 19, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

# PMR Automated Email Consumption: Product Note

---

## What problem are we solving?

Today, Pledge Master Reports (PMRs) are received over email at [collaterals@dspfin.com](mailto:collaterals@dspfin.com). The ops team shares these with engineering, who manually hit an API to consume the report - creating an operational bottleneck that directly impacts loan account opening timelines for the Loan Against Shares (LAS) program.

We need to eliminate this manual handoff by automating PMR ingestion the moment the email arrives, while preserving a checker workflow for validation and audit.

In a Loan Against Securities (LAS) setup, collateral positions are dynamic securities can be lien marked, revoked, confiscated, or impacted by corporate actions at any time. For the NBFC, accurate and timely tracking of these changes is critical to:

- Maintain exposure by ensuring only lien-marked securities are considered as collateral
- Protect against credit and operational risk by reconciling collateral transactions with actual depository data
- Enable detection of lien mismatches (e.g., securities released or confiscated without a request)
- Provide collateral lifecycle visibility to manage releases, substitutions, and invocations
- Track unlinked holdings from pending customer applications

The Pledge Master Report (PMR), received periodically from the depository, provides an authoritative and up-to-date view of the NBFC's lien-marked holdings and pledge status. By systematically consuming and integrating PMR data, we can:

- Verify lien status
- Reconcile pledged holdings between NBFC records and the depository
- Manage the full collateral transaction lifecycle, from pledge to release or invocation
- Identify and manage unlinked collateral to avoid coverage gaps
- Detect and act upon corporate actions impacting pledged securities

---

## Why is it important?

Currently, the PMR email arrives at a group inbox and is manually handed off to the engineering team, who trigger an API call to consume it. This process:

- Creates an unnecessary operational dependency on engineering for a routine data ingestion task
- Introduces latency in collateral data being reflected in CMS
- Directly delays loan account opening timelines for the LAS program
- Is not scalable as PMR frequency increases (hourly files between 09:30–18:00)

Automating this end-to-end - with a system maker and a human checker - removes the bottleneck while preserving auditability and control.

---

## How do we measure success?

| Metric | Description |
| --- | --- |
| Engineering Dependency Eliminated | Engineering team no longer manually called upon to trigger PMR API |
| Lifecycle Tracking Accuracy | % of collateral transactions (release, confiscation, substitution, lien marking) correctly captured and reflected in CMS |
| Reconciliation Accuracy | % match between NBFC's lodged securities and PMR holdings in CMS |
| Corporate Action Capture Rate | % of pledged securities impacted by corporate actions correctly identified and updated |
| Checker Task SLA | % of checker tasks approved within defined ops SLA window |

---

## How are others solving this problem?

CDSL and NSDL do not provide lien verification APIs (unlike KFIN and CAMS for mutual funds). As a result, lenders depend on operational processes where PMRs are periodically consumed, and collateral transactions are manually approved or rejected based on this data.

Benchmarking with TCL indicates a similar approach - PMRs are ingested, and lodgement requests are approved or rejected through operational workflows using the report as the source of truth.

---

## What is the solution?

### Approach: Automated Maker + Checker Flow

Rather than requiring ops to manually download and upload the file (maker-checker via UI), we automate the **maker step** - the system listens to the group email, detects PMR emails, ingests the CSV, and creates a checker task on Command Centre for ops to review and approve.

Email arrives at [collaterals@dspfin.com](mailto:collaterals@dspfin.com)
↓
System identifies PMR email via subject line pattern
↓
CSV attachment parsed → CDSL or NSDL identified via filename and mime type
↓
File ingested into CMS (automated maker)
↓
Checker task created on Command Centre → Ops reviews & approves

We will integrate Pledge Master Report (PMR) consumption into the Collateral Management System (CMS) to create a single, authoritative repository of all securities lien-marked in favour of the NBFC. The PMR, received periodically from the depository, will be ingested into CMS and transformed into a structured collateral database. This will allow:

- Automated lien verification against depository records
- Accurate reconciliation of pledged holdings between NBFC and depository data
- End-to-end collateral transaction lifecycle management - tracking lien marking, revocation, substitution, and invocation
- NBFC-specific pledged collateral tracking to maintain exposure accuracy
- Unlinked collateral identification and resolution for pending customer applications
- Corporate action tracking for pledged securities to manage risk and operational impact

---

## Requirements

### Email Identification

- **Inbox:** [collaterals@dspfin.com](mailto:collaterals@dspfin.com) (existing group email, or a new dedicated one)
- **Subject pattern to match:** Contains `PMR report` or similar identifier
    - Example subject: `PMR report All - for CL ID - 41819492 and 1601010000607033 In PDF and CSV`
- **Attachment type:** Only CSV attachments to be consumed; PDF attachments ignored

### Depository Identification (via Filename)

| Substring in Filename | Depository |
| --- | --- |
| `9492CSV.csv` | CDSL |
| `41819492.csv` | NSDL |

A basic substring check on the filename will be used to associate the file with the corresponding depository.

### Data Consumed from Email

| Field | Source |
| --- | --- |
| Date | Date of the email |
| File name | Used for depository identification |
| CSV rows | Parsed per CDSL / NSDL schema (refer to existing PMR Consumption PRD) |

---

## Scope

Ingest CDSL and NSDL PMR CSVs (holding-style, full-position reports) into CMS to build a single authoritative collateral repository for all securities lien-marked in favour of the NBFC. The repository will be the source for lien verification, collateral lifecycle management, reconciliation, and corporate action identification.

**Source data:**

- Files: CSV (one from CDSL, one from NSDL)
- Delivery method: Automated ingestion from email ([collaterals@dspfin.com](mailto:collaterals@dspfin.com))
- Frequency / Window: Hourly files between 09:30–18:00. Each file is a full holding-style report containing all pledges up to that timestamp (incremental in time, full in content)
- Stability: Columns / order are fixed per source (will not change). Two distinct schemas (CDSL vs NSDL)

---

## User Flow

### Automated Maker (System)

1. Email arrives at [collaterals@dspfin.com](mailto:collaterals@dspfin.com)
2. System detects email subject matches PMR pattern
3. CSV attachment is extracted from the email
4. Filename is checked for depository substring → mapped to CDSL or NSDL
5. CSV is parsed and validated per the relevant schema
6. Rows marked as Verified (where applicable) are consumed; others moved to a pending bucket
7. Collateral records are created/updated in CMS per existing PMR consumption logic
8. A unique Suspension Action ID is generated for this consumption event
9. Checker task is automatically created on Command Centre → Bulk Ops

### Checker (Ops)

1. Ops receives checker task in Command Centre → Bulk Ops
2. Reviews task details: file date, request date, maker remarks, request ID
3. Approves or rejects the consumption
4. On approval, consumption is confirmed and collateral data is live in CMS
5. On rejection, consumption is flagged for review and escalation

---

## Checker Task - Command Centre

Every automated PMR ingestion creates a **checker task** in the **Bulk Ops** section of Command Centre.

### Task Parameters

| Field | Value |
| --- | --- |
| **Name** | Pledge master report update |
| **Approval Status** | Pending for approval |
| **Request ID** | Unique Suspension Action ID generated per consumption |
| **Sub Status** | Pending for approval |
| **Request Date** | Date of consumption (system timestamp) |
| **File Date** | Date of the source email |
| **Maker Name** | System |
| **Maker Remarks** | Automated consumption from email |
| **Maker Created On** | Task creation timestamp |
| **Task Description** | Approval required for PMR consumption |

### UI Notes

- The checker task **must not include a "Regenerate" option**
- Checker will have **Approve** and **Cancel** actions only
- This feature sits within the **Bulk Ops section** of Command Centre

---

## Collateral Mapping

### Pledged Collateral Table

| CMS Key | NSDL Key | CDSL Key | Logic to Compute | Trigger |
| --- | --- | --- | --- | --- |
| pledge_id | N/A | N/A | Generate UUID at first ingestion | On first detection of pledge record |
| Depository | Static = "NSDL" | Static = "CDSL" | Based on file being parsed | Always |
| pledge_seq_no / unique_id | UniqueID | PledgeSeqNo | Direct mapping | Always |
| pledge_instruction_no / parent_psn | PledgeInstructionNo | ParentPSN | Direct mapping | Always |
| agreement_number | AgreementNo | AgreementNumber | Direct mapping | Always |
| isin | ISIN | ISIN | Direct mapping | Always |
| isin_description | ISINDescription | ISINDescription | Direct mapping | Always |
| pledgor_dp | PledgorDP | PledgorDP | Direct mapping | Always |
| pledgor_client_id | PledgorClientID | PledgorClientID | Direct mapping | Always |
| pledgee_dp | PledgeeDP | PledgeeDP | Direct mapping | Always |
| pledgee_client_id | PledgeeClientID | PledgeeClientID | Direct mapping | Always |
| units_lien_marked | PledgeQuantity | PledgeQuantity | Direct mapping | Always |
| units_revoked | ClosedQuantity | TotalUnpledgeAccQty | Direct mapping | Always; if value increases, create Revocation txn |
| units_invoked | InvokedQuantity | TotalConfiscationAccQty | Direct mapping | Always; if value increases, create Invocation txn |
| available_units | N/A | N/A | units_lien_marked - units_revoked - units_invoked | On each ingestion/update |
| status | Status → Canonical Map | PledgeStatus → Canonical Map | Use status mapping table | Always |
| pledge_created_on | ExecutionDate | PledgeAcceptVerifiedDt | Parse date from source | On first detection |
| pledge_closed_on | ClosureDate | PledgeCloseDt | Parse date if provided | When source provides close date |
| lockin_reason | (no direct field) | LockinReason | Direct mapping (CDSL only) | If present |
| lockin_expiry_date | (no direct field) | LockinExpDate | Parse date if present | If present |
| last_pmr_received_on | N/A | N/A | System timestamp of ingestion | On every ingestion |
| raw_row | Entire CSV row | Entire CSV row | Store raw | Always |

### Collateral Transactions Table

| CMS Key | Logic to Compute | Trigger |
| --- | --- | --- |
| transaction_id | Generate UUID | On transaction creation |
| pledge_id (FK) | Link to pledged_collateral | On transaction creation |
| txn_type | If ClosedQuantity ↑ → Revocation; If InvokedQuantity ↑ → Invocation; If status = Pledged-CI → Corporate Invocation; If ISIN change with same ParentPSN → Substitution | On detection of event |
| txn_units_delta | For Revocation: ΔClosedQuantity / ΔTotalUnpledgeAccQty; For Invocation: ΔInvokedQuantity / ΔTotalConfiscationAccQty | On transaction creation |
| txn_isin | Direct mapping from CA row | Only for Substitution or CA event |
| parent_psn / pledge_instruction_no | Direct mapping | Always |
| detected_on | System timestamp when delta detected | On transaction creation |
| reconciliation_status | Default = Open; updated when matched to request | On transaction creation; updated on reconciliation |
| mapped_request_id | Set when matched to LMS lodge/release/invocation request | On reconciliation |
| raw_pmr_reference | Store file timestamp + row ID from ingestion | On transaction creation |

---

## Processing Rules

### Ingestion & Validation

- Only consume rows marked Verified where applicable (CDSL: Initiated/Verified = Verified). If verified flag is absent, ignore the transaction
- Update/Insert into pledged_collateral keyed by source + pledge_seq_no/unique_id. If record exists, treat as updated state (full-position semantics)

### Lien Identification (New Pledge Detection)

- **CDSL:** treat new lien when PledgeStatus = Accepted AND PSN (pledge agreement) does not already exist in CMS. Create a pledged_collateral entry with status = Open / Lodgement Pending until LMS lodgement occurs
- **NSDL:** treat new lien when Status = Pledged AND UniqueID (or AgreementNo) does not already exist in CMS. Create entry status = Open / Lodgement Pending until LMS lodgement occurs
- Lodgement status: collateral remains open in CMS until a corresponding lodgement record in LMS matches the pledge (matching on demat account = pledgor_dp+client and pledge identifiers)

### Transaction Identification Rules

For an incoming PMR row mapped to an existing pledged_collateral:

- If TotalUnpledgeAccQty (CDSL) or ClosedQuantity (NSDL) increased from last stored value → create **Revocation / Release** transaction with txn_units_delta = new_closed - prev_closed
- If TotalConfiscationAccQty (CDSL) or InvokedQuantity (NSDL) increased → create **Invocation / Confiscation** transaction with delta = new_invoked - prev_invoked

### Substitution Detection

- **Unit substitution (same ISIN):** New PMR row Pledge-CI with same PSN/ParentPSN and same ISIN and units increased in a correlated way → create Substitution transaction capturing ratio (units added : units existing)
- **ISIN substitution (ISIN swap):** New Pledge-CI row with same PSN/ParentPSN but different ISIN → create Substitution transaction flagged as ISIN-swap. Create internal CA-substitution feed requiring ratio input to finalize
- **Corporate Action marker:** If incoming row Status = Pledged-CI (CDSL) or equivalent NSDL marker, treat it as a corporate action event and create + queue a corporate_action feed for ratio / resolution

### Reconciliation Mapping

- For PMR-derived release/invocation transactions, attempt auto-match to existing LMS requests by matching: demat account, pledge identifiers, units, and timestamps
- If no match found, reconciliation_status remains Open and the transaction stays in the queue for ops/manual mapping (stored indefinitely)

### Status Mapping

| Source Status | CMS Canonical Status |
| --- | --- |
| Pledged (NSDL) | Pledged |
| Accepted (CDSL) | Accepted |
| Partially Closed | Partially Closed |
| Partially Invoked | Partially Invoked |
| Partial Closed/Invoked | Partially Closed/Invoked |
| Closed | Closed |

**Status semantics:**

- Pledged / Accepted → collateral still active (available_units > 0)
- Partially Closed / Partially Invoked → mixture; available_units adjusted
- Closed → available_units = 0; pledge_closed_on should be set

---

## Business Rules

**Available units formula:**

available_units = units_lien_marked - units_revoked - units_invoked

- **Uniqueness:** pledge agreement number / pledge_seq_no / unique_id must be unique per source. On duplicate incoming IDs, verify if truly duplicate or a stale file
- **Parent key for CA:** use CDSL.ParentPSN or NSDL.PledgeInstructionNo (PIN) to associate corporate action records to existing pledge entries. New Pledged-CI rows referencing those association keys denote CA events
- **Audit:** Store raw rows and file timestamp for audit and rollback
- **Open transactions:** Do not delete open transactions automatically - store indefinitely until mapped/closed by ops or request mapping
- **Consumption validation:** Only rows with Verified (where present) should be consumed; others stored in a pending bucket for ops review. For rows which failed parsing, create a checker task for the operations team to review

---

## Edge Cases & Error Handling

| Scenario | Handling |
| --- | --- |
| Duplicate agreement numbers across different pledgor DPs | Treat as conflict; raise for manual resolution |
| ParentPSN/PIN absent on Corporate Action rows | Store CA as orphan and flag ops (Pledge type should be Pledged-CI / Accepted-CI) |
| Stale file detected (older file uploaded after newer) | Discard unless ops confirms reprocessing. If existing pledge transactions do not exist in the new file being processed, mark file as stale and create approval task |
| Rows that fail parsing | Create a separate checker task for ops review |
| Email arrives with only PDF, no CSV | No consumption triggered; optionally notify ops |

---

## Detection Examples

### Revocation

- Prev: units_revoked = 100; incoming PMR: TotalUnpledgeAccQty = 150 → create Revocation txn with delta = 50; reconciliation_status = Open

### Invocation

- Prev: units_invoked = 0; incoming PMR: TotalConfiscationAccQty = 10 → create Invocation txn with delta = 10; reconciliation_status = Open

### ISIN Substitution (Corporate Action)

- Existing pledge PSN = 1001, ISIN = X, units = 100. Incoming Pledged-CI with PSN = 1001, ISIN = Y, units = 200 → create corporate_action (ISIN swap), expect ratio input to compute mapping, then create substitution transaction

---

## CDSL Parameters Consumed

| Parameter | Description |
| --- | --- |
| Pledge Seq. No. | Unique collateral lien marking reference number |
| Pledge Status | Current status of collateral (Accepted, Closed) |
| ISIN | International Securities Identification Number |
| ISIN Description | Name of the security / Scrip name |
| Pledge Quantity | Total number of units lien marked |
| Total Unpledge Acc Qty | Total number of units released |
| Total Confiscation Acc Qty | Total number of units confiscated |
| Parent PSN | Association key used for corporate actions |
| Agreement Number | Pledge agreement number |
| Pledge Accept Verified Dt | Pledge accepted confirmed at |
| Pledge Close Dt | Pledge closure date |
| Pledge Expiry Dt | Date of expiry of pledge |
| Lockin Exp. Date | Expiry date if securities are locked |
| Lockin Reason | Reason if securities are locked |
| Pledgor DP | DP ID for the customer |
| Pledgor Client ID | Client ID for the user |
| Pledgee DP | DP ID for the NBFC (DSP Finance) |
| Pledgee Client ID | Client ID for the NBFC (DSP Finance) |

---

## NSDL Parameters Consumed

| Parameter | Description |
| --- | --- |
| Pledgor DP | DP ID for the customer |
| Pledgor Client | Client ID for the user |
| Pledgee Client | DP ID for the NBFC (DSP Finance) |
| Pledge Instruction No. | Association key, similar to Parent PSN (CDSL) |
| Unique ID | Unique collateral lien marking reference number |
| ISIN | International Securities Identification Number |
| ISIN Description | Name of the security / Scrip name |
| Pledge Quantity | Total number of units lien marked |
| Closed Quantity | Total number of units released |
| Invoked Quantity | Total number of units invoked |
| Status | Current status of collateral |
| Closure Date | Pledge closure date |
| Agreement No. | Pledge agreement number |
| Pledge Type | Type of transaction |
| Execution Date | Date of execution of pledge |

---

## Analytics

NA

---

## Timeline / Release Planning

NA

---

## Go to Market

- **Marketing:** NA
- **Ops & Sales Training:** Checker workflow and task approval process to be covered in ops training
- **FAQs:** To be added post UAT

---

## Action Items / Checklist

### Product

- [ ]  Finalise email identification logic (subject pattern + sender whitelist if needed)
- [ ]  Confirm inbox strategy - use [collaterals@dspfin.com](mailto:collaterals@dspfin.com) or create a dedicated PMR inbox
- [ ]  Define error handling flows for malformed / missing CSVs
- [ ]  Confirm checker task placement in Bulk Ops section of Command Centre

### Business

- [ ]  Confirm checker ownership and approval SLA
- [ ]  Align on frequency expectations and weekend/holiday handling

### Design

- [ ]  Design checker task UI per parameters above (no Regenerate option, Approve + Cancel only)
- [ ]  Confirm Bulk Ops section layout and task card design

---

## Open Questions

- [ ]  Should we use [collaterals@dspfin.com](mailto:collaterals@dspfin.com) directly or create a dedicated inbox for PMR emails?
- [ ]  What constitutes a valid PMR email beyond subject pattern - do we need additional sender validation?
- [ ]  What should happen if the email arrives with only a PDF and no CSV?
- [ ]  Should failed parsing rows create a separate checker task or be bundled into the same one?
- [ ]  Who are the designated checkers for this task on Command Centre, and what is the approval SLA?

---

## Feedback

---

## Learnings & Next Steps

---

## Appendix

- PMR Consumption PRD (existing) - referenced for collateral mapping, processing rules, and depository schemas
- Checker UI reference - Mandate Presentation Details modal pattern (Approve + Cancel, no Regenerate)

### Meeting Notes