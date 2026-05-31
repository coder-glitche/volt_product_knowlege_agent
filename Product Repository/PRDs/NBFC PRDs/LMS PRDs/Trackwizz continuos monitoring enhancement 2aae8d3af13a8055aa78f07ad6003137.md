# Trackwizz continuos monitoring enhancement

Last Edited: November 13, 2025 12:39 PM
PRD Owner: Vaibhav Arora

# Contract Changes Required for Stopping Continuous Monitoring - AS504 API

## Executive Summary

Based on the AS504 API documentation, the following contract modifications are necessary to effectively discontinue continuous monitoring (Purpose 04) for customers while managing ongoing screening operations.

---

## 1. API Purpose Codes & Termination Logic

### Current Purpose Definitions

- **Purpose 01**: Initial Screening with API Response and No Storage
- **Purpose 03**: Initial Screening with API Response and TW Workflow
- **Purpose 04**: Continuous Screening with TW Workflow

### Key Finding

To stop continuous monitoring, contracts must clarify the mechanisms for Purpose 04 discontinuation, as there is no explicit "Purpose 05" for stopping monitoring in the current API specification.

---

## 2. Required Contract Amendments

### 2.1 Data Retention & Deactivation Terms

**Required Changes:**

### 2.1.1 Customer Status Field Modification

- **Field**: `status` (Customer Status Enum)
- **Current Values**: Active, Closed, Dormant, Inactive, Suspended
- **Contract Change**: Add explicit condition:

`When a customer record's purpose changes from "04" (Continuous Screening) 
to either "01" or "03" (Initial Screening only), the system must:

1. Cease real-time continuous screening operations
2. Maintain historical screening records for audit/compliance purposes
3. Update effectiveDate to reflect when continuous monitoring ended
4. Mark continuous monitoring as "Terminated" in internal tracking`

**Effective Date Requirements:**

- Must be provided in "DD-MMM-YYYY" format
- Should reflect the exact date when continuous monitoring ceases
- Cannot be a future date (must be current or past)

---

### 2.2 Purpose Code Combination Restrictions

**Contract Required Clause:**

The API currently allows:

- Purpose 01 & Purpose 04 (combination allowed)
- Purpose 03 & Purpose 04 (combination allowed)

**To Stop Continuous Monitoring**, the contract must specify:

`Transition Rules for Discontinuing Continuous Monitoring:

1. If Purpose 04 is removed from a request while Purpose 01 or 03 remains:
   - Continuous monitoring CEASES immediately
   - Initial screening continues as specified
   - Customer record remains in TrackWizz but without ongoing monitoring

2. If ONLY Purpose 04 is passed in a new request:
   - Continuous monitoring CONTINUES unchanged
   
3. If NEITHER Purpose 01, 03, nor 04 is passed:
   - Request is REJECTED per validation MRV12`

---

### 2.3 Mandatory Fields for Terminating Continuous Monitoring

**Contract Clause - Purpose 04 Discontinuation:**

When removing Purpose 04, the following fields become mandatory:

```
FieldRequirementFormatPurposesourceSystemCustomerCodeMandatoryString (Max 100)Identifies record to stop monitoringsourceSystemNameMandatoryEnum (Agency Code)System initiating terminationconstitutionTypeMandatoryEnumCustomer type (IND/LE)statusMandatoryEnumShould be "Closed" or "Inactive" to stop monitoringeffectiveDateMandatoryDD-MMM-YYYYDate when continuous monitoring endsfirstName ORpan ORpasscodeMandatory (one of)StringFor verification of customer recordcorrespondenceAddressCountryMandatoryEnumFor validation purposescorrespondenceAddressLine1MandatoryStringFor validation purposescorrespondenceAddressStateMandatoryEnumFor validation purposescorrespondenceAddressZipCodeMandatoryStringFor validation purposes
```

---

### 2.4 Screening Profile & Report Handling

**Contract Amendment Required:**

When discontinuing continuous monitoring:

`1. screeningProfile Field:
   - Can be passed to specify final screening profile used
   - If left blank, the system retains the last active profile
   - No new hits will be generated after termination

2. screeningReportWhenNil Parameter:
   - Values: "0" (No) or "1" (Yes)
   - When Purpose 04 is stopped:
     * screeningReportWhenNil becomes irrelevant
     * Set to "0" or leave empty to prevent final report generation
     * Set to "1" if final screening report required as termination record

3. riskProfile Field:
   - Current risk profile is locked when monitoring ends
   - Future assessments are not performed
   - Historical risk rating remains available for audit`

