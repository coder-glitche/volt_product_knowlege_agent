# LSQ Service Desk

: Vijay Kumar S
Created time: October 22, 2025 11:56 AM
Status: Not started
Last edited: December 24, 2025 11:59 AM

## **1. Overview**

**Objective:**
Phase 1 focuses on building an LSQ-based internal Service Desk that enables structured internal ticketing, SLA management, and Jira integration.

**Scope Includes:**

- Jira Integration with LSQ
- Internal Ticket Management (Sales, Support, Ops)
- Ticket Creation & Assignment Logic
- Volt Operations Team Workflow
- Email Integration (Phase-ready foundation)

## 

[Jira Integration on LSQ Service desk](LSQ%20Service%20Desk/Jira%20Integration%20on%20LSQ%20Service%20desk%202aee8d3af13a80e8a5f7c0b8e990256a.md)

[Support Requirement](LSQ%20Service%20Desk/Support%20Requirement%202aee8d3af13a80e3ae45c08bfa32a8bf.md)

[Volt Ops Requirements

The child ticket will be created and assigned to Volt Ops.](LSQ%20Service%20Desk/Volt%20Ops%20Requirements%20The%20child%20ticket%20will%20be%20cre%202afe8d3af13a80b9be04e4c2eb5d9880.md)

# **3. Internal Ticketing Framework:**

This section defines the **complete ticket lifecycle** for the LSQ Service Desk used by Support, Sales, and Operations teams. It covers how a ticket is created, assigned, triaged, escalated (Volt Ops, Product, Lender), and resolved, including SLA behaviour, parent–child ticket logic, and exception handling.

# **Actively Involved**

- **Customer / MFD**
- **Agent (Chat / Email / Calling)**
- **System (LSQ Automations & Integrations)**
- **Volt Ops Team**
- **Product / Tech (via Jira)**
- **Lender Partners**

# **Ticket Lifecycle Overview**

A ticket progresses through the following high-level stages:

1. **Intake & Ticket Creation**
2. **Classification**
3. **Work / Investigation**
4. **Child Ticket Creation (Volt Ops / Product / Tech / Lender)**
5. **Resolution & Customer Validation**
6. **Closure & CSAT**
7. **Reopen, RCA** 

# **Detailed Step-by-Step Ticket Flow**

## **In Take & Ticket Creation**

1. **Customer initiates contact** via Chat, Call, Email
2. **System identifies the customer**
    - If contact exists → attach to contact.
    - If new → create new contact with basic details.

Use cases where a ticket will be created and a ticket will not be created:

| Channel | Scenario | Condition | Ticket? | Notes |
| --- | --- | --- | --- | --- |
| Call | Registered number call | Lead exists | YES | Auto-link ticket to lead; capture disposition. |
| Call | Unregistered number call | Lead not found | YES | Capture disposiiton and Create new ticket. |
| Call | Telemarketing calls |  | NO | Mark as Spam |
| Call | Missed call from registered number | Customer dropped | YES | New Ticket with status open with associated lead |
| Call | Missed call from non registered number | Customer dropped | YES | New Ticket with status open |
| Email | Any email sent to support@ | Incoming email | YES | LSQ auto-creates ticket. |
| Email | Customer CSAT Negative | Negative feedback/issue | YES | Linked via email match. |
| Email | MFD/Partner raises issue | Operational partner need | YES | Partner support ticket. |
| Email | Internal team request | Ops/Sales request | Yes | Link to ticket if no ticket create new ticket |
| Email | Reply to existing ticket | Email contains ticket ID | YES (updates existing) | Should NOT create new ticket. |
| Email | Spam emails | Marketing/unrelated domains | NO | Mark spam. |
| Email | Auto replies (OOO) | Out-of-office or promotional reply | NO | Update timeline only. |
| Chat | Customer reports issue | Complaint/issue stated | YES | Auto-create ticket. |
| Chat | Registered number chat | Lead exists | YES | Link to lead. |
| Chat | Unregistered number chat | Lead not found | YES | Create  ticket with disposition |
| Chat | Chat abandoned but issue captured | Intent identified | YES | Issue ticket should be created. |
| Chat | Agent flags issue manually | Agent detects problem | YES | Manual ticket creation. |
| Chat | Duplicate chat for same issue | Existing ticket open | NO | Merge into existing ticket. (in a same day) |
| Manual | Ticket reopened | Existing ticket reopened | YES | Continue same ticket. |
| Manual | Internal tracking | Ops/CS task | YES | Internal ticket. |
| Edge Case | Chat from different number | Lead mismatch | YES | Link manually or create lead. |
1. **System checks for duplicate/open tickets**
    - If matching open ticket found → update or create new ticket.
    - If not → proceed with new ticket creation.
