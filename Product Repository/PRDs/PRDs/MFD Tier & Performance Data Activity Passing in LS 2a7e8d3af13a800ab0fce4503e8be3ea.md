# MFD Tier & Performance Data Activity Passing in LSQ

: Vijay Kumar S
Created time: November 10, 2025 10:35 AM
Status: Pending Review
Last edited: November 10, 2025 6:43 PM

# **What problem are we solving?**

RMs lack a unified and actionable view of Mutual Fund Distributor (MFD) engagement, performance, and calling priorities within LSQ.

Current lead-level visibility doesn’t help RMs prioritise their outreach or track monthly conversion performance efficiently.

We are solving for:

- Fragmented data visibility (AUM, tier, last engagement, conversion, pipeline, MFD referred)
- Manual tracking of RM disposition and calling data via google sheets
- Lack of month-on-month visibility into MFD productivity and performance
- No structured, real-time reporting for RM calling effectiveness

**Goal:**

To improve RM productivity and enable better lead management and tracking through Smart Views, automated disposition tracking, and real-time performance reporting.

# **How do we measure success?**

| **Metric** | **Target** | **Measurement Source** |
| --- | --- | --- |
| Smart View adoption | ≥ 90% of active RMs using Smart Views |  |
| Tier-wise calling coverage | ≥ 80% MFDs called monthly | Outbound Calling Tracker |
| Data sync accuracy | ≥ 95% alignment between backend and LSQ | Backend vs LSQ reconciliation |
| RM productivity | +20% increase in connected calls per month | Daily Calling Tracker |
| Conversion improvement | +15% D-30 conversion rate improvement | Backend logic |

# Requirements overview:

We will create:

1. **Smart View** in LSQ showing key MFD performance and engagement data :
    1. MFD Activation team
    2. Repeat MFD Team. → RM & RH
2. **Custom Disposition Form** for RM & RH interactions
3. **Daily data sync** from backend to LSQ for AUM, Tier, and MFD referral data

## User stories / User flow:

- **RM View**
    - As an RM, I should be able to see all my MFDs in one Smart View with relevant columns (Tier, AUM, last call, conversion %, etc.) so that I can plan my daily outreach efficiently.
- **RM Interaction**
    - As an RM, when I log a call disposition via a custom form, the respective Smart View fields (last call date, conversion %, cases committed, etc.) should auto-update.
- **RM Monitoring**
    - As a Sales Manager, I should be able to view real-time RM calling performance and tier-wise connection rates via standard LSQ smart view.

### Existing Activity Mapping and Data Fields:

**Daily partner details update activity:**

- Currently via the Daily partner details update activity. We get the below mentioned parameters flowing to LSQ:
    - Total partner referral count
    - Total Application Completed count
    - Total Application pending count
    - Total pending basic details
    - Total pending asset fetch
    - Total pending KYC
    - Total pending bank verification
    - Total pending agreement
    - Total pending mandate
    - Status

## Additional parameters Required:

### **A. List of parameters Required:**

| **Column Name** | **Description** |
| --- | --- |
| MFD Name | MFD Full Name |
| MFD Phone | Registered number |
| Empanelment Date | MFD empanelment date (if empanelled) |
| Activation Date | MFD activation date (if activated) |
| MFD Tier | MFD tier classification (Super Gold / Gold / Silver / Bronze) |
| Referrer Tier | MFD referrer tier classification (Super Gold / Gold / Silver / Bronze) |
| AUM (Cr) | Total Assets Under Management in volt |
| Outbound Call Priority Score  | Backend-pushed calling priority score (To be added later once score is created) |
| D-30 Eligible Leads | Eligible leads in last 30 days (Referred customer ≥ 10000 eligible limit) |
| Converted Leads (D-7, D-15, D-30, D-60) | Converted leads by duration (separate parameter d-7,d-15,d-30 and d-60) |
| Not Converted Leads (D-7, D-15, D-30, D-60) | Not converted leads by duration (separate parameter d-7,d-15,d-30 and d-60) |
| Converted % in D-30 | Successfully converted leads/total eligible leads(d-30) |
- Fields auto-updated from backend + disposition responses

### **Data Sync / Refresh**

