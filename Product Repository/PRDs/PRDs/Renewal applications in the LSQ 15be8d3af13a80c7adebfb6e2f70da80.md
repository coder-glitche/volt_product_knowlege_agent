# Renewal applications in the LSQ

: Naman Agarwal
Created time: December 13, 2024 2:20 PM
Status: Not started
Last edited: December 17, 2024 7:16 PM

# Customer Lead Renewal Flow

## Customer lead and opportunity creation steps for Renewal

- Create renewal opportunity using lead create and update API
- Save renewal opportunity id
- Post opportunity update
- Post activity on opportunity

## Case Scenarios

### Case 1: Customer initiating renewal through MFC Landing page

- Create renewal opportunity if existing loan is near maturity
- When user clicks on "Renew loan" update opportunity stage to renewal_initiated
- If renewal opportunity already exists, post activity for existing opportunity

### Case 2: Customer initiating renewal through Android/iOS app

When user's existing loan is near maturity:

- Create renewal opportunity if renewal opportunity doesn't exist
- Post activity and update opportunity attributes if renewal opportunity exists
- Post "Renewal initiated" activity
- Update portfolio verification status

### Case 3: Customer initiating renewal through Web App

When user's existing loan is near maturity:

- Create renewal opportunity if renewal opportunity doesn't exist
- Post activity and update opportunity attributes if renewal opportunity exists
- Update portfolio verification status
- Post activity for renewal journey progress

### Case 4: System-initiated renewal notification

- System identifies loans approaching maturity (30 days before)
- Create renewal opportunity if eligible
- Send notification to customer
- Track customer response through activities

## Renewal Lead/Opportunity Attributes

| Lead field name | Data type | Lead Schema name | Opportunity Schema name | Comment | Status |
| --- | --- | --- | --- | --- | --- |
| Original Loan ID | Text | mx_Original_Loan_Id | mx_Custom_70 | Required | sending |
| Renewal Type | Dropdown | mx_Renewal_Type | mx_Custom_71 | Standard/Enhanced | sending |
| Original Maturity Date | Date | mx_Original_Maturity_Date | mx_Custom_72 | Required | sending |
| Portfolio Re-verification | Boolean | mx_Portfolio_Verified | mx_Custom_73 | Required | sending |
| Renewal Amount | Number | mx_Renewal_Amount | mx_Custom_74 | Required | sending |
| Original Loan Amount | Number | mx_Original_Loan_Amount | mx_Custom_75 | Required | sending |
| Days to Maturity | Number | mx_Days_To_Maturity | mx_Custom_76 | System Calculated | sending |
| Renewal Eligibility | Boolean | mx_Renewal_Eligible | mx_Custom_77 | System Calculated | sending |

## Renewal Stage Progression

### Active Stages

- Renewal_Eligible
- Renewal_Initiated
- Portfolio_Verification
- Documentation_Update
- Agreement_Signing
- Mandate_Setup
- Renewal_Processed
- Renewal_Complete

## Custom Activities for Renewal

| Activity Name | Description | Stage Update |
| --- | --- | --- |
| Renewal_Eligible_Notification | System identifies eligible loan | Renewal_Eligible |
| Renewal_Initiated | Customer starts renewal process | Renewal_Initiated |
| Portfolio_Verification_Complete | Portfolio value verified | Portfolio_Verification |
| Documentation_Updated | Required documents updated | Documentation_Update |
| Renewal_Agreement_Signed | New agreement signed | Agreement_Signing |
| Renewal_Mandate_Setup | Bank mandate updated | Mandate_Setup |
| Renewal_Processing | Final processing stage | Renewal_Processed |
| Renewal_Completed | Renewal process complete | Renewal_Complete |

## API Integration Points

### Create Renewal Opportunity

```
POST /v2/ProspectActivity.svc/CreateCustom
Host: api-in21.leadsquared.com
Parameters:
- Original Loan ID
- Renewal Type
- Portfolio Value
- Renewal Amount

```

### Update Renewal Stage

