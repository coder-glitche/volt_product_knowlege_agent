# STP validation for Sell-off Repayment Reconciliation

: Yogesh D
Created time: April 14, 2026 6:32 PM
Status: Not started
Last edited: May 27, 2026 3:11 PM

# What Problem are we solving?

- Today, all sell-off repayment reconciliation(approval) requests initiated via "Bulk Unlodgement Post Sell Off" in the Ops Command Centre go through the NSTP path — every record creates a checker task requiring manual review and approval.
- With an average of 173 requests per day (as of Jan–March 2026), manual processing introduces delay in repayment reconciliation execution.
- Manual processing increases operational bandwidth consumption of OPS team and introduces human-prone errors.
- With the implementation of this feature we will be able to provide task description for checker describing what to check in sell off repayment approval task And reduce operational load by systematically validating and posting repayments.
- Currently the collateral sell off charges are posted before checker approval if the checker rejects the repayment request then an additional step of reversal of charges posted should be performed.

# How do we measure success?

- **STP conversion rate** — ≥ x% of repayment reconciliation records auto-approved without checker intervention.
- **Ops bandwidth reduction** — Manual checker man-hours decrease proportionally with the increase in STP conversion rate.
- **Zero false STP approvals** — 0 instances where a record is auto-approved with an unverified UTR or without a confirmed bank-RTA amount match.
- **Controlled NSTP Routing** — 100% of records failing STP validation routed to NSTP with clear reason codes visible to the checker.

---

# What is the solution?

## Overview

- By introducing STP (Straight-Through Processing) logic, we can auto-approve sell off repayment approval records that satisfy well-defined validation rules, while routing genuinely complex or mismatched records to NSTP for OPS review.
- When the maker uploads a `bulk_unlodgement_post_sell_off` sheet via the Ops Command Centre, the system will before creating a checker task evaluate each record against the STP logic.
- Records that pass all STP validations are auto-processed and posted into the loan account. Records that fail any validation are routed to the existing NSTP checker flow with the corresponding reason and description.
- In the new system sell off charges are posted post the checker approval of repayment approval request.

## STP Validation Logic

### Definitions

| Term | Definition |
| --- | --- |
| **UTR** | Unique Transaction Reference — the bank transaction identifier against a transaction. |
| **Collateral Detail ID CDID** | DSP's internal identifier for the sold collateral record, used to match against RTA sell-off reports. |
| **Bank Statement** | DSP's record of bank transactions. |
| **Settled Amount** | The transaction amount as recorded in the bank statement for a given UTR corresponding to a sell off repayment. |
| **Expected Deposit Amount** | The net receivable amount as per the RTA sell-off(reconciliation) report for the matched collateral record. 

For KFintech: `Redemption Amount − STT`. 
For CAMS: `Net Value`. |
| **Session ID** | KFintech-specific invoke transaction identifier on DSP's collateral record, used for matching with KFintech's sell-off report. |
| **Request ID** | KFintech-specific invoke transaction identifier present in  KFintech's sell-off(pay_out) report |
| **Lien Marking Number** | CAMS-specific lien reference number on DSP's collateral record. |
| **LIEN_REFNO** | CAMS-specific lien reference number present in CAMS sell-off report |

---

### Input file

The Ops team uploads a file containing the following fields:

- Collateral Detail ID
- UTR ****(Unique Transaction Reference)

### Step 1: UTR Validation

- Check whether the UTR provided in the input file has a corresponding entry in the bank statement.
    - If **found** → Proceed to Step 2.
    - If **not found** → Reject the Request and Send the request as Failed in fenix-lsp-alerts with reason UTR entered is wrong.

---

### Step 2: Settled Amount Retrieval

- Retrieve the transaction amount from the bank statement for the matched UTR.
    
    → Proceed to Step 3.
    
- This amount will be used as the posting amount if the record clears all validations

### Step 3: Deriving expected Deposit Amount from RTA reports

Determine the RTA type from the Collateral Detail ID and perform the corresponding match against the relevant sell-off report.

#### KFintech

```jsx
Match :
     Folio + ISIN + Units + Session ID   (from Collateral Detail ID)
With :
     FolioNo + ISIN + Redemptionunits + RequestID   (from KFintech sell-off report)

```

```jsx
Expected Deposit Amount = Redemptionamt − STT  (from KFintech sell-off report)
```

#### CAMS

```jsx
Match :
		Folio + ISIN + Lien Marking Number   (from Collateral Detail ID)
With :
			FOLIO + ISIN_NO + LIEN_REFNO            (from Cams sell-off report)
```

