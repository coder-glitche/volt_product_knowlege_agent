# Charge reversal enhancement V2

Last Edited: March 19, 2026 9:44 PM
PRD ETA: December 11, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

Today, waiving or refunding charges was manual, operationally intensive, and people-dependent. With the charge reversal enhancement now built and deployed, we have eliminated dependency on engineering/backend intervention, reduced friction for internal teams, and improved customer resolution time.

This PRD documents the final implemented solution — including the maker/checker workflow, credit note processing, validations, accounting flows, and the enhancements required to support charges with no GST and the productisation manual JV transaction posting

---

### **Why Do We Waive or Refund Charges?**

- **Operational Errors:** Invalid or incorrect charges (e.g., dishonour fees, penal charge) need correction.
- **User Retention or Exceptions:** Charges waived for goodwill or service recovery.

---

### **Current Pain Points** (Resolved through this enhancement)

- **Manual Intervention:** Refunds/waivers no longer require engineering APIs or direct Finflux access.
- **Process Overhead:** Jira dependency removed; command centre can independently perform refunds.
- Manual JV process automated, no dependency on product or engineering to process manual JV integrations.
- Handling of charges without GST, this is required as a dependency of a RFC item where we have to remove GST application for penal charges and dishonour charges
- **Billing Constraints:**
    - Waiver allowed only for outstanding charges — unchanged.
    - Refund pathway introduced for collected charges through **CREDIT_NOTE**, now implemented.
- **Customer Experience:** Resolution time reduced from ~2–3 days to within one working day.

---

# **How do we measure success?**

- **Metric:** Reduction in Jira tickets for charge waivers/refunds
    
    **Goal:** >90% reduction — achieved in post-go-live baseline.
    
- **Metric:** Average time to process a waiver/refund
    
    **Goal:** Completed within one working day — achieved for ADHOC charges.
    

---

# **How are others solving this problem?**

- TCL and BFL issue **credit notes** for invalid charges, incorrect interest, or backdated adjustments.
- Our implementation now mirrors this industry-standard mechanism with an auditable, maker-checker-based refund workflow.

---

# **What is the solution?**

All components below are **implemented and live**.

We have created a **Charge Refund Maker/Checker workflow** that behaves as follows:

- **If a charge is completely outstanding** → it is waived.
- **If a charge is completely collected/paid** → a **Credit note** is issued to the loan account.
- **If a charge is partially collected** → a **Credit note** is issued to the loan account.

A new repayment type **“Credit note”** is now supported in LMS.

This repayment *does not* trigger any cash movement. Operations uses this type for reconciliation visibility.

The first set of supported use cases now live:

- Processing fees
- Margin pledge charges
- Dishonour fees
    
    (All as configured under ADHOC charges)
    

---

### **Accounting**

A normal pay-in has the following apportionment:

- **Debit:** Fund source
- **Credit:** POS + Interest receivable + Fees receivable + Penalties receivable + Excess

For credit notes, we now record a *non-cash* reversal:

### **Proxy liability account created:**

Intermittent liability control account

### **Implemented behaviour:**

- CREDIT_NOTE reduces receivable/income *without* cash movement.

### **To be implemented:**

Manual JV clears the proxy and posts GST and income reversals to final GLs.

---

## **Why?**

You're simulating a *reduction in income* for previously collected charges without moving money out of the NBFC.

### 1. **Nature of Credit Note**

Charges such as processing fees, margin pledge charges, and dishonour fees are recognized as income. CREDIT_NOTE reverses this.

### 2. **What actually happens**

Instead of cash going out, a **non-cash transaction** is created.

### 3. **Purpose of proxy account**

Debit placeholder until the manual JV clears the reversal into income & tax accounts.

---

## **Post-credit-note Journal Entries (To be implemented)**

A manual JV is passed with:

| Entry | GL | Description |
| --- | --- | --- |
| **Credit** | Credit note balance | Clears proxy liability |
| **Debit** | Income from fees | Reverse collected income |
| **Debit** | GST payables (CGST/SGST/IGST/UTGST) | Reverse tax |
| **Debit** | GST Payable Expense | Only when classified as "Expense" refund type |

---

### **New GL Accounts (Created & Configured)**

| Account Name | Entry Type | Account Type |
| --- | --- | --- |
| Expense from waivers | Credit | Liability |
| Income from Fees (reversal) | Debit | Income (negative) |
| GST/CGST/SGST/etc. Payable refund | Debit | Liability |
| GST Payable Expense | Debit | Expense (Post September 30th) |

---

# **Charge details retrieval (Live)**

Command Centre fetches charge metadata via existing Finflux flat data report:

**Request sample:**

```bash
curl --location '.../runreports/charge_detail/flatdata?R_chargeIdentifier=CRID325313647556'

```

**Sample response:**

