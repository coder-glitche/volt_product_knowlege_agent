# Tally ERP Integration

Last Edited: March 19, 2026 9:44 PM
PRD Owner: Vaibhav Arora
Status: Completed

# **Tally Journal Voucher API Contract (Sample Document)**

This document outlines the proposed API contract for pushing journal voucher entries from the LMS/ERP system to Tally. Each journal voucher corresponds to a single **transaction event**, containing one or more **ledger-level debit/credit lines** with consolidated amounts.

---

## **1. API Overview**

### **Endpoint**

(To be shared by the vendor)

### **Purpose**

Push a complete journal voucher entry at a transaction type level to Tally for accounting purposes.

---

## **2. Request Structure (Batch Journal Posting)**

The API will support **batch posting** of journal vouchers. Each request will contain an **array of transactions**, where each object represents one complete journal voucher.

### **2.1 Journal Voucher Batch Payload**

```json
[
	{
		"transaction_type": "string",
		"narration": "string",
		"voucher_date": "YYYY-MM-DD",
		"tally_txn_id": "1234564534432",
		"ledger_entries": [
			{
				"ledger_name": "Sample1",
				"debit": "number",
				"credit": "number"
			},
			{
				"ledger_name": "Sample2",
				"debit": "number",
				"credit": "number"
			}
		]
	},
	{
		"transaction_type": "string",
		"narration": "string",
		"tally_txn_id": "1234564534433",
		"voucher_date": "YYYY-MM-DD",
		"ledger_entries": [
			{
				"ledger_name": "Sample1",
				"debit": "number",
				"credit": "number"
			},
			{
				"ledger_name": "Sample2",
				"debit": "number",
				"credit": "number"
			},
			{
				"ledger_name": "Sample3",
				"debit": "number",
				"credit": "number"
			}
		]
	}
]

```

---

### **Field Description**

| Field | Type | Description |
| --- | --- | --- |
| transaction_type | string | Preconfigured transaction type (ex: PAYIN, PAYOUT) |
| tally_txn_id | string | Unique transaction identifier used as **dedupe key** |
| voucher_date | date | Voucher posting date |
| narration | string | Narration mapped to transaction type |
| ledger_entries | array | List of debit/credit ledger lines |

---

### **Ledger Entry Object**

| Field | Type | Description |
| --- | --- | --- |
| ledger_name | string | Name of the ledger in Tally |
| debit | number | Amount debited (zero if not applicable) |
| credit | number | Amount credited (zero if not applicable) |

---

## **3. Transaction Type Samples**

Below are examples for each transaction type based on provided data.

---

## **3.1 ADD_FEE**

**Narration:** Being fee income recognition

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "ADD_FEE",
  "voucher_date": "2025-01-01",
  "narration": "Application of fee on loan account",
  "ledger_entries": [
    {"ledger_name": "Fees receivable", "debit": 7109825, "credit": 0},
    {"ledger_name": "Income from Fees", "debit": 0, "credit": 6025269},
    {"ledger_name": "CGST Payable", "debit": 0, "credit": 90382},
    {"ledger_name": "SGST Payable", "debit": 0, "credit": 90382},
    {"ledger_name": "IGST Payable", "debit": 0, "credit": 903793}
  ]
}

```

---

## **3.2 ADD_PENALTY**

**Narration:** Application of penal charges on loan account

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "ADD_PENALTY",
  "voucher_date": "2025-01-01",
  "narration": "Application of penal charges on loan account",
  "ledger_entries": [
    {"ledger_name": "Penalty receivable", "debit": 88400, "credit": 0},
    {"ledger_name": "Income from penalties", "debit": 0, "credit": 74859}
  ]
}

```

---

## **3.3 APPLY_INTEREST**

**Narration:** Application of interest on loan account

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "APPLY_INTEREST",
  "voucher_date": "2025-01-01",
  "narration": "Application of interest on loan account",
  "ledger_entries": [
    {"ledger_name": "Interest Receivable", "debit": 248279, "credit": 0},
    {"ledger_name": "Income from Interest", "debit": 0, "credit": 248279}
  ]
}

