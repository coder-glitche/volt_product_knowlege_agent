# LSQ Revamp

: Vijay Kumar S
Created time: July 8, 2025 11:39 AM
Status: In progress
Last edited: August 20, 2025 3:15 PM

[LSQ Swach ](LSQ%20Revamp/LSQ%20Swach%20239e8d3af13a80bd99dbf15d81b22452.md)

# **What problem are we solving?**

Currently, we have a **single flow** that combines both the **MFD activation journey** and the **customer LAMF journey**. This setup is causing several issues:

- Manage MFDs who have multiple applications/customers under them is a challenge
- Managing multiple products at a customer level is a challenge
- Confusion in workflow management
- Low visibility into which opportunity belongs to which journey
- Difficulty in segregating and tracking MFD vs customer-related progress
- **Since the phone number is used as the primary identifier, we cannot create separate applications for MFD and customer if they share the same number** — limiting our ability to split the journeys cleanly
- Overlap and conflict in automation triggers

To resolve this, we may need to structurally separate the journeys or opportunities to ensure better control, visibility, and scalability.

---

# **How do we measure success?**

We’ll consider this implementation successful if it achieves:

- No automation overlap across MFD and Customer journeys
- Clear visibility for sales (RMs) into journey + product context per opportunity
- Support for one lead progressing through multiple customer products
- Error-free MFD onboarding and follow-up flow for MFDs and Customers
- Ability to track and report performance separately by journey and product

---

# **How are others solving this problem?**

- **Industry best practice**: CRMs like Salesforce and Zoho use an opportunity-based model per product/journey while maintaining a single customer record (lead/contact).
- **LeadSquared limitation**: Native Account view is not built for operational control; most users avoid it when multiple workflows or automation rules are involved.
- **Typical workaround**: Use opportunity segmentation + lead tagging + automation filters to manage overlapping journeys without creating duplicate leads.

---

# **What is the solution?**

We will proceed with using **Leads and Opportunities**, rather than shifting to the **Lead and Account** view.

The key reasons for not adopting the Account view are:

1. **Task limitations** – Tasks cannot be created or managed in Accounts the same way they can be in Leads.
2. **View-only structure** – The Account view primarily serves as a dashboard to display associated leads, with limited operational functionality.
    - This same visibility can be replicated within the Lead view using additional connectors such as the **Custom Tabs Builder**, allowing us to achieve similar outcomes without shifting to the Account model.
3. **No follow-up workflows** – Accounts do not support activity logging or follow-up creation, which are essential for our engagement and tracking needs.

Given these constraints, Leads and Opportunities provide a more functional and scalable approach for our use case.

## ✅ Solution Overview

| Layer | Component | Purpose |
| --- | --- | --- |
| **Data Model Layer** | Lead Entity, Opportunity Entity | Decouple MFD and customer data |
| **Identity Layer** | Lead Type / Role Tag | Distinguish between MFD vs Customer |
| **Automation Layer** | Journey-based automations | Ensure no conflict between flows |
| **Presentation Layer** | UI segregation | Improve RM visibility |

## **Architecture-Level Requirements**

### 📦 Entity-Relationship Diagram (ERD)

**Entity wise Relationships:**

- **Lead ↔ Opportunity** (1:N): A single lead can have multiple opportunities
- **Opportunity ↔ Product** (1:1): Each opportunity is associated with one product
- **Lead ↔ RM** (N:1 or tagged): Multiple leads may be assigned to a single RM
- **Lead ↔ Activities/Tasks/Notes**: Standard engagement and tracking across the lifecycle

**Key Attributes per Entity:**

| Entity | Attributes |
| --- | --- |
| Lead | lead_id, phone, lead_type = MFD/Customer/(Both) |
| Opportunities | opp_id, lead_id, journey_type, product_type, status, created_at, RM_ID |
| Product List | Journey supported, product_id, product_name, valid_for_roles |

## 🎯 **Core Entity Model**

| Entity | Description |
| --- | --- |
| Lead | One per phone number |
| Journey | High-level type: MFD / Customer |
| Product | LAMF / LAS / Term Loan, etc. |
| Opportunities | One per Journey × Product combination |

