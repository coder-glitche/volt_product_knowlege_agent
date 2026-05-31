# Part payments - No cost EMI / TL (Cred)

Last Edited: May 22, 2026 11:34 AM
PRD ETA: May 22, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

## Background and context

### Who is facing the problem

- Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities.
- Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure.
- Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually.

### What is broken today

- Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche.
- The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live.
- Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further.
- Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan.

### Why it matters

- Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this.
- Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure.
- Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path.

---

## 1. Problem scope

| In scope | Out of scope |
| --- | --- |
| Term loan (TL) tranches on active credit lines | Overdraft (OD) products |
| Tranche-level principal reduction | Line-level part payments |
| Payment-led part payment (with repayment order) | Accrued interest settlement |
| Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment |
| Reduce EMI amortisation mode | Generic repayment wallet behaviour |
| Reduce tenure amortisation mode | Prepayment charges |
| Shortfall reduction via principal paydown | Lender-triggered restructuring |
| Tactical deleveraging | Foreclosure flows |
| Collections-assisted restructuring | Unpledging workflows |
| SOA remark on part payment receipt | Borrower communications (separate initiative) |
|  | Cross-tranche excess consumption |

### Rationale for exclusions

- **OD excluded:** OD exposure is a single POS figure with no amortisation schedule. Will be scoped separately.
- **Accrued interest and due settlement excluded:** part payment is strictly a principal-reduction utility. Mixing it with the repayment waterfall creates allocation ambiguity.
- **Cross-tranche excess excluded:** Finflux manages excess consumption order natively. Excess tagged to a different tranche is not made available for a given tranche's part payment. No orchestration required on our side.
- **Foreclosure and unpledging excluded:** these are live features with their own flows. Part payment is explicitly not a near-foreclosure trigger.

---

## 2. Success criteria

### Outcomes

- Borrowers can self-serve a principal reduction on a TL tranche without calling collections or ops.
- Borrowers in shortfall can cure exposure durably through part payment, reducing forced sell-off events.
- Collections teams have a product-supported tool to recommend and assist with partial paydowns.

### Key success metrics

| Metric | Target | Measurement |
| --- | --- | --- |
| Simulation-to-execution conversion | ≥ 60% of simulations result in an executed part payment | Funnel analytics |
| Schedule update success rate | ≥ 99.5% of executions result in correct schedule update in LMS | Error rate monitoring |
| Shortfall cure via part payment | Measurable reduction in sell-off events for borrowers who used part payment | RMS event log |

### Guardrail metrics

- Execution API error rate must not exceed 0.5%.
- LMS schedule version conflicts must not exceed 0.1% of executions.
- Incorrect shortfall recalculation post part payment: zero tolerance.

---

## 3. Solution scope

### Solution overview

Part payment is a borrower-initiated principal reduction utility for active TL tranches. It operates through a single execution API that supports two modes of invocation depending on whether a new payment is being made or existing excess is being consumed. A separate stateless simulation API allows borrowers to preview the impact of any part payment amount before committing.

The execution API handles both flows internally. When a repayment order is passed, it posts the payment first, creates excess tagged to the tranche, and Finflux immediately applies that excess as a part payment against the tranche principal. When no repayment order is passed, Finflux consumes available excess against the tranche directly. Excess sourcing and consumption priority is managed natively by Finflux — we pass the instruction and Finflux handles the excess mechanics.

The backend is structured to be atomic — excess creation, excess consumption, principal reduction, and schedule regeneration happen in a single coordinated sequence. The feature is intentionally narrow: it does not touch accrued interest, overdue dues, or foreclosure flows.

---

### The two execution flows

### Flow 1 — payment-led part payment

Used when the borrower is making a fresh payment alongside the part payment instruction. The repayment order is passed in the API call.

