# DSP QC Reject Handling in LSQ

: Naman Agarwal
Created time: January 14, 2025 7:03 PM
Status: In progress
Last edited: February 27, 2025 7:48 PM

# Custom Activity Configuration: DSP QC Rejection

### Problem Statement

Currently, when DSP operations team rejects an applicationBased on Risk/compliance reasons, they need customer to Re attempt some step.

- That increases Risk of customer application Abandonment
- Customer might not see the message based communication
- Sales team don’t have the List of applications in QC reject to reach out to Customer over a call and get them to complete the applications

### Success Metrics

1. **Primary Metrics**
    - Reduction in application abandonment rate post-QC rejection
    - Decrease in time to resolution for QC issues
    - Sales team response time to QC rejections
2. **Secondary Metrics**
    - Increase in first-time-right applications by understanding the Common QC reject issues

## User Personas & Journey

### 1. DSP Ops Team

- Reviews loan applications
    - Identifies risk/compliance issues
    - Rejects the application on CC
    - Provides detailed feedback on CC
    
    ### 2. Sales Team
    
    - Receives QC rejection notifications
    - Contacts customers for updates
    - Guides application completion
    - Updates activity status
    
    ### 3. Customer - borrower
    
    - Receives rejection notification
    - Needs to update application
    - Requires clear guidance
    - Expects minimal friction

## 1. Activity Setup in LeadSquared

Using LeadSquared's Custom Activities & Scores section:

### 1 Basic Configuration

- Activity Display Name: DSP_QC_Rejection
- Activity Code: 268
- Score: 0
- Show in Activity List: Yes
- Delete Activity: Yes

### 1.1 Activity Setup in LeadSquared

```json

{
  "ActivityEventName": "DSP_QC_Rejection",
  "Code": "268",
  "Score": 0,
  "ShowInActivityList": true,
  "CanDeleteActivity": true
}

```

![Screenshot 2025-02-21 at 4.00.31 PM.png](DSP%20QC%20Reject%20Handling%20in%20LSQ/Screenshot_2025-02-21_at_4.00.31_PM.png)

### 1.2 Custom Fields

1. **Notes Field**
    - Display Name: Notes
    - Schema Name: ActivityEvent_Note
    - Type: String
    - Purpose: Capture rejection reasons
2. **Status Field**
    - Display Name: Status
    - Schema Name: Status
    - Type: Dropdown
    - Options:
        - Pending Review
        - Customer Contacted
        - Update Required
        - Update Received
        - Resolved
3. **Owner Field**
    - Display Name: Owner
    - Schema Name: Owner
    - Type: User
    - Purpose: Track responsibility

### 2.1 API Call for Creating Activity

```json

POST https://{host}/v2/ProspectActivity.svc/Create
{
  "RelatedProspectId": "[LEAD_ID]",
  "ActivityEvent": "268",
  "ActivityNote": "[QC_REJECTION_NOTES]",
  "Fields": [
    {
      "SchemaName": "Status",
      "Value": "Pending"
    },
    {
      "SchemaName": "Owner",
      "Value": "[ASSIGNED_SALES_REP]"
    }
  ]
}

```

### 2.2 Application Logic

1. When QC team rejects application:
    - Create activity with rejection details
    - Set initial status as "Pending"
    - Assign to original sales owner
    - Return customer to specific application section
2. Trigger Conditions:
    - Activity created when QC team selects rejection reason
    - Status updates when sales team takes action
    - Completion marked when customer updates required information

### 3 Activity View

- Display in main activity timeline
- Show rejection reason from Notes field
- Display current status and owner
- Enable filtering by DSP_QC_Rejection activities

![image (29).png](DSP%20QC%20Reject%20Handling%20in%20LSQ/image_(29).png)