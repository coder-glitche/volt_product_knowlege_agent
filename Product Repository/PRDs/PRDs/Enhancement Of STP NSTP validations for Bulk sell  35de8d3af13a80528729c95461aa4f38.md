# Enhancement Of STP NSTP validations for Bulk sell off

: Yogesh D
Created time: May 11, 2026 6:15 PM
Status: In progress
Last edited: May 20, 2026 11:40 AM

# **What problem are we solving?**

[STP validation for Bulk Sell off](STP%20validation%20for%20Bulk%20Sell%20off%20336e8d3af13a802c8283d86e576f3220.md)

[E2E Sell-off Productisation V1 ](../LMS%20PRDs/E2E%20Sell-off%20Productisation%20V1%20352e8d3af13a80f9a75bed081dd798f0.md)

Initial STP/NSTP validation for bulk sell off approvals missed key sell-off logic, causing both false NSTP routing and incorrect STP approvals. 

- **Min redemption round-up missed:** Sell-off units are rounded up to meet minimum redemption requirements, increasing sell-off amount vs obligation — ~800/4,000 cases were wrongly pushed to NSTP.But System had no visibility of this roundup.
- **Incorrect overdue amount used:** Within these ~800 cases, ~480 were wrongly pushed to STP because validation compared against **total overdue** instead of only principal + interest dues for 21st-of-month sell-offs.
- **Principal overdue excluded:** Validation ignored principal overdue and considered only interest + charges, causing ~5–6 cases to be wrongly routed to NSTP.
- With E2E Sell-off Productisation now live, these gaps are identifiable and correctable — fixing them directly increases STP conversion rate by ~20%.
- Improving the STP conversion rate in-turn increases OPS bandwidth.

# How do we measure success?

- **STP conversion rate** — Net improvement in STP conversion rate relative to pre-enhancement baseline (~20% improvement expected).
- **STP false-negative elimination** — 0 records routed to NSTP solely due to minimum redemption round-up overshoot, incorrect overdue base.
- **Zero false STP approvals** — 0 instances where a record is auto-approved that should have gone to NSTP.
- Increase in OPS bandwidth - Minimising OPS load and reducing human prone errors.

# What is the solution?

## Overview

Three enhancements to the existing STP/NSTP validation layer for Bulk Sell Off :

1. **Min Redemption Delta Tolerance** — For CDIDs flagged with `min_redemption_flag`, compute a tolerance delta and absorb the overshoot before routing to NSTP.
2. **Correct Total Overdue for Validation** — Replace the generalised overdue figure with a full overdue (principal + interest + charges) sourced from `get_overdue_detail` API.
3. **Trigger-Aware DPD Amount for Validation** — Read the DPD trigger type stored against the SCRID and use the corresponding amount field from `get_overdue_detail` API as the RHS obligation.

### Enhancement 1 — Min Redemption Delta Tolerance

- In E2E Sell-off Productisation, when the remaining recovery amount R is less than the min_redemption_amount for a fund but the fund's CMV is large enough, the system rounds up the sell amount to min_redemption_amount + 50. This is stored as min_redemption_flag = True against the respective CDID.
- As a result, the LHS of the STP validation formula (∑ CMV_i or ∑ CMV_i × (1 − LTV_i)) is higher than the obligation(RHS), causing all such records to fail STP.

#### Solution

When processing a SCRID for STP/NSTP validation, for each CDID in the sell-off request:

1. Check if `min_redemption_flag = True` for that CDID.
2. If flagged, fetch the `minimum_redemption_amount` for the corresponding ISIN from the script master.
3. Compute a tolerance delta:

```jsx
delta = 1.06 × minimum_redemption_amount
```

1. Apply the adjusted STP check — if after performing the standard validation the difference between LHS and RHS is within `delta`, treat as STP
    
    ```jsx
      If (LHS − RHS) ≤ delta
          → STP   (overshoot is explained by min redemption round-up)
      Else
          → NSTP  (EXCESS_COLLATERAL_SALE — overshoot exceeds tolerance)
    ```
    
    > This adjustment is applied **after** the standard formula runs — it is a tolerance gate, not a replacement for the formula
    > 

#### Data Variables & Source Mapping

| Field | Source | Used In |
| --- | --- | --- |
| min_redemption_flag |  | Determine if delta applies |
| minimum_redemption_amount | Script master  | Delta computation |
| delta | Derived: 1.06 × minimum_redemption_amount | to find tolerance |

