# LSQ misattribution b2c of B2b2c data

: Naman Agarwal
Created time: November 26, 2024 12:50 PM
Status: Ready for Tech
Last edited: November 27, 2024 11:25 AM

# B2C to B2B2C Lead Update Specification

## Background

When MFD (Mutual Fund Distributor) B2B2C leads originate from a B2C platform, we currently use admin actions to assign a lead MFD partner. While the MFD details are stored in our database, they are not synchronized with LeadSquared (LSQ). This creates two primary issues:

1. Lead tracking inefficiencies
2. Service misalignment (B2B2C leads incorrectly assigned to B2C support teams)
3. MFD partner dissatisfaction with direct customer contact

## Objective

Reduce misattributed leads

- Reduce Creation of the new Misattributed leads.
- Update LSQ with admin action (tech pickup)
- Backfill data  to correct misattribution

Implement functionality to update existing B2C leads to B2B2C leads in LeadSquared by synchronizing referral data from our database.

## Technical Implementation

### API Details

- **Endpoint**: POST [http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate](http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate)
- **Identifier**: Mobile Number (unique in LSQ)

### Required Field Updates

```json
{
    "LeadDetails": [
        {"Attribute": "mx_Channel", "Value": "B2B2C"},
        {"Attribute": "Source", "Value": "MFD Referral"},
        {"Attribute": "mx_Referred_By", "Value": "MFD"},
        {"Attribute": "mx_Referrer_Name", "Value": "[MFD_NAME]"},
        {"Attribute": "mx_Referrer_Phone", "Value": "[MFD_PHONE]"},
        {"Attribute": "mx_Referrer_Email", "Value": "[MFD_EMAIL]"},
        {"Attribute": "mx_Referrer_Account_Id", "Value": "[MFD_ID]"},
        {"Attribute": "mx_Referral_Code", "Value": "[REFERRAL_CODE]"},
        {"Attribute": "Phone", "Value": "[CUSTOMER_PHONE]"},
        {"Attribute": "SearchBy", "Value": "Phone"}
    ]
}

```

## Data Migration Plan

### Initial Data Reconciliation

- Tech team to provide excel export of leads updated via admin actions
- Data to be shared with LSQ team for backfill
- Impact: Approximately 12% of leads are currently miscategorized (Extrapolated form a daily count)

### Scope Limitations

- Full LSQ-DB reconciliation not feasible due to lack of MFD assignment markers in LSQ
- Focus on forward data synchronization and provided historical data only

### MFD Status Handling

- Automated daily updates for partially-activated MFD status

## Requirements

### Technical Requirements

1. Admin action implementation for borrower-partner relationship updates
2. API integration with error handling
3. Comprehensive update logging for audit purposes

### Acceptance Criteria

1. Successful lead type transition (B2C to B2B2C)
2. Accurate referrer information mapping
3. Proper API response handling
4. Complete audit logging
5. Visual verification in LSQ dashboard

## Important Notes

- Mobile Number serves as the unique identifier in LSQ
- Lead merges occur when same email is used with different phone numbers
- Implementation must include robust error handling for API failures - API failures should be notified to the team.