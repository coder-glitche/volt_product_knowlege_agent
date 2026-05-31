# Suspension framework

Last Edited: December 30, 2025 2:23 PM
PRD ETA: November 12, 2025
PRD Owner: Vaibhav Arora
Status: Completed

## What problem are we solving?

Currently, suspensions or blacklisting actions (triggered by screening alerts, loan irregularities, or risk assessments) are handled inconsistently across different systems and entities within the NBFC. This fragmented approach creates several critical issues:

1. **Inconsistent Enforcement**: Different systems apply suspension logic differently, leading to gaps where suspended entities can still transact through certain channels
2. **`Missing Hierarchy Propagation**: When a customer is flagged at PAN level, the suspension doesn't automatically cascade to their existing leads, opportunities, and loans
3. **Limited Audit Visibility**: No centralized record of who suspended an entity, when, why, and what actions were taken
4. **Operational Inefficiency**: Teams spend time manually tracking and enforcing suspensions across multiple systems
5. **Compliance Risk**: Inability to demonstrate robust controls for regulatory audits and risk management

---

## How do we measure success?

- **Zero Suspension Leakage**: No transactions processed for suspended entities (except explicitly allowed actions)
- **Audit Completeness**: 100% of suspension actions logged with user, timestamp, and reason

---

## How are others solving this problem?

### Industry Benchmarks

- Centralized blacklist management systems with customer-level flags
- Manual review and approval workflows for suspensions
- Limited real-time propagation across channels
- Focus on account-level rather than entity-level controls

**Fintech Players:**

- Real-time event-driven suspension frameworks
- Automated rule engines for trigger-based suspensions

**Best Practices Observed:**

- **PayTm**: Hierarchical entity management with cascade logic
- **HDFC Bank**: Comprehensive audit trails with reason codes
- **ICICI Bank**: Granular control at different relationship levels

### Gap Analysis

Most solutions focus on either customer-level OR product-level suspension, but lack:

- Multi-level entity hierarchy with cascading
- Granular control at Lead, Opportunity, and Loan levels
- Flexible permission-based access for different suspension types

---

## What is the solution?

### Solution Overview

A **Unified Suspension Framework** that standardize blocking and control mechanisms across all entities and systems within the NBFC. The framework introduces structured, role-controlled, and auditable suspension capabilities at four entity levels.

### Core Principles

1. **Entity-Centric Design**: Suspension tied to entities (Customer, Lead, Opportunity, Loan) rather than systems
2. **Hierarchical cascading**: Parent suspensions automatically cascade to children
3. **Selective Blocking**: Granular control over which operations are blocked vs. allowed
4. **Audit**: Every action logged with full context
5. **Role-Based Control**: Different teams can suspend at different levels based on permissions

### Four Levels of Suspension

### 1. Customer Level (PAN-based)

- **Scope**: Unique customer entity across the NBFC
- **Impact**: Suspends all existing and future leads, opportunities, and loans
- **Use Cases**: PAN blacklist, fraud flags, compliance violations, customer request
- **Cascading**: Suspends all child entities (leads, opportunities, loans)

### 2. Lead Level (Customer + Channel + Product)

- **Scope**: Specific sourcing relationship
- **Impact**: Blocks all opportunities and loans under that lead; prevents new creation
- **Use Cases**: Channel-specific issues, product-channel combination risks
- **Cascading**: Suspends all opportunities and loans under the lead

### 3. Opportunity Level (Application/Sub-product)

- **Scope**: Specific loan application instance
- **Impact**: Blocks further processing (loan creation); allows unpledging actions
- **Use Cases**: Application-level issues, blocking loan creation for suspended opportunities
- **Cascading**: Does not affect other opportunities

### 4. Loan Level (Post-disbursement)

- **Scope**: Active loan account
- **Impact**: Freezes operational activities (withdrawal, refund, foreclosure, lien removal) while allowing repayments
- **Use Cases**: Loan irregularities, payment defaults, servicing issues
- **Cascading**: Isolated to specific loan

---

## Requirements Overview

### Functional Requirements

- Multi-level entity suspension with hierarchy cascading
- Role-based access control (RBAC) for suspension actions
- Comprehensive audit logging
- Suspension reversal capability
- Real-time status propagation across systems
- API context for LSP integration

### Integration Points

- **Command Centre**: Primary UI for internal teams
- **LOS (Loan Origination System)**: Lead and Opportunity checks and validations
- **LMS (Loan Management System)**: Loan-level enforcement
- **LSP APIs**: Status exposure to lending service providers
- **Risk Engine**: Automated suspension triggers
- **Authentication Service**: RBAC enforcement

---

## User Stories / User Flow

### User Stories

**As a Risk Manager, I want to:**

- Suspend a customer at PAN level so that all their relationships are immediately blocked (existing and future)
- View all entities affected by a suspension
- Provide a clear reason for every suspension action
- Reverse suspensions when issues are resolved

**As an Operations Agent, I want to:**

- Check if a customer/lead/opportunity/loan is suspended before processing
- See the reason and history of suspension
- Know which actions are allowed vs. blocked for a suspended entity

**As a Compliance Officer, I want to:**

- Generate audit reports of all suspension actions
- Track who initiated each suspension and why

**As an LSP Partner, I want to:**

- Receive real-time suspension status via API
- Understand what operations are blocked
- Get notified when suspension status changes

### User Flows

### Flow 1: Risk-Initiated Customer Suspension

`1. Risk Manager logs into Command Centre
2. Searches for customer by PAN
3. Clicks "Suspend Customer"
4. Selects reason from dropdown (e.g., "Screening Alert - PEP")
5. Adds detailed notes and description
6. Confirms suspension
7. System:
   - Validates user permissions
   - Creates suspension record
   - Cascades to all leads, opportunities, loans
   - Logs audit trail
   - Sends notifications/Webhooks
