# MFD Payout Calculation Automation

**Introduction**

Volt currently manages payout calculations for its Direct Mutual Fund Distributors (MFDs) through a highly manual process involving multiple Google Sheets, individual SQL queries, and significant analyst effort. This process is prone to errors, lacks scalability, presents a business continuity risk due to analyst dependency, and lacks clear auditability. This document outlines the requirements for building an automated, robust, and scalable Payout Calculation Engine to address these challenges specifically for Volt Direct MFDs. This engine will serve as the foundation for improving the overall payout experience, ensuring accuracy, timeliness, and transparency.

1. we need to handle changing factors like 
    - Monthly Transactions table
    - Marketing Offers /Referral bonuses
    - New Platforms additions
    - Changes in commercials with existing platforms /partners
    - Changes in base rates / Format
    - Negotiations with MFDs
2. We need to be able to audit how an amount was generated 
3. we need to be able to accrue the credits to an account based on the activity
4. We need to have the DB that is specific to transactions i.e we can't modify or delete the transactions that have happened, we can only rollback 

Problem statements

Before base payout calculations

- Delay in updating transaction table due to TATA API rate limits. We can’t differentiate the New transactions so we have download from beginning , this process currently take 3 days and growing.
- We have to reconcile missing Credit applications between transaction table and second data source, currently this process is manual and second data source is not reliable.
- Attribution of customer to correct Platfrom and partner require manual intervention.
- We don’t store the PF and ROI paid by the customer in Credits table.
- Commercials on transactions are added from the Partner commercials sheet manually, we don’t store share and Rates with the Credit application Data adding steps to calculate the payouts

After the Base payout calculation

- TDS rules change and have to accommodate
- GST payout are tracked manually

Payout process

- Tracking payout transactions Reconciliation takes 4 (2+2) days with HSBC
- For Platform Payouts we need to provide a statement and how the Payout amount is calculated.
- Partners have a hard time understanding statements.

Potential solutions

- Get TATA to improve the API data provided to get the updated transactions
- Better fall-back handling  on our side

Activity 

activity triggers a payout flow 

activity gets processed by payout flow through config and config credits the accounts payable of the Borrower/Partner/Platform 

The monthly payout is run to clear the account payable 

| Pre-calculation process | post calculation  |
| --- | --- |
| Updating Transaction tables | verification of the partner bank accounts |
| adding Offer calculations  | Reconciliation of the payout debit transactions  |
| adding Credit application commercials for the payout and share  |  |

Problem statements

- Delay in updating transaction table due to TATA API rate limits. We can’t differentiate the New transactions so we have download from beginning , this process currently take 3 days and growing.
- We have to reconcile missing Credit applications between transaction table and second data source, currently this process is manual and second data source is not reliable.

**2. Goals & Objectives**

The primary goal is to automate the calculation of payouts owed to Volt Direct MFDs accurately and efficiently.

- **Eliminate Manual Calculation:** Replace Google Sheets and manual SQL queries with an automated calculation engine.
- **Improve Accuracy:** Reduce errors stemming from manual data handling, formula mistakes, and reconciliation issues (~2% accounting errors mentioned).
- **Increase Efficiency:** Drastically reduce the time and analyst effort required to calculate monthly payouts (currently involves multiple days for tasks like transaction sync and reconciliation).
- **Ensure Auditability:** Provide a clear, traceable path from source transactions and commercial agreements to the final calculated payout amount for every MFD.
- **Reduce Business Continuity Risk:** Remove dependency on a single analyst for core calculation logic.
- **Scalability:** Build a system capable of handling increasing transaction volumes, MFD numbers, and evolving commercial complexity without proportional increases in processing time or manual effort.
- **Foundation for Improvement:** Provide accurate, structured calculation output data to feed into downstream processes like invoice generation, ledger updates, payment processing, and reporting dashboards.

### **3. Scope**

**In Scope:**

- **Data Ingestion & Preparation:** Automating the pull and preparation of necessary data points for calculation (Transactions, Principal Outstanding, Partner details, etc.).
- **Commercials Management:** Storing and applying MFD-specific commercial agreements (base rates, sharing percentages, upfront fees, trail logic, time-bound validity) stored in a database.
- **Calculation Logic Implementation:** Automating the calculation for Volt Direct MFDs based on:
    - Average Principal Outstanding (POS) for trail calculations.
    - Transaction-based triggers for upfront payouts.
    - Application of base rates and dynamic sharing percentages based on factors like customer ROI.
    - Inclusion of applicable Marketing Offers / Referral Bonuses (e.g., Partner-to-Partner Referral, Partner Self-line PF reversal).
    - Handling negotiated deviations from standard commercials at partner or customer level.
