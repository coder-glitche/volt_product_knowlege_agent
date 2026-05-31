# Support Requirement

## **Objective & Context**

Phase 1 aims to establish a **structured Internal Service Desk** within LeadSquared (LSQ) for Chat, Calling, and Operations teams.

This Service Desk enables internal teams to **log, assign, track, and resolve internal issues** with:

- Standardised ticket lifecycle
- SLA tracking & escalation
- Ownership & accountability
- Reporting & visibility
- Optional Jira escalation for Tech teams

This phase is **manual only (no external integrations)** and forms the foundation for future omnichannel Service Desk capabilities.

## **Problem Statement**

Today, internal issues are logged through scattered channels like WhatsApp, email, and direct calls. This results in:

- No centralised system for ticket creation and disposition capture
- No SLA enforcement
- Manual follow-ups and delays
- No visibility into ticket ageing or owner performance
- No audit trail of actions taken
- No structured categorisation for root-cause insights

A unified LSQ-based Internal Ticketing System will standardise 
**Ticket Creation → Ownership → Resolution → Closure**, ensuring **SLA adherence, accountability, transparency, and improved operational efficiency**.

## **Scope & Deliverables**

Build a structured internal ticketing system within LSQ that supports manual ticket creation, lifecycle tracking, SLA management, parent–child tickets, dashboards, and Tech escalations via Jira.

### **Key Deliverables**

1. **Ticket Schema**
    - L1–L3 categories
    - Priority & SLA mapping
    - Dispositions & RCA fields
2. **Ticket Creation Form**
    - Mandatory fields & validations
    - Customer verification checks
3. **Ticket Activities & Logs**
    - Comments, attachments
    - Status change audits
    - Ownership logs
4. **Assignment & Ownership Rules**
    - Manual owner assignment
    - Owner assignment Automations
5. **SLA Engine**
    - SLA start/stop/pause
    - Breach alerts
    - Escalation alerts to manager/superviours
6. **Parent–Child Ticket Model**
    - Parent ticket by Support team
    - Child ticket for Operations team.
    - Independent SLA for child tickets
7. **System Notifications**
    - SLA breach alerts
    - Assignment alerts
    - Resolution alerts
8. **Agent & Manager Views**
    - Smart Views
    - Ticket ageing dashboards
    - SLA compliance dashboards
9. **Reopen Logic**
    - New SLA cycle on reopen
    - Mandatory reason

### **In Scope**

- Manual ticket creation by Chat/Calling teams
- Parent–child ticket architecture
- Assignment, ownership, and SLA logic
- Disposition capture on resolution
- Agent & Manager dashboards
- Jira integration for Tech escalations
- Ticket activity logs
- SLA breach alerts & escalation rules

### **Out of Scope**

- Auto-ingestion via WhatsApp, Email, or Calls
- CSAT or survey automation
- Voice/Chat bot integrations
- Samadhan integrations

# **System Configuration (Foundation Setup Required in LSQ)**

This section defines all the core configurations required in LeadSquared Service Cloud to ensure consistent ticket handling, proper SLA tracking, accurate assignment, and standardized customer verification.

## **Business Hours Configuration**

- Business Hours define when SLA timers run.
- **Requirements**
    - Each Service Group must have its own business hours:
        - Chat Support: 9:00 AM – 9:00 PM (Mon–Sun)
        - Call Support: 9:00 AM – 9:00 PM (Mon–Sun)
        - Email Support: 10:00 AM – 7:00 PM (Mon–Fri), 10:00 AM – 6:30 PM (Sat)
        - Quality Team: Follows Call Support timings
    - SLA must pause outside business hours.
    - Business hours should be configurable at Service Group level in LSQ.
- **System Behaviour**
    - Response SLA and Resolution SLA should consider only working hours.
    - Parent ticket and child ticket should independently respect their designated business hours.

## **Holiday Calendar**

- The Holiday Calendar marks non-working days where SLAs should pause.
- **Requirements**
    - Create a central “Volt Service Desk Holiday Calendar” in LSQ.
    - Must apply to all service groups.
    - Include company-declared holidays + national holidays.
    - SLA timers pause automatically on holidays.
