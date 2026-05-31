# Ticketing Tool Evaluation Document

: Ranjan kumar Singh
Created time: February 19, 2025 3:31 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

## 1. Introduction

### Purpose of Evaluation

The purpose of this document is to evaluate the ticketing tool based on various predefined criteria. The evaluation aims to determine the tool’s efficiency, usability, integration capabilities, security features, and overall challenges faced by the organisation.

### Scope and Objectives

This evaluation focuses on assessing the ticketing tool’s ability to handle support tickets, automate workflows, and integrate with other systems. The objectives include:

- Analyzing feature sets and usability
- Evaluating system performance and reliability
- Reviewing security and compliance standards
- Assessing cost-effectiveness and support options

DATA sharing over WA and 1:1 WA chat with MFD

- PI Data and any other data

## 2. Current Challenges

## Agent Challenges/process gap

| # | Challenge | Impact | Priority |
| --- | --- | --- | --- |
| 1 | Agents do not have visibility into a customer’s history when handling chats, calls, or emails. | Incomplete context, repetitive customer interactions | P0 |
| 2 | Agents has to navigate multiple tools to gather customer details, as there is no unified **Customer 360** view. | Inefficient workflows, longer resolution times | P0 |
| 3 | Agent handling MAIL support check AppSmith to verify customer registration when responding to emails. | Process fragmentation, additional steps | P2 |
| 4 | Extensive manual data entry for internal tickets Like Phone, PAN, issue category etc | Time-consuming, error-prone processes | P0 |
| 5 | No notifications for **JIRA** ticket updates/comments [ Automation issue] | Missed updates, lack of case transparency | P0 |
| 6 | Agents working on **LSQ** lack visibility into any ongoing tickets while handling the customer or MFD. | Incomplete information, potential duplicate work | P0 |
| 7 | Missing knowledge base for handling basic queries | Inconsistent responses, unnecessary escalations | P0 |
| 8 | Agents not updated on product changes and features | Misinformation to customers, escalations | P0 |
| 9 | Manual email ticket handling with spreadsheet tracking | Inefficient processes, risk of missed tickets, Longer TAT for CX | P0 |
| 10 | No visibility into **TAT of internal ticket and resolution TAT from  the 3P** | Inability to provide ETAs to customers | P0 |
| 11 | No automated greeting/acknowledgment emails | Poor initial customer experience | P0 |
| 12 | MAIL agents has to raise the **JIRA** tickets separately

Zendesk ticket gets created when email is received on support@voltmoney.in | Duplicated effort, system fragmentation | P1 |
| 13 | After raising tickets to **Ops/Tech**, agents has to follow up multiple times manually | Time-consuming, dependent on agent diligence | P0 |
| 14 | Concurrent chat handling issues affecting **FRT - WATI config issue** | Response time delays, overwhelmed agents |  |
| 15 | Slowness of **WATI** dashboard | Reduced agent productivity |  |
| 16 | Chat and MAIL support teams do not have the option to initiate calls with customers, even when a call would be more effective for resolution. Instead, they direct customers to **Volt Support**. | Limited resolution options, additional transfers | P1 |
| 17 | No support for international **WhatsApp call-backs** | Unmet customer needs, service limitations | P3 |
| 18 | Agents are unaware of the necessary details and documents required to debug and resolve customer issues (e.g., for **limit mismatches**, agents should request an **AMC statement**) - Part of knowledge center | Multiple customer contacts, delayed resolution | P0 |
| 19 | When a customer is connected across multiple channels (WhatsApp, call, email), different agents provide different/inconsistent information - 360 not avlbl | Customer confusion, reduced trust | P0 |
| 20 | The **Chat Team** asks the **Ops Team** to use admin actions for service requests, requiring verbal follow-ups. | No tracking, potential for missed requests, Higher TAT | P3 |
| 21 | **Prioritization based on ticket severity is missing**, leading to inefficient handling of critical issues. | Inefficient handling of critical issues | P0 |
|  |  |  |  |

### B2B2C channel

| Challenge | Impact |
| --- | --- |
| FRT for periskope chat and WATI are not getting captured and tracked | - Message on group getting missed |
| We send broadcast on WATI, hence MFD reply on WATI, and then call to RM
 | - Touchpoints are fragmented
