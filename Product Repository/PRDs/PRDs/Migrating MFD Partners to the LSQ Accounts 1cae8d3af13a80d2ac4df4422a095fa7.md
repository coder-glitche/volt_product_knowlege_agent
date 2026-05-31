# Migrating MFD Partners to the LSQ Accounts

: Naman Agarwal
Created time: April 3, 2025 2:44 PM
Status: Ready for Tech
Last edited: May 27, 2025 2:25 PM

[**API Integration Changes for MFD Migration to LSQ Accounts**](Migrating%20MFD%20Partners%20to%20the%20LSQ%20Accounts/API%20Integration%20Changes%20for%20MFD%20Migration%20to%20LSQ%20A%201cae8d3af13a8009aa10eac1a34936f0.md)

- Accounts are now enabled for org: volt
- Reading LSQ documentation to understand and create a transition plan
- MFD is currently treated as lead and should be moved to accounts
- RMs will be assigned accounts and will be responsible for its success
- All the customer of a MFD will be under their account
- 

**1. Purpose & Goal:**

- **Current State:** Mutual Fund Distributors (MFDs) are currently managed as Leads within LeadSquared, identified by a specific Lead Type (e.g., "MFD"). This mixes partner data with end-customer data.
- **Desired State:** Migrate MFD entities to the dedicated **Accounts** module for better organization, relationship management, reporting, and utilization of B2B features. This clearly separates partners from end-customer leads.
- **Benefit:** Improved clarity, focused partner management workflows, ability to associate end-customer Leads under the correct MFD Account, and leverage specific Account-level features (stages, activities, ownership).

**3. Procedure:**

**Phase 1: Configure the Accounts Module for MFDs**

Setting up the Accounts entity for MFDs 

- **3.1 Identify Required MFD Fields:**
    - Review the current Lead fields list
    - List *all* fields containing essential MFD information that needs to be moved to the Account record. Examples:
        - PAN
        - ARN No
        - Referral Code / Partner Code
        - Partner Referral Link
        - Partner Type
        - Platform / Platform Id
        - Empanelment Date
        - Company (if used for MFD firm name)
        - Key contact details (Email, Mobile Number, Address, City, State, Zip Code)
        - Ownership (Owner)
        - Any other relevant custom fields.
