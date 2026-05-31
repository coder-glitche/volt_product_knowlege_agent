# Product note - DRPS

: Ranjan kumar Singh
Created time: February 5, 2026 5:16 PM
Status: In progress
Last edited: February 25, 2026 11:01 AM
Owner: Lalit Bihani

## **Background and Context**

- **Who is facing the problem**
    - End customers using LAMF with multiple/single disbursals and part repayments
    - Customer support & operations teams
    - NBFC has to provide DRPS to borrower due to regulatory requirement.
- **What is the challenge today**
    - Repayment schedules are **static** and was generated at the time of Agreement sign
    - Any transaction post generation (disbursal, part payment, interest payment) makes the schedule **outdated**
    - Users rely on SOA or support teams to understand:
        - Updated interest dues
        - Final maturity amount
        - Remaining principal and cash flow expectations
- **Why this is important**
    - LAMF is a **dynamic credit line**, not a fixed EMI loan
    - Mismatch between schedule vs actual dues creates:
        - User confusion understanding the EMI
    - A real-time repayment schedule improves **transparency, self-service, and confidence**
    - **It’s a regulatory requirement to provide dynamic schedule post disbursal and repayment to borrower.**

<aside>
💡

**What is Dynamic repayment schedule (DRS/DRPS)**

**Dynamic Repayment Schedule (DRS)** is a **continuously recalculated repayment plan** that reflects the **current and actual state of a loan**, instead of a fixed, one-time schedule.

Unlike traditional EMI schedules, a DRPS is an **updated document that changes whenever the loan balance is impacted by a transaction**, ensuring alignment with actual utilisation and repayments.

*In simple terms:* 

A Dynamic Repayment Schedule shows **what borrower owe, how it is calculated, and how it changes** — based on everything that has *actually happened* on **borrowers** loan till now.

</aside>

---

## **1. Problem Scope**

### **In scope**

- Enable users to **download an updated repayment schedule(on 100% loan)** that reflects:
    - Disbursals
    - Part payments (principal / interest / charges)
    - Interest based on actual utilisation
    - Loan meta data [ROI, Credit limit, Sanction limit, Interest due, Charges due, Principal due, LAN]
    - Should reflect any change in ROI during loan tenure
- Ensure schedule is **regenerated dynamically** after every transaction
- Provide a **single source of truth** aligned with system calculations
- **Data type:** JSON and PDF
- API to generate the DRP [Download feature to enable at LSP end]

**Primary users**

- LSPs → LAMF customers

**Secondary users**

- Customer support teams
- Relationship managers / partners
- Internal ops and reconciliation teams

### **Out of scope**

- Real-time in-app visualisation (non-download view)
    
    *Rationale: Phase-1 focuses on downloadable schedule*
    
- Manual override or editing of schedule
    
    *Rationale: Schedule must remain system-derived*
    

---

## **2. Success Criteria**

**Primary outcomes**

- NBFC meet regulatory requirement
- Reduce customer confusion around dues and maturity amounts
- Enable complete self-service for repayment understanding

**Key success metrics**

- TAT for schedule generation (target: < 5 seconds)

**Post-launch good state**

- Schedule reflects **100% of transactions** till last system event
- Zero mismatch between schedule and SOA at any point in time
- High availability of API and data delivery (99.9% uptime)

**Guardrail metrics**

- No increase in EMI amount disputes
- No degradation in transaction posting TAT
- Any other API performance while creating and generating report in realtime(system slowness).

---

## **3. Solution Scope**

### **Solution Overview**

- Introduce a **Dynamic Repayment Schedule** that is regenerated **on-demand** based on the latest loan state
- The schedule recalculates cash flows after every:
    - Disbursement
    - Repayment (principal, interest)
    - Change in ROI
