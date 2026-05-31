# E2E Sell-off Productisation 34ae8d3af13a80928d80d8cf9376836c

# E2E Sell-off Productisation

: Yogesh D
Created time: April 22, 2026 4:44 PM
Status: Not started
Last edited: April 30, 2026 5:35 PM

# What problem are we solving?

- Today, sell-off execution is a fully manual, analytics-dependent process — ops teams rely on daily risk reports, manually compute DPD and shortfall sell off amounts, select funds, prepare maker file, and initiate sell-offs via the Command Centre.
- With an average of 193 sell-off requests per day (Jan–March 2026) and a peak of upto 4000 DPD requests (as on 21st Apr 2026), this introduces significant delay between trigger and execution.
- Any error in selecting accounts for sell off , sell off amount computation, fund selection, or file preparation by analytics and ops directly translates into over-selling, under-selling, or missed sell-offs.
- There is no system-level intelligence today for identifying eligible accounts, computing amounts, or selecting the right funds — all three steps are done outside the product.

# How do we measure success?

- **End-to-end automation rate** — % of eligible sell-offs initiated without manual file preparation by ops/analytics. (95% of total sell offs are Shortfall and DPD).
- **Time to initiate** — No delay directly initiated from system on scheduled time.
- **Zero over-sell instances** — 0 accounts where sell-off amount exceeds obligation.
- **Zero missed eligible accounts** — 100% of shortfall ageing >= 7 and DPD accounts identified and processed daily.
- **Ongoing sell-off conflicts** — 0 instances of duplicate sell-offs initiated against an account with a non-terminal sell-off already in progress.

# What is the solution?

## Overview

The system will automatically identify eligible accounts, compute the correct sell-off amounts (DPD Amount and Shortfall Amount), select the optimal mutual funds to liquidate, and initiate sell off by creating the sell off approval checker tasks — replacing the current manual analytics + ops workflow end-to-end.

The solution covers three sequential scopes:

1. **Account Identification** — determine which LANs are eligible for sell-off on a given day (Shortfall and DPD triggers).
2. **Amount Calculation** — compute `DPD_amount` and `shortfall_amount` per LAN.
3. **Fund Selection** — select which ISINs/folios to sell and how many units, using a ranked liquidation algorithm.

## Scope 1: Account Identification

### Shortfall-Eligible Accounts

- Eligible condition: `shortfall_ageing >= 7`.
- Store them as `is_shortfall_eligible` list.

### DPD-Eligible Accounts

- Exclude accounts that are already in `is_shortfall_eligible` list— their overdue is already recovered via the shortfall path.
- check for 2 Triggers :
- 1st Trigger : DPD
- Eligible condition: DPD > 75 AND not in `is_shortfall_eligible` list
- add it in `is_dpd_eligible` list.
- 2nd Trigger: Interest_DPD (21st of the month or next market open day)
- Eligible condition : (Interest_overdue + principal_overdue) > 10 AND not in `is_shortfall_eligible` OR already in `is_dpd_eligible` list.

NOTE :

- We exclude accounts that are already in `is_shortfall_eligible` list— because their overdue is already recovered via the shortfall path.
- We exclude accounts eligible for DPD 75 sell off from interest_DPD (21st sell off) (case where customer has DPD 75 on 21st) because thier interest and principal overdue are recovered in DPD 75 sell off

## Scope 2: Amount Calculation

### For Shortfall-Eligible Accounts

Before computing any amounts, check `fenix_sell_off_collaterals_request` for each LAN to find any ongoing sell off.

| Ongoing sell-off type | Action |
| --- | --- |
| None | • DPD amount = total_overdue |
| • Shortfall amount = shortfall amount |  |
| DPD (non-terminal) | • DPD amount = total_overdue - (ongoing dpd request amount) |
| • Shortfall amount = shortfall amount |  |
| Shortfall / Voluntary / Other (non-terminal) | Skip — do not initiate sell off |

### For DPD-Eligible Accounts (not shortfall-eligible)

| Ongoing sell-off (any type) | Action | logic |
| --- | --- | --- |
| Any non-terminal | Skip — do not initiate |  |
| None | Trigger = DPD > 75: |  |
| • DPD amount = “dpd_amount_75_trigger” | “dpd_amount_75_trigger” = total_overdue |  |
| None | Trigger = interest_DPD > 14 : |  |
| • DPD amount = “dpd_amount_21_trigger” | “dpd_amount_21_trigger” = Total Overdue - Current Month Charges |  |

