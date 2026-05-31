# MFD Activation Flow in LSQ

: Vijay Kumar S
Created time: May 26, 2025 6:25 PM
Status: In progress
Last edited: June 30, 2025 11:39 AM

# **What problem are we solving?**

Currently, MFD leads entering through multiple channels lack a unified onboarding and activation process. This results in:

- Productivity Loss
    - Data inconsistencies
    - Delayed activation due to low follow up mechanism
    - Fragmented visibility across different channel of leads
- Activation Process currently is adhoc and dependent on the Google sheets for tracking
- Enhance Follow up mechanism

---

# **How do we measure success?**

- **Lead Ingestion rate**
    
    Number of leads successfully ingested across all channels (website, Csv upload, Referrals, LSQ forms)
    
- **Lead Registration Rate**
    
    % of leads ingested that complete OTP verification and move to "Registered" status within 24 hours.
    
- **SLA Compliance for Calls & Follow-ups**
    
    % of leads contacted and disposition updated by activation agents within 24 hours.
    
- **Empanelment Conversion Rate**
    
    % of Registered leads successfully empanelled within 24–48 hours.
    
- **Activation Completion Rate**
    
    % of empanelled leads that complete full activation (agreement signed).
    
- **Automation & System Accuracy**
    
    % of automated handovers, alerts, and API syncs functioning without errors.
    

---

# Proposed Solution and Approach