- **3.2 Create Custom Account Fields:**
    - Adding all the Lead files to account
    - For every required MFD field *not* present by default in Accounts, create a custom field:
        - Navigate: My Profile -> Settings -> Accounts-> Account settings>Account type>Actions
        - Click **Add**.
        - Define:
            - **Display Name:**
            - **Schema Name:**  format cf_display_name.  custom field for easy reference
            - **Field Type:** Match
    - **Reference:** [https://help.leadsquared.com/account-settings/](https://help.leadsquared.com/account-settings/)
- 3.3 Add Drop-downs in fields like stage, etc.

**Phase 2: Migrate MFD Data from Leads to Accounts**

- **3.4 Extract MFD Leads:**
    - Manage leads
    - Use **Advanced Search**  Lead Type != MFD
    - **Manage Columns:** Add *all* source Lead fields identified in Step 3.1, **including the Lead Id (ProspectID)**.
    - **Export:** Select Actions -> Export Leads -> Export as CSV.
- **3.5 Prepare the Import File (CSV):**
    - Open the exported CSV.
    - **Clean Data:** Review for errors or inconsistencies.
    - **CRITICAL - Rename Columns:** Rename the CSV column headers to *exactly match the **Target Account Field Schema Names*** (including default fields like CompanyName, EmailAddress, Phone and your custom cf_... fields from Step 3.2).
    - **Map Data:**
        - Map Lead EmailAddress -> Account EmailAddress.
        - Map Lead Mobile -> Account Phone.
        - Decide CompanyName: Map Lead Company -> Account CompanyName OR combine Lead FirstName + LastName into the CompanyName column.
        - Map all other relevant Lead columns to their corresponding Account schema name columns (cf_pan, cf_arn_no, etc.).
        - Map Lead ProspectID -> Account cf_original_lead_id.
        - Map Lead OwnerId -> Account OwnerId (to retain ownership).
    - **Format Data:** Ensure dates, dropdown values, and checkbox values match the format/options expected by the Account fields.
    - **Save:** Save the prepared file as CSV.
- **3.6 Import MFDs into Accounts:**
    
    <aside>
    🚨
    
    This process is not yet straightforward, setting up time with Vijay LSQ on the same day on Tuesday (Vijay is on leave)
    
    </aside>
    
    - Navigate: Leads -> Manage Accounts (or the specific menu for your Account type if configured).
    - Click **Actions** -> **Import Accounts**.
    - Upload the prepared CSV file.
    - **Map Fields:** Carefully review the automatic mapping. Ensure every CSV column correctly maps to the intended Account field Schema Name. Manually correct any errors.
    - **Duplicate Handling:**
        - Select unique identifier(s) for checking duplicates (e.g., EmailAddress, cf_arn_no, cf_pan).
        - Choose a handling strategy:
            - Skip: Safest if unsure about existing partial Account data.
            - Overwrite: Updates existing matching Accounts (use cautiously, ensure unique ID is reliable).
            - Merge: Updates only blank fields.
        - **Recommendation:** Test with a small batch first. Overwrite based on a solid unique ID (like ARN or PAN) is often suitable for migration.
    - **Assign Owner:** If OwnerId was mapped, this should be handled. Otherwise, select a default owner.
    - **Start Import:** Monitor progress via import logs (Settings -> Data Management -> Import History).
    - **Reference:** How to Import Accounts Help Article

**Phase 3: Post-Migration Verification & Cleanup**

- **3.7 Verify Import:**
    - Check import logs for successes and failures. Investigate errors.
    - Go to **Manage Accounts**. Spot-check several newly created MFD Accounts. Verify all fields (especially custom ones) populated correctly. Compare counts (exported leads vs. imported accounts).
    - **Reference:** Manage Accounts & Account Details Help Articles (to navigate and view account data).
- **3.8 Clean Up MFD Records in Leads Module (Choose ONE):**
    - **Option A (Recommended): Mark as Migrated:**
        - Create a Lead Stage "Migrated to Account" or a custom checkbox field "Is Migrated".
        - Use the same Smart List/Search from Step 3.4.
        - Perform a **Bulk Update** on these Leads to set the Stage/Checkbox. Filters out MFDs from active Lead views while preserving history.
    - **Option B (Caution): Delete Migrated Leads:**
        - **Only after 100% verification.**
        - Use the Smart List/Search.
        - Perform **Bulk Delete**. *Warning: Permanent deletion. May impact historical reporting tied solely to the Lead record.*

**Phase 4: Link End-Customer Leads to MFD Accounts (Ongoing/Separate Process)**

- **3.9 Establish the Link:** Now that MFDs are Accounts, you need to link existing (and future) end-customer Leads to their respective MFD Account.
    - **Requirement:** Add a custom **Lookup** field (preferred) or Text field on the **Lead** object to store the MFD's Account ID. Let's call the schema name cf_mfd_account_id.
    - **Process for Existing Leads:**
        1. **Export MFD Accounts:** Go to Manage Accounts, filter for MFDs, export **Account ID** and a unique identifier (e.g., EmailAddress, cf_arn_no, cf_original_lead_id).
        2. **Export Customer Leads:** Export customer leads that need linking. Include the Lead ID and the field that identifies their MFD (e.g., Referrer Email, Referrer Name, or the cf_original_lead_id if the MFD was previously their owner/referrer lead).
        3. **Match Data (Excel/Sheets):** Use VLOOKUP/INDEX-MATCH to add the correct MFD Account ID from the Account export to each corresponding customer Lead row in the Lead export, matching via the common identifier.
        4. **Prepare Lead Update CSV:** Create a CSV with two columns: ProspectID (Lead ID) and cf_mfd_account_id.
        5. **Bulk Update Leads:** Use LeadSquared's **Bulk Update** feature for Leads, uploading this CSV to populate the MFD Account ID link.
    - **Process for New Leads:** Update your lead capture forms/processes/automations to populate the cf_mfd_account_id field when a lead is associated with an MFD.

**4. Updating Processes & Training:**

- **New MFDs:** All *new* MFD partners must now be created directly in the **Accounts** module.
- **Automations:** Review/update LeadSquared automations to differentiate between Leads and Accounts (MFDs). Create new automations triggered by Account events if needed.
- **Training:** Inform all relevant teams (Partner Management, Sales Ops, Support) about the change. Train them on finding, managing, and creating MFD records in the Accounts module.

API changes required 

---