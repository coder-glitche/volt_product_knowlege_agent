# Analytics requirement for amortisation of PF

Last Edited: April 24, 2026 8:59 AM
PRD ETA: April 24, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

# **1. Objective**

Generate month-level amortised accounting entries for Processing Fee (PF) income against loan accounts across LAMF, LAS, and Term Loan product lines. The report will be consumed by the Finance team and downloaded on-demand from the Finflux analytics module.

The design must be extensible to accommodate other fee/cost types in future iterations without structural rework.

# **2. Scope & Exclusions**

## **2.1 In Scope**

- Product lines: LAMF, LAS, Term Loan (TL)
- Charge type: Processing Fee (PF)
- Accounting entries: Income recognition at monthly amortisation level
- Amortisation method: Straight Line Method (SLM)
- Report period: M-N (N>0) (previous calendar months only)
- Waiver handling: Partial and complete waivers with corresponding reverse entries
- Loan closure handling: Remaining balance acceleration on closure date

## **2.2 Explicitly Out of Scope**

- GST component of processing fee excluded from amortisation entries
- Current month entries - report is strictly retrospective
- Real-time or intra-month amortisation schedules

# **3. Source Data & Key Fields**

All data will be sourced from the accounting report. The following fields are required at a schedule/charge level:

| **Field** | **Source / Table** | **Notes** |
| --- | --- | --- |
| FXLAN / Term Loan Account No. | LMS – Loan Master | External loan identifier |
| Client External ID | LMS – Loan Master | FXCID reference |
| Product Type | LMS – Loan Master | LAMF / LAS / TL |
| Charge Application Date | LMS – Fee Schedule | Date PF was applied |
| PF Income Amount | LMS – Fee Schedule | Excludes GST; 'Income from Fees' leg only |
| Transaction ID (Fees) | LMS – Transaction Log | Original fee transaction reference |
| Loan Status | LMS – Loan Master | Active / Closed |
| Closure Date | LMS – Loan Master | Populated only if loan is closed |
| Loan Tenure (Original) | LMS – Loan Master | In days, for SLM denominator |
| Waiver Amount | LMS – Waiver Log | Partial or full waiver on fee |
| Waiver Date | LMS – Waiver Log | Date waiver was applied |
| Waiver Type | LMS – Waiver Log | Partial / Complete |

# **4. Amortisation Logic – Straight Line Method**

## **4.1 Daily Amortisation Rate**

Daily Amortisation = PF Income Amount ÷ Original Tenure (in days)

The denominator uses the original loan tenure in calendar days from disbursement date to scheduled maturity date. Tenure is not re-computed on closure.

## **4.2 Processing Fee Income Amount (Effective)**

Only the income leg of the PF accounting entry is considered, i.e., the 'Income from Fees' credit entry. The IGST Payable and Fees Receivable legs are excluded.

Example from sample entry: PF Income = ₹9,990 (the credit to Income from Fees). The ₹179.82 IGST leg is excluded.

## **4.3 Scenario-Based Amortisation Rules**

| **#** | **Scenario** | **Condition** | **Amortisation Treatment** |
| --- | --- | --- | --- |
| 1 | Charge in current month; loan open at EOM | charge_date in [M-1 start, M-1 end] AND loan active | Generate daily SLM entries from charge_date to EOM (M-1). Total = Daily Rate × days from charge date to EOM. |
| 2 | Charge in prior month; loan open through full M-1 | charge_date < M-1 start AND loan active | Generate one entry for the full month. Amount = Daily Rate × number of days in M-1. |
| 3 | Charge in current month; loan closed within M-1 | charge_date in M-1 AND closure_date in M-1 | Generate daily entries from charge_date to closure_date. On closure_date, remaining unamortised balance (PF - amortised to date) is fully recognized as a single accelerated entry. |
| 4 | Charge in prior month; loan closed within M-1 | charge_date < M-1 start AND closure_date in M-1 | Generate daily SLM entries from M-1 start to (closure_date - 1). On closure_date, recognize full remaining unamortised balance (including any unrecognized from prior months) as a single accelerated entry. |

# **5. Accounting Entry Structure**

## **5.1 Standard Monthly Amortisation Entry**

For each amortisation date, generate the following journal entry:

| **Ledger Account** | **Debit** | **Credit** | **Entry Type** |
| --- | --- | --- | --- |
| Amortised Fees Receivable | Amortised Amount | — | Standard |
| Amortised Income from Fees | — | Amortised Amount | Standard |

Each row in the report output maps to one accounting entry date. Daily granularity is required for Scenarios 1, 3, and 4.

## **5.2 Accelerated Closure Entry (Scenarios 3 & 4)**

On the loan closure date, an additional entry is generated for the remaining unamortised balance:

| **Ledger Account** | **Debit** | **Credit** | **Entry Type** |
| --- | --- | --- | --- |
| Amortised Fees Receivable | Remaining Balance | — | Accelerated |
| Amortised Income from Fees | — | Remaining Balance | Accelerated |

Remaining Balance = Total PF Income − Sum of all previously amortised amounts (including any months prior to M-1).

# **6. Waiver Handling**

## **6.1 Waiver Proportionality**

Since the PF amount is inclusive of 18% GST, the effective income component for any waiver is:

**Effective Income Waived = Waiver Amount ÷ 1.18**

Only this income-equivalent portion is reversed in the amortisation ledger. The GST portion is handled separately by Finance and is not part of this report.

## **6.2 Partial Waiver**

On the waiver date, generate a reverse (debit) entry in the Amortised Income from Fees account for the effective income waived:

| **Ledger Account** | **Debit** | **Credit** | **Entry Type** |
| --- | --- | --- | --- |
| Amortised Income from Fees | Effective Income Waived | — | Partial Waiver Reversal |
| Fees Receivable | — | Effective Income Waived | Partial Waiver Reversal |

The remaining (post-waiver) PF income becomes the new base for future SLM amortisation from the waiver date onward.

## **6.3 Complete Waiver**

A full waiver reverses the entire remaining unamortised income balance as a single entry on the waiver date:

| **Ledger Account** | **Debit** | **Credit** | **Entry Type** |
| --- | --- | --- | --- |
| Amortised Income from Fees | Full Remaining Balance | — | Full Waiver Reversal |
| Fees Receivable | — | Full Remaining Balance | Full Waiver Reversal |

No further amortisation entries should be generated for this LAN after a complete waiver.

# **7. Report Output Specification**

## **7.1 Output Columns**

| **#** | **Column Name** | **Description** | **Example** |
| --- | --- | --- | --- |
| 1 | loan_account_number | FXLAN or Term Loan account number | FXLAN16472899 |
| 2 | client_external_id | Client reference (FXCID) | FXCID42126519 |
| 3 | product_type | LAMF / LAS / TL | LAS |
| 4 | fee_transaction_id | Transaction ID of the original PF application | 0002e84d-0d1a-456f-... |
| 5 | charge_application_date | Date the PF was applied on the loan | 2025-06-25 |
| 6 | pf_income_amount | Total PF income (excl. GST) | 9990.00 |
| 7 | amortisation_date | Date of the individual amortisation entry | 2025-06-25 |
| 8 | amortised_amount | Amount recognised on this date (SLM or accelerated) | 333.00 |
| 9 | entry_type | Standard / Accelerated / Partial Waiver / Full Waiver | Standard |
| 10 | debit_account | Debit leg account name | Fees Receivable |
| 11 | credit_account | Credit leg account name | Amortised Income from Fees |
| 12 | debit_amount | Amount in debit column | 333.00 |
| 13 | credit_amount | Amount in credit column | 333.00 |
| 14 | report_month | M-1 month this entry belongs to (YYYY-MM) | 2025-06 |
| 15 | loan_closure_date | Date of closure if applicable, else blank | — |
| 16 | scenario_flag | Which scenario applies (1/2/3/4) | 1 |
| 17 | unamortised_balance | Remaining balance after this entry | 9657.00 |
| 18 | waiver_amount | If a waiver applies on this date, else blank | — |
| 19 | office | Booking office (e.g., Head Office) | Head Office |

## **7.2 Delivery**

- Available as a downloadable CSV/XLS report in the Finflux Analytics module
- Finance team can trigger download on-demand for any prior calendar month and year combination
- Report will not be generated for current month or future months
- One row per amortisation entry date per LAN

# **8. Extensibility Note**

The report schema is designed to accommodate additional charge types (e.g., Documentation Fee, Insurance Premium) in future phases. The following fields will remain generic:

- charge_type (currently hardcoded to 'Processing Fee')
- pf_income_amount can be renamed to charge_income_amount
- fee_transaction_id can reference any charge transaction

When extending to new charge types, only data sourcing and charge identification logic needs to change; the amortisation, entry generation, and waiver logic remains identical.

# **9. Validation & Controls**

- Sum of all amortised_amount entries for a LAN must equal pf_income_amount (net of waivers)
- No amortisation entries should be dated beyond closure_date or EOM of M-1
- Unamortised balance must never be negative
- No duplicate entries for the same (LAN, amortisation_date, entry_type)
- Waiver reversal amount must not exceed current unamortised_balance

# **10. Open Questions / Assumptions**

| **#** | **Question / Assumption** | **Owner** | **Status** |
| --- | --- | --- | --- |
| 1 | Original tenure is defined as disbursement date to scheduled maturity date in calendar days. Confirm with Finance. | Finance | Open |
| 2 | For partial waiver, the new SLM base is (pf_income_amount - effective_income_waived) from waiver date onward. Confirm. | Finance | Open |
| 3 | Fees Receivable account exists as a debit account in the GL. Confirm account code. | Finance | Open |
| 4 | Can multiple waivers occur on the same LAN within the same month? If yes, each is treated independently. | Product | Assumed Yes |
| 5 | Is the report output expected to be grouped by office/branch in addition to LAN? | Finance | Open |