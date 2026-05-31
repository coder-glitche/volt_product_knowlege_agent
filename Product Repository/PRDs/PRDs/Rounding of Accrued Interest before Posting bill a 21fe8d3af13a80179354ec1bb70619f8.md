# Rounding of Accrued Interest before Posting bill amount

: Ranjan kumar Singh
Created time: June 27, 2025 4:54 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

### **1. Background**

Currently, the system posts accrued interest **without rounding**, i.e., if accrued interest is ₹100.10, the same amount is posted on the due date.

As per **RBI Fair Practices Code** and **industry standards**, it's a best practice to **round interest to the nearest rupee** at the time of posting, especially when the amount is debited from the customer’s bank account. This ensures clarity and fairness, and aligns with most NBFC/bank practices.

## **2. Objective**

- Implement a logic to **round accrued interest to the nearest rupee (₹)** at the time of posting (auto-debit or manual payment).
- Ensure **compliance with RBI guidelines** around customer transparency and fair charging.
- Update all internal and customer-facing views (e.g., statements, ledgers, dashboards) to reflect the **rounded amount**.

## **3. Scope**

### **In Scope**

- Rounding logic implementation before **posting accrued interest** on billing date.
- Update interest posting jobs to use the rounded value.
- Update ledger to reflect the rounded amount.
- Audit log and internal reporting to capture both actual accrued and posted amount for reconciliation.
- Penal should only apply on overdue interest amount >100

### **Out of Scope**

- Rounding of accrued interest, **principal amount** or **fees/penalties**.
- Changes to real-time interest accrual logic.
- Historical interest adjustment.

---

## **4. RBI Guideline Reference**

RBI’s Fair Practices Code emphasizes:

- Transparency in the **amount being recovered**.
- No excess or hidden charges.
- Any **automated debit** must be **precise, disclosed, and fair**.
- Must ensure that rounding doesn’t lead to **systematic overcharging (may happen in case of always rounding up the amount)**.

Most regulated financial institutions follow rounding to the nearest rupee to avoid fractional debit issues and disputes.

Page: 91 (30.4 Rounding off of transactions)

[https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/72MC010714CS.pdf](https://www.rbi.org.in/commonman/Upload/English/Notification/PDFs/72MC010714CS.pdf)

[Round off all transactions to nearest rupee: RBI to NBFCs](https://economictimes.indiatimes.com/news/economy/policy/round-off-all-transactions-to-nearest-rupee-rbi-to-nbfcs/articleshow/35635116.cms)

[Reserve Bank of India](https://www.rbi.org.in/commonman/english/Scripts/Notification.aspx?Id=241#:~:text=1%2D90%2D91%20dated%20January,and%20fraction%20of%20less%20than)

[Reserve Bank of India](https://www.rbi.org.in/commonman/english/scripts/Notification.aspx?Id=1066#29)

[Reserve Bank of India](https://www.rbi.org.in/commonman/english/scripts/Notification.aspx?Id=894)

---

## **5. Functional Requirements**

| # | Requirement Description | Type | Priority | Remarks |
| --- | --- | --- | --- | --- |
| 1 | On due date(EOM), before posting interest, **round the total accrued interest to the nearest rupee** using standard rounding (₹100.49 → ₹100, ₹100.50 → ₹101). | Functional | High |  |
| 2 | Store both the **raw accrued interest** and the **rounded interest posted** in the ledger and system DB for audit. | Functional | High |  |
| 3 | Ensure customer is shown only the **rounded amount** in statements, LSP app, and communications. | UX/Data | High |  |
| 4 | Reconcile the difference (if any) between actual and rounded amount into **system account (interest variance GL)** for accounting parity. | Accounting | Medium |  |
| 6 | If loan is prepaid before due date, round the netPayable | Functional | NA | Already handled in foreclosure API |
| 7 | Audit logs should capture original accrued amount, rounded posted amount, timestamp, and job ID. | Audit | Medium |  |

---

## **6. Non-Functional Requirements**

- **Accuracy**: Must round only at posting, not during accrual.
- **Compliance**: Ensure rounded amount does not exceed actual accrued interest over the loan lifecycle cumulatively.
- **Performance**: No significant delay should be introduced in daily interest posting job.

---

## **7. Edge Cases**

| Scenario | Expected Behavior |
| --- | --- |
| Accrued Interest = ₹0.49 | Round down to ₹0 |
| Accrued Interest = ₹0.50 | Round up to ₹1 |
| Accrued Interest = ₹199.51 | Round to ₹200 |
| Manual Prepayment before Due Date | Net Payable Rounding is handled in foreclosure API |
| Refund/waive-off of posted interest (If any) | Refund rounded amount (same as posted) |

---

## **8. Acceptance Criteria**

- [ ]  Accrued interest is rounded only during posting.
- [ ]  Customer account is debited by the rounded amount.
- [ ]  Ledger contains both actual and posted interest.
- [ ]  No rounding discrepancies observed in audit.
- [ ]  Backward compatibility maintained for historical records.

---

## **9. Dependencies**

- Finance/Accounting team for GL mapping of interest variance.
- Data/Reporting team to reflect updated fields.
- QA team to test edge rounding cases.

[How **banks and NBFCs** manage **rounding of interest and charges**, and how they handle **accounting** in these cases.](Rounding%20of%20Accrued%20Interest%20before%20Posting%20bill%20a/How%20banks%20and%20NBFCs%20manage%20rounding%20of%20interest%20an%2022de8d3af13a802bb01be4e3ed6b56e0.md)