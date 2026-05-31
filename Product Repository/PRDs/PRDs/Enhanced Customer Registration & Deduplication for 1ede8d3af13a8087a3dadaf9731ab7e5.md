# Enhanced Customer Registration & Deduplication for MFDs

: Naman Agarwal
Created time: May 8, 2025 4:24 PM
Status: Done
Last edited: May 12, 2025 12:46 PM

**Enhanced Customer Registration & Deduplication for MFDs**

### **Problem**

1. MFDs often hit blockers or need RM support when trying to register customers who already exist in Volt’s system (e.g., as B2C users, under another B2B partner, or with active loans).
2. The current error message—“Failed to register customer”—is vague and doesn’t guide the MFD on what to do next based on the type of duplicate.
3. There were 1,200 such error on MFD portal. ~50% of the registered TOFU. and 185 admin actions to Map partners 

### **Goal**

- Simplify the customer registration journey for MFDs, especially in common duplicate scenarios.
- Reduce RM dependency, particularly for B2C linking.
- Provide clear, actionable feedback to MFDs when a duplicate is found.

### **Proposed Solution: Automat**

When an MFD submits “Register Customer” with Name, Mobile, and:

### 1. **Backend Deduplication Check**

- Use Mobile and to detect existing customer records.

### 2. **Modal-Based Responses Based on Scenario**

- **A. New Customer (No Prior Account)**
    - **Action:** Add customer —> OTP
    - **UI:** No modal or interruption.
- **B. Customer Exists as B2C (Registered directly on Volt)**
    - **Modal Title:** *Customer Found in Volt*
    - **Message:** “This customer is already registered directly with Volt. To add them to your portfolio, OTP verification is required.”
    - **CTAs:**
        - “Send OTP & Add Customer” (launches OTP flow)
        - “Cancel”
- **C. Customer Linked to Another Partner or Has Active Application**
    - **Modal Title:** *Customer Already Registered*
    - **Message:** “This customer ([Name or Masked ID]) is already registered with Volt and may be linked to another partner or have an active application/loan. Please contact your RM for support.”
    - **CTA:** “Okay” (returns MFD to form)
- **D. Typo/Error in Initial Input (Pre-dedupe)**
    - If the MFD catches a mistake before dedupe runs (e.g., wrong PAN), allow them to use the existing “Edit details” button.
    - Once dedupe identifies a match, scenario-specific modals override the generic error message.

### **Key Requirements**

- Backend API for robust deduplication using PAN/Mobile.
- API must return customer status:
    - Not found
    - Existing B2C
    - Linked to another partner
    - Active loan/application
- Dynamic modals based on API response.
- OTP flow for linking B2C customers to MFDs.
- Clear attribution/commission logic for B2C linking.

### **Benefits**

- Fewer MFD drop-offs and RM escalations.
- Seamless onboarding for B2C customers already on Volt.
- Cleaner data—no duplicate accounts.
- MFDs feel empowered to resolve common issues on their own.