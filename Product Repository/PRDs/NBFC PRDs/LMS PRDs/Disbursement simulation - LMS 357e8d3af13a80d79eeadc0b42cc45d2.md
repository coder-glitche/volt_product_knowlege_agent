# Disbursement simulation - LMS

Last Edited: May 22, 2026 3:49 PM
PRD ETA: May 5, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

## Background and Context

- **Who is affected**
    - Borrowers using Volt (DSP Finance's LSP) who initiate withdrawal requests from their Loan Against Mutual Fund (LAMF) accounts.
    - All LSP partners integrated with DSP Finance's disbursement infrastructure.
    - DSP Finance's Risk Operations team, who are exposed to collateral shortfall risk when disbursements breach the safe limit.
- **What is broken today**
    - The current Available Limit calculation — `AL = min(DP, SL) - POS + EM`  does not account for accrued interest, charges, or scenarios where non-principal exposure grows to exceed the margin held against collateral. Two specific scenarios expose DSP Finance to risk:
        - **Case 1 — Collateral Removal:** After a borrower repays principal and requests maximum collateral removal, the remaining collateral may only cover the Drawing Power. Any subsequent withdrawal creates a situation where accrued interest (once booked as Interest Due) pushes total exposure above collateral value.
        - **Case 2 — Voluntary Sell-off:** After a sell-off settles principal, the sell-off proceeds inflate Excess Money, which inflates the Available Limit. A borrower can withdraw this excess, creating a POS that, combined with accrued interest becoming due, exceeds the remaining collateral value.
    - Today, the Loan Detail API value is trusted by all downstream systems (Fenix, Volt, and LSP partners) as the authoritative available limit. There is no pre-disbursement validation layer that applies the updated risk-safe AL formula before funds are transferred.
- **Why it matters**
    - Collateral shortfall represents direct credit risk for DSP Finance — in cases of default, outstanding dues cannot be fully recovered.
    - The gap grows over time as accrued interest compounds, making early intervention critical.
    - LSP partners rely on the available limit shown to borrowers; without a simulation gate, disbursements that breach exposure limits will be processed without any check.

---

## 1. Problem Scope

### In scope

- Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula.
- Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen.
- Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum allowed amount and enabling re-entry.
- API design contract documentation to be shared with all LSP partners for integration.
- Post-integration: enforcement gate in the Disbursement Request API that hard-blocks disbursements exceeding the simulated limit.
- Primary users: Borrowers (Volt), LSP partner systems, DSP Finance Risk Ops.

### Out of scope

| Item | Rationale for Exclusion |
| --- | --- |
| Changes to the Available Limit shown on the Loan Detail API or LMS (Finflux) | Decoupling risk enforcement from the displayed AL is accepted. Core LMS logic and user-facing limit remain unchanged in this phase. |
| Real-time market pricing integration for Loan Against Shares | Future extension of the RMS layer; out of scope for this release. |
| LSP partner frontend integration beyond Volt | LSPs will self-integrate against the API contract; DSP Finance provides the API and documentation only. |

---

## 2. Success Criteria

- **Outcome 1 — Zero Collateral Shortfall Disbursements**
    - Post-launch, no disbursement processed through any LSP partner should result in total exposure (POS + accrued interest + charges) exceeding the collateral value at time of disbursement.
    - Key metric: Count of disbursements where post-disbursement TOS > Collateral Value = 0.
    - Measurement: Daily Risk Ops reconciliation report.
- **Outcome 2 — Seamless Borrower Experience on Volt**
    - Borrowers who enter an amount within the simulation limit experience zero additional friction. Borrowers who exceed the limit are shown the maximum allowed amount clearly and can re-enter without drop-off.
    - Key metric: Withdrawal funnel drop-off rate (Enter Amount → Confirm Amount) should not increase by more than 2% post-launch.
    - Guardrail: Disbursement Simulation API P99 latency < 500ms; error rate < 0.5%.
- **Outcome 3 — All LSP Partners Integrated Before Hard Enforcement**
    - The enforcement gate in the Disbursement Request API is switched on only after all active LSP partners have confirmed successful integration and testing against the simulation API.
    - Key metric: 100% of active LSP partners complete integration sign-off before gate activation.
    - Guardrail: Zero legitimate disbursement failures due to enforcement gate after go-live.

---

## 3. Solution Scope

### Solution overview

- We will build a standalone Disbursement Simulation API (within the Fenix Risk Management System layer) that computes the maximum safe withdrawal amount using the updated AL formula. Volt's frontend will call this API between withdrawal amount entry and confirmation. All LSP partners will be required to integrate this simulation check. Once integrations are confirmed, a hard enforcement gate will be placed in the Disbursement Request API to block non-compliant requests.
- This approach preserves existing Loan Detail API behaviour and Finflux LMS logic, avoiding cross-cutting changes to the displayed available limit, while placing enforcement at the disbursal action point where risk is actually realised.

**Updated Available Limit for Disbursement Formula**

`If (TOS − POS + Accrued Interest) > 5% of DP:
    Available limit for disbursement = DP − POS + Excess Margin − (TOS − POS + AI)
Else:
    Available limit for disbursement = DP − POS + Excess MarginmLMS OMssdfds\`

`dfdsfKM 

Note: The 5% scale factor ensures that the exposure beyond principal
is less than half the minimum 10% margin held for liquid funds.`

### Detailed solution scope

**A. Disbursement Simulation API — Backend (Fenix / RMS)**

| Description | Details |
| --- | --- |
| Simulate maximum disbursement for a loan | Given a `loan_id`, compute the AL using the updated formula. Return: `sim_max_amount`

(standard or risk-adjusted), and input values used for computation (DP, POS, EM, TOS, AI). |
| API availability / fail-open behaviour | If the simulation API is unavailable or times out, the calling system (Volt FE or LSP) should fail open — i.e., allow the disbursement to proceed. To be reviewed once the enforcement gate is live.

Impact: Disbursement request may fail |
| Data freshness | The API must consume real-time loan data (POS, AI, TOS, DP, EM) at the time of the call, not cached values. |

**B. Volt Frontend Integration — Withdrawal Flow**

| Description | Details |  |
| --- | --- | --- |
| Happy path: amount within limit | Borrower enters withdrawal amount on Screen 1 (Enter Amount) and taps 'Proceed to confirm amount'. Volt calls the Disbursement Simulation API. If `requested_amount ≤ sim_max_amount`, proceed to Screen 2 (Confirm Amount) as today — no change to borrower experience. |  |
| Amount exceeds simulation limit | If `requested_amount > sim_max_amount`, Screen 1 shows an inline error: *"You can withdraw up to ₹X based on your current loan position. Please update the amount to proceed."* The amount field is pre-filled with `sim_max_amount`. Borrower can edit and re-submit. |  |
| Simulation API unavailable (fail-open) | If the API call fails or times out, Volt proceeds to Screen 2 without blocking. No error shown to borrower.  |  |
| Loading state | A brief loading indicator is shown while the simulation API call is in flight (between tapping 'Proceed' and navigating to Screen 2). Target: < 500ms so the loading state is imperceptible in normal conditions. |  |

**C. LSP Partner Integration (GTM)**

| Description | Details |
| --- | --- |
| API contract distribution | DSP Finance / Fenix team publishes the Disbursement Simulation API contract (OpenAPI spec) to all active LSP partners. |
| Partner integration window | Each LSP partner is expected to integrate the simulation call into their withdrawal UX before the enforcement gate is activated. DSP Finance to track integration status per partner. |
| Enforcement validations activation | Once all partners confirm integration and sign off on testing, the Disbursement Request API will begin validating that `requested_amount ≤ sim_max_amount`. Requests exceeding this will be rejected with a clear error code and message. |
| Partners who have not integrated by gate activation | Their disbursements will begin to fail at the Disbursement Request API. This is an intentional risk outcome — non-integrated partners are the source of exposure. |

**D. Impact on Existing Workflows**

| Workflow | Impact |
| --- | --- |
| Loan Detail API / displayed available limit | No change. The limit shown to borrowers on account summary screens remains as today. |
| Finflux LMS | No change to core LMS logic. |
| Sales / onboarding conversations | No change to borrower-facing available limit communication. Internal note: the amount a borrower can actually disburse may be lower than displayed AL in high-accrued-interest scenarios. |

---

## 5. High-Level System, User or Process Flow

**Volt Borrower Withdrawal Flow (Updated)**

`Step 1 — Borrower opens withdrawal screen (Volt Screen 1: Enter Amount)
          └ Available limit displayed from Loan Detail API (unchanged)

Step 2 — Borrower enters withdrawal amount and taps 'Proceed to confirm amount'

Step 3 — Volt calls Disbursement Simulation API
          ├ If API responds within timeout:
          │   ├ requested_amount ≤ sim_max_amount → Navigate to Screen 2 (no change)
          │   └ requested_amount > sim_max_amount → Inline error on Screen 1
          │                                          Pre-fill with sim_max_amount; borrower re-enters
          └ If API times out or errors → Fail open: navigate to Screen 2; log as simulation-skipped

Step 4 — Borrower reviews and confirms on Screen 2 (Confirm Amount)

Step 5 — Volt submits Disbursement Request to Fenix
          ├ [Pre-enforcement]  Request processed as today
          └ [Post-enforcement] Fenix validates amount ≤ sim_max_amount; rejects if not`

**LSP Partner Integration GTM Flow**

`1. Fenix publishes Disbursement Simulation API OpenAPI spec to all LSP partners
2. Each LSP partner integrates simulation call into their withdrawal UX
3. DSP Finance conducts integration testing with each partner in staging
4. Partner sign-off obtained
5. Once 100% of active partners are signed off → enforcement gate activated on Disbursement Request API
6. Risk Ops monitors daily reconciliation report post-activation`

**Edge Cases**

| Scenario | Handling |
| --- | --- |
| Simulation API down / timeout | Fail open — borrower proceeds. Logged as `simulation-skipped` for Risk Ops. |
| Borrower enters amount exactly equal to `sim_max_amount` | Treated as within limit — proceed to confirm screen. |
| `sim_max_amount` is zero or negative | Show message: *"Withdrawal is not available on your account at this time. Please contact support."* Block proceed. |
| Un-pledge request in progress (existing warning) | Existing warning displayed as today; simulation check is independent. |
| LSP partner does not integrate before enforcement gate | Disbursement Request API rejects their requests. Partner notified with error code and remediation steps. |
| EOD excess release with new formula producing negative value | `max()` floor ensures zero is released; no negative excess. |

---

## High-Level Design Requirements

**Screen 1 — Enter Withdrawal Amount (Updated States)**

| Element | Requirement |
| --- | --- |
| Loading state (simulation in flight) | On tap of 'Proceed to confirm amount', show a brief inline spinner or disable the button with a loading label (e.g. *"Checking…"*). Must not feel like a page navigation delay. |
| Error state — amount exceeds limit | Inline error below the amount field (not a modal). Show: *"You can withdraw up to ₹[sim_max_amount] right now. Please update the amount."* Pre-fill amount field with `sim_max_amount`. CTA remains 'Proceed to confirm amount'. |
| Error state — withdrawal unavailable (zero sim max) | Replace amount field area with a message card: *"Withdrawal is not available on your account at this time. Please contact support."* Disable CTA. |
| Tone | Non-alarming, factual. Avoid language implying the borrower has done something wrong. Frame as a 'current account position' limit, not a penalty. |
| Existing elements | Available cash, un-pledge warning, amount-in-words, WhatsApp help button — all unchanged. |

**Screen 2 — Confirm Amount**

- No changes required. The confirm screen is only reached after the simulation check passes.

## 6. Appendix

### Definitions

| Term | Definition |
| --- | --- |
| AL | Available Limit — the amount a borrower is permitted to withdraw at a given point in time. |
| DP | Drawing Power — maximum credit limit basis current collateral value and LTV. |
| SL | Sanctioned Limit — maximum approved credit limit. |
| POS | Principal Outstanding — amount currently drawn by borrower. |
| AI | Accrued Interest — interest earned but not yet booked as due. |
| ID / IOD | Interest Due / Interest Overdue. |
| CD / COD | Charges Due / Charges Overdue. |
| TOS | Total Outstanding = POS + CD + COD + ID + IOD. |
| EM | Excess Money — funds in the loan account above POS (e.g. from sell-off proceeds). |
| RMS | Risk Management System — the Fenix layer that owns risk validation logic independently of Finflux LMS. |
| LSP | Lending Service Provider — partner platforms (including Volt) that originate loans on behalf of DSP Finance. |

### Risk Scenario Reference

Refer to Shreyas's original risk memo (DSP Risk Ops, 05 May 2026) for full numerical worked examples of Case 1 (Collateral Removal) and Case 2 (Voluntary Sell-off).