| Step | Action | System behaviour |
| --- | --- | --- |
| 1 | Repayment order received with tranche ID and amortisation mode | Payment posted as a standard loan repayment |
| 2 | Excess created | Excess created at loan level and tagged to the specified tranche by Finflux |
| 3 | Part payment processed | Finflux applies tagged excess to post a part payment against the tranche principal |
| 4 | Schedule regenerated | Amortisation recalculated from next EMI cycle date per selected mode |
| 5 | SOA remark written | Part payment received for tranche account number: [FXTLAN] |

### Flow 2 — excess-led part payment

Used when the borrower already holds excess and wishes to apply it as a principal reduction. No repayment order is passed.

| Step | Action | System behaviour |
| --- | --- | --- |
| 1 | Part payment request received with amount, tranche ID, and amortisation mode | Eligibility validated: line active, no overdue on line, sufficient excess available |
| 2 | Excess sourced and applied | Finflux manages excess consumption order natively against the specified tranche. If available excess < requested amount: transaction rejected with available balance returned. |
| 3 | Part payment processed | Principal outstanding reduced by part payment amount |
| 4 | Schedule regenerated | Amortisation recalculated from next EMI cycle date per selected mode |
| 5 | SOA remark written | Part payment received for tranche account number: [FXTLAN] |

---

### Simulation API

Separate, stateless, and independent of the two execution flows. Used for borrower decision-making and UX preview only. Takes amount, tranche ID, and amortisation mode. Simulates the effect of a part payment on the schedule regardless of whether the borrower intends to use Flow 1 or Flow 2. Does not validate excess availability or repayment order — execution validates independently.

---

### Supported use cases

| Use case | Description | Outcome |
| --- | --- | --- |
| **Reduce EMI** | Borrower pays down principal; tenure stays the same; future EMI reduces. | Lower monthly obligation; improved affordability. |
| **Reduce tenure** | Borrower pays down principal; EMI stays the same; loan closes earlier. | Faster closure; reduced total interest. |
| **Tactical deleveraging** | Borrower deploys temporary liquidity (bonus, redemption) to reduce exposure and improve LTV. | Lower principal outstanding; improved collateral coverage. |
| **Shortfall cure** | Borrower reduces principal outstanding to cure shortfall exposure and avoid forced liquidation. | Durable shortfall reduction; liquidation risk lowered. |
| **Collections-assisted restructuring** | Collections team recommends a part payment amount and mode; borrower executes via app. | Reduced delinquency probability; sustainable repayment plan. |

---

### Core happy path — Flow 1 (payment-led)

1. Borrower navigates to active tranche, taps 'Make part payment'.
2. Eligibility check: line active, no overdue on line.
3. Borrower enters amount and selects amortisation mode.
4. Simulation API called (stateless): returns revised schedule, new EMI or tenure, shortfall and LTV impact.
5. Borrower reviews before/after schedule and confirms.
6. Execution API called: repayment order + tranche ID + amortisation mode + idempotency key.
7. Payment posted as loan repayment → excess created and tagged to tranche → Finflux applies excess as part payment → principal reduced.
8. LMS schedule regenerated from next EMI cycle.
9. SOA remark written: *Part payment received for tranche account number: [FXTLAN]*.
10. Borrower sees updated schedule in app.

### Core happy path — Flow 2 (excess-led)

1. Borrower navigates to active tranche, taps 'Make part payment'.
2. Eligibility check: line active, no overdue on line, available excess balance surfaced.
3. Borrower enters amount (≤ available excess) and selects amortisation mode.
4. Simulation API called: returns revised schedule, shortfall and LTV impact.
5. Borrower reviews before/after and confirms.
6. Execution API called: amount + tranche ID + amortisation mode + idempotency key (no repayment order).
7. Finflux sources and consumes excess against the tranche. If insufficient, reject with available balance.
8. Principal reduced → LMS schedule regenerated from next EMI cycle.
9. SOA remark written: *Part payment received for tranche account number: [FXTLAN]*.
10. Borrower sees updated schedule in app.

---

### Key edge cases at launch

