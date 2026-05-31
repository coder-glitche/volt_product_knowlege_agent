# PRD: Disbursement Method Selection Logic (BRE Optimization)

: Ameya Aglawe
Created time: April 6, 2026 3:17 PM
Status: Not started
Last edited: April 7, 2026 11:53 AM

---

# **1. Problem Statement**

Currently, payout method selection (IMPS / NEFT / RTGS) is not dynamically optimized based on:

- Disbursement sequence (1st vs subsequent)
- Loan type (co-lending vs non co-lending)
- Ticket size
- Sourcing channel (e.g., CRED)

This leads to:

- Suboptimal payout routing
- Higher costs and delays
- Lack of configurability at product / contract / channel level

---

## **2. Objective**

Enable a rule-based engine (BRE) to dynamically select payout method based on:

- Disbursement sequence
- Loan type
- Amount slab
- Sourcing channel

---

## **3. Scope**

### **Dimensions for Rule Evaluation**

1. **Contract type**
    - Co-lending
    - Non co-lending
2. **Sourcing Channel**
    - Volt
    - CRED (override rules)
3. **Nth Disbursement**
    - 1st
    - Subsequent
4. **Amount Slabs**
    - < 2 lakhs
    - 2–5 lakhs
    - 5 lakhs

---

## **4. Business Rules**

### **4.1 Co-lending Loans**

| Disbursement | < 2L | 2L–5L | > 5L |
| --- | --- | --- | --- |
| **1st** | NEFT | NEFT | RTGS |
| **Subsequent** | NEFT | RTGS | RTGS |

---

### **4.2 Non Co-lending Loans**

| Disbursement | < 2L | 2L–5L | > 5L |
| --- | --- | --- | --- |
| **1st** | IMPS | IMPS | RTGS |
| **Subsequent** | NEFT | RTGS | RTGS |

---

### **4.3 Sourcing Channel: CRED**

| Disbursement | < 2L | 2L–5L | > 5L |
| --- | --- | --- | --- |
| **1st** | IMPS | IMPS | RTGS |
| **Subsequent** | IMPS | RTGS | RTGS |

**Note:**

- These rules override both co-lending and non co-lending logic when sourcing channel = CRED

---

## **5. Rule Priority Logic**

Order of evaluation:

1. **Sourcing Channel Override (Highest Priority)**
2. **Contract Type (Co-lending / Non co-lending)**
3. **Nth Disbursement**
4. **Amount Slab**

---

## **6. Configurability Requirements**

- Rules should be configurable at:
    - Product level (for future requirements)
    - Contract level
    - Sourcing channel level
- Ability to:
    - Add/edit slabs
    - Change payout method mapping
    - Introduce new channels without code changes

---

## **8. Success Metrics**

- Reduction in payout failures
- Reduction in payout cost per transaction
- Improvement in disbursement TAT
- % of transactions routed via optimal rail

---