# Finflux Product Setup for Co-Lending

Last Edited: March 19, 2026 9:44 PM
PRD ETA: January 27, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## 1. Background & Context

As part of the co-lending setup, loans are economically split between:

- **10% exposure (CLA portion)**
- **90% exposure (TCL)**
- **100% loan representation** required for operational and accounting purposes

Current state:

- Finflux is running on a **single instance** supporting **OD and TL products**
- All reporting, accounting, SMA/NPA tagging, and operational workflows are currently **instance-scoped**
- Finflux manages collateral and exposure deduplication

The setup needs to support:

- Fast go-live
- Clean accounting
- Correct delinquency signaling to TCL
- Minimal disruption to existing production flows

---

## 2. Problem Statement

The co-lending structure introduces multiple complexities:

- **Collateral deduplication risk** if multiple loans referencing the same securities exist in the same instance
- **Client-level SMA/NPA contagion**, where delinquency in a small CLA exposure may impact unrelated production loans
- **Accounting segregation** required across different exposure types
- **Operational overhead** introduced by multiple Finflux instances
- **Reporting and reconciliation complexity** across LMS, Finflux, and TCL

---

## 3. Design Options Considered

### Option A: Single Finflux Instance with Multiple Products

- All co-lending loans (10% and 100%) reside in the same instance
- Separation handled purely via product-level configurations

**Challenges**

- High risk of collateral dedupe conflicts
- Client-level NPA impact across all loans
- Heavy reliance on product-level filters across reporting and accounting
- Higher regression risk for existing OD and TL products

---

### Option B: Multiple Finflux Instances for All Co-Lending Loans

- Separate instances for 10% and 100% loans

**Challenges**

- Higher setup and maintenance effort
- Configuration and version-sync risks
- Increased reporting and reconciliation overhead
- Multiple operational points of failure at launch

---

## 4. Final Recommendation (Chosen Approach)

**Recommended Setup**

- **10% co-lending loan (CLA exposure)**
→ Booked in the **existing Finflux instance**
- **100% loan**
→ Booked in a **separate Finflux instance**
- **90% exposure**
→ Booked in **TCL**

This approach optimizes for **lower effort, faster go-live, and controlled risk**, while keeping core production flows isolated.

---

## 5. Rationale for the Recommendation

### 5.1 Faster Go-Live with Minimal Change Surface

- Existing Finflux instance already supports:
    - Live products
    - Accounting
    - Reporting
    - Monitoring
- Adding a **single CLA product (10%)** is significantly lower effort than:
    - Standing up and operationalising a new instance
- Risk exposure is limited due to the **small economic size** of the CLA loan

---

### 5.2 Clean Accounting Separation

- **10% loan**
    - Fully accounted within the existing instance
- **100% loan**
    - Accounted in a separate instance with its own chart of accounts

This avoids:

- Complex product-level GL segregation within a single instance
- Accounting ambiguity during audits and reconciliations

---

### 5.3 Reduced Collateral & LTV Risk for Production Loans

- Production-critical loan (100%) is isolated from CLA exposure
- Avoids:
    - Security duplication
    - LTV contamination
    - Margin and collateral misinterpretation in LMS

Collateral integrity is preserved where it matters most.

---

### 5.4 Controlled SMA / NPA Handling

- CLA delinquency will be:
    - Managed at the loan level
    - Explicitly communicated to TCL when required
- Client-level contagion is avoided by:
    - Process controls
    - Defined suppression logic for non-production exposure

This keeps architectural complexity low while ensuring regulatory signaling is preserved.

---

### 5.5 Lower Operational & Reporting Overhead vs Full Multi-Instance Split

- Small, operationally noisy CLA exposure remains in a known system
- Large, clean production exposure is isolated
- Reporting and reconciliation complexity is reduced compared to managing two co-lending instances

---

## 6. Known Risks & Explicit Trade-Offs

### Risk 1: Client-Level Delinquency Divergence

- A customer may be standard in one loan and delinquent in another

**Mitigation**

- Documented policy stating exposure-specific delinquency treatment
- Explicit escalation and notification to TCL for CLA NPA events

---

### Risk 2: Bureau & Regulatory Interpretation

- Divergent loan statuses may be visible externally

**Mitigation**

- Bureau reporting treatment to be explicitly defined
- Regulatory narrative documented and approved

---

### Risk 3: One-Way Architectural Decision

- Post-go-live instance consolidation is expensive

**Mitigation**

- Accepted as a conscious trade-off to enable faster market entry
- Revisit only if scale or regulatory requirements change

---

## 7. Summary

The recommended setup prioritizes **speed, operational safety, and accounting clarity** for the initial co-lending launch. By keeping the ten percent CLA loan in the existing Finflux instance and isolating the hundred percent loan in a separate instance, we minimize production risk while avoiding unnecessary infrastructure complexity.

This approach deliberately accepts manageable process-level risks in favor of a faster and more controlled go-live, with clear paths to revisit the architecture as the co-lending portfolio scales.