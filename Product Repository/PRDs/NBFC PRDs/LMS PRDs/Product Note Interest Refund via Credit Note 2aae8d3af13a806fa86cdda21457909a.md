# Product Note: Interest Refund via Credit Note

Last Edited: January 23, 2026 8:15 PM
PRD ETA: July 22, 2025
PRD Owner: Vaibhav Arora
Status: Completed

## Background and Context

**Who is facing the problem:**

- End customers awaiting resolution of incorrectly charged or goodwill interest waivers
- Operations team processing interest refunds/waivers
- Finance team managing manual accounting entries for interest reversals
- Tech ops/Product handling backend interventions for interest adjustments

**What is the challenge that they are facing? What is broken today?**

- Interest refunds and waivers currently require manual engineering intervention through backend APIs or direct Finflux access
- Process is operationally intensive with dependency on Jira ticket workflows
- No standardized maker-checker workflow for interest refunds similar to charge refunds
- Manual JV posting for interest reversals creates additional overhead for Finance team
- Lengthy resolution time (2-3 days) impacting customer experience
- No automated validation mechanism to prevent duplicate interest waivers or refunds for the same period
- Lack of visibility and tracking for interest refund requests across the loan lifecycle

**Why is it important? What is getting impacted?**

- Customer satisfaction is negatively impacted due to delayed resolution of legitimate interest refund requests
- Operational inefficiency with high manual effort required for each interest refund case
- Risk of errors and duplicate processing without systematic validations
- Finance team bandwidth consumed by repetitive manual JV entries
- Lack of audit trail and reconciliation capabilities for interest reversals
- Inconsistent treatment of interest refunds compared to the now-standardised charge refund process

---

## 1. Problem Scope

### In scope

**What specific problems are we solving?**

1. **Slow Resolution Time:**
    - Interest refund requests take 2-3 days to resolve from initiation to completion
    - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times
    - Delays compound when requests require back-and-forth clarifications between operations, engineering, and product
2. **Operational Bottleneck and Dependency:**
    - Operations teams cannot independently process interest refunds or waivers
    - Every interest adjustment requires raising a Jira ticket and waiting for engineering/product team intervention
    - Backend access and API calls are needed for what should be a routine operational task
    - Process creates unnecessary dependencies across multiple teams for resolution
3. **Risk of Duplicate Processing:**
    - No systematic validation exists to check if interest for a specific period has already been waived or refunded
    - Product team rely on manual record-keeping and memory to avoid duplicate refunds
    - Risk of processing the same interest refund twice for the same loan-month-tranche combination
    - No single source of truth for tracking interest refund history
4. **Lack of Process Standardization:**
    1. **Manual Accounting Overhead:**
        - Product team must manually post journal vouchers (JVs) for every interest reversal
        - Each refund requires manual calculation of debit/credit entries across multiple GL accounts
        - Product bandwidth is consumed by repetitive mechanical tasks rather than strategic work
    - Interest refunds follow ad-hoc processes that vary by team member and situation
    - No defined maker-checker workflow creates approval ambiguity and accountability gaps
    - Inconsistent treatment compared to charge refunds which now have a standardized process
    - Difficulty in training new team members due to lack of documented, systematic workflow
5. **Limited Visibility and Audit Trail:**
    - No centralized tracking system for interest refund requests across their lifecycle
    - Cannot easily answer questions like "How many interest refunds were processed last month?" or "What was the total refunded amount?"
    - Difficult to reconcile interest reversals in financial statements due to scattered records
    - Compliance and audit requirements are harder to meet without systematic documentation

**Who are we solving it for?**

*Primary users:*

- End customers (experiencing delays in receiving legitimate interest refunds)
- Operations team (makers who initiate refunds and checkers who approve them)

*Secondary users:*

- Engineering team (currently burdened with operational refund requests)
- Product/Business team (lack visibility into refund patterns for risk and product insights)

### Out of scope

**Call out on items out of scope:**

