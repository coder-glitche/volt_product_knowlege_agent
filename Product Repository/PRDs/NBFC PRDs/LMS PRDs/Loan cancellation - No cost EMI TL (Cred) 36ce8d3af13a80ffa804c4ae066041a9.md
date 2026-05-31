# Loan cancellation - No cost EMI / TL (Cred)

Last Edited: May 26, 2026 9:08 PM
PRD ETA: May 26, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

---

## Background and context

### Who is facing the problem

- Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey.
- Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower.
- CRED TL customers who have taken a loan and want to cancel within the loan cancellation period.
- Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure.
- Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED.

### What is broken today

- There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery.
- When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower.
- Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed.

### Why it matters

- **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on.
- **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect.
- **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone.

---

## 1. Problem scope

| In scope | Out of scope |
| --- | --- |
| No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) |
| Insurance Premium Financing (IPF) loan cancellation | Partial cancellation |
| All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) |
| Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) |
| Obligation-level configurability for waiver and refund | Bureau reporting exclusion logic (Fenix layer) |
| Excess creation tagged to cancelled tranche | Collateral release and unpledging (separate flow) |
| Accrued interest waiver with income reversal accounting entry | DP recalculation on cancellation |
| Collected obligation refund via excess → foreclosure flow | Communications to borrower (separate initiative) |
| Tranche mapping update on excess consumption | OD product cancellation |
| CANCELLED status distinct from CLOSED and FORECLOSED |  |

### Cancellation triggers by product

| Product | Trigger | Initiator |
| --- | --- | --- |
| No Cost EMI | Product return by borrower | Merchant + DSP Finance (mutual) |
| No Cost EMI | User drop-off during journey | DSP Finance |
| IPF | Insurance policy cancelled by insurer | Insurer via DSP Finance |
| IPF | Insurance policy cancelled by borrower | Borrower via DSP Finance |
| TL CRED | Loan cancelled via Lender on borrower request | Borrower via DSP Finance |

### Rationale for exclusions

- **Foreclosure excluded:** live feature with different trigger, charge treatment, and settlement logic. Cancellation must not reuse the foreclosure flow.
- **Partial cancellation excluded:** only full loan cancellation is in scope. Tranche-level partial principal reduction is handled by part payment.
- **Borrower-unilateral cancellation excluded:** cancellation requires merchant initiation and settlement first. Enforced at Fenix layer; not a Finflux constraint.
- **Communications excluded:** borrower notifications will be handled as a separate initiative post-launch.

---

## 2. Success criteria

### Outcomes

- Cancelled loans carry a distinct CANCELLED status that prevents bureau reporting and is distinguishable from CLOSED and FORECLOSED in all downstream systems.
- Collected amounts are refunded to borrowers accurately and without manual intervention via the excess → foreclosure refund flow.
- P&L treatment for interest waiver on cancellation is clean — income reversal, not write-off.

### Key success metrics

| Metric | Target | Measurement |
| --- | --- | --- |
| Cancellation execution success rate | ≥ 99.5% | Error rate monitoring on cancellation API |
| Incorrect bureau reporting on cancelled loans | Zero | Bureau report audit post-launch |
| Refund accuracy (excess created = collected obligations configured for refund) | 100% | Reconciliation report |

### Guardrail metrics

- Cancellation must not trigger foreclosure flow or create CLOSED status. Zero tolerance.
- Income reversal entry for accrued interest must be posted on every cancellation where accrued interest exists. Zero misses.
- Excess tagged to wrong tranche or wrong amount: zero tolerance.

---

## 3. Solution scope

### Solution overview

Loan cancellation is a new lifecycle event for NCEMI and IPF tranches. It is triggered after merchant settlement is confirmed (for NCEMI) or after policy cancellation is confirmed (for IPF). The cancellation flow waives all outstanding and accrued obligations, moves collected amounts to excess tagged to the cancelled tranche, updates the loan status to CANCELLED, and returns a confirmation with the excess amount created. The excess is then consumed by the existing foreclosure process to refund the customer.