### Buffer Application

Before passing to fund selection, apply the 5% execution buffer to account for NAV movement between request and settlement:

> DPD amount = DPD amount × 1.05 (if CA > 0, else 0)
Shortfall amount = Shortfall amount × 1.05 (if SA > 0, else 0)
> 

### Merge Rule (Only for shortfall sell off)

When both DPD amount > 0 and shortfall amount > 0 for shortfall accounts, we combine the amount and sell as shortfall amount for shortfall sell off.

> shortfall amount = shortfall amount + DPD amount
DPD component = 0
> 

This ensures the entire sell-off — both overdue recovery and DP restoration — is executed through the shortfall pass with the correct `1/(1−LTV)` gross-up, avoiding under-selling.

### Sell_off_type assign

For each LAN, by the time fund selection runs, amounts are always in one of two mutually exclusive states due to the merge rule:

- `shortfall amount > 0`— Assign type SHORTFALL
- `DPD amount > 0` — Assign type DPD

## Scope 3: Fund Selection

### Fund Ranking

Funds are ranked per LAN using::

| Priority | Criterion | Order |
| --- | --- | --- |
| 1 | `is_fof` (Fund of Funds flag) | ASC — non-FoF sold first |
| 2 | LTV of collateral | ASC — lowest LTV sold first |
| 3 | CMV of collateral | DESC — highest CMV sold first among same LTV |

### Shortfall sell off fund selection

Applies to: pure shortfall accounts AND combined DPD+Shortfall accounts (after merge rule).

All computation is in **DP-contribution space** (regularized values).

```jsx
R = amount to recover
```

**Pre-compute per fund:**

```jsx
regularized_value_i = cmv_i × (1 − LTV_i)
```

**For each fund in ranked order:**

```jsx
if R <= 0 → stop, target met

if min_redemption_i > cmv_i → SKIP
   (fund cannot contribute enough to meet its minimum redemption)

if R >= regularized_value_i:
    → FULL SELL
    amount_collected = regularized_value_i
    R = R - amount_collected

    sell_amount_i = amount_collected / (1 − LTV_i)
        sell_units_i  = sell_amount_i / NAV_i   (rounded to 3dp)

if (R < regularized_value_i):
    → PARTIAL SELL
    if R < min_redemption_i:
            if(cmv_i > (min_redemption_i + 50)):
                amount_collected = min_redemption_i + 50 ← round up to min redemption amount
                sell_amount_i = amount_collected
                sell_units_i = sell_amount_i / NAV_i
            else: -> SKIP
    else:
        amount_collected = R
        sell_amount_i = amount_collected / (1 − LTV_i)
            sell_units_i  = sell_amount_i / NAV_i   (rounded to 3dp)
    R = R - amount_collected   ← R becomes 0 or negative,after this then stopped
```

---

> The gross-up converts from DP-contribution space back to CMV space — because each rupee of CMV sold only contributes (1 − LTV) towards closing the DP gap, you must sell 1/(1−LTV) times the DP shortfall to fully restore it.
> 

> A flag (min_Redemption_flag) needs to be stored in **fenix_sell_off_collaterals_request table if** we have rounded up any fund to minimum redeption amount when we create a sell off request for a loan account.
> 

---

### DPD fund selection

Applies to: pure DPD accounts only.

```jsx
R = DPD component (amount to recover)
```

All computation is in **CMV space** (no conversion to account for LTV).

For each fund in ranked order:

```jsx
if R <= 0 → stop, target met

if min_redemption_i > cmv_i → SKIP
   (fund CMV too small to meet its own minimum redemption)

if R >= cmv_i:
    → FULL SELL
    amount_collected = cmv_i
    R = R - amount_collected

if R < cmv_i:
    → PARTIAL SELL
    if R < min_redemption_i:
            if (cmv_i > (min_redemption_i + 50):
            amount_collected = min_redemption_i + 50 ← round up to min
          else: -> SKIP

    else:
        amount_collected = R
    R = R - amount_collected  ← R becomes 0 or negative, after this then stopped
```

**Convert to units — no gross-up needed:**

