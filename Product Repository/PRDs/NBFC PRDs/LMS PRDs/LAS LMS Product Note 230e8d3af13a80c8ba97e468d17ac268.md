# LAS LMS Product Note

Last Edited: March 16, 2026 4:03 PM
PRD Owner: Vaibhav Arora
Status: Completed

## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds**

---

### **Overview**

This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds).

Key principles:

- A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**.
- **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices.
- All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency.

---

## **1. MONEY TRANSACTIONS**

---

### **1.1 Disbursement (Forward + Reverse)**

- **Forward Disbursement:**
    - Triggered post approval and sufficient DP validation (LMS)
    - RMS validates real-time prices (every 15 minutes).
    - LMS validates EOD price consistency
    - Both systems must independently confirm DP sufficiency.
    - On success: disbursement request is sent to TSP; loan status updated. (Cashfree)
- **Reverse Disbursement:**
    - Used in cases of failed payout
    - Transaction reversed, collateral DP recalculated.

---

### **1.2 Repayment (Forward + Reverse)**

- **Forward Repayment:**
    - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA)
    - LMS receives repayment; validates against due and excess amounts.
- **Reverse Repayment:**
    - Applicable when repayment fails due to banking errors or incorrect credit.
    - LMS adjusts ledger and reverses credit.

---

### **1.3 Excess Refund**

- LMS calculates overpayment (e.g., duplicate repayment, excess interest).
- Refund is initiated after checking **updated DP position** via (RMS + LMS)
- Final payout initiated via TSP only when RMS confirms buffer post-refund.

---

### **1.4 Charge Application (Forward + Waiver + Refund)**

- **Forward:**
    - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers.
- **Waiver:**
    - Ops-triggered waiver requests.
- **Refund:**
    - Charge reversed, and refund processed. (Credit note)

---

## **2. SERVICING**

---

### **2.1 Closure**

- Triggered after full repayment and complete collateral release.
- LMS validates:
    - Zero principal (LMS)
    - No pending charges (LMS)
    - No open collateral pledges (CMS)
- Closure confirmation sent to DP, TSP, and customer.

---

### **2.2 Renewal**

- Applicable for LAMF/LAS products with fixed-term limits.
- At maturity, a renewal window opens.

---

### **2.3 Mobile / Email / Bank Account Update (Not specific to LAS)**

- Customer-initiated or ops-triggered.
- Updates reflected across servicing stack.
- Bank account updates require:
    - Re-registration of mandate (eNACH or UPI)
    - TSP confirmation
    - Soft lock-in period post-change for fraud mitigation

---

### **2.4 Interest Rate Update (Not specific to LAS)**

- Triggered by internal policy, RBI repo-linked updates, or customer negotiation.
- LMS updates rate → recalculates EMI/schedule.
- System audit log maintained for rate change traceability.

---

### **2.5 Mandate Update**

- Mandate update triggers:
    - New repayment mode
    - Old mandate failure
- LMS triggers re-registration with TSP.
- Until mandate is re-confirmed, fallback collection strategies initiated.

---

### **2.6 Limit Enhancement**

- Customer or system-initiated (basis DP buffer).
- RMS performs real-time DP recalculation for enhanced pledged amount.
- LMS evaluates loan history + RMS DP to approve or decline.

---

### **2.7 Communications**

- Event-based:
    - Disbursement, Repayment, Renewal, Shortfall, Limit Use, Closure.
- Multi-channel:
    - SMS, Email, In-app notifications, IVR (To be evaluated)
- Configurable as per product or regulatory guidelines (e.g., SEBI, RBI).

---

### **2.8 Account Statements**

- Auto-generated:
    - Monthly, Quarterly, Yearly.
- On-demand:
    - Customer via app or support.
- Includes:
    - Loan principal, interest schedule, charges, collateral status, disbursements.

---

## **3. COLLATERAL TRANSACTION & MANAGEMENT**

---

### **3.1 Margin Pledge**

- Customer pledges MF or Shares.
- Separate request per (RTA/Depository)
- DP creates pledge → RMS calculates updated DP in real-time.
- LMS records the asset and assigns DP to the loan ledger.

---

### **3.2 Collateral Release**

- Triggered post repayment, limit reduction, or asset switch.
- Separate request per asset.
- RMS + LMS validate:
    - Post-release DP ≥ Outstanding + buffer (To be defined by risk)
- If confirmed → LMS initiates unpledge → LMS updates ledger.

---

### **3.3 Collateral Sell-off**

- Triggered by:
    - Continuous shortfall
    - Loan default
    - Closure without repayment
    - Voluntary (User asks to sell securities) - Cover how to handle this
- RMS suggests ISINs/folios to liquidate. (RMS to decide this - What will be the logic)
- LMS creates transaction entry and tracks proceeds application.

---

### **3.4 Shortfall**

- Unique to each loan.
- Triggered when:
    - DP <  Principal Outstanding
    - Asset value fall detected by RMS (real-time)
- LMS flags shortfall:
    - Blocks disbursements
    - Sends alerts to customer
    - Triggers top-up or sell-off flows

---

## **System Design Notes**

| Area | Detail |
| --- | --- |
| **DP Composition** | Unified per customer, computed in real-time by RMS, and recorded daily by LMS. |
| **RMS vs LMS Role** | RMS owns risk triggers, shortfall detection, and market price updates. LMS governs ledger, repayments, and compliance. |
| **Asset Management** | All collateral operations (add, release, sell) are initiated as separate, traceable requests. MF and shares are maintained in separate queues. |
| **Servicing Separation** | Money flows and asset flows operate independently, yet are linked via DP validation and transaction sequencing. |

[credit_bureau_reporting_comms_product_note](LAS%20LMS%20Product%20Note/credit_bureau_reporting_comms_product_note%20325e8d3af13a807cafc1d6cd5c139524.md)