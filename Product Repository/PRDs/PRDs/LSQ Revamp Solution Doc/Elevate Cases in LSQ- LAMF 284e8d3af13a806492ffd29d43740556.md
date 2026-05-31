# Elevate Cases in LSQ- LAMF:

### 1. **Purpose**

To define the business and system requirements for handling **Elevate Cases** in LeadSquared (LSQ).

Elevate Cases allow creation of a **new LAMF opportunity** for a borrower even if they already have an won LAMF opportunity with a different lender, enabling **parallel opportunities** under the same borrower account while keeping the opportunity name consistent.

### 2. **Background**

Currently, LSQ enforces a “one-active-opportunity-per-lender” rule for each customer, identified by phone number.

In *Elevate* scenarios, a borrower who has availed or is availing a LAMF loan from **Tata** or **Bajaj** may now seek a **new LAMF loan from DSP**.

The Elevate mechanism ensures:

- The **existing opportunity remains untouched**, and
- A **new parallel LAMF opportunity** is created for DSP, maintaining full visibility and independent tracking without renaming opportunities.

### 3. **Scope**

**In Scope**

- Creation of a **new LAMF opportunity** when an existing LAMF opportunity belongs to another lender.
- Detection and handling of duplicate opportunities via lender-based exception logic.
- Full journey and disposition tracking for both opportunities.
- Tagging and reporting visibility for all opportunities per borrower.

**Out of Scope**

- Changes to standard LAMF journey flow for non-elevate cases.
- Changes to lender onboarding or scoring logic.
- Non-LAMF product types.

### 4. **Trigger Condition for Elevate Case Creation**

An **Elevate Case** is triggered when **all** of the following are true:

1. **Existing Opportunity Check**
    - Opportunity Type = Loan Against Mutual Fund
    - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER
    - Lender = TATA or BAJAJ
    - Phone Number matches existing record (primary identifier)
    - Status = WON
2. **New Opportunity Request**
    - Opportunity Type = Loan Against Mutual Fund
    - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER
    - Lender =  DSP
    - Phone Number matches existing opportunity’s phone number
3. **Borrower Account ID Check**
    - Borrower Account ID ≠ Existing opportunity’s Borrower Account ID

If all conditions above are true → **flag as Elevate case** and create a new opportunity with the same name.

### 5. **Functional Requirements**

| **#** | **Requirement** | **Description** |  |
| --- | --- | --- | --- |
| 1 | Elevate Case Detection | System should detect when a new opportunity matches Elevate trigger conditions. |  |
| 2 | Parallel Opportunity Creation | Allow creation of a new LAMF opportunity for a different lender without overwriting existing opportunities. |  |
| 3 | Duplicate Detection Override | Modify duplicate detection logic to allow lender mismatch opportunities. |  |
| 4 | Elevate Tagging | Tag opportunities meeting elevate criteria with 
mx_Custom_75 = **Elevate** |  |
| 5 | Borrower Account ID Creation | Create a unique Borrower Account ID for each Elevate opportunity. |  |
| 6 | Reporting/ smart views | Dashboards must filter and display elevate opportunities distinctly. |  |

### 6. **Opportunity Creation Logic**

### **Trigger Check (Pre-conditions)**

An Elevate case is triggered when all conditions under Section 4 are met.

### **Step-by-Step Logic**

1. **Duplicate Detection Override**
    - Allow creation of a new opportunity if lender names differ even if the phone number matches in LSQ LAMF opportunity
2. **Tagging for Elevate Cases**
    - Field: **mx_Custom_75 = Elevate** or C**urrent Opportunity type = Elevate**
3. **Opportunity Creation**
    - Opportunity Name: CREDIT AGAINST SECURITIES BORROWER
    - Lender Name: DSP
    - Borrower Account ID: Newly generated ID
    - Copy borrower details from existing opportunity
    - Opportunity Status: Open
    - Opportunity Type: Loan Against Mutual Fund
4. **Journey Initialisation**
    - Start the standard LAMF journey.
    - Associate automations and dispositions to this opportunity.
5. **Audit Logging**
    - Log: Existing Opportunity ID, New Opportunity ID, Borrower Account IDs, Source Lender, Target Lender, Timestamp, RM/User who initiated creation.
6. **Reporting**
    - Dashboards to have filters for **current opportunity type = Elevate**

### 7. **Acceptance Criteria**

- Given a borrower with an active or won LAMF opportunity with Lender A, when an Elevate case is triggered for Lender B, a **new LAMF opportunity** is created without modifying the existing one.
- Opportunities are tagged with **current opportunity type = Elevate**
- Dashboards clearly identify elevate opportunities with lender and borrower account details.
- Borrower Account ID for Elevate cases is unique.

### 8. **KPIs & Success Metrics**

- % Elevate cases correctly flagged and created.
- Reduction in RM manual intervention.
- Accuracy of reporting on Elevate cases.

### 8. **Smart Views**

![image.png](Elevate%20Cases%20in%20LSQ-%20LAMF/image.png)

# Tushar POV

## What & when should flow into LSQ CRM?

| **Scenario** | **System Expectation** | Sales team expectation |
| --- | --- | --- |
| BFL Customer clicks on 9.99% Banner in App & checks the limit via that banner | Create opportunity in LSQ which is tagged as elevate.

Some signal need to be there that this user came via banner | Sales member will call the lead immediately & communicate.

B2C= opportunity gets assigned on round robin basis, but should be easily distiguishable so that the sales team can differentiate New vs Elevate one

B2B2C= MFD owner gets this lead assigned & this person has to add dispositions

B2B= elevate leads to be assigned in same logic as B2B current new leads are assigned |
| When a 2nd application ID is created of BFL client. As in current borrower of BFL fetched limit again. | Create opportunity in LSQ & which is tagged as elevate.

Signal needs to be there how the application ID was created, even if it was via admin action | Same as above |
| When nothing is created but MFD communicates that this customer will do & this customer wont do elevate | Not clear to me at least

Need to discuss with Vijay | For eg. Bhutra has 80 BFL customers. Now system will create opportunity only when customer does something or new application id is created. But the real game is to track & understand before customer initiates & thats where the real selling & convincing starts. Now my POV is that, RM should be able to know about all 80 clients of MFD, whether MFD has even spoken to them, what is client by client disposition, will they even move from BFL to DSP, if Yes, by when? |
|  |  |  |