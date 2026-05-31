# credit_bureau_reporting_comms_product_note

# Credit Bureau Reporting Communication — Interest Payment Default Notification

: Yogesh D
Created time: March 16, 2026 2:53 PM
Status: Not started
Last edited: March 16, 2026 3:38 PM

---

## **Background and Context**

- VoltMoney is a Loan Against Mutual Funds (LAMF) LSP operating on DSP Finance’s NBFC lending infrastructure. As part of its regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window.
    - **Who is facing the problem:**
        - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness
        - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting
        - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is manual or absent for this event
        - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism
    - **What is broken today:**
        - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau
        - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap
        - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting
        - Manual triggering of communications is error-prone and does not scale with increased reporting frequency
    - **Why it is important / What is getting impacted:**
        - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance
        - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations
        - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution
        - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP depends on proactive borrower communication at critical account events

---

## **1. Problem scope**

### In scope

- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a bureau reporting notification to each eligible borrower via SMS and Email at the time of reporting
        - Support for both the current cadence (15th and EOM) and the July 2026 cadence (9th, 16th, 23rd, EOM) — configurable without code change
        - Logging of all communication dispatch events for compliance audit and reconciliation
        - Idempotency to prevent duplicate communications per borrower per reporting event
    - **Who are we solving it for:**
        - **Primary:** Borrowers with outstanding interest dues (totalInterestDue > 0) on active LAMF accounts — they receive the notification and gain awareness of the adverse credit event
        - **Secondary:** Compliance team — receives automated confirmation that communication obligations are met; Data Analytics team — no change to their workflow, but gains a downstream comms handoff; Customer Support team — equipped to handle inbound borrower queries about the notification

### Out of scope

- The following items are explicitly excluded from this scope:
    - **Pre-reporting “pay now to avoid bureau reporting” reminders** — already handled by the existing overdue notification flow (`overdue_notification_updated` SMS template, DLT ID: 1107175525443527157). Rationale: Duplicate communication effort; existing flow covers pre-event borrower nudges
    - **Changes to the bureau reporting process or data submission logic** — owned entirely by Analytics / Compliance. Rationale: This note covers only the borrower-facing communication layer, not the reporting engine
    - **Bureau reporting for principal overdue** — only interest overdue is in scope. Rationale: Principal overdue bureau reporting follows a separate regulatory track with its own timelines and thresholds
    - **Post-reporting dispute or resolution workflow** — addressed by the grievance redressal mechanism. Rationale: Out of scope for a notification-only feature; disputes are a separate product and ops problem
    - **Multi-language / vernacular communications** — English only for Phase 1. Rationale: Not a blocker for compliance; vernacular support can be addressed in a future iteration consistent with other charter communications
    - **NPA classification warning communication** — separate communication type per the charter (stack rank 7). Rationale: NPA classification triggers a different regulatory obligation and a different borrower action; addressed in a separate feature

---

## **2. Success Criteria**

- **Outcome 1 — 100% bureau reporting events result in a communication batch (zero silent failures)**
    - Every instance of bureau reporting must trigger a corresponding comms job run. No reporting event should complete without a notification batch being attempted and logged
    - *Measurement:* Reconciliation between reporting completion log and comms dispatch log — any gap raises an alert to compliance
- **Outcome 2 — ≥ 95% of identified defaulters receive at least one channel notification within 1 hour of reporting job completion**
    - The communication job must complete within 60 minutes of the reporting event and achieve delivery to ≥ 95% of the target population on at least one channel (SMS or Email)
    - *Measurement:* Comms delivery log vs. reporting list per batch
- **Outcome 3 — Zero communication errors on non-defaulters (no false positives)**
    - No borrower with `totalInterestDue = 0` at the time of job execution receives a bureau reporting notification
    - *Measurement:* Pre-dispatch validation audit; zero tolerance guardrail
- **Key success metrics:**

| Metric | Target | Method |
| --- | --- | --- |
| Communication delivery rate | ≥ 95% per batch | Comms log vs. reporting list |
| Zero missed reporting events | 100% coverage | Reporting log vs. comms dispatch log |
| Job completion SLA | Within 60 minutes of reporting event | Job timestamp audit |
| Delivery failure / error rate | < 2% per batch | Comms failure logs |
| Duplicate communication rate | 0% (idempotency enforced) | Idempotency check on LAN + reporting date |
| False positive rate (non-defaulter comms) | 0% | Pre-dispatch validation audit |
- **Post-launch good state:** All bureau reporting events result in a logged comms batch. Compliance team receives a daily reconciliation report (comms sent vs. reporting list) confirming 100% coverage. Customer Support team observes no spike in borrower complaints attributable to surprise bureau reports
- **Guardrail metrics (must not degrade):** Existing overdue reminder delivery rates; existing LMS API response time SLAs; existing comms channel uptime (SMS gateway, SendGrid)

