# Product Note: Penalty migration to Fenix (Colending)

Last Edited: April 14, 2026 4:02 PM
PRD ETA: March 15, 2026
PRD Owner: Vaibhav Arora
Status: Completed

# **Background and Context**

Currently, penal charges for overdue loan accounts are computed by an **automated job in Finflux**. This job runs daily at 4 AM and applies penalties when interest becomes overdue. These charges are stored as **applicable charges in Finflux** and surfaced to downstream systems primarily through foreclosure simulations.

This architecture introduces several operational and product limitations.

**Who is impacted**

- Operations teams
- Product and engineering teams
- Finance and customer support teams
- Borrowers indirectly (through slower issue resolution)

**Challenges in the current setup**

1. **Limited product control**
    
    Penal charge computation logic currently resides inside Finflux jobs. Any change to the logic requires dependency on Finflux configuration and third party coordination.
    
2. **Limited configurability**
    
    The current implementation applies a **flat penalty of ₹10 per day**, whereas the Key Fact Statement (KFS) requires **slab-based penalty computation based on overdue amount**. (This is a compliance observation)
    
3. **No operational control**
    
    Since penalties are not created as **transactions inside Fenix (internal LMS)**:
    
    - Operations cannot **waive or refund penalties directly**
    - Charge-level audit and tracking are difficult
4. **Colending complexity**
    
    In Loan-90 / Loan-10 structures, penalties must be **orchestrated across loan legs**. The Finflux-driven penalty logic does not provide sufficient control to ensure accurate charge allocation across colending loans.
    
5. **Foreclosure simulation dependency**
    
    Foreclosure calculations rely on Finflux charge simulations. This makes enhancements difficult and increases dependency on an external system for a critical borrower-facing calculation (Finflux).
    

Additionally, the current system lacks a **generalised framework for defining and applying loan charges**. Future charges such as **Annual Maintenance Charges (AMC)** or other contingent fees would require ad-hoc implementations.

This enhancement addresses these limitations by:

- Migrating **penal charge computation to Fenix**
- Introducing a **generic Applicable Charges framework**
- Enabling **charge-level operational controls**
- Supporting **future charge types such as AMC**

---

# **1. Problem Scope**

## **In Scope**

This enhancement addresses the following problems.

### **Migration of penalty computation to Fenix**

Daily penal charge computation will move from **Finflux jobs to Fenix**, eliminating system dependency and enabling full product control.

### **Penalty pricing enhancement**

Penalty logic will be enhanced from **flat charges to slab-based pricing**, as defined in the KFS.

### **Minimum overdue threshold**

Penalties will only be applied when:

Overdue Amount ≥ ₹10

This avoids unnecessary micro-charges. (Reduce customer escalations)

### **Introduction of Applicable Charges framework**

A reusable framework will be introduced to define and apply multiple charge types such as:

- Penal charges (contingent)
- Annual maintenance charges (non-contingent)
- Future fee types (As scoped in the future)

### **CRID-based charge tracking for Penalties**

Each applied charge currently has a **Charge Reference ID (CRID)** within Fenix apart from Penalty charges, with this change penalties will also start having one.

This enables:

- Penalty auditability
- Penalty waivers
- Penalty refunds via credit note
- Penalty operational tracking

### **Colending support**

Penalty charges will be orchestrated across **Loan-90 / Loan-10 legs**, ensuring accurate accounting.

### **Foreclosure simulation enhancement**

Foreclosure calculations will simulate **future charges using the applicable charges framework** instead of relying on Finflux logic.

---

## **Out of Scope**

The following items are not included in this scope:

- Migration or adjustment of **historical penalties already applied in Finflux**
- Support for additional charge types beyond **penalties and AMC framework capability**
- UI redesign of the command centre maker/checker workflows

---

# **2. Success Criteria**

### **Primary outcomes**

1. Penal charge computation fully migrated to Fenix for Colending (Phase -1)
2. Applicable Charges framework implemented and operational.
3. Penalty waiver and refund workflows supported via existing charge reversal framework.
4. Colending Penalty application enablement

---

### **Key Success Metrics**

| Metric | Target |
| --- | --- |
| Dependency on Finflux for penalties | Eliminated |
| Penalty computation accuracy | 100% aligned with KFS slabs |
| Penalty transactions with CRID | 100% coverage |
| Foreclosure simulation accuracy | 100% |

---

### **Guardrail Metrics**

- No increase in **loan accounting discrepancies**
- No increase in **foreclosure API latency**
- No duplicate penalty applications due to job retries

---

# **3. Solution Scope**

## **Solution Overview**

This enhancement migrates penalty computation from **Finflux to Fenix** and introduces a **generic Applicable Charges framework** within the internal LMS.

The solution will:

- Define configurable **charge rules**
- Map applicable charges to loans
- Apply charges based on **frequency and conditions**
- Generate **CRID-based charge transactions for Penalties**
- Support **operational waivers and refunds**
- Enable application of **charges such as AMC and its support in Foreclosure simulation**
- Support **accurate foreclosure simulation**

---

# **Detailed Solution Scope**

## **1. Applicable Charges Framework**

A reusable charge framework will be introduced within Fenix.

The framework will consist of three components.

### **Charge Configuration**

Defines the behaviour of a charge.

Example attributes include:

- Charge type
- Pricing model (flat / slab)
- Frequency (daily / yearly / Monthly)
- Classification (contingent / non-contingent)
- Controlling value (overdue amount / outstanding principal)