```jsx
sell_units_i = actual_sell / NAV_i   (rounded to 3dp)
```

> A flag (min_Redemption_flag) needs to be stored in **fenix_sell_off_collaterals_request table if** we have rounded up any fund to minimum redeption amount when we create a sell off request for a loan account.
> 

### Post-fund Selection Outcomes

| Outcome | Condition | Handling |
| --- | --- | --- |
| Target met exactly | R = 0 after pass | Proceed to create sell off request and send the Bulk Sell off Request batch file to Command centre. |
| Target over-recovered | R < 0 (min redemption round-up) | Acceptable — slight over-sell due to minimum redemption constraint. Proceed to create sell off request and send the Bulk Sell off Request batch file to Command centre. |
| Target under-recovered | R > 0, all funds exhausted | initiate sell of request for recoverable amount and send the details to RiskOPS via email. |
| No funds sellable | Every fund skipped via min redemption check | Send the details to RiskOPS via email. |

---

## Data Sources (to be discussed)

| Field | Source |
| --- | --- |
| Shortfall ageing, SA (DP − POS) | “fenix_data_lake”.”fenix_shortfall_aging” |
| DPD API | get_overdue_detail API |
| Total Overdue (principle + interest + charges) | get_overdue_detail API |
| Ongoing sell-off status | “fenix_data_lake”.”fenix_sell_off_collaterals_request” (non-terminal records) |
| Pledged funds (ISIN, units, NAV, CMV, LTV) | get_asset_against_lien API |
| blocked units and NAV for them | check for SCRIDs present against LAN and derive blocked units. |
| Minimum Redemption Amount for a fund | script master |
| Fund category (FoF flag) | script master |
| 21st Date | market_calendar |

### get_overdue_detail API

### cURL

curl –location ‘[https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata)’

–header ‘accept: application/json, text/plain, */*’

–header ‘accept-language: en-US,en;q=0.9’

–header ‘authorization: Bearer OFWFEY6QzBPa9XQTYvM-eWGNmGY’

–header ‘sec-ch-ua: “Not.A/Brand”;v=“8”, “Chromium”;v=“114”, “Google Chrome”;v=“114”’

### Request

GET [https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_overdue_detail/flatdata)

### Response

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

### get_asset_against_lien API

### cURL

curl –location ‘[https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_asset_against_lien/flatdata?R_loanId=(’000151232’%2C’000151011’)](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_asset_against_lien/flatdata?R_loanId=(%27000151232%27%2C%27000151011%27))’

–header ‘accept: application/json, text/plain, */*’

–header ‘accept-language: en-US,en;q=0.9’

–header ‘authorization: Bearer f3QrZoa0-bb8kuu7lD5eP3II5Ns’

–header ‘sec-ch-ua: “Not.A/Brand”;v=“8”, “Chromium”;v=“114”, “Google Chrome”;v=“114”’

–header ‘sec-ch-ua-mobile: ?0’

–header ‘sec-ch-ua-platform: “Windows”’

–header ‘sec-fetch-dest: empty’

–header ‘sec-fetch-mode: cors’

–header ‘sec-fetch-site: same-origin’

–header ‘user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36’

### Request