| **Data Type** | **Refresh Frequency** | **Source** |
| --- | --- | --- |
| AUM, Tier, Priority Score | Backend → LSQ | Daily once via API/Webhook |
| Disposition-based Updates | Real-time | LSQ form automation |

The data will be taken from the backend logic built by Akash.
The Tier can be fetching using the below mentioned sql query:

[Query for MFD tiering:](MFD%20Tier%20&%20Performance%20Data%20Activity%20Passing%20in%20LS/Query%20for%20MFD%20tiering%202a7e8d3af13a8036b28ccbf35e27ecdb.md)

From this MFD Tiering Query we directly get the details such as 

- **Partner name**
- **Partner Phone number**
- **Registered Date**
- **Empanelment Date**
- **Total no of completed applications**
- **Total Pledged credit limit = AUM**
- **Percentile completed cases**
- **Percentile pledged limit**
- **Tier → MFD Tier**

# **Data Flow & Architecture**

### **1. Backend to LSQ Data Push**

- A daily backend job (as part of the Partner Data Sync Service) will push updated **AUM**, **Tier**, **Referral Data**, and **Conversion Metrics** to LSQ via API or Webhook.
- LSQ custom fields will be created to store each parameter and will be used in Smart Views and reports.
- Any new MFD or updates to existing records will be upserted in LSQ based on the **MFD Phone Number** (unique key).

### **2. LSQ Smart View Configuration**

- Smart Views will be configured for each RM, filtered by the “Owner” field.
- Columns will include all backend parameters (AUM, Tier, Conversion %, D-30 Eligible, etc.) and disposition-linked fields (Last Call Date, Call Outcome, Next Action Date).
- Managers can create team-level Smart Views to monitor performance by tier, conversion, or engagement level.

### **3. Disposition Form Automation**

- A **call disposition form** will be configured in LSQ for RMs to capture:
    - Call Outcome (Connected / Not Connected / Interested / Not Interested / Follow-up / Converted)
    - Remarks
    - Next Follow-up Date
    - Number of Cases Committed (if any).
- Upon disposition form submission, the following LSQ fields will auto-update:
    - **Last Call Date**
    - **Last Disposition**
    - **Next Action Date**
    - **Conversion Count (if applicable)**

### **4. Reporting & Tracking**

- A **Smart View Dashboard** (available under Manage Views) will allow:
    - RM-wise and Tier-wise calling coverage
    - Conversion trends **(D-7, D-15, D-30, D-60)**
    - AUM growth over time
    - RM productivity metrics **(Calls made, Connected %, Conversion %)**
- Monthly reports can be exported or automated to Sales Managers.

## **Daily Partner Details Activity: Enhancement & Data Mapping Logic**

The **Daily Partner Details Update Activity** will act as the **single source of truth** for all MFD-related data updates in LSQ.

It will push updated performance, engagement, and referral metrics daily from the backend and automatically distribute the data between the **Lead** and **Opportunity** entities based on the MFD’s lifecycle stage.

Each MFD will have **only one Opportunity** of type **MFD Activation Journey.** This Opportunity represents the complete activation lifecycle for that MFD and remains the only opportunity that the Daily Partner Details Activity will ever update.

### **Lifecycle-Based Update Logic**

| **MFD Stage** | **Primary Data Target** | **Update Behaviour** | **Remarks** |
| --- | --- | --- | --- |
| **Before Opportunity is Won/Closed** | **Lead + MFD Activation Journey Opportunity** | The Daily Partner Details Activity will update both the **Lead** and the single **MFD Activation Journey Opportunity** linked to it. | Ensures the RM has full visibility of activation progress. Post activation |
| **After Opportunity is Won (MFD Activated)** | **Lead only** | Once the MFD Activation Journey Opportunity is marked as **Won**, the Opportunity stops receiving updates. All subsequent Daily Partner Details updates will be pushed only to the **Lead**. | Locks the Opportunity for accurate reporting. |

## **New Fields to Be Added in LSQ and Field Update Logic**