```

---

## **3.4 CHARGE_REVERSAL**

**Narration:** Reversal of charges applied on loan

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "CHARGE_REVERSAL",
  "voucher_date": "2025-01-01",
  "narration": "Reversal of charges applied on loan",
  "ledger_entries": [
    {"ledger_name": "Expense from waivers", "debit": 47695, "credit": 0},
    {"ledger_name": "Excess COA", "debit": 0, "credit": 47695}
  ]
}

```

---

## **3.5 EXCESS_PAYMENT**

**Narration:** Excess payment towards loan

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "EXCESS_PAYMENT",
  "voucher_date": "2025-01-01",
  "narration": "Excess payment towards loan",
  "ledger_entries": [
    {"ledger_name": "Excess COA", "debit": 1865304, "credit": 0},
    {"ledger_name": "Fees receivable", "debit": 0, "credit": 62679},
    {"ledger_name": "Interest Receivable", "debit": 0, "credit": 248279},
    {"ledger_name": "Loan portfolio", "debit": 0, "credit": 1554186},
    {"ledger_name": "Penalty receivable", "debit": 0, "credit": 160}
  ]
}

```

---

## **3.6 EXCESS_REFUND**

**Narration:** Excess refund to customer

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "EXCESS_REFUND",
  "voucher_date": "2025-01-01",
  "narration": "Excess refund to customer",
  "ledger_entries": [
    {"ledger_name": "Excess COA", "debit": 1820629, "credit": 0},
    {"ledger_name": "Fund Source", "debit": 0, "credit": 1820604},
    {"ledger_name": "Round off adjustment", "debit": 0, "credit": 26}
  ]
}

```

---

## **3.7 PAYIN**

**Narration:** Repayment posting on loan

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "PAYIN",
  "voucher_date": "2025-01-01",
  "narration": "Repayment posting on loan",
  "ledger_entries": [
    {"ledger_name": "Fund Source", "debit": 795459732, "credit": 0},
    {"ledger_name": "Intermittent Liability Control A/c", "debit": 29694, "credit": 0},
    {"ledger_name": "Round off adjustment", "debit": 23, "credit": 0},
    {"ledger_name": "Loan portfolio", "debit": 0, "credit": 771767140},
    {"ledger_name": "Fees receivable", "debit": 0, "credit": 6545637},
    {"ledger_name": "Interest Receivable", "debit": 0, "credit": 1510867},
    {"ledger_name": "Penalty receivable", "debit": 0, "credit": 31785},
    {"ledger_name": "Excess COA", "debit": 0, "credit": 15634019}
  ]
}

```

---

## **3.8 PAYOUT**

**Narration:** Disbursement posted on loan

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "PAYOUT",
  "voucher_date": "2025-01-01",
  "narration": "Disbursement posted on loan",
  "ledger_entries": [
    {"ledger_name": "Loan portfolio", "debit": 1513975349, "credit": 0},
    {"ledger_name": "Fund Source", "debit": 0, "credit": 1513975349}
  ]
}

```

---

## **3.9 RETURN**

**Narration:** Disbursement return due to failure

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "RETURN",
  "voucher_date": "2025-01-01",
  "narration": "Disbursement return due to failure",
  "ledger_entries": [
    {"ledger_name": "Fund Source", "debit": 4047959, "credit": 0},
    {"ledger_name": "Loan portfolio", "debit": 0, "credit": 4047959}
  ]
}

```

---

## **3.10 UNDO_EXCESS_PAYMENT**

**Narration:** "Excess payment reversal on loan

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "UNDO_EXCESS_PAYMENT",
  "voucher_date": "2025-01-01",
  "narration": "Excess payment reversal on loan",
  "ledger_entries": [
    {"ledger_name": "Fees receivable", "debit": 44939, "credit": 0},
    {"ledger_name": "Loan portfolio", "debit": 1150, "credit": 0},
    {"ledger_name": "Penalty receivable", "debit": 120, "credit": 0},
    {"ledger_name": "Excess COA", "debit": 0, "credit": 46209}
  ]
}

```

