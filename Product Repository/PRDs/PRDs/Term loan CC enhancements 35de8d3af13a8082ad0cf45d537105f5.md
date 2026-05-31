# Term loan CC enhancements

: Ameya Aglawe
Created time: May 11, 2026 10:00 AM
Status: Not started
Last edited: May 11, 2026 11:26 AM

# **Background and Context**

- Operations teams currently face multiple visibility and workflow challenges while managing term loans in Command Centre.
    - Closed tranches automatically disappear from Command Centre once they are closed, resulting in complete loss of visibility for the Ops team for historical tracking and issue resolution.
    - Excess refund handling for term loans differs from OD loans. Tranche-tagged excess margins are non-refundable, however Command Centre currently does not provide a granular split between refundable and non-refundable excess. This creates inconsistencies between excess refund tasks and the loan details page, making it difficult for Ops teams to follow existing SOPs.
    - During collateral release approval flows, Ops teams need to validate whether requested DP for un-pledge is within permissible limits `(Unpledge requested DP <= Total DP - TOS)`. Currently, checker tasks do not display TOS or due details, forcing Ops users to manually navigate to loan details pages to retrieve data, leading to delays and increased chances of operational errors.
- These gaps impact operational efficiency, increase dependency on manual checks, and create risks of incorrect approvals/refunds.

---

# **1. Problem scope**

### In scope

- Providing visibility for automatically closed tranches within Command Centre
- Displaying granular excess margin breakdown:
    - Total excess margin
    - Refundable excess margin
    - Non-refundable excess margin (tranche-tagged)
- Displaying the above excess details within:
    - Loan details page
    - Checker task screens
- Displaying due details/TOS visibility within collateral release checker tasks
- Supporting operational workflows for:
    - Excess refund handling
    - Collateral release approval validation
    - Historical tranche visibility

### Out of scope

- Any modification in tranche closure logic
- Changes in excess refund business rules or refund eligibility logic
- Any customer-facing UI changes
- Automation of collateral release approval decisions
- SOP/process changes outside visibility enhancements

---

# **2. Success Criteria**

- Reduction in Ops dependency on manual loan detail verification during checker approvals
- Elimination of visibility gaps for closed tranches within Command Centre
- Alignment of excess margin values across:
    - Excess refund tasks
    - Loan details page
    - Checker tasks
- Reduction in operational TAT for:
    - Excess refund processing
    - Collateral release approvals
- Reduction in manual operational errors caused due to context switching between pages

### Guardrail metrics

- No degradation in Command Centre task loading latency
- No incorrect excess classifications post launch
- No impact on existing tranche closure or refund workflows

---

# **3. Solution Scope**

### Solution overview

The solution focuses on improving operational visibility and reducing manual dependency within Command Centre for term loan workflows. The scope includes enabling visibility for closed tranches, exposing granular excess margin bifurcation, and surfacing due details/TOS directly within checker tasks.

The implementation will involve a mix of backend and frontend enhancements:

- Closed tranche visibility requires backend API enhancements only
- Excess margin bifurcation requires both backend and frontend changes
- Due details visibility in checker tasks requires frontend integration with existing due details APIs

### Detailed solution scope:

- Closed tranches will continue to remain visible in Command Centre even after automatic closure
- Existing APIs will be enhanced to fetch and return closed tranche details
- No frontend UI changes required for tranche visibility enhancement
- Command Centre will display:
    - Total excess margin
    - Refundable excess margin
    - Non-refundable excess margin (tranche-tagged)
- The same bifurcation will be visible within loan details sections inside checker tasks
- Excess refund task values and loan details values will remain aligned as per Ops SOP expectations
- Checker tasks for collateral release approvals will additionally display:
    - Maximum Un-pledge Eligible Amount
        - Maximum Unpledge Eligible Amount = Drawing Power - POS of All Tranches- Interest Dues of Tranches - One Upcoming Interest Due for across all Tranches(Not Due) + Total Excess
    - Due details
    - TOS visibility
- Frontend will consume due details APIs within checker task flows to avoid manual navigation by Ops users
- Existing operational SOPs remain unchanged; this enhancement primarily reduces manual effort and improves visibility
- No impact expected on customer journeys or onboarding/sales conversations as all changes are internal tooling enhancements

| Description | Details |
| --- | --- |
| Closed tranche visibility | Backend APIs enhanced to fetch and expose closed tranche data in Command Centre |
| Excess margin bifurcation | Visibility of refundable vs non-refundable excess margins in Command Centre and checker task loan details |
| Checker task enhancements | Due details and TOS visibility added directly within collateral release checker tasks |
| Frontend changes | Required for excess visibility and due details integration |
| Backend changes | Required for tranche APIs and excess margin bifurcation support |

---

# **5. High level system, user or process flow**

**Closed tranche**

1. Tranche gets automatically closed
2. Command Centre continues fetching tranche details using APIs
3. Ops users retain visibility of historical closed tranche data

---

**Refundable excess**

1. Excess refund task gets generated
2. Command Centre fetches:
    - Total excess margin
    - Refundable excess margin
    - Non-refundable excess margin
3. Same values are displayed consistently across:
    - Refund tasks
    - Loan details page
    - Checker task loan details

---

**Collateral removal** 

1. Ops user opens collateral release checker task
2. FE calls due details API
3. Checker task displays:
    - TOS
    - Due details
4. Ops validates:
    
    Requested DP ≤ Total DP - TOS
    
5. Ops completes approval/rejection without navigating to loan details page