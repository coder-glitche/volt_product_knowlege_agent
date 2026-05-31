# Approved Scrips productisation

Last Edited: May 8, 2026 12:03 PM
PRD ETA: April 21, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

## Background and Context

The approved scrip list is the master reference that controls which ISINs can be pledged as collateral in the LMS, and at what LTV. It has two layers:

- **Finflux approved scrip** — Global NBFC-level list managed in the LMS (Finflux). Stores min LTV and max LTV per ISIN and enforces that no lodged collateral exceeds max LTV.

(Min LTV for default LTV value, Max LTV as a ceiling validation) - Finflux max LTV should be equal to Risk LTV and Finflux min LTV should be equal to Fenix min LTV

- **Fenix approved scrip** — Internal list managed at a co-lender relationship (contract) level (colending vs non-colending) and product level (LAS and LAMF). Fenix carries three LTV values per ISIN: Regulatory LTV (= max LTV), Risk LTV (internal ceiling set by the risk team, ≤ Regulatory LTV), and Min LTV.

Today, updates to both scrips require manually calling APIs in Fenix and Finflux separately. This is done by anyone with API access and without any audit trail, approval gate, or role-based control.

**Who is affected:**

- Risk ops team (makers) who need to update scrips frequently but have no safe, governed tool to do so
- Risk managers (checkers) who have no visibility into what changed, when, and by whom
- End users and LSPs who are indirectly impacted by incorrect LTV values (inflated or deflated offers, wrong shortfall calculations)

**What is broken today:**

- Fenix and Finflux scrips are updated separately and can fall out of sync — they should be updated atomically
- Direct API updates are error-prone. A documented past incident set LTVs to 50 instead of 50% causing 100x limit inflation
- No audit log exists for scrip changes — there is no way to trace who changed what and when
- No role-based control — anyone with API access can make changes with immediate live impact on offer generation and shortfall computation

**Why it matters now — three upcoming catalysts:**

1. **Colending expansion** — More colending relationships mean more contract-level approved scrip variants, increasing change frequency
2. **LTV increase to 70%** — Moving from 45% to 70% introduces higher risk volatility and requires more frequent scrip tuning by the risk team
3. **Loan against Shares launch** — Shares are more volatile than mutual funds and will drive significantly more frequent scrip changes

---

## 1. Problem Scope

### In scope

We are solving for:

- A governed, audited maker-checker flow for all approved scrip updates in Command Centre
- Support for the following scrip operations via this flow:
    - **Approve new ISIN** — add a new ISIN (Mutual fund or Share) to the approved scrip with all required parameters
    - **Stop new lodgements** — set min LTV to zero for an ISIN (blocks new pledges without impacting existing collateral)
    - **Make exposure zero** — set max LTV to zero for an ISIN (sets max drawing power to zero, forcing users to cover shortfall via repayment or additional pledging)
    - **Reduce LTV** — reduce min LTV, Risk LTV, or Regulatory LTV for an existing ISIN (Regulatory LTV can only be reduced, never increased via this flow)
- The flow must be file-based (CSV/XLSX upload from the maker) since scfout ofrip updates typically involve multiple ISINs at once
- Updates must propagate atomically to both Fenix and Finflux in a single approved action
- A full audit trail per request — the maker file must be preserved as evidence; the checker output file must show the complete approved scrip post-change
- Contract selection must be mandatory — all operations are scoped to a specific contract (colending or non-colending)

**Primary users:** Risk ops team (maker), Risk managers (maker, checker)
**Secondary users:** Engineering and compliance teams who consume audit logs

### Out of scope

- **Increasing Regulatory LTV** — Regulatory LTV represents the regulatory ceiling. This flow will not allow it to be increased; only reduced. Rationale: increasing it carries regulatory risk and should go through a separate controls process.
- **Per-loan or per-collateral LTV overrides** — this is handled by the Update Collateral flow (separate PRD). This PRD covers the approved scrip master list only.
- **Finflux-only or Fenix-only partial updates** — both systems must be updated together. Partial updates are not permitted.
- **UI-based row-by-row editing** — the maker flow is file-based. A row-by-row UI editor is out of scope for this release.
- **Automated scrip change triggers** (e.g. auto-reduce LTV on NAV drop) — out of scope; this flow is operator-initiated only.
- ISIN change is not supported in the flow

---

## 2. Success Criteria

### Outcomes