> ✅ So, one Lead → multiple Journeys → multiple Opportunities
> 

### Opportunities Structure (1:N from Lead)

| opportunity_id | lead_id | journey_type | product_type | status |
| --- | --- | --- | --- | --- |
| 1001 | 12345 | MFD | null | Completed |
| 1002 | 12345 | Customer | LAMF | In-Process |
| 1003 | 12345 | Customer | LAS | Not Started |
| 1004 | 12345 | Customer | Term Loan | In Review |

## 🔁 Journey Type:

1. **MFD:**
    1. **MFD Onboarding Journey** → Unregistered → Registered → Empanelled → Partially Activated → Activated
2. **Customer:**
    1. **LAMF Journey** → MFC Limit Fetched → Portfolio fetched → KYC verification → Photo Verification → Link Bank Account → Mandate setup  → MF Pledge → Sign agreement → Loan Created

All Journey logic must be trigger based on:

If Lead_type =”Customer” and product_type - “LAMF” → Run LAMF journey

If Lead_type =”Customer” and product_type - “LAMF TL” → Run LAMF TL journey

If Lead_type =”MFD” → Run MFD Onboarding Journey

Each **Opportunity** contains fields that make it uniquely identifiable by:

- Journey type
- Product
- Status
- RM assigned

**Opportunity Handling Reframe:**

Each **opportunity** must have its own **distinct journey, set of activities, and automations**, configured specifically based on the **type of journey** it belongs to.

- For example, opportunities related to the **MFD onboarding journey** should have:
    - Their own defined onboarding stages and automation flows
        - Such as Registered, Unregistered, Empanelled, Partial Activation, Activation
    - Proper **assignment rules**, such as allocation to the **Pre-Activation** and **Post-Activation** teams at appropriate stages:
        - Stage in Registered or Unregsitered then assign to Pre Activation Group
        - Stage in Empanelled or Partially aActivated then assign to Post Activation Group.
        - Stage in Activated then Assign to MFD RM groups.
- In addition, all **Leads tagged as MFDs** must trigger an automation at the **Lead level**, which assigns the correct opportunity based on lead properties.
    - Example automation rule:
        - If a **Lead** has lead_type = customer and product = LAMF, then a **LAMF opportunity** must be created and linked to the lead.
- This activity (opportunity assignment) should be triggered via automation as soon as the lead is created or updated with relevant attributes.

### We will be needing multiple Opportunities such as :

1. MFD Onboarding Journey
2. MFD Journey
3. Customer - LAMF Journey
4. Enhancement - LAMF Journey 

# **MFD Activation Opportunities**

## 1. **Journey Stages:**

The MFD onboarding opportunity progresses through the following 5 stages:

1. **Unregistered**
2. **Registered**
3. **Empanelled**
4. **Partially Activated**
5. **Activated**

## 2. **Lead Input Sources:**

Leads entering the MFD onboarding journey can originate from:

- **Bulk Uploads → On bulk upload**
    - The phone number is mandatory and lead type = MFD then auto MFD onboarding opportunity must be created.
- **LSQ Forms : Similar to above logic a opportunity must be created.**
- **Referral-based journeys: We need to create a opportunity as the lead enters the lsq via automations**

## 3. **Activities in the MFD Onboarding Journey:**

### 1. **Outbound Calling - Integration between the LSQ and Exotel**

- **Activities:**
    - Conduct outbound calls
    - Add call disposition
    - Schedule follow-up calls
