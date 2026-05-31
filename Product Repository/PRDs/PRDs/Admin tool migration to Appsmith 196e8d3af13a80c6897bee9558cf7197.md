# Admin tool migration to Appsmith

: Ameya Aglawe
Created time: February 10, 2025 11:32 AM
Status: In progress
Last edited: April 14, 2025 2:14 PM

# **What problem are we solving?**

- The support and ops teams currently rely on two separate tools (admin tool & service dashboard) to handle customer queries and unblock the customer
- The admin tool requires extensive training since its actions are standalone, lacking context on their use cases, and limitations
- Access control, error handling, education, high effort

---

# **How do we measure success?**

- Reduction in queries related to admin actions
- Decrease in training time required for admin actions
- Improvement in TAT for executing an admin action

---

# **How are others solving this problem?**

---

# **What is the solution?**

---

### **Migration Plan**

- Admin actions will be migrated to Appsmith in phases. In Phase 1, we will move the top 15 most-used admin actions, which account for 96.5% of admin tool usage. [Usage patterns of admin action list can be found [here](https://docs.google.com/spreadsheets/d/1r4iaLdcfBNGC6NUzZXscfeJzfEO7A7PMNP6ClvPEBH4/edit?usp=sharing)]
- Each admin action will be categorised based on its use case:
    - **Bulk Actions**: Performed for multiple users/cases at once → Will remain standalone.
    - **User-Specific Actions**: Performed for an individual user → Will be integrated with the service dashboard.
- Access control details to be confirmed with Nishant.

### 1. Admin actions use-cases (Phase 1)

| Serial No. | Admin action  | Category  | User(s)  | Entry field | Validations | Use case  |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | TATA_COLLECTION_SETTLEMENT_RETRY | Bulk | Operations | - collection_id | - Not blank 
- Should be success_lender_recon_failed | Retrying the repayment posting in case TCL’s saveLoanReceipt API fails  |
| 2. | UPDATE_COLLECTION_STATUS | Bulk  | Operations | - collection_id | - Not blank 
- Should be success_lender_recon_failed, collection_complete, pending_settlement | Update the collection status of a repayment (majorly use cases to mark the repayment as settled if they are already posted in SOA even if the TCL’s saveLoanReceipt API fails)  |
| 3. | ENABLE_ENHANCE_LIMIT | User specific  | Sales | - PAN number  | - Not blank 
- should be linked to a borrower account  | Enable the “Pledge More” option for the BFL users (margin pledge) |
| 4. | CHANGE_LENDER_FOR_APPLICATION | User specific | Sales | - application_id
- new lender ID (not case sensitive)  | - Not blank 
- same lender check
- lender change to bajaj
- dedupe check
- Only to DSP allowed | Change the lender for the ongoing user application |
| 5. | UPDATE_BORROWER_PARTNER_RELATIONSHIP | User specific | Sales | - PAN number
-newPartnerAccountId | - Not blank 
- linked to a borrower account
- should have minimum one application
- new & existing parterAccountID should not be same | To link a customer to a particular MFD  |
| 6. | UPDATE_MANDATE_TYPE | User specific | Sales | - applicationId 
- Mandate type 
 | - Not blank 
- only for DSP
- if Digio Mandate should not be completed
- Application should be in progress
- Input should be API_MANDATE,PHYSICAL_MANDATE | To enable physical mandate in the DSP application flow  |
| 7. | SUSPEND_CREDIT_APPLICATION | User specific | Operations | - application ID | - Not blank 
- Application state should not be completed | To suspend an ongoing user loan application so that customer can either start a new application (if they dont wish to continue with application after pledging)  |
| 8. | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | User specific | Sales | - application ID 
- ISIN, value  | - Not blank 
- Not allowed for DSP 
- borrowerAccount must exist 
- ISIN is not present in the lender’s approved list 
- Current LTV should not be zero 
- LTV cannot be more than 5  |  Increase the limit (margin pledging or if MFD wants that they want 50%)  |
| 9. | REFRESH_CREDIT_INFO | User specific | Sales/Support/Operations | - PAN number  | - borrowerAcconut must be linked
- For DSP/BFL/TCL | Get the latest credit information by hitting the lender APIs (limit reflecting in holdings but not in app) |
| 10. | FORECLOSE_LOAN_ACCOUNT & APPROVE_REJECT_LOAN_FORECLOSURE | User specific | Operations | - PAN number 
- credit ID 
- radio button : approve, reject | - borrowerAccount must exist 
- credit must exist 
- Will throw error is linked foreclosure is not in terminal state
- Net payable should be > 0 
(if excess present than raise a disbursal request)
- credit should be in pending closure | Close loan account at Volt’s end if there is an issue with account opening at lender end |
| 11. | GRANT_PERMISSION | Bulk  | To confirm with Nishant | - mobile number  | - Not blank 
- user must be present in the system  | Grant permission to admin action to the team members  |
| 12. | CHANGE_EMAIL_MOBILE | User specific | Operations  | - borrowerAccountID
- Mobile number/email address | - Not blank
- There must be one application linked
-  mobile & email already exists  | Update email & mobile number in Volt system (for loan application flow only) |
| 13. | APPLICATION_RULE_OVERRIDE | User specific | Sales | - application ID 
- sanction limit 
- ROI  | - Not blank 
- borrower account must exist 
- Not allowed for DSP | Update the sanction limit for the loan application (will enable user to do margin pledging later) |
| 14. |  UPDATE_DISBURSAL_STATUS | Bulk/User specific  | Operations  | - disbursal ID 
- Button : settled, rejected | - disbursal ID should be blank 
- disbursal status should be in approved, queued, pending credit approval  | Update the disbursal status from QUEUED to REJECTED (terminal state) so that user can raise another disbursal request  |
| 15. | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | User specific | Operations  | - creditID
- bank account number, IFSC code | - Not null
- BorrowerAccount must exist 
- Credit must exist | Update bank account details in Volt system (for loan application flow only) |
| 16. | PROCESSING_FEE_OVERRIDE | User specific | Sales | - application ID
- newProcessingFees | - Not blank 
- If lender DSP & loan contract is complete then error (post KFS not allowed)
- For DSP override is allowed between 499 & 20000 | Update the processing fees for the loan application  |
| 17. | APPLICATION_ROI_OVERRIDE | User specific | Sales | - application ID 
- new ROI  | - Error if application is suspended or completed 
- For DSP if current step is loan contract then throw error 
- ROI should be 9.99 < ROI < 15 | Update the rate of interest for the loan application  |
| 18. | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | User specific | Sales | - application ID 
 | - Not blank 
- if asset pledge completed then throw error  | Skip KFIN pledging at pledge step  |

### 1a. User specific admin action flows

| Admin action | Change level | Additional validations | Flow |
| --- | --- | --- | --- |
| ENABLE_ENHANCE_LIMIT | Account level | - Disabled for DSP/TCL |  |
| CHANGE_LENDER_FOR_APPLICATION | Application level | - Disabled if asset_pledge step is complete
- Disabled if application state suspended/complete
- Only enabled for TCL applications | -  |
| UPDATE_BORROWER_PARTNER_RELATIONSHIP | Account level | -  | - Enter customers PAN
- Tap on edit button besides partner details option
- Pop up opens 
- Enter partner details 
- Tap on submit |
| UPDATE_MANDATE_TYPE | Application level | - Disable if the step is not digio_mandate
- Disabled if application state suspended/complete |  |
| SUSPEND_CREDIT_APPLICATION | Application level | - Disabled if application state suspended/complete |  |
| OVERRIDE_ISIN_LTV_BASED_ON_ISIN | Application level | - Disabled if application state suspended/complete
- Disabled if the current step is loan_contract, TATA_AGREEMENT

i.e If agreement step in_progress/completed then the admin action should be disabled |  |
| REFRESH_CREDIT_INFO | Credit level | Disable if credit status is closed |  |
| FORECLOSE_LOAN_ACCOUNT & APPROVE_REJECT_LOAN_FORECLOSURE | Credit level | - Disable if credit status is closed
- Disabled if foreclosure is not raised (for APPROVE_REJECT_LOAN_FORECLOSURE) |  |
| CHANGE_EMAIL_MOBILE | Account level | - Disabled if elevate case | - Enter customers PAN
- Tap on edit button besides contact details option
- Pop up opens 
- Enter email/mobile details 
- Tap on submit |
| UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | Account level | -  | - Enter customers PAN
- Tap on edit button besides bank details option
- Pop up opens 
- Enter bank details
- Tap on submit |
| PROCESSING_FEE_OVERRIDE | Application level | - disabled if current step is loan contract, agreement
- Disabled if application state suspended/complete |  |
| APPLICATION_ROI_OVERRIDE | Application level | - disabled if current step is loan contract, agreement
- Disabled if application state suspended/complete |  |
| APPLICATION_RULE_OVERRIDE | Application level  | - Disabled for DSP application (sanction limit cannot be updated for DSP)
- Disabled if application state suspended/complete |  |
| SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | Application level | - Disabled if application state suspended/complete
- Disabled if asset_pledge is complete |  |

### 1b. Bulk admin action flows

| Admin action | Additional validations |
| --- | --- |
| TATA_COLLECTION_SETTLEMENT_RETRY | - Only for lender TCL |
| UPDATE_COLLECTION_STATUS | - For BFL & TCL |
| GRANT_PERMISSION |  |
| UPDATE_DISBURSAL_STATUS |  |

### 2. Admin actions use-cases (Phase 2)

| S.no | Admin action  | Category  | User (s) | Entry field  | Existing validations | Use-case |
| --- | --- | --- | --- | --- | --- | --- |
| 1.  | APPROVE_PARTIAL_LIEN_REMOVAL | Bulk  | Ops | - Un-pledge request ID
- Approve/Reject | - Not null
- Request should be present against the ID
- Status should not be terminial
- Not allowed for DSP | - Update the status for lien removals |
| 2.  | FORECLOSURE_REMOVE_SECURITIES_RETRY | Bulk | Ops | - PAN  | - Not null check
- PAN should be linked to a borrowerAccount
- Active credit should be there
- Only for TCL  | - Retry TCL lien removals raised with foreclosure in case they get rejected |
| 3. | SHORTFALL_FILE_UPLOAD | Bulk | Ops | - Filename 
- File | - Not null
- Shortfall file not found in S3  | - Upload shortfall data file |
| 4.  | REVOKE_PERMISSION | Bulk | Tech | - Mobile number 
- Permissions | - Phone number should not be not null, starts with +91
- User should be present against that number & should be mapped to user persmission table
- Does not work on admin user | - Revoke admin action permissions from the user |
| 5.  | INTEREST_SHEET_UPLOAD | Bulk | Ops | - Filename 
- File | - Not null
- Interest file not found in S3  | - Upload interest data file |
| 6.  | PLATFORM_CHANGE_FOR_USER | User specific | Tech | - Mobile number 
- Platform code | - Not null
- User should be present
- platformCode shoud be present in platform_accounts table | - Change the partner platform of the user |
| 7.  | UPLOAD_MANDATE_SHEET | Bulk | Ops | - Filename 
- File | - Not null
- Mandate file not found in S3  | - Upload madate data file |
| 8.  | UPLOAD_BAJAJ_EOD_FILE | Bulk | Ops | - Filename 
- File | - Not null
- BFL EOD file not found in S3  | - Upload bajaj EOD data file |
| 9.  | CHANGE_PARTNER_PHONE_NUMBER | Bulk | Sales | - Current partner mobile number 
- New partner mobile number  | - Not null
- Partner should be linked to the number
- Partner exists for a phone number (check but not validation check) | - Update partners’ mobile number |
| 10.  | UPDATE_PARTNER_DETAILS | Bulk | Sales | - partnerAccountID
- partner name
- partner email 
- referring account | - Not null
- Partner account should be present for the account ID  | - Update partner’s name, email & referring account |
| 11.  | CREATE_OR_GET_DSP_APPLICATION | User specific | Sales, Support | - accountID | - Not null
- borrowerAccountID should be present in the system  | - Create a DSP application for an account |
| 12.  | CHANGE_PRIMARY_CREDIT_FOR_BORROWER_ACCOUNT | User specific | Sales, Support | - accountID, creditID | - Not null
- borrowerAccountID should be present in the system
- creditID should be linked to the borrowerAccountID | - Change primary credit ID for an account |
| 13.  | ENABLE_ENHANCED_LIMIT_AGREEMENT | User specific | Sales, Support | - applicationID | - Not null
- Not allowed for DSP
- borrowerAccount should be present | - Enable agreement for enhancement application  |
| 14.  | REPAYMENT_LINK_GENERATION | User specific | Support, Ops | - creditID | - Not null
- credit should be linked to a borrowerAccountID  | - Create a repayment link for a credit  |
| 15.  | GET_ALL_DOCUMENTS | User specific | Sales, Support | - applicationID | - Not null
 | - Fetch all the documents for an application |
| 16.  | UNIFY_MF_DATA_V2 | Bulk  | Sales | - primary applicationID
- secondary applicationID | - Both application should be present and linked to credits
- Primary should be in in-progress and secondary should be in-progress
- both the application should not be of TCL & DSP
- both the application should be of same lender
- borrowerAccountID of both the applications should be different | - Used for BFL line unification  |
| 17.  | ADD_ADMIN_USER | Bulk | Tech  | - mobile number  | - Not null
- borrowerAccount should be present  | - Add admin user for the admin tool  |

### 2a. User specific admin actions

| Admin action | Change level | Additional validations  |
| --- | --- | --- |
| PLATFORM_CHANGE_FOR_USER | Account level |  |
| CREATE_OR_GET_DSP_APPLICATION | Account level |  |
| CHANGE_PRIMARY_CREDIT_FOR_BORROWER_ACCOUNT | Account level |  |
| ENABLE_ENHANCED_LIMIT_AGREEMENT | Application level |  |
| GET_ALL_DOCUMENTS | Application level |  |
| REPAYMENT_LINK_GENERATION | Credit level |  |

### 2b. Bulk admin actions

| Admin actions  | Additional validations |
| --- | --- |
| APPROVE_PARTIAL_LIEN_REMOVAL |  |
| FORECLOSURE_REMOVE_SECURITIES_RETRY | - Add a check of a foreclosure request already being in progress |
| SHORTFALL_FILE_UPLOAD |  |
| REVOKE_PERMISSION |  |
| INTEREST_SHEET_UPLOAD |  |
| UPLOAD_MANDATE_SHEET |  |
| UPLOAD_BAJAJ_EOD_FILE |  |
| CHANGE_PARTNER_PHONE_NUMBER |  |
| UPDATE_PARTNER_DETAILS |  |
| UNIFY_MF_DATA_V2 |  |
| ADD_ADMIN_USER |  |

# **Design**

---

https://www.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-dump?node-id=13-291&p=f&t=oOsUj1PqMSBz5c0I-0

# **Analytics**

---

- Audit data from the admin tool should flow correctly.
- Each request should be associated with a `borrowerAccountId`.
- ApplicationId, CreditId, borrowerAccountId, disbursalId, collectionId, revocationId, foreclosureId should be mapped to the relevant admin actions

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