- **Principal refunds/waivers:** Not covered in this scope. Principal adjustments follow a different accounting treatment and will be addressed separately if needed.
- **Bulk interest refund operations:** Initial release supports single loan account level requests. Bulk processing across multiple accounts is out of scope.
- **Automated goodwill/retention rules:** System will not automatically determine eligibility for interest waivers. All requests must be manually initiated by operations based on approved business criteria.

**Rationale for exclusion:**

- Principal refunds have fundamentally different accounting implications and require separate product design
- Bulk operations can be added in a subsequent phase once single-transaction flow is stabilized
- Automated eligibility rules require extensive business rule configuration and should follow after manual process is established

---

## 2. Success Criteria

**Top 2-3 clear outcomes that we are looking to achieve:**

1. **Average processing time:** Maker submission → Checker approval → Accounting closure completed within 1 business hour (improves customer experience)
2. **Operational Efficiency:** Reduce Jira ticket dependency for interest refunds by >90% and eliminate engineering intervention for standard interest refund cases
3. **Process TAT:** Complete interest refund processing from maker submission to accounting closure within one working day for approved requests
4. **Error Reduction:** Zero duplicate interest refunds for the same loan-month-tranche combination through system-driven validations

**Key success metrics:**

- **Reduction in manual intervention:** >90% reduction in Jira tickets related to interest refunds (baseline to be established pre-launch)

**Define post launch good state:**

- All interest refund requests flow through maker-checker workflow in Command Centre
- System automatically validates against duplicate refunds using schedule tables
- Credit note transactions posted successfully with correct GL mappings
- End-of-day automated JV posting clears intermittent liability and reverses income
- Complete audit trail available for all interest refund requests with enrichments
- Finance team can reconcile interest reversals through standard reports using JE IDs and enrichment tags

**Guardrail metrics:**

- Productization should not increase interest refunds - Legitimacy of refunds should be maintained via strict SOPs
- GL balancing maintained (every credit note must have matching JV reversal)

---

## 3. Solution Scope

### Solution overview

We are implementing an **Interest Refund Maker-Checker Workflow** using credit note transactions, mirroring the successful charge refund process. The solution enables operations to independently process interest refunds/waivers for both OD and Term Loan products through a validated, approval based task that automatically handles accounting through credit notes and JV reversals.

**Key product and system changes:**

- New maker task interface for interest refund request submission (loan account level with month-year-tranche specification)
- Validation API leveraging `f_account_schedule` and `f_account_schedule_derived` of finflux tables to prevent duplicate refunds
- Credit note repayment type extended to support interest reversals (non-cash transaction)
- Automated end-of-day JV posting workflow for interest income reversal with proper enrichments
- Checker task interface with computed refund details and approval controls

**Rationale on scoping/phasing:**

- **Phase 1 (Current):** OD and Term Loan interest refunds with manual maker initiation. This establishes the core workflow and validation framework.
- **Phase 2 (Future):** Bulk processing capabilities and integration with customer communication systems.

**Scope scoped out and rationale:**

- Automated interest recalculation and schedule adjustment is out of scope because the credit note approach treats interest refund as an accounting reversal, not a schedule modification. Schedule recalculation would require loan restructuring logic which is a separate product capability.

### Detailed solution scope

**User and system use cases that are supported:**

**Core happy path:**

1. **Maker initiates interest refund request:**
    - Maker selects loan account and initiates interest refund request
    - For **OD loans:** Maker specifies month-year (e.g., Jan 2025) and refund amount
    - For **Term loans:** Maker specifies tranche ID, month-year, and refund amount
    - System fetches schedule details from validation API
    - System validates interest charged for that period:
        - Interest has not already been waived for this loan-month-tranche combination - Fenix
        - No existing credit note for interest exists for the same period - Fenix
        - Interest can be either outstanding or collected (both supported) - Finflux schedule
        - Interest reversal amount cannot be more than what was posted for the loan/tranche for the month - Finflux schedule
    - Maker provides justification/remarks with approval documents and submits request
    - System creates interest refund request with unique ID (e.g., IR34234325342) and a checker task
2. **Checker reviews and approves request:**
    - Checker receives task with all request details:
        - Request ID, loan account, month-year, tranche (if applicable)
        - Refund amount with breakdown (interest amount)
        - Maker name, remarks, documents, and submission timestamp
    - Checker validates approval documentation
    - Checker verifies dedupe logic and amount correctness
    - Checker approves request
    - System posts credit note transaction on loan account / tranche
