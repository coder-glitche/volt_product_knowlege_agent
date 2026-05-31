# flow

**User Journey Map for a Loan Against Mutual Funds Application**

This user journey map outlines the steps a user goes through when applying for a loan against mutual funds (MF) using our platform. The journey is segmented into logical phases, incorporating both front-end (FE) interactions and back-end (BE) events. The map also considers different sourcing channels: B2C (Business-to-Consumer), B2B (Business-to-Business), and B2B2C (Business-to-Business-to-Consumer).

---

### **1. User Acquisition and Onboarding**

### **1.1. Launching the App**

- **FE Snippet:**
    - *Splash Screen > Launch App*

### **1.2. User Signup**

- **FE Snippets:**
    - *Signup > View Signup Page*
    - *Signup > Click T&C or Privacy Policy*
    - *Signup > Edit Phone Number*
    - *Signup > Navigate to OTP Page*
    - *Signup > Resend OTP*
    - *Signup > Enter Invalid OTP*
    - *Signup > Complete Signup*
    - *Signup > View Verify Email Page*
    - *Signup > Verify Email with Google*
    - *Signup > Verify Email with Other Method*
    - *Signup > View Enter Email Page*
    - *Signup > Email Verification Result*
- **BE Events:**
    - *Backend Events > OTP > Trigger OTP*
    - *Backend Events > OTP > Verify OTP*
    - *Backend Events > User Management > Create user context*
    - *Backend Events > User Management > Update user email*

---

### **2. Eligibility and Limit Check**

### **2.1. PAN Verification**

- **FE Snippets:**
    - *Cash Limit > Enter PAN*
    - *Cash Limit > Verify PAN*
    - *Cash Limit > PAN Verification*
    - *Cash Limit > Edit PAN Details*
    - *Cash Limit > Confirm PAN Details*
- **BE Events:**
    - *PAN Verification > Initiate PAN verification*
    - *PAN Verification > Complete PAN verification*
    - *PAN Verification > PAN verification failed*

### **2.2. Eligibility Check**

- **FE Snippets:**
    - *Cash Limit > Trigger Eligibility Check*
    - *Cash Limit > Eligibility Check Result*
    - *Cash Limit > Application Under Review*
    - *Cash Limit > Application Rejected*
- **BE Events:**
    - *Credit Application > Create credit application*
    - *Credit Approval Request > Receive credit approval request*
    - *Credit Approval Request > FAS creates the request*
    - *Credit Approval Request > LAN generation successful*
    - *Credit Approval Request > LAN generation failed*

---

### **3. Mutual Fund Portfolio Integration**

### **3.1. Linking MF Portfolio**

- **FE Snippets:**
    - *Cash Limit > View Check Limit Page*
    - *Cash Limit > Edit Details on Check Limit Sheet*
    - *Cash Limit > Update Portfolio Source*
    - *Cash Limit > Request MF Portfolio Details*
    - *Cash Limit > Resend OTP for Portfolio*
    - *Cash Limit > Portfolio OTP Result*
    - *Cash Limit > MF Portfolio Auth Result*
    - *Cash Limit > View Success Page*
    - *Cash Limit > Get More Portfolio*
- **BE Events (CAMS):**
    - *CAMS MF Fetch and Pledge > Request OTP for CAMS MF fetch*
    - *CAMS MF Fetch and Pledge > Trigger OTP for CAMS MF fetch*
    - *CAMS MF Fetch and Pledge > Request OTP verification for CAMS MF fetch*
    - *CAMS MF Fetch and Pledge > Successful OTP verification for CAMS MF fetch*
    - *CAMS MF Fetch and Pledge > OTP verification failed due to invalid entry*
    - *CAMS MF Fetch and Pledge > OTP verification failed due to expiration*
    - *CAMS MF Fetch and Pledge > OTP verification failed due to no portfolio*