```jsx
Expected Deposit Amount = Net Value      (net value in Cams sell-off Report)
```

#### MFC

```jsx
if repository_type = CAMS
		Match :
				Folio + ISIN + Lien Marking Number   (from Collateral Detail ID)
		With :
				FOLIO + ISIN_NO + LIEN_REFNO         (from mfc sell-off report)

if repository-type = Kfintech:
		Match :
     Folio + ISIN + Units + bank statement Amount   (from Collateral Detail ID)
		With :
     FolioNo + ISIN + Redemptionunits + Redemptionamt - STT  (from KFintech sell-off report)

		
```

```jsx
Expected Deposit Amount = Net Value      (net value in MFC sell-off Report)
```

- If a match is found and Expected Deposit Amount is derivable → proceed to Step 4.
- If **no match found** or Expected Deposit Amount is unavailable → Route to NSTP (`RTA_MATCH_NOT_FOUND`).

### Step 4: Amount Validation

Compare the Settled Amount from the bank statement against the Expected Deposit Amount from the RTA report.

```jsx
If Settled Amount (bank statement) == Expected Deposit Amount (RTA)
    → STP
Else
    → NSTP (AMOUNT_MISMATCH)
```

### Exception Handling — NSTP Amount Mismatch

- If the checker **approves** a record routed via `AMOUNT_MISMATCH`, the transaction is posted using:
    - **Amount**: Settled Amount from the bank statement.
    - **UTR**: UTR from the input file.

## In Scope

- For all UTRs in input file, UTR existence check against the bank statement.
- Settled Amount retrieval from the bank statement for the matched UTR.
- RTA report matching using the appropriate logic per RTA type — Folio + ISIN + Units + Session ID for KFintech, and Folio + ISIN + Lien Marking Number for CAMS.
- Bank-vs-RTA amount comparison, with auto-posting of matched records into the loan account without checker intervention.
- NSTP routing with structured reason codes and checker-visible task descriptions for every record that fails any validation step.
- Checker override for `AMOUNT_MISMATCH` records — post with bank settled amount on approval.
- Log result of validation  as is_maker_checker_skipped.
- batch summary comms to ops team in fenix-lsp-alerts stating number of requests processed as STP and NST

#### **Data Variables & Source Mapping**

| Field | Source | Used In |
| --- | --- | --- |
| Bank Statement | "third-party-data-lake"."ybl_bank_statements” and cod_acct_no = '000481300003223’ for corresponding ‘txn_date’. | used to verify UTR existence and transaction amount in step 2 |
| K-fintech Payout Report | "third-party-data-lake"."kfin_payouts_reconciliation" | used for fetching variables used in step 3 |
| CAMS/MFC Payout Report | "third-party-data-lake"."cams_reconciliation_dsp”
 | used for fetching variables used in step 3 |
| Collateral Detail ID | Input file (maker upload) | RTA matching — primary key per row |
| UTR | Input file (maker upload) | Step 1 — UTR lookup in bank statement |
| RTA Type | Derived from Collateral Detail ID (CDID) | Step 3 — determines matching logic |
| Folio | Collateral Detail record | Step 3 RTA match |
| ISIN | Collateral Detail record | Step 3 RTA match |
| Units | Collateral Detail record | Step 3 KFintech match |
| Session ID | Collateral Detail record | Step 3 KFintech match |
| Lien Marking Number | Collateral Detail record | Step 3 CAMS match |
| Request ID | KFintech sell-off report | Step 3 — matched against Session ID from Collateral Detail record to identify the correct KFintech redemption entry |
| LIEN_REFNO | CAMS sell-off report | Step 3 — matched against Lien Marking Number from Collateral Detail record to identify the correct CAMS redemption entry |
| Settled Amount | Bank statement (UTR lookup) | Step 4 amount comparison |
| Expected Deposit Amount | KFintech / CAMS sell-off report | Step 4 amount comparison |
| Redemption Amount, STT | KFintech sell-off report | Expected Deposit Amount derivation |
| Net Value | CAMS sell-off report | Expected Deposit Amount derivation |

#### NSTP Reason Codes

When a record is routed to NSTP, the system logs a reason code for the checker's reference.

| Reason Code | Reason | checker_task_description |
| --- | --- | --- |
| `RTA_MATCH_NOT_FOUND` | No matching record found in KFintech or CAMS sell-off report | Sell-off Repayment received against sale of security {ISIN}. Approval required for loan account {LAN} as no matching record was found in the RTA sell-off report. |
| `AMOUNT_MISMATCH` | Settled Amount (bank) does not match Expected Deposit Amount (RTA) | Sell-off Repayment received against sale of security {ISIN}. Approval required for loan account {LAN} as the bank settled amount does not match the RTA  deposit amount . If approved, transaction will be posted with the bank settled amount. |
| `API_FAILURE` | Bank statement or RTA report lookup returned an error | Sell-off Repayment received against sale of security {ISIN}. Approval required for loan account {LAN} as STP validation could not be completed for collateral. |