- **Required Features:**
    - Call dialler integration (manual/auto)
    - Customer form to capture Disposition capture with dropdown
        - **Disposition and Sub disposition is mandatory***
        - Disposition and Sub Disposition Required -
            - Interested:
                - Wants assisted Journey
                - Follow Up
                - Wants to negotiate for ROI
                - Mandate Issue at customer end
                - Unified Line Case
                - MFD - Customer not available
                - MFD - Awaiting Customer Approval
                - Customer KYC Pending
                - Customer Documents Pending
                - EBNA Referred Customer
            - Interested - Tech Issue:
                - Pledging Issue with CAMS/KFIN
                - Portfolio Fetch Issue
                - KYC Issue - Unable to share selfie link
                - KYC Issue - Aadhar OTP Issue
                - KYC Issue - Aadhar Phone not linked
                - Technical issue in Mandate(Tech)
                - Agreement not Generated
                - Incorrect name in agreement
                - Bank A/C verification issue
                - Blocked on Lender
                - Other Tech Issue
            - Not Interested:
                - Loan Taken from Elsewhere
                - High Interest rate
                - High PF
                - Low Eligible Loan Amount
                - Faced too many tech issues
                - Was just checking
                - Not a Customer
                - EBNA MFDs Customer
            - Not Eligible:
                - MFC Fetch less than CAMS & KFIN
                - Demat Portfolio
                - Age Diviations
                - ELSS Funds
                - Non Approved Funds
                - Minor Folio
            - RNR:
                - Not Reachable
                - Switch off
                - Did not pick the call
                - Wrong Number
            - Exisiting Customer:
                - Assistance for Existing Loan
                - Casually Checking
                - Line Enhancement
            - Already Loan Completed
                - Yes
                - No
    - Follow-up task creation with due date/reminder
    - Lead timeline to show call history

### 2. **Inbound Call Handling -  Integration between the LSQ and Exotel**

- **Activities:**
    - Should be able to pick up inbound calls
    - Log missed calls for follow-up
- **Required Features:**
    - Inbound call pop-up with lead details
    - Add disposition form with same dispositions and sub dispositions as outbound call
    - Missed call alert + auto task creation
    - Tag missed calls distinctly in timeline

### 3. **Follow-up Management**

- **Activities:**
    - Follow up on prior conversations
    - Nudge for pending actions
- **Required Features:**
    - Auto-reminder for scheduled follow-ups
    - Task prioritization based on status (e.g., delay >2 days)
    - Follow-up outcome logging

### 4. **Webinar Attendance Tracking**

- **Activities:**
    - Monitor if MFDs accessed onboarding content via web
- **Required Features:**
    - Webinar attendance webhook/API integration
    - Tag lead with attendance status (attended/not attended)
    - Auto-trigger next step based on attendance
        - If attended then set up a task for Follow up call
    

### 5. **UTM Interaction Tracking**

- **Activities:**
    - Understand source and medium of lead generation
    - Fields must be updated on adding the activity via api.
        - Campaign Source
        - Campaign Name
        - Campaign Medium
        - Campaign Id
        - Campaign Term
- **Required Features:**
    - UTM field mapping on lead creation
    - Timeline tagging for UTM events
    - Dashboard/report to analyze UTM performance by source/campaign

## 4. Tasks **in the MFD Onboarding Journey:**

1. Missed Call
2. Follow up 
3. Exotel - Inbound 

## 5. Lead Deatils **in the MFD Onboarding Journey:**

To be retained the existing lead details fields.

## 6. Lead Allocation logic **in the MFD Onboarding Journey:**

1. All leads generated via (Bulk Upload, LSQ Form and Referral journey) and lead type = MFD then they have to create a MFD On boarding Journey opportunities.
2. Post Opportunities creation:
- Lead Stage in Registered or Unregistered then assign to Pre Activation Group
- Lead Stage in Empanelled or Partially aActivated then assign to Post Activation Group.
- Lead Stage in Activated then Assign to MFD RM groups.

### **Migration Plan for Existing MFD Leads to the MFD Onboarding Journey**

1. Identify all leads in the current LSQ structure where:
    - `lead_type = MFD`, and
    - `lead_stage` is one of: **Unregistered**, **Registered**, **Empanelled**, or **Partial Activation**.
2. For each of these leads, create or migrate them into a **new Opportunity** under the **MFD Onboarding Journey** to ensure proper tracking and alignment with the updated flow.
3. The previous stage for each lead must be retained when migrated to the new opportunity as we would not like to lose the process made on the mfd for activating the lead.

