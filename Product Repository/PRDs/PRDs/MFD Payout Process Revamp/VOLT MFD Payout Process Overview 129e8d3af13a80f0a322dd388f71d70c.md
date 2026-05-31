# VOLT MFD Payout Process Overview

## **1. Introduction**

VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure:

- **Accuracy**
- **Visibility**
- **Transparency**
- **Quick turnaround time (TAT)**
- **Efficient issue resolution**

### **1.1 Payout Process Workflow**

1. **Registration** – Onboarding entities for payouts
2. **Activation** – Meeting eligibility requirements
3. **Calculation** – Computing payouts and tax deductions
4. **Payment** – Disbursement of funds to entities
5. **Reconciliation** – Verifying and settling transactions

---

## **2. Registration**

Entities must be registered with VOLT to be eligible for payouts.

### **2.1 Entity Categories**

1. **Customers / Borrowers** – Required to open credit accounts.
2. **MFDs**
    - **Volt Direct** – Registered on VOLT platform
    - **SaaS MFDs** – Onboarded through partner platforms
    - **Affiliates** – Engaged through business deals
3. **Platforms**
    - **B2B / SaaS** – Engaged through business agreements

### **2.2 Registration Platforms**

- **Volt B2C** (App & Web)
- **Volt Partner Dashboard**
- **B2B SDK**
- **MFD SaaS SDK**

### **2.3 Registration Details**

- Customer: Basic details
- MFD: Commercial agreements, POC details

### **2.4 Communication Channels**

- MFD Partner Dashboard
- Email
- WhatsApp

---

## **3. Payout Activation**

### **3.1 Customers**

1. **MFD Selfline**
    - Special LAS offer at reduced rates for MFD family members
    - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval
    - **Proposed Process**: Automate self-line applications for registered MFD numbers
2. **Customer Cashback**
    - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%)
    - **The system detects eligible customers through queries**

### **3.2 MFDs**

1. **Volt Direct MFDs**
    - Eligible when:
        - A referred customer opens a credit line
        - The referred customer signs up with the MFD’s code
        - MFD registers a bank account & GSTN
2. **SaaS MFDs**
    - Eligible when: A referred customer opens a credit line
    - **Issues:**
        - Unclear data collection process for bank accounts & commercials
        - No clear data storage process
3. **Affiliates**
    - Non-MFD influencers (e.g., YouTubers)
    - Eligible when leads convert to credit lines
4. **Platforms**
    - Activated by Business Development
    - Payouts based on:
        - **Total business volume**
        - **Agreed commercial terms**

---

## **4. Payout Calculation**

Payouts consist of:

- **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules)
- **TDS** (Tax Deducted at Source)
- **GST Tax**
- **Arrears** (Pending payments from previous cycles)
- **Corrections** (Fixed calculation issues)
- **Final Ledger & Payout File**

### **4.1 Base Payout**

1. **Base Rates**
    - **Processing Fee (PF)**: Starting ₹999
    - **Interest Rate**: 10.49%
2. **Negotiated Rates**
    - **Default MFD Payout Structure:**
        - PF: ₹200
        - Trail: 0.5% of POS
    - **Additional Earnings:**
        - Share of deviation from base rates
        - PF Difference (Actual PF - Base PF) × Negotiated Rate
3. **Marketing Offers**
    - Example: ₹3,000 payout for 3 activated applications
4. **Slab-Based Rules**
    - Higher business volumes qualify for better rates
    - Example: >₹10 CR business = 0.6% trail (up from 0.5%)

### **4.2 TDS**

- 5% **TDS deduction** applies if total payout exceeds **₹15,000**.
- Deduction starts after **₹14,250**, refunded if not reaching **₹15,000**.

### **4.3 GST**

- **18% GST applies** to gross payouts for MFDs with valid GSTN.
- Requires **GST ledger** for tax filings.

### **4.4 Arrears**

- This should be **tracked under double-entry bookkeeping**.
- **Accrued payouts should be credited** to entity accounts before reconciliation.
- Currently, **total accrued amounts are not tracked**.

### **4.5 Correction of Calculation Issues**

- Any entity raising an issue with payout calculations gets **adjustments in the next cycle**.

### **4.6 Final Payout File & Ledger**

- Entities should receive a **detailed payout ledger** covering:
    - Base pay breakdown (PF, Trail, etc.)
    - **TDS & GST deductions**
    - **Pending arrears & adjustments**
    - **Transaction-level payout data**

---

## **5. Accounting & Payout Processing**

Before payments are made, all transactions require **accounting approval**.

### **5.1 Accounting**

- Maintains ledgers for:
    1. **MFD Payouts**
    2. **TDS Collection**
    3. **GST Collection**
    4. **Debit Transactions from VOLT Accounts**

### **5.2 Accounting Ledger Requirements**

- Every **transaction should have an attached invoice**.
- **A transaction ledger system should support:**
    - **Transaction Recording** (debits, credits)
    - **Ledger Management** (AP/AR tracking)
    - **Reconciliation** (automated matching)
    - **Audit Trails** (track modifications)
    - **Invoice Management** (automated generation)
    - **Role-Based Access** (security)

### **5.3 Payment Processing**

1. **Beneficiary Addition**
    - Collect & verify **bank accounts** via **Penny Drop**
    - Approve if bank name matches; **escalate** if mismatch
2. **Trigger Payout Requests**
    - Upload verified payout file to **banking software**
    - Process payments and notify relevant teams
3. **Reconciliation & Status Updates**
    - **Mark transactions as successful/failed**
    - **Attach UTR details** for tracking

### **5.4 Common Escalations**

- **Bank account issues**
    - Missing details
    - Mismatched account names
- **Payout issues**
    - Request for correction
    - GST/TDS discrepancies

---

## **6. Reconciliation**

Reconciliation involves **matching payout transactions with system records**.

### **6.1 Key Data Sources**

1. **Application-Level Data:** `credit_applications_entity`
2. **Loan-Level Data:** `credit_main`
3. **Transactions Ledger:** `transactions`
4. **Partner Data:** `partner_accounts`

### **6.2 Common Issues in Reconciliation**

- **Delays in processing regular payouts**
- **Inconsistent GST payments**
- **Cashback calculation issues**
- **Bank account verification delays**
- **Gaps in payout status communication**

---

This version is **structured, clear, and eliminates redundancy** while keeping all important details. Let me know if you need further refinements! 🚀