### Out Of Scope

- Automated generation of the input file (RTA data sourcing and bank statement aggregation)

# Happy Path

1. Maker uploads `bulk_unlodgement_post_sell_off.xlsx` in the Ops Command Centre.
2. System reads all rows from the uploaded file.
3. For each record:
    - Validates UTR against the bank statement (Step 1).
    - Retrieves Settled Amount from the bank statement (Step 2).
    - Determines RTA type from Collateral Detail ID and matches against KFintech or CAMS sell-off report (Step 3).
    - Computes Expected Deposit Amount from the matched RTA record.
    - Compares Settled Amount with Expected Deposit Amount (Step 4).
4. **STP records**: Transaction auto-posted into the loan account with Settled Amount and UTR — no checker task created.
5. **NSTP records**: Routed to checker task with the corresponding reason code and description for manual review.
6.  In "fenix_data_lake"."fenix_repayment_posting_and_unlodgment_post_sell_off" table
table of save the result of validation is_maker_checker_skipped.

# Edge Cases

| Case | Handling |
| --- | --- |
| Bank statement record exists but amount is null/unavailable | → Reject the request and send alert request as Failed in fenix-lsp-alerts with reason UTR entered is wrong. |
| No matching record in KFintech or CAMS report for Collateral Detail ID | → NSTP (`RTA_MATCH_NOT_FOUND`) |
| Settled Amount ≠ Expected Deposit Amount | → NSTP (`AMOUNT_MISMATCH`); if checker approves, post with bank settled amount |
| Bank statement or RTA API returns error | → NSTP (`API_FAILURE`) |
| Collateral Detail ID does not resolve to a known RTA type | → NSTP (`API_FAILURE`) |

# Process Flow

```jsx
┌──────────────────────────────────────────────────────┐
│  Maker uploads bulk_unlodgement_post_sell_off.xlsx   │
└─────────────────────────┬────────────────────────────┘
                          │
                          ▼
          ┌───────────────────────────┐
          │  Read all rows from file  │
          └──────────────┬────────────┘
                         │
                         ▼
         ┌───────────────────────────────┐
         │  For each record:             │
         │  • Read Collateral Detail ID  │
         │  • Read UTR                   │
         └──────────────┬────────────────┘
                        │
                        ▼
          ┌─────────────────────────────┐
          │  Step 1: UTR in bank stmt?  │
          └──────────────┬──────────────┘
                         │
              ┌──────────┴──────────┐
             Yes                   No
              │                     │
              ▼                     ▼
  ┌────────────────────┐          NSTP
  │   Step 2: Fetch    │     (UTR_NOT_FOUND)
  │   Settled Amount   | 
	|	  From Bank Stmt   │
  └──────────┬─────────┘
             │
						 ▼ 
  ┌──────────────────────────────────┐
  │  Step 3:Determine RTA type       │
  │  KFintech: Folio+ISIN+Units+     │
  │            Session ID            │
  │  CAMS:     Folio+ISIN+           │
  │            Lien Marking No.      │
  └──────────────┬───────────────────┘
                 │
        ┌────────┴────────┐
      Match           No match
        │                 │
        ▼                 ▼
   Derive Expected      NSTP
   Deposit Amount   (RTA_MATCH
                     _NOT_FOUND)
        │
        ▼
  ┌─────────────────────────────────────┐
  │  Step 4: Settled Amt == RTA Amt?    │
  └──────────────┬──────────────────────┘
                 │
       ┌─────────┴──────────┐
      Yes                  No
       │                    │
       ▼                    ▼
      STP                 NSTP
  Auto-post           (AMOUNT_MISMATCH)
  (bank amt +              │
   UTR)             Checker reviews
                          │
                ┌─────────┴────────┐
             Approve            Reject
                │
                ▼
         Post with bank
         settled amount
         + UTR
```

# Open Items / Checklist

- [x]  Tech — API for UTR lookup and Settled Amount retrieval from bank statement
- [x]  Tech — API / data source for KFintech sell-off report (Redemption Amount, STT, Request ID)
- [x]  Tech — API / data source for CAMS sell-off report (Net Value, LIEN_REFNO)
- [x]  Tech — Collateral Detail ID → RTA type resolution mapping confirmed