- **GST & TDS Calculation:** Calculating applicable GST (on payout amount) and TDS based on MFD details (GSTN validity, PAN) and prevailing tax rules.
- **Accrual Logic:** Ability to calculate and potentially track accrued earnings based on qualifying activities.
- **Audit Logging:** Detailed logging of data inputs, commercial rules applied, and calculation steps for each payout amount.
- **Output Generation:** Producing structured output data representing the calculated gross payout, GST, TDS, and net payable amounts, linked to specific MFDs, periods, and source transactions/activities. This output should feed the Payout Ledger.

**Out of Scope (for this phase 1 ):**

- **Invoice Generation & Approval Workflow**
- **Payout *Execution*:** (API integration with HSBC/Bank for initiating payments).
- **Payment Status Reconciliation & UTR Backfill:** (Handling bank feedback post-payment) Will Be maual for time being.
- **MFD-facing Dashboard:**
- **Platform Payout Calculations:** (Focus is solely on Volt Direct MFDs for now).
- **GST/TDS *Filing* Automation:** (Focus is on *calculation*, not filing).
- **Fixing Upstream Data Source Issues:** (e.g., Solving TATA API rate limits – this is a dependency, but the calculation engine must handle potentially delayed/incomplete data gracefully).
- **Customer Attribution Logic:** (Assume attribution is done upstream, calculation engine uses the provided mapping).
- **Bank Account Verification (Penny Drop):** (Separate operational process).

## **4. Current Process Analysis & Pain Points (Calculation Focus)**

The current calculation process for Volt Direct MFDs suffers from:

1. **Data Fragmentation:** Critical data like Principal Outstanding, Partner Commercials, Ledgers, and Calculations reside in disparate Google Sheets, making data consistency and integrity difficult.
2. **Manual Data Aggregation & Prep:**
    - Significant delay (3+ days) and manual effort in syncing/reconciling transaction data (TATA API limitations, secondary source unreliability).
    - Manual application of commercials from Sheets to transaction data.
    - Manual identification and calculation of Marketing Offers (Self-line, P2P referral) and Negotiations.
3. **Complex & Opaque Logic:** Calculations are performed via complex Sheets formulas and individual SQL queries, understood fully by only one analyst. Difficult to audit or modify reliably.
4. **Lack of Auditability:** No systematic way to trace a final payout figure back through the specific data, commercials, offers, and calculation steps used. Audits are manual and time-consuming.
5. **Error Prone:** Manual steps, complex formulas, and data inconsistencies lead to calculation errors discovered late (e.g., during tax filing).
6. **Scalability Issues:** The process time grows significantly with data volume and partner complexity. Handling changing commercials, rates, or offers requires extensive manual updates.
7. **Manual GST/TDS Calculation:** GST applicability and TDS deductions are tracked and calculated manually based on rules that can change.

### **5. Proposed Solution: Automated Payout Calculation Engine**

1. **Data Ingestion Module:** Fetches required data from source databases (Application Data DB, Transaction Data DB, Partner Info DB, new Commercials DB, new POS DB). Includes logic for handling data availability issues (e.g., process based on available data up to a point, flag inconsistencies).
2. **Commercials & Rules Repository (Database):** Stores all relevant commercial terms (versioned, time-bound) for Direct MFDs, including default rates, specific overrides, offer details, negotiation terms, and GST/TDS rules.
3. **Calculation Core:** Executes the payout calculation logic based on the ingested data and configured rules. Handles different payout types (upfront, trail), applies sharing logic, incorporates offers/negotiations, and calculates taxes.
4. **Audit Logging Service:** Records detailed logs for each calculation run – inputs used, rules applied, intermediate results, final outputs, timestamps, user triggering the run (if applicable).
5. **Output Module:** Generates structured data files or database entries containing the detailed calculation results (per MFD, per payout reason, per period) ready for ingestion by the Payout Ledger, Invoice Generation system, and reporting tools.
6. Slab based payment : - above a AUM for a partner or platfrom the base payout changes 
7. Upfront to adding customers fee, we will not pay for new line creation 
8. 

**Workflow:**

1. Trigger (Scheduled or Manual): Initiate calculation run for a specific period (e.g., previous month).
2. Data Ingestion: Pull necessary data (Transactions, POS, MFD details, Commercials) for the period.
3. Pre-Calculation Validation: Perform basic checks on data completeness and consistency.
4. Calculation Execution:
    - Calculate average POS where needed for trail payouts.
    - Identify trigger events for upfront payouts.
    - Apply relevant commercials (base, dynamic, negotiated, offers) based on MFD, customer, transaction date, etc.
    - Calculate gross payout amounts per reason code.
    - Aggregate payouts per MFD.
    - Calculate applicable GST based on MFD's GSTN status and payout type.
    - Calculate applicable TDS based on MFD's PAN and threshold rules.
