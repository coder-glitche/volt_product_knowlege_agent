# Sell-off Repayment Reconciliation — Maker Automation

: Yogesh D
Created time: May 25, 2026 12:37 PM
Status: Not started
Last edited: May 29, 2026 3:39 PM

# What problem are we solving?

- Today, the maker step for sell-off repayment reconciliation is entirely manual: the ops team downloads the bank statement and RTA/MFC payout reports, manually cross-references UTRs and amounts, and then maps each payout row transaction to a CDID before uploading the `bulk_unlodgement_post_sell_off` file into the Command Centre.
- This process is error-prone, time-consuming, and creates a daily dependency on ops/analytics bandwidth before the repayment posting flow can even begin.

# How do we measure success?

- **Selloff repayment posting automation rate** — 100% of reconcilable repayment rows (UTRs matched + amounts matched + CDID resolved) get posted to loan accounts without manual intervention.
- **Row-level audit coverage** — 100% of rows across all three report types (KFin, CAMS, MFC) and the bank statement are tagged with a `status_notes` value after each run.
- **Zero incorrect CDID assignments** — 0 instances of a CDID mapped to the wrong payout row.
- **Time to maker file** — Maker file available in Command Centre by 11 AM daily.

---

# What is the solution?

## Overview

A job runs immediately after the maker uploads Reconcilation reports. The job ingests the bank statement (settlements from `ybl_bank_statements`) and the payout/reconciliation reports (KFintech, CAMS, MFC, smallcase, cred).

 It performs two sequential steps:

1. **UTR Matching** — matches each report row's UTR against the bank statement UTRs and validates(matches) amounts.
2. **CDID Mapping** — for rows that clear Step 1, resolves the internal Collateral Detail ID (CDID) from the system using key-based matching via the customer loan account (FXLAN) and corresponding collateral records (SCRIDs → CDIDs).

Rows that clear both steps are marked as success and written to  (`bulk_unlodgement_post_sell_off.xlsx`) along with failed rows with  and surfaced in the Command Centre under **Ops → Bulk Repayment Reconciliation**.

### Step 1: UTR Matching and Amount Validation

#### 1.0 Pre-check: Empty UTR or Dedupe UTRs within each report

Check for empty or duplicate UTRs within each report**.** 

```jsx
FOR each report IN [kfintech, cams, mfc]:
			  IF UTR not in a row:
            → tag all such rows as MISSING_UTR_IN_REPORT

        IF UTR appears in more than one row a report:
            → tag all such rows as DUPLICATE_UTR_IN_REPORT

```

Rows with `MISSING_UTR_IN_REPORT` or`DUPLICATE_UTR_IN_REPORT` or are flagged for manual reconciliation and excluded from further steps.

#### Step 1.1 UTR Lookup in Bank Statement

For each report row where UTR is non-empty and not flagged as a duplicate:

```jsx
	FOR each report IN [kfintech, cams, mfc]:
		FOR each report_row:
				IF report_row.UTR found in (bank_statement.BANKREFERENCENUMBER,bank_statement.utr_22) :
					    → UTR matched — proceed to 1.2
					ELSE:
					    → tag as MISSING_UTR_IN_BS — exclude from Step 2
```

#### Step 1.2 Amount Validation

For UTR-matched rows, compare the bank statement `amount` against the Expected Deposit Amount derived from the report.

| Report | Expected Deposit Amount |
| --- | --- |
| KFintech | `Redemptionamt − STT` |
| CAMS | `NET_VALUE` |
| MFC | `NET_VALUE` |

```jsx
IF bank_statement.amount == Expected Deposit Amount:
    → tag report row and corresponding BS row as SUCCESS_UTR_AMOUNT_MATCH
    → carry forward to Step 2
ELSE:
    → tag report row and corresponding BS row as as AMOUNT_MISMATCH_BS_VS_REPORT
    → exclude from Step 2
```

### Step 2: CDID Mapping

Only rows tagged `SUCCESS_UTR_AMOUNT_MATCH` from Step 1 enter this step.

> Before proceeding to next ensure to find the pledging source for each transaction in K-fintech Payout report this is don by fetching collateral detail table and status pending repayment posting.
> 

#### Step 2.1 PAN → Active FXLAN Resolution

```jsx
FROM report_row.PAN (InvPAN for KFin, PAN for CAMS/MFC):
    → Fetch the active FXLAN and add it to report_row
```

#### **Step 2.2 Mapping CDID to Report Transactions**

```jsx
 for each FXLAN in report_row  
    → Fetch all SCRIDs under the FXLAN
			→ For each SCRID, fetch all CDIDs
				→	For each CDID : Apply the matching keys as per pledge source and repo type to identify the correct CDID for this report_row
```

**Matching key matrix:**