---

## **3. Solution Scope**

### Solution overview

- A scheduled, event-triggered communication job will be built on top of the existing LMS mandate summary API and DSP Finance’s communications infrastructure. On completion of each bureau reporting event, the job will call the mandate summary API, filter for accounts with `totalInterestDue > 0`, and dispatch a bureau reporting notification to each eligible borrower via SMS and Email — with full logging for compliance audit.
    - **Key product and system changes:**
        - New communication template (SMS via DLT registration + Email via SendGrid) for the bureau reporting notification event type
        - New comms job / scheduled trigger tied to the bureau reporting completion event
        - Idempotency layer (keyed on `fenixLoanAccountId` + reporting date) to prevent duplicate sends
        - Compliance reconciliation log generated per reporting batch
    - **Rationale on phasing:**
        - Phase 1 (this note): Notification at the point of bureau reporting — uses existing LMS API, existing comms channels, new template. Lowest implementation complexity, highest compliance impact
        - Phase 2 (future): Pre-reporting “pay now to avoid bureau reporting” warning communication, driven by the NPA classification warning flow
    - **Scope called out:** WhatsApp is excluded from Phase 1 for this communication type (not listed as a required channel in the charter for regulatory communications of this nature). DLT template registration is a prerequisite before go-live.

### Detailed solution scope:

- **Core happy path:**
    - Analytics team generates the defaulted borrower list on the reporting date (15th / EOM currently; 9th / 16th / 23rd / EOM from July 2026) at 11:59 PM
    - Bureau reporting is executed by Analytics / Compliance within the 7-day window from data generation
    - On reporting completion, the comms job is triggered (via webhook or scheduled poll against a reporting completion flag)
    - Job calls `GET http://api.core-lms.internal.dspfin.com:8080/lms/loan/account/v1/mandate/summary/all`
    - API response is filtered: accounts where `totalInterestDue > 0` are the target population
    - For each eligible account, `fenixLoanAccountId` and `fenixClientId` are used to resolve borrower contact details
    - Idempotency check: skip if this LAN has already been notified for this reporting event date
    - Dispatch bureau reporting notification via SMS (registered DLT template) and Email (SendGrid template)
    - Log delivery status (sent / failed / opted-out) per account in the comms audit log
    - Compliance team reconciles comms log vs. reporting list to confirm coverage
- **Key edge cases that must be handled at launch:**
    - **Multiple tranches with interest due:** Communication sent once per LAN (account level), not per tranche. `totalInterestDue` at account level is the filter field, not tranche-level `interestDue`
    - **Reporting delayed within the 7-day window:** Communication trigger must be tied to the actual reporting completion event, not the data generation date. A borrower should not receive the notification before reporting has been filed
    - **Partial payment between list generation and reporting:** API is called at job runtime — real-time `totalInterestDue` at the time of the comms job determines eligibility. If the borrower has cleared dues, `totalInterestDue` will be 0 and they will be excluded
    - **Borrower opted out of SMS / Email:** Existing opt-out logic applies. Communication attempted on available channels only; failure logged
    - **API unavailability or timeout:** Retry up to 3 times at 10-minute intervals. If all retries fail, a manual alert is raised to the compliance team for manual intervention
    - **Duplicate trigger (job fires twice for same reporting event):** Idempotency key on `[fenixLoanAccountId + reporting date]` ensures no duplicate communication is sent
    - **Zero defaulters on a reporting date:** Job completes with an empty batch; a compliance log entry is still created for audit purposes confirming the job ran
    - **July 2026 cadence change:** Reporting date configuration must be parameterised (9, 16, 23, EOM) so the cadence change requires only a config update, not a code deployment
    - **SOP impact for Compliance team:** Instead of manually tracking communication obligations, compliance team will receive an automated reconciliation report per reporting event. No change to the reporting process itself
    - **End user experience change:** Borrowers will now receive a transparent, timely notification at the moment their interest default is reported to the bureau — including their LAN, the overdue interest amount, and the reporting date. They will be directed to support for queries
    - **Sales / onboarding impact:** No direct impact. Customer Support team should be briefed so they can handle inbound borrower queries about the notification