---

## Why is two opportunities required for MFD?

### Two Opportunities Make Sense

| Opportunity Name | Purpose | Outcome / Closure Criteria |
| --- | --- | --- |
| **MFD Activation Journey** | To activate the MFD (Unregistered, Registered, Empanelled, Partial Activation, Activation) | MFD is activated and ready to use the Volt |
| **MFD Repeat Journey** | To track recurring activity from an already activated MFD (sharing leads) | MFD shares eligible leads again (repeat intent) |

**Reasons to go with separate opportunities:**

1. **Different Journey Types**: Activation and Repeat are functionally different journeys.
2. **Distinct Triggers and Automations**: Activation might involve document collection, onboarding steps, whereas Repeat may involve nudges, reminders, incentives.
3. **Independent Lifecycle**: One MFD can go through Activation once but Repeat multiple times.
    1. Use a naming convention to track versions (e.g., “Repeat #1”, “Repeat #2”)
    2. Auto-create a new Repeat Opportunity every time an MFD is idle for X days and gets re-nudged
4. **Cleaner Reporting**: You can better analyze drop-offs and performance separately for first-time vs repeat behaviour.
5. **Avoid Polluting Opportunity Stages**: Having one Opportunity with too many mixed stages (activation + repeat) will confuse RMs and make automation messy.

### Downsides of having one opportunities for MFD:

- Automations need complex logic to differentiate between activation vs repeat
- RM may miss re-engagement opportunities if the single Opportunity is marked "Closed – Activated"

# **MFD Repeat Journey Opportunities:**

### **Automation for Creating “MFD Journey Opportunities”**

- Whenever a lead has:
    - `lead_type = MFD`, and
    - `lead_stage = Activated`
    
    → A new **Opportunity** of type **“MFD Journey Opportunity”** must be **automatically created** with the status set to **Open**.
    
- Simultaneously, the **previous opportunity** under the **MFD Onboarding Journey** (if any) must be **automatically closed**.
- The newly created opportunity must be **assigned to the RM group** for further handling.

The Tabs required in the MFD journey opportunities are as follows:

1. MFD details
2. Activity history
3. Tasks
4. Leads Referred (Customer Tab required)
5. Sales Activity

## MFD Details Tab:

1. This tab must have complete details of the MFD such as 
    1. Partner Name
    2. Partner stage
    3. Partner tier
    4. Partner Primary phone number
    5. Partner email id
    6. Partner AUM
    7. Partner Client Base
    8. Partner ARN
    9. Partner referral link
    10. Partner referral code
    11. Platform
    12. Empanelment date
    13. Activation date
    14. City
    15. State
    16. Address
    17. Owner
    18. Created on
    19. Total Customer
2. A small tab containing:
    1. Total customers referred till date
    2. Total AUM referred
    3. Total employees referred

## 2. Activity History:

The list of activity to be added in this opportunity are mentioned as below:

1. Calls
    1. Outbound
    2. Inbound
    3. Missed Calls
2. Whatsapp messages (add only if required)
- Disposition will be added soon with respect to the opportunities (i will add it )
- The list of all the activities will be recorded here and all the automation activity will be added here similar to the lead currently how it is functioning

## 3.Tasks:

1. The list of tasks required here are :
    1. Missed Call
    2. Follow up 
    3. Exotel - Inbound 

## 4. Leads Referred:

In the leads referred tab we need a list of all the leads which are referred by the respective mfd.

the list of columns required for each leads are as follow:

1. Lead name (Hyper link)
2. Lead Stage
3. Phone number (Hyper link to call)
4. Owner
5. Modified on
6. Activity dates
7. Lead score
8. disposition custom (to be editable)
9. Last disposition added

## 5. Sales Activity tab:

### **Sales Activity Disposition Feature Requirement**

- In the **Sales Activity** tab, enable the ability to **add dispositions** directly from an **Activity** or **Customer Form**.
- This Sales Activity should support **only "Calling" activities**.
- Based on the inputs in the **custom form**, users should be able to:
    - **Add a Disposition**, with the following required fields:
        - **Total leads to be referred for the month**
        - **AUM to be referred for the month**
        - **Expected date of referral**
        - **Follow-up on the expected date**
- Upon submission, the system should:
    - Log the calling activity
    - Create and display the relevant **disposition view** for tracking and follow-up

In addition to the disposition we need the below mentioned table to track the performance of the MFD:
**Month on month View:**

| Month | Total Leads Referred | Converted | Outbound Disposition | Conversion % | Total Calls in this month | Promised Leads | Promised AUM (in CR) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-01 | 10 | 5 | RNR | 50% | 2 | 20 | 1.2 |
| 2025-02 | 5 | 3 |  | 60% | 1 | 10 | 0.75 |
| 2025-03 | 5 | 2 |  | 40% | 1 | 10 | 0.5 |

In addition to this tabs we need to be able to create a portion in the Overview which must have a profiling data highlighting in the top:

| **MFD Name** | **MFD Phone** | **Activation date** | **Tier** | **AUM** | **Outbound call priority score(Backend pushed)** | **Last call attempted date(Outbound)** | **Last outbound connected date** | **Last call connected date(Inbound+Outbound)** | **D-30 eligible leads** | **Not converted leads D-7** | **Not converted leads D-30** | **Not converted leads D-60** | **Cases committed in D-30** | **Converted in D-30** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | Should have connected with anyone in system for this |  | 10 | 20 | 30 | (disposition basis) |  |

## 6. Employees referred tab:

**Employee View Details Tab must contain the below mentioned data:**

| Employee # | Employee Name | Total Leads Referred | AUM Referred | Converted Leads | Converted AUM | Phone number | Customisable fields |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E001 | ABC | 100 | 1.25 CR | 10 | 0.50 CR | 999999999 |  |
| E002 | DEF | 50 | 0.75 CR | 30 | 0.60 CR | 988776898 |  |

# **Customer - LAMF Opportunities**

This opportunity must continue to be **linked with the existing LAMF opportunity** where the `lead_type = Customer`.

In this opportunities the journey of customers will be done.

**The opportunity will be used to complete journey of B2B, B2C AND B2B2C Customers LAMF Journey.**

### **Journey Flow:**

The stages in this opportunities are as follows:

**Stages —> Logic**

Portfolio fetch - MF fetched using MFC activity passed to LSQ

Credit offer page - Completes KYC and fetch and reaches the credit offer page

KYC Verification - KYC Verification completed

Verify Photo - Photo verification completed

Link Back Account - Link back account completed

Setup Mandate - Mandate setup completed

Portfolio Pledge - Portfolio pledge completed

Portfolio Pledge CAMS - MF pledge via CAMS Completed

Portfolio Pledge KFIN - MF pledge via KFINS Completed

Sign Agreement - Sign Agreement Completed

Credit Approval - Moved to Credit approval flow

Loan Created - Loan account created

We need to make the edits in the existing journey LAMF opportunities so this will support the LAMF customer journey well.

The activities and tasks to be retained as well.

1. Activities :
    1. Calling Activities
2. Tasks - Each tasks must have a custom form to add disposiitons and sub dispositions
    1. Missed Call
    2. Inbound calls
    3. Follow up
    4. Customer drop off
    
    ### **Tabs required in the Customer journey are as below:**
    
    1. Activity History - This must have activities like automations, API journey update 
    2. Sales Activity History - This must have the calling effort and dispositions history
        1. Call Logs with time stamp
        2. Disposition logs with timestamp
    3. Lead Details
    4. Tasks
    5. Notes

# **Enhancement - LAMF Opportunities**

### **Enhancement Journey Opportunity Creation**

- When a lead has:
    - `lead_type = Customer`, and
    - `lead_stage = Loan Created`,
    
    and a **new MFC fetch** is captured in the activity,
    

→ A **new opportunity** must be **automatically created** for the **Enhancement Journey**.

- This new opportunity will be used to manage and track the enhancement request.
- The **Enhancement Journey** flow will be TBD and shared soon.