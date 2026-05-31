# Volt: Mandate re-registration : Post loan

: Ranjan kumar Singh
Created time: July 23, 2025 4:08 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

In the current LOS journey, users are required to add their bank account and complete mandate registration as part of the loan application process. However, after the loan account is created, users may face situations where they need to re-register the mandate or update their bank account. These situations typically arise due to:

1. Initial mandate registration failure
2. Revocation of mandate by the user
3. User’s intention to change the previously added bank account (e.g., convenience, account freeze, operational issues) — applicable across all lending partners

At present, there is no UI-based option available to users post-loan to initiate mandate re-registration. This creates friction in the user experience and results in increased dependency on manual support processes.

### **Key Insights:**

- Approximately **600 users currently have no active mandate** linked to their loan account across all lenders.
- Around **300 users in DSP have no active mandate.**
- We receive **~33 monthly support requests** from users who wish to update their bank account and re-initiate mandate setup.

---

# **How do we measure success?**

- % of mandate re-registrations successfully completed via self-serve
- Reduction in Bank and mandate-related support tickets
- Improved collection success rate (post re-registration)
- Number of users re-registering via new flow
- Time taken from action initiation to mandate status = "Registered"

---

# **How are others solving this problem?**

---

# **What is the solution?**

- **Mandate and bank account details visibility:** On the account details page, show bank account information and mandate registration status (registered / not registered / pending).
- **Conditional Actions & Validations based on mandate status:**
    - If mandate is **registered**:
        - User can attempt to **add a new bank account (max 5 bank account is allowed to add from UI)** and **set up mandate** on the new account.
            - For both the lenders(DSP & TCL), Bank account for the disbursal and mandate should be always same.
            - Every time user try to setup mandate (switch mandate) on the bank account either new or old, bank verification using penny drop needs to be done for both DSP and TCL.
        - **Validation:** If the user **fails to add or verify the new bank account**, or if the **mandate setup on the new account fails or in progress**, the system **retains the previously registered bank account and mandate** as the active mandate for the loan.
        - User should receive clear feedback about failure reasons and be guided to retry or revert.
    - If mandate is **not registered** or **revoked**:
        - User can **set up mandate on existing bank account(bank needs to be verified)** or **add new bank account, verify bank and set up mandate**.
        - The system must validate that mandate registration completes successfully(UMRN number is received) before updating the active mandate.
        - If mandate setup fails, user remains on the previous state with no impact on loan processing until a mandate is successfully registered.
        - Volt system to maintain mandate registration status at bank level

## Requirements overview (optional)

## User stories / User flow

### **User Flow Summary:**

1. **User lands on the Account Details page.**
    - Bank account details and current mandate registration status (e.g., *Registered*, *Not-Registered*,) are clearly displayed.
2. **System dynamically shows context-aware actions based on the mandate status:**
    - If mandate is **not registered** → Show: *"Set Up Mandate"*
    - If mandate is **registered** → Show: *"Change Bank & Setup New Mandate"*
3. **User selects an action:**
    - **Re-register Mandate** (on the same account)
    - **Add New Bank Account & Setup Mandate**
4. **User completes the flow:**
    - Enters new bank details (if applicable)
    - Completes bank account verification
    - Proceeds with eMandate setup via API provider (e.g., Digio for DSP, TCL mandate)
5. **Post-action feedback is shown to the user:**
    - Successful registration → Updated status is shown in real-time
        - Communication is triggered on registered phone and Email id to confirm user about bank change, Add nudge: Report if not requested by customer.
    - Failure during mandate setup → Clear error message + option to retry
    - If the user drops off before completing mandate registration → Status remains “Incomplete”; option to retry
6. **Edge Case Handling:**
    - Bank account verification fails → Show validation error and allow retry
    - Mandate registration fails due to system/API issues → Show fallback guidance and allow user to retry
    - Mandate requested b/w 1st to 7th will queued at Volt End for DSP
    - Mandate requested b/w 1st to 3rd will queued at Volt End for TCL
    - BRE to manage the Mandate registration TAT

### User stories:

- **US1:** *As a customer, I want to view my bank account details and mandate registration status after loan activation, so that I’m aware of whether my mandate setup was successful or not.*
- **US2:** *As a user whose mandate was not registered successfully, I want to re-register the mandate on my existing bank account, so that EMI auto-debit can be initiated without any disruptions.*
- **US3:** *As a user who wants to switch bank accounts, I want the option to add a new bank account and set up a mandate on it, so that my EMI repayments can be managed through the preferred account.*
- **US4:** *As a user, I want clarity on whether only interest/charges will be auto-debited from my registered bank account, so that I can plan my balance and payments accordingly.*
- **US5:** *As a user with multiple bank accounts added, I want a clear indication of which account currently has an active mandate, so I can track and manage repayments easily.*
- **US6:** *As a user, I want clear on-screen guidance and feedback on my mandate registration status and what actions (if any) are required from me, to ensure smooth EMI processing.*

## Requirements

**Process to update bank and mandate for DSP:**

