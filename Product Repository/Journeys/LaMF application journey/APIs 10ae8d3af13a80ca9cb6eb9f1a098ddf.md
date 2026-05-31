# APIs

**Explanation of the API Sequence in the Volt Money Application Flow**

Welcome aboard! As the head developer for the Volt Money product, I'd like to walk you through the sequence of APIs that power our application flow. This explanation will help you understand how each step functions, the APIs involved, and how they contribute to the overall user experience.

---

### **Overview**

The Volt Money application process involves several key steps:

1. **Login**
2. **PAN Verification**
3. **Fetch Folio**
4. **Eligibility Assessment and Lender Assignment**
5. **KYC Verification**
6. **Bank Account Verification**
7. **Mandate Setting**
8. **Asset Pledge**
9. **KFS and Documentation**
10. **Loan Agreement Execution**

Each of these steps is supported by specific APIs and may involve external partners. I'll explain each step in detail.

---

### **1. Login**

- **API Used:** *Custom Authentication API (Not listed in the provided APIs)*
- **Functionality:**
    - **User Authentication:** The user logs in using their mobile number and an OTP (One-Time Password) sent to their phone.
- **Notes:**
    - This step establishes a secure session for the user.
    - While not specified in the provided API list, we use a standard authentication service to handle this process.

---

### **2. PAN Verification**

- **API Used:**
    - `POST /app/borrower/application/kyc/pan/panVerify`
- **Partner:** Decentro (facilitates connection to NSDL)
- **Functionality:**
    - **PAN Validation:** Verifies the user's PAN number with NSDL to ensure it is valid.
    - **Data Retrieval:** Fetches the full name associated with the PAN.
- **Notes:**
    - Essential for KYC compliance and identity verification.
    - Helps prevent fraudulent applications.

---

### **3. Fetch Folio**

- **APIs Used:**
    - `POST /app/borrower/application/fetch/init/otp/v3`
    - `POST /app/borrower/application/fetch/authCAS/v2`
- **Partners:** Cams, KFintech, MF Central
- **Functionality:**
    - **Initiate Fetch:** Sends an OTP to the user to authenticate the retrieval of their mutual fund folio.
    - **Authenticate and Retrieve:** Verifies the OTP and fetches the folio details.
- **Notes:**
    - The folio contains information like ISIN and NAV, which are crucial for assessing the user's assets.
    - This data is used later in the asset pledge and eligibility assessment.

---

### **4. Eligibility Assessment and Lender Assignment**

- **API Used:**
    - `POST /app/borrower/application/credit/profile/evaluate`
- **Partner:** Internal Business Rule Engine (BRE)
- **Functionality:**
    - **Eligibility Calculation:** Uses BRE to compute the eligible loan limit based on the user's assets and lender criteria.
    - **Lender Assignment:** Assigns the user to a lender (either Bajaj Finance or TATA Capital) based on the evaluation.
- **Notes:**
    - The BRE applies lender-specific rules and approved lists.
    - Ensures that the user is matched with the most suitable lender.

---

### **5. KYC Verification**

**For Bajaj Finance:**

- **APIs Used:**
    - `GET /app/borrower/application/kyc/bajaj/init/{applicationId}`
    - `GET /app/borrower/application/kyc/bajaj/status/{applicationId}`
- **Partner:** Digilocker
- **Functionality:**
    - **Initiate KYC:** Starts the KYC process using Digilocker.
    - **Check Status:** Retrieves the status of the KYC verification.

**For TATA Capital:**

- **APIs Used:**
    - `GET /app/borrower/application/kyc/digio/init/{applicationId}`
    - `GET /app/borrower/application/kyc/digio/status/{applicationId}`
- **Partner:** Digio
- **Functionality:**
    - **Initiate KYC:** Starts the KYC process using Digio's Aadhaar-based verification.
    - **Check Status:** Retrieves the status of the KYC verification.
- **Notes:**
    - The KYC process varies depending on the assigned lender due to their internal policies.
    - Ensures compliance with regulatory requirements.

---

### **6. Bank Account Verification**

- **APIs Used:**
    - `POST /app/borrower/application/bav/add`
    - `POST /app/borrower/application/bav/verify`
    - `GET /app/borrower/application/bav/status/{applicationId}`
- **Partner:** Decentro
- **Functionality:**
    - **Add Bank Details:** Collects the user's bank account information.
    - **Verify Account:** Validates the bank account to ensure it belongs to the user.
    - **Check Verification Status:** Retrieves the current status of the verification process.
- **Notes:**
    - Critical for disbursing the loan amount.
    - Necessary for setting up repayment mechanisms.

---

### **7. Mandate Setting**

**For Bajaj Finance:**

- **APIs Used:**
    - `GET /app/borrower/application/mandate/digio/init/{applicationId}`
    - `GET /app/borrower/application/mandate/digio/status/{applicationId}`
- **Partner:** Digio
- **Functionality:**
    - **Initiate Mandate:** Starts the e-mandate setup process.
    - **Check Status:** Retrieves the status of the mandate setup.