2. **Ticket is created (Parent Ticket)**
    
    Mandatory fields:
    
    - Requester
    - Contact mapping
    - Subject
    - Description
    - Product Type (Pre-Loan / Post-Loan / Other)
    - Issue Type (L1/L2/L3)
    - Priority
    - Group
    - Channel
    
    ```mermaid
    flowchart TD
    
    %% ----------------------
    %% Dedup Check
    %% ----------------------
    A["Email received"] --> S{"Duplicate email?<br/>(Same Lead + Same Subject + Within 1 Day)"}
    
    S -- Yes --> T["Update existing LSQ Ticket"]
    S -- No --> P["Create LSQ Ticket"]
    
    %% ----------------------
    %% Acknowledgement
    %% ----------------------
    P --> ACK["Send Acknowledgement Email to Customer<br/>with Ticket ID"]
    T --> ACK
    
    %% ----------------------
    %% SLA Starts
    %% ----------------------
    ACK --> D["Start SLA on Ticket"]
    
    %% ----------------------
    %% Triage & Categorisation
    %% ----------------------
    D --> E["Email Agent triage"]
    E --> F["Fill Issue Type + L1 + L2 + L3"]
    
    %% ----------------------
    %% Issue Type Branch
    %% ----------------------
    F --> C1{"Issue Type?<br/>Misc / Pre-Loan / Post-Loan"}
    
    %% ============================
    %% 1. MISC FLOW
    %% ============================
    C1 -- Misc --> M1["Email Team resolves ticket"]
    M1 --> MFE["Send Final Resolution Email"]
    MFE --> MCSAT["Send CSAT Survey"]
    MCSAT --> M3["Close Ticket with RCA"]
    
    %% ============================
    %% 2. PRE-LOAN FLOW
    %% ============================
    C1 -- Pre-Loan --> PL1["Email Team attempts resolution"]
    
    PL1 --> PL2{"Resolved by Email Team?"}
    
    PL2 -- Yes --> PL3["Send Final Resolution Email"]
    PL3 --> PLCSAT["Send CSAT Survey"]
    PLCSAT --> PL4["Close Ticket with RCA"]
    
    PL2 -- No --> PLOPS1["Assign Ticket to Ops (Pre-Loan)"]
    
    PLOPS1 --> PLOPS2["Ops attempts resolution"]
    
    PLOPS2 --> PLOPSDEC{"Need Tech support (Jira)?"}
    
    %% Ops resolves without Tech
    PLOPSDEC -- No --> PLOPSDONE["Ops resolves & updates ticket"]
    PLOPSDONE --> PLU1["Email Team sends Final Resolution Email"]
    PLU1 --> PLCSAT2["Send CSAT Survey"]
    PLCSAT2 --> PL4
    
    %% Ops needs Tech
    PLOPSDEC -- Yes --> PLJ1["Ops raises Jira & stores Jira ID in Ticket"]
    PLJ1 --> PLJ2["Tech works on issue"]
    PLJ2 --> PLBACK["Tech updates Ops via Jira"]
    
    PLBACK --> PLOPS3["Ops updates ticket with fix"]
    PLOPS3 --> PLU2["Email Team sends Final Resolution Email"]
    PLU2 --> PLCSAT3["Send CSAT Survey"]
    PLCSAT3 --> PL4
    
    %% ============================
    %% 3. POST-LOAN FLOW
    %% ============================
    C1 -- Post-Loan --> PLO1["Email Team attempts resolution"]
    
    PLO1 --> PLO2{"Resolved by Email Team?"}
    
    PLO2 -- Yes --> PLO3["Send Final Resolution Email"]
    PLO3 --> PLOCSAT["Send CSAT Survey"]
    PLOCSAT --> PLO4["Close Ticket with RCA"]
    
    PLO2 -- No --> PLO4A["Send Update Email<br/>(Case routed to Ops)"]
    PLO4A --> PLO4B["Assign Ticket to Ops (Post-Loan)"]
    
    PLO4B --> PLO5["Ops attempts resolution"]
    
    PLO5 --> PLODEC{"Support needed?"}
    
    %% Ops resolves internally
    PLODEC -- No --> PLOINT["Ops resolves & updates ticket"]
    PLOINT --> PLOU1["Email Team sends Final Resolution Email"]
    PLOU1 --> PLOCSAT2["Send CSAT Survey"]
    PLOCSAT2 --> PLO7["Close Ticket with RCA"]
    
    %% Ops needs Tech or Lender
    PLODEC -- Yes --> PLOPATH{"Support type?<br/>Tech (Jira) / Lender Offline"}
    
    PLOPATH -- Tech (Jira) --> PLOJ1["Ops raises Jira & stores Jira ID"]
    PLOJ1 --> PLOJ2["Tech provides update"]
    PLOJ2 --> PLOUP1["Ops updates ticket"]
    
    PLOPATH -- Lender Offline --> PLOL1["Ops contacts Lender offline"]
    PLOL1 --> PLOL2["Ops updates ticket with Lender response"]
    
    PLOUP1 --> PLO6
    PLOL2 --> PLO6
    
    PLO6 --> PLOU2["Email Team sends Final Resolution Email"]
    PLOU2 --> PLOCSAT3["Send CSAT Survey"]
    PLOCSAT3 --> PLO7["Close Ticket with RCA"]
    
    %% ----------------------
    %% Customer Dependency
    %% ----------------------
    F --> CD0{"Need more info from Customer?"}
    
    CD0 -- Yes --> CE["Send 'Need More Info' Email"]
    CE --> CR["Customer replies"]
    CR --> E2["Email Team continues triage"]
    E2 --> C1
    
    CD0 -- No --> C1
    
    %% ----------------------
    %% SLA Monitoring
    %% ----------------------
    D --> S1["Monitor SLA on Ticket"]
    
    S1 -->|L1 Breach| S2["Notify Email Agent"]
    S1 -->|L2 Breach| S3["Escalate to Manager"]
    S1 -->|L3 Breach| S4["Escalate to Leadership / Critical Queue"]
    
    ```
    