- **System Behaviour**
    - If a ticket is opened 1 day before a holiday, SLA must resume the next working day.

## **Assignment Rules**

- Assignment rules determine how tickets flow to the correct teams.
- **Requirements**
    - **Channel-Based Routing**

| Channel | Assign To | Service Group |
| --- | --- | --- |
| Chat | Agent | Chat Support Team |
| Email | Agent / Group Manager | Email Support Team |
| Inbound Call | Agent | Call Support Team |
| Quality (Monitoring) | Light Agent | Call Support Team |
- **Auto Assignment Rules**
    - Chat → Round-robin assignment across Chat Agents
    - Email → Round-robin for Agents; Group Manager receives escalations
    - Call → Round-robin across Call Agents
    - Child tickets created for Ops automatically route to Ops Service Group
    - Supervisor can override assignment
    - Supervisor can bulk assign or reassign tickets

## **Customer Verification Rules**

- Customer identity must be validated based on the channel and ticket type.
- **Primary Verification Variables**
    - Customer Phone Number
    - Email ID (for email-based cases)
- **Rules Per Channel**
    - **Chat Support**
        - Mandatory: Registered Phone number or email
    - **Call Support**
        - Mandatory: Registered Phone number or email
    - **Email Support**
        - Email auto-matched with CRM
        - Agent must request phone number if customer is not found in CRM

## **Notification Settings**

- Notifications ensure internal visibility on ticket movements.
- **Events for Notification trigger:**
    - Ticket creation
    - Assignment
    - Reassignment
    - Parent ↔ Child ticket assignment
    - Reopen event
    - SLA Reminder
    - SLA breach alerts
    - Escalation alerts
    - Pending RCA updates
- **Notification Delivery:**
    - In-app notifications (LSQ)
- **Recipients**
    - Assigned Agent → For assignment, reassignment, SLA Reminder and reopen event
    - Group Manager → SLA L1 Breach Alert
    - Supervisor → SLA L2 Breach Alert
    - Admin → Automation failure

## **Quick Replies → (WIP)**

- Predefined templates for standard responses.
- **Requirements**
    - Separate quick replies per Service Group
    - Categories:
        - General Updates
        - Document Requests
        - Lender Escalation Required
        - Ops Dependency
        - Follow-up Messages
        - Resolution Templates
    - Supervisor can create & manage quick replies
    - **Agents can use but cannot edit templates**

## Duplication Configurations

- Match Condition based on the associated Lead and ticket type

## **Ticket Lifecycle – Parent & Child Ticket Handling :**

- **Parent Ticket Lifecycle**
    - **Parent Ticket – Status Flow (High-Level)**
        - **Open**
        - **In Progress**
        - **Assigned to Ops** (Child ticket creation)
        - **Assigned to Tech** (Jira escalation)
        - **On Hold**
        - **Pending RCA**
        - **Resolved**
        - **Reopened**
    - **Parent Ticket – Detailed Lifecycle & SLA Mapping**

| Stage | Description | System Behaviour | Owner | SLA Status | Notes |
| --- | --- | --- | --- | --- | --- |
| **1. Open** | Ticket created by Support / CX / Chat / Calling. | Ticket ID generated, mandatory field validation. Status = Open. | Ticket Creator | SLA starts | Awaiting assignment. |
| **2. In Progress** | Work has started on the ticket. | Comments, internal notes, attachments captured. | Assigned Agent | SLA continues | Agent begins investigation. |
| **3. Assigned to Ops** | Ops dependency identified; child ticket created. | Child ticket auto-created. Parent shows “Assigned to Ops”. | Ops Team (Child Owner) | Parent SLA continues; Child SLA starts | Child ticket completely drives Ops SLA. |
| **4. Assigned to Tech** | Tech escalation via Jira./ external dependency. | Jira ticket created. Status & priority auto-synced. | Tech Team (via Jira) | SLA active | Parent continues until closure. |
| **5. Assigned to Product** | Jira ticket assigned to Product team. | Tech / Product (via Jira Sync) | Parent SLA Running
 | Jira integration updates LSQ status automatically | Same as “Tech Working” but specific label for Product category. |