---

### Enhancement 2 — Correct Total Overdue for Validation

- The current DPD STP validation formula (Step 3.2) uses `Total Due + Total Overdue` on the RHS. The `Total Overdue` figure sourced from the Summary API historically only captured interest overdue + charge overdue. Principal overdue was absent.
- As identified in the 21 Apr 2026 post-production finding (covered in the existing STP PRD), principal overdue is excluded from current validation for term loans, understating the RHS and incorrectly pushing valid DPD sell-offs to NSTP.
- Since OD loans will also carry principal overdue in future, fixing this now makes the validation loan-type agnostic and future-proof.

#### Solution

Replace the existing `Total Overdue` input to the validation formula with the **full overdue** from the `get_overdue_detail` API, which includes principal + interest + charges overdue.

**Updated Step 2.2 — Shortfall with Dues/Overdues**

> Applies when `SELLOFF_TYPE = SHORTFALL` and `Total Due > 0` AND/OR `Total Overdue > 0`
> 

```jsx
If ∑ (CMV_i × (1 − LTV_i)) ≤ 1.06 × (Regulatory Shortfall Amount + Total Due + Total Overdue)
    → STP
Else
    → NSTP

Where:
  Total Overdue = principal_overdue + interest_overdue + fee_overdue + penalty_overdue
```

**Updated Step 3.2 — DPD Sell-Off Validation**

> Applies when `SELLOFF_TYPE = DPD`
> 

> Step 3.2 is excluded from this enhancement, as trigger-type logic for DPD sell-offs is being handled under the third enhancement, which also covers this logic.
> 

```jsx
If ∑ CMV_i ≤ 1.06 × (Total Due + Total Overdue)
    → STP
Else
    → NSTP

Where:
  Total Overdue = principal_overdue + interest_overdue + fee_overdue + penalty_overdue
```

#### **Data Variables & Source Mapping**

| Field | Source | Used In |
| --- | --- | --- |
| `total_overdue` | `get_overdue_detail` API — `total_overdue` field | RHS of Step 2.2 and Step 3.2 |

#### get_overdue_detail API

#### cURL

curl –location ‘[https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata)’

–header ‘accept: application/json, text/plain, */*’

–header ‘accept-language: en-US,en;q=0.9’

–header ‘authorization: Bearer OFWFEY6QzBPa9XQTYvM-eWGNmGY’

–header ‘sec-ch-ua: “Not.A/Brand”;v=“8”, “Chromium”;v=“114”, “Google Chrome”;v=“114”’

#### Request

GET [https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata)

#### Response

```
 {
        "loan_id": "000154569",
        "principal_due": 0.000000,
        "interest_due": 0.000000,
        "fee_due": 1770.000000,
        "penalty_due": 0.000000,
        "total_overdue": 1770.000000,
        "current_month_charges": 1770.000000,
        "dpd_amount_21_trigger": 0.000000,
        "dpd_amount_75_trigger": 1770.000000,
        "dpd": 0
    }
```

### Enhancement 3 — Trigger-Aware DPD Amount for Validation

- DPD sell-offs are initiated by one of two triggers, each with a different recovery amount:

| Trigger | Recovery Amount Used |
| --- | --- |
| DPD > 75 | dpd_amount_75_trigger = total_overdue (all dues recovered) |
| 21st of month (or next market open day) | dpd_amount_21_trigger = total_overdue − current_month_charges (only principal + interest + prior charges recovered) |
- Current STP/NSTP validation uses Total Due + Total Overdue as the RHS for all DPD sell-offs, irrespective of trigger type.
- For 21st-trigger sell-offs, the actual sell-off amount is dpd_amount_21_trigger (lower than total_overdue as we dont recover current month charges), so using total_overdue overstates the RHS and leads to incorrect comparisons.

#### Solution

- Read the DPD trigger stored against the SCRID in fenix_sell_off_collaterals_request — field: dpd_trigger (values: DPD_75 or DPD_21).
- Call get_overdue_detail API for the LAN.
- Based on the trigger, select the correct obligation amount for the RHS:

```jsx
If dpd_trigger = 'DPD_75':
     
If ∑ CMV_i ≤ 1.06 × dpd_amount_75_trigger   (from get_overdue_detail API)
    → STP
Else
    → NSTP
```

```jsx
If dpd_trigger = 'DPD_21':
If ∑ CMV_i ≤ 1.06 × dpd_amount_21_trigger   (from get_overdue_detail API)
    → STP
Else
    → NSTP
```

> Enhancement 2 and Enhancement 3 apply jointly to DPD sell-offs. Enhancement 3 ensures the correct overdue components are included within `total_overdue`.
> 

#### **Data Variables & Source Mapping**

| Field | Source | Used In |
| --- | --- | --- |
| dpd_trigger | fenix_sell_off_collaterals_request (per SCRID) | Determines which obligation field to use |
| dpd_amount_75_trigger | get_overdue_detail API response | Obligation for DPD > 75 trigger |
| dpd_amount_21_trigger | get_overdue_detail API response | Obligation for 21st-of-month trigger |

#### get_overdue_detail API

#### cURL

curl –location ‘[https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata)’

–header ‘accept: application/json, text/plain, */*’