| Pledge Source | RTA / Repo Type | Keys from CDID | Keys from Report |
| --- | --- | --- | --- |
| RTA | K-Fintech | Folio + ISIN + Units + Session ID | `FolioNo` + `ISIN` + `Redemptionunits` + `RequestID` |
| RTA | CAMS | Folio + ISIN + Lien Marking Number | `FOLIO` + `ISIN_NO` + `LIEN_REFNO` |
| MFC | K-Fintech  | Folio + ISIN + Units + expected_Amount(calculated by nav * units at CDID level). | `FolioNo` + `ISIN` + `Redemptionunits` + (`Redemptionamt − STT`) |
| MFC | CAMS  | Folio + ISIN + Lien Marking Number | `FOLIO` + `ISIN_NO` + `LIEN_REFNO` |

```jsx
IF matching CDID found:
	→ tag report row with RESOLVED_CDID add that CDID against the row
	→ proceed to 2.3
ELSE:
	→ tag as CDID_NOT_FOUND (status_notes: KEY_MATCH_FAILED)/
```

> It can happen that for Pledge Source : MFC and Repo Type : K-fintech 2 or more CDID with same Folio + ISIN + Units + expected_Amount and the same customer may have had the same folio/ISIN/units sold multiple times, may exist we need to ensure we assign unique CDID in report for the 2 transaction.
> 

### Output

#### A. Annotated Report Files

Each of the three report sheets (KFin, CAMS, MFC) is updated with two additional columns appended at row level:

| Column | Description |
| --- | --- |
| `cdid` | Resolved CDID; blank if not resolved |
| `status_notes` | One of the status codes below |

#### B. Annotated Bank Statement

Each bank statement row is updated with:

| Column | Description |
| --- | --- |
| `matched_report` | Which report the UTR was matched from (`kfintech` / `cams` / `mfc`); blank if unmatched |
| `status_notes` | Corresponding status from Step 1 |

#### C. Maker Input File

`bulk_unlodgement_post_sell_off.xlsx` — contains only rows where status = `SUCCESS`, with the following fields:

| Column | Source |
| --- | --- |
| `collateral_detail_id` | Resolved CDID from Step 2 |
| `utr` | UTR from payout report (matched in BS) |

This file is surfaced in the Command Centre under **Ops → Bulk Repayment Reconciliation** for the ops maker to review and submit into the existing STP/NSTP validation flow.

## In Scope

- Daily automated UTR matching between payout reports (KFin, CAMS, MFC) and bank statement.
- Amount validation (BS settled amount vs. report expected deposit amount) at row level.
- Intra-report UTR deduplification before matching.
- PAN → FXLAN → SCRID → CDID key-based resolution per pledge source and repo type.
- CDID uniqueness enforcement with disambiguation logic for repeated sales.
- Row-level status annotation on all three reports and the bank statement.
- Maker file (`bulk_unlodgement_post_sell_off.xlsx`) generation containing only `SUCCESS` rows.
- Summary alert to `fenix-lsp-alerts` on job completion.
- Surfacing maker file and annotated reports in Command Centre — Ops → Bulk Repayment Reconciliation.

## Out of Scope

- Downstream STP/NSTP validation and posting — covered in the Sell-off Repayment Reconciliation STP PRD.
- Retry logic on failed rows — all failures are tagged and require manual recon.
- Cross-report UTR deduplication (each report is deduped independently).
- Live tracking of posting outcomes.

## Log Schema

Each run's results are persisted at row level for audit.

| Field | Description |
| --- | --- |
| `run_id` | Unique identifier for the job run |
| `run_date` | Date the job executed |
| `report_type` | `kfintech` / `cams` / `mfc` |
| `report_row_key` | Unique row identifier from report (UTR or composite key) |
| `pan` | PAN from report row |
| `utr` | UTR from report row |
| `bs_utr_match` | Whether UTR was found in bank statement (`true` / `false`) |
| `bs_amount` | Settled amount from bank statement |
| `expected_deposit_amount` | Computed expected amount from report |
| `amount_match` | Whether BS amount == expected amount (`true` / `false`) |
| `resolved_cdid` | CDID resolved in Step 2; null if not resolved |
| `fxlan` | FXLAN resolved from PAN; null if not resolved |
| `status_notes` | Final status code for this row |
| `included_in_maker_file` | `true` if row was included in maker output file |

---

## Open Items / Checklist

- [ ]  **KFin RTA vs MFC-KFin disambiguation** — Both pledge sources use the same KFin payout report. The internal system has a pledge source marking on the collateral record. Confirm with Tech whether this field is reliably populated and usable as the dispatch key at Step 2 before building the matching logic for MFC-KFin path.
- [ ]  **22-digit UTR column** — Currently both 16-digit and 22-digit formats land in `BANKREFERENCENUMBER`. Confirm with Tech that this is the final schema for the 22-digit rollout; no separate column required.
- [ ]  **CDID disambiguation logic** — Exact tiebreaker fields for cases where folio/ISIN/units match multiple CDIDs to be confirmed with Tech (e.g. collateral creation date vs. settlement date matching).
- [ ]  **Command Centre UI** — Define the table view for Bulk Repayment Reconciliation under the Ops section: columns, filter/sort options, download buttons for annotated reports and maker file.
- [ ]  **fenix-lsp-alerts message format** — Define exact alert body for job completion summary.

# Process Flow