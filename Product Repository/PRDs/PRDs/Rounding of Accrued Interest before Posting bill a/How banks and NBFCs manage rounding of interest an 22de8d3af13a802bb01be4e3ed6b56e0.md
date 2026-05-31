# How banks and NBFCs manage rounding of interest and charges, and how they handle accounting in these cases.

## **1. Regulatory & Industry Context**

### RBI Guidelines:

RBI doesn’t dictate **how to round**, but it **expects fairness, transparency, and precision** in:

- Customer charging
- Auto-debit recovery
- Tax invoicing
- Reconciliation of ledgers

So, banks and NBFCs need to:

- Ensure **customers aren’t overcharged**
- Match debits with invoices/statements
- Maintain proper **audit trail** and **variance accounting** if rounding is applied

---

## 2. Rounding Methods Used by Banks & NBFCs

| Type | Common Use Case | Real-world Examples |
| --- | --- | --- |
| **No Rounding (Post exact value)** | Charges with GST, floating interest | HDFC Bank, Axis Bank, Bajaj Finance (on fees), most NBFCs |
| **Round to Nearest Rupee** | Interest on EMI loans, penal charges | SBI, ICICI Bank, Fullerton |
| **Round Up (Conservative)** | Micro loans, prepaid cards | Some gold loan NBFCs |
| **Cumulative Rounding** | Long tenure loans | Used in housing finance |

---

## 3. Detailed Accounting Treatment by Banks/NBFCs

### **A. Exact Posting (No Rounding)**

### Use Case:

- Processing fees + GST
- Penal charges

### System Flow:

1. Fee computed: ₹100
2. GST @18% = ₹18
3. Total = ₹118.00 (posted and debited as-is)

### Accounting Entries:

| Ledger Name | Debit (₹) | Credit (₹) |
| --- | --- | --- |
| Customer Loan Account | ₹118.00 |  |
| Processing Fee Income |  | ₹100.00 |
| GST Payable (Output) |  | ₹18.00 |

✅ Matches invoice and is tax compliant

---

### **B. Round at Posting (Nearest Rupee)**

### Use Case:

- Accrued interest
- EMI interest
- Installment schedules

### Example:

- Accrued Interest: ₹199.48 → Rounded: ₹199
- Accrued Interest: ₹199.50 → Rounded: ₹200

### System Flow:

- Round value **at the point of debit**

### Accounting Entries:

| Ledger Name | Debit (₹) | Credit (₹) |
| --- | --- | --- |
| Customer Loan Account | ₹200.00 |  |
| Interest Income |  | ₹199.48 |
| **Rounding Reserve GL (Internal)** |  | ₹0.52 |

> 🔸 If we round down, the 0.52 may be debited to an expense account.
> 

### Why Rounding Reserve GL?

To track small deltas between system-calculated interest and posted amount.

✅ Fair to customer

✅ Keeps books accurate

✅ Required for **audit trail** and **RBI/Stat audit queries**

---

### **C. Round Up with Final Adjustment or Refund**

### Use Case:

- Some microfinance NBFCs
- Short term loans

### Example:

- Monthly interest = ₹100.35 → Round up to ₹101
- Over 12 months, excess collected = ₹0.65 × 12 = ₹7.80
- At closure, refund ₹7.80 or adjust in final EMI

### Ledger at Posting:

| Ledger Name | Debit (₹) | Credit (₹) |
| --- | --- | --- |
| Customer Loan Account | ₹101.00 |  |
| Interest Income |  | ₹100.35 |
| Rounding Reserve |  | ₹0.65 |

### At Closure:

| Ledger Name | Debit (₹) | Credit (₹) |
| --- | --- | --- |
| Rounding Reserve | ₹7.80 |  |
| Customer Refund Payable |  | ₹7.80 |

✅ Customer is not overcharged overall

✅ Finance team reconciles Rounding GL every month

---

## 4. How GST Affects Rounding

When **charges include GST**, banks and NBFCs:

- **Never round** the amount arbitrarily
- Ensure final amount is **precisely calculated** based on GST laws
- GST must be reported to **2 decimal places**

### Example:

| Component | Amount |
| --- | --- |
| Bounce Charge | ₹100.00 |
| GST @18% | ₹18.00 |
| **Total Posted** | ₹118.00 |

If the base fee was ₹99.99, GST = ₹17.9982 → round to ₹18.00

Then total = ₹117.99 + ₹18.00 = **₹117.99**, which can be posted as-is.

⚠️ Rounding GST manually may lead to **tax mismatches** and **audits**.

---

## 5. How Banks/NBFCs Track Variance

- A separate **Rounding GL** or **Variance Ledger** is maintained.
- The GL holds cumulative impact of all rounding adjustments.
- Monthly/quarterly, Finance does a **Rounding GL reconciliation** and:
    - Adjusts to P&L (if immaterial)
    - Clears it out during loan closure
    - Reports it to auditors as part of provisioning

---

## 6. Audit & Compliance Expectations

Auditors (internal or statutory) expect:

- A well-documented **rounding policy**
- Ability to **track variance to each customer level**
- Clean mapping of **posted vs accrued interest**
- No systematic overcharging

RBI expects:

- Transparency to customer
- Refunds if cumulative excess due to rounding
- Clean audit trail in **digital loan flows**

---

## ✅ Best Practices Summary

| Practice | Recommendation |
| --- | --- |
| Rounding Interest | Round to nearest rupee, track delta in internal ledger |
| Charges with GST | Always post full decimal value |
| Statements to Customers | Show rounded amount |
| Final Repayment | Adjust any over-recovery due to rounding |
| Internal GL | Use Rounding Reserve GL to capture net impact |
| Audits | Reconcile Rounding GL quarterly, document policies clearly |