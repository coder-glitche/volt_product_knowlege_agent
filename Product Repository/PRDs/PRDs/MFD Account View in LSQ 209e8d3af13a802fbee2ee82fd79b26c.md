# MFD Account View in LSQ

: Vijay Kumar S
Created time: June 5, 2025 4:40 PM
Status: In progress
Last edited: July 3, 2025 12:49 AM

# **What problem are we solving?**

Volt Money’s CRM (LeadSquared) is currently optimized for B2C workflows. However, the B2B2C sales channel relies on MFDs (Mutual Fund Distributors) to bring in retail loan customers. Since RMs (Relationship Managers) interact only with MFDs and not directly with end customers, the lead-level view is insufficient.

Key gaps include:

- No account (MFD)-level visibility
- Lack of pipeline tracking across referred leads
- No structure to capture relationship intelligence
- Inability to assess MFD performance, intent, or conversion potential
- Performance of Agents are affected as the leads are misplaced
- Misplacement of leads across RMs and poor lead-RM alignment
- Reduced productivity and conversion rates for RMs due to data fragmentation

---

# **How do we measure success?**

1. Adoption of account-level CRM by all active RMs within 2 weeks of launch.
2. 100% mapping of existing MFDs to new account view in LSQ.
3. Visibility of pipeline metrics at account level (number of leads, conversion %) for all MFDs.
4. Increase in RM productivity, measured by:
    - Increase in meaningful outbound interactions captured monthly.
    - Uplift in lead conversions from MFD referrals (MoM).
    - Reachout % of the MFD to increase ( Total MFD’s Connected)
    - Improve the MFD profiling and tiering
5. Reduction in lead misrouting issues.
6. Improved RM-MFD assignment logic, including referral and language-based logic.

---

# **What is the solution?**

Create a dual-layer CRM structure in LeadSquared (LSQ) that allows RM teams to operate with both:

- **Account-level visibility** (for MFDs)
- **Lead-level granularity** (for referred end-customers)