–header ‘accept-language: en-US,en;q=0.9’

–header ‘authorization: Bearer OFWFEY6QzBPa9XQTYvM-eWGNmGY’

–header ‘sec-ch-ua: “Not.A/Brand”;v=“8”, “Chromium”;v=“114”, “Google Chrome”;v=“114”’

#### Request

GET [https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata)

#### Response

```
 {
        "loan_id": "000154569",
        "principal_due": 0.000000,
        "interest_due": 0.000000,
        "fee_due": 1770.000000,
        "penalty_due": 0.000000,
        "total_overdue": 1770.000000,
        "current_month_charges": 1770.000000,
        "dpd_amount_21_trigger": 0.000000,
        "dpd_amount_75_trigger": 1770.000000,
        "dpd": 0
    }
```

### Updated NSTP Reason Codes

All existing reason codes remain. One reason code description is updated to reflect the delta-tolerance gate for min redemption.

| Reason Code | Reason | checker_task_description |
| --- | --- | --- |
| `EXCESS_COLLATERAL_SALE` | LHS exceeds RHS beyond the min-redemption delta tolerance | approval required for sale of collateral as sell-off amount exceeds the validation rule for loan: {LAN}. |
| `MIN_REDEMPTION_DELTA_BREACH` | LHS − RHS exceeds the computed `total_delta` for flagged CDIDs | approval required for sale of collateral as sell-off amount exceeds the minimum redemption tolerance for loan: {LAN}. |
| `DPD_TRIGGER_NOT_FOUND` | `dpd_trigger` field missing or unrecognised on SCRID | approval required for sale of collateral as STP validation could not be completed due to missing trigger type for loan: {LAN}. |
| `PROCESSING_TYPE_NOT_ELIGIBLE` | Physical sell-offs — unchanged | approval required for sale of collateral as processing is physical for auto-approval for loan {LAN}. |
| `SELLOFF_TYPE_NOT_ELIGIBLE` | Voluntary, Other, unrecognised types — unchanged | approval required for sale of collateral as sell-off type is not eligible for auto-approval for loan {LAN}. |
| `ONGOING_SELLOFF_EXISTS` | Non-terminal sell-off already in progress — unchanged | approval required for sale of collateral as an existing sell-off is currently in progress for loan: {LAN}. |
| `LTV_NOT_FOUND` | LTV mapping missing — unchanged | approval required for sale of collateral as STP validation could not be completed for loan: {LAN}. |
| `NAV_UNAVAILABLE` | Latest NAV not available — unchanged | approval required for sale of collateral as STP validation could not be completed for loan: {LAN}. |
| `API_FAILURE` | Any API returned an error — unchanged | approval required for sale of collateral as STP validation could not be completed for loan: {LAN}. |

## In Scope

- Per-CDID min_redemption_flag check and delta-tolerance  applied after standard STP formula.
- Replacement of partial overdue with full total_overdue (principal + interest + charges) from get_overdue_detail API in all DPD and Shortfall validation formulas.
- Reading dpd_trigger from fenix_sell_off_collaterals_request and selecting dpd_amount_75_trigger or dpd_amount_21_trigger from get_overdue_detail API as the DPD obligation figure.

## Out of Scope

- Changes to the Shortfall STP formula beyond the overdue correction (Enhancement 2).
- Manual (non-E2E) sell-off requests where `dpd_trigger` and `min_redemption_flag` are not set; these continue through the existing validation path unchanged.

# Happy Path

1. System processes a SCRID from `fenix_sell_off_collaterals_request` for STP/NSTP validation.
2. Reads `SELLOFF_TYPE` and `dpd_trigger` (if DPD) from the SCRID record.
3. Calls `get_overdue_detail` API — retrieves `total_overdue`, `dpd_amount_75_trigger`, `dpd_amount_21_trigger`.
4. For each CDID in the SCRID, checks `min_redemption_flag` in . For flagged CDIDs, fetches `minimum_redemption_amount` from script master and computes `delta_i`. Aggregates `total_delta` across all flagged CDIDs.
5. Runs the standard STP formula (Step 2 or Step 3 depending on SELLOFF_TYPE) using:
    - Correct full `total_overdue` (Enhancement 2).
    - Trigger-correct obligation amount for DPD (Enhancement 3).
6. If standard formula passes → **STP**. No further checks needed.
7. If standard formula fails:
    - If `delta > 0` and `(LHS − RHS) ≤ delta` → **STP** (min redemption overshoot absorbed).
    - Else → **NSTP** with appropriate reason code.
8. STP records auto-approved and dispatched. NSTP records routed to checker task with reason code and description.

# Edge Cases

| Case | Handling |
| --- | --- |
| `min_redemption_flag = True` for a CDID but `minimum_redemption_amount` not found in script master | Treat delta for that CDID as 0 — conservative; record still subject to standard formula |
| `dpd_trigger` not set on SCRID (non-E2E initiated sell-off) | Use existing `Total Due + Total Overdue` as obligation — existing behaviour unchanged |
| `dpd_trigger` set to an unrecognised value | → NSTP (`DPD_TRIGGER_NOT_FOUND`) |
| `get_overdue_detail` API failure | → NSTP (`API_FAILURE`) — existing behaviour |
| LAN has both `min_redemption_flag` CDIDs and a genuine excess-collateral-sale overshoot | Delta gate applied; if `(LHS − RHS) > total_delta`, → NSTP (`EXCESS_COLLATERAL_SALE`) |
| OD loan with principal overdue present (future) | Automatically handled — `total_overdue` from `get_overdue_detail` includes principal overdue for all loan types |

# Process Flow

```jsx
┌───────────────────────────────────────────────┐
│  Pick SCRID for STP/NSTP validation           │
│  Read SELLOFF_TYPE, dpd_trigger from SCRID    │
└────────────────────┬──────────────────────────┘
                     │
                     ▼
       ┌──────────────────────────────┐
       │  Call get_overdue_detail API │
       │  → total_overdue             │
       │  → dpd_amount_75_trigger     │
       │  → dpd_amount_21_trigger     │
       └──────────────┬───────────────┘
                      │
                      ▼
     ┌────────────────────────────────────┐
     │  For each CDID against SCRID:      │
     │  Check min_redemption_flag         │
     │  If True → fetch min_red_amount    │
     │         → delta = 1.06 × min_red   │
		 │                                    |
     └──────────────┬─────────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │   SELLOFF_TYPE?      │
         └──────────┬───────────┘
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
   SHORTFALL                   DPD
       │                         │
       ▼                         ▼
  Use total_overdue         Read dpd_trigger
  (full, incl. principal)        │
  in Step 2.2 / 2.3        ┌────┴────┐
       │                  DPD_75   DPD_21
       │                    │        │
       │                    ▼        ▼
       │             dpd_amount_ dpd_amount_
       │             75_trigger  21_trigger
       │                     │        │
       └──────────┬──────────┘        │
                  └──────────┬────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │  Run standard STP formula   │
              │  (Step 2 or Step 3)         │
              └──────────────┬──────────────┘
                             │
                  ┌──────────┴──────────┐
                Pass                  Fail
                  │                     │
                  ▼                     ▼
                 STP         Is delta > 0?
                                        │
                           ┌────────────┴────────────┐
                           Yes                       No
                            │                         │
                            ▼                         ▼
	               (LHS − RHS) ≤ delta?               NSTP
                            │                  (reason code)
               ┌────────────┴──────────┐
              Yes                     No
               │                       │
               ▼                       ▼
              STP                    NSTP
         (min red            (EXCESS_COLLATERAL_SALE
          overshoot           or MIN_REDEMPTION_
          absorbed)           DELTA_BREACH)
```