3. **SLA & FRT timers start** as soon as the ticket is created.
4. **Acknowledgement sent** to Customer/MFD with Ticket ID & expected timelines.

Email Ticket workflow:

# Internal ticket workflow:

![image.png](LSQ%20Service%20Desk/image.png)

## **Process note:**

| **Scenario** | **Existing Ticket?** | **Should Agent Create a Ticket?** | **Action for the Agent (Simple Instruction)** | **Who Resolves the Ticket?** |
| --- | --- | --- | --- | --- |
| **1. First call, issue not resolved** | No | **Yes** | Create new ticket with clear notes | Support/Ops team (assigned owner) |
| **2. Follow-up call for SAME issue** | Yes (Open) | **No** | Open the existing ticket → Add call update | Assigned owner (Support/Ops) |
| **3. Follow-up call, ticket is Closed but SAME issue continues** | Yes (Closed) | **No** | Reopen the ticket & add update | Assigned owner |
| **4. Customer calls for a DIFFERENT issue** | Yes | **Yes** | Create a new ticket for the new issue | Assigned owner |
| **5. Customer calling ONLY for “status update?”** | Yes | **No** | Add follow-up note in existing ticket | Assigned owner |
| **6. Issue fully resolved on the call** | No | **No** | Close the call with a proper disposition | N/A |
| **7. Customer calls again but Agent 2 receives the call (no sticky agent)** | Maybe | If same issue → No  If new issue → Yes | Check tickets → Update existing OR create new | Assigned owner (not the calling agent) |
| **8. Customer provides extra information for an open ticket** | Yes | **No** | Add note to the same ticket | Assigned owner |
| **9. Customer has multiple issues in one call** | No/Yes | **Yes (per issue)** | Create separate tickets for each issue | Assigned owner |

