# ADMIN Actions for the RM Sales Team

: Naman Agarwal
Created time: January 14, 2025 3:55 PM
Status: Pending Review
Last edited: February 27, 2025 3:34 PM

### **Problem Statement**

1. RMs spend considerable time Raising ops tickets and following up. 

- ALL B2B2C Admin actions
    
    
    | admin_action | COUNTA of admin_action |
    | --- | --- |
    | APPLICATION_ROI_OVERRIDE | 6 |
    | APPLICATION_RULE_OVERRIDE | 337 |
    | APPROVE_MANDATE | 45 |
    | APPROVE_PARTIAL_LIEN_REMOVAL | 14 |
    | APPROVE_REJECT_LOAN_FORECLOSURE | 44 |
    | CHANGE_LENDER_FOR_APPLICATION | 927 |
    | FORECLOSE_LOAN_ACCOUNT | 27 |
    | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 |
    | OVERRIDE_CREDIT_APPROVAL | 4 |
    | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 |
    | PROCESSING_FEE_OVERRIDE | 16 |
    | RECREATE_LENDER_APPLICATION | 96 |
    | REFRESH_CREDIT_INFO | 173 |
    | REGENERATE_AGREEMENT_LINK | 1 |
    | REGENERATE_MANDATE_LINK | 6 |
    | REVIEW_APPLICATION | 4 |
    | REVIEW_CO_BORROWER_DOCUMENTS | 65 |
    | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 |
    | SUSPEND_CREDIT_APPLICATION | 563 |
    | TATA_COLLECTION_SETTLEMENT_RETRY | 199 |
    | UNIFY_MF_DATA_V2 | 2 |
    | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 |
    | UPDATE_PARTNER_DETAILS | 13 |
    | VERIFY_BANK_ACCOUNT | 3 |
    | Grand Total | 2860 |

1. Actions that RMs can take but have to raise to ops can be reduced 
    1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. 

## Success metrics

- Reduction in Pre-loan customer details change tickets to Ops
- TAT for customer requests for the customer details change

Impact 

The current count is 121 cases in the past 2 months

## Proposed solution

- We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details
- These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation.

For Tata

- We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB.

For DSP

- We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB.

 

# **Previous Understanding Proposed Solution**

### **Admin Action Portal Enhancements**

- Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently.

### **Workflow for Pre-Loan Admin Action**

1. **Access Control:**
    - “Change customer details -Pre Agreement “ admin action will be provided to support team
2. **Process Steps:**
    - Agent logs into the Admin Portal.
    - Selects the "Change Customer Details" admin action.
    - Inputs either the **current mobile number, borrower ID, or PAN** to locate the relevant user.
    - Admin portal displays only those applications that:
        - Belong to the user.
        - Are at stages prior to **Agreement Completion**.
    - **Confirmation and Validation:**
        - Display a confirmation message in the UI for all successful phone number updates.
        - Validate the updated phone number to ensure:
            - No duplicate entries with live applications.
            - Proper formatting and OTP verification for unverified numbers.
        - OTP verification, after the agent has added the Phone number a OTP will be send and has to be entered on the Next step. We will have this OTP send and Enter as Optional for now
        - **Error Cases**
            1. No application found for the number provided.
            2. Dedupe validation failed for the updated number.
            3. Number linked to a different PAN.
            4. Invalid phone number format.
            5. Unverified phone number (require OTP verification).
3. **Post-Agreement Stage Handling:**
    - Once the agreement is signed, agents will need to escalate phone number changes to the Ops team, as Lender is required to be notified

- After agreement is signed the agent would need to Raise the issue to Ops team for a Number change (based on discussion with RMs)

### **Tracking and Accountability**

- Record login ID and application details for every admin action.
- Add an optional support  Ticket ID field to track the reason behind each admin action.

 

### 

![MFD channel .png](ADMIN%20Actions%20for%20the%20RM%20Sales%20Team/MFD_channel_.png)

### **Current Setup**

- Currently, agents can change the borrower account ID, phone number, and email without verification, using the Borrower Account ID (BAI) from Retool.
- An admin action configuration table exists (created by Nishant) to manage admin action access.
- Phone numbers (P1 for app login and P2 for fetch step) are handled as follows:
    - P2 defaults to P1 unless updated during the fetch step.
    - OTPs for fetch and pledge are sent to P2.
    - Withdrawal OTPs are sent to P1.
    - If a user registers with P2, it creates a new account with no associated applications.
- P1 is used for KYC verification
- Key considerations:
    - Define when RMs can change phone numbers.
    - Establish the process for OTP collection from customers during number changes.

### **Additional Actions**

- **Bank Account Changes**: Permitted until the application is in "Progress."
- **Suspend Application**: Required in cases like:
    - Pledge-related issues.
    - Significant delays in account opening, resulting in funds being unliened.