- Tracking, Visibility and reporting is missing
- Context retention |
| Chat are getting closed after 24 hours [Limitation of WABA] and hence can’t initiate chat from WATI | - Agent can’t initiate chat 
- Can’t share any update on issue |
| WATI chat SLA is not tracking |  |
| Support ask repetitive question as they do have the visibility of past interactions at one place |  |
| SLA management on periscope do not exists |  |
| Periscope only allow to create tickets on individual chat but not on the group level | Tracking and escalation  |
| MFD team want to solve for visibility by using Periskope, but Periscope is not solving for same |  |
| SLA and escalation metric for MFD ticket is not present, unless we get escalation we do not inform MFD about the updates |  |
| No linking of ZOHO and zendesk |  |
| No bucketing of ticket for MFD channels |  |
| MFD level knowledge gap tracking is not happening |  |
| Auto assignment of chat on periscope is not available   |  |
| Tracking of Who all are interacted with the MFD or customer is not avlbl |  |
| MFD employee interaction is not getting captured and need to solve |  |
| Sub-broker interaction, prudent  |  |
| Handling of B2B like jupitor/ZYPE |  |
| No of tool that will used by one person |  |

** Periscope team has stopped development on tool

** WA group as a solution to handle MFD is not sustainable for scale

** Kapil WA and phone hangs due to WA group and removed Kapil from the many group

** Auto reply not supported on periscope.

** Employee use case:

**** Only few MFD has employee not all, they have dedicated employee to handle LAS since they also do not want to involve many employee 

** MFD who has employee do not monitor group. and hence we do not need to solve for MFD visibility but we need to solve for internal multi agent visibility [RH → RM → RM back up → support team] 

** For top 100 MFD we need to set escalation metric..KAPIL/BHARAT/SHIVANSH directly want to interact with them in case of any escalation.

### Limitations of whatsApp groups:

1. **Limited organizational structure**
    - We can't effectively map our hierarchical team structure (RM → RM Backup → Regional → Escalation)
    - No built-in ticket assignment or routing capabilities
    - Messages easily get buried in busy groups
2. **Poor Visibility & Tracking**
    - No centralized dashboard for open issues
    - Difficult to track resolution status of multiple queries
    - No way to generate reports on service performance
3. **Data Security & Compliance Risks**
    - Financial data shared in WhatsApp may violate regulatory requirements
    - No audit trails for compliance and audit purposes
    - Limited control over who can access sensitive customer information
4. **Poor Scalability**
    - Hard to manage increasing number of groups
    - Becomes unmanageable as volume increases
    - Hard to onboard/offboard team members

### **Take on WhatsApp group:**

Using **WhatsApp Groups** alone is **not an ideal solution** for managing customer service at scale. While WhatsApp is great for quick communication, it lacks **structured tracking, reporting, and escalation workflows**. However, WhatsApp can be **integrated as a communication channel** within a proper **CRM + Ticketing system** to improve efficiency.

---

## **🚫 Why WhatsApp Groups Are NOT the Best Solution?**

❌ **No Ticket Tracking:** Issues get lost in chat history.

❌ **No Workflow Management:** No assignment, escalation, or SLA tracking.

❌ **No Reporting:** Cannot analyze common issues, resolution times, or performance.

❌ **No Role-Based Access:** Everyone in the group sees all conversation, which may not be desirable.

❌ **Difficult to Scale:** Managing multiple MFDs with multiple employees in groups can get messy.

---

## **✅ Best Approach: Use WhatsApp Integrated with a Ticketing System**

Instead of **WhatsApp Groups**, consider using **WhatsApp Business API** integrated with a **CRM**

### **How It Works:**

1️⃣ **MFD Employees & Customers Message on WhatsApp → Auto-Create a Ticket**

2️⃣ **Ticket Gets Categorized & Assigned to the Right Volt Team Member [Based on workflow]**

3️⃣ **Volt Team Resolves the Issue & Updates the Ticket via CRM**

4️⃣ **MFD Employee or Customer Gets WhatsApp Updates on Ticket Status**

5️⃣ **Issues Are Tracked in Dashboards for Reporting & SLA Monitoring**

---

## **🚀 Benefits of WhatsApp + Ticketing System**

✔ **MFDs & Customers Get a Familiar Interface (WhatsApp) to Raise Issues**

✔ **Volt’s Internal Teams Get a Structured Workflow in the CRM**

✔ **Tickets Are Properly Tracked, Categorized & Escalated Automatically**

✔ **Reports Help Identify Common Issues & Improve Loan Servicing**

---

### **🔹 Example: How Volt Can Use WhatsApp Effectively**

✅ **MFD-Specific WhatsApp Numbers:** Assign a unique WhatsApp number for each region or key MFDs.

✅ **Chatbots for Common Queries:** Automate simple queries (e.g., "What’s my loan status?") before creating tickets.