## Chat

| **Scenario** | **Existing Ticket?** | **Should Agent Create a Ticket?** | **Action for the Agent (Simple Instruction)** | **Who Resolves the Ticket?** |
| --- | --- | --- | --- | --- |
| 1. First chat, issue not resolved | No | Yes | Create new ticket with clear description | Support/Ops team (assigned owner) |
| 2. Customer chats again for SAME issue | Yes (Open) | No | Update the existing ticket with chat summary | Assigned owner |
| 3. Customer chats again but old ticket is Closed and SAME issue reappears | Yes (Closed) | No | Reopen the ticket and add chat update | Assigned owner |
| 4. Customer raises a COMPLETELY NEW issue in chat | Yes | Yes | Create a new ticket for the new issue | Assigned owner |
| 5. Customer only asks “status update?” | Yes | No | Add a follow-up note in the existing ticket | Assigned owner |
| 6. Issue resolved completely during chat | No | No | Close chat & document resolution in chat notes | N/A |
| 7. Customer returns to chat later (no sticky agent) | Maybe | If same issue → No  If new issue → Yes | Check existing tickets → Update or create new | Assigned owner |
| 8. Customer sends extra documents/info for an ongoing ticket | Yes | No | Add attachments/info to existing ticket | Assigned owner |
| 9. Customer sends multiple issues in one chat | No/Yes | Yes (per issue) | Create separate ticket(s) for each different issue | Assigned owner |
| 10. Bot escalates chat to agent due to unresolved issue | No/Yes | Check | If issue exists → update ticket; else → create new | Assigned owner |

## **Classification**

1. **Agent performs classification**
    - Determines Issue Type (L1/L2/L3)
    - Sets Product
    - Sets Priority
    - Sets Channel
    - Adds description
2. **System determines routing logic**
    - Auto-assign based on Issue Type and channel
    - Or place into “Unassigned” queue
3. **SLA alerts & reminders trigger**
    - FRT alert to assigned agent
    - SLA breach escalations to TL/Ops

## **Work / Investigation**

1. **Agent begins working on the ticket**
    - Responds to customer
    - Requests missing information
    - Uploads documents
2. **Decision: Is escalation required?**
    - If internal product/tech issue → Jira Ticket Creation
    - If requires Ops or Lender → Raise child ticket to Ops and ops raises it to the Lender
    - If agent can resolve → proceed to resolution

## **Child Ticket Creation & Escalation**

1. **Create Child Ticket (Volt Ops / Product / Tech)**
    - Linked to Parent ID
    - Captures reason, required documents, expected SLA
2. **Parent Ticket moves to “On Hold”**
    - Parent SLA paused or modified (as per policy)
3. **Volt Ops validates child ticket**
4. **Decision: Is lender involvement needed?**
    - If NO → Volt Ops resolves internally
    - If YES → Volt Ops sends request to Lender
5. **Lender responds** (three possibilities):
    - **Approved / Resolved** → Volt Ops updates Child
    - **Needs more information** → Volt Ops requests docs from Agent/Customer
    - **Rejected** → Volt Ops records rejection reason
