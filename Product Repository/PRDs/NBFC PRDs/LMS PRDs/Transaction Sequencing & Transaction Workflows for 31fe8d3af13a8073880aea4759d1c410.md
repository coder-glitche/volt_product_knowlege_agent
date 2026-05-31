# Transaction Sequencing & Transaction Workflows for Co-Lending LMS

Last Edited: March 19, 2026 9:44 PM
PRD ETA: March 10, 2026
PRD Owner: Vaibhav Arora
Status: Completed

# Background and Context

DSP Finance is implementing a **co-lending structure between DSP and TCL** where a single customer loan is operationally represented by **three loan accounts inside the LMS**.

The loan accounts are structured as follows:

- **Loan 100** → Customer facing orchestration loan (Finflux)
- **Loan 90** → TCL lender loan (Swiffy LMS)
- **Loan 10** → DSP lender loan (Finflux)

All **customer-facing interactions and repayments occur on Loan 100**, while lender accounting and settlement must be reflected in the **individual lender loan books**.

This PRD introduces the need for **systematic orchestration across multiple loan books** to ensure:

- lender accounting reconciliation
- schedule consistency
- correct split of repayments
- ransaction ordering
- correct DP (Drawing Power) management

---

### Transaction Categories

The system processes two categories of transactions.

---

## Money Transactions

These impact loan balances or receivables.

Examples:

- Disbursement
- Repayment
- Refund / Disbursement reversal
- Charge application
- Charge knock off
- Interest posting
- Credit note adjustments
- Waivers
- Excess payment handling
- Excess refunds
- Clear dues transactions

---

## Collateral Transactions

These impact collateral and **DP calculations**.

Examples:

- Add collateral
- Remove collateral
- Sell-off collateral

Collateral operations may also **trigger money transactions**, such as:

- Margin pledge charges
- Invocation charges
- Repayment from sell-off proceeds

---

# Current Challenge

The LMS currently processes transactions **independently per loan account** without orchestration across lender books.

This introduces several operational risks in a co-lending structure.

---

## 1. Transaction Ordering Risk

Example sequence:

Repayment → Interest posting → Charge posting

If these are processed **in different orders across lender loan books**, the share calculations become inconsistent.

---

## 2. Money Flow vs Accounting Mismatch

Customer funds move through **escrow accounts**, while lender receivables are maintained in the LMS.

Without deterministic orchestration:

- escrow balances may move
- lender books may not reconcile

---

## 3. Collateral and Money Transaction Race Conditions

Example:

Sell-off collateral and repayment arriving simultaneously.

This may result in:

- incorrect DP recalculation
- incorrect sell-off triggers
- incorrect available limit.

---

## 4. Partial Transaction Failures

Example:

Loan 100 disbursement succeeds but lender loan posting fails.

This creates **partial system states** that break reconciliation.

---

# Why Solving This Is Important

Without proper transaction orchestration:

- lender reconciliation will break
- interest and charge split logic will drift
- DP calculations may become inconsistent
- operational errors may cascade

Given the scale of **automated repayment flows and disbursements**, these errors can create **systemic accounting breaks**.

A **transaction orchestration framework** is therefore required.

---

# 1. Problem Scope

---

## In Scope

This document defines the **transaction orchestration logic across all supported transaction types**.

Specifically it covers:

### Transaction orchestration across loan books

Transactions must always execute in the following order:

```
Loan 100 → Loan 90 → Loan 10
```

---

### Transaction sequencing

All money and collateral transactions will be processed via a **LAN-level transaction queue**.

This ensures:

- no race conditions
- deterministic execution
- reconciliation integrity.

---

### Multi-loan transaction state management

Each transaction will maintain states across:

- Loan 100
- Loan 90
- Loan 10

---

### Failure handling

Define system behavior when:

- lender loan posting fails
- escrow confirmation delays
- reconciliation mismatches occur.

---

## Out of Scope

### Loan contract share logic

Principal and schedule share ratios are defined in a **separate split logic document**.

---