| **6. On Hold** | Ticket pending customer input  | SLA clock paused. | Assigned Agent | SLA paused | Moves to On-Hold queue. |
| **7. Pending RCA** | RCA is not identified and documented. | Mandatory RCA field must be entered. | Assigned Agent | SLA active | Used when RCA is needed before closure. |
| **8. Resolved** | Final resolution provided. | SLA stops. Resolution notes mandatory. | Assigned Agent | SLA stops | Ticket moves to resolved state. |
| **9. Reopened** | Customer responds after closure or issue persists. | SLA restarts; reopen reason required. | Assigned Agent | SLA restarts | Treated as continuation of the parent ticket. |
- **Child Ticket Lifecycle**
    - **Child Ticket – Status Flow (High-Level)**
        - **Open**
        - **In Progress**
        - **Assigned to Tech** (Jira escalation)
        - **Blocked on Info**
        - **Pending RCA**
        - **Resolved**
        - **Reopened**
    - **Child Ticket – Detailed Lifecycle & SLA Mapping**

| Stage | Description | System Behaviour | Owner | SLA Status | Notes |
| --- | --- | --- | --- | --- | --- |
| **1. Open** | Child ticket created from parent. | Auto-generated with mapping to parent ticket. | Ops Team | SLA starts | Dependency work begins. |
| **2. In Progress** | Ops work initiated. | Notes, attachments, field updates allowed. | Ops Team | SLA continues | Standard processing. |
| **3. Forwarded to Lender Team** | Issue belongs to NBFC side (DSP Finance or other lender). | Volt Ops/automation | Parent SLA Running
Volt Ops SLA Stops
Lender SLA Starts | Create Zoho ticket (DSP) or Email (External NBFC) | Reference ID mandatory. |
| **4. Assigned to Tech** | Escalation to engineering (Jira). | Jira ticket creation & sync. | Tech Team | SLA active | Used when engineering involvement required. |
| **5. Blocked on Info** | Ops cannot proceed due to missing or incorrect information. | SLA pauses. Notification sent to parent ticket owner. | Parent Ticket Owner | SLA paused for child | Used when child ticket is blocked for more information |
| **6. Pending RCA** | RCA identified by Ops. | Mandatory RCA field. | Ops Team | SLA active | RCA stage before resolution. |
| **7. Resolved** | Ops completes required subtask. | Child SLA stops. Parent notified. | Ops Team | SLA stops | Parent returns to active state. |
| **8. Reopened** | Incomplete Ops work or new dependency. | SLA restarts. | Ops Team | SLA restarts | Treated as continuation of dependency. |
- **Relationship Between Parent & Child Tickets**
    - **Child Ticket Creation →** Created when Ops must perform a dependency task.
    - **When a Child is “Blocked on Info”**
        - This means:
            - Ops cannot continue.
            - Required information/details are missing.
            - Parent ticket owner must supply data or clarification.
        - System behaviour:
            - Child ticket → “Blocked on Info”
            - SLA (child) → Paused
            - Parent ticket owner receives alert
            - Parent ticket remains In Progress
        - SLA Behaviour
            - Parent ticket SLA continues until On Hold.
            - Child ticket SLA:
                - Runs normally during In Progress
                - Stops at Resolving
                - Pauses only during Blocked on Info

## **SLA Definition & Escalation Logic**

Tickets are categorised under **four priority levels**:

1. **Urgent**
2. **High**
3. **Medium**
4. **Low**

### **A major constraint on the SLA is that only one SLA can be triggered at a time. → Product constraint**
Based on the priority, we will be defining the SLA’s:

| **Priority** | **Definition** | First Response time | Next Response Time | **Resolution Time** | Reminder | **Escalation** |
| --- | --- | --- | --- | --- | --- | --- |
| **P1 – Urgent** | System-blocking issue (tech blocker, live process failure) | 15 min | 1 hour | 2 hours | - 10 min before FRT
- 20 min before Next Response
- 30 min before Resolution Time
 | Escalate to Ops Head / Tech Lead / Support Head |