| Scenario | System behaviour | Validation layer |
| --- | --- | --- |
| Amount = 0 | Rejected. Amount must be greater than zero. | Simulation + Execution API |
| Amount ≥ total principal outstanding on tranche | Rejected. Borrower directed to foreclosure flow if intent is full closure. | Simulation + Execution API |
| Overdue exists anywhere on line | Part payment blocked. Borrower must clear dues through normal repayment flow first. | Execution API eligibility check |
| Line inactive or closed | Part payment blocked. Line status error surfaced. | Execution API eligibility check |
| Flow 2: available excess < requested amount | Transaction rejected in full. Error returned with available excess balance. Partial processing not supported. | Finflux / Execution API |
| Duplicate execution (same idempotency key) | Second call returns result of first execution without reprocessing. | Execution API idempotency |
| Part payment after NACH presented for current cycle | Effective date defaults to next EMI cycle. Due dates for current cycle unchanged. | LMS schedule regeneration |
| Multiple part payments on same tranche | Each execution is independent. Schedule regenerated from next cycle on each execution. | LMS schedule versioning |
| Residual principal after part payment | No auto-closure. Tranche continues on revised schedule. Foreclosure is a separate explicit flow. | LMS + DRPS |

---

### Stakeholder impact

| Stakeholder | Impact |
| --- | --- |
| **Borrower** | New self-serve flow to reduce principal on a TL tranche via fresh payment or existing excess. Revised schedule visible in app after execution. |
| **Collections team** | Product-supported tool to recommend part payment as part of restructuring conversations. Execution remains borrower-initiated; no SOP change required. |
| **Risk / RMS** | Shortfall recalculation happens automatically after principal reduction. No change to liquidation trigger logic — part payment reduces Σ principal outstanding, RMS re-evaluates on next cycle. |
| **Ops / Lender** | SOA remark written on every part payment execution. Full audit trail via transaction reference and schedule version. |
| **LSP partners** | No immediate interface change. Future: part payment status surfaced via webhook on execution. |

---

## 4. API specification

### Simulation API

Stateless. No side effects. No persistence. Independent of execution flow. Used for borrower decision-making and UX preview only.

**Request inputs**

- `line_id`
- `tranche_id` — always passed explicitly, even on single-tranche lines
- `part_payment_amount` — must be > 0 and < total principal outstanding on tranche
- `amortisation_mode` — enum: `reduce_emi` | `reduce_tenure`
- `effective_date` — defaults to next EMI cycle date

**Response outputs**

- `revised_schedule` — full updated repayment schedule
- `current_emi` / `revised_emi`
- `current_tenure` / `revised_tenure`
- `principal_reduction`
- `shortfall_impact` — delta on shortfall exposure
- `ltv_improvement` — revised LTV post part payment
- `warnings` — e.g. amount ≥ principal outstanding

---

### Execution API

Single API. Two modes depending on whether a repayment order is passed. Idempotent. Validates all eligibility rules independently of simulation. Excess sourcing and consumption handled natively by Finflux.

**Request inputs**

- `line_id`
- `tranche_id` — always explicit
- `part_payment_amount`
- `amortisation_mode` — `reduce_emi` | `reduce_tenure`
- `repayment_order` — optional. If present: Flow 1 (payment-led). If absent: Flow 2 (excess-led).
- `idempotency_key` — caller-provided, unique per transaction
- `transaction_reference` — for audit trail

**Eligibility validations**

- Amount > 0
- Amount < total principal outstanding on tranche
- No overdue dues anywhere on line
- Line status = active
- Flow 2 only: available excess ≥ requested amount (validated by Finflux; rejection returned with available balance)

**On successful execution (both flows)**

- DRPS updated: principal outstanding on tranche reduced.
- LMS triggered: amortisation schedule regenerated from next EMI cycle date.
- SOA remark written: *Part payment received for tranche account number: [FXTLAN]*.
- Response: updated schedule summary, transaction reference, new principal outstanding, flow type used.

---

## 5. High level system and process flow

### System sequencing — Flow 1 (payment-led)

> Steps 2–5 must be treated as an atomic unit. A failure at any step must not leave the system in an inconsistent state.
> 