---

### 2.5 Related Persons & Relations - Impact on Monitoring Termination

**Contract Requirement:**

When discontinuing Purpose 04 for Legal Entities with Related Persons:

`1. Customer Continuous Monitoring (Purpose 04) - CEASES
   
2. Related Person Screening - DEPENDS ON PURPOSE PASSED:
   - If Purpose 01 or 03 passed → Related persons screened one-time only
   - If no purpose passed for related persons → Related persons also stop monitoring
   
3. Relation Tracking:
   - relatedPersonRelationResponse continues to display historical relations
   - Future relation updates will NOT trigger continuous monitoring
   - Relation data retention follows the Primary Customer termination date

4. Mandatory Relation Fields When Stopping Monitoring:
   - customerSourceSystemCode (identifies LE)
   - relatedPersonSourceSystemCode (identifies RP)
   - relationCode (specifies relationship type)
   - relationStartDate (when relationship began)
   - relationEndDate (MUST be passed when stopping monitoring)
   - shareHoldingPercentage (if applicable)`

---

## 3. Validation Changes & Error Handling

### 3.1 New Validation Rules Required in Contract

**Validation Code**: VS_STOP_04

`When Purpose 04 is discontinued (removed from request):

Validation Message: "Continuous Screening (Purpose 04) for customer 
{sourceSystemCustomerCode} has been terminated as of {effectiveDate}. 
No future hits will be generated."

This is an INFO-level message, not a rejection.`

### 3.2 Existing Validations Applicable to Termination

```
CodeValidationImpact on DiscontinuationMRV7Purpose 01, 02, 03 together not allowedPass Purpose 01 alone to stop Purpose 04MRV14ConstitutionType is mandatoryRequired for identifying correct recordVS1PAN/FormSixty - Either value requiredEnhanced verification when stoppingVS20If permanent address passed, AddressLine1 and PIN mandatoryValidation still appliesVS31If Correspondence address passed, Permanent address mandatoryApplies during termination requestVS42Status & EffectiveDate mandatoryCRITICAL for termination
```

---

## 4. Response Structure Changes

### 4.1 Purpose Response When Discontinuing Purpose 04

**Current Structure for Purpose 04:**

json

`{
  "purpose": "Continuous Screening with TW Workflow",
  "purposeCode": "04",
  "data": null,
  "validationCode": "",
  "validationDescription": "",
  "validationFailureCount": 0
}`

**Required Contract Change - When Terminating:**

json

`{
  "purpose": "Continuous Screening with TW Workflow",
  "purposeCode": "04",
  "terminationStatus": "Stopped",
  "terminationEffectiveDate": "DD-MMM-YYYY",
  "data": {
    "hitsDetected": "No",
    "hitsCount": 0,
    "confirmedHits": "No",
    "reportData": null,
    "hitResponse": [],
    "message": "Continuous monitoring has been successfully terminated"
  },
  "validationCode": "VS_STOP_04",
  "validationDescription": "Continuous Screening (Purpose 04) terminated successfully",
  "validationFailureCount": 0
}`

### 4.2 Overall Status Response

**Contract Requirement for Termination Scenarios:**

`overallStatus values when stopping continuous monitoring:

1. "AcceptedByTW" - Termination request accepted, monitoring stopped
2. "RejectedByTW" - Termination failed (missing mandatory fields, invalid status)

The response data field must include:
- terminationTimestamp: When monitoring actually stopped in system
- lastScreeningDate: Date of last screening performed under Purpose 04
- archivedReportData: Link/reference to final screening report (if generated)`

---

## 5. Data Management & Compliance Terms

### 5.1 Historical Data Retention

**Contract Clause - Data After Discontinuation:**

`Post-Discontinuation Data Management:

1. RETENTION: All screening records generated during continuous monitoring
   shall be retained indefinitely for audit and compliance purposes.

2. ARCHIVAL: Upon Purpose 04 discontinuation, all related hit data,
   case records, and workflow actions are moved to archived state
   but remain queryable for regulatory purposes.

3. NO DELETION: No screening data shall be deleted. The system only
   stops GENERATING new screening results.

4. ACCESS: Historical records remain accessible through:
   - TrackWizz Case Manager
   - API queries using sourceSystemCustomerCode
   - Compliance/Audit reports`

