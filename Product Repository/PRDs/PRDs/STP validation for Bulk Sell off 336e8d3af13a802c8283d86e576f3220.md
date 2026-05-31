# STP validation for Bulk Sell off

: Yogesh D
Created time: April 2, 2026 4:31 PM
Status: Done
Last edited: May 19, 2026 4:09 PM

# What problem are we solving?

- Today, all sell-off requests initiate via the "Bulk Initiate Sell Off"  in the Ops Command Centre and go through the NSTP (Non-Straight-Through Processing) path — every record creates a checker task requiring manual review and approval.
- With average of 193 requests per day (as of Jan-March 2026), manual processing introduces delay in sell-off execution.
- Manual processing increases operational bandwidth consumption of OPS team and introduces human-prone errors.

# How do we measure success?

- **STP conversion rate** — ≥ x% of shortfall and DPD sell-off records auto-approved without checker intervention.
- **Ops bandwidth reduction** — Manual checker man-hours decrease proportionally with the increase in STP conversion rate
- **Zero false STP approvals** — 0 instances where STP-approved sell-off results in over-selling, Multiple sell offs being executed when pre-existing sell off request still in process.
- **Controlled NSTP Routing** — 100% of records failing STP validation routed to NSTP with clear reason codes.

---

# What is the solution?

## Overview

- By introducing STP (Straight-Through Processing) logic, we can auto-approve sell-offs that satisfy well-defined validation rules, while routing genuinely complex or edge-case requests to NSTP for OPS review.
- When the maker uploads an `initiate_sell_off` sheet via the Ops Command Centre, the system will — before creating a checker task — evaluate each request against the STP logic.
- Sell off Requests that pass STP validations are auto-approved and processed. Records that fail the STP validations are routed to the existing NSTP checker flow.

## STP Validations Logic

### Definitions

| Term | Definition |
| --- | --- |
| **CMV_i** | Current Market Value of the collateral (ISIN-level), derived from `units × latest NAV` for each row in the initiate_sell_off sheet. |
| **LTV_i** | Max Loan-to-Value ratio (regulatory/policy LTV mapped to each ISIN). This is the fixed LTV used for shortfall calculation — not the effective/realised LTV. |
| **Shortfall Amount (SA)** | `POS − DP` where `DP = ∑(LTV_i × CMV_i)` across all pledged collateral on the loan. Fetched from the    Summary API. |
| **POS** | Principal Outstanding — the current loan balance. |
| **DP** | Drawing Power — `∑(LTV_i × CMV_i)` across the full pledged portfolio. |
| **Total Due** | Interest due for the current billing cycle (not yet overdue). |
| **Total Overdue** | Sum of all overdue amounts — interest overdue + charge overdue. |
| **Interest Overdue** | Overdue interest component specifically (subset of Total Overdue). |
| **Minimum Redemption Amount** | The minimum amount that can be redeemed from a mutual fund scheme. If SA < minimum redemption amount, after STP validation will auto move into NSTP. |
| **Non-terminal sell-off** | A sell-off that is in progress (not in a terminal state like `COMPLETED`,  `FAILED`). |
| **STP** | Straight-Through Processing — auto-approved, no checker required. |
| **NSTP** | Non-Straight-Through Processing — routed to checker for manual review. |

### Step 1: Identify Sell-Off Type and processing type

Read SELLOFF_TYPE from the initiate_sell_off sheet uploaded by maker  for each LAN.

| **PROCESSING_TYPE** | **Routing** |
| --- | --- |
| DIGITAL | Check SELLOFF_TYPE |
| PHYSICAL | N-STP |

| SELLOFF_TYPE | Routing |
| --- | --- |
| Shortfall | Validate as per Step 2 |
| DPD | Validate as per Step 3 |
| Voluntary | → NSTP |
| Other | → NSTP |
| DECEASED | → NSTP |
| PRINCIPAL | → NSTP |

---

### Step 2: Shortfall Sell-Off

#### 2.1 Ongoing Sell-Off Check

- If a shortfall sell-off is already in progress → NSTP
    - this will be checked by existing sell off request in fenix_sell_off_collaterals_request table against each LAN.
- Else → proceed to Step 2.2 or Step 2.3 depending on Dues and Overdues.

#### 2.2 Loan HAS Dues and/or Overdue

> Applies when Total Due > 0 AND/OR Total Overdue > 0
> 

```jsx
If ∑ (CMV_i × (1 − LTV_i)) ≤ 1.05 × (Regulatory Shortfall Amount + Total Due + Total Overdue)
    → STP
Else
    → NSTP
```

#### 2.3 Loan has NO Dues / Overdues