5. Audit Logging: Log all steps and results.
6. Output Generation: Create structured output data (e.g., CSV, database table update) detailing MFD_ID, Period, Payout_Reason, Source_Reference (e.g., Credit_ID), Calculation_Base, Rate_Applied, Gross_Amount, GST_Applicable, GST_Amount, TDS_Rate, TDS_Amount, Net_Payable, Calculation_Timestamp, Run_ID.
7. Post-Calculation Validation (Optional Manual Step): Allow review/sign-off of calculated amounts before feeding downstream.

**6. Functional Requirements**

| ID | Requirement Description | Details/Acceptance Criteria | Priority |
| --- | --- | --- | --- |
| **Data** |  |  |  |
| F-01 | Ingest Transaction Data | System must ingest relevant transaction data (credits, disbursements, repayments) from the source DB for the specified calculation period. Handle date filters correctly (e.g., IST). | Must |
| F-02 | Ingest/Calculate Principal Outstanding (POS) | System must access or calculate daily/average POS data for relevant credits from the designated POS source (new DB table). | Must |
| F-03 | Ingest Partner/MFD Data | System must ingest MFD details including partner_account_id, name, PAN, GSTN, bank account status (for flagging, not verification). | Must |
| F-04 | Ingest Commercials Data | System must read versioned, time-bound commercial rules (upfront fee, trail %, base rate, sharing %, offer flags) for each MFD from the Commercials DB. | Must |
| F-05 | Ingest Negotiation/Offer Data | System must ingest specific negotiation overrides (rates, shares) and flags for applicable marketing offers (Self-line, P2P referral) linked to partners/credits. | Must |
| **Commercials** |  |  |  |
| F-06 | Apply Default Commercials | System must apply default commercial rules for Volt Direct MFDs if no specific override exists for the MFD/credit/time period. | Must |
| F-07 | Apply MFD-Specific Commercials | System must prioritize and apply specific commercial terms defined for an individual MFD over default rules. | Must |
| F-08 | Apply Time-Bound Commercials | System must apply the correct commercial version based on the transaction/activity date relative to the commercial validity period (from_date, to_date). | Must |
| F-09 | Apply Negotiated Rates/Shares | System must apply negotiated rates or sharing percentages sourced from the negotiation data, overriding standard/MFD-specific commercials where applicable. | Must |
| **Calculations** |  |  |  |
| F-10 | Calculate Trail Payouts | Calculate trail amounts based on (Avg_POS * Payout_Rate * Days_Active_in_Period) / Days_in_Year. Correctly handle partial months. | Must |
| F-11 | Calculate Upfront Payouts | Calculate fixed upfront amounts triggered by specific events (e.g., loan activation) based on applicable commercials. | Must |
| F-12 | Calculate Dynamic Sharing | Calculate additional payout based on (Customer_ROI - Base_Rate) * Sharing_Percentage * Calculation_Base, where applicable. | Must |
| F-13 | Calculate Marketing Offers | Calculate amounts for specific offers like P2P referral (fixed amount) or Self-line (PF reversal/negation of standard upfront). | Must |
| F-14 | Aggregate Payouts | System must aggregate all calculated payout amounts for a single MFD within the period, potentially grouped by reason code. | Must |
| F-15 | Calculate GST | Apply correct GST rate based on MFD's GSTN status (registered/unregistered) and payout reason eligibility. Output GST_Amount. | Must |
| F-16 | Calculate TDS | Apply correct TDS rate based on MFD's PAN status, payout thresholds, and current tax regulations. Output TDS_Amount. | Must |
| F-17 | Generate Unique Calculation Identifiers | Assign unique identifiers (payout_transaction_id concept) to calculated line items for traceability and linking to ledger/payments. Hashkey logic needs refinement for DB context. | Must |
| **Audit** |  |  |  |
| F-18 | Log Calculation Inputs | Log the specific data records (transactions, POS, MFD details) used for each calculation. | Must |
| F-19 | Log Rules Applied | Log the specific commercial rule versions (default, MFD-specific, negotiated, offer) applied during calculation. | Must |
| F-20 | Log Calculation Results | Log intermediate and final calculation results (gross, GST, TDS, net) with timestamps and run IDs. | Must |
| F-21 | Enable Traceability | Audit logs must allow tracing a final net payout amount back to its constituent gross amounts, the rules applied, and the source data. | Must |
| **Output** |  |  |  |
| F-22 | Generate Structured Output | Produce output in a predefined format (e.g., DB table, CSV) containing all necessary fields for the Payout Ledger and downstream processes (see Workflow step 6 for fields). | Must |
| **Config** |  |  |  |
| F-23 | Configurable Base Rates | Allow admin users to configure and update Volt's internal base rates (PF, ROI) used in calculations, with effective dates. | Should |
| F-24 | Configurable Tax Rules | Allow admin users to configure and update GST and TDS rates/rules applied in calculations, with effective dates. | Should |

