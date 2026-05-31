# Shortfall Enhancement

Last Edited: May 6, 2026 2:55 PM
PRD ETA: April 23, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## Background and Context

Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP.

Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture.

**Who is affected:**

- Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned
- Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open
- Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day
- LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types

**What is broken today — six specific gaps:**

1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them.
2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis.
3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today.
4. **No reliable NAV gate.** The shortfall job and the NAV update job are time-dependent but not atomically linked. In past instances, the NAV job extended past its window or failed to trigger, and the shortfall job ran on stale NAV data — producing incorrect DP calculations and wrong shortfall amounts.
5. **Manual communications create a hard dependency on operations.** Shortfall notices go into an ops approval queue before being sent to borrowers. This means the 9 AM target (before markets open) is frequently missed. With LAS launching, same-day communications for intra-day 85% breaches will be impossible if the manual gate remains.
6. **No accelerated sell-off mechanism for severe deterioration.** Today, regardless of how bad the collateral coverage gets, the system waits for ageing day 7 before initiating sell-off. With LTVs increasing to 70% for equity MFs and the addition of shares (which are more volatile), a 45% LTV regime's safety buffer no longer exists. A 70% LTV with a 10% market fall can take DP/Exposure below 85% in a single day — requiring same-day action.

**Why it matters now — three catalysts that make this urgent:**

- LTV increase to 70% for equity MFs — higher LTV means smaller buffer, faster deterioration, more frequent shortfalls
- LAS launch — shares are intra-day volatile; NAVs move continuously; an end-of-day shortfall job is structurally insufficient
- Colending expansion — more partner relationships mean more borrower accounts and higher ops exposure to manual bottlenecks

---

## 1. Problem Scope

### In scope

We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall job — market day and non-market day**
Run the shortfall job every business day. On post-holiday BODs, run a recovery-only pass — refresh Exposure and DP, apply any recoveries from the holiday period, but do not increment ageing. Ageing increments only on market days.

**C. NAV pre-check gate**
Gate the shortfall job on confirmed NAV receipt. Two-layer validation: (1) Finflux job status API confirms NAV fetch and DP update jobs completed; (2) `fenix_script_master_nav` (CMOTS table) `created_on` date equals today, confirming the CMOTS fetch succeeded. If validation fails, the job holds; it does not proceed on stale data. On timeout, email alerts are sent to [risk@dspfin.com](mailto:risk@dspfin.com) and [operations@dspfin.com](mailto:operations@dspfin.com), and an alarm is raised for the LMS on-call team.

**D. Automated shortfall communications**
Auto-trigger shortfall communications on BOD job completion, without manual approval. Launch in ops-gated mode for a 2-week validation window; promote to STP after 14 consecutive clean cycles (no corrections by ops team). All comms include due date and the 85% accelerated sell-off disclaimer.

**E. Exposure breach shortfall type + accelerated sell-off**
Introduce two new shortfall types: `EXPOSURE_BREACH_SHORTFALL` (identified at BOD for LAMF) triggered when DP/Exposure ratio falls below a configurable threshold (default 85%), and `INTRADAY_EXPOSURE_BREACH_SHORTFALL` (identified intra-day for LAS via the sell-off request API). Both are distinct entities in the shortfall system. The breach threshold is configurable at product level by the risk team without a deployment. Due date = same day 12 noon. Product-level configuration controls which shortfall types are applicable.

**F. Noon sell-off identification process**
A structured, auditable noon process that produces a categorised list of all accounts requiring immediate sell-off, segmented by whether a sell-off is already underway. Persisted with a unique run ID for audit and regulatory purposes.

**G. API enhancements**
Shortfall API response to include due date per shortfall instance and the new Exposure Breach shortfall type. Webhooks to LSPs to be extended accordingly.

**Primary users:** Engineering (build), Risk team (consume shortfall data and sell-off list), Operations team (post-facto comms review)
**Secondary users:** Borrowers (receive timely and accurate shortfall communications), LSPs (consume API and design borrower experience)

### Out of scope

**Intra-day DP recalculation for LAMF** — MF NAVs update once daily. Even if a borrower pledges additional securities during the day, the DP benefit of that pledge is not reflected until the next BOD. This is a known limitation of the LAMF product architecture and is acknowledged as such in this PRD. It is not addressed here.

**Monitoring dashboards and alerting infrastructure** — The PRD specifies the NAV validation requirement and the job completion gate. Alerting (8:30 AM warning, 9 AM P1), escalation matrices, and operational dashboards are engineering's remit and will be implemented via the standard alarms infrastructure. This PRD does not prescribe escalation tooling.

**Automated sell-off execution** — The noon process identifies and categorises accounts requiring sell-off. Execution of the sell-off remains with the operations and risk team. Automated sell-off execution is out of scope.

**Debt fund market calendar differences** — The PRD assumes a single market calendar applicable to both equity MFs and shares. Debt fund holidays may differ; handling this divergence is deferred.

**Automated portfolio shortfall** — Portfolio shortfall (computed using customer LTV, used as a preventive trigger) is in scope as a prerequisite check but its calculation logic is not being changed. It remains the entry condition for risk and exposure breach shortfall computation.

---

## 2. Success Criteria

### Outcomes

- Every borrower who makes a repayment or pledges collateral on a shortfall day receives the corresponding ageing benefit, independent of same-day market movements
- Shortfall communications reach borrowers before market open (9 AM) every business day, without manual intervention
- Zero shortfall jobs run on stale NAV data after go-live

### Key success metrics

| Metric | Target |
| --- | --- |
| Shortfall job completion by 9 AM | 100% of business days |
| Shortfall comms dispatched before 9 AM | 100% of business days post-STP |
| Shortfall jobs run on stale NAV data | 0 post go-live |
| Accounts with correct ageing benefit (repayment on shortfall day) | 100% — verifiable in audit trail |
| Exposure breach shortfall correctly identified and communicated same day | 100% of breaching accounts |
| Ops corrections during 2-week STP validation window | Target: 0 corrections across 14 cycles |

### Post-launch good state

- BOD job runs every business day including post-holidays, completes by 9 AM, and the audit trail shows decomposed ΔDP/ΔExposure for every account processed
- Comms are STP within 3 weeks of launch (14 clean cycles achieved)
- The noon sell-off list is generated, categorised, and accessible to authorised team members every business day
- The shortfall API response includes due date and exposure breach shortfall type for all active shortfall accounts

### Guardrail metrics

- No increase in incorrect shortfall amounts post-launch (validate against a parallel-run period)
- No degradation in offer generation — shortfall logic changes must not affect the approved scrip or offer computation path
- No increase in customer escalations related to incorrect shortfall communications

---

## 3. Solution Scope

### Solution overview

We are rebuilding the shortfall engine's incremental logic from a single-net-figure model to a decomposed ΔDP/ΔExposure model, running the job daily (not just on market days), gating it on confirmed NAV receipt, automating borrower communications, and introducing a new Exposure Breach shortfall type that triggers same-day sell-off at 85% DP/Exposure deterioration. A noon identification process provides a structured, auditable sell-off list.

The solution is phased: communications launch ops-gated, with STP promotion after 14 clean cycles. The intra-day LAS breach path (Exposure Breach via sell-off request API) is in scope but may ship as a fast-follow if LAS launch timing requires it — this should be confirmed with engineering.

The monitoring and alerting infrastructure (job failure escalation, dashboards) is excluded from this PRD and handled separately by engineering via standard alarms — this keeps the PRD focused on product and logic changes rather than infrastructure tooling.

### Detailed solution scope

**A. Decomposed incremental shortfall — new calculation logic**

- Exposure is redefined as POS + Interest Overdue across the entire shortfall system. All references to POS-only Exposure must be updated
- Incremental shortfall is computed as two independent components:
    - ΔExposure = Exposure(today) − Exposure(yesterday). If negative (repayment or interest reduction), apply FIFO knock-off against open shortfall instances before processing ΔDP
    - ΔDP = DP(today) − DP(yesterday). If positive, apply FIFO knock-off against open shortfall instances independently, regardless of whether ΔExposure recovery was also applied in the same cycle. If negative, compute new shortfall amount and create new instance with ageing = 1 (on market days only)
- Ageing increments by 1 for all residual open instances on market days only. On post-holiday days, ageing does not change
- All six ΔDP/ΔExposure scenarios are handled (see Section 5 — process flow)
- **Known limitation to call out to stakeholders:** if a borrower pledges additional securities on a day where the market falls further, the DP benefit of the new pledge is offset by the market fall in the same ΔDP calculation. The gross pledge benefit is not independently isolated. This is a known architectural constraint of the daily NAV model and is not addressed in this release

**B. Daily shortfall job — market day vs non-market day handling**

- Job runs every business day. At runtime, it checks whether the previous day was a market day using a configurable market calendar
- **Market day path (full run):**
    - NAV pre-check (see C below) runs first
    - DP refreshed using updated NAV, Exposure refreshed (POS + Interest Overdue)
    - Decomposed ΔDP/ΔExposure logic applied
    - Ageing incremented for all residual open instances
    - Portfolio shortfall filter applied: only accounts with non-zero portfolio shortfall proceed to risk and exposure breach calculation
    - If an account previously in shortfall no longer shows portfolio shortfall, all open shortfall instances for that account are automatically recovered
- **Non-market day path (recovery-only):**
    - NAV pre-check is skipped (no new NAV available)
    - Exposure refreshed to capture repayments or interest changes that occurred on the holiday
    - ΔExposure computed: if negative, FIFO knock-off applied to open instances
    - ΔDP is checked: if positive (e.g. borrower pledged on the holiday), pass on the recovery benefit. No action taken if ΔDP is same or negative
    - Ageing is NOT incremented
    - No new shortfall instances created
    - This is a recovery-only pass — the job can reduce or close existing shortfall instances but cannot worsen shortfall or age accounts

**C. NAV pre-check gate**

- Two-layer validation before shortfall job proceeds on market day BODs:
    - Layer 1: Call Finflux job status API — confirm both NAV fetch job and DP update job completed successfully
    - Layer 2: Query `fenix_script_master_nav` (CMOTS table) — confirm `created_on` date = today for the ISINs against which active loans have pledged collateral
- If either layer fails at job start, the job holds and waits. The timeout duration is an engineering decision; the BRD suggests 30 minutes as a starting point
- If validation fails post-timeout, an email alert is sent to [risk@dspfin.com](mailto:risk@dspfin.com) and [operations@dspfin.com](mailto:operations@dspfin.com), and an alarm is raised for the LMS on-call team to investigate. The shortfall job does not proceed on stale data

**D. Automated shortfall communications**

- Communications are triggered automatically on BOD job completion — no manual initiation
- **Launch phase (ops-gated, weeks 1–2):** comms go to an ops review queue before dispatch. Ops team has a defined window to flag incorrect communications before they are sent
- **STP promotion criteria:** after 14 consecutive clean cycles (no corrections flagged by ops team across 14 business days), the system is promoted to full STP mode — comms are dispatched automatically without any queue
- The 14-cycle window and promotion are configurable. Ops team or Risk Manager sign-off required to formally promote to STP
- Every shortfall communication must include: FXLAN, current shortfall amount, current DP, current Exposure (POS + Interest Overdue), ageing in market days, due date for resolution, repayment/pledge instructions, and the 85% accelerated sell-off disclaimer
- Communication templates are configurable by the operations team without a system deployment
- Communication log: records recipient, channel, timestamp, content, and delivery status (sent/delivered/failed) for every message
- Failed communications trigger an automated alert to the ops team for follow-up

**E. Exposure breach shortfall — new shortfall type**

- A new shortfall type: **EXPOSURE_BREACH_SHORTFALL**, created when DP/Exposure ratio falls below the configured breach threshold (default: 85%). The threshold is a system-level configuration, updatable by the risk team without a deployment, and is configurable at product level
- This is a distinct entity in `shortfallAnalysis` — not a flag on the account
- Three shortfall types now exist: `PORTFOLIO_SHORTFALL`, `RISK_SHORTFALL`, `EXPOSURE_BREACH_SHORTFALL`
- **Product-level configuration:** which shortfall types are applicable is configurable per product (LAMF, LAS). At launch, all three types apply to both products
- **Ageing logic for exposure breach:** single instance maintained per account. Ageing is incremented each market day. Amount is updated in place (not a new instance on each breach day). Due date = same day 12 noon (ageing day = 1 maps to same-day action)
- **Due date logic by shortfall type:**
    - Exposure breach shortfall: due date = 12 noon, current day
    - Risk shortfall: due date = EOD of the day on which ageing reaches the configured threshold (default: 7 market days). If today is ageing day 9, the due date is calculated as the working day on which ageing day 7 would have fallen — not today. This corrects the current bug where due dates keep shifting
    - Portfolio shortfall: same due date logic as risk shortfall (7 working days, non-shifting)
- **LAMF path:** Exposure Breach Shortfall is identified as part of the BOD shortfall job. If DP/Exposure < 85%, instance is created/updated; account is flagged for noon sell-off list
- **LAS intra-day path:** For shares, DP moves continuously during market hours. When a sell-off request is submitted with `type: INTRADAY_EXPOSURE_BREACH`, the system:
    - Checks if an `INTRADAY_EXPOSURE_BREACH_SHORTFALL` instance already exists for that account today
    - If yes: proceeds to sell-off (NSTP)
    - If no: instantaneously computes DP/Exposure at that moment, creates the `INTRADAY_EXPOSURE_BREACH_SHORTFALL` instance, then proceeds to sell-off (NSTP)
    - This ensures every LAS intra-day exposure breach sell-off has a corresponding auditable shortfall record, distinct from the BOD-identified `EXPOSURE_BREACH_SHORTFALL`
- The DP/Exposure ratio and any breach flag are stored in the audit trail per account per BOD

**F. Noon sell-off identification process**

- Runs at 12 noon every business day
- Identifies all accounts where: shortfall ageing ≥ configured threshold (default: 7 market days), OR DP/Exposure ratio < 85%
- Segmented into two groups:
    - **Group 1 — No ongoing sell-off:** accounts meeting eligibility where no sell-off is currently underway. Require immediate initiation
    - **Group 2 — Ongoing sell-off:** accounts meeting eligibility where a sell-off is already in progress. Require NSTP review
- Data captured per account: shortfall date, FXLAN, DP, Exposure (refreshed at noon to capture intra-day repayments), shortfall amount, shortfall ageing, DP/Exposure ratio, ongoing sell-off status and type, Exposure capture timestamp, DP capture timestamp, sell-off trigger reason (ageing threshold vs exposure breach), list generation timestamp, communication status
- Each run assigned a unique run ID; full list persisted in database for audit and regulatory purposes
- Accessible to authorised operations and risk team members; downloadable as CSV or Excel
- Role-restricted access — view and download requires explicit authorisation

**G. Shortfall API response enhancements**

- The `get shortfall details` API response is enhanced to include:
    - `RISK_SHORTFALL` and `EXPOSURE_BREACH_SHORTFALL` and `INTRADAY_EXPOSURE_BREACH_SHORTFALL` as shortfall types alongside existing types
    - `dueDate` field per shortfall instance — LSPs can use this directly to design the borrower experience without computing it themselves
    - `dpExposureRatio` at the account level
    - `isInExposureBreachShortfall` boolean flag at the account level
- Corresponding webhooks to LSPs extended to include the new fields
- Sample enhanced response structure:

json

`{
  "fenixLoanAccountId": "FXLAN65378191",
  "dpExposureRatio": 0.83,
  "isInPortfolioShortfall": true,
  "isInRiskShortfall": true,
  "isInExposureBreachShortfall": true,
  "shortfalls": [
    {
      "shortfallType": "PORTFOLIO_SHORTFALL",
      "shortfallAmount": -276707.41,
      "ageing": 3,
      "calculatedOn": "2025-01-07",
      "dueDate": "2025-01-14"
    },
    {
      "shortfallType": "RISK_SHORTFALL",
      "shortfallAmount": -276341.57,
      "ageing": 3,
      "calculatedOn": "2025-01-07",
      "dueDate": "2025-01-14"
    },
    {
      "shortfallType": "EXPOSURE_BREACH_SHORTFALL",
      "shortfallAmount": -89200.00,
      "ageing": 1,
      "calculatedOn": "2025-01-07",
      "dueDate": "2025-01-07T12:00:00"
    }
  ]
}`

**Impact on existing SOPs**

- Ops team's morning shortfall communication approval task is reduced to a post-facto review workflow during the 2-week validation window, and eliminated entirely after STP promotion
- Ops team retains the ability to flag incorrect communications in the review log; flagging triggers a re-investigation workflow
- Risk team gains a structured noon sell-off list reducing reliance on manual shortfall monitoring reports
- Intra-day sell-off initiation for LAS continues to be a manual process — this is not changing
- No change to the borrower-facing experience beyond receiving communications earlier and with more complete information (due date, exposure breach notice)

---

## 5. High-level process flow

### BOD shortfall job — market day

`1. Check market calendar → T-1 was a market day
2. Layer 1: Call Finflux job status API — NAV fetch + DP update complete?
   → If no: hold, wait. On timeout: send email alert to risk@dspfin.com and operations@dspfin.com, raise LMS on-call alarm. Job does not proceed
3. Layer 2: Query fenix_script_master_nav — created_on = today for all active ISINs?
   → If no: hold, wait. On timeout: send email alert, raise LMS on-call alarm. Job does not proceed
4. For each loan account in portfolio shortfall:
   a. Refresh Exposure = POS + Interest Overdue
   b. Compute ΔExposure = Exposure(today) − Exposure(yesterday)
   c. If ΔExposure < 0: apply FIFO knock-off against open shortfall instances
   d. Compute ΔDP = DP(today) − DP(yesterday)
   e. Apply scenario logic (see Section 5.3 below)
   f. If DP/Exposure < configured breach threshold: create/update EXPOSURE_BREACH_SHORTFALL instance
   g. Increment ageing by 1 for all residual open instances
5. If account no longer in portfolio shortfall: auto-recover all open instances
6. Trigger shortfall communications (ops-gated or STP)
7. Log audit trail: ΔDP, ΔExposure, instances created/closed, NAV timestamps`

### BOD shortfall job — non-market day (recovery-only)

`1. Check market calendar → T-1 was a market holiday
2. Skip NAV pre-check
3. For each loan account with open shortfall instances:
   a. Refresh Exposure = POS + Interest Overdue
   b. Compute ΔExposure. If negative: apply FIFO knock-off
   c. Compute ΔDP. If positive: apply FIFO knock-off on residual instances
   d. If ΔDP negative or same: no action
4. Do NOT increment ageing
5. Do NOT create new shortfall instances
6. Log audit trail: recoveries applied, accounts cleared`

### ΔDP / ΔExposure scenario matrix

| Scenario | ΔDP | ΔExposure | Action |
| --- | --- | --- | --- |
| 1 | Positive | Non-negative | Apply ΔDP FIFO knock-off against open instances. Compute residual shortfall and run standard logic |
| 2 | Positive | Negative | Apply ΔExposure FIFO knock-off first. Then apply ΔDP knock-off against residual. No new instance unless residual shortfall remains |
| 3 | Same | Non-negative | Compute Δshortfall, run standard logic |
| 4 | Same | Negative | Apply ΔExposure knock-off. No new shortfall |
| 5 | Negative | Non-negative | Compute Δshortfall. Create new instance (ageing = 1). Age all existing instances +1 |
| 6a | Negative | Negative (recovery > worsening) | Apply ΔExposure knock-off. Compute remaining shortfall. Create new instance for residual. Do not double-recover |
| 6b | Negative | Negative (worsening > recovery) | Apply ΔExposure knock-off. Compute shortfall. If CSA > LSA: new instance + age all. If CSA < LSA: knock off difference, age remainder |

### Noon sell-off identification process

`1. At 12 noon: run sell-off eligibility scan
2. For each active loan account:
   a. Refresh Exposure at noon (captures intra-day repayments)
   b. Check: shortfall ageing ≥ 7 market days OR DP/Exposure < configured breach threshold
   c. If eligible: check ongoing sell-off status
3. Assign to Group 1 (no ongoing sell-off) or Group 2 (sell-off in progress)
4. Persist full list with unique run ID
5. Make accessible to authorised users in LMS dashboard`

### LAS intra-day exposure breach path

`1. Sell-off request received with type: INTRADAY_EXPOSURE_BREACH
2. Check: does INTRADAY_EXPOSURE_BREACH_SHORTFALL instance exist for today?
   → If yes: proceed to sell-off (NSTP)
   → If no: compute DP/Exposure instantaneously
             Create INTRADAY_EXPOSURE_BREACH_SHORTFALL instance
             Proceed to sell-off (NSTP)
3. Audit trail: shortfall record created before sell-off initiated`

### Communications flow — phased

`Launch (Weeks 1–2, ops-gated):xx
BOD job completes → comms generated → enter ops review queue
→ Ops reviews within defined window
→ If no correction flagged: comms dispatched automatically
→ If correction flagged: hold, investigate, resend

After 14 clean cycles (STP):
BOD job completes → comms dispatched automatically
→ Ops perform post-facto review via communications log
→ Flag incorrect comms for investigation workflow`

### Edge cases

- **Account exits portfolio shortfall:** all open risk and exposure breach instances auto-recovered. No manual action required
- **ΔExposure knock-off fully clears all instances + ΔDP creates new shortfall:** ageing restarts at 1 with no pre-existing instances. Clean slate
- **Exposure breach + ageing trigger simultaneously at noon:** account appears in Group 1 or 2 with both trigger reasons recorded. Sell-off proceeds under the more urgent trigger (breach threshold = same-day)
- **Finflux NAV job completes but CMOTS table not updated:** Layer 1 passes, Layer 2 fails. Job holds. On timeout, email alert sent to [risk@dspfin.com](mailto:risk@dspfin.com) and [operations@dspfin.com](mailto:operations@dspfin.com), LMS on-call alarm raised. Engineering to investigate CMOTS sync failure. Job does not proceed
- **STP promotion and then a correction:** ops team can raise a correction post-STP. Any correction triggers a 14-cycle reset — the system returns to ops-gated mode until 14 new clean cycles are accumulated

---

## 6. Appendix

### Repayment behaviour data — justification for ageing reform

This data shows the proportion of accounts in shortfall at each ageing day that made repayments. These customers received zero ageing benefit under the current net-figure logic. The new decomposed model ensures their repayments are recognised independently.

| Ageing day | Accounts in shortfall | Repayments made | % making repayments |
| --- | --- | --- | --- |
| 1 | 80,046 | 9,698 | 12.12% |
| 2 | 45,744 | 3,570 | 7.80% |
| 3 | 25,461 | 2,194 | 8.62% |
| 4 | 17,999 | 1,140 | 6.33% |
| 5 | 13,625 | 716 | 5.26% |
| 6 | 8,194 | 1,015 | 12.39% |
| 7 | 5,630 | 521 | 9.25% |

At ageing day 6 alone, 12.4% of accounts in shortfall made repayments — accounts that under the current logic were still sold off the next day despite acting in good faith.

### Shortfall type reference

| Type | Trigger | Ageing logic | Due date | Applicable products |
| --- | --- | --- | --- | --- |
| `PORTFOLIO_SHORTFALL` | Customer LTV DP < Exposure | Multiple instances, +1 per market day | EOD of ageing day 7 (non-shifting) | LAMF, LAS (configurable) |
| `RISK_SHORTFALL` | Risk LTV DP < Exposure | Multiple instances, +1 per market day | EOD of ageing day 7 (non-shifting) | LAMF, LAS (configurable) |
| `EXPOSURE_BREACH_SHORTFALL` | DP/Exposure ratio < configured breach threshold (default: 85%) | Single instance, ageing maintained, amount updated in place | Same day 12 noon | LAMF (configurable) |
| `INTRADAY_EXPOSURE_BREACH_SHORTFALL` | DP/Exposure ratio < configured breach threshold, identified intra-day via sell-off request | Single instance per day, created at time of sell-off request | Same day, time of breach | LAS (configurable) |

### Due date calculation — non-shifting logic

Current bug: due date shifts every day as ageing increases (due date = today + remaining days to threshold). Correct behaviour: due date is anchored to the day on which ageing day 7 would have occurred relative to the shortfall creation date.

Example: if today is ageing day 9 of a risk shortfall, the due date is calculated as: date on which ageing day 7 fell (2 days ago) → not today + 0, but that historical date. This means the account is already past due, and the noon process will have already flagged it for sell-off.

### Key terminology

| Term | Definition |
| --- | --- |
| DP | Drawing Power — max permissible loan amount based on pledged collateral value × LTV |
| Exposure | POS + Interest Overdue — total customer liability |
| ΔDP | Change in Drawing Power day-over-day |
| ΔExposure | Change in Exposure day-over-day. Negative = repayment/reduction |
| FIFO knock-off | Recovery applied to oldest open shortfall instance first |
| BOD job | Beginning-of-Day batch job, runs before market opens |
| Market day | Day on which securities markets are open and MF NAVs are published |
| Portfolio shortfall | Shortfall computed using customer LTV — preventive threshold |
| Risk shortfall | Shortfall computed using Risk LTV — enforcement threshold |
| Exposure breach shortfall | Shortfall triggered when DP/Exposure ratio falls below configured threshold (default 85%) — same-day action, identified at BOD for LAMF |
| Intraday exposure breach shortfall | Shortfall triggered intra-day for LAS when sell-off request is raised and DP/Exposure breach is identified at that moment |
| STP | Straight-through processing — automated comms with no manual gate |
| FXLAN | Unique loan account identifier |