- Zero unaudited approved scrip changes in Fenix or Finflux after go-live — every change has a corresponding maker-checker request on record
- Risk ops can execute all five scrip operations (approve, stop lodgements, zero exposure, reduce LTV, unapprove) entirely within Command Centre, replacing the current manual API workflow
- Fenix and Finflux approved scrips remain in sync — no divergence post any approved change

### Key success metrics

| Metric | Target |
| --- | --- |
| Scrip changes with full audit trail | 100% post go-live |
| Regulatory LTV increase attempts blocked | 0 breaches |
| Fenix–Finflux sync failures post approval | 0 |
| Checker TAT for scrip update tasks | < 4 hours (p90) |
| File validation error rate (maker upload) | < 0% of rows per upload |

### Guardrail metrics

- No degradation in offer generation success rate post launch
- No increase in shortfall computation errors
- Zero direct API calls to Finflux or Fenix approved scrip endpoints outside of this governed flow after launch

---

## 3. Solution Scope

### Solution overview

We will build a file-based maker-checker flow within Command Centre's Collaterals section that governs all approved scrip updates. The maker (risk ops) uploads a CSV/XLSX file containing the scrip changes they want to make; the system validates the file, surfaces row-level errors, and — on confirmation — creates a checker task. The checker (risk manager) downloads a pre-generated output file showing the complete approved scrip as it would look post-change, reviews it, and approves or rejects. On approval, the system updates both Fenix and Finflux atomically.

The flow is intentionally file-based rather than row-by-row UI because scrip updates typically touch many ISINs at once and the risk team already works in spreadsheets. The file also serves as the natural audit artefact.

### Detailed solution scope

**A. Entry point**

- The flow is accessible from the Collaterals section in Command Centre
- It is a global (non-loan-level) action, not tied to any specific customer account
- Contract selection is the first mandatory step — the maker selects which contract (e.g. colending partner or DSP 100%) the scrip update applies to

**B. Maker flow — Enter details (step 1)**

- Maker selects contract (mandatory dropdown)
- **Maker downloads the current approved scrip file  the template contains the required columns**: `isin`, `scheme_code`, `scheme_name`, `asset_type`, `amfi_code`, `amc_name`, `scheme_type`, `revised_min_ltv`, `revised_risk_ltv`, `regulatory_ltv`, `is_approved`, `is_updated, remarks`
- Maker uploads the incremental file (CSV or XLSX). PDF, EML also supported as supporting documents (separate field)
- Maker adds request-level remarks (mandatory)
- Maker attaches optional supporting documents (PDF, CSV, XLSX, EML — mime type extension from current PDF-only)
- On clicking Continue, the system runs file validation:
    - All mandatory columns present
    - ISIN format valid (Regex)
    - No negative LTV values (and they cannot be more than 70)
    - Regulatory LTV not higher than existing approved value (increases blocked)
    - Risk LTV ≤ Regulatory LTV
    - Min LTV ≤ Risk LTV
    - asset_type is one of `MUTUAL_FUNDS` or `SHARES`
    - For new ISINs and updates: all parameters mandatory

**C. Maker flow — Confirm details (step 2)**

- System shows a validation summary: rows submitted, rows verified, rows with errors
- Maker can download the verified file to review row-level validation results
- If any rows have errors, the maker cannot proceed — they must fix and re-upload
- Once all rows are verified, maker can confirm submission
- Confirmation modal: "Are you sure you want to submit this scrip update for approval?"
- On confirm, a checker task is created and a UCRID is generated

**D. Checker flow**

- Checker sees the task in the pending approvals queue in Command Centre
- Task header shows: request ID (UCRID), created on timestamp, substatus (Pending checker approval), maker name, maker remarks
- Checker can download two files:
    - **Maker file** — the original file uploaded by the maker (audit evidence)
    - **Checker output file** — system-generated file showing the complete approved scrip as it will look after the change is applied, with a diff column flagging changed rows
- Checker reviews and approves or rejects
- On approval: system calls Fenix and Finflux APIs atomically to apply all scrip changes in the file
- On rejection: no changes are made; rejection reason is logged to audit trail
- Partial approval (row-level) is not supported in v1 — the checker approves or rejects the entire batch
- If there are any issues in uploading the flow, product and engineering teams will support the risk operations and risk team.

**E. Audit log**

- Every request has a permanent audit entry: maker identity, maker file, timestamp, contract, checker identity, checker decision, checker timestamp, system API response (Fenix + Finflux)
- Audit log is accessible in Command Centre under the Collaterals section - Reports

**F. Validations and constraints**

