# API Integration Changes for MFD Migration to LSQ Accounts

**Document: API Integration Changes for MFD Migration to LeadSquared Accounts**

## **1. Introduction & Goal**

This document outlines the necessary changes to the existing API integration between our internal systems (e.g., Redvision/Middleware) and LeadSquared (LSQ) to support the migration of Mutual Fund Distributors (MFDs) from the LSQ **Leads** module to the **Accounts** module.

The primary goal is to leverage LSQ's Accounts feature for better B2B relationship management of MFDs, separating them distinctly from end-customer leads while maintaining the ability to track their performance and associate customer activities/loans back to the correct MFD partner.

## **2. Current API Usage Summary (Pre-Migration)**

- **MFD Creation/Updates:** Using LSQ Lead APIs (Lead.Create, Lead.CreateOrUpdate, Lead Capture) to create/update MFDs as Lead records (Lead Type = MFD).
- **Customer Lead Creation:** Using LSQ Lead APIs or ULC Connector. MFD referrer information is likely stored in custom fields on the customer Lead record.
- **Opportunity Creation:** Using LSQ Opportunity APIs (Opportunity.Create), linked to the *customer Lead*.
- **Activity Logging:**
    - Using LSQ Activity APIs (Activity.CreateOnLead) or ULC to post activities (like status changes, performance metrics updates, PARTNER_... events) *directly onto the MFD Lead record*.
    - Customer-specific activities (loan creation, MFC check) are posted on the *customer Lead record*.

## **3. Required API Changes (Post-Migration)**

The core change involves shifting MFD record management from Lead APIs to Account APIs and adjusting how activities are logged and linked.

**3.1 MFD Creation**

