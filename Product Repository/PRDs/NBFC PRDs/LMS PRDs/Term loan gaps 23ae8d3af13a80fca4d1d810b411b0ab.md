# Term loan gaps

Last Edited: July 24, 2025 5:10 PM
PRD Owner: Vaibhav Arora

### **Spend & Convert Enhancements**

- Support for **flat PF (Processing Fee)** values in spend and convert requests.
- Allow **knockoff remarks** to be passed in the spend and convert payload.
- Support passing **different charge types** and **collecting multiple charges** in a single spend and convert request.

---

### 🧾 **Repayment Logic**

- Enable both **loan-level and line-level repayments** to co-exist for term loans.
- Mark **repayment at loan level** as a current **gap** in configuration.
- Support **EMI-level repayments**.
- Include **apportionment details** in the repayment response (internal checks needed).
- Support **loan-level excess refunds**.
- **Excess amounts**:
    - Should remain **parked** after due generation (do not auto-settle dues via FIFO).
    - At **line level**, should **increase available limit**.

---

### 🧮 **Due/Bill Generation**

- Bills should be generated **independent of the due generation job**—on demand.

---

### 📆 **Schedule and Simulation**

- Provide a **preview schedule API** without needing to create a line.
- Enable **tranche-level simulation API** for a given date.
- All **date fields** must be passed as **EPOCH timestamps**.

---

### 🧠 **Tagging & Status Configurations**

- SMA tagging should be **configurable**.
- **NPA to be tracked at client level**, while **SMA is tracked at loan level**.

---

### 📉 **Interest & Limit Management**

- Support **interest rate updates** on loans.
- **Limit replenishment** should only occur when the **underlying loan is fully closed**, whether via EMI or part-payment.