8. All systems immediately reflect suspended status`

### Flow 2: Operations Agent Checking Status

`1. Agent receives loan servicing request
2. Agent opens loan in CC
3. System automatically checks suspension status
4. If suspended:
   - Shows red banner with suspension reason
   - Shows suspension date and initiator
5. Agent explains situation to customer
6. Agent can request suspension review if appropriate` (to be managed operationally)

### Flow 3: Automated Suspension Trigger (Future scope)

`1. Risk engine detects PAN in blacklist
2. Risk engine calls Suspension API
3. System validates trigger rules
4. Creates suspension task with system-generated reason for risk manager to review
5. Cascades to all entities
6. Sends alert to Risk team
7. Risk Manager reviews and can add notes or reject suspension via checker task`

### Flow 4: Suspension Reversal

`1. Risk Manager identifies incorrectly suspended customer
2. Navigates to customer details section
3. Clicks "Reverse Suspension"
4. Adds reversal reason and notes
5. Confirms action
6. System:
   - Validates permissions
   - Marks suspension as reversed
   - Restores entities (unless individually suspended)
   - Logs reversal in audit trail
7. Sends notification to relevant teams`

---

## Requirements

### 1.1 Customer Suspension

Actor will be able to suspend customers using the command centre opportunity view, in future customer level views can be prioritised to have more direct action with deeper integration with Trackwizz (Continuous and initial screening) and CIBIL/Equifax (Credit underwriting).

User flow:

- Alert is created for a customer via initial screening or continuous monitoring (Email is triggered via Trackwizz to the risk team).
- Risk team reviews the case, and decides to approve or reject applications from the customer. In addition to approve or reject the case, Risk team will be able to decide the future relationship with the customer. The customer can be blocked for the following reasons.
    
    
    | **Code** | **Reason** | **Description** |
    | --- | --- | --- |
    | AML_FLAGGED | Flagged under AML or PEP screening | Found in AML/PEP database (WorldCheck, sanction list) |
    | LEGAL_HOLD | Under legal dispute or injunction | Customer under investigation or litigation |
    | FRAUD_SUSPECTION | Suspicious activity under investigation | Interim suspension during fraud probe |
    | REPEATED_REJECTIONS | Repeated KYC or bank verification failures | Pattern of failed verifications |
    | SELF_DECLARED_BLOCK | Customer requested blocking | Voluntary request by customer to block profile |
    | PAYMENT_MANIPULATION | Tampering or reversal attempts | Repayment manipulation through PG/VA |
    | HIGH_DELINQUENCY | History of chronic delinquency | Customer has consistent overdue or write-off history |
    | OTHER |  |  |

### 1.2 Lead Suspension

Actor should be able to perform suspension at Lead level (Customer + Channel + Product) this will block all opportunities and loans under that lead and will prevent creation for new opportunities and loans  and will not affect leads with same customer but different channel/product

**User flow:**

- Operations team identifies repeated issues for an application for a customer from a sourcing channel, or a specific policy violation in the onboarding journey by the customer and the sourcing channel.
- Operations team will search the opportunity for the customer with the specific channel or product and block all future applications for that product by the channel for the customer.

| **Code** | **Reason** | **Description** |
| --- | --- | --- |
| LSP_VIOLATION | LSP violation | Lead sourced from partner under compliance review |
| REPEATED_VERIFICATION_FAILURE | Repeated verification failure | Multiple failed attempts at KYC/bank checks |
| OTHER |  |  |

Lead suspension shall prevent creation of new opportunities and shall not affect leads with same customer but different channel/product. The suspension should cascade to all the opportunities for the lead.

### 1.3 Opportunity Suspension

Actor should be able to perform suspension at an opportunity level  this will block the respective opportunity, utility submission and opportunity submission within the opportunity.

If a loan is created and active for the opportunity, the loan will also be suspended automatically.

| **Code** | **Reason** | **Description** |
| --- | --- | --- |
| BANK_ACCOUNT_MISMATCH | Bank account mismatch | Suspension applied when customer’s bank account details fail validation or mismatch with KYC data, preventing disbursement or lien creation. |
| CUSTOMER_DROP_OFF | Customer dropped off from the application | Applied when the customer abandons the opportunity after partial onboarding or KYC completion, marking the opportunity as inactive. |
| APPLICATION_HARD_REJECTED | Hard rejected application | Applied when the opportunity is permanently rejected due to policy violations, fraud detection, or credit rule failures. |
| OTHER |  |  |

<aside>
💡

Please note that for all suspensions, the operations/risk team should be able to pass remarks as reference notes in the system. These remarks will be further used as an audit as well as to improve reasons for suspensions across entities

</aside>

### 2. Hierarchy & Cascading

![image.png](Suspension%20framework/image.png)

If a top level entity is suspended, the suspension is trickled down to the respective sub entities linked with it. 

### 3. Access Control (RBAC)

| **Permission** | **Operations Agent** | **Support Agent** | **Operations Manager** | **Risk Manager** | **MIS Agent** | **Business** | **Finance** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| View Suspend Status | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| View Suspension Reasons | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Suspend Customer | No | No | Yes | Yes | No | No | No |
| Suspend Lead | Yes | No | Yes | Yes | No | No | No |
| Suspend Opportunity | Yes | No | Yes | Yes | No | No | No |
| Suspend Loan | Yes | No | Yes | Yes | No | No | No |
| Unsuspend Customer | No | No | No | Yes | No | No | No |
| Unsuspend Lead | No | No | No | Yes | No | No | No |
| Unsuspend Opportunity | No | No | No | Yes | No | No | No |
| Unsuspend Loan | No | No | No | Yes | No | No | No |

### Permissions:

### View Suspend Status

**Access Level:** All Roles

**Description:** Ability to check if an entity (Customer/Lead/Opportunity/Loan) is currently suspended

### Suspend Customer

**Access Level:** Operations Manager, Risk Manager

**Impact:**

- New opportunity creation to be blocked
- New lead creation to be blocked
- Opportunity submission for existing opportunity to be blocked
- Existing loans to be suspended/frozen to block new disbursal requests

**Description:** Ability to suspend at PAN level, affecting all child entities

**Includes:**

- Select suspension reason
- Add detailed notes (mandatory)
- Preview impact (affected leads, opportunities, loans)
- Confirm suspension action
- Triggers cascade to all child entities

### Suspend Lead

**Access Level:** Operations Agent, Operations Manager, Risk Manager

- New opportunity creation to be blocked
- Opportunity submission for existing opportunity to be blocked
- Existing loans to be suspended/frozen to block new disbursal requests

**Description:** Ability to suspend specific lead (Customer + Channel + Product combination)

**Includes:**

- Select suspension reason
- Add detailed notes (mandatory)
- Confirm suspension action
- Triggers cascade to opportunities and loans under that lead

### Suspend Opportunity

**Access Level:** Operations Agent, Operations Manager, Risk Manager

**Impact**:

- Opportunity submission for existing opportunity to be blocked
- Existing loans to be suspended/frozen to block new disbursal requests

**Description:** Ability to suspend specific opportunity/application

**Includes:**

- Select suspension reason
- Add detailed notes (mandatory)
- Preview impact (loan if exists)
- Confirm suspension action
- Triggers cascade to loan if exists

### Suspend Loan

**Access Level:** Operations Agent, Operations Manager, Risk Manager

**Impact**:

- Existing loan to be suspended/frozen to block new disbursal requests

**Description:** Ability to suspend specific loan account

**Includes:**

- Select suspension reason
- Add detailed notes (mandatory)
- Confirm suspension action
- No cascade (loan is leaf node)

### Unsuspend Customer (Only customer becomes unsuspended, existing suspended child entities do not automatically unsuspended)

**Access Level:** Risk Manager Only

**Description:** Ability to reverse customer-level suspension

**Includes:**

- View suspension details
- Add reversal reason (mandatory)
- Add reversal notes (mandatory)
- Confirm reversal action
- Reversal logged in audit trail

| **Code** | **Reason** | **Description** |
| --- | --- | --- |
| AML_CLEARED | AML or PEP clearance received | Customer cleared from AML/PEP screening; removed from WorldCheck or sanction list |
| LEGAL_RESOLVED | Legal dispute or injunction resolved | Investigation or litigation concluded; no adverse findings |
| SUSPICION_CLEARED | Suspicious activity investigation cleared | Fraud probe completed; customer cleared of suspicion |
| OTHER | Other valid reason | Any other justified reason for unsuspension with proper documentation |

### Unsuspend Lead

**Access Level:** Risk Manager Only

**Description:** Ability to reverse lead-level suspension

**Includes:**

- View suspension details
- Add reversal reason (mandatory)
- Add reversal notes (mandatory)
- Confirm reversal action
- Reversal logged in audit trail

| Code | Reason | Description |
| --- | --- | --- |
| CHANNEL_ISSUE_RESOLVED | Channel-specific issue resolved | Issues with channel partner or product combination addressed |
| COMPLIANCE_CLEARED | Compliance requirements met | Lead-level compliance documentation verified and approved |
| RISK_REASSESSED | Risk assessment updated - acceptable | Fresh risk evaluation shows acceptable risk for this lead |
| OTHER | Other valid reason | Any other justified reason for unsuspension with proper documentation |

### Unsuspend Opportunity

**Access Level:** Risk Manager Only

**Description:** Ability to reverse opportunity-level suspension

**Includes:**

- View suspension details
- Add reversal reason (mandatory)
- Add reversal notes (mandatory)
- Confirm reversal action
- Reversal logged in audit trail

| **Code** | **Reason** | **Description** |
| --- | --- | --- |
| APPLICATION_VERIFIED | Application documents verified | All application documents validated and approved |
| ELIGIBILITY_MET | Eligibility criteria now met | Customer now meets eligibility requirements for the product |
| CREDIT_APPROVED | Credit assessment approved | Fresh credit evaluation shows acceptable risk |
| TECHNICAL_RESOLVED | Technical issue resolved | System or processing error fixed |
| OTHER | Other valid reason | Any other justified reason for unsuspension with proper documentation |

### Unsuspend Loan

**Access Level:** Risk Manager Only

**Description:** Ability to reverse loan-level suspension

**Includes:**

- View suspension details
- Add reversal reason (mandatory)
- Add reversal notes (mandatory)
- Confirm reversal action
- Reversal logged in audit trail

| Code | Reason | Description |
| --- | --- | --- |
| PAYMENT_REGULARIZED | Payment irregularities resolved | Outstanding dues cleared or payment plan agreed |
| DOCUMENT_VERIFIED | Documentation issues resolved | Required loan documents submitted and verified |
| OPERATIONAL_CLEARED | Operational issue resolved | Technical or processing issues fixed |
| OTHER | Other valid reason | Any other justified reason for unsuspension with proper documentation |

### 4. Audit & Logging

- System shall log every suspension action with: user ID, timestamp, entity ID, entity type, reason, notes
- System shall log every reversal action with: user ID, timestamp, reversal reason, notes

### 5. Reason Management

- System shall maintain master list of suspension reasons
- Users shall be able to add free-text notes with any reason

### 6. Suspension Status & Visibility

- System shall expose suspension status, and reason via real-time API in the get details API for each entity:
    - Get Opportunity: Status: Suspended, Reason
    - Get Customer details: Status: Suspended, Reason
    - Get Lead: Status: Suspended, Reason
    - Get loan details and summary: Status: Suspended, Reason
- Command Centre shall display suspension status prominently on all entity pages (Opportunity / Loan) - Currently lead detail page will show status for both Customer and Lead, opportunity and loan will have their statuses respectively
- LOS shall check suspension before: lead creation, opportunity creation, application processing
- LMS shall check suspension before: disbursement, withdrawal, foreclosure, lien removal
- System shall provide suspension status history

### 7. Reversal & Exception Handling

Actors should be able to un-suspend entities, unlike suspension, un-suspension will not be cascaded, and will be at an entity level.

That is, un-suspension actions will operate strictly at the entity level. While suspensions cascade downward across hierarchy (Customer → Lead → Opportunity → Loan), the reversal process will not cascade upward or downward.

Example:
If a customer is un-suspended, the leads, opportunities, and loans previously suspended under that customer will remain in suspended state until explicitly un-suspended at their respective levels.

Controlled Governance:
This design ensures that risk or compliance overrides are intentional and traceable, avoiding inadvertent reactivation of lower-level entities that may still be under review or flagged independently.

Audit & Logging:
Each un-suspension event will be logged with user ID, timestamp, entity reference, and justification. This allows clear traceability for exception handling or retrospective review.

Outcome:
This approach prevents blanket reactivation and enforces granular control, ensuring reinstatement only when the specific suspension reason is resolved

## Design

### UI Design Guidelines

### Command Centre - Suspension Interface

**Customer Page:**

- Prominent suspension banner if active (red background similar to loan)
- "Suspend Customer" button (top-right) in the actions tab
- Suspension history tab showing all suspensions and reversals (Phase 2)

**Suspension Modal:**

- Reason dropdown (required)
- Submit and Cancel buttons

**Suspension Status Badge:**

- Red badge with "SUSPENDED" label
- Hover shows: Reason, Suspended by, Date
- Click opens full suspension details

---

## Analytics

### Tracking Events

**Suspension Actions:**

- `suspension_created` - track entity_type, reason_code, user_role
- `suspension_reversed` - track reason, timestamp
- `suspension_cascade_triggered` - track parent_entity, (suspension trigger)
- `suspension_status_checked` - track entity_type, source_system

**Usage Metrics:**

- `suspensions_by_reason` - track frequency of each reason
- `suspensions_by_entity_type` - track distribution
- `suspensions_by_user_role` - track who suspends most