- Add bank account → penny drop → Complete mandate on same bank account → update bank and mandate both
    - Note: Bank and PAN name mismatch credit referral is out of scope and if threshold is less then 80% than we will show mismatch error to user as suggest to reach out to Volt support.
- If bank is verified and mandate is not success-full → Do not update bank

**Process to update bank and mandate for TCL:**

- Before penny drop, very bank from Bank master list using IFSC code and send bank code in client update API
    - Bank master list:
    
    [Bank Master_10412025120350.csv](Volt%20Mandate%20re-registration%20Post%20loan/Bank_Master_10412025120350.csv)
    
    ![Screenshot 2025-08-13 at 5.34.54 PM.png](Volt%20Mandate%20re-registration%20Post%20loan/Screenshot_2025-08-13_at_5.34.54_PM.png)
    
- Penny drop > Save mandate API > Verify mandate API
    - Generate report and push to WEB-TOP
    - Report format:
    
    [Document List.xlsx](Volt%20Mandate%20re-registration%20Post%20loan/Document_List.xlsx)
    
- Call clientMasterUpdate API to update the bank and to change the default bank
- Sample request:
    
    ```json
    curl --location 'https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/clientMasterUpdate' \
    --header 'Authorization: Basic dm9sdG1vbmV5cHJvZDp2b2x0bW9uZXlwcm9k' \
    --header 'ConversationID: 7214da30-01f8-405e-9672-9874cf21dfde' \
    --header 'SourceName: VoltMoney' \
    --header 'Content-Type: application/json' \
    --data-raw '[
    
    {
        "AadharCardNo": "XXXXXXXX8396",
        "Address1": "S/O,A Sarvabowma 8/82 Royapettah Royapettah",
        "Address2": "Royapettah Chennai Royapettah Hospital",
        "Address3": "Tamil Nadu India 600014",
        "BOCodeSecurity": "47097-291BZ8694024",
        "BorrowerIndustryID": "2",
        "BorrowerIndustryName": "Non face to face customers",
        "Category": "Individual",
        "CategoryCode": "1",
        "City": "Chennai",
        "ClientBankDetailsUpdate": [
        {
    
                    "Action": "Add",
                    
                    "BankId": "1453",
    
                    "BankName": "FEDERAL BANK",
    
                    "BankBranch": "Epifi Federal Neo Banking",
    
                    "MICR": "682049068",
    
                    "IFSC": "FDRL0005555",
    
                    "AccountNo": "55550100002730",
    
                    "FirstHolderName": "Athmakoori Nishant",
    
                    "AcctOpeningDt": "12-09-2018",
    
                    "DefaultAccount": "Yes",
    
                    "Accounttype": "Savings",
    
                    "BankDtl_CCY": "INR",
    
                    "PaymentMode": "Account/Fund Transfer",
    
                    "PaymentCode": "I",
    
                }
    
    ],
        "ClientBranchDetailsUpdate": [],
        "ClientBrokerDetailsUpdate": [],
        "ClientCreditCardUpdate": [],
        "ClientCreditFacilityUpdate": [],
        "ClientDPDetailsUpdate": [],
        "ClientGSTDetailsUpdate": [],
        "ClientIntroducerUpdate": [],
        "ClientKeyManagementPersonnelUpdate": [],
        "ClientPrimaryRMUpdate": [],
        "ClientRelatedCompaniesUpdate": [],
        "ClientSecondaryRMUpdate": [],
        "ClientSubBrokerDetailsUpdate": [],
        "CommenceOn": "2025-02-28",
        "CommonClientCode": "90001088",
        "Country": "India",
        "CountryID": "91",
        "DOB": "06-Jul-1995",
        "DefaultMailing": "Home",
        "Email": "ameya.aglawe@voltmoney.in",
        "Email_YesNo": "Yes",
        "FamilyID": "1298",
        "FamilyName": "LAS_DIGITAL",
        "FatherOrHusbandName": "Sarvabowma Athmakoori",
        "FirstName": "Athmakoori",
        "Gender": "Male",
        "GroupID": "1210",
        "GroupName": "LAS_DIGITAL",
        "HeadOfFamily": "No",
        "LastName": "Nishant",
        "LoanRequests": "Investments In Securities",
        "MaritalStatus": "unMarried",
        "MobileNo": "7418304754",
        "Nationality": "Indian Citizen",
        "OccupationCode": "7",
        "OtherDetails": [],
        "PinCode": "600014",
        "PoolAccount": "Yes",
        "State": "Tamil Nadu",
        "StateID": "38",
        "TaxIdOrPAN": "BQOPA5141D",
        "TaxPercent": "0",
        "TaxStatus": "Individual",
        "TaxStatusCode": "01",
        "UniqueRecordID": "90001088"
    }
       
    
    ]'
    ```
    

**Communication requirement:**

1. Mandate update is requested by user:
    
    ```
    Subject: Your mandate update request is being processed
    
    Hi {{customer_name}},
    
    We’ve received your request to update the mandate linked to your Volt Money account.
    
    Expected completion by: {{completion_date}}
    Bank Account: {{bank_name}} XXXX{{bank_last_4_digit}}
    
    Note:
    You can check the mandate status on the Volt Money app under Profile > Account Details.
    
    For any query, feedback or support, call us or whatsapp us at {contact_number}.
    
    Regards,
    Team Volt Money
    ```
    
