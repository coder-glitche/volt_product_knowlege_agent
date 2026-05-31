# [DSP] SMA & NPA Tagging at Customer Level

: Ranjan kumar Singh
Created time: July 16, 2025 11:45 AM
Status: Done
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

### Scope

- Automatic classification of customer accounts into SMA and NPA categories
- DPD-based classification logic
- Account reversion rules and conditions
- Customer-level classification aggregation across multiple loans (Currently only for LAS)

---

# **How do we measure success?**

### Functional Success

- 100% accurate classification based on defined rules
- Zero data loss during classification updates

### Business Success

- Improved early warning system for potential defaults
- Enhanced regulatory compliance reporting
- Reduced manual effort in classification management

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

## Business Requirements

### 1. Classification Objectives

- **Risk Management**: Early identification of potential defaulters through SMA classifications
- **Regulatory Compliance**: Adherence to NBFC regulations for NPA reporting
- **Portfolio Monitoring**: Real-time visibility into portfolio health across different risk buckets

### 1.1 Key Stakeholders

- **Primary**: Risk Management Team, Credit Operations Team
- **Secondary**: Finance Team, Compliance Team
- **Technical**: Development Team, Data Engineering Team

## 2. Functional Requirements

### 2.1 Overview

| # | Requirement Description | Type | Priority |
| --- | --- | --- | --- |
| 1 | Fetch max DPD across all active LANs per customer daily | Functional | P0 |
| 2 | Classify customer based on max DPD using the table above | Functional | P0 |
| 3 | Once tagged as NPA, continue tagging as NPA until DPD = 0 | Functional | P0 |
| 4 | Store historical tagging in customer account logs | Data | P1 |
| 5 | Expose classification in internal systems and reports | Data | P1 |

### 2.2 Classification Matrix

| DPD Range (Max across all LANs) | SMA/NPA Classification | Loan Status | NPA Stage |
| --- | --- | --- | --- |
| 0 | Current | Standard | – |
| 1 – 30 | SMA-0 | Standard | – |
| 31 – 60 | SMA-1 | Standard | – |
| 61 – 90 | SMA-2 | Standard | – |
| 91 – 456 | NPA | Substandard | NPA |
| 457 – 821 | NPA | Doubtful 1 | NPA |
| 822 – 1551 | NPA | Doubtful 2 | NPA |
| ≥ 1552 | NPA | Doubtful 3 | NPA |

### 2.3 Customer-Level Classification Logic

### 2.3.1 Aggregation Rule

- Classification is determined at **customer level**
- Use **Maximum DPD across all LANs (Loan Account Numbers)** for a customer
- If a customer has multiple loans, the worst classification applies to the entire customer relationship

### 2.3.2 Examples

- Customer A has 3 loans: DPD 0, DPD 15, DPD 45 → Customer classification: **SMA1** (based on max DPD of 45)
- Customer B has 2 loans: DPD 25, DPD 95 → Customer classification: **NPA Substandard** (based on max DPD of 95)

### 2.4 Classification Movement Rules

### 2.4.1 Degradation (Worsening Classification)

- **Trigger**: DPD increases due to non-payment
- **Process**: Automatic daily batch job to recalculate classifications
- **Timing**: Real-time updates as DPD crosses thresholds

### 2.4.2 SMA Reversion Rules

- **SMA to Standard**: When customer makes payments/waivers and DPD resets to 0 across all loans
- **SMA Inter-movement**: Direct movement between SMA categories based on current max DPD
- **Timeline**: Immediate upon payment processing and DPD recalculation

### 2.4.3 NPA Reversion Rules

- **Strict Condition**: Account can revert from NPA to Standard ONLY when:
    - ALL dues are cleared across all customer loans
    - DPD = 0 across all customer loans
- **Persistence Rule**: Account remains NPA even if DPD becomes 1 day, until complete due clearance
- **No Intermediate Steps**: No movement from NPA to SMA categories; direct jump to Standard only

### **3. Non-Functional Requirements**

- **Scalability**: System should support tagging at scale for all customers daily.
- **Auditability**: Maintain change history for classification.
- **Performance**: Tagging logic to be executed as part of the daily EOD process.

### **4. Edge Cases**

| **Scenario** | **Expected Behavior** |
| --- | --- |
| Customer with one LAN at DPD 45 and another at DPD 0 | Max DPD = 45 → SMA1 |
| Customer tagged as NPA, clears part payment → DPD = 5 | Remains NPA until DPD = 0 |
| Customer clears all dues → DPD = 0 | Classification resets to **Current** |

## 5. Business Rules and Validations

### 5.1 Data Validation Rules

- DPD cannot be negative
- Classification date cannot be future dated
- Customer must have at least one active loan for classification
- All customer loans(currently only LAS) must be considered for max DPD calculation

### 5.2 Business Logic Validations

- Ensure SMA accounts can move freely between categories based on current DPD
- Validate NPA accounts follow strict reversion rules
- Prevent classification downgrades without proper payment reconciliation

## 6. Reporting Requirements

### 6.1 Operational Reports

- **Daily Classification Summary**: Count and value by classification bucket
- **Classification Movement Report**: Accounts moved between categories

---

# **Design**

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes