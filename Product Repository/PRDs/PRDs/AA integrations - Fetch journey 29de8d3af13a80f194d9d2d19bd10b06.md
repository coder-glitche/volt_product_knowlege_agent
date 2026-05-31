# AA integrations - Fetch journey

: Ranjan kumar Singh
Created time: October 31, 2025 4:41 PM
Status: Not started
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

DSP needs a compliant, automated way to fetch users’ demat **stock holdings** via AA for LAS underwriting, without handling other asset classes.

---

# **How do we measure success?**

- % LAS applications where at least one **equities** consent is ACTIVE and data fetch is successful (target ≥ 80%).
- Drop‑off rate between “Start AA stocks journey” and “AA consent completed” (target ≤ 20%).
- Time from “Start AA journey” to “Stocks visible in LAS UI” (p95 < 60 seconds).
- % of LAS limits computed **exclusively** from AA stock data vs other sources (target ≥ 90% in target cohorts).

---

# **How are others solving this problem?**

---

# **What is the solution?**

Introduce an **AA Consent & Data module** backed by Finarkein Nerv “dynamic multi‑consent” APIs.

The module will orchestrate: journey creation, consent state management, data fetch, webhook processing, and normalized holdings storage for LAS underwriting.

## Requirements overview (optional)

- UI: entry point in LAS LOS flow, consent status management, portfolio view (Equities), error and retry handling.
- Backend: integration with Finarkein’s Auth, Consent+Data, Get Status, Data Fetch, Get Result APIs plus three webhooks (journeyStatus, rawDataPush, flowRunStatus).
- LAS logic: convert holdings → eligible collateral → loan limit; expose to LMS/LOS.

## User stories / User flow

### Primary user stories

- As a **borrower**, I want to link my demat accounts via AA so that Volt can compute my LAS limit without asking for manual statements.
- As a **credit underwriter**, I want a consolidated view of all AA consents and holdings per customer so that I can calculate the loan eligibility.

### High‑level user flow

1. User starts LAS application / limit enhancement.
2. Volt UI prompts “Link your demat account via AA”.
3. Backend calls Finarkein Consent+Data API, gets **`requestId`** and **`journeyUrl`**, and UI redirects to AA journey.
4. User discovers and selects accounts (across multiple FIPs) on AA UI.
5. AA/Finarkein creates multiple consents (per FI‑type × account × FIP) and triggers data fetch if **`autoFetch: true`**.
6. Backend receives journeyStatus and rawDataPush webhooks, stores consent artefacts and financial data.
7. User returns to Volt UI and sees linked accounts and holdings; LAS limit is computed and displayed.

### Partial failure flow

- If any consent’s auto data fetch fails, but others succeed, user still sees successful accounts; failed consents show “Data fetch failed – Retry” button, which triggers Data Fetch API.

## Requirements

### Functional

- R1: Ability to initiate an AA consent journey using Finarkein Consent+Data API, passing mobile, PAN, applicationNo, consent templates, and webhooks.
- R2: Persist journey and consent metadata using **`requestId`**, **`consents[].id`**, **`consentHandle`**, **`consentStatus`**, **`dataFetchStatus`**, and **`rawDataPushStatus`**.
- R3: Support autoFetch (true) per consent, with auto data fetch on approval and manual data fetch using Data Fetch API for retries/recurring pulls for failed cases.
- R4: Implement three webhook endpoints for journeyStatus, rawDataPush, and flowRunStatus, ensuring idempotency via **`webhookId`**.
- R5: For each consentHandle, store and normalize AA data (equitiesAccounts) into DSP’s holdings schema.
- R6: Compute collateral value and LAS limit based on holdings and internal risk rules; expose to LOS/LMS.

### Non‑functional

- NF1: p95 time from consent COMPLETED to holdings available < 30 seconds (assuming AA responds within SLA).
- NF2: Webhook processing must be idempotent, durable (logged) and retriable.
- NF3: All AA data encrypted at rest and in transit; strict access control and auditing.

## Status‑mapping for the **AA flow:**

Note: Consent status and data fetch status will be at account level.