**For TATA Capital:**

- **APIs Used:**
    - `POST /app/borrower/application/tata/mandate/link/`
    - `GET /app/borrower/application/tata/mandate/status/{applicationId}`
- **Partner:** TATA Capital's internal systems
- **Functionality:**
    - **Get Mandate Link:** Provides a link for the user to set up the e-mandate.
    - **Check Status:** Retrieves the status of the mandate setup.
- **Notes:**
    - Mandate setting authorizes automatic loan repayments from the user's bank account.
    - Different lenders use different systems for mandate setup.

---

### **8. Asset Pledge**

- **APIs Used:**
    - `POST /app/borrower/application/pledge/init`
    - `POST /app/borrower/application/pledge/create`
    - `POST /app/borrower/application/pledge/authPledge`
- **Partners:** Cams, KFintech, MF Central
- **Functionality:**
    - **Initiate Pledge:** Begins the process of pledging mutual fund assets.
    - **Create Pledge:** Submits a pledge request to the RTA (Registrar and Transfer Agent).
    - **Authenticate Pledge:** Verifies the pledge through an OTP sent to the user.
- **Notes:**
    - Pledged assets serve as collateral for the loan.
    - The value of the pledged assets affects the loan amount and terms.

---

### **9. KFS and Documentation**

- **APIs Used:**
    - `GET /app/borrower/application/review/kfs/init/{applicationId}`
    - `GET /app/borrower/application/review/kfs/link/{applicationId}`
    - `GET /app/borrower/application/review/kfs/status/{applicationId}`
    - `POST /app/borrower/application/review/kfs/accept`
- **Functionality:**
    - **Initiate KFS Review:** Prepares the Key Fact Statement (KFS) for the user.
    - **Provide KFS Link:** Offers a link for the user to access the KFS.
    - **Check KFS Status:** Monitors whether the user has reviewed and accepted the KFS.
    - **Accept KFS:** Records the user's acceptance of the KFS.
- **Notes:**
    - The KFS outlines the loan terms and conditions.
    - Reviewing and accepting the KFS is required for compliance and transparency.

---

### **10. Loan Agreement Execution**

- **APIs Used:**
    - `GET /app/borrower/application/agreement/link/{applicationId}`
    - `GET /app/borrower/application/agreement/status/{applicationId}`
    - **For e-Signature:**
        - `GET /app/borrower/application/signdesk/esign/init/{applicationId}`
- **Partners:** SignDesk (for e-signature)
- **Functionality:**
    - **Provide Agreement Link:** Supplies a link to the loan agreement document.
    - **Check Agreement Status:** Monitors the signing status of the agreement.
    - **Initiate e-Signature:** Starts the e-signing process through SignDesk.
- **Notes:**
    - Finalizes the loan process by creating a legally binding agreement.
    - e-Signatures expedite the process and are legally recognized.

---

### **Additional Considerations**

### **Error Handling and Status Checks**

- **Status Endpoints:** Many APIs have corresponding `/status` endpoints to check the progress of asynchronous operations.
- **Error Handling:** Proper error messages and handling mechanisms are in place to guide the user in case of issues.

### **Conditional Flows**

- **Lender-Specific Paths:** Depending on the assigned lender, certain steps like KYC verification and mandate setting follow different APIs and processes.
- **Dynamic Assignments:** The BRE may re-evaluate and reassign lenders if necessary based on updated information.

### **Security and Compliance**

- **Data Protection:** All APIs comply with data protection regulations to safeguard user information.
- **Regulatory Compliance:** Processes are designed to meet financial regulations, including KYC norms and loan documentation requirements.

---

### **Sequence Dependencies**

- **Sequential Flow:** Each step relies on the successful completion of previous steps.
    - **Example:** Bank account verification must be completed before mandate setting.
- **Interconnected Processes:** Data from one step is often used in subsequent steps.

---

### **Technical Integrations**

- **External Partners:**
    - **Decentro:** For PAN and bank account verification.
    - **Digio and SignDesk:** For KYC verification, e-mandate setup, and e-signature services.
    - **Cams, KFintech, MF Central:** For fetching folio and pledging assets.
- **Internal Systems:**
    - **Business Rule Engine (BRE):** Evaluates eligibility and assigns lenders.
    - **Secure Data Storage:** Handles sensitive documents and user data.

---

### **Summary**

The Volt Money application flow is designed to be seamless for the user while ensuring compliance and security. Each API plays a specific role in:

- **User Verification:** Ensuring the user is who they claim to be.
- **Asset Assessment:** Evaluating the user's financial assets for loan eligibility.
- **Regulatory Compliance:** Meeting all legal requirements for lending.
- **User Experience:** Providing a smooth and efficient application process.

---

**Feel free to reach out if you have any questions or need further clarification on any of these steps. Understanding this flow will be instrumental in managing product features, timelines, and aligning with our development efforts.**