```
POST /v2/ProspectActivity.svc/Update
Parameters:
- Opportunity ID
- New Stage
- Activity Details

```

## Open Items

- Define SLA for renewal processing
- Setup renewal-specific automations in LSQ
- Configure renewal eligibility notifications
- Define portfolio re-verification rules
- Setup renewal tracking dashboard
- Define renewal-specific MIS reports

## Note

- Renewal opportunities must be linked to original loan application
- Portfolio verification is mandatory for all renewals
- KYC update required if existing KYC is older than 2 years
- Bank mandate must be active or renewed
- All renewal activities must be tracked in LSQ

# MFD Lifecycle and LSQ Integration PRD

## 1. Project Overview

### Objective

Align RedVision MFD functionality with Volt MFDs by implementing comprehensive lifecycle management and LSQ integration.

### Success Criteria

- Complete feature parity between RedVision and Volt MFDs
- Successful integration with LSQ for lead management
- Automated lifecycle stage transitions
- Accurate tracking of referrals and performance metrics

## 2. Technical Requirements

### 2.1 Integration Points

### LSQ Integration

1. Lead Capture API Integration
    - Implement direct lead capture from LSQ
    - Support real-time lead creation and updates
2. Universal Lead Capture (ULC) Connector
    - Convert activities to B2C/MFD leads
    - Process partner events and status updates
3. Manual Entry Support
    - Enable data entry through LSQ portal
    - Maintain data consistency with automated entries

### 2.2 MFD Lifecycle Management

### Stage Transitions

1. Unregistered
    - Initial stage for new MFD leads
    - System assignment for 30-minute evaluation
    - Automatic transition to MFD Sales Team if unchanged
2. Registered
    - Enhanced data collection
    - Verification process initiation
    - Basic requirement validation
3. Empanelled
    - Documentation verification
    - System access setup
    - Transition to Onboarding Expert Team
4. Partially Activated
    - Feature access provisioning
    - Training module activation
    - Progress tracking implementation
5. Fully Activated
    - Triggered by first customer loan approval
    - Transition to Relationship Manager Team
    - Complete access grant

### 2.3 Data Processing

### Event Handling

Must support the following partner events:

- PARTNER_ACCOUNT_CREATED
- PARTNER_ACCOUNT_UPDATED
- PARTNER_CUSTOMER_LOAN_CREATED
- PARTNER_CUSTOMER_BORROWER_ACCOUNT_CREATED
- PARTNER_CUSTOMER_LEAD_CREATED
- PARTNER_CUSTOMER_MFC_LIMIT_CHECK
- PARTNER_CUSTOMER_CAMS_ASSET_FETCH_STEP
- PARTNER_CUSTOMER_KFIN_ASSET_FETCH_STEP
- PARTNER_ACCOUNT_PARTNER_REFERRED
- PARTNER_ACCOUNT_REFERRAL_DETAILS_UPDATED

### External System Integration

1. CAMS Integration
    - Mutual Fund data fetching
    - Portfolio activity tracking
2. KFIN Integration
    - Asset data synchronization
    - Performance metrics collection

## 3. Performance Tracking

### 3.1 Metrics

- Number of completed customers
- Total referred customers
- Conversion rates by stage
- Time in each lifecycle stage
- Partner referral statistics

### 3.2 Reporting Requirements

- Real-time status updates
- Performance dashboards
- Activity logs
- Referral tracking

## 4. Implementation Considerations

### 4.1 Technical Dependencies

- LSQ API access
- CAMS/KFIN integration capabilities
- Existing Volt MFD system access

### 4.2 Data Migration

- Plan for RedVision data transfer
- Data mapping between systems
- Historical data handling

## 5. Next Steps

1. Technical Assessment
    - Review current Volt MFD implementation
    - Document gaps between RedVision and Volt MFDs
    - Evaluate RedVision data sources
2. Development Planning
    - Gather development effort estimates
    - Create implementation timeline
    - Identify resource requirements
3. Integration Strategy
    - Define API integration approach
    - Plan testing strategy
    - Establish rollout phases

#