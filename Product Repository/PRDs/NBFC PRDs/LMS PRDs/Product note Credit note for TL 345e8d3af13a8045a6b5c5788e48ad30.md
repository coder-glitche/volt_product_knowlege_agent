# Product note: Credit note for TL

Last Edited: April 28, 2026 4:45 PM
PRD ETA: April 17, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

# **PRD: Interest Refund via Credit Note – Term Loan (Tranche-Level)**

---

## **Background and Context**

**Who is facing the problem:**

- End customers awaiting resolution of incorrectly charged interest
- Operations team handling refund/waiver requests
- Finance team managing manual income reversals and reconciliation
- Product/Tech teams currently intervening via backend/API

---

**What is the challenge today?**

- Interest refunds require **manual intervention via engineering or Finflux access**
- No standardized **maker-checker workflow**
- **Not supported for Term loans, currently productised and implemented only for OD**
- Manual JV posting required for income reversal
- No **system-driven dedupe or validation**
- No **tranche-level visibility or audit tracking**
- Turnaround time is **2–3 days**, impacting CX

---

**Why is it important?**

- Poor customer experience due to delays
- High operational dependency and inefficiency
- Risk of duplicate or incorrect refunds
- Manual accounting overhead for finance
- Lack of audit trail and reconciliation visibility

---

## **1. Problem Scope**

### **In Scope**

We are solving:

### **1. Operational Independence**

- Enable Ops to process **interest refunds without engineering dependency for Term loans**
- Introduce **maker-checker workflow**

---

### **2. Standardized Accounting**

- Eliminate manual JV posting
- Introduce **credit note + automated income reversal**

---

### **3. Tranche-Level Refund Handling**

- Refunds applied at **tranche level (not line level)**
- Excess created is:
    - Initially **tranche-tagged**
    - **Not usable across tranches while tranche is active**
    - Becomes **line-level usable only after tranche closure**

---

### **4. Validation & Dedupe**

- Prevent duplicate refunds via:
    - Schedule validation
    - Credit note existence checks

---

### **5. Audit & Traceability**

- Full linkage:
    - Interest → Credit Note → JV
- Tranche-level enrichment and reporting

---

### **Out of Scope**

- Principal refunds
- Bulk refund processing
- Automated eligibility rules
- Reversal of incorrect refunds (no reversal flow)

---

## **2. Success Criteria**

### **Outcomes**

- Maker → Checker → Accounting completion within **1 hour**
- **>90% reduction** in Jira dependency
- Capability to refund interest for Term Loan
- **Zero duplicate refunds** at tranche-month level

---

### **Post-launch Good State**

- All refunds processed via maker-checker
- Credit notes posted correctly at tranche level
- Automated JV posted for income reversal
- Finance can reconcile via GL + enrichments

---

### **Guardrails**

- No increase in refund misuse
- GL always balanced (CN ↔ JV linkage mandatory)

---

## **3. Solution Scope**

---

## **Solution Overview**

We extend the **Credit Note Interest Refund construct** to **Term Loans**, with **tranche-level application and isolation**.

---

### **Key Design Principle (Important Callout)**

> For Term Loans, **interest is never waived or modified at schedule level**.
> 
> 
> All adjustments are handled strictly via **credit note transactions (accounting reversal)**.
> 

---

## **Detailed Solution**

---

## **1. Maker Flow**

- Maker selects loan account
- System identifies **Term Loan**
- Maker selects:
    - **Tranche ID**
    - **Month-Year**
    - **Refund amount**

---

### **System Validation**

- Fetch from:
    - `f_account_schedule`
    - `f_account_schedule_derived`

Checks:

- Interest exists for that tranche-month
- Refund ≤ interest charged
- No duplicate refund for:

```
loan_id + tranche_id + month_year + refund_type
```

---

- Partial refunds not allowed at a tranche level, only one refund per tranche per month as per dedupe logic

### **Output to Maker**

- Interest charged
- Already refunded
- Available refundable

---

### **Submission**

- Maker adds remarks
- Request created → routed to checker

---

## **2. Checker Flow**

Checker sees:

- Loan account
- **Tranche ID (mandatory visibility)**
- Month-year
- Refund amount
- Remaining refundable amount
- Maker remarks

---

Checker actions:

- Approve → triggers credit note
- Reject → no accounting impact

---

## **3. Credit Note Posting (Core Behavior)**

---

### **Transaction Type**

- Payment Type: **Credit note interest refund (global type)**

---

### **Application Logic**

At **tranche level initiate a payment with type “Credit note interest refund”**:

**Case 1: Dues exist**

- Credit note settles:
    - Interest receivable

**Case 2: No dues**

- Creates **tranche-tagged excess**

---

### **Excess Behavior**

| Scenario | Behavior |
| --- | --- |
| Tranche active | Excess **locked to tranche** |
| Other tranche dues | Cannot auto-adjust |
| Foreclosure | Auto-consumed |
| Tranche closed | Becomes **line-level usable** |

---

## **4. Accounting Treatment**

---

### **A. Credit Note Entry (LMS)**

- Debit: Credit note interest refund (TL)
- Credit:
    - Interest receivable (if outstanding) OR
    - Interest income (if already collected) OR Loan Portfolio OR Excess

---

### **Important Accounting Notes**

- GL override:
    - Applies **only to Term Loan credit note refund**
    - OD flow remains unchanged

---

## **6. Validation & Controls**

---

### **Dedupe Logic**

- Key:

```
loan_id + tranche_id + month_year + refund_type
```

- Allows:
    - Multiple partial refunds
- Blocks:
    - Over-refunding beyond charged interest

---

### **System Validations**

- Interest exists
- Refund amount valid
- No prior full refund

---

## **7. Edge Case Handling**

---

### **Multi-Tranche Loans**

- Refunds allowed:
    - Same month across multiple tranches
- Validation scoped at:
    - **Tranche level (not loan level)**

---

### **Backdated Refund**

- If dues exist → reduces receivable
- If no dues → creates excess

---

### **DPD / SMA / NPA Impact**

- If dues reduced → DPD improves automatically
- If no dues → no impact

---

### **No Reversal Flow**

- Incorrect refunds:
    - No reversal support
    - Handled outside system (out of scope)

---

## **8. Reporting & Reconciliation**

---

### **Finance Requirements**

Finance must be able to:

- Track refunds:
    - Loan + tranche + month
- Reconcile:
    - GL 270 vs Credit Note entries

---

### **Audit Trail**

Mandatory linkage:

```
Interest Posting → Credit Note → JV
```

With:

- Tranche ID
- Month-year
- Transaction IDs

---

## **9. Stakeholder Impact**

---

### **Customer**

- Faster refunds
- Sees credit note in statement

---

### **Operations**

- No Jira dependency
- Uses maker-checker flow

---

### **Finance**

- No manual JVs
- Better reconciliation

---

### **Product / Engineering**

- Reduced backend intervention
- Standardized workflow

---

## **10. Key Open Confirmation (if needed before build)**

- Finflux support for:
    - Tranche-tagged excess behavior
- Reporting format for:
    - GL 270 reconciliation