---

### **Loan Applicable Charges Mapping**

Defines which charges apply to each loan.

Example fields:

- Loan ID
- Charge configuration
- Effective start date
- Optional overrides

This allows **loan-level configurability of charge behaviour**.

---

### **Charge Transactions**

Whenever a charge is applied, a transaction will be created.

Each transaction will include:

- **CRID (Charge Reference ID)**
- Loan ID
- Charge type
- Charge amount
- Charge date
- Charge status

This enables:

- refunds
- waivers
- reconciliation
- auditability

---

## **2. Penal Charge Logic**

Penalties will be applied **daily** when overdue exists.

### **Overdue Amount Definition**

Overdue Amount = Interest Overdue + Principal Overdue

### **Minimum Threshold**

Penalties are applied only when:

Overdue Amount ≥ ₹10

---

### **Penalty Slabs (KFS compliant)**

| Overdue Amount | Daily Penal Charge |
| --- | --- |
| Up to ₹25k | ₹10 |
| ₹25k – ₹50k | ₹25 |
| ₹50k – ₹1L | ₹50 |
| ₹1L – ₹2.5L | ₹100 |
| ₹2.5L – ₹5L | ₹250 |
| ₹5L – ₹10L | ₹500 |
| ₹10L – ₹25L | ₹1000 |
| ₹25L – ₹50L | ₹2500 |
| ₹50L – ₹1Cr | ₹5000 |
| Above ₹1Cr | ₹10000 |

Penalties are **exclusive of GST, GST is not applied on Penalties in the LMS and is configured in the same manner)**

---

## **3. Colending Support**

For colending loans:

Penalties will be computed once at the 100% **loan level**, then allocated across lender loans.

Example For TCL:

Penalty applied = ₹100 on Loan 100

| Loan Leg | Charge Allocation |
| --- | --- |
| Loan 90 | ₹0 |
| Loan 10 | ₹100 |

Separate transactions will be created for each leg.

---

## **4. Foreclosure Simulation**

The foreclosure API will simulate charges dynamically.

Supported scenarios:

- Foreclosure amount for **current date (this will be as is directly from LMS)**
- Foreclosure simulation for **future date (here we will have to build a simulation logic - For accrued interest we will continue to rely on amount shared from Finflux however applicable charges will be simulated from Fenix instead of Finflux)**

The system will:

1. Fetch applicable charges
2. Determine frequency and logic
3. Simulate charges until requested date
4. Return computed foreclosure amount

This removes dependency on Finflux simulations.

---

## **5. Annual Maintenance Charges (Future Support)**

The framework will support **AMC charges**.

Example characteristics:

| Attribute | AMC |
| --- | --- |
| Classification | Non-contingent |
| Frequency | Yearly |
| Pricing | Flat |

Example:

AMC = ₹500 annually. (Annually on the loan account opening date)

---

## **6. Penalty Waiver and Refund Support**

Penalty charges will integrate with the existing **Charge Reversal framework**.

The behaviour will follow the existing logic.

| Charge Status | Behaviour |
| --- | --- |
| Fully outstanding | Charge waived |
| Fully collected | Credit note issued |
| Partially collected | Credit note issued |

Refunds will use the **Credit_note_penalty repayment type**, which creates a **non-cash transaction**.

---

## **Accounting Behaviour**

Refunds will trigger a **credit note + manual JV reversal**.

The only change compared to other charges is the **income GL account used for reversal**.

For penalty refunds:

| Entry | GL Account | Description |
| --- | --- | --- |
| Credit | Intermittent liability account | Clears proxy liability |
| Debit | Income from Penalty | Reverse penalty income |

---

### **Operational Impact**

Operations teams will now be able to:

- waive outstanding penalty charges
- refund collected penalties
- track charge history via CRID

All actions can be performed via **Command Centre without engineering intervention**.

---

| Description | Details |
| --- | --- |
| Penalty computation | Migrated from Finflux to Fenix |
| Pricing logic | Flat → Slab based |
| Minimum penalty threshold | ₹10 overdue |
| Charge tracking | CRID-based transactions |
| Colending support | Loan-90 / Loan-10 allocation |
| Operational control | Waiver & refund supported |
| Foreclosure simulation | Fenix-based simulation |
| Future extensibility | AMC support |

---

# **5. High Level System Flow**

### **Penalty Application Flow**

Daily job runs within Fenix.

1. Fetch active loans
2. Compute overdue amount
3. Check minimum threshold
4. Identify penalty slab
5. Create charge transaction
6. Generate CRID
7. Allocate across loan legs if colending

---

### **Foreclosure Simulation Flow**

1. Foreclosure request received
2. Fetch loan balances
3. Retrieve applicable charges
4. Simulate future charges
5. Return foreclosure amount

---

# **6. Appendix**

### **Benchmarking**

Industry lenders such as **Bajaj Finance and Tata Capital** maintain internal **charge rule engines** within their LMS to control:

- penalty fees
- bounce charges
- maintenance fees
- foreclosure charges

Migrating charge computation to Fenix aligns with this architecture and positions Fenix as the **system of control for loan economics**.

---

### **User Feedback / Operational Inputs**

Operations teams highlighted the need for:

- direct waiver capability
- faster penalty refunds
- removal of engineering dependency

This enhancement directly addresses these requirements.