| Scope | AA status combo (journey / consent / data) | Where it comes from | UI status text (short) | Explanation / long copy (if needed) | Primary CTA (if any) |
| --- | --- | --- | --- | --- | --- |
| Journey | `journeyStatus = COMPLETED` | Journey Status webhook[eventData.journeyStatus] | “AA journey completed” | “Your AA journey is complete. We’re updating your stock holdings now.” | None (auto progress) |
| Journey | `journeyStatus = ABANDONED` (timeout) | Journey Status webhook | “Consent not completed” | “You didn’t finish connecting your demat account. Please complete this step to get a limit against your stocks.” | “Retry AA consent” |
| Journey | `journeyStatus = FAILED` | Journey Status webhook | “AA journey failed” | “We couldn’t complete the AA journey due to a technical issue. Please try again after some time.” | “Try again” |
| Consent | `consentStatus = ACTIVE`, `dataFetchStatus = SUCCESS` | Journey Status / Get Status / flowRunStatus | “Linked · Data ready” | “Your consent is active and your stock data has been fetched successfully.” | “View stocks” |
| Consent | `consentStatus = ACTIVE`, `dataFetchStatus = PENDING/RUNNING` | Journey Status / Get Status | “Linked · Fetching data” | “Your consent is active. We are currently fetching your stock holdings from AA.” | “Refresh status” (optional) |
| Consent | `consentStatus = ACTIVE`, `dataFetchStatus = FAILED` | Journey Status / flowRunStatus | “Linked · Data fetch failed” | “We couldn’t fetch your stock data from AA. You can retry the fetch or reconnect later.” | “Retry fetching stocks” (Data Fetch API) |
| Consent | `consentStatus = REJECTED` | Journey Status / Get Status | “Consent denied” | “You denied access to your stock data on AA. To get a loan against stocks, please allow read‑only access.” | “Try again with AA” |
| Consent | `consentStatus = REVOKED` | Get Status / future webhooks | “Consent revoked” | “Your consent to share stock data has been revoked. Your holdings may be outdated. Please reconnect via AA.” | “Reconnect via AA” |
| Consent | `consentStatus = PAUSED` | Get Status | “Consent paused” | “Your consent is paused, so we can’t update your stocks. Resume or reconnect to keep your limit updated.” | “Reconnect via AA” (or “Resume” if offered) |
| Data fetch | `state = SUCCESS` (flowRunStatus), `dataFetchStatus = SUCCESS` | flowRunStatus + Get Status / rawDataPush | “Stocks updated” | “Your stock holdings have been refreshed successfully.” | None (auto refresh view) |
| Data fetch | `state = FAILED` (flowRunStatus), `dataFetchStatus = FAILED` | flowRunStatus + Get Status | “Update failed” | “We couldn’t refresh your stock data. This won’t impact your existing limit, but the latest prices may be missing.” | “Try again later” |
| Data fetch | `dataFetchStatus = SUCCESS` but **no holdings** in equities | Get Result / rawDataPush (`summary` empty) | “No stocks found” | “We couldn’t find any stocks in the linked demat account. Please choose another account or proceed without this step.” | “Link another account via AA” |
| System | 400 `InvalidRequest` / `Invalid Consent Handle` | Any Finarkein API error payload | “Session expired / consent invalid” | “This consent has expired or is invalid. Please reconnect your demat through AA to continue.” | “Start new AA journey” |
| System | Network / 5xx while calling Finarkein | DSP backend | “Connection issue” | “We’re facing an issue connecting to AA. Please try again in a few minutes.” | “Retry” |

## Cases handling - Detailed

## 1. Journey creation cases

### Case 1.1 – Start stocks AA journey (happy path)

- **Trigger**: User clicks “Connect demat / Fetch stocks” in LAS flow.
- **Backend**:
    - Generate auth token.
    - Call Consent+Data API with:
        - User: mobile, PAN, clientUserId.
        - `consents[]`: only equities templates (e.g., `Equities01`) with `autoFetch: true`.
        - Webhooks: `journeyStatus`, `rawDataPush`, `flowRunStatus`.
    - Persist Journey with `requestId` and stub Consents with `consents[].id`