- **BE Events (KFIN):**
    - *KFIN MF Fetch and Pledge > Request OTP for KFIN MF fetch*
    - *KFIN MF Fetch and Pledge > Trigger OTP for KFIN MF fetch*
    - *KFIN MF Fetch and Pledge > Request OTP verification for KFIN MF fetch*
    - *KFIN MF Fetch and Pledge > Successful OTP verification for KFIN MF fetch*
    - *KFIN MF Fetch and Pledge > OTP verification failed due to invalid entry*
    - *KFIN MF Fetch and Pledge > OTP verification failed due to expiration*
    - *KFIN MF Fetch and Pledge > OTP verification failed due to no portfolio*
    - *KFIN MF Fetch and Pledge > Pull bank account from KFIN MF fetch*

---

### **4. Unlocking and Setting Credit Limit**

### **4.1. Unlock Credit Limit**

- **FE Snippets:**
    - *Unlock Credit Limit > View Page*
    - *Unlock Credit Limit > View Portfolio*
    - *Unlock Credit Limit > Refresh Portfolio*
    - *Unlock Credit Limit > Continue to Set Limit*
    - *Unlock Credit Limit > View Set Credit Limit Tab*
    - *Unlock Credit Limit > View Interest Tab*
    - *Unlock Credit Limit > View Benefits Tab*
    - *Unlock Credit Limit > Set Credit Limit*

### **4.2. Set Credit Limit**

- **FE Snippets:**
    - *Set Credit Limit > View Set Credit Limit Page*
    - *Set Credit Limit > Edit Amount*
    - *Set Credit Limit > View Portfolio Selection*
    - *Set Credit Limit > Edit Fund Amount*
- **BE Events:**
    - *CAMS MF Fetch and Pledge > Request OTP for CAMS MF pledge*
    - *CAMS MF Fetch and Pledge > Trigger OTP for CAMS MF pledge*
    - *CAMS MF Fetch and Pledge > Request OTP verification for CAMS MF pledge*
    - *CAMS MF Fetch and Pledge > Successful OTP verification for CAMS MF pledge*
    - *CAMS MF Fetch and Pledge > OTP verification failed due to invalid entry*
    - *CAMS MF Fetch and Pledge > OTP verification failed due to expiration*
    - *CAMS MF Fetch and Pledge > OTP verification failed due to no portfolio*

---

### **5. Loan Summary and Pledge Confirmation**

- **FE Snippets:**
    - *Confirm Pledge > View Loan Summary*
    - *Confirm Pledge > View KFS (Key Fact Statement)*
    - *Confirm Pledge > Click FAQ*
    - *Confirm Pledge > Request OTP*
    - *Confirm Pledge > Resend OTP*
    - *Confirm Pledge > Verify OTP*
    - *Confirm Pledge > Pledge Success*
- **BE Events:**
    - *Backend Events > OTP > Trigger OTP*
    - *Backend Events > OTP > Verify OTP*

---

### **6. KYC Process**

### **6.1. Initiate KYC**

- **FE Snippets:**
    - *KYC > Start KYC Process*
    - *KYC > Start Application*
    - *KYC > View KYC Start Page*
    - *KYC > Proceed with Digilocker*
- **BE Events:**
    - *CKYC > Request CKYC*
    - *CKYC > CKYC search successful*
    - *CKYC > CKYC search failed*
    - *Digilocker KYC > Request Digilocker KYC*
    - *Digilocker KYC > Trigger OTP for mobile Digilocker KYC*
    - *Digilocker KYC > Successful OTP verification for Digilocker KYC*

### **6.2. Document Verification**

- **FE Snippets:**
    - *KYC > Name Match Result*
    - *KYC > Digilocker Verification Success*
    - *KYC > Confirm Additional Info*
    - *KYC > Confirm KYC Summary*
    - *KYC > Complete KYC*
- **BE Events:**
    - *KYC Additional Details > Request additional KYC details*
    - *KYC Additional Details > Additional KYC details successfully provided*
    - *KYC Summary > Request KYC summary*
    - *KYC Summary > KYC summary successfully generated*
    - *Manual Document Upload > Request manual document upload*
    - *Manual Document Upload > Manual document upload successful*

### **6.3. Eligibility Check**

- **FE Snippets:**
    - *KYC > Trigger Eligibility Check (Credit/AML)*
    - *KYC > Eligibility Check Result (Credit/AML)*
- **BE Events:**
    - *Application > Complete all steps of credit application*
    - *Credit Approval Request > Credit approval request approved by lender*

---

### **7. Agreements and Mandates**

### **7.1. E-Agreement Setup**

- **FE Snippets:**
    - *Agreement Flow > View Agreement Page*
    - *Agreement Flow > Receive Agreement Link*
    - *Agreement Flow > Review Agreement*
    - *Agreement Flow > Sign Agreement*
    - *Agreement Flow > Retry Agreement*
- **BE Events:**
    - *EAgreement Setup > Receive e-agreement setup link*
    - *EAgreement Setup > E-agreement setup received successfully via notification*
    - *EAgreement Setup > Request to regenerate e-agreement setup link*

### **7.2. E-Mandate Setup**

- **FE Snippets:**
    - *Autopay Flow > View Autopay Setup Page*
    - *Autopay Flow > Receive Autopay Link*
    - *Autopay Flow > Add Autopay Successfully*
    - *Autopay Flow > Proceed to Dashboard*
- **BE Events:**
    - *EMandate Setup > Receive e-mandate setup link*
    - *EMandate Setup > E-mandate setup received successfully via notification*
    - *EMandate Setup > Request to regenerate e-mandate setup link*

---

### **8. Bank Account Verification**

- **FE Snippets:**
    - *Bank Verification > View Verify Bank Page*
    - *Bank Verification > Add Bank Account*
    - *Bank Verification > Select Existing Account*
    - *Bank Verification > Verify Bank Details*
    - *Bank Verification > Bank Account Result*
    - *Bank Verification > Bank Name Match Result*
    - *Bank Verification > Add Another Bank*
- **BE Events:**
    - *Bank Account Verification > Pre-fetch available bank accounts*
    - *Bank Account Verification > Enter bank account details manually*
    - *Bank Account Verification > Request bank account verification*
    - *Bank Account Verification > Bank account verification successful*
    - *Bank Account Verification > Bank account verification failed due to name mismatch*

---

### **9. Selfie Capture and Application Submission**

- **FE Snippets:**
    - *Selfie Capture > Initiate Selfie Capture*
    - *Selfie Capture > Selfie Match Result*
    - *Selfie Capture > Retake Selfie*
    - *Selfie Capture > Submit Application*
- **BE Events:**
    - *Application > Complete all steps of credit application*

---

### **10. Loan Withdrawal**

- **FE Snippets:**
    - *Withdraw Amount > View Account Page*
    - *Withdraw Amount > Create Loan*
    - *Withdraw Amount > Confirm Withdrawal*
    - *Withdraw Amount > View Success Page*
    - *Withdraw Amount > Withdrawal OTP Result*
- **BE Events:**
    - *Backend Events > OTP > Trigger OTP*
    - *Backend Events > OTP > Verify OTP*
    - *Credit Line > Create credit line for application*

---

### **11. Account Management**

### **11.1. Transactions and Statements**

- **FE Snippets:**
    - *Transactions > View Transactions Page*
    - *Transactions > Email Statement*
    - *Transactions > View Email Statement Page*
    - *Transactions > Send Email Result*

### **11.2. Manage Credit Limit**

- **FE Snippets:**
    - *Manage Limit > Click Manage Limit*
    - *Manage Limit > View Manage Limit Page*
    - *Manage Limit > View Email Holding Statement*
    - *Manage Limit > Enhance Limit*
    - *Manage Limit > Margin Call*
    - *Manage Limit > Contact Us*

### **11.3. Contact Support**

