# Product Note – DRPS (Final Version – Unified Format)

: Vaibhav Arora
Created time: February 25, 2026 11:26 AM
Status: Ready for Tech
Last edited: April 22, 2026 7:17 PM

# 1. Background & Context

## Who is facing the problem

- End customers using LAMF (Credit Line / LAS)
- Customer support & operations teams
- NBFC (regulatory requirement to provide updated repayment schedule)

---

## What is the challenge today

- Static schedules become outdated after:
    - Disbursement
    - Part repayment
    - ROI change
    - Charge application
- Users depend on SOA to understand updated dues.
- No single structured month-wise forward view aligned with current POS.

---

## Why this is important

LAMF is a **dynamic demand loan**, not a fixed EMI loan.

A Dynamic Repayment Schedule must:

- Reflect actual utilisation
- Reflect historical interest accrual
- Provide predictive view till closure
- Be aligned with system ledger
- Be audit-reconcilable

---

# 2. Problem Definition

DRPS must:

1. Reflect actual historical data till generation timestamp.
2. Reflect projected dues till closure date.
3. Be aligned to:
    - Current POS
    - Current ROI
    - Closure date (currentTermEndDate)
4. Include non-contingent charges prospectively.
5. Use a **single continuous table format**.

---

# 3. Solution Scope

## In Scope

- Credit Line products only
- Monthly frequency
- Single unified schedule table
- JSON + PDF output

Term Loans are out of scope.

---

# 4. DRPS Structure

There will be **one unified repayment schedule table**.

Older rows = system-derived actuals.

Future rows = system-computed projections.

The format remains identical for all rows.

---

# 5. Repayment Schedule Columns (Final – As Per New Requirement)

| Column | Description |
| --- | --- |
| Repayment Date | Month-end date (7th of next month for due logic; last row = closure date if mid-month) |
| Outstanding principal (Opening) | Principal outstanding at start of period |
| Principal payable/Prepayment | Principal component (only non-zero in closure row unless repayment exists historically) |
| Outstanding principal (Closing) | Opening − Principal (interest does not reduce principal) |
| Instalment | Interest + Charges

(Last instalment principal will be included in instalment) |
| Interest payable/Paid | Interest for that period (actual for past, computed for future)

Middle of the month accrued interest for interest until now + calculate future interest based on current ROI |
| Charges payable/Paid | Retro charges for past; Non-contingent charges for future

(AMC charge) |

No instalment type column.

---

# 6. Data Logic

## 6.1 Historical Rows (Actuals)

Source:

- Finflux schedule details API
- Transaction ledger

Rules:

- Chronological replay of transactions
- Opening & closing balances must reconcile with system ledger
- ROI per period must reflect actual rate applicable
- All actual charges shown
- Installment = actual principal + interest + charges posted

---

## 6.2 Future Rows (Forecasted)

Computation Basis:

- Current POS
- Current ROI
- Remaining tenure till closure
- No further disbursement assumed
- No further repayment assumed

Interest Calculation:

- Daily accrual
- 365-day year
- Actual days between repayment dates

Charges:

- Only non-contingent charges
- Applied based on stored applicability schedule

Principal:

- Zero for all future months except final row

Final Row:

- Principal = full remaining POS
- Interest = interest for last partial period
- Charges = applicable
- Closing balance = 0
- Date (Loan term end date)

---

# 7. Charges Handling

## Historical (Retro)

- All actual charges reflected from ledger.

## Future (Non-Contingent Only)

Included if predefined:

- AMC
- Platform fee
- Recurring predefined charges

Excluded:

- Bounce charges
- Penal interest
- Event-driven charges

Enhancement:

Loan account must store:

- Charge type
- Frequency
- Applicability start date
- Charge amount logic

DRPS will derive future charge rows using this metadata.

---

# 8. Interest Logic

- Daily accrual basis
- 365-day year
- Period = previous repayment date to current repayment date
- ROI change historically must be reflected in older rows
- Future assumes current ROI constant

Disclaimer:

> Future values assume no further utilisation, repayment, or rate change.
> 

---

# 9. Edge Case Handling

| Scenario | Behaviour |
| --- | --- |
| Loan inactive | Error |
| No disbursement | Error |
| POS = 0 | Generate single closure row |
| Today > closure date | Show closed schedule summary |
| ROI changed historically | Reflect in older rows only |
| Mid-month closure | Final row = closure date |

---

# 10. Rounding Logic

- Computation at high precision
- Each row rounded to 2 decimals (Rounded Up)
- Final row reconciliation:

```
Final Installment =
Total Outstanding − Sum(previous projected installments)
```

Ensures mathematical closure.

---

# 11. Summary Section (Header)

Fields:

- Generated On
- Customer Name
- Loan Account Number
- Sanctioned Limit
- Credit Limit
- Currency
- APR
- Rate of Interest (Current)
- Interest Type (Floating)
- Loan Maturity Date
- Loan Status
- Principal Outstanding
- Charges Outstanding
- Total Outstanding

---

# 12. Disbursement & Repayment Details Section

Below schedule:

Show last 5:

### Disbursement Table

- Date
- Effective ROI
- Amount

### Repayment Table

- Date
- Effective ROI
- Amount

Shown only if count ≥ 1.

---

# 13. Regulatory Alignment

DRPS must:

- Be system-generated and read-only
- Align with SOA and ledger
- Reflect all historical transactions
- Include non-contingent charges prospectively
- Clearly indicate predictive rows are indicative
- Not expose internal allocation logic

---

# 14. API & Output

Endpoint:

```
GET /transactions/report-data/{fenixLoanAccountId}
```

Response:

`CreditLineReportDataResponse`

Embedded:

`monthEndRepaymentSchedule`

Formats:

- JSON
- PDF

TAT target: < 5 seconds