```json
[
  {
    "account_number": "000008048",
    "external_identifier": "CRID325313647556",
    "charge_due_on": "1753697507199",
    "charge_type": "Processing Fee",
    "total_charge_amount": "1180.000000",
    "charge_amount_excluding_tax": "1000.000000",
    "charge_outstanding_amount": "0.000000",
    "tax_name": "IGST",
    "tax_amount": "180.000000"
  }
]

Add GL account ID mapping

```

Sample where there is no tax applied:

```json
[
    {
        "account_number": "000010995",
        "external_identifier": "CR1223232232323232",
        "charge_due_on": "1765455968494",
        "charge_type": "Dishonour charge",
        "total_charge_amount": "1000.000000",
        "charge_amount_excluding_tax": "1000.000000",
        "charge_outstanding_amount": "1000.000000",
        "tax_name": "",
        "tax_amount": ""
    }
]
```

---

# **Validations** (All implemented)

- Already waived charges → **cannot** be refunded
- Already refunded charges → **cannot** be refunded again
- Collected charges → **cannot** be waived (only refunded)
- Outstanding charges → **cannot** be refunded (only waived)
- Charges with existing waiver request → **blocked**

---

# **Interface (Implemented)**

### Maker task

Fetches CRID → shows metadata → shows computed refund type → allows submission.

### Checker task

Shows debit/credit breakdown, refund type, justification fields → approve/reject.

---

# **Design**