2. Nudge user to register mandate for non mandate registered user
    
    Trigger: 25th of every month
    

```
Subject: Action Required: Register for Auto-Debit to Avoid Late Fees

Hi {{customer_name}},

We noticed that your auto-debit is not yet registered. This could lead to missed payments and late fees on your account.

Why register for auto-debit?
✔️ No missed payments—your dues are auto-debited on due date
✔️ Protect your credit score—build a strong payment history
✔️ Stress-free payments—no need to remember due dates

Setup auto-debit in just a few steps on the Volt Money app:

Open the app

Go to Account > Bank Details > Register Mandate

If you’ve already completed your registration, please ignore this message. You can always check your mandate status in the app.

For any query, feedback or support, call us or whatsapp us at {contact_number}.

Regards,
Team Volt Money

```

1. Feature announcement for customers: 
    
    Same as content mentioned in point 2, we will send 1 broadcast to customer when feature is live 
    
2. Feature announcement for MFDs:
    
    ```
    Subject: Auto-Debit Setup Now Available for DSP & TATA Customers on Volt Money App
    
    Dear {{partnername}},
    
    We’re excited to announce that customers with loans from DSP Finance and TATA Capital can now easily set up auto-debit directly from the Volt Money app.
    
    How it works:
    If a customer doesn’t have an active auto-debit mandate, they can quickly enable auto-debit on their existing bank account or add a new one—right from the app. The entire process takes less than 2 minutes and requires no paperwork.
    
    Key benefits:
    
    Never miss an EMI—payments are auto-deducted on the due date
    
    No risk of late fees or penalties
    
    Fast, secure, and fully digital process
    
    Next Steps:
    Encourage your clients to enable auto-debit through the Volt Money app to ensure smooth and timely EMI payments.
    
    For any questions or support, please reach out to your Volt relationship manager.
    
    Best regards,
    Team Volt Money
    
    ```
    

---

# **Design**

[https://www.figma.com/design/P6LkjMfxq3UFY2l3JHOIUW/Profile-section?node-id=1576-1879&t=YGEYbeRojqRg5Kwn-4](https://www.figma.com/design/P6LkjMfxq3UFY2l3JHOIUW/Profile-section?node-id=1576-1879&t=YGEYbeRojqRg5Kwn-4)

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

**Q: Will this impact existing mandate status?**

No. These changes apply only after loan creation and do **not modify** any existing registered mandates unless the user explicitly initiates a change.

**Q: Can users switch banks multiple times?**

Yes, users will have the flexibility to add and switch between multiple bank accounts. However, to minimize risk and ensure security, we will allow only **a limited number of bank accounts** to be added.

**Q: What happens if a user initiates the mandate flow but doesn’t complete it?**

We will track the incomplete status via Digio/TCL webhooks and implement reminder nudges after a defined timeout to prompt the user to complete the process.

**Q: What types of mandates are supported post-loan?**

Both **e-NACH(Digital,physical) and UPI-based mandates** will be supported for post-loan bank account updates.

Note: Validation to allow user to setup UPI mandate will

**Q: Will users be allowed to set up a physical mandate post-loan?**

For DSP - YES

For TATA - NO

**Q: Are we sending any communication to remind customer to register mandate if mandate is not registered?**

Yes, we will send reminder to customer to register the mandate to ensure the timely collection of due amount.

**Q: What will be the mandate registration amount?**

UPI: max 15000

eNach: 10L

**Q: When user are allowed to re-register the mandate and when not?**

**1. For mandate *registered* cases:**

Users should **not be allowed** to update or re-register the mandate once the bill is generated, as the lender schedules mandate presentation on the existing registered mandate during this period.

- **TCL:** Restriction period is from **1st to 3rd of every month And**
- **DSP:** Restriction period is from **1st to 7th of every month, Handle this at DSP end as well**

~~To avoid the confusion in scenario like user re-registered the mandate but mandate was presented on the previous registered mandate, we will inform them through appropriate communication that:~~

- **~~Mandate update may take up to 15 days~~**
- ~~They must **maintain sufficient balance in the both bank account** during this period to avoid bounce and penal charges~~
- ~~Volt will accept the mandate re-registration request but request will be in queue based on lender presentation date~~

**2. For mandate *not registered* cases:**

Users are allowed to register a new mandate at **any time**, as no existing mandate is active or scheduled for presentation.

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

- Mandate re-register with same bank
    - Reason:
        - Revoked by customer
        - Mandate not registered successfully
        - 
- Change bank account
    - Reason:
        - Convinice based
        - Account blocked/freezed
        - 
- TCL mandate
    - API: Client master update API- this is to update the registered bank account
        - Bank account number
        - IFSC
        - Bank ID: TCL has shared Bank master sheet, we need to use this to get the Bank Id by bank account number and IFSC combination
    - Mandate update: Use mandate API to create the mandate and upload to webtop