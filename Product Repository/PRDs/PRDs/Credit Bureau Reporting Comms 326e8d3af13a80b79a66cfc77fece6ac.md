# Credit Bureau Reporting Comms

: Yogesh D
Created time: March 17, 2026 5:13 PM
Status: Pending Review
Last edited: March 19, 2026 11:57 AM

# Credit Bureau Reporting Comms

---

# What problem are we solving?

- DSP Finance is required by RBI regulations to report borrowers with outstanding interest dues to credit bureaus.
- Currently, **no communication is sent to borrowers at the time of reporting** — creating a regulatory compliance gap and leaving borrowers unaware of adverse credit events being filed against them.

- As reporting frequency increases from **2x/month (15th, EOM) to 4x/month (9th, 16th, 23rd, EOM) from July 1, 2026**, the gap scales without an automated solution in place.

---

# How do we measure success?

- 100% of bureau reporting events result in a dispatched comms batch — zero silent failures
- ≥ 95% delivery rate per batch (SMS) with < 2% error rate
- Zero communications sent to non-defaulters (`totalInterestDue = 0`)

| Metric | Target |
| --- | --- |
| Delivery rate | ≥ 95% per batch |
| Missed reporting events | 0 |
| Error / failure rate | < 2% |
| False positives (non-defaulters notified) | 0% |

---

# What is the solution?

## Overview

- A **scheduled comms job** runs at **12:00 AM on T+1** of the reporting date. It calls the LMS mandate summary API, filters accounts with `totalInterestDue > 0`, and dispatches a bureau reporting notification via SMS . Email communication is not necessary.
- New DLT-registered SMS template to be created. Idempotency keyed on `fenixLoanAccountId + reporting date` prevents duplicate sends.

---

## Scope

**In scope**
- Comms job triggered at 12 AM on T+1 of reporting date
- API-based defaulter identification (`totalInterestDue > 0`)
- SMS (primary) dispatch with compliance audit log
- Configurable reporting dates as mentioned  — supports cadence change via config, no code deploy needed

- **Out of scope**
    
    
     - **No auto-retry in place** — if the API call fails, a manual alert is raised to the compliance          team who will trigger the comms manually.
    
    - Pre-reporting “pay now” reminders — covered by existing overdue notification flow
    
    - Changes to bureau reporting/data submission logic — Analytics/Compliance owned
    
    - Post-reporting dispute workflows — separate grievance redressal product
    
     
    
     
    

---

## Happy Path

1. Analytics generates defaulter list at 11:59 PM on reporting date (15th / EOM or 9th / 16th / 23rd / EOM from July 2026)
2. Compliance executes bureau reporting within 7-day window
3. Comms job triggers at **12:00 AM on T+1**
4. Job calls mandate summary API → filters `totalInterestDue > 0`
5. Idempotency check: skip if LAN already notified for this reporting date
6. Dispatch SMS → log delivery status per account
7. Compliance reconciles comms log vs. reporting list

---

## Edge Cases

| Scenario | Handling |
| --- | --- |
| Borrower partially paid between list generation and job run | Real-time API called at job time — excluded if `totalInterestDue = 0` at runtime |
| Borrower opted out of SMS | Skipped on opted-out channel; attempted on remaining channel; logged as opted-out |
| API failure | Manual alert raised to compliance team — **no auto-retry** |
| Duplicate job trigger | Idempotency check on `[LAN + reporting date]` — second run is a no-op |
| Zero defaulters on reporting date | Job completes with empty batch; compliance log entry still created |
| July 2026 cadence change | Reporting dates parameterised in config — no code change required |

---

## Communication Template

**SMS (DLT registration required before go-live)**

Dear [Name], an interest due of Rs [Amount] on your LAS account [LAN]
with DSP Finance has been reported to the credit bureau as on [Reporting Date]. Please clear dues immediately to avoid further credit impact. Support: support@dspfin.com / +91 96117 49097 – DSP FINANCE

---

## Technical Details

| Parameter | Details |
| --- | --- |
| Comms trigger time | 12:00 AM on T+1 of reporting date |
| Sender | NBFC — DSP Finance |
| Channels | SMS |
| Idempotency key | `fenixLoanAccountId` + reporting date |
| API failure handling | Manual alert to compliance — no auto-retry |
| Logging | Required — compliance audit log per batch |
| maker - checker (batch aproval) | Not required |

---

## API Reference

- 🔌 **GET** `http://api.core-lms.internal.dspfin.com:8080/lms/loan/account/v1/mandate/summary/all`
    
    **Filter:** Accounts where `totalInterestDue > 0` are eligible for comms dispatch.
    
    **Sample Response:**
    
    ```json
    [
      {
        "fenixLoanAccountId": "FXLAN13166311",
        "fenixClientId": "FXCID69538254",
        "accountOpeningDate": 1770860207000,
        "excess": 0,
        "totalPrincipalDue": 4470.71,
        "totalInterestDue": 818.29,
        "totalDue": 5289,
        "dueDay": 7,
        "trancheLevelDetails": [
          {
            "fenixTrancheAccountId": "FXTLAN476636353",
            "excess": 0,
            "principalDue": 4470.71,
            "interestDue": 818.29
          }
        ]
      },
      {
        "fenixLoanAccountId": "FXLAN71875571",
        "fenixClientId": "FXCID37153433",
        "accountOpeningDate": 1771640756000,
        "excess": 0,
        "totalPrincipalDue": 0,
        "totalInterestDue": 0,
        "totalDue": 0,
        "dueDay": null,
        "trancheLevelDetails": [
          {
            "fenixTrancheAccountId": "FXTLAN492824296",
            "excess": 0,
            "principalDue": 0,
            "interestDue": 0
          }
        ]
      }
    ]
    ```
    
    > ℹ️ `FXLAN13166311` → `totalInterestDue: 818.29` → **eligible for comms**`FXLAN71875571` → `totalInterestDue: 0` → **excluded**
    > 

---

# Process Flow

> 📎 See attached workflow diagram — `credit_bureau_comms_flow.png`
> 

---

![trash (1).png](Credit%20Bureau%20Reporting%20Comms/e2f4b5a9-9ded-4ab5-a54d-be568e64d796.png)