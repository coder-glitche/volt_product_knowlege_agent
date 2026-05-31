# LMS: Multiple sell off requests

Last Edited: March 19, 2026 9:44 PM
PRD ETA: January 16, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## 1. Background & Context

In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time.

Operationally, this  breaks in real-world scenarios where:

- Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level
- Failed invocations do not cover the **entire overdue or shortfall**
- Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed).

This leads to:

- Manual workarounds by the engineering team to support the use case
- Delays in curing shortfall / overdue
- Risk of exposure breach if sell-off cannot be retriggered in time
- Risk of incorrect updates by the engineering team

---

## 2. Problem Statement

**Ops raises a sell-off request for multiple securities.**

- Some invocations succeed
- One or more invocations fail or get stuck (e.g. CAMS / KFIN issues)
- Proceeds received are **insufficient to cover the shortfall**
- System blocks Ops from raising another sell-off request due to an existing non-terminal request

This creates a deadlock where:

- Exposure remains unresolved
- Ops cannot act despite legitimate need
- Manual intervention becomes necessary

---

## 3. Current Sell-Off Flow (As-Is)

1. **Sell-off Initiation**
    - Ops raises sell-off via **Bulk Maker** at **collateral level**
    - Requests are consolidated at **loan level**
    - A single sell-off request is created per loan
2. **Blocking Logic**
    - Selected units are blocked in LMS
    - Blocked units stop contributing to **Drawing Power (DP)**
3. **Threshold Calculation**
    
    ```
    AvailableThreshold= DP - POS - COS - IOS - Accrued Interest
    
    ```
    
    - Blocking ensures:
        - No excess collateral release
        - No further disbursement beyond safe exposure
4. **Invocation Flow**
    - RTA APIs (CAMS / KFIN) invoked
    - RTAs pass requests to AMCs
    - AMC sells securities
5. **Settlement & Reconciliation**
    - Proceeds credited to NBFC bank account
    - Settlement TAT: 2–3 working days
    - Ops reconciles proceeds via bulk operation
    - Proceeds mapped to collateral sell-off requests
    - Amount posted to respective loan accounts in LMS

---

## 4. Key Issue in Current Design

- System enforces **single non-terminal sell-off request per loan**
- Partial failures leave the loan **under-covered**
- Ops cannot initiate corrective sell-off until the earlier request reaches a terminal state
- External dependencies (RTA / AMC) make resolution time unpredictable

---

## 5. Proposed Change (To-Be)

### 5.1 New Rule for Sell-Off Requests

Modify sell-off request validation to allow:

> Up to 3 concurrent non-terminal sell-off requests per loan, provided:
> 
- Existing requests are in a **Pending reconciliation state.**
- Requests in **terminal state** do not count toward the limit

---

### 5.2 Definition of States

**Terminal States**

- Success / Completed
- Failed (explicitly closed)

**Non-Terminal States**

- Created
- Invocation in progress
- Pending Reconciliation
- Mapping / posting to loan pending

---

## 6. Functional Requirements

### FR-1: Concurrent Sell-Off Limit

- LMS must allow **maximum 3 non-terminal sell-off requests per loan**
- 4th request should be rejected with a clear system error (not allowed)

### FR-2: Blocking Logic (No Change)

- Units selected in **each sell-off request** must be blocked independently
- Blocked units must stop contributing to DP immediately
- Blocking must be **request-specific**, not global

---

## 7. Risk & Mitigations

| Risk | Mitigation |
| --- | --- |
| Excessive blocking reduces DP sharply | Cap of 3 requests |
| Ops misuse by raising unnecessary sell-offs | Role-based access + audit logs |
| Edge cases with partial settlement | Explicit state handling |

---

## 9. Success Metrics

- Zero manual overrides needed for partial sell-off failures
- Reduction in TAT for curing shortfall / overdue
- No increase in exposure breaches

---