GET [https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_asset_against_lien/flatdata?R_loanId=(‘000151232’,‘000151011’)](https://voltmoney.finflux.io/fineract-provider/api/v2/runreports/get_asset_against_lien/flatdata?R_loanId=(%27000151232%27,%27000151011%27))

### Response

```
[
    {
        "account_number": "000151011",
        "isin": "INF204K01HY3",
        "scheme_name": "Nippon India Small Cap Fund (G)",
        "amfi_code": 113177,
        "nav": 170.740000,
        "max_ltv": 50.000000,
        "scheme_type": "MUTUAL_FUND",
        "total_units": 13.500000,
        "blocked_units": 0.000000
    },
    {
        "account_number": "000151011",
        "isin": "INF247L01BV9",
        "scheme_name": "Motilal Oswal Small Cap Fund - Regular (G)",
        "amfi_code": 152232,
        "nav": 14.340000,
        "max_ltv": 50.000000,
        "scheme_type": "MUTUAL_FUND",
        "total_units": 1771.210000,
        "blocked_units": 0.000000
    },
    {
        "account_number": "000151011",
        "isin": "INF204K01HY3",
        "scheme_name": "Nippon India Small Cap Fund (G)",
        "amfi_code": 113177,
        "nav": 170.740000,
        "max_ltv": 50.000000,
        "scheme_type": "MUTUAL_FUND",
        "total_units": 131.050000,
        "blocked_units": 0.000000
    },
    {
        "account_number": "000151232",
        "isin": "INF277KA1190",
        "scheme_name": "Tata Business Cycle Fund (G)",
        "amfi_code": 149068,
        "nav": 18.540000,
        "max_ltv": 50.000000,
        "scheme_type": "MUTUAL_FUND",
        "total_units": 15590.970000,
        "blocked_units": 0.000000
    }]
```

## In Scope

- Daily automated identification of shortfall-eligible LANs (`shortfall_ageing >= 7`) and DPD-eligible LANs (DPD > 75 trigger 1st and then 21st-of-month trigger)
- Shortfall amount and DPD amount computation per LAN using get overdue detail API and shortfall ageing data
- Ongoing sell-off detection from `fenix_sell_off_collaterals_request` and appropriate skip/adjustment logic
- 5% execution buffer application on both DPD and shortfall components
- Merge rule — collapsing DPD component into shortfall component when both are present
- Fund ranking per LAN (`is_fof → LTV → CMV`) and unit-level computation for each ISIN/folio
- Shortfall pass (with `1/(1−LTV)` gross-up) and DPD pass (direct CMV) — mutually exclusive per LAN
- Sell-off type assignment (`SHORTFALL` or `DPD`) per LAN before task creation
- Send the Bulk Sell off Request batch file to ops section of command centre and get approval from RiskOPS
- Storing computed maker table (`LAN, ISIN, folio, units, RTA, selloff_type`) for downstream STP-NSTP validation
- Sell-off request creation and checker task dispatch into the existing Ops Command Centre flow
- Persisting results in `fenix_sell_off_collaterals_request` and Mailing Sell_off_request summary report to RiskOPS.

## Out Of Scope

- Current productisation only considers DPD and Shortfall Sell off Types. Voluntary, Deceased and other sell offs are out of scope.

# Happy Path

1. Sell off job runs daily.
2. Identifies `is_shortfall_eligible` LANs (shortfall ageing = 7).
3. Identifies `is_dpd_eligible` LANs (21st of month, DPD > 75 ,not already shortfall-eligible).
4. For each eligible LAN, checks fenix_sell_off_collaterals_request for any non-terminal sell-off.
5. Applies ongoing sell-off rules — skips or adjusts DPD amount accordingly.
6. Applies 5% buffer and merge rule (collapse DPD component into Shortfall component where both present)
7. Fetches pledged fund details, ranks funds per LAN by `is_fof → LTV → CMV`.
8. Runs shortfall pass or DPD pass (mutually exclusive per LAN) to compute `total_units_to_sell` per ISIN/folio.
9. Send the Bulk Sell off Request batch file to ops section of command centre and get approval from RiskOPS
10. store lan, isin, folio, units, rta, selloff_type as maker table for STP - NSTP validation
11. Creates Sell off request and create sell off approval checker tasks.
12. requests are stored and tracked in “fenix_data_lake”.”fenix_sell_off_collaterals_request”

# Log schema

### **fenix_sell_off_collaterals_request**

One new column should be added in **fenix_sell_off_collaterals_request table** Min_Redemption_flag when we have rounded up any fund to minimum redeption amount when we create a sell off request for a loan account.

| **#** | **sell_off_collaterals_request_id** | **completed_on** | **fenix_loan_account_id** | **is_maker_checker_skipped** | **last_updated_on** | **maker_notes** | **processing_type** | **request_source** | **requested_on** | **sell_off_request_type** | **status** | **status_notes** | **workflow_execution_id** | **sub_status** | **total_collateral_value** | **total_charge_amount** | **year** | Min_Redemption_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SCRID3814393249 | 2026-04-29 18:34:30.129000 | FXLAN48697333 | true | 2026-04-29 18:34:30.130000 | DPD Sell off 21 April 2026 | Upload Via Document ID : DOC3239235655 | DIGITAL | COMMAND_CENTER | 2026-04-21 06:44:15.005000 | DPD | SUCCESS | Collateral removed from LMS successfully | 8a814d139d8bc47c019daec84a4e3941 | SUCCESS | 438.8500 | 2.4300 | 2026 |

### Bulk Sell off Request batch file

This excel file is for RiskOPS team to review and approve the created sell off request as batch file in command centre.

| dsp_loan_account_no | isin | folio_number | security_asset_item_ltv | nav | Units | shortfall_amount | dpd_amount | Minimum redemption | rta |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FXLAN13471649 | INF109K01464 | 6282757 | 50 | 912.37 | 0.767 | 0 | 699.8985 | 1 | cams |  |

### Sell_off_requests_summary_report

This report is mailed to the Risk OPS team to convey the summary of successful sell off requests and partial recovered or non recovered.

# Edge Cases

| Case | Handling |
| --- | --- |
| LAN is both shortfall-eligible and DPD-eligible | Shortfall takes priority; DPD list excludes accounts already in `is_shortfall_eligible` |
| LAN has DPD > 75 on the 21st of the month | Included only in DPD 75 path; excluded from the 21st trigger to avoid double sell-off |
| Ongoing DPD sell-off exists when processing a shortfall-eligible LAN | DPD component = `total_overdue − (blocked_units × NAV)` from ongoing sell-off; shortfall component unchanged |
| Ongoing shortfall / voluntary / other sell-off exists for shortfall-eligible LAN | Skip — do not initiate |
| Any ongoing sell-off exists for a DPD-eligible LAN | Skip — do not initiate |
| DPD component or shortfall component computes to a negative value after adjustment | Set to zero before buffer application |
| All funds exhausted before shortfall/DPD target is met | Create sell-off with available units; flag residual gap in task description for checker review |
| 21st falls on a market holiday | Job runs on the next market open day (per `market_calendar`) |

# Process Flow

![shortfall E2E@2x (5).png](E2E%20Sell-off%20Productisation%2034ae8d3af13a80928d80d8/d7cfaea2-d3ed-419c-8dfd-e292e5a60b37.png)

shortfall E2E@2x (5).png

![shortfall E2E@2x (7).png](E2E%20Sell-off%20Productisation%2034ae8d3af13a80928d80d8/42183735-6406-43be-b5c0-8011164ea897.png)

shortfall E2E@2x (7).png

---

# Open items

- [x]  If not able to allocate enough funds to sell ? Do we sell for partial or reject completely
- [x]  How do we communicate it to OPS / Risk (Command centre) — email to riskops
- [x]  If we Round off because of minimum redemption logic how do we produce visibility for NSTP cheker task
- [x]  STP-NSTP flow changes? like will the same flow exist or what are the changes?
- [x]  Risk Dashboard content
- [x]  front-end requirements

# Frontend Requirements

In the Command centre:

- [ ]  Under OPS section add Actions Button
- [ ]  Move “the mandate presentation file generation task” to the drop down menu of Actions Button
- [ ]  Make “Bulk Collateral Sell off Approval” as one of the tasks in drop down menu
- [ ]  A task would be created by the system (maker) these tasks should be displayed once user clicks on “Bulk Collateral Sell off Approval” option
- [ ]  the UI will have table with following fields as tables
- Task Type : Bulk Collateral Sell off Approval
- Product type: Loan agaisnt security
- Created on : Date and time of creation
- Last updated On : Date and time of last status update
- Action filed with review button

![image.png](E2E%20Sell-off%20Productisation%2034ae8d3af13a80928d80d8/1fe0f941-e2f6-492d-872d-85ce2b55bc96.png)

image.png

- [ ]  Upon clicking the Review button a checker menu will be shown
- [ ]  Before checker approval

![Screenshot 2026-04-30 at 4.32.33 PM.png](E2E%20Sell-off%20Productisation%2034ae8d3af13a80928d80d8/f7c9998c-7d76-44ba-af93-8c1592d26461.png)

Screenshot 2026-04-30 at 4.32.33 PM.png

- [ ]  After checker approval

![Screenshot 2026-04-30 at 4.37.45 PM.png](E2E%20Sell-off%20Productisation%2034ae8d3af13a80928d80d8/cf8a0ac3-613a-4354-89a5-12b5d63c3954.png)

Screenshot 2026-04-30 at 4.37.45 PM.png