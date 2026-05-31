# Product Note: LAS Customer Consent Capture

Last Edited: March 16, 2026 2:48 PM
PRD ETA: March 11, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## **Background and Context**

**Loan Against Shares (LAS)** is a facility where customers pledge listed securities to obtain credit from DSP Finance. We must ensure that borrowers **explicitly acknowledge the risks and operational mechanics of pledged securities** to maintain compliance, risk, and operational coverage for taking necessary collection actions if the market falls significantly.

Regulatory expectations from **SEBI (pledge of securities framework)** and **RBI digital lending guidelines** require lenders to ensure:

- Customers provide **explicit consent for pledge enforcement and liquidation of securities**.
- Customers acknowledge **market-linked risks** associated with pledged securities.
- Customers consent to **digital communication and electronic execution of records**.
- Lenders ensure the borrower **is not pledging promoter-held securities**, which may be subject to additional regulatory restrictions.

Currently, the onboarding journey **does not capture an explicit promoter declaration nor structured consent acknowledgement**. This creates a **compliance and enforceability gap** if securities liquidation is required.

Additionally:

- The **risk disclosure document is not explicitly presented within the user journey**.
- Users are **not asked to explicitly consent to the document during onboarding**.

---

# **1. Problem Scope**

## **In scope**

We are introducing **structured consent capture for Loan Against Shares onboarding**.

This change introduces **explicit consent capture within the KYC verification screen**, ensuring users acknowledge the consent declaration before proceeding.

This includes:

- Displaying a **hyperlinked Consent Declaration** document in the KYC verification screen.
- Allowing users to **view the document within the app/web (bottom sheet)** without leaving the journey.
- **([Document](https://docs.google.com/document/d/1-v_MdBdQrdfxgLhRGK2A4SNq0RYtCBF3/edit))**
- Capturing **explicit consent via checkbox acknowledgement**.
- Recording consent metadata in the **DSP Additional Details API**.
- Introducing **validation in Submit Opportunity** to ensure consent is captured when collateral type is shares.

Primary users:

- Customers applying for **Loan Against Shares**

Secondary users:

- Risk and compliance teams
- DSP LOS integration
- Customer support and collections teams

---

## **Out of scope**

- Changes to the **core pledge creation flow with the depository participant (DP)**.
- Any changes to **loan agreement documentation or e-sign flows**.
- Changes to **collateral valuation or margin monitoring logic**.
- Retrospective capture of consent for **existing users or existing loans**.

These may be handled through **future compliance or document versioning initiatives**.

---

# **2. Success Criteria**

### **Key outcomes**

1. Ensure **regulatory compliant capture of LAS consent declaration** during onboarding.
2. Ensure **100% capture of promoter declaration and risk consent for LAS opportunities**.

### **Key metrics**

| Metric | Expected State |
| --- | --- |
| Consent capture rate | 100% for LAS journeys |
| KYC screen drop-off due to consent | 0% |

### **Guardrail metrics**

- No increase in **KYC completion drop-offs**
- No increase in **onboarding latency**

---

# **3. Solution Scope**

## **Solution Overview**

Volt will introduce an **explicit LAS Consent Declaration acknowledgement within the KYC verification screen**.

Users will:

- View the consent document through a **bottom sheet modal within the app/web**.
- Provide **acknowledgement through a pre-checked checkbox**.
- On confirmation, Volt will **send the consent flag and metadata to DSP via the Additional Details API**.

Additionally, **Submit Opportunity validation will ensure consent is captured whenever collateral type = shares**.

---

## **Detailed Solution Scope**

### **1. KYC Verification Screen Update**

Add a third consent checkbox:

**Copy**

> I confirm that I am not a promoter of the companies whose shares are pledged and that I understand the terms outlined in the document.
> 

![image.png](Product%20Note%20LAS%20Customer%20Consent%20Capture/image.png)

The text **Consent Declaration** will be a **hyperlink**.

---

### **2. Consent Document Behaviour**

When user clicks **Consent Declaration**:

- Open document in a **bottom sheet modal**
- Do **not redirect outside Volt app/web**
- Document should be **scrollable**

---

### **3. Consent Document Hosting**

- Document will be hosted on a **public Volt/DSP accessible link**
- Link will be embedded in the app
- Versioning to be maintained by product/compliance

---

### **4. Consent Data Capture**

When user taps **Confirm** on the KYC screen:

Volt will send consent details via:

**API**

`POST /los/api/v1/utility/additional/data`

Additional parameter to be stored:

| Field | Description |
| --- | --- |
| promoterDeclaration | Boolean indicating borrower is not promoter |
| consentStatus | APPROVED |
| approvalTimestamp | Timestamp of user consent |
| ipAddress | User IP captured during consent |

Example structure:

```
customerConsent: {
   consentStatus: "APPROVED",
   ipAddress: "user-ip",
   approvalTimestamp: "timestamp"
}
```

---

### **5. Submit Opportunity Validation**

Add validation rule:

If:

```
collateralType = SHARES
```

Then:

```
promoterDeclaration = TRUE
```

must exist in **Additional Details API payload**.

Otherwise:

**Block opportunity submission**

Error message:

> "Consent declaration required for Loan Against Shares."
> 

---

### **6. UX Behaviour**

| Description | Details |
| --- | --- |
| Consent checkbox | Mandatory for LAS |
| Document interaction | Bottom sheet modal |
| External navigation | Not allowed |
| User confirmation | Checkbox + Confirm button |
| Consent persistence | Stored in Additional Details API |
| Validation point | Submit Opportunity |

---

# **5. High Level System / User Flow**

### **User Journey**

1. User reaches **KYC Verification Screen**
2. User sees **three consent checkboxes**
3. User taps **Consent Declaration**
4. Bottom sheet opens showing document
5. User reviews and closes document
6. User checks consent checkbox
7. User taps **Confirm**
8. Volt sends **Additional Details API with consent metadata**
9. Opportunity proceeds to next onboarding stage

---

### **Error Case**

If user attempts to proceed without consent:

- Show validation:

> “Please accept the Consent Declaration to continue.”
> 

---

# **6. Appendix**

Typical disclosures include:

- Market volatility acknowledgement
- Margin shortfall liquidation consent
- Enforcement rights on pledged securities
- Digital communication consent

---

## **User Feedback / Operational Context**

Support and collections teams have observed that **users frequently dispute liquidation events during margin shortfalls**.

Capturing explicit acknowledgement of:

- **market risk**
- **auto-liquidation rights**
- **enforcement of pledge**

helps ensure **legal enforceability and reduces dispute risk during collateral liquidation events**.