**7. Data Requirements**

- **Source Data:** Access required to Production Databases for:
    - credits, transactions, borrower_accounts, credit_applications_entity (or equivalents for Application/Transaction data).
    - partner_accounts (for MFD details, PAN, GSTN).
    - customer_leads (if needed for attribution confirmation, though attribution ideally happens upstream).
- **New Database Tables:**
    - **PrincipalOutstandingDaily (or similar):** To store reliable daily POS per credit, replacing Google Sheets. Needs population mechanism.
    - **PartnerCommercials:** To store versioned, time-bound commercial rules (default, MFD-specific) replacing Google Sheets. Needs structure for various rate types, sharing rules, validity.
    - **PayoutNegotiationsOffers:** To store specific negotiated terms and offer applicability, replacing Google Sheets.
    - **PayoutCalculationResults:** To store the detailed output of the calculation engine.
    - **CalculationAuditLog:** To store detailed audit trails.
- **Data Integrity:** Mechanisms needed to ensure data consistency between sources (e.g., reconciliation flags if upstream data like TATA sync is delayed).
- **Immutability:** Calculated results and audit logs should be immutable for historical accuracy. Corrections should be handled via adjustment entries, not overwriting history.

**8. Non-Functional Requirements**

- **Accuracy:** Calculations must be mathematically correct and precisely reflect the defined commercial logic and tax rules. Verifiable against manual checks on sample data.
- **Auditability:** All calculations must be fully traceable via logs.
- **Performance:** Calculation for a full month's data for all Direct MFDs should complete within an acceptable timeframe (e.g., < 4 hours, TBC).
- **Scalability:** The system architecture should handle a 10x increase in MFDs and transaction volume over the next 2 years without significant performance degradation or redesign.
- **Reliability:** The engine must produce consistent results for the same inputs and rules. Failures should be logged clearly.
- **Maintainability:** Code should be well-structured, documented, and tested. Configuration of rules (commercials, taxes) should be manageable without code changes where possible.
- **Security:** Access to the engine, configuration, and logs must be controlled via appropriate permissions. Sensitive data (PAN, Bank details) handled securely.

**9. User Roles & Permissions**

- **Payout Analyst:** Triggers calculation runs, reviews results, investigates discrepancies using audit logs.
- **System Administrator:** Manages system configuration (base rates, tax rules), potentially manages commercial rule updates via controlled interface/process. Monitors system health and logs.
- **Finance Team:** Access to view final calculation outputs for ledger posting and verification.
- **Business/Sales Ops:** Access to view commercial rule configurations, potentially manage negotiation/offer data inputs via a defined process/interface. Read-only access to calculation results/reports.

**10. Success Metrics**

- **Calculation Accuracy:** Target >99.9% accuracy compared to manually verified sample calculations. Measured by incidents of incorrect calculation reported post-automation.
- **Processing Time:** Reduction in end-to-end calculation time from >3 days (including sync) to < 1 day (post-data availability).
- **Manual Effort Reduction:** Decrease in analyst hours spent on manual calculation, reconciliation, and validation by >80%.
- **Audit Trail Utility:** Successful tracing of >95% of payout queries back to source data and rules within minutes using the audit log.
- **Reduction in Calculation-Related Support Queries:** Decrease in internal (Finance, RM) and external (MFD) queries related specifically to *how* an amount was calculated.

**11. Open Questions & Future Considerations**

- What is the agreed source of truth and update frequency for the new PrincipalOutstandingDaily table? How are TATA API delays handled?
- What is the precise workflow and authorization process for updating PartnerCommercials and PayoutNegotiationsOffers data? (Admin UI vs. controlled DB scripts?)
- Define the exact schema for the new database tables.
- How should historical corrections/adjustments be processed by the engine? (Rerun for past period? Adjustment entries in current period?)
- Clarify exact hashkey logic requirements for payout_transaction_id in the new DB context.
- Explore potential for near real-time accrual calculations (Phase 3 goal).
- Integration points and data contracts with Invoice Generation and Payout Ledger systems.

**12. Appendix**

---