| **P2 – High** | Major issue impacting multiple workflows | 30 hour | 4 hours | 12 hours | - 10 min before FRT
- 20 min before Next Response
- 30 min before Resolution Time | Escalate to Reporting manager |
| **P3 – Medium** | Single-issue or functional dependency | 2 hour | 8 hours | 1 business day | - 10 min before FRT
- 20 min before Next Response
- 30 min before Resolution Time | Escalate to Team Lead |
| **P4 – Low** | General request, service requests, documentation, or info query | 4 hour | 1 day | 2 business days | - 10 min before FRT
- 20 min before Next Response
- 30 min before Resolution Time | Escalate to TL post 48 hours |

## **Ticket Schema (Field-by-Field Table)**

| **#** | **Field Name** | **Description / Purpose** | **Field Type** | **Notes** | Mandatory |
| --- | --- | --- | --- | --- | --- |
| 1 | **Associated Lead** | Link customer by phone or email | Auto-lookup / Input | Auto-associates lead record | Y |
| 2 | **Requester** | Agent/manager creating the ticket | Auto-fill / Dropdown | Captures creator identity | Y |
| 3 | **Ticket Type** | Nature of issue | Dropdown | Incident / Service Request / Bug / Error / General | Y |
| 4 | **Tags** | Additional labels for filtering | Multi-select | Lender name / Issue type/ bulk issue | N |
| 5 | **Ticket Status** | Current lifecycle status | System dropdown | Open / In Progress / Assigned to Tech / Assigned to Ops / Resolved / Reopened | N |
| 6 | **Ticket Owner** | Current assignee | Dropdown (User list) | Determines SLA owner | N |
| 7 | **Product** | Product | Dropdown (Product) | LAMF / LAS / Term Loan (Default LAMF) | Y |
| 8 | **Priority** | SLA classification | Dropdown | Urgent / High / Medium / Low (Default Medium) | Y |
| 9 | **Ticket Subject** | One-line issue summary | Text |  | Y |
| 10 | **Channel** | Journey type | Dropdown | B2B / B2C / B2B2C | N |
| 11 | **Description** | Detailed explanation of issue | Text area |  | Y |
| 12 | **L1 Category** | Top-level classification | Dropdown | Pre-Loan / Post-Loan / enhancement | Y |
| 13 | **L2 Category** | Operational sub-category | Dropdown |  | Y |
| 14 | **L3 Category** | Granular RCA-level classification | Dropdown |  | n |
| 15 | **Attachments** | Supporting files/screenshots | File upload |  | N |
| 16 | **Jira ID** | Linked Jira ticket (if escalated) | Text / Auto-sync | Populated when escalated | N |
| 17 | **Lender** | Lending partner affected | Dropdown / Multi-select | Bajaj / Tata / DSP | Y |
| 18 | RCA | Gives the root cause analysis of the ticket | Text |  | N |

The objective is to ensure all important ticket information is captured, while also simplifying the form by limiting the number of fields.

# Mapping of L1 & L2 Category

| **L1 Category** | **L2 Category** | **L3 Category (To be defined)** |
| --- | --- | --- |
| Post-Loan | Lodgement issue |  |
|  | Details update |  |
|  | Document request |  |
|  | Document required by lender |  |
|  | Excess refund |  |
|  | Foreclosure |  |
|  | Interest / Charge dispute |  |
|  | Lien removal |  |
|  | Limit incorrect / not updated |  |
|  | Renewal |  |
|  | Repayment issue |  |
|  | Sell-off request |  |
|  | Withdrawal issue |  |
| Pre-Loan | Bank account / mandate | * Change bank account after mandate
*Mandate completed - error on screen
* Mandate completed - still on mandate step
* Mandate screen not opening
* Mandate screen opened - error on screen
* Penny drop failing
* Request for mandate link
* Unable to add IFSC
*Unable to upload supporting doc |
|  | Blocked at check eligibility | * Blocked at check eligibility |
|  | Co-applicant KYC | * Additional details issue
* Selfie issue |
|  | Credit referral |  |
|  | Customer doesn't want to continue |  |
|  | Customer wants to delete data |  |
|  | Details update required |  |
|  | Error while pledging |  |
|  | Incorrect PF / ROI / Tenure |  |
|  | KFS / Agreement |  |
|  | Primary applicant KYC |  |
|  | Unable to fetch portfolio |  |
|  | Credit Referral |  |
|  | Account Opening |  |