| Step | Action | Owner system |
| --- | --- | --- |
| 1 | Execution API receives request: repayment order + tranche ID + amortisation mode + idempotency key | Fenix / Orchestration |
| 2 | Eligibility validated: amount, overdue check, line status | Fenix |
| 3 | Repayment order posted as standard loan repayment | Finflux / LMS |
| 4 | Excess created at loan level, tagged to specified tranche | Finflux / LMS |
| 5 | Tagged excess applied as part payment; principal reduced | Finflux / LMS |
| 6 | Amortisation schedule regenerated from next EMI cycle date | Finflux / LMS |
| 7 | SOA remark written against tranche account number | Finflux / LMS |
| 8 | Response returned with updated schedule summary and transaction reference | Fenix |

### System sequencing — Flow 2 (excess-led)

> Steps 2–4 must be treated as an atomic unit.
> 

| Step | Action | Owner system |
| --- | --- | --- |
| 1 | Execution API receives request: amount + tranche ID + amortisation mode + idempotency key (no repayment order) | Fenix / Orchestration |
| 2 | Eligibility validated: amount, overdue check, line status | Fenix |
| 3 | Finflux sources and applies excess against the tranche. If insufficient: reject with available balance. Stop. | Finflux / LMS |
| 4 | Principal reduced | Finflux / LMS |
| 5 | Amortisation schedule regenerated from next EMI cycle date | Finflux / LMS |
| 6 | SOA remark written against tranche account number | Finflux / LMS |
| 7 | Response returned with updated schedule summary and transaction reference | Fenix |

### Shortfall sequencing

Part payment reduces Σ principal outstanding on the tranche. This directly improves the shortfall formula (min(DP, SL) − Σ principal outstanding + line-level excess). RMS re-evaluates shortfall on its next recalculation cycle. No special orchestration between part payment execution and RMS is required.

### Error handling

- **Simulation validation failures** (amount ≥ principal, invalid tranche): returned as structured warnings. No execution attempted.
- **Execution eligibility failures:** HTTP 422 with structured error payload. Idempotency key not consumed.
- **Flow 2 insufficient excess:** HTTP 422 with available excess balance in response. Returned by Finflux. Idempotency key not consumed.
- **Finflux / LMS failure after eligibility pass:** compensating event raised, ops alert triggered. Must not leave principal reduced without a corresponding schedule update.

---

## 6. Key open items for engineering

| # | Question | Context | Owner |
| --- | --- | --- | --- |
| 1 | Does Finflux expose a simulation API for part prepayments that returns a revised schedule without committing the transaction? | Pending response from Finflux. If not exposed, need to determine whether it exists in product and can be surfaced, or requires net new development. | Finflux / Engineering |
| 2 | Does the Finflux simulation API support both reduce EMI and reduce tenure modes? | Required for launch. If only one mode is supported natively, we need a fallback plan for the other. | Finflux / Engineering |
| 3 | What is the rollback mechanism if Finflux schedule update fails after principal reduction is posted? | Must not leave principal reduced without a corresponding schedule update. Compensating event or saga pattern needed. | Engineering |
| 4 | Does NACH presentation for the current cycle get affected by a principal update mid-cycle? | Due dates are unchanged and new schedule applies from next cycle. Confirm NACH debit for current cycle is not impacted. | Engineering / Payments |
| 5 | What is the schedule versioning scheme in Finflux for multiple successive part payments? | Each part payment must produce a clean new version without conflicts when multiple payments occur on the same tranche. | Finflux / Engineering |

---

## Appendix

### Amortisation mode behaviour summary

| Dimension | Reduce EMI | Reduce tenure |
| --- | --- | --- |
| EMI amount | Reduces | Unchanged |
| Loan tenure | Unchanged | Reduces |
| Due dates | Unchanged | Unchanged |
| Principal outstanding | Reduced immediately | Reduced immediately |
| Schedule effective from | Next EMI cycle | Next EMI cycle |
| Borrower benefit | Lower monthly burden | Faster closure; less total interest |

### Execution flow decision tree

