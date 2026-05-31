# Razorpay SDK enhancement for Colending

Last Edited: April 22, 2026 6:29 PM
PRD ETA: April 22, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

## **Background and Context**

Today, LSPs (e.g. Volt, CRED, PhonePe) can integrate with DSP for repayments via multiple payment gateway (PG) options:

- DSP internal PG
- Razorpay
- Cashfree
- Native PG managed by LSP (direct settlement)

### **Current Challenge**

With **colending**, regulatory guidelines mandate:

- Funds must flow into **escrow accounts**
- This leads to **different MIDs**:
    - DSP loans → DSP current account MID
    - Colending loans → Escrow MID

For Razorpay SDK:

- `client_id` is tied to MID
- SDK invocation becomes **MID dependent**

### **What is broken today**

- LSPs need **loan-type aware logic**
- Multiple client IDs → complex integration
- Breaks abstraction:
    
    > DSP vs Colending loans should be indistinguishable
    > 

### **Why this matters**

- Colending is a key growth lever
- Repayment friction directly impacts:
    - Conversion
    - Partner experience
- Slows onboarding of new LSPs

---

## **1. Problem Scope**

### **In scope**

- Unified Razorpay integration across:
    - DSP loans
    - Colended loans
- Support for:
    - SDK-based flow
    - Payment link flow
- Dynamic resolution of:
    - MID
    - Razorpay client_id
- Contract-level PG configuration
- Frontend enablement for SDK invocation

**Primary users**

- LSP engineering teams (Volt FE + BE)
- DSP LMS / PG systems

**Secondary users**

- End customers
- Ops / reconciliation teams

---

### **Out of scope**

- Supporting multiple PGs for colending (Razorpay only)
- Changes to settlement / reconciliation
- Native LSP PG flows

---

## **2. Success Criteria**

### **Primary outcomes**

- Single integration for all loan types
- SDK invocation fully abstracted
- No increase in payment failures

### **Post-launch good state**

- 100% repayments via unified API
- No loan-type branching at LSP
- 99.9% uptime

### **Guardrails**

- No reconciliation mismatch
- No incorrect MID usage
- No increase in disputes

---

## **3. Solution Scope**

### **Solution Overview**

Introduce **contract-driven PG abstraction** where:

- `create repayment order API` determines:
    - PG (Razorpay)
    - MID
    - client_id
- LSP consumes a **single API**
- SDK invocation is **agnostic to loan type**

---

### **Core Design**

### **1. API Enhancement**

**Endpoint**

```
POST /repayment/order/v1
```

**Enhancements**

- Add: `paymentGateway`
- Populate: `paymentGatewayOrderId` (for SDK)

---

### **2. Contract-Level Configuration**

| Field | Description |
| --- | --- |
| paymentGateway | Razorpay / Cashfree |
| clientId | Razorpay client ID |
| midType | Current / Escrow |

---

### **3. Flow Handling**

### **Payment Link Flow**

- DSP generates link
- No SDK / client_id needed

### **SDK Flow**

- DSP:
    - Creates Razorpay order
    - Resolves correct client_id
- Returns `paymentGatewayOrderId`

---

### **Detailed Use Cases**

| Description | Details |
| --- | --- |
| DSP loan repayment | Uses DSP MID |
| Colending repayment | Uses escrow MID |
| SDK flow | Uses contract client_id |
| Payment link flow | Redirect-based |
| Retry | New order creation |
| Multi-LSP | Same integration |

---

### **Edge Cases**

- Missing contract config → fail fast
- Invalid client_id → block order creation
- Expired link → regenerate
- Loan migration → use latest contract

---

### **Impact**

**LSP**

- No integration change required

**Ops**

- No SOP changes

**Sales**

- Simpler pitch: unified integration

**User**

- No experience change

---

## **4. Frontend Scope (Volt)**

### **Objective**

Enable Volt to invoke Razorpay SDK using DSP response **without loan-type awareness**

---

### **Frontend Responsibilities**

- Call repayment order API
- Determine flow:
    - SDK vs Payment Link
- Invoke SDK using:
    - `paymentGatewayOrderId`
- Handle success / failure / retry

---

### **Frontend Flow**

### **Step 1: Initiate repayment**

Call backend with:

- Loan ID
- Amount
- Order type

---

### **Step 2: Parse response**

| Field | Usage |
| --- | --- |
| payInOrderType | Flow selection |
| paymentLink | Redirect |
| paymentGatewayOrderId | SDK |
| amount | Validation |

---

### **Step 3: Execute flow**

### **Payment Link**

- Open link in WebView

### **SDK Flow**

```
constoptions= {
  key:client_id,
  amount:amount,
  order_id:paymentGatewayOrderId,
  handler:handleSuccess
};

newRazorpay(options).open();
```

---

### **Key Principles**

- No loan-type branching
- No MID awareness
- No PG decisioning at FE

---

### **Error Handling**

| Scenario | Action |
| --- | --- |
| API failure | Retry |
| Missing order ID | Block SDK |
| SDK failure | Retry |
| Pending state | Poll backend |

---

### **Success Handling**

- Capture SDK response
- Send to backend for verification
- Show success screen

---

### **UX Expectations**

- Fast checkout
- Minimal redirects
- Clear states (success/failure/pending)

---

## **5. High-Level Flow**

### **Step 1: LSP → DSP**

- Call repayment order API

---

### **Step 2: DSP Processing**

- Fetch contract
- Resolve:
    - PG = Razorpay
    - MID
    - client_id

---

### **Step 3: Order Creation**

- SDK → Razorpay order
- Link → Payment link

---

### **Step 4: Response to LSP**

- SDK:
    - `paymentGatewayOrderId`
- Link:
    - `paymentLink`

---

### **Step 5: Payment Completion**

- Razorpay webhook → DSP
- DSP:
    - Verify
    - Update LMS
    - Trigger reconciliation

---

### **Error Scenarios**

- Config missing → fail
- Razorpay failure → retry
- Timeout → re-initiate

---

## **6. Appendix**

### **Key Principle**

> **Complete abstraction at LSP layer**
> 
> 
> LSP should behave as if:
> 
> - There is only one loan type
> - There is only one payment gateway