## Tags Required:

- lodgement
- account_opening
- enhancement
- disbursal
- foreclosure
- lien_removal
- repayment
- service_request
- details_update
- voluntary_sell_off
- customer_drop_off
- shortfall
- interest
- renewal
- Lender wise

# **System Architecture Overview (LSQ Objects Used)**

# **Ticket Creation Flow (High-Level Architecture)**

This flow clarifies how internal teams create tickets and how parent–child tickets are generated within LSQ.

## **Flow Sequence**

**Support Team → Create New Ticket → Parent Ticket Generated → Create Sub-Ticket → Child Ticket Generated**

## **Detailed Breakdown**

1. **Support (Chat/Calling/Ops) creates a new ticket**
    - Uses LSQ Ticket Creation Form
    - Mandatory fields validated
    - Associated Lead auto-linked
    - Ticket enters **Open** status
2. **Parent Ticket is created**
    - Owned by Support team
    - SLA begins
    - Used to track end-to-end resolution
    - Parent ticket contains the primary issue description
3. **If dependencies exist → Create Child ticket in Associated tickets**
    - Selecting “Create Child” option on the parent ticket
    - Used when Ops intervention is required
    - Inherits context from Parent Ticket
4. **Child Ticket is generated**
    - Assigned to Ops team
    - New SLA cycle starts for child ticket
    - Parent ticket remains active
    - Child ticket maintains:
        - Its own owner
        - Its own SLA
        - Its own “Resolve → Pending RCA” logic
5. **Closure flow**
    - Child Ticket resolution → updates Parent Ticket
    - Parent ticket only moves to “Pending RCA” when all child tickets are resolved

| Component | LSQ Object Used | Purpose |
| --- | --- | --- |
| Ticket Entity | Service Desk Ticket | Main internal ticket object |
| Child Ticket | Sub-ticket object | Used for Ops/Tech dependencies |
| Lead Association | Lead Entity | Auto-lookup using phone/email |
| Ticket Custom Fields | Ticket Custom Fields | L1–L3, Lender, Product, Priority |
| Activities | Ticket Activities | Comments, attachments, status updates |
| SLA Engine | LSQ SLA Rules | Tracks start/stop/pause, escalations |
| Automations | LSQ Workflow Automation | Assignment, status update checks, alerts |
| Reporting | LSQ Reports + Dashboards | SLA, ageing, RCA, team performance |

# **Ticket List View (Agent & Manager View Configuration)**

### **A. Ticket Columns to Display**

- Ticket ID
- Ticket Subject
- Priority
- Ticket Status
- Ticket Owner
- Ageing (Time since creation)
- L1, L2, L3 Category
- Lender
- Product
- Associated Lead
- Created Date
- Last Updated

### **Default Saved Views**

| Team | Saved View |
| --- | --- |
| Support Team | My Open Tickets |
| Ops | Assigned to Ops (Child Tickets) |
| Tech (Through Jira) | Jira Escalated Tickets |
| Managers | SLA Breached, Tickets Pending Closure |

### **Filters**

- Priority
- Status
- Owner
- L1/L2/L3
- Product
- Lender
- Ageing buckets
- Channel

# **Ticket Details Page Layout**

### **Section 1: Ticket Overview**

- Ticket Subject
- Priority
- Status
- Ticket Owner
- Requester
- Product
- Channel

### **Section 2: Associated Lead Panel**

- Lead details auto-fetched
- PAN/Phone visibility
- Lead stage & RM details

### **Section 3: Ticket Description**

- Problem description
- Attachments
- Tags

### **Section 4: Classification & RCA**

- L1 / L2 / L3
- Lender
- Disposition (Resolution Time)
- RCA (Mandatory on Resolve)

### **Section 5: SLA Tracker Widget**

- SLA start time
- SLA time left
- SLA paused/resumed history
- Breach indicator

### **Section 6: Child Ticket Panel**

- Child ticket list
- Status
- SLA for each child ticket
- Resolution summary
- Auto-close logic

### **Section 7: Jira Escalation Panel**

- Jira Ticket ID
- Linked status
- Last sync timestamp

### **Activity Timeline in Activities Tab**