**BRD :** [BRD Activation Sales to LSQ](https://www.notion.so/volt-money/Moving-activations-sales-to-LSQ-1fbe8d3af13a8077b410decb7ce88a24)

We are currently taking 2 phase approach to solve this issue:

PRD Shared with LSQ:

[https://docs.google.com/document/d/13q9AUGMdax29NBsOUsGaA58DrazYGETYyoYW1rrfawE/edit?usp=sharing](https://docs.google.com/document/d/13q9AUGMdax29NBsOUsGaA58DrazYGETYyoYW1rrfawE/edit?usp=sharing)

## LSQ’s Current Functional Capabilities at the System Architecture Level:

| **Features** | **Lead** | **Oppurtunities** | **Account** | **Use Cases** |
| --- | --- | --- | --- | --- |
| Task Creation | Yes | Yes | No | Missed calls cannot be captured |
| Follow Up Mechanism | Yes | Yes | No | When a missed call is not captured the trigger cannot be created to trigger a follow up mechanism |
| Trigger for SLA's maintaining | Yes | Yes | No |  |
| Bulk Upload | Yes | Yes | Yes |  |
| Automations | Yes | Yes | Yes(Limited) |  |
| Activities | Yes | Yes | Yes (Customise activites as per our requirement) |  |
| Import Bulk Leads | Yes | No (Bulk Update available) | Yes ( max 25000) |  |

## Phases

Below are the phases we are looking to go live with the accounts module.

- Phase 1:
- Phase 2:

### Phase 1 Scope

**Problem Statement We Are Solving:**

- Lack of visibility into the status and progress of activation leads
- Inconsistent or poor follow-up on leads, leading to drop-offs
- Disjointed lead flows across multiple sources, causing inefficiencies
    - Currently the leads bulk uploaded in LSQ is not synced with volt db
    - Currently the leads created using the lead form are not synced with volt db.
    - This creates a different funnels and no uniform data to track.
- Absence of automated alerts for timely handover to the Relationship Manager (RM), resulting in delays in activation steps
    - We currently do not have any task or automation in place to assign leads to RMs based on RM language, region, or referral logic post-activation. As a result, the assignment process is manual, which leads to delays.

**Included:**

- Lead ingestion from multiple sources:
    - Website (Direct DB sync)
    - Event submissions (CSV Upload)
    - MFD referrals (via referral links)
    - LSQ Lead Forms
- Lead de-duplication and registration with key data verification (mobile, email)
- Partial and full activation workflows on LSQ
- Real-time status monitoring and automated handover alerts:
    - **Automated Handover alerts:**
        - Automation: We currently do not have any task or automation in place to assign leads to RMs based on RM language, region, or referral logic post-activation. As a result, the assignment process is manual, which leads to delays.
        - Trigger : Stage = Activation
        - Parameters/fields to consider:
            - RM language - Lead language
            - RM region - Lead region
            - RM leads list - Lead referral
        - Once the automation is triggered, a follow-up task or reminder should be created for the RM to call the MFD (lead).
    - **Real - time status monitoring:**
        - Currently we do not have a out of box real time dashboard we have few reports. opening each report is not feasible to drive activations.
        - Enable a real-time or near real-time (updated every 15 minutes) dashboard in LeadSquared to track lead status across agents and teams. This dashboard will provide visibility into the activation funnel, enabling proactive strategy adjustments, performance tracking, and faster decision-making.
        - Objective:
            - Improve visibility into lead progression and bottlenecks.
            - Drive RM accountability through agent-wise and team-wise tracking.
            - Enable faster interventions to optimize activation rates.
            - Support data-driven decision-making with timely and actionable insights.
        - A centralised, dynamic view of lead statuses that helps drive RM actions, reduce delays in activation, and improve conversion efficiency.

**Excluded (Planned for future phases):**

- Tele-calling workflows
- Lead scoring based on UTM parameters

### Phase 1 Approach

Implement an end-to-end automated flow for capturing, validating, registering, and activating MFD leads to ensure high data quality and operational efficiency.

## **Process Flow:**

### **Lead Entry Sources:**

| **Source Type** | **Input Fields** | **Method** |
| --- | --- | --- |
| Website | Name, Mobile, Email, City, ARN, Company Name | Direct DB |
| Event Submissions | Name, Phone, Email, City, ARN, Event Date, Company Name | CSV Upload |
| MFD Referrals | Name, Phone, Email, ARN, City, Referral Details | LSQ Form Upload |
| LSQ Lead Form | Name, Mobile, Email, City, Company | LSQ Lead form |

### The major missing steps in the activation journey in LSQ:

1. The bulk upload is presently missing for the event and the marketing data that creates new leads using the dedupe logic.
2. The WhatsApp leads and MFD referrals are to be created using the quick MFD leads. The lead created in the LSQ is not flown back to the database.
3. Disposition currently is not been used for MFD profiling, and this data is not synced back to the database.
4. Group-wise allocation in the activation team (pre-empanelment team and post-empanelment team)
5. Follow up and lead servicing reminder for the respective lead owner.
6. Automated Handover trigger via WhatsApp group creation and MFD assignment on MFD activation.
7. MFD servicing and KT on the MFD dashboard scheduling within 24 hours of the activation with the respective RM.

# Key System Actions:

### Lead De-duplication

- Check for existing leads via phone number match
    - We have to create a sync to DB and try to create sanity between the two funnels
- Update existing lead status if found, else create new lead with status = Unregistered

### MFD Lead Creation & Assignment

- New leads assigned to activation agents via round robin
- Agents must call within 24 hours and update disposition
- Follow-up task auto-created if SLA missed

### Lead Registration

- OTP verification via SMS completed on dashboard
- Successful verification updates lead stage to "Registered" in LSQ via API
- Mandatory fields: Name, Mobile, Verified Status, Email, ARN, City
- Additional profiling fields (via disposition): AUM, Total Customer base

### Empanelment

- Triggered post-registration
- Backend validation of ARN via API/manual check (TBD)
- Leads assigned to activation sales team via round robin
- Calls and follow-ups with strict SLAs (24-hour call, 48-hour follow-up)
- Lead stage updated to "Empanelled"

### Partial Activation

- Triggered upon dashboard login and eligibility check (within 15/30 minutes)
- Lead stage updates to "Partially Activated"
- Opportunity auto-created and assigned to Post-Empanelment Sales Team
- Mandatory disposition capturing profiling data (AUM bracket, Customer base, Products sold)
- Data mapped to custom lead fields for segmentation and prioritization

### Full Activation

- Completion of agreement / onboarding journey
- Backend validation of agreement completion
- Lead stage updated to "Activated"

### Automated Handover & Notifications

- On activation, assign MFD to RM and create opportunity with call scheduled within 24 hours
- Enable dashboard access upon approval
- Trigger automated email/SMS with login credentials
- **Referral-Based Routing**
    - If an **MFD is referred by another MFD**, assign the **same RM** as the **referring MFD**.
    - 🔁 *"Parent RM inheritance" to ensure continuity and better engagement.*
- **Language-Based Routing**
    - Assign based on the MFD’s preferred language:
    
    | Language | Assigned RM |
    | --- | --- |
    | **Bengali** | Amrit |
    | **Tamil, Telugu, Malayalam** | Lohit |
    | **Kannada** | Swara |
    | **Marathi** | Bhagyesh |
    | **Other Languages** | Evenly distributed among other available RMs or RHs |
    
    *Fallback logic*: If no specific RM is mapped to a language, or capacity is full, rotate among other RMs with capacity.
    
    If both referral and language assignment fail (i.e., no RM match or capacity full):
    
    Implement **round-robin** or **capacity-based distribution** among general RMs/RHs.
    

---

## Monitoring & Reporting

**Real-Time Dashboard for Internal Stakeholders:**

- Funnel visualization from Registered → Empanelled → Activated
- Filter by user, lead owner, source, city, region, campaign
- CSV export and daily summary email with follow-up reminders

| **Stage** | **Trigger** | **Owner** | **SLA** | **Output** |
| --- | --- | --- | --- | --- |
| Lead Ingestion | Web/Form/CSV/Referrals | System | Realtime | Lead created or updated |
| Registration | OTP Verification | Activation Agent | 24 hrs | Lead marked "Registered" |
| Empanelment | ARN Verified | Activation Team | 24 hrs | Lead marked "Empanelled" |
| Partial Activation | Dashboard Login | MFD + RM | N/A | Lead marked "Partially Activated" |
| Full Activation | Agreement signed | System + RM | 24 hrs | Lead marked "Activated" |
| Handover | Lead = Activated | System | 24 hrs | RM assigned + WhatsApp + Email/SMS
**** |

## **UI/UX Screens**

| **Screen** | **Functionality** |
| --- | --- |
| Lead Intake Form | Data input → Website/Event referral |
| Bulk Upload Interface | File upload → Map columns → Submit |
| MFD Profile Page | Displays all lead data and current status |
| Empanelment Form | Bank Details, PAN Upload, Entity ID |
| Partial Activation Dashboard | Reminders for pending onboarding steps |
| Activation Panel | Upload KYC, give consent |
| Monitoring Dashboard | Status funnel, drop-off graph, team-wise breakdown |

## **Integrations**

- **LSQ API**: For status sync and lead updates
- **CRM Automations**: For automating the tasks for creating a follow-up and lead stage update

**Disposition-based Reminders:**

Post 48 hours after any lead disposition of interest must be shared an auto reminder to the lead owner.

## **Phase 2:**

## **Calling Flow (Engagement & Activation)**

### **Objective:**

To convert registered leads to active customers through telephonic engagement.

### **Steps in Detail:**

1. **Trigger:**
    - Lead is marked as "Registered", "Empanelled", or "Partially Activated"
2. **Lead Assignment:**
    - Based on availability, scoring, and load balancing
3. **Call Workflow:**
    - Agent receives lead with pre-filled data
    - Call is initiated with a guided script
4. **Call Dispositions (Mandatory):**
    - Lead Status Disposition (e.g., Interested, Not Interested, Callback)
    - Lead Profiling Disposition (e.g., Age, AUM Range, Experience)
5. **Follow-Up Handling:**
    - If a callback or additional time is requested, a follow-up schedule will be created
    - If lead converted, mark as "Activated"
6. **Outcome:**
    - Tracked and logged into the system for monitoring
    - Real-time updates reflected on dashboards

## **Lead Prioritisation (Scoring & Routing)**

### **Objective:**

To determine priority and route leads intelligently based on intent and completeness.

### **Scoring Inputs:**

- Source of lead (Website > Event > Bulk Upload)
- Time since lead creation
- Completeness of profile (ARN + Verified Email + Verified Mobile)
- Empanelment status
- Call outcome dispositions
- Agent feedback

### **Scoring Logic:**

- **High Priority:** Empanelled + Mobile verified → Route to top agents
- **Medium Priority:** Registered but not empanelled → Assigned within 24 hours
- **Low Priority:** Only email present, no mobile verification → Add to nurture pool

### **Assignment Logic:**

- Integrated with call centre tools or CRM
- The lead score prioritises the lead and defines follow-up SLAs

### **Monitoring:**

- Dashboard with:
    - Priority group conversion rates
    - SLA adherence
    - Agent-wise lead performance

## **User Flow:
Activation Journey:**
[https://whimsical.com/activation-Mx7vnkvjZPPbGUZF7AqzwE](https://whimsical.com/activation-Mx7vnkvjZPPbGUZF7AqzwE)

**Phase 1 - Activation Flow:**
[https://whimsical.com/phase-1-activation-flow-VaNFkDVugjt8MnRNfq9Mp1](https://whimsical.com/phase-1-activation-flow-VaNFkDVugjt8MnRNfq9Mp1)

## Addendum by Tushar

[Addendum on activations LSQ.pdf](MFD%20Activation%20Flow%20in%20LSQ/Addendum_on_activations_LSQ.pdf)

## **Leadsquared**

****

[LSQ BRD For MFD Activations](MFD%20Activation%20Flow%20in%20LSQ/LSQ%20BRD%20For%20MFD%20Activations%2020fe8d3af13a80679a3cc54172908b37.md)

---

## Analytics Requirements

### Leadsquared

1. Capture the LSQ data using the LSQ API to update the DB with new leads created using the LSQ forms
2. Final sign off on which database must be used to check for dedupe.

### Internal

---