---

## **3.11 UNDO_PAYIN**

**Narration:** Being reversal of repayment received

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "UNDO_PAYIN",
  "voucher_date": "2025-01-01",
  "narration": "Being reversal of repayment received",
  "ledger_entries": [
    {"ledger_name": "Excess COA", "debit": 11609885, "credit": 0},
    {"ledger_name": "Fees receivable", "debit": 49828, "credit": 0},
    {"ledger_name": "Interest Receivable", "debit": 37367, "credit": 0},
    {"ledger_name": "Loan portfolio", "debit": 28391470, "credit": 0},
    {"ledger_name": "Penalty receivable", "debit": 4500, "credit": 0},
    {"ledger_name": "Fund Source", "debit": 0, "credit": 40093051}
  ]
}

```

---

## **3.12 WAIVE_FEE**

**Narration:** Being Fees reversed

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "WAIVE_FEE",
  "voucher_date": "2025-01-01",
  "narration": "Being Fees reversed",
  "ledger_entries": [
    {"ledger_name": "CGST Payable", "debit": 5, "credit": 0},
    {"ledger_name": "SGST Payable", "debit": 5, "credit": 0},
    {"ledger_name": "IGST Payable", "debit": 41, "credit": 0},
    {"ledger_name": "Income from Fees", "debit": 278, "credit": 0},
    {"ledger_name": "Fees receivable", "debit": 0, "credit": 329}
  ]
}

```

---

## **3.13 WAIVE_PENALTY**

**Narration:** Being penalty reversed

```json
{
  "tally_txn_id": "<unique-id>",
  "transaction_type": "WAIVE_PENALTY",
  "voucher_date": "2025-01-01",
  "narration": "Being penalty reversed",
  "ledger_entries": [
    {"ledger_name": "CGST Payable", "debit": 345, "credit": 0},
    {"ledger_name": "SGST Payable", "debit": 345, "credit": 0},
    {"ledger_name": "IGST Payable", "debit": 3143, "credit": 0},
    {"ledger_name": "Income from penalties", "debit": 21230, "credit": 0},
    {"ledger_name": "Penalty receivable", "debit": 0, "credit": 25062}
  ]
}

```

---

## **3.14 Term Loan (TL) – Additional Transaction Coverage**

In addition to the transaction types listed above (which are applicable across OD lines and loans), the following **Term Loan–specific accounting events** are supported. These transactions are **accounted strictly at a loan level** and will always carry a valid **Loan Account ID / Term Loan Account Number**.

**Scope of TL-specific transactions:**

- Loan repayments mapped to repayment schedules
- Loan part payments (principal-only or mixed allocations)
- Loan foreclosure payments (full and partial)
- Disbursements (initial and subsequent tranches)
- Charge posting against disbursement (e.g., processing fees)
- Interest accrual (only at a loan level)

**Mapping to transaction types (TL-specific):**

- Loan repayments / part payments → `REPAYMENT` *(New transaction type)*
- Loan foreclosure payments → `FORECLOSURE_PAYMENT` *(New transaction type)*
- Disbursements → `EMI_CONVERSION` *(New transaction type)*
- Disbursement returns / reversals → *Not applicable for Term Loans*
- Interest accrual → `INTEREST_ACCRUAL` *(New transaction type)*
- Processing fee posting → `ADD_FEE`

**Key characteristics:**

- All TL transactions are posted as **single journal vouchers per transaction event**.
- Debit–credit equality is enforced at the transaction level.
- `tally_txn_id` remains the idempotency key for upsert behaviour.
- TL transactions will never be mixed with line-level dues or excess creation logic.

---

## **4. Response Structure**

```json
{
  "status": "SUCCESS/FAILED",
  "voucher_number": "string",
  "timestamp": "ISO8601",
  "message": "string"
}

```

---

## **5. Error Codes**