### 5.2 Storage Implications

**Contract Requirement:**

`Storage Behavior Upon Purpose 04 Discontinuation:

Purpose 01: Initial Screening (No Storage)
→ Customer NOT stored in TrackWizz

Purpose 03: Initial Screening (TW Workflow)
→ Only case details stored (if hits detected)

Purpose 04: Continuous Screening (TW Workflow)
→ FULL customer record stored for continuous monitoring

Discontinuation Scenario:
- If switching from Purpose 04 to Purpose 01:
  * Full record is RETAINED (not deleted)
  * Continuous monitoring flag is SET TO FALSE
  * No new hits generated going forward
  
- If switching from Purpose 04 to Purpose 03:
  * Full record is RETAINED
  * One-time screening performed with new request
  * Continuous monitoring flag is SET TO FALSE`

---

## 6. Service Level Agreement (SLA) Changes

### 6.1 Monitoring Cessation Timeline

**Contract SLA for Purpose 04 Discontinuation:**

`Upon receiving a valid discontinuation request:

1. Immediate Processing (< 1 minute):
   - Request received and validated
   - Purpose 04 flag updated to inactive
   
2. System Synchronization (< 5 minutes):
   - No new screening queries sent to watchlist sources
   - Any in-flight screening requests are cancelled if possible
   
3. Confirmation (< 10 minutes):
   - Confirmation response sent to client
   - Historical records marked as archived
   - Compliance logs updated

4. Final Settlement (< 1 business day):
   - Final report generated (if requested)
   - All pending workflows closed
   - Dashboard updated for end users`

### 6.2 Communication Requirements

**Contract Change - Notification Upon Discontinuation:**

`When Purpose 04 is successfully discontinued:

1. TO SYSTEM: Response JSON includes terminationStatus = "Stopped"

2. TO END USERS: Email notification (if applicable per original Purpose 03/04 setup)
   - Subject: "Continuous Screening Terminated for Customer [CODE]"
   - Content: Effective date, reference number, archive location
   
3. TO AUDIT: System logs capture:
   - Discontinuation request timestamp
   - Authorizing user/system
   - Effective termination time
   - Last screening date`

---

## 7. Sample Implementation Scenarios

### Scenario 1: Stop All Monitoring (Purpose 04 Only)

**Previous Request:**

json

`{
  "purpose": "04",
  "sourceSystemCustomerCode": "CUST-001"
}`

**Termination Request:**

json

`{
  "requestId": "TERM-20250113-001",
  "purpose": "01",  *// Changed from "04"*
  "sourceSystemName": "Finacle",
  "customerList": [
    {
      "sourceSystemCustomerCode": "CUST-001",
      "constitutionType": "1",
      "status": "Inactive",
      "effectiveDate": "13-Jan-2025",
      "firstName": "John",
      "correspondenceAddressCountry": "IND",
      "correspondenceAddressLine1": "123 Main St",
      "correspondenceAddressState": "MH",
      "correspondenceAddressZipCode": "400001"
    }
  ]
}`

**Response:**

json

`{
  "requestId": "TERM-20250113-001",
  "response": {
    "overallStatus": "AcceptedByTW",
    "customerResponse": [
      {
        "sourceSystemCustomerCode": "CUST-001",
        "purposeResponse": [
          {
            "purposeCode": "01",
            "terminationStatus": "Purpose 04 monitoring stopped",
            "terminationEffectiveDate": "13-Jan-2025"
          }
        ]
      }
    ]
  }
}`

### Scenario 2: Continue Initial Screening, Stop Continuous

**Previous Request:**

json

`{
  "purpose": "01,04",
  "sourceSystemCustomerCode": "CUST-002"
}`

**Termination Request:**

json

`{
  "purpose": "01",  *// Remove 04*
  "sourceSystemCustomerCode": "CUST-002"
  *// Include mandatory fields as per Purpose 01 requirements*
}`

---

## 8. Risk Mitigation & Exception Handling

### 8.1 Potential Issues During Discontinuation