[https://miro.com/app/board/uXjVKvYl1nc=/](https://miro.com/app/board/uXjVKvYl1nc=/)

---

# **Analytics (Live)**

## Volume metrics

| Metric Name | Description | Frequency |
| --- | --- | --- |
| total_refund_requests | No. of refund requests initiated | Daily, Weekly |
| total_refunds_processed | Successful refunds | Daily, Weekly |
| refund_approval_rate | approvals / total requests | Daily, Weekly |
| average_processing_time | Maker → Checker → Completion | Weekly |
| refunds_by_charge_type | PF, Margin pledge, Dishonour | Weekly |

## Impact metrics

| Metric Name | Description | Frequency |
| --- | --- | --- |
| total_refunded_amount | Sum of all refunds | Weekly, Monthly |
| gst_adjusted_refund_amount | Refunds treated as Reversal | Monthly |
| gst_expensed_amount | Refunds treated as Expense | Monthly |

---

# **Timeline/Release Planning**

### **Phase 0 — Go Live (Completed)**

- ADHOC charges supported
- Manual JV batch (monthly) live
- All validations, accounting logic, enrichments functional

---

### **Phase 1 — Go Live (This requirement)**

- Manual JVs automated at refund completion
- Refund maker will support penalty refunds using same credit note + JV framework

---

### **Phase 2 — Go Live (Upcoming)**

- Penalty charges to move from Finflux to Fenix
- Interest waivers supported via credit note

---

## Marketing

NA

---

## Ops & Sales training

Pending scheduling.

---

# **Frequently asked questions (FAQs)**

(To be expanded)

---

# **Action items / checklist**

- [ ]  Product
- [ ]  Business
- [ ]  Design

---

# **Feedback**

(To be filled post review)

---

# **Learnings & Next steps**

- Need for automated JV ingestion to reduce finance load
- Need to extend refund support to penalties & interest
- Need for N-level analytics on reversal vs expense classification

---

# **Appendix**

## Meeting notes

*(Existing screenshot retained)*

---

# **Enhancements included in this update (post-development)**

Two enhancements to be incorporated into the now-live implementation:

---

## **1. Charges with no GST**

System now supports charge records where:

```json
"tax_name": "",
"tax_amount": ""

```

- Validations remain unchanged
- JV computation ignores GST lines (GST stored as 0 in such scenario)
- Income reversal continues normally

---

## **2. Second-leg manual JV productised**

After credit note creation, the manual JV is now a **productised step**, with consistent accounting enrichments and structured payloads.

### Implemented enrichments:

### **LMS Transaction Enrichments (Implemented)**

- **Transaction Enrichment 1:** Charge reversal initiation timestamp
- **Transaction Enrichment 2:** CRID (ID of transaction being reversed)

### **Accounting Transaction Enrichments**

- **Enrichment 1:** JE ID of original CREDIT_NOTE transaction
- **Enrichment 2:** `"CHARGE_REVERSAL"` — constant identifier

These enrichments ensure visibility for analytics and reconciliation pipelines.

---

## **Manual JV API Reference (Implemented)**

Below is the reference for how finance posts JVs (based on your shared script):

```json
{
  "locale": "en",
  "dateFormat": "dd MMMM yyyy",
  "officeId": 1,
  "transactionDate": "30 September 2025", (Date of credit note transaction)
  "currencyCode": "INR",
  "credits": [
    { "glAccountId": 41 (Static), "amount": 1180.00 } - Total charge amount
  ],
  "debits": [
    { "glAccountId": 43, "amount": 1000.00 }, Amount excluding GST
    { "glAccountId": 45, "amount": 180.00 }, GST distribution  (This can be either IGST or split between CGST and SGST)
  ],
  "referenceNumber": "CRID325313647556",
  "comments": "Charge reversal for external ID: CRID325313647556",
  "Enrichment1": "txn_id",  (Credit note transaction)
  "Enrichment2": "CHARGE_REVERSAL"
}

```

## **3. Automated Manual JV Posting Workflow (Enhancement Included in This Release)**

To support full automation of the second-leg accounting movement, the following workflow has been implemented. This ensures that every CREDIT_NOTE transaction is correctly reversed in the books through a matching manual JV, without requiring Finance or Engineering intervention.

### **Workflow of transaction**

1. **Consume charge detail**
    - Using the charge identifier (CRID), the system fetches charge metadata via the existing flat report.
    - This includes charge amount (ex-GST), GST component (if any), charge type, loan account, and application date.
2. **Post credit note**
    - The refund maker initiates a CREDIT_NOTE repayment on the loan account.
    - This is a non-cash posting that reduces receivables.
    - LMS enrichments (Transaction Enrichment 1 & 2) are populated at this step.
3. **Get credit note JE transaction detail**
    - CREDIT_NOTE postings generate accounting entries within LMS/Finflux.
    - To retrieve the system-generated JE for the CREDIT_NOTE, the following API is consumed:
        
        ```bash
        /runreports/get_je_detail/flatdata?R_transactionId=<credit_note_transaction_id>
        
        ```
        
        Example response:
        
        ```json
        [
          {
            "transaction_identifier": "905f5618-319b-4004-9987-8e13991842d3",
            "id": 69576,
            "entry_date": "Dec 10, 2025",
            "account_id": 36,
            "name": "Fees receivable",
            "type_enum": 2,
            "amount": 1532.820000
          },
          {
            "transaction_identifier": "905f5618-319b-4004-9987-8e13991842d3",
            "id": 69576,
            "entry_date": "Dec 10, 2025",
            "account_id": 31,
            "name": "Income from Fees",
            "type_enum": 1,
            "amount": 1299.000000
          },
          {
            "transaction_identifier": "905f5618-319b-4004-9987-8e13991842d3",
            "id": 69576,
            "entry_date": "Dec 10, 2025",
            "account_id": 18,
            "name": "IGST Payable",
            "type_enum": 1,
            "amount": 233.820000
          }
        ]
        
        ```
        
        - **`id` = JE ID of the CREDIT_NOTE transaction**
        - This JE ID must be used as *Enrichment1* in the reversal JV.
4. **Delay before processing**
    - To ensure all CREDIT_NOTE entries and their accounting lines have been fully posted in Finflux,
        
        **the JE retrieval and JV construction will be scheduled at end-of-day (6 PM IST).**
        
    - This avoids race conditions, missing entries, or partial GL postings.
5. **Basis the CREDIT_NOTE JE detail, compute JV reversal entries**
    - Using the JE ID returned above, and the corresponding charge detail from Fenix:
        - Determine the income reversal amount (charge_excluding_tax).
        - Determine the GST reversal amount(s) (IGST/CGST/SGST) based on `tax_name`.
        - Determine the total charge amount (for the credit side).
    - This mirrors the logic in the script shared earlier and ensures the reversal matches the exact accounting posted during CREDIT_NOTE.
6. **Populate all debit/credit accounts for reversal JV**
    - Credit: Intermittent liability control account (credit note balance)
    - Debit: Income from Fees (charge amount ex-GST)
    - Debit: GST Payable Accounts (IGST/CGST/SGST) if applicable
    - Debit: GST Payable Expense (if refund type = Expense)
    
    These accounts follow the final GL configuration approved by Finance.
    
7. **Post manual JV entries**
    - The final reversal JV is posted via:
        
        ```
        POST /fineract-provider/api/v1/journalentries
        
        ```
        
    - Enrichment fields applied:
        - **Enrichment1:** JE ID of CREDIT_NOTE transaction
        - **Enrichment2:** `"CHARGE_REVERSAL"`
    - This closes the loop:
        
        CREDIT_NOTE (proxy debit) → Reversal JV (proxy credit + income/GST debit)
        

---

# **Resulting End-to-End Automated Flow**

| Step | System | Outcome |
| --- | --- | --- |
| Charge detail consumed | Fenix | System retrieves amount + GST split |
| Credit note posted | LMS | Creates CREDIT_NOTE repayment (non-cash) |
| End-of-day JE extraction | Finflux | Retrieves JE ID for CREDIT_NOTE |
| JV constructed | Workflow engine | GL debits/credits computed |
| JV posted | Finflux | Final accounting reversal completed |
| Enrichments stored | LMS + Analytics | Full reconciliation visibility |