| **Field Name (Label in LSQ)** | **Description / Use** | **Source System** | **Backend Field / Logic** | **Update Frequency** | **Update Location** |
| --- | --- | --- | --- | --- | --- |
| **MFD Tier** | Classification of MFD based on percentile rank (Super Gold / Gold / Silver / Bronze) | Volt Backend | Derived from Tiering SQL (Partner percentile logic) | Daily | **Lead + Opportunity (until Won)** → Lead (post-Won) |
| **Referrer Tier** | Classification of MFD based on percentile rank (Super Gold / Gold / Silver / Bronze) | Volt Backend | Derived from Tiering SQL (Partner percentile logic) | Daily | **Lead + Opportunity (until Won)** → Lead (post-Won) |
| **AUM (Cr)** | Total assets under management with Volt | Volt Backend | Partner AUM aggregation logic (pledged credit limit) | Daily | Lead + Opportunity (until Won) → Lead (post-Won) |
| **D-30 Eligible Leads** | Count of eligible leads referred by MFD in last 30 days (eligible for conversion) | Volt Backend | Count of referred customers with eligible limit ≥ ₹10,000 | Daily | Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Not Converted Leads (D-7)** | Leads referred in last 7 days not yet converted (stage <> loan created) | Volt Backend | Filtered referral count by D-7 window
(D is today) | Daily | Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Not Converted Leads (D-15)** | Leads referred in last 15 days not yet converted | Volt Backend | Filtered referral count by D-15 window (D is today) | Daily | Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Not Converted Leads (D-30)** | Leads referred in last 30 days not yet converted | Volt Backend | Filtered referral count by D-30 window
(D is today) | Daily | Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Not Converted Leads (D-60)** | Leads referred in last 60 days not yet converted | Volt Backend | Filtered referral count by D-60 window
(D is today) | Daily | Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Converted Leads (D-30)** | Successfully converted leads in last 30 days | Volt Backend | Filtered referral count by D-30 window
(D is today) | Daily | Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Last Call Date** | Last date of RM interaction (from disposition form) | LSQ (Form Automation) | Captured via disposition submission | LSQ Automation | **Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Next Action Date** | Planned next follow-up date | LSQ (Form Automation) | Captured via disposition submission | LSQ Automation | **Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Call Outcome / Last Disposition** | Summary of last call outcome | LSQ (Form Automation) | Captured via disposition submission | LSQ Automation | **Lead + Opportunity (until Won)** → Lead (post-Won)** |
| **Conversion % (D-30)** | D-30 conversion = Total converted / Total eligible referred | Volt Backend | Filter for (Total converted / Total eligible referred) by 
D -30 | Daily | **Lead + Opportunity (until Won)** → Lead (post-Won)** |

### **Summary of Field Sources**

| **Source** | **Type of Data Provided** |
| --- | --- |
| **Volt Backend (Partner Data Sync Service)** | Tier, AUM, Referrals, Conversion %, Pending Stage Counts, Status |
| **Volt Backend (Tiering SQL Logic)** | Tier, AUM percentile logic |
| **LSQ Form Automation** | RM Disposition Data (Call Outcome, Last Call Date, Next Action) |
| **Conversion Logic** | D-30 conversion = Total converted / Total eligible referred |

### **Field Schema mapping in LSQ.**

Opportunity Schema in Sandbox are as below:

- MFD Tier → mx_Custom_95 → String
- Referrer Tier → mx_Custom_5 → String
- Total cases in T-30D → mx_custom_24 → Number
- Total cases in T-30D eligible → mx_custom_6 → Number
- Pending cases in T-30D eligible → mx_custom_7 → Number
- Total Partner referral Count → mx_custom_84 → Number
- Total Referred Leads → mx_custom_41 (all time referred) → Number
- Total application pending count → mx_custom_85(all time referred application pending) → Number
- Total Application completed count → mx_custom_49(all time referred application completed) →  Number
- Total Pending KYC → mx_Custom_87 → Number
- Total Pending Bank Verification → mx_custom_88 → Number
- Total Pending Mandate → mx_custom_51 → Number
- Total Pending Asset pledge → mx_custom_86 → Number
- Total Pending Agreement → mx_custom_89 → Number

### Summary:

| Section | What Changed |
| --- | --- |
| **Activity Logic** | Single Opportunity per MFD Activation Journey |
| **Fields Added** | 12 new backend + disposition fields |
| **Update Flow** | Daily push → Lead + Opportunity (till won) |
| **Ownership** | Query (Akash) + Backend Logic (Priyesh) |