Cancellation is configurable at the obligation level — DSP Finance controls which obligation types are included in the waiver and refund pool per cancellation request. The cancellation window is also configurable at the product level, replacing the original 14-day hard limit.

---

### Merchant settlement sequencing (context for ops)

Cancellation always follows merchant settlement. The sequence is:

| Step | Action | Owner |
| --- | --- | --- |
| 1 | Merchant or insurer initiates cancellation | Merchant / Insurer |
| 2 | Merchant settles complete loan amount to DSP Finance via MMS | Merchant / MMS |
| 3 | DSP Finance confirms settlement receipt | DSP Finance / Fenix |
| 4 | Fenix triggers loan cancellation API on Finflux | Fenix |
| 5 | Finflux executes cancellation: waive obligations, create excess on tranche, update status | Finflux / LMS |
| 6 | Fenix initiates refund to borrower via foreclosure process using excess on cancelled tranche | Fenix |
| 7 | Excess consumed; tranche mapping updated | Finflux / LMS |

---

### The four cancellation scenarios

| Scenario | Loan state at cancellation | Finflux actions | Excess created? |
| --- | --- | --- | --- |
| 1 | No obligations of any kind | Status → CANCELLED | No |
| 2 | Outstanding / due principal only. No accrued. No collected. | Waive outstanding obligations. Status → CANCELLED. | No |
| 3 | Accrued interest + outstanding / due principal. Nothing collected. | Waive accrued interest (income reversal entry). Waive outstanding obligations. Status → CANCELLED. | No |
| 4 | Collected obligations exist (any type). May also have outstanding and accrued. | Move collected amounts (per obligation config) to excess tagged to cancelled tranche. Waive accrued interest (income reversal). Waive outstanding obligations. Status → CANCELLED. | Yes tagged to cancelled tranche |

---

### Obligation-level configurability

Each obligation type can be independently configured for waiver and inclusion in the excess refund pool. This replaces the blanket "PF non-refundable" rule from the original BRD.

| Obligation type | Default treatment | Configurable? | Notes |
| --- | --- | --- | --- |
| Principal collected | Refund via excess | Yes | Borrower's repaid principal — always refunded by default |
| Interest collected | Refund via excess | Yes | Any interest collected before cancellation |
| Processing fee (PF) | Retained | Yes | Default is retain; can be waived and refunded if configured |
| GST on PF | Retained | Yes | Default is retain; follows PF treatment if waived |
| Penal charges collected | Refund via excess | Yes | Refunded by default on cancellation |
| Accrued interest (uncollected) | Waive — income reversal entry | No | Always waived. Accounting entry only — not a cash refund. |
| Outstanding principal | Waive | No | Always waived. Merchant has already settled full loan amount via MMS. |

---

### Core happy path — Scenario 4 (most complex)

1. Fenix triggers cancellation API with tranche ID, cancellation reason, and list of obligations to waive/refund.
2. Finflux validates: loan is ACTIVE, cancellation date within configured window.
3. Finflux waives accrued interest — posts income reversal accounting entry automatically.
4. Finflux waives outstanding and due obligations.
5. Finflux creates excess equal to collected obligations configured for refund, tagged to the cancelled tranche.
6. Finflux updates loan status to CANCELLED.
7. Finflux updates tranche mapping to reflect cancellation and excess creation.
8. Finflux returns confirmation: interest waived, obligations waived, excess created, tranche ID.
9. Fenix receives response and initiates refund to borrower via foreclosure process using excess on cancelled tranche.
10. Foreclosure process consumes excess; Finflux updates tranche mapping to reflect consumption.

---

### Key edge cases at launch