- Regulatory LTV can only be reduced or zeroed, never increased — enforced at file validation before the checker task is created
- Risk LTV must always be ≤ Regulatory LTV; Min LTV must always be ≤ Risk LTV — enforced at validation
- If the same ISIN appears more than once in the upload file, the system returns a duplicate row error
- Contract is always required — a scrip update without a contract context will be rejected at validation

**G. Impact on existing SOPs**

- The current manual API-based process for updating Finflux and Fenix scrips is fully replaced by this flow
- Risk ops no longer require direct API access credentials for scrip updates — access is governed by the maker role in Command Centre
- The risk manager's approval is the only gate before any scrip change goes live

---

## 4. Open questions for design

1. **Partial row failure on approval** — if the Finflux API call succeeds but the Fenix API call fails mid-execution, what is the rollback strategy? Engineering must define the atomicity guarantee before build.
2. **Checker output file format** — should the diff column show old value → new value inline, or should it be a separate tab? Design team to decide. It should show older and newer values
3. **Contract-level vs global view** — should the checker output file show only the ISINs changed, or the full approved scrip for that contract? Recommendation: full scrip, with changed rows highlighted, so the checker has complete context.

**Maker and checker files:**

[approved_scrip_maker.html](Approved%20Scrips%20productisation/approved_scrip_maker.html)

[approved_scrip_checker (1).html](Approved%20Scrips%20productisation/approved_scrip_checker_(1).html)

---

## 5. High-level process flow

**Maker flow**

1. Risk ops navigates to Collaterals → Update approved scrip in Command Centre
2. Selects contract
3. Downloads sample template, fills in ISIN changes, uploads file
4. Attaches supporting documents and adds remarks
5. Clicks Continue — system validates file rows via API
6. If errors: system shows row-level failures, maker fixes and re-uploads
7. If all rows pass: confirm screen shows verified row count and download link for verified file
8. Maker confirms submission → checker task created → UCRID returned

**Checker flow**

1. Risk manager opens pending task in Command Centre
2. Reviews task metadata (request ID, maker, timestamp, remarks)
3. Downloads maker file (original evidence) and checker output file (full scrip with diff)
4. Reviews changes against risk policy
5. Approves or rejects with remarks
6. On approval: Fenix and Finflux updated atomically; audit log entry closed
7. On rejection: no system change; rejection reason logged

**Edge cases**

- **Finflux/Fenix API failure on approval** — checker is notified of failure; request moves to an error state; engineering is alerted; no partial state is committed
- **Duplicate ISIN in upload** — blocked at step 1 validation with row-level error
- **Regulatory LTV increase attempt** — blocked at step 1 validation; specific error message returned to the maker
- **Checker is same person as maker** — system enforces separation; maker cannot approve their own request

---

## 6. Appendix

### Key terminology

| Term | Definition |
| --- | --- |
| Approved scrip | Master list of ISINs eligible for pledging as collateral |
| Regulatory LTV | Maximum LTV ceiling for an ISIN (can only be reduced, not increased) |
| Risk LTV | Internal risk ceiling set by risk team; ≤ Regulatory LTV |
| Min LTV | Default LTV assigned at lodgement |
| Max drawing power | Computed as sum(units × NAV × Regulatory LTV); used for shortfall calculation |
| Shortfall | Drawing power − POS; triggers user action if negative |
| LAMF | Loan Against Mutual Funds |
| LAS | Loan Against Shares |
| Contract | Colending or non-colending relationship context for the scrip |
| UCRID | Update Collateral Request ID — unique ID for a maker-checker request |

### Fenix LTV hierarchy

`Regulatory LTV  ≥  Risk LTV  ≥  Min LTV
(= max LTV)        (internal)    (default at lodgement)`

### Approved scrip file schema (upload template)

| Column | Required for new ISIN | Required for update | Notes |
| --- | --- | --- | --- |
| isin | ✓ | ✓ | Unique key |
| scheme_code | ✓ | — |  |
| scheme_name | ✓ | — |  |
| asset_type | ✓ | — | MUTUAL_FUNDS or SHARES |
| amfi_code | ✓ (MF only) | — |  |
| amc_name | ✓ | — |  |
| scheme_type | ✓ | — |  |
| revised_min_ltv | ✓ | if changing |  |
| revised_risk_ltv | ✓ | if changing | Must be ≤ regulatory_ltv |
| regulatory_ltv | ✓ | if changing | Can only be reduced |
| is_approved | ✓ | if changing | true / false |
| remarks | — | — | Row-level notes |