- Comments
- Attachments
- Status change logs
- Owner change logs
- Automation logs

# **Reopen Logic – Detailed Rules**

| Item | Rule |
| --- | --- |
| Who can reopen? | Requester, Ticket Owner, Manager |
| When can reopen? | Only from “Ready for Closure” or “Closed” |
| Mandatory field | Reopen Reason |
| SLA effect | SLA resets to **full cycle** based on priority |
| Max reopen count | Unlimited (logged in audit trail) |
| Owner after reopen | Same as last owner |

# **Validation Rules (Mandatory & Conditional Checks)**

| Field | Validation Rule |
| --- | --- |
| Associated Lead | Must match existing LSQ lead (phone/email). Error if not found. |
| Priority = Urgent | L1/L2/L3 cannot be empty. |
| Product | Always required. |
| Resolution | Disposition + RCA mandatory. |
| Reopen | Reopen reason mandatory. |
| Tech Escalation | Lender + L1–L3 + Description must be present. |

# **Notification & Communication Matrix**

| Event | Triggered When | Recipient(s) |
| --- | --- | --- |
| Ticket Assigned | Owner updated | New Owner |
| Ticket Reassigned | Ownership changed | Old + New Owner |
| SLA Breach Warning | 10/20/30 min before cut-offs | Owner, Manager |
| SLA Breach | SLA exceeded | Owner, Manager, BU Head |
| Tech Escalation | Jira ticket created | Tech Lead |
| Child Ticket Resolved | Child moved to Resolved | Parent Owner |
| Ticket Resolved | Agent marks resolved | Requester |
| Ticket Reopened | Reopen action | Owner, Manager |

# **Reporting Requirements (Dashboards)**

### **A. Operational Dashboards**

- Tickets created by day/week/month
- Tickets on L1/L2/L3
- Tickets on Product
- Tickets on Lender

### **B. SLA Dashboards**

- SLA met vs breached %
- SLA trend over time
- Priority-wise SLA performance
- Owner-wise SLA compliance

### **C. Ageing Dashboards**

- Ageing buckets (0–2h, 2–6h, 6–24h, 1–2 days, 2–5 days, >5 days)
- Tickets ageing by team
- Escalations ageing

### **D. RCA Dashboards**

- Frequency of L3 issues
- Lender-specific RCA trends
- Tech vs Ops RCA splits

### **E. Reopen Dashboard**

- Reopen rate %
- Reopen frequency by team
- Reopened tickets SLA compliance

# **LSQ Automation Requirements (In Progress)**

| Automation | Trigger | Action |
| --- | --- | --- |
| SLA Start | Ticket moved to Open | Start SLA timer |
| SLA Pause | Ticket moved to On Hold | Pause SLA |
| SLA Resume | Removed from On Hold | Resume SLA |
| Child Ticket Auto Close | All child tickets Resolved | Move parent to “Ready for Closure” |
| Jira Sync Watcher | Status change in Jira | Update LSQ status |
| Assignment Reminder | Owner idle for X minutes | Notify owner |
| Breach Alerts | SLA time = threshold | Alerts sent |

# **Support Team Roles, Permissions & Service Group Mapping**

This section defines the **roles**, **permissions**, and **service group assignments** required for operating the LSQ Service Desk across Chat, Email, Call, and Quality functions.

- All support team members must be assigned a **Role** + **Service Group** before go-live.
- Role-based access must be enforced within LSQ:
    - Ticket visibility
    - Ticket modification rights
    - Bulk actions
    - SLA ownership
- Supervisory oversight must be available to:
    - Monitor queues
    - Reassign backlogs
    - Handle escalations
- **Debesh** must receive **Supervisor** role for complete operational oversight.
- LSQ configuration must maintain a **strict separation of service groups** for:
    - Queue segregation
    - SLA management
    - Reporting & dashboards
    - Ownership clarity

## **A. Service Groups & Member Mapping**