| Scenario | System behaviour | Validation layer |
| --- | --- | --- |
| Cancellation attempted outside configured window | Rejected. Error returned with configured window and days elapsed. | Finflux cancellation API |
| Loan status is not ACTIVE | Rejected. Error returned with current loan status. | Finflux cancellation API |
| Accrued interest exists — accounting entry | Income reversal entry posted automatically as part of atomic cancellation transaction. Not a separate manual step. | Finflux — atomic |
| PF configured as retained (default) | PF and GST excluded from excess pool. Not refunded to customer. | Obligation config — Fenix layer |
| PF waived before cancellation | Waived amount excluded from excess pool automatically. Refund amount reflects net of waiver. | Finflux |
| No collected obligations (Scenarios 1–3) | No excess created. Cancellation completes with status → CANCELLED only. | Finflux |
| Excess consumed by foreclosure | Tranche mapping updated atomically to reflect consumption. No stale mappings. | Finflux |
| Duplicate cancellation request (same tranche) | Rejected. Loan is already in CANCELLED status. | Finflux cancellation API validation |
| Cancellation attempted on foreclosed loan | Rejected. Foreclosure and cancellation are distinct flows. | Finflux cancellation API validation |

---

### Stakeholder impact

| Stakeholder | Impact |
| --- | --- |
| **Borrower** | Collected amounts refunded accurately via excess → foreclosure flow. No manual intervention. Cancellation distinct from foreclosure on their loan account. |
| **Merchant** | Cancellation is triggered only after merchant settlement is confirmed via MMS. No change to merchant-facing flows. |
| **Collections / Ops** | CANCELLED status is distinct and filterable. Bureau reporting exclusion logic can act on this status cleanly. No manual P&L adjustments needed for interest waiver. |
| **Risk / Bureau** | Loans with CANCELLED status must be excluded from bureau reporting. Enforced at Fenix layer using the CANCELLED status from Finflux. |
| **Finance / Accounting** | Accrued interest waiver is posted as an income reversal automatically — P&L treatment is clean without manual entries. |
| **LSP partners** | No immediate interface change. Cancellation status will be surfaced via loan status APIs. |

---

## 4. API specification

### Cancellation API

Idempotent. Atomic — all steps (interest waiver, obligation waiver, excess creation, status update) execute in a single transaction or roll back entirely.

**Request inputs**

- `tranche_id` — loan account / tranche ID
- `cancellation_date` — date of cancellation event
- `cancellation_reason` — enum: `PRODUCT_RETURN` | `USER_DROP_OFF` | `INSURER_CANCELLATION` | `BORROWER_CANCELLATION`
- `obligations_to_refund` — array of obligation types to include in excess refund pool (e.g. `[PRINCIPAL, INTEREST, PENAL_CHARGES]`)
- `idempotency_key` — caller-provided, unique per cancellation request

**Validations**

- Loan status must be ACTIVE
- Cancellation date must be within the configured cancellation window for the product
- Tranche ID must be valid and belong to an active credit line

**On successful execution**

- Accrued interest waived — income reversal accounting entry posted automatically
- Outstanding and due obligations waived
- Collected obligations in `obligations_to_refund` moved to excess tagged to the cancelled tranche
- Loan status updated to CANCELLED
- Tranche mapping updated to reflect cancellation and excess

**Response**

| Field | Description |
| --- | --- |
| `cancellation_confirmation` | Confirmation of successful cancellation |
| `tranche_id` | Tranche ID cancelled |
| `cancellation_reason` | Reason code echoed back |
| `interest_waived` | Amount of accrued interest reversed |
| `obligations_waived` | Breakdown of waived obligations by type and amount |
| `excess_created` | Total excess created and tagged to cancelled tranche (0 if no collected obligations in scope) |
| `updated_loan_status` | CANCELLED |

---

## 5. High level system and process flow

### End-to-end cancellation flow

