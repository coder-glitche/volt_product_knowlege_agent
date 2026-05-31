# Term Loan: DPD handling

## **Handling of Days Past Dues (DPD) for Overdue Tranches**

### **Definition of DPD**

- **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date.
- DPD shall be calculated **per tranche/EMI** and maintained at both:
    - **Tranche level** → to identify overdue EMIs.
    - **Loan account level** → to reflect overall delinquency status.

---

### **DPD Lifecycle & Tracking**

- **0 DPD:** EMI due on the due date but not yet paid.
- **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation.
- **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency.
- Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**.
- If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance.

---

### **DPD & Apportionment Interaction**

- When sell-off proceeds are received:
    1. First, they are applied to the **oldest overdue tranche (highest DPD)**.
    2. Within a tranche, proceeds are apportioned as:
        - Interest component → Principal component → Charges.
    3. Once all overdue tranches are cleared, any remaining proceeds are applied towards:
        - Upcoming EMIs (not yet due), then
        - Loan-level excess balance.

---

### **DPD in Customer Communication(To be closed)**

- Customer statements and notifications shall explicitly display:
    - Current DPD status per tranche.
    - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days).
    - Post-sell-off DPD reset (or residual overdue if sell-off insufficient).

---

### **Regulatory & Credit Bureau Reporting**

- DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax).
- If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement.
- Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems.

---

### **Exception Handling**

- If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized.
- In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.