6. **Volt Ops closes Child Ticket**
    - Adds final notes
    - Uploads lender response
    - Provides TAT & RCA where applicable

## **Parent–Child Sync & Resolution**

1. **System syncs Child Ticket status → Parent Ticket**
    - If child resolved → Parent moves to “Awaiting Customer Confirmation”
    - If child rejected → Parent moves to “Action Required”
2. **Agent validates and communicates resolution**
    - Shares resolution details with Customer/MFD
3. **Decision: Customer accepts resolution?**
    - **Yes → Proceed to Closure**
    - **No → Parent Ticket reopens; SLA resumes**
    - If additional Ops/Lender work needed → create new child ticket

## **Closure & CSAT**

1. **Agent marks Parent Ticket as “Resolved”**
2. **System sends Closure Notification** to Customer/MFD
3. **CSAT triggered** immediately or after X hours
4. **System logs final timestamps** for reporting:
    - Creation time
    - First response
    - Assignment time
    - Escalation timestamps
    - Child ticket sync
    - Closure time

# **Reopen Handling**

1. **Customer reopens ticket within allowed window**
    - Ticket status returns to **Reopened**
    - SLA resumes (or restarts based on policy)
2. **If child ticket required again** → create new child ticket
3. Agent continues resolution loop.

# **Exception Handling**

1. **Customer not responding to agent requests**
    - System sends 2 reminders
    - Auto-closure after X days
2. **Lender SLA breach**
    - Escalate to Volt Ops Lead → Ops Manager → CX Head
3. **Product/Jira SLA breach**
    - Jira escalation to Product Manager / Tech Lead
4. **Incorrect assignment**
    - If ticket is in wrong group → re-assigned with audit trail
5. **Insufficient documentation**
    - Ticket moved to “Awaiting Customer” until docs are provided

# **Ticket Status Flow**

- **New**
- **Open**
- **In Progress**
- **Awaiting Customer**
- **On Hold (Child Ticket Active)**
- **Escalated (Volt Ops / Tech / Lender)**
- **Resolved**
- **Pending RCA**
- **Closed**
- **Reopened**

# **SLA Rules**

- **SLA starts at ticket creation**
- Parent SLA **pauses** when:
    - Child ticket is active
    - Ticket is Awaiting Customer
- **Child ticket SLA** separate for Volt Ops, Product, Lender
- **Escalation hierarchy:**
    
    Agent → Team Lead → Ops Manager → CX Head
    

# **Mandatory Field Validation**

| Stage | Mandatory Fields |
| --- | --- |
| Ticket Creation | Requester, Contact, Subject, Product, Priority, Description |
| Classification | Issue Type (L1/L2/L3), Group, Sub-Product |
| Escalation | Reason, Documents, Lender Name (if applicable) |
| Child Ticket | Parent ID, SLA Class, Owner |
| Closure | Resolution Notes, Sub-status, CSAT trigger |

# **System Integrations**

- **Jira Integration**
    - Create linked Jira ticket
    - Sync status updates back to LSQ
- **Email / WhatsApp Integration**
    - Acknowledgements, reminders, closure messages
- **Reporting Engine**
    - SLA, Reopen Rate, Lender TAT, RCA logs
- **Audit Trail**
    - Every state change recorded with Actor + Timestamp

# **Metrics & Reporting**

- SLA Compliance %
- Pending RCA tickets
- FRT %
- Reopen Rate
- Avg TAT (Agent / Ops / Lender)
- Channel-wise ticket split
- Issue Type distribution
- Escalation rate
- Agent workload & productivity dashboards

# **End-to-End Summary**

This ticket lifecycle ensures:

- Complete traceability
- Structured routing & escalations
- Parent–Child ticket integrity
- SLA governance
- Lender & Product visibility
- Unified reporting
- Consistent customer experience
- Faster resolution through standardised processes