| Description | Details |
| --- | --- |
| API endpoint | `GET http://api.core-lms.internal.dspfin.com:8080/lms/loan/account/v1/mandate/summary/all` |
| Filter condition | `totalInterestDue > 0` at account level |
| Key response fields used | `fenixLoanAccountId`, `fenixClientId`, `totalInterestDue`, `trancheLevelDetails[].interestDue` |
| Communication channels | SMS (primary), Email (secondary) |
| Sender | NBFC — DSP Finance (consistent with regulatory comms per charter) |
| Logging | Required (compliance audit log per batch) |
| Batch approval required | No (event-driven, compliance-mandated communication) |
| Idempotency key | `fenixLoanAccountId` + reporting event date |
| Retry logic | 3 retries at 10-minute intervals on API failure |
| Proposed SMS template | `Dear [Name], an interest due of Rs [Amount] on your LAS account [LAN] with DSP Finance has been reported to the credit bureau as on [Reporting Date] per regulatory requirements. Please clear dues immediately to avoid further credit impact. Support: support@dspfin.com / +91 96117 49097 – DSP FINANCE` |
| Email template variables | `date`, `clientId`, `lan`, `customerName`, `interestDue`, `reportingDate`, `supportEmail`, `supportNumber` |

---

## **5. High level system, user or process flow**

- **End-to-end process flow — Bureau Reporting Communication:**
    - **Step 1 — Data Generation (Analytics, Reporting Date at 11:59 PM)**
        - Analytics team generates the list of interest-defaulted borrowers on the reporting date
        - Current cadence: 15th and EOM | From July 1, 2026: 9th, 16th, 23rd, EOM
    - **Step 2 — Bureau Reporting (Compliance, within 7-day window)**
        - Compliance team executes credit bureau reporting using the generated list
        - On completion, a reporting completion event is emitted (webhook / flag update)
    - **Step 3 — Comms Job Trigger (System)**
        - Comms job is triggered by the reporting completion event
        - Calls `mandate/summary/all` API to fetch real-time account state
    - **Step 4 — Eligibility Filter (System)**
        - Filter API response for accounts where `totalInterestDue > 0`
        - Apply idempotency check: exclude any LAN already notified for this reporting date
    - **Step 5 — Communication Dispatch (System)**
        - For each eligible account: resolve contact details → dispatch SMS + Email via registered templates
        - Log delivery status (sent / failed / opted-out) per account
    - **Step 6 — Compliance Reconciliation (Compliance team)**
        - Compliance receives automated reconciliation report: comms sent vs. reporting list
        - Any gap triggers a manual review and alert
    - **Step 7 — Borrower Query Handling (Customer Support)**
        - Borrowers who receive the notification and have queries reach Customer Support
        - CS team handles as per updated SOPs
- **Error / edge case flows:**
    - **API timeout:** Retry up to 3 times at 10-minute intervals → if all retries fail, raise manual alert to compliance team; compliance team manually confirms communication obligation and triggers fallback
    - **Duplicate job trigger:** Idempotency check on `[LAN + reporting date]` prevents double-send; second trigger results in a no-op with a log entry
    - **Zero defaulters on reporting date:** Job completes with empty batch; compliance log entry created confirming job ran successfully with 0 eligible accounts
    - **Opted-out borrower:** Communication skipped for opted-out channel; attempted on remaining available channels; logged as opted-out (not a failure)
    - **Partial payment post list generation:** Job uses real-time API data at runtime — if `totalInterestDue = 0` at job time, borrower is excluded from the batch

---

## **6. Appendix (Optional)**

### Benchmarking:

- **Reporting cadence comparison:**

| Parameter | Current (Until June 30, 2026) | From July 1, 2026 |
| --- | --- | --- |
| Reporting dates | 15th and EOM | 9th, 16th, 23rd, and EOM |
| Frequency | 2x per month | 4x per month |
| Data generation time | 11:59 PM on reporting date | 11:59 PM on reporting date |
| Reporting window | Within 7 days of data generation | Within 7 days of data generation |
| Comms trigger | On bureau reporting completion | On bureau reporting completion |
- **Related communications charter entries (for reference):**

| Communication Type | Charter Status | Relevance to this note |
| --- | --- | --- |
| Payment Reminders / Overdue Notification | Deployed | Covers pre-reporting reminders; out of scope here |
| NPA Classification Warning | Not picked (stack rank 7) | Separate communication type; out of scope |
| No-dues Certificate + Closure | Deployed | Post-closure event; separate flow |
| Interest Rate Changes | Not picked | Separate regulatory obligation |

### User feedback / Calling:

- To be populated post-launch based on borrower response to the notification, Customer Support query volume, and compliance team feedback on reconciliation report usability
- Recommended: Sample 20–30 borrowers who received the notification in the first two reporting cycles to assess comprehension of the communication and any actionability gaps