> Applies when `Total Due = 0` AND `Total Overdue = 0`
> 

```jsx
If ∑ (CMV_i × (1 − LTV_i)) ≤ 1.05 × Shortfall Amount
    → STP
Else
    → NSTP
```

---

### Step 3: DPD Sell-Off

#### 3.1 Ongoing Sell-Off Check

- If ANY sell-off is already in progress → NSTP
- Else → proceed to Step 3.2.

#### 3.2 proceed for sell off

```jsx
If ∑ CMV_i ≤ 1.05 × (Total Due + Total Overdue)
    → STP
Else
    → NSTP
```

### LOGICS EXPLAINED

#### Why `(1 − LTV)` in Shortfall?

In a shortfall sell-off, the sale proceeds repay principal (reduce POS) but also reduce collateral (reduce CMV and therefore DP). The effective shortfall cure per rupee sold is only `(1 − LTV)`. The formula ensures the total  value from the collateral being sold does not exceed what is needed to close the shortfall + dues.

#### Why no `(1 − LTV)` in DPD?

DPD sell-off proceeds go to clear dues — they don't reduce POS. The full CMV is cash collected. There is no haircut because the objective is dues recovery, not shortfall cure. The collateral erosion is a known and accepted side effect, corrected by the next EOD shortfall job.

#### The 1.05 Buffer — Why?

The 5% multiplier on the RHS of every STP condition is a conservative execution cushion accounting for:

- NAV movement between request time and actual redemption (T+1 / T+2 settlement).

## In Scope

- STP validation for Shortfall and DPD sell-off types .
- Auto-approval and dispatch for STP-eligible LANs (no checker task created)
- NSTP routing with reason codes for all non-eligible LANs
- Ongoing sell-off status check before STP approval
- Multi-row LAN aggregation (∑ across ISINs for CMV )and LTV fetch for CMV × (1 − LTV))
    - **Aggregation rule**
        
        > **Important**: A single LAN can have **multiple rows** (multiple ISINs/folios being sold). All rows for a LAN must be aggregated for the summation ∑ CMV_i × (1 − LTV_i) or ∑ CMV_i. Check for Multiple SELL_OFF_TYPE in same sheet for same LAN if so →NSTP.
        > 
        
        ```jsx
        For each unique LAN in sheet:
        1. Group all request_rows by LAN AND ensure no mulitple SELL_OF_TYPE
        
        2. For each row i:
        a. Fetch Latest_NAV for ISIN_i → compute CMV_i = Units_i × NAV_i
        b. Fetch LTV for ISIN_i → compute CMV_i × (1 − LTV_i)
        
        3. Sum across all rows:
        ∑ CMV_i  (for DPD)
        ∑ CMV_i × (1 − LTV_i)  (for Shortfall)
        
        4. Run STP logic at the LAN level
        ```
        
    - **Data Variables & Source Mapping**
        
        
        | Field | Source | Used In |
        | --- | --- | --- |
        | LAN | Initiate Sell-Off Sheet | All steps — primary key to group rows |
        | ISIN | Initiate Sell-Off Sheet | CMV calculation, LTV lookup |
        | UNITS | Initiate Sell-Off Sheet | CMV calculation |
        | SELLOFF_TYPE | Initiate Sell-Off Sheet | Step 1 routing |
        | Ongoing Sell-Off Status | Check for pre existing in `fenix_sell_off_collaterals_request`  table in non terminal state | Steps 2.1, 3.1 |
        | POS |    Summary API  | Shortfall derivation |
        | DP |    Summary API  | Shortfall derivation |
        | Total Due |    Summary API  | Steps 2.2, 3.2 |
        | Total Overdue |    Summary API  | Steps 2.2, 3.2 |
        | Shortfall Amount |     derived (POS − DPmax) | Steps 2.2, 2.3 |
        | LTV | ISIN → LTV mapping API | `(1 − LTV_i)` in shortfall formula |
        | NAV | ISIN → NAV mapping API  | CMV calculation (Units × NAV) |
        
        #### Derived Variables (computed at validation time)
        
        | Variable | Formula | Notes |
        | --- | --- | --- |
        | **CMV_i** | `Units_i × Latest_NAV_i` | Per row in the sheet |
        | **∑ CMV_i** | Sum of CMV across all rows for a LAN | Used in DPD formula |
        
        #### NSTP Reason Codes
        
        When a record is routed to NSTP, the system should log a reason code for the checker's reference.
        
        | Reason Code | Reason | checker_task_description |
        | --- | --- | --- |
        | `PROCESSING_TYPE_NOT_ELIGIBLE` | Physical sell-offs to be taken non-STP | approval required for sale of collateral as processing is physical for auto-approval for loan {LAN}.  |
        | `SELLOFF_TYPE_NOT_ELIGIBLE` | Voluntary, Other, or unrecognised sell-off type prinicipal, deceased | approval required for sale of collateral as sell-off type  is not eligible for auto-approval for loan {LAN}.  |
        | `ONGOING_SELLOFF_EXISTS` | Non-terminal sell-off already in progress | approval required for sale of collateral as an existing sell-off is currently in progress for loan: {LAN}. |
        | `MULTIPLE_SELLOFF_TYPES` | LAN has rows with different SELLOFF_TYPEs in sell_off_sheet. | approval required for sale of collateral as Multiple sell-off types found against loan: {LAN}. |
        | `EXCESS_COLLATERAL_SALE` | `∑ CMV_i × (1 − LTV_i)` or `∑ CMV_i` exceeds 1.05 × obligation | approval required for sale of collateral as sell of amount  exceeds the validation rule for loan: {LAN}. |
        | `LTV_NOT_FOUND` | LTV mapping missing for one or more ISINs | approval required for sale of collateral as STP validation could not be completed for loan: {LAN}. |
        | `NAV_UNAVAILABLE` | Latest NAV not available for one or more ISINs | approval required for sale of collateral as STP validation could not be completed for loan: {LAN}. |
        | `API_FAILURE` | Summary or LTV API returned error | approval required for sale of collateral as STP validation could not be completed for loan: {LAN}. |