- **FE Snippets:**
    - *Contact Us > Contact via WhatsApp*
    - *Contact Us > Contact via Call*
    - *Contact Us > Contact via Email*
    - *Header > Click Call Button*
    - *Header > Click WhatsApp Button*

### **11.4. Account Settings**

- **FE Snippets:**
    - *Account Management > Click Account Icon*
    - *Account Management > View Account Details Page*
    - *Account Management > Click About Us*
    - *Account Management > Click Flexi Pay*
    - *Account Management > Logout*

---

### **12. Repayment**

- **FE Snippets:**
    - *Repayment > View Repayment Page*
    - *Repayment > Make Online Payment*
    - *Repayment > Select Repayment Amount*
    - *Repayment > View Repayment Success Page*
    - *Repayment > Repayment Result*
- **BE Events:**
    - *Transactions > Update repayment status*
    - *Application > Update loan balance*

---

### **13. Joint Holder Flow (If Applicable)**

- **FE Snippets:**
    - *Joint Holder Flow > [All relevant joint holder interactions]*
- **BE Events:**
    - *Co-Borrower PAN Verification > Initiate co-borrower PAN verification*
    - *Co-Borrower PAN Verification > Complete co-borrower PAN verification*
    - *Co-Borrower PAN Verification > Co-borrower PAN verification failed*

---

### **14. Additional Document Upload (If Required)**

- **FE Snippets:**
    - *AS ES Additional Documents > [All relevant document upload interactions]*
- **BE Events:**
    - *Manual Document Upload > Request manual document upload*
    - *Manual Document Upload > Manual document upload successful*

---

### **Partner Journey Map**

For B2B and B2B2C channels, partners play a crucial role in user acquisition and loan facilitation.

### **1. Partner Signup**

- **FE Snippets:**
    - *Partner Signup > View Signup/Login Page*
    - *Partner Signup > Enter OTP*
    - *Partner Signup > Empanelment Success*
- **BE Events:**
    - *Backend Events > OTP > Trigger OTP*
    - *Backend Events > OTP > Verify OTP*
    - *User Management > Create user context*

### **2. Partner Dashboard and Lead Management**

- **FE Snippets:**
    - *Dashboard > View Dashboard Page*
    - *Dashboard > Click "Get It Now via WhatsApp"*
    - *Dashboard > Click "Know More" CTA*
    - *Dashboard > Click Assisted Journey CTA*
    - *Assisted Journey > Lead Creation*
    - *Dashboard > Click Share Unique Link CTA*
    - *Dashboard > Initiate Client Invitation*
    - *Leads > View Leads Page*
    - *Customers > View Customers Page*

### **3. Partner Referrals and Resources**

- **FE Snippets:**
    - *Partners > View Invite Partner Page*
    - *Dashboard > Initiate MFD Referral*
    - *Collateral > View Collateral Page*
    - *Collateral > Download Collateral*
    - *Collateral > Preview Collateral*
    - *Collateral > Download Presentation Material*
    - *Demo Video > View Demo Video Page*

### **4. Partner Account Management**

- **FE Snippets:**
    - *Account Details > View Account Details Page*
    - *Account Details > Edit Profile Success*
    - *Header > Click FAQ Button*
    - *Header > Contact via WhatsApp*
    - *Header > Contact via Call*
    - *Account Management > Logout*

### **5. Authentication and Security**

- **FE Snippets:**
    - *Authentication > Login with Password*
    - *Authentication > Set New Password*
    - *Authentication > Change Password*

---

**Note:** This user journey map integrates the provided front-end snippets and back-end events into a cohesive flow, illustrating the steps a user or partner takes when interacting with our loan application platform. It considers various sourcing channels (B2C, B2B, B2B2C) and includes conditional flows such as joint holder scenarios and additional document uploads.

---

By organizing the snippets into this logical sequence, we create a comprehensive map that can be used for development, testing, training, or presentation purposes. It ensures that every possible interaction is accounted for, enhancing user experience and operational efficiency.