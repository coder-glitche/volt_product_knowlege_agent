# Jira Integration on LSQ Service desk

## **Jira Integration with LeadSquared Service Desk**

### **Context**

Volt is implementing a Service Desk in LeadSquared (LSQ) to manage all internal and external support requests.

While LSQ will serve as the primary ticketing and workflow system for business and operations teams, Jira will continue to be the engineering and product team’s issue tracking system.

### **Objective**

Build a **Jira Integration Layer** within LSQ to enable:

- Direct **ticket creation in Jira from LSQ**.
- **Bidirectional sync** for key fields — Status, Comments, SLA, and Priority.
- **Embedded Jira ticket visibility** within LSQ UI.
- Unified **SLA compliance tracking** in LSQ for Jira-linked issues.

### **Problem Statement**

At present, there is no structured mechanism for Ops or Support teams to escalate issues from LSQ to Jira.

Without integration:

- Engineering escalations must be manually recreated in Jira.
- Status tracking between LSQ and Jira is disconnected.
- SLA compliance and visibility across tools is missing.
- No unified audit trail exists across ticket lifecycles.

**Challenges / Gaps Identified**

The following key Jira–LSQ integration elements are **not currently visible or functional** within the LSQ Service Desk:

- SLA metrics not visible in Service Desk.
- Jira Owner (Assignee) and reassignment not visible in Service desk
- Status changes visibility not visible in the Service desk

### **Existing Jira Integration (Zendesk Reference)**

Currently, Volt’s Zendesk–Jira setup supports:

- Ticket creation from Zendesk → Jira
- Limited field sync (status, comments)
- No SLA sync or audit visibility

This integration will be **replicated and enhanced** in LSQ.

![image.png](Jira%20Integration%20on%20LSQ%20Service%20desk/image.png)

### **In Scope**

- Ticket creation from LSQ → Jira
- Bidirectional sync for:
    - Status
    - Comments
    - SLA metrics
    - Priority
- Jira issue visibility inside LSQ ticket view
- SLA compliance dashboards within LSQ

**Out of Scope**

- Jira → LSQ ticket creation
- Custom Jira workflow or automation changes
- Integration with other Atlassian tools (Confluence, Slack, etc.)

### **Functional Requirements**

### **1 Jira Ticket creation:**

- Out of the box jira ticket creation fields:
    - Project
    - Issue Type
    - Ticket Owner
    - Priority
    - Summary
    - Description
    - Attachement
- Additional Fields Required:
    - L1 Category
    - L2 Category
    - Requester
- LSQ Agent creates ticket → fills L1, L2, Issue Type, Summary, Priority, Description.
- LSQ → Jira API creates issue with above fields + Reporter + Lender
- Jira ID & URL returned to LSQ.

### **2 Sync (Jira → LSQ)**

| Sync Type | Description |
| --- | --- |
| **Status Sync** | Jira status updates (e.g., *To Do → WIP → Resolved*) reflected in LSQ. |
| **Comment Sync** | Public Jira comments pushed as LSQ internal notes. |
| **SLA Sync** | LSQ displays Jira SLA compliance (% met, breached). *(to be explored)* |
| **Owner Updates** | Jira assignee reflected in LSQ. |

### **3 Sync (LSQ → Jira)**

| Sync Type | Description |
| --- | --- |
| **Comment Sync** | LSQ comments (marked “public to Tech”) reflected in Jira comments. |
| **Attachment Sync** | Any new attachment in LSQ auto-syncs to linked Jira issue. |

### **Field Mapping and Sync Logic**

The following fields must be created in Jira when a ticket is initiated from LSQ, and kept in sync between both systems as applicable.

| **Field Name** | **Source (Created in)** | **Sync Direction** | **Behavior / Logic** | **Notes / Remarks** |
| --- | --- | --- | --- | --- |
| **Summary** | LSQ | LSQ → Jira | Mandatory; maps to Jira “Summary” | Derived from LSQ ticket title |
| **Description** | LSQ | LSQ → Jira | Full description captured from LSQ ticket | Rich text supported |
| **Attachments** | Both | Bidirectional | All attachments uploaded in LSQ must flow to Jira and vice versa | Sync to occur automatically on upload |
| **Comments / Notes** | Both | Bidirectional | Comments added in LSQ appear in Jira (as public); Jira comments appear in LSQ (as internal notes) | Maintain chronological order |
| **Priority** | Both | Bidirectional | Priority updates in LSQ must reflect in Jira and vice versa | User with permission can edit |
| **Current Assignee** | Jira | Jira → LSQ | Jira assignee auto-populates in LSQ and updates dynamically | Used for visibility only in LSQ |
| **Reporter (Ticket Owner)** | LSQ | LSQ → Jira | LSQ ticket creator mapped to Jira “Reporter” field | Mandatory field |
| **Issue Type** | LSQ | LSQ → Jira | Derived from LSQ L1 category | Example: Bug, Change, Service Request, Improvement |
| **L1 Category** | LSQ | LSQ → Jira | Maps to Jira custom field “Issue Type” | For classification consistency |
| **L2 Category** | LSQ | LSQ → Jira | Maps to Jira custom field “Issue Sub-type” | Example: Data Issue, API Error, UAT Blocker |
| **L3 Category** | LSQ | LSQ → Jira | Separate Jira custom field; populated based on L2 value | Required for reporting |
| **Critical Since (Date)** | LSQ | LSQ → Jira | Captures when issue became critical | Used for SLA breach reporting |
| **Lender** | LSQ | LSQ → Jira | Optional field to capture lender tag | Enables lender-wise analytics in Jira |
| **SLA Metrics** | Jira | Jira → LSQ | Jira SLA performance to be displayed in LSQ | Data pulled via API |
| **Status** | Both | Bidirectional | Reflects Jira workflow status changes (To Do, WIP, Resolved, Closed) | Auto-updated in LSQ UI |

### **Access & Edit Permissions for Jira**

| **Action** | **Allowed In** | **Reflected In** | **Notes** |
| --- | --- | --- | --- |
| Change Priority | LSQ | Jira | Accessible to LSQ Managers & Supervisors (Escalations) |
| Add / Edit Comments | Both | Both | Syncing in both jira and lsq |
| Add Attachments | Both | Both | File types to match Jira allowed formats |
| Assign Ticket | Jira | LSQ | LSQ displays current assignee; not editable from LSQ |
| Close / Resolve Ticket | Both | Both | Closure auto-syncs and updates LSQ ticket to “Resolved from Tech” |