## Requirements overview :
BRD From sales:
[https://www.notion.so/volt-money/BRD-Account-Based-CRM-Revamp-for-Distributor-B2B2C-Sales-1fae8d3af13a8045a3c7c45e7eb39f83](https://www.notion.so/volt-money/BRD-Account-Based-CRM-Revamp-for-Distributor-B2B2C-Sales-1fae8d3af13a8045a3c7c45e7eb39f83)

PRD Shared with LSQ:
[https://docs.google.com/document/d/1i-qDDq0IcC9YunVrY08DOYcQnsFmfsMWd2iC9qYFrwI/edit?usp=sharing](https://docs.google.com/document/d/1i-qDDq0IcC9YunVrY08DOYcQnsFmfsMWd2iC9qYFrwI/edit?usp=sharing)

LSQ’s Current Functional Capabilities at the System Architecture Level:

| **Features** | **Lead** | **Opportunities** | **Account** | **Use Cases** |
| --- | --- | --- | --- | --- |
| Task Creation | Yes | Yes | No | Missed calls cannot be captured |
| Follow Up Mechanism | Yes | Yes | No | When a missed call is not captured the trigger cannot be created to trigger a follow up mechanism |
| Trigger for SLA's maintaining | Yes | Yes | No |  |
| Bulk Upload | Yes | Yes | Yes |  |
| Automations | Yes | Yes | Yes(Limited) |  |
| Activites | Yes | Yes | Yes (Customise activites as per our requirement) |  |

## User stories / User flow:

1. MFD Account is Created - Captures MFD details, RM owner, referral history.
    1. The MFD Account is created using the below 
        1. MFD Lead Form - Currently the data is not synced with the volt database 
        2. Bulk Upload - Currently the data is not synced with the volt database
        3. Referral link (Will be generated from volt DB)
    2. Minimum fields to be Fielded when bulk uploaded and filling the lead form :
        1. First Name
        2. Phone Number (Primary Key to dedupe)
        3. Email 
        4. Referred Name ( Can be auto fetched via Automations)
        5. Referred Phone Number (Mandatory to Assign the MFD’S)
        6. City
        7. Lead Type = “MFD”
2. Lead is Referred by MFD - Lead is linked to the MFD’s account object.
3. RM Reviews Account Page - Sees account-level dispositions, tier, referral pipeline and activity summaries.
4. RM Adds Outbound Disposition - Records intelligence (interest, preferences, bottlenecks).
5. Lead is Worked On - RM or backend team updates lead-level disposition (KYC, Offer Shared, Loan Approved).
6. Monthly Review - RMs review MFD-level conversion, call volume, and performance insights.

## Requirements:

Enable a dual-layer CRM setup in LSQ that:

- Adds an account-level view for MFDs.
- Migrates existing MFD data into new account format.
- Allows multi-opportunity tracking per MFD.
- Captures MFD employee contact details (e.g., Relationship Person, Sales Rep).
- Links all leads to respective MFD account for pipeline visibility.
- Displays a consolidated account-level dashboard.
- Captures dispositions at both lead and account levels.
- Supports monthly tracking of account dispositions.
- Maintains all existing lead-level automation/workflows.
- Allows custom account-tiering for performance segmentation (Bronze, Silver, Gold, Super Gold).

Account level view for MFD in the LSQ

Create the MFD as the account level view :

In the MFD account level view we have to create the heirachy of account and the lead

### **Account (MFD)  Page**

### **Account-Level Tabs & Views**

| Tab Name | Description |
| --- | --- |
| Overview 
(Account Details) | Snapshot of leads, products, conversions, active employees, and recent actions |
| Lead Details | Table of all leads linked to this MFD with key metrics, filters, and priority score |
| Employee View | Performance view for each employee (referral count, conversions, activity) |
| Month-on-Month | MoM table of activities (leads, calls, registration, conversion, product mix) |
| Dispositions | Monthly logged RM feedback, pipeline notes, and objections |
| Profiling | MFD preferences, typical lead pattern, common objections, RM insights |

### Fields to Included in Overview Account Details:

| Field | Description |
| --- | --- |
| MFD Name | Unique account (MFD) name |
| Tier | Bronze / Silver / Gold / Super Gold |
| RM Owner | Relationship Manager assigned |
| Last Call Date | Most recent call date |
| Total Leads Referred | Leads associated with the MFD |
| Conversion % | Total leads converted/ Total Leads |
| Active Products |  |
| Geography |  |
| Language preference |  |
| Last activity Date |  |
| Retain all the existing fields in the MFD leads |  |

**Lead Details Tab View:**

| Lead Id | Lead Stage | Lead Disposition | Hyperlink to detailed lead records | Customisable fields |
| --- | --- | --- | --- | --- |
| L001 | Loan Created | Summary remarks on lead pipeline | [www.google.com](http://www.google.com/) |  |
| L002 | KYC Pending | Summary remarks on lead pipeline | [www.google.com](http://www.google.com/) |  |

**Employee View Details Tab View:**

| Employee # | Employee Name | Total Leads Referred | AUM Referred | Converted Leads | Converted AUM | Phone number | Customisable fields |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E001 | ABC | 100 | 1.25 CR | 10 | 0.50 CR | 999999999 |  |
| E002 | DEF | 50 | 0.75 CR | 30 | 0.60 CR | 988776898 |  |

**Month on month tab View:**

| Month | Total Leads Referred | Converted | Outbound Disposition | Conversion % | Total Calls in this month |
| --- | --- | --- | --- | --- | --- |
| 2025-01 | 10 | 5 | RNR | 50% | 2 |
| E 001 | 5 | 3 |  | 60% | 1 |
| E 002 | 5 | 2 |  | 40% | 1 |

In addition to this tabs we need to be able to create a portion in the Overview which must have a profiling data highlighting in the top:
**Profiling will be a section in the Overview page:**

| Field | Description |
| --- | --- |
| MFD Name | Unique account (MFD) name |
| Tier | Bronze / Silver / Gold / Super Gold |
| RM Owner | Relationship Manager assigned |
| AUM | 50 CR |
| Total Leads Referred | 70 |
| Conversion % | Total leads converted/ Total Leads |

# Activities in the Accounts:

### Lead-Level Dispositions *(existing – retained)*

Captures status updates on individual leads (e.g., “KYC pending,” “Offer under discussion”).

### Account-Level Dispositions *(new – to be added)*

Two categories:

1. **Pipeline Dispositions**: Lead-level summaries from MFD point of view (e.g., “Client not interested,” “Docs awaited”).
2. **Outbound Dispositions**: Profiling data from RM’s regular outbound interactions (e.g., “Prefers xyz provider,” “Unaware of Volt process”).

Dispositions must be **addable per calendar month** to support continuous engagement tracking.

## **Data Model Updates**

### Entities to Be Created/Updated:

- **Account Object** → MFD entity with associated fields & disposition module
- **Lead Object Extension** → Include MFD linkage field
- **Disposition Logs** → Dual-layer (Account + Lead)
- **Assignment Rules** → Logic for language/referral-based RM assignment
- **Custom Reports/Dashboards** → RM performance, MFD performance, lead conversion

# Migration Plan:
1. Trail base:

1. 

---

## **Dependencies**

- LSQ technical team to enable custom account-level disposition logs
- Migration script for mapping historical MFD-lead relationships
- Training for RMs on usage of new views
- Updated assignment rules engine (language + referral logic)

---

## **Additional Requirements**

- The existing MFD must be migrated to the account-level view
- Lead activities and opportunities must be replicated for an account-level view.
- Dual dispositions must be available for the RM, where the disposition on an account level and the lead level inside the account view must be possible.

## User Flow:
[https://whimsical.com/accounts-journey-user-flow-A8kiJB63X3ogFRaKUAtc4D](https://whimsical.com/accounts-journey-user-flow-A8kiJB63X3ogFRaKUAtc4D)