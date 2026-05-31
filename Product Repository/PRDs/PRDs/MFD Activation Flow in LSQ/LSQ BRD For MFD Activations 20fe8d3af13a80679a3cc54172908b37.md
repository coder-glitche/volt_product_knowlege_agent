# LSQ BRD For MFD Activations

# **What problem are we solving?**

Currently, MFD leads entering through multiple channels lack a unified onboarding and activation process. This results in:

- Productivity Loss
    - Data inconsistencies
    - Delayed activation due to a low follow-up mechanism
    - Fragmented visibility across different channels of leads
- The Activation Process is currently ad hoc and dependent on Google Sheets for tracking
- Enhance the follow-up mechanism

---

# **Proposed Solution and Approach**

**Problem Statement We Are Solving:**

- Lack of visibility into the status and progress of activation leads
- Inconsistent or poor follow-up on leads, leading to drop-offs
- Disjointed lead flows across multiple sources, causing inefficiencies
- Absence of automated alerts for timely handover to the Relationship Manager (RM), resulting in delays in activation steps

**Included:**

- Lead ingestion from multiple sources:
    - Website (Direct DB sync)
    - Event submissions (CSV Upload)
    - MFD referrals (via referral links)
    - LSQ Lead Forms
- Lead de-duplication and registration with key data verification (mobile, email)
- Partial and full activation workflows on LSQ
- Real-time status monitoring and automated handover alerts
- Tele-calling workflows
- Lead scoring based on UTM parameters

Implement an end-to-end automated flow for capturing, validating, registering, and activating MFD leads to ensure high data quality and operational efficiency.

## **Process Flow:**

### **Lead Entry Sources**

| **Source Type** | **Input Fields** | **Method** |
| --- | --- | --- |
| Website | Name, Mobile, Email, City, ARN, Company Name | Direct DB |
| Event Submissions | Name, Phone, Email, City, ARN, Event Date, Company Name | CSV Upload |
| MFD Referrals | Name, Phone, Email, ARN, City, Referral Details | LSQ Form Upload |
| LSQ Lead Form | Name, Mobile, Email, City, Company | LSQ Lead form |

### **The major missing steps in the activation journey in LSQ:**

1. The bulk upload is presently missing for the event and the marketing data that creates new leads using the dedupe logic.
2. The WhatsApp leads and MFD referrals are to be created using the quick MFD leads. The lead made in the LSQ is not flown back to the database.
3. Disposition is currently not being used for MFD profiling, and this data is not synced back to the database.
4. Group-wise allocation in the activation team (pre-empanelment team and post-empanelment team)
5. Follow up and lead servicing reminder for the respective lead owner.
6. Automated Handover trigger via WhatsApp group creation and MFD assignment on MFD activation.
7. MFD servicing and KT on the MFD dashboard scheduling within 24 hours of the activation with the respective RM.

# **Key System Actions:**

### **Lead De-duplication**

- Check for existing leads via phone number match
- Update existing lead status if found, else create new lead with status = Unregistered

### **MFD Lead Creation & Assignment**

- New leads assigned to activation agents via a round robin
- Agents must call within 24 hours and update the disposition
- Follow-up task auto-created if SLA missed

### **Lead Registration**

- OTP verification via SMS completed on the dashboard
- Successful verification updates lead to "Registered" in LSQ via API
- Mandatory fields: Name, Mobile, Verified Status, Email, ARN, City
- Additional profiling fields (via disposition): AUM, Total Customer base

### **Empanelment**

- Triggered post-registration
- Backend validation of ARN via API/manual check (TBD)
- Leads are assigned to the activation sales team via a round robin
- Calls and follow-ups with strict SLAs (24-hour call, 48-hour follow-up)
- Lead stage updated to "Empanelled"

### **Partial Activation**

- Triggered upon dashboard login and eligibility check (within 15/30 minutes)
- Lead stage updates to "Partially Activated"
- Opportunity auto-created and assigned to Post-Empanelment Sales Team
- Mandatory disposition capturing profiling data (AUM bracket, Customer base, Products sold)
- Data mapped to custom lead fields for segmentation and prioritisation

### **Full Activation**

- Completion of the agreement/onboarding journey
- Backend validation of agreement completion
- Lead stage updated to "Activated"

### **Automated Handover & Notifications**

- On activation, assign MFD to RM and create an opportunity with a call scheduled within 24 hours
- Enable dashboard access upon approval
- Trigger an automated email/SMS with login credentials
- Send webhook alert and WhatsApp group creation notification to the MFD team with RM's name
- **Referral-Based Routing**
    - If an **MFD is referred by another MFD**, assign the **same RM** as the **referring MFD**.
    - 🔁 *"Parent RM inheritance" to ensure continuity and better engagement.*
- **Language-Based Routing**
    - Assign based on the MFD’s preferred language:

| **Language** | **Assigned RM** |
| --- | --- |
| **Bengali** | Amrit |
| **Tamil, Telugu, Malayalam** | Lohit |
| **Kannada** | Swara |
| **Marathi** | Bhagyesh |
| **Other Languages** | Evenly distributed among other available RMs or RHs |
- *Fallback logic*: If no specific RM is mapped to a language, or capacity is full, rotate among other RMs with capacity.
- If both referral and language assignment fail (i.e., no RM match or capacity full):
    
    Implement **round-robin** or **capacity-based distribution** among general RMs/RHs.
    

---

## **Monitoring & Reporting**

**Real-Time Dashboard for Internal Stakeholders:**

- Funnel visualisation from Registered → Empanelled → Activated
- Filter by user, lead owner, source, city, region, campaign
- CSV export and daily summary email with follow-up reminders

| **Stage** | **Trigger** | **Owner** | **SLA** | **Output** |
| --- | --- | --- | --- | --- |
| Lead Ingestion | Web/Form/CSV/Referrals | System | Realtime | Lead created or updated |
| Registration | OTP Verification | Activation Agent | 24 hrs | Lead marked "Registered" |
| Empanelment | ARN Verified | Activation Team | 24 hrs | Lead marked "Empanelled" |
| Partial Activation | Dashboard Login | MFD + RM | N/A | Lead marked "Partially Activated" |
| Full Activation | Agreement signed | System + RM | 24 hrs | Lead marked "Activated" |
| Handover | Lead = Activated | System | 24 hrs | RM assigned + WhatsApp + Email/SMS |

## **Additional Activities and Automations for Activation Journey:**

- The UTM-based prioritisation is to be created
- Activities can include
    - Marketing UTM link click
        - Marketing at events
        - Marketing through a webinar
        - Marketing through referrals
- **CRM Automations**: For automating the tasks for creating a follow-up and lead stage update
- **Disposition-based Reminders:**
    - Post 48 hours after any lead disposition of interest must be shared an auto reminder to the lead owner.

## **Lead Prioritisation for Calling (Engagement & Activation)**

### **Objective:**

To convert registered leads to active customers through telephonic engagement.

### **Steps in Detail:**

1. **Trigger:**
    - Lead is marked as "Registered", "Empanelled", or "Partially Activated" based on the lead update api and on each lead update, and if there is no activity made within 2 hours and calling notification to alert RM must be created.
2. **Lead Prioritisation::**
    - **Scoring Inputs:**
        1. Source of lead (Website > Event > Bulk Upload)
        2. Time since lead creation
        3. Completeness of profile (ARN + Verified Email + Verified Mobile)
        4. Empanelment status
        5. Call outcome dispositions
        6. Agent feedback
    - **Scoring Logic (Without UTM activities):**
        1. **High Priority:** Empanelled + MFC Fetch + 2 hours → Route to top
        2. **Medium Priority:** Registered but not empanelled → Assigned within 24 hours
        3. **Low Priority:** Unregistered
3. **Call Dispositions (Mandatory):**
    - Lead Status Disposition (e.g., Interested, Not Interested, Callback)
    - Lead Profiling Disposition (e.g., Age, AUM Range, Experience)
4. **Follow-Up Handling:**
    - If a callback or additional time is requested, a follow-up schedule will be created\
    - The follow-up must be notified to the agent in the LSQ app at least 10 minutes before the follow-up time.
    - Until the activity call is logged, the notification must be shared with the RM.
5. **Outcome:**
    - Tracked and logged into the system for monitoring
    - Real-time updates reflected on dashboards
6. **Dashboard to monitor:**
- Priority group conversion rates
- SLA adherence
- Agent-wise lead performance

## **Activation Flow:**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcvolWZ1PAAT8ZZ4cP2d4eQBARIkcb8YLylLBnRAjV-mXLPExdQ9jFROMfYEsx2li-Snn6U-szRyubjvozowz2ZgsoyqHy9n9XazjJ3FivNRfx_0sBjsJ6kd6dBUNIv9WzXJgHUJA?key=si4mBLp53bRoRYW5Es55Rw)