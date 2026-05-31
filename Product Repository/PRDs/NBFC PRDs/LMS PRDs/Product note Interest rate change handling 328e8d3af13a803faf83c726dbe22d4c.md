# Product note: Interest rate change handling

Last Edited: March 19, 2026 9:51 PM
PRD ETA: March 19, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

## **Background and Context**

In the current co-lending construct between DSP (NBFC) and TCL (co-lender), loans are originated and managed across multiple representations within the LMS:

- **Loan 90 (TCL Book):** Represents TCL’s capital contribution and is controlled externally by TCL, including interest rate decisions.
- **Loan 10 (DSP Book):** Represents DSP’s capital contribution and follows DSP’s internal benchmark and pricing logic.
- **Loan 100 (Customer-facing Loan):** A composite loan created in the LMS, reflecting the borrower’s obligation and used for repayment schedules, accruals, and customer communication.

The effective interest rate for the borrower is derived as a **weighted average of the underlying lender rates based on capital contribution**:

- 90% → TCL (Loan 90)
- 10% → DSP (Loan 10)

However, from a system and implementation perspective:

- The LMS treats **Loan 100 as an independent loan** with its own benchmark and ROI.
- Interest rates are currently configured using **benchmark + spread constructs defined at an organizational level**.
- There is **no native support for dynamic weighted rate computation** across multiple lender loans within the LMS.

---

### **Problem Statement**

As part of ongoing co-lending operations:

1. **Independent Rate Changes by Lenders**
    - TCL may revise its interest rates (benchmark or spread) independently.
    - DSP may also revise its own benchmark rates.
    - These changes directly impact the **effective blended ROI** applicable to the borrower.
2. **Lack of Native Synchronization**
    - Since Loan 90, Loan 10, and Loan 100 are maintained separately:
        - Rate changes in Loan 90 (TCL) do not automatically reflect in Loan 100.
        - Loan 100 must be **manually or systematically updated** to maintain parity with the blended rate.
3. **Risk of Misalignment**
    - If Loan 90 and Loan 100 are not updated in sync:
        - Incorrect borrower interest may be charged.
        - Accruals and repayment splits between lenders may become inconsistent.
        - Downstream systems (accounting, reconciliation, reporting) may break.
4. **Operational Complexity**
    - Current benchmark configuration is **organization-wide**, not contract-specific.
    - With multiple co-lending partners, each having:
        - Different benchmarks
        - Different spreads
        - Different rate change cycles
            
            → A single benchmark approach does not scale.
            

---

### **Constraints**

- Loan 100 **must exist as a physical loan in the LMS** and cannot be treated as a derived construct.
- LMS supports:
    - Benchmark + differential-based rate configuration
    - Loan-level ROI updates
- LMS does **not support dynamic runtime recomputation** of ROI based on multiple linked loans.
- TCL has agreed to **pre-notify rate changes within a defined time window**, enabling controlled updates.

---

### **Proposed Approach**

To address the above challenges while working within LMS constraints:

### **1. Contract-Level Benchmark Configuration**

- Each **co-lending relationship (DSP + TCL)** will have a **dedicated benchmark configuration** defined at the **contract level**.
- This benchmark will represent the **effective blended benchmark** applicable for Loan 100 under that specific co-lending agreement.
- During loan creation:
    - LMS will pick:
        - Benchmark
        - Spread/differential
            
            from the **contract configuration** instead of organization-level defaults.
            

---

### **2. Unified Benchmark Strategy for DSP**

- DSP’s:
    - **100% book loans**
    - **Loan 10 (co-lending DSP portion)**
    
    will continue to use a **common benchmark (IBLR)**.
    
- This ensures:
    - Centralized control of DSP’s cost of funds
    - Minimal operational overhead in benchmark management

---

### **3. Loan 100 Benchmark Handling**

Two key principles:

- Loan 100 will:
    - Either use a **contract-specific benchmark**, or
    - Use DSP benchmark with a **contract-specific spread adjustment**
- The benchmark for Loan 100 will act as a **control layer** to:
    - Absorb changes from both TCL and DSP sides
    - Ensure borrower-facing ROI reflects the correct blended rate

---

### **4. Rate Change Handling Process**

### **(A) TCL Rate Change**

- TCL will notify DSP prior to any rate revision.
- Upon notification:
    - Loan 90 ROI will be updated in LMS
    - Corresponding adjustment will be made to:
        - Loan 100 benchmark and/or spread
            
            such that:
            
    - **Blended borrower ROI remains consistent**

---

### **(B) DSP Rate Change**

- DSP updates its internal benchmark (IBLR).
- Impact:
    - Loan 10 ROI changes automatically (linked to benchmark)
    - Loan 100 benchmark/spread will be updated accordingly

---

### **5. Synchronization Requirement**

To ensure system consistency:

- **Loan 90 and Loan 100 rate updates must be executed together**
- Updates must:
    - Use the **same effective date**
    - Be processed within the **same operational window**

This ensures:

- Accurate interest accrual
- Correct repayment splitting logic
- No downstream reconciliation breaks

---

### **6. Reconciliation Safeguard**

Although proactive notification is expected from TCL:

- A **periodic reconciliation process (daily or T+1)** will be implemented to:
    - Validate Loan 90 ROI in LMS vs TCL communicated rates
    - Flag any discrepancies

This acts as a **risk mitigation layer**, not the primary control.

---

### **Scalability Consideration**

With multiple co-lending partners:

- Each **(Colender + Product + Agreement)** combination will have:
    - Its own **contract-level benchmark configuration**

This enables:

- Independent rate management per relationship
- Clean isolation of pricing logic
- Scalable onboarding of new co-lenders without impacting existing setups

---

### **Summary**

This approach ensures:

- Compatibility with LMS constraints (Loan 100 as a physical loan)
- Controlled handling of independent lender rate changes
- Contract-level flexibility for multiple co-lending relationships
- Reduced operational risk through synchronization and reconciliation safeguards

At the same time, it avoids:

- Complex dynamic rate computation layers
- Over-reliance on manual differential adjustments
- Benchmark fragmentation at the organization level