| **Email** | **Channel** | **Ticket Assignment** | **Role** | **Service Group** | **Agent Name** |
| --- | --- | --- | --- | --- | --- |
| rashmirekha.das@voltmoney.in | Chat | Yes | Agent | Chat Support team | Rashmirekha Das |
| faryal.muskan@voltmoney.in | Chat | Yes | Agent | Chat Support team | Faryal Muskan |
| revanth.bn@voltmoney.in | Chat | Yes | Agent | Chat Support team | Revanth |
| soundarya.v@voltmoney.in | Email | Yes | Agent | Email Support Team | Soundarya V |
| ranjithkumar.g@voltmoney.in | Email | Yes | Group Manager | Email Support Team | Ranjithkumar G |
| snehalata.rout@voltmoney.in | Email | Yes | Agent | Email Support Team | Snehalata Rout |
| swati.tiwari@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Swati Tiwari |
| apoorva.mishra@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Apoorva Mishra |
| amitkumar.pandey@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Amit Kumar Pandey |
| manoj.gv@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Manoj GV |
| archana.r@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Archana R |
| kashif.hassan@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Kashif |
| muskanbanu.s@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Muskan Banu |
| sagar.cg@voltmoney.in | Inbound Call | Yes | Agent | Call Support Team | Sagar Chindan |
| mohamad.yusuf@voltmoney.in | Quality | No | Light Agent | Call Support Team | Yusuf |
| [debesh.pattanaik@voltmoney.in](mailto:debesh.pattanaik@voltmoney.in) | Quality | No | Supervisor | Manager | Debesh |

## **Role Definitions & Permissions**

### **1. Admin**

- Full access across LSQ Service Cloud.
- Can configure:
    - Ticket schema
    - Automations
    - SLA rules
    - Service groups and roles
- Can view and modify all tickets across all groups.

### **2. Supervisor**

- All **Group Manager** permissions +
- Can:
    - Bulk update tickets within their service group
    - View & assign **unassigned tickets**
    - Override ticket priority/status
- Used for **support leadership oversight**
- **Debesh must be assigned Supervisor access**

### **3. Group Manager**

- Can perform all **Agent** actions.
- Can:
    - View all tickets within their service group
    - Reassign tickets between agents
    - Update ticket priority & status
    - Review SLA breaches and pending closures
- Cannot modify system-level configurations.

### **4. Agent**

- Core support user role.
- Can:
    - Create tickets
    - View tickets assigned to them or their service group
    - Reply to tickets
    - Add comments & attachments
    - Update status & resolve tickets
- Cannot view tickets belonging to other service groups.

### **5. Light Agent**

- Designed for Quality & Monitoring teams.
- Can:
    - View all tickets
    - Add internal notes
- Cannot:
    - Update ticket status
    - Reply to customer
    - Assign or reassign tickets

## **Service Group Definitions**

| Service Group | Description | Channels Included |
| --- | --- | --- |
| **Chat Support Team** | Handles real-time chat support-raised issues | Chat |
| **Email Support Team** | Manages all email-based support requests | Email |
| **Call Support Team** | Handles inbound call issues + Quality checks | Inbound Call, Quality |

# **Support Agent Journey – Ticket Details Page**

This section outlines the end-to-end workflow that a Support Agent follows within the LSQ Service Desk. It covers login, ticket discovery, ticket actions, and resolution flow based on the defined agent permissions.

## **Agent Login & Landing Page**

1. The agent logs into LeadSquared Service Desk.
2. The default landing page shows the **Ticket List View** with configured smart columns:
    - Ticket Subject
    - Customer
    - Status
    - Priority
    - Resolution Due
    - Ticket Owner
3. The agent can switch between predefined ticket views:
    - **My Tickets**
        - Unresolved
        - Overdue
        - Escalated
        - All
        - Customer Responded
    - **All Tickets**
        - All
        - Mentioned me
        - Spam

## **Ticket Discovery & Navigation**

1. Agent reviews My Tickets to see tickets assigned to them.
2. Agent checks All Tickets only to view; they cannot update or assign unless permissions allow.
3. Clicking on any ticket opens the Ticket Details Page.

## **Ticket Details Page – What the Agent Sees**

When an agent opens a ticket, the interface displays the following:

- **Right-Side Panel**
- The agent can view:
    - **Customer Details**
    - **SLA Information**
    - **Ticket Properties**, including:
        - Ticket Type
        - Requester
        - Group
        - Status
        - Ticket Owner
        - Priority
        - Jira ID
        - Description
        - Ticket Subject
    - **Tags**
    - **Associated Tickets**
    - **Linked Jira Ticket**