- **Old Method:** Lead.Create / Lead.CreateOrUpdate / Lead Capture API.
- **New Method:** POST {{host}}CompanyManagement.svc/Company.Create or POST {{host}}CompanyManagement.svc/Company/Bulk/CreateOrUpdate
- **Changes Required:**
    - Replace API calls creating MFD Leads with calls to the Account creation endpoints.
    - **Payload Construction:**
        - CompanyType: Must specify the correct CompanyTypeName configured in LSQ for MFDs (e.g., "MFD Partners", "Distributors"). This needs to be set up in LSQ Account Settings first.
        - CompanyProperties: Provide an array of Attribute/Value pairs.
            - **Mandatory:** Attribute: "CompanyName", Value: [MFD's Name or Firm Name]
            - **Map Existing Lead Fields:** Map current MFD Lead fields (PAN, ARN, Partner Code, Type, Email, Phone*, etc.) to corresponding Account fields (default or custom cf_... schema names created during setup).
                - Example Pair: { "Attribute": "cf_arn_no", "Value": "ARN12345" }
                - Example Pair: { "Attribute": "EmailAddress", "Value": "mfd@example.com" }
                - Example Pair: { "Attribute": "cf_partner_code", "Value": "PARTNERXYZ" }
            - **Phone Number Handling (Redvision MFDs):** If the requirement is to *not* use the primary Phone field, map the phone number to a custom Account field (e.g., cf_alternate_phone) and ensure the Phone attribute is *not* sent or handled as per rules. For Volt MFDs, map to the standard Phone field if applicable.
    - **Event Trigger:** The PARTNER_ACCOUNT_CREATED event should now trigger this API call.

**3.2 MFD Updates**

- **Old Method:** Lead.Update / Lead.CreateOrUpdate / Lead Capture API.
- **New Method:** POST {{host}}CompanyManagement.svc/Company.Update?companyId=<string> or POST {{host}}CompanyManagement.svc/Company/Bulk/CreateOrUpdate
- **Changes Required:**
    - Replace API calls updating MFD Leads with calls to the Account update endpoints.
    - **Identification:**
        - For Company.Update, the LSQ companyId (obtained upon creation or via Get API) is required in the URL query parameter. This is the most reliable method.
        - For Company/Bulk/CreateOrUpdate, you can use SearchBy ("CompanyName", "CompanyNumber", "CompanyIdentifier", or a custom unique field schema name if configured) to find the account to update.
    - **Payload Construction:**
        - Similar to creation, provide CompanyProperties with Attribute/Value pairs for the fields being updated. Map fields correctly.
        - For Bulk endpoint, specify CompanyType, Options (SearchBy, CollisionResolutionStrategy), and Companies array.
    - **Event Trigger:** The PARTNER_ACCOUNT_UPDATED event (or specific field update events) should now trigger these API calls.

**3.3 Logging MFD-Specific Activities/Events (Lifecycle Stages, Referrals)**

- **Old Method:** Activity.CreateOnLead (posting on the MFD Lead).
- **New Method:** POST {{host}}CompanyActivity.svc/Create
- **Changes Required:**
    - Identify activities/events related *directly* to the MFD relationship or status (e.g., Stage Changes like "Empanelled", "Partially Activated", "Fully Activated", PARTNER_ACCOUNT_PARTNER_REFERRED, PARTNER_ACCOUNT_REFERRAL_DETAILS_UPDATED).
    - Modify the system triggering these events to call the CompanyActivity.Create endpoint.
    - **Payload Construction:**
        - RelatedCompanyId: The LSQ CompanyId of the MFD Account this activity belongs to.
        - ActivityEvent: The numeric ID of the corresponding **Account Custom Activity Type** configured in LSQ (e.g., an activity type named "MFD Stage Change" or "Partner Referred"). These *must* be created in LSQ first (Settings -> Accounts Customization -> Custom Activities & Scores).
        - ActivityNote (Optional): Any relevant notes.
        - Fields (Optional): Array of Attribute/Value pairs for custom fields defined *within that specific Account Activity Type*.
            - Example: To log a stage change: { "SchemaName": "cf_new_stage", "Value": "Empanelled" } (assuming cf_new_stage is a custom field on the "MFD Stage Change" account activity type).

**3.4 Customer Lead Creation & Linking**

- **Old Method:** Lead.Create / Lead.CreateOrUpdate / Lead Capture / ULC. MFD info likely in lead fields.
- **New Method:** Same Lead creation APIs, BUT **crucially adding the MFD Account Link**.
- **Changes Required:**
    - When a customer lead is created (triggered by PARTNER_CUSTOMER_LEAD_CREATED or other sources):
        1. Identify the referring MFD.
        2. **Lookup the MFD's LSQ CompanyId** (Account ID) based on the MFD's identifier (e.g., Partner Code, ARN). This might require an internal lookup or a call to CompanyManagement.svc/Company.Get if necessary.
        3. Modify the Lead.Create (or equivalent) API call payload for the *customer lead* to include an Attribute/Value pair for the **custom Lead lookup field** pointing to the Account.
            - Example: { "Attribute": "cf_mfd_account_id", "Value": "ACCOUNT_ID_OF_THE_MFD" } (assuming cf_mfd_account_id is the schema name of the lookup field created on the Lead object).
    - This linkage is **essential** for associating customer activities and performance back to the correct MFD Account.

**3.5 Logging Customer-Specific Activities (Linked to MFD)**

- **Old Method:** Activity.CreateOnLead (posting on the customer Lead).
- **New Method:** Activity.CreateOnLead (posting on the customer Lead). **No change in endpoint, but context is important.**
- **Changes Required:**
    - Events like PARTNER_CUSTOMER_LOAN_CREATED, PARTNER_CUSTOMER_BORROWER_ACCOUNT_CREATED, PARTNER_CUSTOMER_MFC_LIMIT_CHECK, PARTNER_CUSTOMER_CAMS/KFIN_ASSET_FETCH_STEP should continue to trigger Activity.CreateOnLead API calls targeting the **customer's Lead ID**.
    - **Verification:** Ensure the customer Lead record *has* the cf_mfd_account_id populated (as per step 3.4). This allows LSQ reports and potentially automations to associate this activity with the parent MFD Account.
    - **Payload:** The payload for these activities should contain data relevant to the *customer's* action/event.

**3.6 Opportunity Creation**

- **Old Method:** Opportunity.Create linked to customer Lead ID.
- **New Method:** Opportunity.Create linked to customer Lead ID.
- **Changes Required:** **No direct API change.** Ensure the ProspectId used in the API call correctly identifies the *customer Lead* ID. The opportunity will be implicitly linked to the MFD Account via the customer lead's cf_mfd_account_id field.

**4. API Endpoint Mapping Summary**

| Process | Old LSQ API Endpoint(s) | New LSQ API Endpoint(s) | Key Change |
| --- | --- | --- | --- |
| Create MFD | Lead Create/Update/Capture | CompanyManagement.svc/Company.Create | Target Account object, use Account fields, specify CompanyType |
| Update MFD | Lead Create/Update/Capture | CompanyManagement.svc/Company.Update | Target Account object, use companyId or SearchBy, map fields |
| Log MFD-Specific Activity | Activity.CreateOnLead (on MFD Lead) | CompanyActivity.svc/Create | Target Account Activity, use RelatedCompanyId, ActivityEvent ID |
| Create Customer Lead | Lead Create/Update/Capture | Lead Create/Update/Capture | **Add cf_mfd_account_id field populated with MFD's Account ID** |
| Log Customer-Specific Activity | Activity.CreateOnLead (on Customer Lead) | Activity.CreateOnLead (on Customer Lead) | No endpoint change, ensure customer Lead is linked to MFD Account |
| Create Customer Opportunity | Opportunity.Create (on Customer Lead) | Opportunity.Create (on Customer Lead) | No endpoint change, ensure customer Lead is linked to MFD Account |

**5. Prerequisites for API Changes**

- **LSQ Account Module Configured:**
    - Account Type created for MFDs (e.g., "MFD Partners"). Note the exact CompanyTypeName.
    - All necessary custom Account fields created (e.g., cf_pan, cf_arn_no, cf_partner_code, cf_empanelment_date, cf_alternate_phone, cf_original_lead_id). Note their **Schema Names**.
- **LSQ Account Activities Configured:**
    - Relevant Account Custom Activity Types created (e.g., "MFD Stage Change", "Partner Referred"). Note their numeric **ActivityEvent IDs**.
    - Any necessary custom fields within these activity types created. Note their **Schema Names**.
- **LSQ Lead Module Configured:**
    - A custom **Lookup** field (e.g., cf_mfd_account_id) created on the Lead object, configured to look up the MFD Account Type.

**6. Data Mapping & Event Handling**

- Thoroughly map all current MFD-related Lead fields to their corresponding target Account fields (default or custom).
- Re-map event triggers:
    - PARTNER_ACCOUNT_CREATED -> Company.Create
    - PARTNER_ACCOUNT_UPDATED -> Company.Update or CompanyActivity.Create (if update is logged as activity)
    - PARTNER_ACCOUNT_PARTNER_REFERRED -> CompanyActivity.Create (on referrer's Account)
    - PARTNER_CUSTOMER_LEAD_CREATED -> Lead.Create (for customer, ensure cf_mfd_account_id is set)
    - Other PARTNER_CUSTOMER_... events -> Activity.CreateOnLead (on customer lead)

**7. Recommendations**

- **Staging Environment:** Test all API changes thoroughly in a LeadSquared sandbox/staging environment before deploying to production.
- **Error Handling:** Implement robust error handling and logging for all API calls.
- **Idempotency:** Consider idempotency for create/update operations where feasible, especially for bulk operations.
- **Documentation:** Update internal API integration documentation to reflect these changes.
- **Coordination:** Coordinate closely between the middleware/Redvision development team and the LeadSquared admin/implementation team.

---