| Code | Description |
| --- | --- |
| ERR_LEDGER_NOT_FOUND | Ledger name does not exist in Tally |
| ERR_INVALID_AMOUNT | Debit/Credit not balanced |
| ERR_DUPLICATE_TXN | Transaction ID already exists |
| ERR_INTERNAL | Generic processing error |

---

## **6. Notes for Tally Team**

- All amounts are consolidated at the **transaction level**.
- Debit and Credit totals will always match before sending.
- Ledger names will exactly match Tally masters.
- Narration should appear at voucher header.

---

## **7. Response Structure (Batch Aware)**

The API response will return **transaction-level status**, complete request echo, and ledger-level posting status.

```json
{
  "status": "SUCCESS/PARTIAL_SUCCESS/FAILED",
  "timestamp": "ISO8601",
  "results": [
    {
      "tally_txn_id": "string",
      "operation": "INSERT/ALTER",
      "voucher_number": "string",
      "status": "SUCCESS/FAILED",
      "message": "string",
      "request_echo": { },
      "ledger_status": [
        {
          "ledger_name": "string",
          "posted": true,
          "message": "string"
        }
      ]
    }
  ]
}

```

---

## **8. Validations (System-Level and Tally-Level)**

### **8.1 Debit–Credit Validation (Mandatory)**

- For each transaction object, sum of **debit** amounts must equal sum of **credit** amounts.
- Validation is performed **per transaction**, not across the batch.
- Error code: `ERR_DEBIT_CREDIT_MISMATCH`.

### **8.2 Voucher Name Validation**

- Voucher type must be preconfigured in Tally and mapped to transaction type.
- Invalid mapping → `ERR_INVALID_VOUCHER_TYPE`.

### **8.3 Transaction Type Validation**

- Only preconfigured transaction types are allowed.
- Narration is **derived from transaction type** and validated against PRD definitions.
- Error code: `ERR_INVALID_TRANSACTION_TYPE`.

### **8.4 Ledger Validation**

- All ledger names must exist and be active in Tally.
- Missing/inactive ledger → `ERR_LEDGER_NOT_FOUND`.

### **8.5 Transaction ID (Dedupe & Upsert Logic)**

- `tally_txn_id` acts as the **idempotency key**.
- If `tally_txn_id` is **new** → journal voucher is **inserted**.
- If `tally_txn_id` already exists → voucher is **altered/updated**.
- Alter operation will overwrite ledger lines for the transaction.
- Error during alter → `ERR_UPDATE_FAILED`.

### **8.6 Amount Validation**

- Amount must be numeric and non-negative.
- Max two decimal precision allowed.
- Error code: `ERR_INVALID_AMOUNT`.

### **8.7 Mandatory Fields Validation**

Required per transaction:

- `tally_txn_id`
- `transaction_type`
- `voucher_date`
- `narration`
- `ledger_entries` (minimum two lines)

Missing fields → `ERR_MISSING_FIELD`.

---

## **9. Ledger-Level Posting Status**

Tally should return posting status for each ledger line item:

- `posted: true/false`
- Failure message if not posted (ex: ledger disabled, mismatch in group, inactive, etc.)

---

## **10. Manual Journal Vouchers (MANUAL_JV)**

In addition to system-generated transaction types, the API will support **manual JVs**, which will allow finance teams to post one-off accounting adjustments directly via the API.

### **Purpose**

Manual JVs are used for exceptional or ad-hoc accounting entries that are not tied to a predefined transaction workflow in the system.

### **Transaction Type**

`MANUAL_JV`

### **Rules & Behaviour**

- **Not system-generated** — entries are created manually by finance/operations.
- **Flexible ledger mapping** — any valid Tally ledger can be used.
- **Mandatory Debit–Credit equality** — same validation rules as other JVs apply.
- **Narration is mandatory** and should clearly explain the adjustment.
- **Audit requirement** — system will store creator, timestamp, and reason for the manual JV.
- **Voucher type** — must be mapped to a preconfigured Journal Voucher type in Tally.

### **Recommended Use Cases**

- Rounding adjustments beyond automated thresholds
- Exceptional ledger corrections (e.g., reclassifications)
- Journal entries required during monthly closing

---

End of document.