| Step | Action | Owner system |
| --- | --- | --- |
| 1 | Merchant settlement confirmed in MMS | MMS / Fenix |
| 2 | Fenix calls cancellation API: tranche ID + reason + obligations_to_refund + idempotency key | Fenix |
| 3 | Finflux validates: ACTIVE status, within cancellation window | Finflux |
| 4 | Accrued interest waived — income reversal entry posted atomically | Finflux |
| 5 | Outstanding / due obligations waived | Finflux |
| 6 | Collected obligations (per config) moved to excess tagged to cancelled tranche | Finflux |
| 7 | Loan status updated to CANCELLED. Tranche mapping updated. | Finflux |
| 8 | Cancellation response returned to Fenix with excess_created amount | Finflux |
| 9 | Fenix initiates borrower refund via foreclosure process using excess on cancelled tranche | Fenix |
| 10 | Foreclosure process consumes excess. Finflux updates tranche mapping. | Finflux |

---

### Cancellation vs foreclosure

| Dimension | Cancellation | Foreclosure |
| --- | --- | --- |
| Initiator | Lender + merchant (mutual) | Borrower |
| Window | Configurable — no hard limit | Anytime post origination |
| Interest treatment | Fully waived — income reversal | Collected up to foreclosure date |
| Principal recovery | From merchant via MMS | From borrower |
| Charges | Not applicable | Ad hoc foreclosure charge at tranche level |
| Loan status | CANCELLED | CLOSED |
| Bureau reporting | Excluded (CANCELLED status) | Reported (CLOSED status) |
| Excess created | Yes (if collected obligations exist) | Yes (refund of overpayment if any) |

### Error handling

- **Cancellation outside window:** HTTP 422 — error with window config and days elapsed. Idempotency key not consumed.
- **Non-ACTIVE loan status:** HTTP 422 — error with current status. Idempotency key not consumed.
- **Partial failure mid-transaction:** full rollback. Cancellation must be atomic — no partial state updates.
- **Duplicate request (same idempotency key):** returns result of first request without reprocessing.

---

## 6. Key open items for engineering

| # | Question | Context | Owner |
| --- | --- | --- | --- |
| 1 | Does Finflux support excess creation at tranche level? | Net new requirement. Hard dependency for Scenario 4. Pending Finflux confirmation. | Finflux / Engineering |
| 2 | Is the cancellation window configurable at product level in Finflux? | Original BRD had hard 14-day rule. Needs to be a configurable parameter. | Finflux / Engineering |
| 3 | Can obligation-level waiver be controlled per API call in Finflux? | `obligations_to_refund` parameter needs Finflux support. | Finflux / Engineering |
| 4 | How does NACH mandate interact with cancellation? | If a NACH mandate is live at cancellation, it must be deactivated. Confirm whether this is handled at Fenix layer or if Finflux needs to flag it. | Engineering / Payments |
| 5 | What is the Finflux mechanism for tranche mapping update on excess consumption? | Required to prevent stale mappings when foreclosure process consumes excess on cancelled tranche. | Finflux / Engineering |

---

## Appendix

### Cancellation vs foreclosure — obligation treatment summary

| Obligation type | Cancellation treatment | Foreclosure treatment |
| --- | --- | --- |
| Principal outstanding | Waived (merchant has settled) | Collected from borrower |
| Accrued interest | Waived — income reversal entry | Collected up to foreclosure date |
| Interest collected | Refunded via excess (configurable) | N/A |
| Principal collected | Refunded via excess (configurable) | N/A |
| Processing fee | Retained by default (configurable) | Retained (collected at origination) |
| GST on PF | Retained by default (configurable) | Retained (collected at origination) |
| Penal charges | Refunded via excess (configurable) | Collected if outstanding |
| Foreclosure charge | Not applicable | Ad hoc flat fee at tranche level |

### Cancellation scenario decision tree

| Condition | Scenario | Key action |
| --- | --- | --- |
| No obligations of any kind | Scenario 1 | Status → CANCELLED only |
| Outstanding/due exists. No accrued. No collected. | Scenario 2 | Waive outstanding. Status → CANCELLED. |
| Accrued + outstanding exist. Nothing collected. | Scenario 3 | Waive accrued (income reversal) + outstanding. Status → CANCELLED. |
| Collected obligations exist (any type) | Scenario 4 | Move collected to excess on tranche. Waive accrued + outstanding. Status → CANCELLED. |