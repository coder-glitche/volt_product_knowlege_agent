# Custom Comms based for Ad-hoc situations

: Yogesh D
Created time: March 19, 2026 11:58 AM
Status: Not started
Last edited: March 27, 2026 2:28 PM

# Custom Ad Hoc Comms — DSP Ops Command Centre

---

# What problem are we solving?

- All comms today are system-triggered and automated — ops, compliance, and analytics have zero ability to send ad hoc communications without a tech deployment.
- High-urgency situations (system or service down , regulatory events, manual outreach, one-off campaigns) require immediate comms capability that bypasses the automated pipeline.
- Today adhoc communcoation are sent by product using a script, this consumes a lot of product effort
- There are a few communications which are dependent on flows are in itself are not produtised, hence it is challenching to productise communciation for such flows

---

# How do we measure success?

- **Self-serve rate:** 100% of batches completed by internal teams with 0 engineering tickets and time saved compared to script based approcach by product team
- **Turnaround time:** Median end-to-end time from draft to dispatch ≤ *[X mins/hrs]*
- **Unauthorised send rate:** 0 — 100% of batches pass checker approval before dispatch
- **S3 logging coverage:** 100% of sent batches logged with per-recipient success/failure status
- **Delivery success rate:** ≥ *[X%]* successful deliveries per batch (tracked via S3 logs)
- but we are not doing live tracking and storing of open and click events(webhook based events)

| Metric | Target |
| --- | --- |
| Delivery failure rate | < 2% per batch |
| Log coverage | 100% of records in S3 |
| handle Upto 2 lakh Comms | should be scalable with 
less than 2% error |
| Time to send (maker to dispatch) | < x min |
| Batches dispatched without approval | 0% |

---

# What is the solution?

## Overview

Process for ad-hoc communications - 

1. Analytics team generates recipient data with relevant details (variables)
2. Operations/Product-ops team create and manage SMS/email templates 
    1. L1 owner : Operations/Product Ops
    2. L2 owner : Product 
3. Operations agent use “Bulk communications” maker in the comms section in the command centre and creates a bulk communication checker task
4. Operations agent approves the bulk communication checker task (view access of the bulk communication checker task to be given to compliance team for sampling) 

## Scope

**In scope**

- Actions button + "Send Comms" option in Comms section
- Maker flow:
    - channel selection (SMS, Email)
    - per-channel dynamic variable builder
    - recipient batch file upload (xlsx)
    - remarks window
- Checker flow: approval modal
    - recipient batch file download
    - remarks window
- S3 batch logging: success / failure / opted-out per record (sync API response)

**Out of scope**

- Template creation or DLT registration (templates must exist before use)
- Automated retry on record-level failure (logged as failed, no retry)
- Live tracking of click and open events and Database storage only logs on s3

---

## Fields per channel

| Channel | Required fields |
| --- | --- |
| SMS |   • DLT template ID
  • SMS template body, 
  • variables  |
| Email |   • SendGrid template ID,  
  • variables |

---

## Happy path

1. Operation agent opens Comms section → clicks **Actions** → selects **Send Bulk comms**
2. Maker modal opens → uploads recipient batch file xlsx → selects channel(s) → fills channel fields + variables → clicks **Submit for approval**
3. Batch saved as `PENDING_CHECKER_APPROVAL` — no messages sent yet
4. Checker opens approval modal → reviews batch details + downloads recipient batch file → clicks **Approve**
5. System dispatches comms to all recipients via selected channels
6. Delivery logs (success / failure / opted-out per record) written to S3 sync responses (no webhooks)

## Edge cases

| Scenario | Handling |
| --- | --- |
| Required field missing on submit | Inline validation, highlight empty fields |
| Checker rejects batch | Status → `REJECTED`, maker notified, no comms sent |
| Record-level send failure | Logged as `FAILED` in S3, rest of batch continues — no retry |
| API error during dispatch | Batch-level failure logged; compliance team alerted manually |

---

## Log schema (S3)

- fields to be stored
    
    
    | Field | Description |
    | --- | --- |
    | `batchId` | Unique ID per comms batch |
    | `clientId` | `fenixClientId` of recipient |
    | `channel` | `SMS`  / `EMAIL` |
    | `templateId` | Template used |
    | `status_batch_level` | `SUCCESS` / `FAILED` at batch  level |
    | `status_record_level` | `SUCCESS` / `FAILED` at record level |
    | `timestamp` | Dispatch timestamp |
    | `variables` | Variables used comms |
    | `reciepent address` | phone number, email address |

---

## RBAC

- role based access control
new role added : compliance team
    
    
    | Module | Tasks | Permission Enums | Operations Agent | Support Agent | Operations Manager | Risk Manager | MIS Agent | Business | Finance | Compliance
     |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | Ad hoc Bulk Communications task | Send Custom Comms (Maker) | `MAKER_SEND_ADHOC_COMMS` | Maker | Viewer | Maker | Viewer | Viewer | Viewer | Viewer | Viewer |
    | Ad hoc Bulk Communications task | Send Custom Comms (Checker/Approve) | `APPROVE_TASK_ADHOC_BULK_COMMS` | Checker | Viewer | Checker | Viewer | Viewer | Viewer | Viewer | Viewer |

# Process flow

> 📎 UI maker - checker
> 
- maker UI
    
    requirements:
    
    - [ ]  Button to attach comms batch file
    - [ ]  Purpose of Comms
    - [ ]  Remarks
    - [ ]  option to download sample spreadsheet file
    - [ ]  display the attached file
    - [ ]  Comms **modes** selection sms, Email and whatsapp (multi-select or single)
    - [ ]  **for sms input**
        - [ ]  DLT approved template ID
        - [ ]  SMS body template (add an info(i) button to show sample sms body template
        - [ ]  Abiltity to ADD and remove multiple variable  (add an info(i) button to for instructions to add variables (same as spreadsheet format).
    - [ ]  **for email input**
        - [ ]  approved template ID
        - [ ]  Abiltity to ADD and remove multiple variable  (add an info(i) button to for instructions to add variables (same as spreadsheet format)
    - [ ]  confirm button (for making it ready for checker) or cancel button
    
    ![maker.png](Custom%20Comms%20based%20for%20Ad-hoc%20situations/maker.png)
    
- checker UI
    - [ ]  Details about batch reviewing
        - [ ]  type, channels, created by and creation time,date
    - [ ]  Remarks.
    - [ ]  SMS, Email  Template details for checker review
    - [ ]  option to Download the spreadsheet for reviewing
    - [ ]  approve or reject button
    
    ![checker.png](Custom%20Comms%20based%20for%20Ad-hoc%20situations/checker.png)
    

---

# Open items / checklist

- [x]  Tech — S3 log write on each dispatch
- [x]  Ops — define max batch size limit (5,000 rows proposed)
- [x]  Compliance — sign off on checker approval requirement
- [x]  Template creation or DLT registration (templates must exist before use)
- [x]  RBAC