3. **Automated credit note posting:**
    - For OD
        - Credit note repayment posted against loan account with interest (reversal mapping and details)
        - Transaction enrichments populated:
            - **Enrichment 1:** Month and year in MMYYYY format
            - **Enrichment 2: “**Interest**”** (month-year-tranche combination)
        - Credit note debits intermittent liability control account
        - Credit note credits as per apportionment of the Credit note repayment transaction
    - For TL
        - Credit note repayment posted against tranche account with interest (reversal mapping and details) - (This will be a tranche level payment which will create tranche tagged excess on the line for the loan)
        - Transaction enrichments populated
            - **Enrichment 1:** Month and year in MMYYYY format
            - **Enrichment 2: “**Interest**”** (month-year-tranche combination)
        - Credit note debits intermittent liability control account
        - Credit note credits as per apportionment of the Credit note repayment transaction
4. **End-of-day automated JV posting:**
    - System constructs reversal JV:
        - **Credit:** Intermittent liability control account (clears proxy)
        - **Debit:** Income from interest (reverses interest income (Separate GL for interest refunds)
    - JV posted with accounting enrichments:
        - **Enrichment 1:** transaction ID of credit note transaction
        - **Enrichment 2:** "INTEREST_REVERSAL" constant identifier
    - Accounting loop closed

**Key edge cases handled at launch:**

1. **Duplicate refund prevention:**
    - System checks `f_account_schedule_derived` table for existing `interest_waived` or `tax_reversed` values for the specified month-year-tranche
    - If previous refund exists, validation fails with clear error message
    - Maker cannot proceed with duplicate request
2. **Checker rejection:**
    - If checker rejects request (invalid documentation, incorrect amount, etc.), request moves to rejected state
    - No credit note posted, no accounting impact
    - Maker can create fresh request if needed with corrected details (Dedupe should only be on approved refunds and not requests)
3. **Multi-tranche term loan:**
    - For term loans with multiple tranches, each tranche's interest can be refunded independently
    - Validation scoped at loan-tranche-month level to allow different months to be refunded for different tranches
    - Checker task clearly displays tranche details for verification

**Stakeholder impact considerations:**

**End customer:**

- **Experience change:** Customers will see credit note transaction in their account statement (similar to a repayment entry)
- No direct customer communication change in scope, but customer service team should be equipped to explain credit note entries if customers inquire
- Faster resolution time improves customer satisfaction for legitimate refund cases

**Operations team:**

- **Change in SOP:** Ops team will now use Command Centre maker-checker interface instead of raising Jira tickets. Training required on:
    - How to interpret validation error messages
    - Approval documentation requirements for checker review

**Finance team:**

- **Change in process:** Product team no longer needs to manually post JVs for interest reversals
- Reconciliation process changes to leverage enrichment tags and JE ID linkages

**Sales and onboarding:**

- No direct impact on sales conversations
- Onboarding teams should be aware that interest refunds are now systematically supported for operational error corrections and goodwill scenarios

---

## 5. High Level System, User or Process Flow

**End-to-End Interest Refund Flow:**

`[MAKER INITIATES REQUEST]
   ↓
Maker logs into Command Centre
   ↓
Goes to the loan details page for the specific loan (TL/OD)
   ↓
Selects "Interest Refund" option
   ↓
System identifies product type (OD vs Term Loan)
   ↓
IF Term Loan → Maker selects Tranche
   ↓
Maker enters Month-Year for interest refund (e.g., Jan 2025)
   ↓
Maker enters Refund Amount
   ↓
[VALIDATION API CALL]
   ↓
System calls validation API with:
   - Loan Account ID
   - Tranche ID (if term loan)
   - Month-Year
   - Refund Amount
   ↓
Validation API queries f_account_schedule and f_account_schedule_derived:
   - Fetches schedule record for specified month-year
   - Checks interest_charged for that period
   - Checks interest_waived and tax_reversed values
   - Verifies no existing credit note for same loan-month-tranche
   ↓
IF validation passes:
   System displays:
   - Interest charged for the month: ₹X
   - Interest already waived: ₹Y
   - Available for refund: ₹(X-Y)
   - GST component: ₹Z (if applicable)
   ↓
IF validation fails:
   Error displayed: "Interest already waived for this period"
   → Maker cannot proceed
   ↓
Maker adds justification remarks
   ↓
Maker submits request
   ↓
System generates Request ID (e.g., IR34234325342)
   ↓
Request routed to Checker queue

[CHECKER REVIEWS REQUEST]
   ↓
Checker receives notification of pending interest refund request
   ↓
Checker opens task and reviews:
   - Request ID: IR34234325342
   - Loan Account: 000012345
   - Product Type: Term Loan
   - Tranche: Tranche 2
   - Interest Refund Month: Jan 2025
   - Refund Amount: ₹5,000
   - Interest Amount (ex-GST): ₹4,500
   - GST Amount: ₹500
   - Maker Name: John Doe
   - Maker Remarks: "Customer complaint - incorrect interest calculation"
   - Requested On: 15-Jan-2025 10:30 AM
   ↓
Checker validates approval documentation
   ↓
Checker verifies amount matches schedule data
   ↓
IF Checker Approves:
   ↓
   [CREDIT NOTE POSTING]
      ↓
   System posts CREDIT_NOTE transaction:
      - Transaction Type: CREDIT_NOTE
      - Loan Account: 000012345
      - Amount: ₹5,000
      - Apportionment: Interest = ₹4,500, GST = ₹500
      - Transaction Date: Current date
      - Enrichment 1: Interest refund timestamp
      - Enrichment 2: Schedule ID reference (month-year-tranche)
      ↓
   Accounting entries for CREDIT_NOTE:
      Debit: Intermittent Liability Control Account = ₹5,000
      Credit: Interest Receivable (if outstanding) = ₹4,500
      Credit: Interest Income (if collected) = ₹4,500
      ↓
   Credit note transaction ID generated: TXN_CN_67890
      ↓
      ↓
   System retrieves transaction ID details for credit note transaction:
      ↓
   System constructs reversal JV:
      {
        "transactionDate": "15-Jan-2025",
        "credits": [
          { "glAccountId": 41, "amount": 5000 } // Intermittent liability
        ],
        "debits": [
          { "glAccountId": 43, "amount": 4500 }, // Income from interest
        ],
        "referenceNumber": "IR34234325342",
        "comments": "Interest reversal for month Jan-2025, Loan 000012345",
        "Enrichment1": "3424234234", // TxnID ID of credit note
        "Enrichment2": "INTEREST_REVERSAL"
      }
      ↓
   JV posted via:
      POST /fineract-provider/api/v1/journalentries
      ↓
   JV transaction ID generated: JV_89012
      ↓
   Request status updated to "Completed - JV Posted"
      ↓
   Notification sent to maker and finance team

IF Checker Rejects:
   ↓
   Request status updated to "Rejected"
   ↓
   Rejection remarks captured
   ↓
   No credit note posted, no accounting impact
   ↓
   Maker notified of rejection with reason via request status`

**Error case flow:**

`[VALIDATION ERROR HANDLING]

Scenario 1: Duplicate refund attempt
   ↓
Maker enters month-year for which interest was already waived
   ↓
Validation API detects interest_waived > 0 in f_account_schedule_derived
   ↓
Error returned: "Interest for Jan-2025 has already been waived. Amount waived: ₹5,000 on 10-Dec-2024"
   ↓
Maker cannot proceed with submission

Scenario 2: Amount exceeds charged interest
   ↓
Maker enters refund amount = ₹10,000
   ↓
Validation API finds interest_charged for that month = ₹5,000
   ↓
Error returned: "Refund amount (₹10,000) exceeds interest charged (₹5,000) for Jan-2025"
   ↓
Maker corrects amount and resubmits

Scenario 3: Credit note posting failure
   ↓
Checker approves request
   ↓
System attempts to post credit note`

---

## 6. Appendix

### Benchmarking

- NA

### User Feedback / Calling

- Na