### Escrow settlement reconciliation

Daily lender settlement processes will be covered in the **Finance Reconciliation PRD**.

---

### Collateral valuation and DP calculations

These are handled by the **CRMS module**.

---

# 2. Success Criteria

---

## Deterministic Transaction Execution

For every transaction:

```
Loan 100 → Loan 90 → Loan 10
```

must execute in strict order.

---

## No Reconciliation Breaks

Success state requires:

- lender loan balances reconcile with customer loan
- escrow balances reconcile with lender payables
- schedule mappings remain consistent.

---

## Minimal Customer Impact

Customer operations such as:

- repayments
- disbursements
- collateral actions

must remain **available while lender postings occur asynchronously**.

---

## Guardrail Metrics

The following metrics must not degrade:

- repayment posting latency
- disbursement approval TAT
- DP calculation accuracy.

---

# 3. Solution Overview

A **transaction orchestration layer (CLMS)** will manage transaction execution across all loan books.

Key principles:

1. All transaction requests (**money + collateral**) are accepted asynchronously
2. Transactions are queued at **LAN level**
3. Execution happens sequentially
4. Each transaction maintains a **state machine**

---

# 4. Transaction Queue

All transaction requests will be stored in a **LAN level queue**.

Example:

```
LAN 123

1 Disbursement
2 Add collateral
3 Repayment
4 Interest posting
```

Transactions are processed sequentially.

---

## Transaction States

Each transaction moves through the following states.

```
REQUEST_RECEIVED
↓
LOAN_100_PROCESSING
↓
LOAN_100_COMPLETE
↓
LOAN_90_PROCESSING
↓
LOAN_90_COMPLETE
↓
LOAN_10_PROCESSING
↓
LOAN_10_COMPLETE
↓
TRANSACTION_COMPLETE
```

If any stage fails:

```
TRANSACTION_FAILED
```

Retries or manual reconciliation will be triggered.

---

# 5. Transaction Workflows

---

# 5.1 Disbursement

## Request Flow

1. User raises disbursement request via LSP up to available limit.
2. Available limit derived from:

```
Available limit = DP − POS
```

Excess does not contribute to available limit.

1. LSP calls lender disbursement API.
2. Loan 100 creates disbursement request.
3. Finflux **approval-based disbursement API** triggered.
4. DP is blocked.
5. Cashfree payout initiated.
6. System waits for credit confirmation.

Once credit succeeds:

- disbursement approved
- charge knock-offs executed.

---

## Transaction Flow

```
Loan 100 disbursement
↓
Loan 90 posting
↓
Loan 10 posting
```

Charges knocked off from disbursement proceeds.

---

## Money Flow

```
Escrow → Customer payout
```

Lender shares reconciled during EOD settlement.

---

# 5.2 Repayment

## Request Flow

Repayment can occur via:

- payment gateway
- virtual account
- NACH mandate
- sell-off proceeds

Loan 100 processes the repayment.

Two data sets are extracted:

### Repayment metadata

Contains:

- principal settled
- excess created
- interest settled
- fees and penalty settled

### Schedule derived data

Contains obligation-level settlement (Charge level or monthly interest level):

- interest
- penalty
- fees.

---

## Validation

Schedules across loan books must satisfy:

Interest:

```
Loan 100 interest = Loan 10 + Loan 90
```

Charges:

```
Loan 100 charges = Loan 10 * sharing split + Loan 90 * sharing split (0)

Loan 100 charges = Loan 10 charges
```

Principal:

```
Loan 100 principal = Loan 10 + Loan 90
```

If validation fails:

- repayment queue pauses (In CLMS)
- Tech Ops investigates.

---

## Transaction Flow

```
Loan 100 repayment
↓
Loan 90 repayment posting
↓
Loan 10 repayment posting
```

Split logic follows contract configuration (A version of contract should be stored at a LAN level post origination) and that should be the source of truth for that LAN.

---

## Money Flow

```
Customer → Repayment escrow
```

Settlement:

```
Escrow → TCL
Escrow → DSP
```

---

# 5.3 Charge Application

Charges exist only for DSP exposure.

---

## Transaction Flow

```
Charge applied in Loan 100
↓
Charge replicated in Loan 10
```

TCL loan does not carry charges.

The penalty job will not run in Loan 10. (Loan 100 will have the Finflux penalty job active.) Instead, a **daily cron** replicates penalties in Loan 10.

(Loan 10 applicable charges) - Penalty 

(Evaluate if we can move the penalty job to Fenix)

---

# 5.4 Charge Knock Off

Charge knock-off occurs during disbursement.

Only DSP charges exist.

---

## Transaction Flow

```
Loan 100 knock-off
↓
Loan 10 knock-off replication
```

Each charge is associated with the **disbursement ID**.

---

# 5.5 Excess Handling

Excess will only exist in **Loan 100**.

---

## Behaviour Change

Current formula:

```
Available limit = DP − POS + Excess
```

New formula:

```
Available limit = DP − POS
```

Excess will be parked.

(We need to test the configuration on Finflux)

---

## Excess Refund

Daily job triggers refunds:

```
Excess detected
↓
Refund initiated
↓
Customer receives refund
```

Exact retention rules defined in **Excess Refund PRD**.

---

# 5.6 Interest Posting

Interest posted independently in all LMS systems.

Systems:

- Loan 100 (Finflux)
- Loan 10 (Finflux)
- Loan 90 (TCL Swiffy)

---

## Monthly Sync Window

```
6PM (T) – 10 AM (T+1) (Non business hours for all three loans)
```

Interest reconciliation job runs.

---

### Scenario 1

Loan 100 interest equals lender interest.

No action required.

---

### Scenario 2

Loan 100 interest greater.

Waiver applied in Loan 100.

---

### Scenario 3

Loan 100 interest lower.

Waiver applied in Loan 10.

---

# 5.7 Excess Payment

Excess payments are not generated automatically.

They must be orchestrated manually.

Example:

- foreclosure using excess.

Transaction processed as repayment with separate accounting.

---

# 5.8 Clear Dues

Clear dues API posts accrued interest and settles it using excess.

Validation:

```
Loan 100 dues
=
Loan 10 dues + Loan 90 dues
```

---

# 5.9 Credit Notes

Two types exist.

### Charge refund credit note

Refund posted as liability for DSP.

---

### Interest refund credit note

Interest refund must also be reflected in TCL system.

---

# 5.10 Add Collateral

Collateral added across all loans.

```
Loan 100
↓
Loan 90
↓
Loan 10
```

Margin pledge charges may apply.

---

# 5.11 Remove Collateral

Collateral removal reduces DP.

Transaction must be sequenced with money transactions.

---

# 5.12 Sell-Off Collateral

Sell-off creates repayment flows.

Instead of backdated posting:

```
Forward dated repayment posting
```

Snapshots stored:

```
POS before repayment
POS after repayment
```

Used to compute interest benefit.

Credit note issued for adjustment. 

(Cosolidation) - of sell off repayment

---

# 5.13 Waivers

Two waiver types exist.

---

## Interest Waiver

Requires TCL API.

Validation:

```
Loan 100 interest outstanding
=
Loan 10 + Loan 90
```

---

## Charge Waiver

Charge waivers only affect:

```
Loan 100
Loan 10
```

---

# 6. Key Dependencies

| Dependency | Description |
| --- | --- |
| Available limit API | Limit propagation to LSP |
| Cashfree payout | Escrow disbursement |
| Finflux approval disbursement | DP blocking |
| TCL schedule API | Repayment validation |
| Interest waiver API | Disbursement reversal |
| Collateral APIs | DP updates |

---

# 7. Pending Decisions

| Topic | Decision Needed |
| --- | --- |
| Limit propagation to LSP | Real-time vs periodic sync |
| Partial return handling | TCL capability |
| Charge knock-off timing | Before/after disbursement |
| Sell-off sequencing | Repayment timing |