## Out of Scope

- Penal charges applicable are not included in formula.
- Automation of Data Generation for Sell off request is out of scope. It is done by analytics and ops (maker).

---

# Happy Path

1. Maker uploads `initiate_sell_off.xlsx` in the Ops Command Centre
2. System reads all rows, groups by LAN
3. For each LAN:
    - Reads `SELLOFF_TYPE` → determines validation path (Step 1)
    - Calls    Summary API → fetches POS, DP, shortfall, dues, overdue, ongoing sell-off status
    - Calls LTV Lookup API for each ISIN → fetches LTV per ISIN
    - Calls NAV API for each ISIN → fetches latest NAV, computes CMV
    - Runs corresponding STP validation formula
4. **STP LANs**: Auto-approved and processed immediately — no checker task created
5. **NSTP LANs**: Grouped into a checker task for manual review (existing flow) with corresponding task description.
6. In fenix_sell_off_collaterals_request table of save the result of validation is_maker_checker_skipped.

---

# Edge Cases

| Case | Handling |
| --- | --- |
| Shortfall sell-off already in progress for LAN | → NSTP (Step 2.1) |
| LTV not found for an ISIN | → NSTP (cannot compute formula) |
|  Summary API failure | → NSTP (entire batch for that LAN) |
| SELLOFF_TYPE  unrecognised | → NSTP |

---

# Process Flow

```jsx
┌─────────────────────────────────────────┐
│   Maker uploads initiate_sell_off.xlsx  │
└──────────────────┬──────────────────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Group rows by LAN  │
        └─────────┬───────────┘
                  │
                  ▼
    ┌──────────────────────────────┐
    │  For each LAN:               │
    │  • Read SELLOFF_TYPE         │
    │  • Fetch    Summary API │
    │  • Fetch LTV per ISIN        │
    │  • Fetch NAV per ISIN        │
    │  • Compute CMV, summations   │
    └──────────────┬───────────────┘
                   │
          ┌────────┴────────┐
          │  SELLOFF_TYPE?  │
          └────────┬────────┘
                   │
     ┌─────────────┼──────────────┬──────────────┐
     ▼             ▼              ▼              ▼
 Shortfall       DPD         Voluntary        Other
     │             │              │              │
     ▼             ▼              │              │
 Step 2        Step 3             └──────┬───────┘
 logic         logic                     │
     │             │                     ▼
     ▼             ▼                   NSTP
  STP / NSTP   STP / NSTP
     │             │
     └──────┬──────┘
            │
     ┌──────┴──────┐
     │             │
     ▼             ▼
   STP           NSTP
     │             │
     ▼             ▼
  Auto-         Create
  approve      checker
  & dispatch    task
```

# Open Items

- [x]  folio RTA needed?
- [x]  API for LTV, NAV per ISIN
- [x]  API for   summary
- [x]  charges specified list
- [x]  NAV according SF job
- [x]  API for existing selloff request

# Post-Production Review

## Findings (13 April 2026 batch)

Analysis of the first production batch revealed the STP conversion rate was significantly below target. Key observations from the 44 sell-off requests processed:

| Metric | Count | % |
| --- | --- | --- |
| Total requests | 44 | 100% |
| STP (auto-approved) | 16 | 36.4% |
| NSTP (routed to checker) | 28 | 63.6% |

**Breakdown of NSTP routing:**

| Reason | Count |
| --- | --- |
| `SELLOFF_TYPE_NOT_ELIGIBLE` (Voluntary) | 10 |
| `PROCESSING_TYPE_NOT_ELIGIBLE` (Physical Shortfall) | 1 |
| `EXCESS_COLLATERAL_SALE` (DPD + Shortfall, buffer breach) | 17 |
- The Voluntary and Physical NSTP routings are by design and cannot be optimised. However, the 17 records routed to NSTP under `EXCESS_COLLATERAL_SALE` were all **marginal failures** — the LHS exceeded `1.05 × RHS` by a very small margin (typically < 1%). These represent the optimisation opportunity.

## Root Cause

The 1.05 (5%) buffer was set as a conservative cushion for NAV settlement movement, The marginal overshoots are caused by:

- Rounding in unit-level NAV × Units computation
- The 5% buffer being tighter than the natural variance
- When the buffer is recomputed at **1.06 (6%)**, all 17 marginally-failing records pass the validation (verified against the 13 April batch — see equation sheet analysis where `LHS ≤ 1.06 × RHS` evaluates to True for 100% of records).

## Change Request — Buffer Update from 1.05 → 1.06

### Updated Formulas

### Step 2.2 — Shortfall with Dues/Overdues

```jsx
If ∑ (CMV_i × (1 − LTV_i)) ≤ 1.06 × (Regulatory Shortfall Amount + Total Due + Total Overdue)
    → STP
Else
    → NSTP
```

### Step 2.3 — Shortfall with No Dues/Overdues

```jsx
If ∑ (CMV_i × (1 − LTV_i)) ≤ 1.06 × Shortfall Amount
    → STP
Else
    → NSTP
```

### Step 3.2 — DPD

```jsx
If ∑ CMV_i ≤ 1.06 × (Total Due + Total Overdue)
    → STP
Else
    → NSTP
```

### Expected Impact (based on 13 April batch)

| Metric | Before (1.05) | After (1.06) |
| --- | --- | --- |
| Total DPD + Shortfall (digital) eligible | 33 | 33 |
| STP auto-approved | 16 | 33 |
| NSTP due to `EXCESS_COLLATERAL_SALE` | 17 | 0 |
| **STP conversion rate (digital eligible)** | **48.5%** | **100%** |
| **Overall STP rate (incl. Voluntary/Physical)** | **36.4%** | **75.0%** |

## Findings (21 April 2026 batch)

Analysis of DPD sell offs revealed Term loans failed the STP validation because we were not taking into consideration Princpal Over due charges into consideration and only validatinf for interest and charges overdue.

Currently only term loans have the principle due and overdue but down the line even OD loans will have principle dues and overdues.

So when consider dues it is better to include principle , interest and charges overdue.

Same has been aligned with tech team and Principle overdue from mandate summary API will be utilized For Validation.

| dsp_loan_account_no | isin | folio_number | nav | shortfall | collection | Units | rta | minimum Redemption | Amount Due | NAV | sell_off_type | LHS(summation of cmv) | RHS tech (overdue) | LHS <= 1.06 *RHS ? | Actual overdue with principle OD included |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FXLAN92732262 | INF247L01CV7 | 91059135365 | 11.34 | 0 | 188905.5 | 16658.333 | kfin | 500 | 188905.4962 | 11.34 | DPD | 188905.4962 | 10520.6 | FALSE | 179910 |
| FXLAN11632453 | INF879O01019 | 18298849 | 84 | 0 | 2688 | 32 | cams | 1000 | 2688 | 83.71 | DPD | 2678.72 | 154.5 | FALSE | 2560 |
| FXLAN83241344 | INF761K01199 | 9139035936 | 61.47 | 0 | 4195.8 | 68.258 | kfin | 1000 | 4195.81926 | 61.47 | DPD | 4195.81926 | 656.79 | FALSE | 3996 |
| FXLAN88918893 | INF174K01DS9 | 11652543 | 138.01 | 0 | 23992.5 | 173.846 | cams | 1000 | 23992.48646 | 138.01 | DPD | 23992.48646 | 883.75 | FALSE | 22850 |
| FXLAN81184721 | INF204K01HY3 | 477281144752 | 168.02 | 0 | 102.9945 | 0.613 | kfin | 100 | 102.99626 | 168.02 | DPD | 102.99626 | 0 | FALSE | 98.09 |