✅ **Smart Routing:** Forward complex issues to Volt’s internal teams via CRM.

✅ **Escalation Triggers:** If an issue is unresolved in 24 hours, automatically escalate within CRM.

---

## **📌 Final Recommendation**

❌ **Don’t Rely on WhatsApp Groups** – Unmanageable at scale.

✅ **Use WhatsApp Business API + CRM** – Best for structured issue tracking, escalation, and reporting.

---

B2B2C servicing challenges: [https://docs.google.com/spreadsheets/d/1n4HxOPhb_KT5ZWd39QTB3sgyW6L0dC9IpwtkjUpSw68/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1n4HxOPhb_KT5ZWd39QTB3sgyW6L0dC9IpwtkjUpSw68/edit?usp=sharing)

# User Journey Across Channels with Team Structure and Ticket Management [Proposed]

## B2B2C Channel

**🔹 Persona: MFD, MFDs employee, Customer associated with MFD**

**🔹 Interaction: WhatsApp,** Email & Call

### User Journey for MFD and their employee

1. **Initial Contact**
    - MFD or employee contacts dedicated partner WhatsApp, calls partner line, or emails support
    - Query typically involves client loan applications issues, payout concerns, or client loan servicing
2. **Ticket Creation**
    - **For Phone Call**: Agent creates ticket, Automatically tags MFD  identifier, links recording
    - **For WhatsApp**: System identifies MFD from registered number, creates pre-categorized ticket [Employee <> MFD mapping has to be done if employee reach out on MFD behalf]
    - **For Email**: System identifies MFD from email, creates ticket and tags MFD indetifies
    - Help center /portals on partner dashboard: MFD/MFD employee creates and track tickets on partner dashboard
    - If any open tickets exists for a MFD then create child tickets
3. **Team Assignment**
    - System identifies specific Relationship Manager assigned to the MFD/IFA
    - Ticket assigned to Support Team CC'd RM
    - RM, B2B2C support, regional head and backup RM have visibility
4. **Resolution Process**
    - B2B2C support has primary ownership of resolution
    - RM assists B2B2C support
    - All communications visible to RM, B2B2C support, regional head and backup RM
    - MFD/IFA can view all interactions related to their clients at one place and tickets on partner dashboard
5. **Escalation Path**
    - Support Team → Relationship Manager → Regional Head → Escalation Manager
    - Automatic escalation if SLA breached
    - Manual escalation available to RM for complex cases
    - Regional Head has dashboard view of all open tickets across their MFDs/IFAs

### User Journey clients associated with MFDs

1. **Initial Contact**
    - B2B2C customers contacts dedicated customer WhatsApp, calls, or emails support
    - If common customer support team is handling the all customer irrespective the channel, then RM should have the visibility of customer linked to MFD who belongs to the RM
    - Query typically involves loan applications issues, or client loan servicing
2. **Ticket Creation**
    - **For Phone Call**: Agent creates ticket, Automatically tags MFD identifier, links recording
    - **For WhatsApp**: System identifies customer from registered number, creates pre-categorized ticket, Tag as B2B2C channel and partner/MFD identifiers
    - **For Email**: System identifies Customers from email id, creates ticket and tags MFD indetifies
3. **Team Assignment**
    - System identifies specific Relationship Manager assigned to the Customers
    - Ticket assigned to Support Team CC'd RM
    - RM, B2B2C support, regional head and backup RM have visibility
4. **Resolution Process**
    - B2B2C support has primary ownership of resolution
    - RM assists B2B2C support team
    - All communications visible to RM, B2B2C support, regional head and backup RM
    - MFD/IFA can view all interactions related to their clients at one place and tickets on partner dashboard
5. **Escalation Path**
    - Support Team → Relationship Manager → Regional Head → Escalation Manager
    - Automatic escalation if SLA breached
    - Manual escalation available to RM for complex cases
    - Regional Head has dashboard view of all open tickets across their MFDs/IFAs

## B2B Channel

**🔹 Persona: B2B partner SPOC, Customer associated with partner platform** 

**🔹 Interaction: WhatsApp,** Email & Call

### User Journey for **B2B partner SPOC**

1. **Initial Contact**
    - Partner SPOC contacts dedicated WhatsApp number, calls phone, or emails support
    - Query typically involves API integration issues, dashboard access, or customer-specific concerns
2. **Ticket Creation**
    - **For Phone Call**: Support agent creates ticket with call recording link, categorizes as B2B
    - **For WhatsApp**: System automatically creates ticket from chat, tagged as B2B channel
    - **For Email**: System generates ticket with email thread, categorizes based on sender channel
3. **Team Assignment**
    - Ticket automatically routed to B2B Support Team based on partner identification
    - B2B Support team member assigned as primary owner
4. **Resolution Process**
    - Assigned team member works on resolution within SLA (faster for partners)
    - All communications (calls, chats, emails) logged centrally in ticket
    - Team has full visibility of all partner interactions across channels
5. **Escalation Path**
    - L1 → L2 B2B Support → B2B Manager → Technology Team (if needed)
    - Automatic escalation triggered if SLA breached
    - Partner-specific escalation protocols based on agreement
    - Visibility to partners on the Ticket raised ,current status and feasibility to reopen a ticket should also be explored.

### User Journey for **Customer associated with partner platform like Jupitor**

1. **Initial Contact**
    - Customer contacts dedicated WhatsApp number, calls phone, or emails support
    - Query typically involves loan application issue, withdrawals, repayment, lien removal etc
2. **Ticket Creation**
    - **For Phone Call**: Support agent creates ticket with call recording link, categorizes as B2B customer and platform name as Jupitor
    - **For WhatsApp**: System automatically creates ticket from chat, tagged as B2B channel and platform name as Jupitor
    - **For Email**: System generates ticket with email thread, categorizes based on sender channel and name
3. **Team Assignment**
    - Ticket automatically routed to B2B Support Team based on partner identification
    - B2B Support team member assigned as primary owner or assign to B2C support team [Based on team structure or business requirement]
4. **Resolution Process**
    - Assigned team member works on resolution within SLA
    - All communications (calls, chats, emails) logged centrally in ticket
    - Team has full visibility of all customer interactions across channels
5. **Escalation Path**
    - L1 → L2 B2B Support → B2B Manager → Tech Team (if needed)
    - Automatic escalation triggered if SLA breached
    - Partner-specific escalation protocols based on agreement

## B2C Channel (Direct Customers)

### User Journey

1. **Initial Contact**
    - End customer contacts customer WhatsApp number, customer phone line, or emails support
    - Typical queries: loan application issues, repayment questions, withdrawals
2. **Ticket Creation**
    - **For Phone Call**: IVR collects basic info, agent creates ticket with call summary
    - **For WhatsApp**: Bot collects initial information, creates categorized ticket
    - **For Email**: System parses email, creates ticket with auto-categorization
3. **Team Assignment**
    - Ticket routed to B2C Support Team queue
    - Assigned based on availability and query category
4. **Resolution Process**
    - Agent follows standard B2C resolution workflow
    - All follow-up communications tracked in centralized ticket
    - Customer receives consistent responses regardless of channel switching
5. **Escalation Path**
    - B2C Support Agent → B2C L2 Support → B2C Manager
    - Escalation triggers: SLA breach, customer dissatisfaction, complex cases
    - All team members can view full communication history [Call, Chat, Mail] during escalation

## Unified Channel Management for Mixed Customer Queries

### 1. Initial Customer Identification System

When a contact comes in through any shared channel (WhatsApp or phone):

1. **Automatic Lookup Process**
    - System performs database lookup using phone number/Email ID
    - Checks customer database for channel association
    - Identifies if the customer is:
        - Direct B2C customer
        - Associated with a B2B partner
        - Client of an MFD/IFA (B2B2C)
2. **Unknown Number Handling**
    - If phone number not in database, implement a brief identification flow:
        - Collect basic identifying information
        - And assign customer to queue accordingly

### 2. Channel-Specific Routing After Identification

Once the customer's channel is identified:

**For B2C Customers:**

- Route to B2C support team queue
- Apply standard B2C handling protocols
- Create tickets according to standard B2C rules

**For B2B Partner Customers:**

- Identify specific B2B partner
- Route to B2B support team with partner context
- Flag with partner-specific handling protocols

**For B2B2C (MFD/IFA) Customers:**

- Identify specific MFD/IFA association
- Identify the client's specific RM
- Route directly to B2B2C support with client context
- CC RM for visibility
- For MFDs not tagged to any RM or is tagged to system, the ticket should be associated with Team lead/Nitin.

### 3. Off-Hours Management for Mixed Channel Queries

For off-hours contacts with mixed channel origins:

1. **Universal Off-Hours Protocol**
    - Create ticket for all off-hours communications
    - Include channel identification data (once determined)
    - Set priority based on channel SLAs (B2B2C might have higher priority)
2. **Channel-Specific Next business hours processing**
    - Team sorts tickets by channel
    - Distributes to appropriate teams based on channel
    - For example - B2B2C tickets routed to specific RMs based on MFD association

---

---

## Cross-Channel Visibility & Management

### Team-Level Visibility

1. **Relationship Manager Dashboard**
    - All interactions (calls, chats, emails, tickets) for their assigned MFDs/IFAs
    - Performance metrics against SLAs
    - Escalation alerts and pending actions
2. **Regional head View**
    - Aggregated view of all RMs and their MFDs/IFAs
    - SLA compliance reports by RM
    - Critical escalations requiring attention
    - Trend analysis of recurring issues
3. **Support Team Dashboard**
    - Queue of tickets requiring backend support
    - Cross-channel communication history for context
    - SLA tracking for assigned tickets

### Ticket Integration

1. **Phone Call Integration**
    - Call recordings linked to tickets
    - Call transcripts for searchability
    - Agent notes and categorization
2. **WhatsApp Integration**
    - Complete chat history embedded in ticket
    - File/document sharing capabilities
    - Status updates via WhatsApp
3. **Email Integration**
    - Email threads maintained within ticket
    - Attachments accessible to all team members
    - Reply-from-ticket functionality

### Reporting & Analytics

- Channel performance metrics (resolution time, satisfaction)
- Team performance by channel and query type
- Common issues by channel for process improvement
- MFD/IFA-specific analytics for relationship management

This integrated approach ensures that regardless of which channel a customer, partner, or MFD uses to contact Volt, their query is properly tracked, assigned to the appropriate team, and visible throughout the resolution process with clear escalation paths defined for each channel.

### Tool commercials:

LSQ:

| Tool/service | Cost | Remarks |
| --- | --- | --- |
| Service desk | 1300 per user | No concept of light agent |
| Hybrid | 2700 per user | Sales CRM + Service desk |
| WATI connector | 4000 per connector |  |
| Converse | RS 2.80 per session | WABA session |
| Bulk messaging(Marketing suite) |  |  |
|  |  |  |

Eazybe:

| Tool/service | Cost | Remarks |
| --- | --- | --- |
| Web WA with LSQ chrome extension | 900 per seat |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

| Strength | Weakness |
| --- | --- |
| RM can send WA message to lead from LSQ using personal number | WA sync is not working |
| Task/Notes/leads can be created without going to LSQ dashboard | UI is looking cluttered on window laptop |
| Performance/Analytics of personal chat is available | Support is not to good |
| Can schedule WA message | Group chat is not getting synced |
| AI capability: summaries inbound message, create reply, rephrase message | Search lead with phone no available |
| Quick reply |  |
| Set reminder  |  |
| Filter chat based on mention |  |

---

---

**Add ons**

-If an MFD wants to share an image , SS or physical mandate pictures, where will he share it.

-In case an MFD employee wants to initiate a chat, share documents, he should be able to use a common identifier(MFD No) so that he lands at the correct place

-Visibility also to be provided to Partners on the number of ticket raised and current status.

-How can feasibility of raising tickets can be given to MFD/Platforms so that they have reduced reliance on RMs

-SLAs to be defined for various ticket types

Hi Lalit,

We have conculed the problem statement we need to solve after discussion with Kapil, shivansh and Tusher

All are aligned to not to use WhatsApp group for servicing because of the below reason.

**No Ticket Tracking:** Issues get lost in chat history.

**No Workflow Management:** No assignment, escalation, or SLA tracking.

**No Reporting:** Cannot analyze common issues, resolution times, or agent performance.

**No Role-Based Access:** Everyone in the group sees all conversation, which is not desirable.

**Difficult to Scale:** Managing multiple MFDs with multiple employees in groups can get messy, groups on periskope are becoming unmanageable as volume increases

**Unofficial tool:** I benchmarked tools which offers the WhatsApp group solution but all are unofficial, non compliment, storing data on their cloud and server is out of India. with this limitation we will not able to do integration with out internal system like appSmith, LeadSquared.

**Fragmented touch points: MFDs are connect on Perskope, Partner WATI, Partner phone number and even on the personal phone of RM and hence we as a team lacks the visuality of reach out as their are not centralised system** 

**Poor Visibility & Tracking**

- No centralised dashboard to track and monitor open issues
- Difficult to track resolution status of multiple queries
- No way to generate reports on service performance and categorisations of issue raised in B2B2C channel

Conclusion:

Using **WhatsApp Groups** alone is **not an ideal solution** for managing customer service at scale. While WhatsApp is great for quick communication, it lacks **structured tracking, reporting, and escalation workflows**. However, WhatsApp can be **integrated as a communication channel** within a proper **CRM + Ticketing system** to improve efficiency.