- **Main Section**
    - The main workspace contains four primary tabs:
        - **Customer Information**
        - **Ticket Conversation**
        - **Previous Tickets**
        - **All Files**
- On the top of the right panel we have a 360 view button which redirects the ticket to the 360 sheet where the agent can see all the calls,email and chats and ticket history for the customer.

## **Ticket Actions Based on Permissions**

### Agent Ticket Permissions - Sales & Support

| **Permission** | **All Tickets** | **My Tickets** | **Service Group Tickets** | **Unassigned Tickets** | **Other Tickets** |
| --- | --- | --- | --- | --- | --- |
| **View Tickets** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Update Tickets** | ❌ No | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Delete Tickets** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Mark Tickets as Spam** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Add an Internal Note** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Merge Tickets** | ❌ No | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Export Tickets** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Reply** | ❌ No | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Bulk Update Tickets** | ❌ No | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Edit Internal Note** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Assign Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Edit Own Internal Note** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Close Tickets** | ❌ No | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Delete Tickets** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Resolve Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Import Tickets** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **View Dashboards** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **View Reports** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |

### Group Manager permissions- Sales & Support

| **Permission** | **All Tickets** | **My Tickets** | **Service Group Tickets** | **Unassigned Tickets** | **Other Tickets** |
| --- | --- | --- | --- | --- | --- |
| **View Tickets** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Update Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Delete Tickets** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Mark Tickets as Spam** | ❌ No | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Add an Internal Note** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Merge Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Export Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Reply** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Bulk Update Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Edit Internal Note** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Assign Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Edit Own Internal Note** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Close Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Purge Tickets** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Resolve Tickets** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **Import Tickets** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **View Dashboards** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **View Reports** | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ❌ No |

### **Allowed for the Agent (My Tickets Only)**

1. **Reply to Customer**
    - Agent can send email/chat replies.
    - Auto-logs communication in the timeline.
2. **Update Ticket Status**
    - Move to In-Progress, Customer Responded, Pending Customer, Resolved, Closed.
3. **Change Priority**
    - Update priority from Low → High as required (if enabled).
4. **Assign/Re-assign Tickets**
    - Can assign to self or other members in their Service Group.
5. **Add Internal Notes**
    - Notes visible only to internal teams.
6. **Merge Tickets**
    - Agent can merge duplicate tickets assigned to them.
7. **Close or Resolve Tickets**
    - Agent can mark a ticket as Resolved or Closed when completed.
8. **Mark as Spam**
    - For unwanted/irrelevant tickets.
9. **Bulk Update** (Only in My Tickets)
    - Status
    - Priority
    - Assignment

### **Not Allowed for the Agent**

- Cannot edit ticket properties not owned by them.
- Cannot delete tickets.
- Cannot export or import tickets.
- Cannot update tickets outside “My Tickets” unless permissions allow.
- Cannot edit internal notes once added.

## **SLA & Timers**

- Agent sees SLA countdown on the ticket.
- Agent receives automated reminders on SLA breach risk.
- SLA breach notifications escalate to lead / team manager.

## **Parent–Child Ticket Flow (Agent Perspective)**

1. If a ticket has child tickets, the agent can see:
    - List of all child tickets
    - Current status of each child
    - Owner of each child ticket
2. For child tickets assigned to the agent, they can:
    - Update progress
    - Communicate
    - Resolve
3. Parent ticket resolution is only allowed once all child tickets are resolved (business rule).

## **Ticket Resolution Journey**

1. Agent works on the ticket (communication, internal notes, attachments).
2. Once resolved:
    - Updates resolution details
    - Marks ticket as Resolved
3. After 48 hours (configurable), if no reopen happens, ticket auto-closes.

## **Smart Views & Filters**

Agents rely on smart filters for faster and smarter groups, where we can add new groups based on each status and priority of tickets.

- Status-based (Open, In-Progress, Pending Customer)
- Priority-based (High, Medium, Low)
- SLA (Due Soon / Overdue)

Smart views improve handling efficiency for high-volume teams.