```
IssueContract ResolutionIn-Flight Screening: Ongoing screening when termination requestedCancel with status "TERMINATED_BEFORE_COMPLETION"Pending Hits: Hits generated but not yet deliveredDeliver final batch with "Last Screening" flagRelated Persons: RP continuous monitoring state unclearExplicitly link RP monitoring cessation to Parent LE terminationDispute Resolution: Client claims monitoring continued after requestQuery lastScreeningDate and provide audit logs
```

### 8.2 Contract Language for Edge Cases

`Edge Case 1: Customer status is "Closed" but Purpose 04 still active
→ System should automatically stop Purpose 04 if not already terminated
→ Send notification to client about auto-termination

Edge Case 2: Multiple discontinuation requests for same customer
→ First valid request wins
→ Subsequent requests receive "Already Terminated" response
→ Effective date of first request honored

Edge Case 3: Related Person monitoring stops, but Parent company continues
→ RP monitoring MUST stop independent of parent company status
→ Relation data preserved but no future RP screening conducted`

---

## 9. Compliance & Audit Requirements

### 9.1 Mandatory Audit Trail

**Contract Requirement:**

`The API implementation must maintain audit logs capturing:

1. Original Purpose 04 start date (from first enrollment)
2. All Purpose code changes over customer lifetime
3. Discontinuation request date and time (ISO 8601 format)
4. Authorizing source system and user ID
5. Last successful screening before discontinuation
6. Reason code for discontinuation (if provided by client)
7. Cryptographic hash of request/response for immutability`

### 9.2 Regulatory Compliance

**Contract Clause:**

`By discontinuing Purpose 04 (Continuous Screening), both parties 
acknowledge that:

1. The customer is no longer subject to ongoing AML/CFT screening
   as of the effective date specified.

2. Historical screening records are retained solely for compliance
   and audit purposes and shall not be used for ongoing monitoring.

3. The customer record remains available in the system for:
   - Future one-time screening requests
   - Historical data queries
   - Regulatory/law enforcement requests

4. Neither party shall use the archived record for any purpose
   beyond regulatory compliance without re-initiating Purpose 01
   or Purpose 03 screening.`

---

## 10. Implementation Checklist

- [ ]  Update Master Service Agreement to define Purpose 04 termination process
- [ ]  Amend SLA to include discontinuation response times
- [ ]  Revise data retention policy with post-discontinuation archival terms
- [ ]  Document effective date requirements for monitoring cessation
- [ ]  Define escalation procedures if discontinuation fails
- [ ]  Establish audit logging requirements per compliance standards
- [ ]  Create termination request templates and samples
- [ ]  Train support teams on discontinuation procedures
- [ ]  Update API documentation with discontinuation workflow
- [ ]  Establish monitoring dashboard showing active Purpose 04 records
- [ ]  Implement automated alerts when monitored customer status changes
- [ ]  Create rollback procedures in case discontinuation needs reversal

---

## 11. Critical Takeaways

1. **No Explicit "Stop" Purpose Code**: The AS504 API does not have a dedicated Purpose 05 for stopping monitoring. Instead, discontinuation is achieved by removing Purpose 04 from request and providing valid status/effective date.
2. **Mandatory Fields for Termination**: Unlike Purpose 04 requests (which accept limited fields), discontinuation requires FULL customer record with all mandatory fields including addresses and status.
3. **Effective Date is Key**: The `effectiveDate` field in `DD-MMM-YYYY` format marks when continuous monitoring ceases. Must be current or past date.
4. **Data Retention, Not Deletion**: Discontinuation stops future screening but retains all historical records. This is critical for compliance.
5. **Status Field Critical**: Setting customer status to "Inactive" or "Closed" and providing `effectiveDate` is the primary mechanism to stop Purpose 04 monitoring.
6. **Purpose Code Combination**: To stop Purpose 04, either pass Purpose 01/03 alone, or remove Purpose 04 from the purpose list.

---

## Conclusion

Contract modifications must explicitly address:

- The mechanism for discontinuing Purpose 04 monitoring
- Mandatory fields and validation rules for termination requests
- Data retention and archival policies post-discontinuation
- Timeline commitments for cessation of monitoring activities
- Audit trail requirements for compliance purposes
- Status change procedures that trigger monitoring cessation

These changes ensure clear contractual obligations, reduce ambiguity, and provide both parties with explicit procedures for managing continuous monitoring lifecycle.