- **Response**: `requestId`, `journeyUrl`
- **UI handling**:
    - Show “Redirecting to AA to fetch your stocks…”.
    - Open `journeyUrl` in new webview.

---

### Case 1.2 – Consent+Data API validation error (400 InvalidRequest)

- **Examples**: Missing mobile, invalid PAN, bad webhook URL
- **Backend**:
    - Do not create journey; log errorCode + errorMessage.
    - Return structured error to UI.
- **UI**:
    - Show inline error: “Could not start stocks fetch. Please check your details and try again.”

---

### Case 1.3 – Auth or network failure while creating journey

- **Backend**:
    - If auth failure: refresh token once, retry; if still fails, return consistent error.
    - If network/5xx: retry with backoff up to 2 times; then mark as technical failure.
- **UI**:
    - Show: “We’re facing an issue connecting to AA. Please try again in a few minutes.”
    - Allow user to retry starting the journey.

---

## 2. In‑AA flow and journey status

### Case 2.1 – User completes AA flow (COMPLETED)

- **Webhook**: `journeyStatus` with `journeyStatus: COMPLETED` and `state[]` containing each consent: `id`, `consentHandle`, `consentStatus`, `dataFetchStatus`, `rawDataPushStatus`
- **Backend**:
    - Mark Journey COMPLETED.
    - Upsert each Consent: store `consentHandle`, `consentStatus`, and statuses.
- **UI** (on user returning):
    - If at least one consent is `ACTIVE`: show success banner “Account linked successfully”.
    - Show status of each accounts with status (see section 4).

---

### Case 2.2 – User abandons AA (ABANDONED/timeout)

- **Webhook**: `journeyStatus` with `journeyStatus: ABANDONED`
- **Backend**:
    - Mark Journey ABANDONED.
- **UI**:
    - On return or refresh, show: “You did not finish connecting your demat account. Please complete this to get a limit against your stocks.”
    - Primary CTA: “Retry AA consent”.

---

### Case 2.3 – Journey FAILED (system error at AA/Finarkein)

- **Webhook**: `journeyStatus` with `journeyStatus: FAILED`
- **Backend**:
    - Mark Journey FAILED, log payload.
- **UI**:
    - Show: “We couldn’t complete the AA journey due to a technical issue. Please try again later.”
    - Allow retry; optionally suggest manual document route if multiple failures.

---

## 3. Consent‑level cases

### Case 3.1 – Consent ACTIVE, autoFetch SUCCESS (ideal)

- **Webhook**:
    - `journeyStatus`: `consentStatus: ACTIVE`, `dataFetchStatus: SUCCESS`, `rawDataPushStatus` may be `PENDING/SUCCESS`.
    - `rawDataPush`: with `equitiesAccounts` data
- **Backend**:
    - Store consent handle and artefact.
    - Persist raw data snapshot and normalized StocksHolding records (equities)
- **UI**:
    - Consent chip: “Linked · Data ready”.
    - Display stocks table and computed LAS limit.

---

### Case 3.2 – Consent ACTIVE, autoFetch RUNNING/PENDING

- **journeyStatus** webhook: `consentStatus: ACTIVE`, `dataFetchStatus: PENDING/RUNNING`, `rawDataPushStatus: PENDING`.
- **Backend**:
    - Wait for `rawDataPush` or Data Fetch status; optionally show RUNNING in internal tools.
- **UI**:
    - Consent chip: “Linked · Fetching data”.
    - Show skeleton or “We’re fetching your stocks from AA…”.
    - Auto‑refresh holdings periodically or via “Refresh status” button that hits Get Status API.

---

### Case 3.3 – Consent ACTIVE, autoFetch FAILED

- **journeyStatus** webhook: `consentStatus: ACTIVE`, `dataFetchStatus: FAILED`, `rawDataPushStatus: NA/FAILED`.
- **Backend**:
    - Mark consent’s `latestDataFetchStatus: FAILED`.
    - No holdings stored for this consent.