- Repayment schedule includes Past transactions and predictive schedules based on assumed future behaviour like interest on current outstanding and total outstanding amount.
- Show total Paid/payable at the end of the tenure [Interest + Principal]
- Output is a JSON/**PDF** aligned with system ledger and SOA

**Phasing rationale**

- Phase 1: Downloadable dynamic schedule (PDF)
- Phase 2 (future): In-app schedule view

---

### **Detailed Solution Scope**

**Supported use cases**

- User requested to downloads schedule immediately after:
    - New disbursement
    - Part payment
    - Interest posting
- Schedule reflects:
    - Facility date
    - Transaction type
    - Transaction-wise balance movement
    - Updated interest calculations
    - Total amount (Paid+predictive) at the end of the loan tenure

**Core happy path**

1. User initiates “Download Repayment Schedule”
2. System fetches latest loan ledger
3. Schedule is generated using:
    - Actual utilisation
    - Actual transaction dates
    - Current ROI
4. User receives updated PDF

**Key edge cases handled**

- Part payments on non-due dates
- Near-zero balance scenarios

**Validations**

- Allowed only when loan is Active
- And at least one disbursement is done successfully

**Operational & business impact**

- Reduced dependency on SOA explanations
- Lower call and email volumes
- Cleaner foreclosure and renewal conversations

| Description | Details |
| --- | --- |
| Trigger | User action or support request |
| Data source | Loan ledger + transaction history |
| Calculation basis | Actual utilisation & effective dates |
| Output format | JSON/PDF |
| Ownership | System-generated (read-only) |

---

## **5. High-level System / User Flow**

1. User clicks **Download Repayment Schedule**
2. Backend fetches:
    - Loan account details
    - Transaction ledger
    - Interest configuration
3. Dynamic computation engine:
    - Replays transactions chronologically
    - Calculates opening/closing balances
    - Computes interest per period
4. Schedule is rendered in standard PDF format
5. User downloads the latest version

**Error / edge handling**

- If ledger fetch fails → retry + user message
- If loan is not active → Can’t generate as loan is not active
- API timeout → Facing technical issue, retry later

## 6. Sample repayment schedule based on the scenario

### 6.1 Loan and client details:

### 6.2: Repayment schedule:

### **CASE 1: New Loan Account – No Disbursement**

### Assumptions

- Loan tenure: 6 years (72 months)
- Facility date: 01-Jan-2026
- Sanctioned amount: ₹10,00,000
- ROI: 10% floating
- No disbursement done yet

Repayment Schedule (as of 01-Jan-2026) : Throw error: Repayment schedule is not allowed to generate.

### CASE 2: Loan Aging 6 Months – Multiple Disbursements & Repayments

### Assumptions

- Facility date: 01-Jul-2025
- User downloads schedule: 01-Jan-2026
- Disbursements:
    - Jul: ₹2,00,000
    - Aug: ₹1,50,000
- Part repayment:
    - Nov: ₹50,000
- ROI: 10%

Repayment Schedule (as of 01-Jan-2026)

PAST (Actuals)

| Type | Date | Opening | Installment | Principal | Interest | Closing | ROI | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F | 01-Jul-2025 | 0 | 0 | 0 | 0 | 0 | 10% | Facility |
| D | 05-Jul-2025 | 0 | 0 | 0 | 0 | 2,00,000 | 10% | Disbursement |
| D | 10-Aug-2025 | 2,00,000 | 0 | 0 | 0 | 3,50,000 | 10% | Disbursement |
| 1 | 31-Aug-2025 | 3,50,000 | 2,900 | 0 | 2,900 | 3,50,000 | 10% | Interest |
| P | 15-Nov-2025 | 3,50,000 | 0 | 0 | 0 | 3,00,000 | 10% | Part Payment |
| 5 | 31-Dec-2025 | 3,00,000 | 2,500 | 0 | 2,500 | 3,00,000 | 10% | Interest |

FUTURE (Indicative):

| Type | Date | Opening | Installment | Principal | Interest | Closing | ROI | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 31-Jan-2026 | 3,00,000 | 2,500 | 0 | 2,500 | 3,00,000 | 10% | Projected |
| … | … | … | … | … | … | … | 10% | — |
| 72 | 30-Jun-2031 | 3,00,000 | 3,02,500 | 3,00,000 | 2,500 | 0 | 10% | Maturity |
| Total |  |  | 3,12,400 | 3,00,000 | 12,400 |  |  |  |

Installment = Principal + Interest (Actual + Indicative Interest on current Outstanding amount)

### CASE 3: Loan Aging 13 Months – ROI Changed

### Assumptions

- ROI:
    - 10% till Jul-2026
    - 11% from Aug-2026 onwards
- Outstanding principal: ₹4,00,000
- Schedule generated in Aug-2026

Repayment Schedule (as of Aug-2026)

PAST (Actuals)

| Type | Date | Opening (₹) | Installment (₹) | Principal (₹) | Interest (₹) | Closing (₹) | ROI | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D | 01-Jul-2025 | 0 | 0 | 0 | 0 | 4,00,000 | 10% | Disbursement |
| 6 | 31-Dec-2025 | 4,00,000 | 3,333 | 0 | 3,333 | 4,00,000 | 10% | Interest |
| 13 | 31-Aug-2026 | 4,00,000 | 3,667 | 0 | 3,667 | 4,00,000 | 11% | Interest |

FUTURE (Indicative):

| Type | Date | Opening (₹) | Installment (₹) | Principal (₹) | Interest (₹) | Closing (₹) | ROI | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 | 30-Sep-2026 | 4,00,000 | 3,667 | 0 | 3,667 | 4,00,000 | 11% |  |
| … | … | … | … | … | … | … | 11% |  |
| 72 | 30-Jun-2031 | 4,00,000 | 4,03,667 | 4,00,000 | 3,667 | 0 | 11% |  |
| Total |  |  | 4,33,334 | 4,00,000 | **33,334** |  |  |  |

Interest aggregated across **multiple ROI regimes**

### 6.3: Disbursement and repayment details

We need to show latest last 5 disbursement and repayment details on the document

Logic to show table: 

1. Disbursement: When Disbursement Transaction is ≥1
2. Repayment: When repayment Transaction is ≥1

**Sample data:**

Disbursement Details

| S. No | Disbursement Date | Effective ROI (%) | Disbursement Amount (₹) |
| --- | --- | --- | --- |
| 1 | 13-Oct-2025 | 10.19 | 10,000.00 |
| 2 | 17-Oct-2025 | 10.19 | 20,000.00 |
| 3 | 20-Oct-2025 | 10.19 | 15,000.00 |
| 4 | 27-Oct-2025 | 10.19 | 4,500.00 |
| 5 | 08-Dec-2025 | 10.19 | 1,000.00 |

Repayment Details (Part Payments):

| S. No | Effective Date | Description | Effective ROI (%) | Part Payment Amount (₹) |
| --- | --- | --- | --- | --- |
| 1 | 17-Nov-2025 | Part Payment | 10.19 | -1.00 |
| 2 | 02-Dec-2025 | Part Payment | 10.19 | -19,580.00 |
| 3 | 09-Dec-2025 | Part Payment | 10.19 | -1,001.00 |
| 4 | 29-Dec-2025 | Part Payment | 10.19 | -10.00 |
| 5 | 02-Jan-2026 | Part Payment | 10.19 | -30,000.00 |

## 7. Benchmarks

TCL DRPS document: 

[Repayment_Schedule_3900 (4)](Product%20note%20-%20DRPS/Repayment_Schedule_3900%20(4)%202ffe8d3af13a8193aa68c48c68b0250b.md)