| Condition | Flow invoked | Key behaviour |
| --- | --- | --- |
| `repayment_order` present in API call | Flow 1 — payment-led | Post repayment → create tagged excess → Finflux applies excess → principal reduced |
| `repayment_order` absent in API call | Flow 2 — excess-led | Finflux sources and applies available excess against tranche |
| Available excess < requested amount (Flow 2) | Reject | Finflux returns available excess balance in error response |

### Validation rules summary

| Rule | Flow | Layer | Behaviour on failure |
| --- | --- | --- | --- |
| Amount > 0 | Both | Simulation + Execution | Reject with validation error |
| Amount < total principal outstanding | Both | Simulation + Execution | Reject; direct to foreclosure if full closure intended |
| No overdue on line | Both | Execution only | Block; surface dues clearance instruction |
| Line status = active | Both | Execution only | Block; surface line status error |
| Available excess ≥ requested amount | Flow 2 only | Finflux | Reject in full; return available excess balance |
| Idempotency key unique per transaction | Both | Execution only | Duplicate returns first result without reprocessing |

---

## Version history

| Version | Section changed | Change summary | Reason |
| --- | --- | --- | --- |
| v1 → v2 | Core architecture — all sections | Replaced single execution flow with a single API operating in two distinct modes: Flow 1 (payment-led, with repayment order) and Flow 2 (excess-led, without repayment order). Principal reduction is now always excess-mediated via Finflux. | New understanding that payment must be posted as a loan repayment first, creating excess which is then applied as part payment. |
| v1 → v2 | Solution overview | Added explanation of excess as the internal mechanism through which part payment is processed in both flows. | Architectural clarification on payment posting sequence. |
| v1 → v2 | Problem scope — in scope | Added: payment-led part payment (with repayment order) and excess-led part payment (consuming existing excess). | Two distinct invocation modes now explicit. |
| v1 → v2 | Problem scope — out of scope | Added: cross-tranche excess consumption with rationale. | Finflux manages excess consumption natively; cross-tranche excess is never made available. |
| v1 → v2 | Happy paths | Split into two separate happy paths — one per flow — with excess availability check and sourcing logic called out in Flow 2. | Single happy path was insufficient to describe both modes. |
| v1 → v2 | System sequencing | Split into two sequencing tables (one per flow) with owner systems (Fenix, Finflux/LMS) called out per step. | Responsibility boundary between Fenix and Finflux needed to be explicit. |
| v1 → v2 | Edge cases | Added: Flow 2 insufficient excess → reject with available balance. Added: Flow 2 cross-tranche only → reject. | New failure modes introduced by excess-led flow. |
| v1 → v2 | Execution API spec | Added repayment_order as optional input. Added Flow 2 excess sufficiency validation. Removed explicit excess consumption priority (delegated to Finflux). | API contract updated to reflect two-mode design. |
| v1 → v2 | Open items | Added item 3: whether LMS supports excess tagging to a tranche atomically. | New hard dependency introduced by Flow 1. |
| v1 → v2 | Appendix | Added execution flow decision tree. Updated validation rules table to distinguish flow applicability. | Engineering reference aids for routing logic. |
| v2 → v3 | Solution overview + sequencing tables | Removed explicit excess consumption priority order as a system behaviour we orchestrate. Finflux manages this natively — we pass the instruction, Finflux handles sourcing. | Confirmed that Finflux owns excess consumption order internally. No orchestration required on our side. |
| v2 → v3 | Open items | Closed item 3 (excess tagging to tranche confirmed to exist in Finflux). Replaced with two new items: does Finflux expose a simulation API and does it support both amortisation modes. | Excess tagging confirmed live. Simulation API availability is the remaining open dependency pending Finflux response. |
| v2 → v3 | Scope rationale — cross-tranche exclusion | Updated rationale to reflect that Finflux manages consumption order natively, not that we enforce it. | Accurate attribution of system responsibility. |
| v2 → v3 | Version history page | Added this changelog as an appendix page. | Document version tracking. |