- **UI**:
    - Consent chip: “Linked · Data fetch failed”.
    - Show CTA: “Retry fetching stocks” → triggers Data Fetch API with that `consentHandle`.

---

### Case 3.4 – Consent REJECTED

- **journeyStatus** webhook: `consentStatus: REJECTED`.
- **Backend**:
    - Mark consent REJECTED; no data fetch attempts.
- **UI**:
    - If all consents REJECTED:
        - Show: “You denied access to your stock data on AA. To get a loan against stocks, please allow read‑only access.”
        - CTA: “Try again with AA”.
    - If mixed (some ACTIVE, some REJECTED):
        - Treat ACTIVE ones normally; show REJECTED ones as “Consent denied” in a secondary section.

---

### Case 3.5 – Consent REVOKED / PAUSED (later state)

- **Get Status** or future webhooks: `consentStatus: REVOKED/PAUSED`.
- **Backend**:
    - Mark consent accordingly; stop new data fetches.
- **UI**:
    - Show: “Consent revoked” with info that holdings may be outdated.
    - If critical for ongoing line, prompt user to re‑link via new AA journey.

---

## 4. Data fetch & refresh cases

### Case 4.1 – Manual Data Fetch (retry / periodic)

- **Trigger**:
    - User clicks “Retry fetching stocks” OR scheduled periodic refresh.
- **Backend**:
    - Call Data Fetch API with `consentHandle` and webhooks (dataPush + flowRunStatus).
    - Persist DataFetchRun with returned `requestId`.
- **Webhook**:
    - `flowRunStatus` with `state: SUCCESS/FAILED`.
    - `rawDataPush` with updated `equitiesAccounts` data if success.
- **UI**:
    - While running: show “Refreshing your stocks data…”.
    - On SUCCESS: update tables and LAS limit; show “Updated just now”.
    - On FAILED: show “Couldn’t refresh data. Please try again later.”

---

### Case 4.2 – Get Result fallback

- **Trigger**: No `rawDataPush` received but Data Fetch status `SUCCESS` OR user manually requests immediate view.
- **Backend**:
    - Call Get Result API with `consentHandle` to retrieve cached data; process only `equitiesAccounts`sections.
- **UI**:
    - Same as success path once data is stored.

---

### Case 4.3 – Invalid consent handle in fetch

- **Error**: Data Fetch or Get Result returns 400 with `errorMessage: "Invalid Consent Handle"`.
- **Backend**:
    - Mark DataFetchRun FAILED with that error.
    - Mark consent as “unusable” for fetch; may require new AA journey.
- **UI**:
    - Show: “This consent has expired or is invalid. Please reconnect your demat through AA.”
    - CTA: Start new AA journey.

---

## 5. Data handling cases

### Case 5.1 – equitiesAccounts only

- **Payload**: `data.equitiesAccounts.accounts[]` with `summary` and `profile` arrays.
- **Backend**:
    - Normalize into StocksHolding rows with:
        - issuerName, ISIN, isinDescription, units, lastTradedPrice, currentValue, maskedAccNumber, dematId, brokerName, fipId, consentHandle.
- **UI**:
    - Single “Stocks” table (equities) and LAS collateral summary.

### Case 5.2 – Empty holdings

- **Payload**: `equitiesAccounts` present but `accounts[].summary` empty
- **Backend**:
    - Store that consent has zero holdings.
- **UI**:
    - Show: “No stocks found in the linked demat account. Please choose another account or proceed without LAS against stocks.”
    - Offer option to start another AA journey (if user has multiple brokers).

## 6. Webhook & infra‑level cases

### Case 6.1 – Duplicate webhook

- **Cause**: Retry from Finarkein.
- **Backend**:
    - De‑duplicate by `webhookId`; if already processed, ignore body.
- **UI**:
    - No visible impact.

### Case 6.2 – Webhook delivery failure

- **Cause**: Our API down / times out.
- **Backend**:
    - Ensure can handle re‑deliveries; monitor missing/late webhooks.
    - If missing too long, UI relies on Get Status / Get Result polling.

---

# **Design**

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes