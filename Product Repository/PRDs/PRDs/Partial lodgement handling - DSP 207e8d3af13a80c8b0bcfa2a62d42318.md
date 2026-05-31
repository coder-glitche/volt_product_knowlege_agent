# Partial lodgement handling - DSP

: Ranjan kumar Singh
Created time: June 3, 2025 12:42 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

There is a recurring issue with **pledged mutual funds not being lodged** by DSP when the **pledge status remains in "Pending" or “HOLD”** (DSP check pledge status through get lien status **API before initiating the lodgement**). This results in customer confusion, manual intervention from DSP Ops, and lack of visibility for Volt Ops/Support.

---

### 👤 **Customer Pain Point**

- When a customer's pledged mutual funds are stuck in a **pending or hold status**, DSP does not lodge those funds.
- As a result, the customer receives a **lower-than-expected available amount for disbursement (AMFD)**—sometimes even zero if lodgement is rejected of completely failed.
- Since **Volt does not surface collateral lodgement status at fund level** or communicate the reason for reduced AMFD, the customer is left **confused and dissatisfied**.

---

### 🛠 **DSP Operations Pain Point**

- When DSP gets pledge status as **Pending in** get lien status **API,** DSP polls for **only 30 minutes (every 5 mins)** to check the pledge status.
- If the status remains **"Pending" after 30 minutes**, DSP marks the lodgement status as **"Failed"**. For Hold status, lodgement status is directly marked as FAILED.
- However, in many cases, the **RTA file later shows the pledge as "Successful"**, but DSP has already skipped lodgement.
- In such cases, **DSP Ops must manually lodge the funds**, creating operational inefficiencies and delays.

---

### 🧑‍💻 **Volt Support/Ops Pain Point**

- When a customer raises a ticket regarding **less-than-expected AMFD**, the issue is escalated to the on-call team.
- The on-call team then contacts DSP to verify the pledge and lodgement status.
- Volt Ops/Support **lacks visibility at the fund level** for lodgement status, making it difficult to resolve user queries efficiently or proactively.

---

# **How do we measure success?**

- Reduced number of customer queries regarding lower-than-expected AMFD
- Reduced operations team hours spent on manual lodgement
- Reduce ticket resolution time related to lodgement cases.

---

# **How are others solving this problem?**

---

# **What is the solution?**

To address the visibility gaps, manual operations, and poor customer experience caused by undisbursed pledged funds, the following solutions are proposed:

---

### ✅ 1. **Fund-Level Lodgement Status Tracking at Volt end**

- **Volt will store collateral lodgement status at the individual fund level** (i.e., per folio/ISIN).
- This enables:
    - **Transparent communication** to the customer about why their AMFD is lower than expected.
    - **Internal visibility** for Volt Support and Ops teams to resolve queries without raising tickets to DSP.
    - Retry lodgement of funds that failed to lodge due to RTA issues or unconfirmed pledge status.

---

### 🔁 2. **Automated Retry Logic for Failed Lodgements**

- **Volt will actively fetch and monitor the lodgement status** of pledged funds.
- In case a pledge is eventually successful but lodgement failed (e.g., due to DSP’s 30-minute polling timeout), **Volt will trigger a retry for the 'Add Collateral' request** automatically.

---

### 🧹 3. **DSP Feedback Loop for Retry Eligibility**

- **DSP will provide a sanitized list or tagging mechanism** to identify which failed lodgements are eligible for retry.
    - Example: Status codes like `RETRYABLE` vs. `NON-RETRYABLE`
- **Volt will only retry lodgement** for those funds explicitly marked as **retryable** by DSP.

<aside>
💡

At the time of opportunity creation, LSPs are not required to call the Add Collateral API to lodge the funds. DSP will handle the lodgement automatically after the integration of pledge V2 API. Therefore, this solution will only apply to line enhancement cases, where LSPs need to call the Add Collateral API. 

</aside>

## Requirements overview (optional)

Requirement for DSP:

- Expose subStatus to LSP in Add collateral web-hook, This will enable LSPs implement logic to retry lodgement for partial lodgement cases when they get Partial success as subStatus.
- Sanitisation of fund level status to identify which funds can be retried for lodgement.
- Flag to identify weather lodgement request will go under STP flow or Non STP flow.

Requirement for Volt:

- Volt to Start maintaining the lodgement status of each funds at ISIN/folio level
    - lodged: TRUE/FALSE
    - Mapping with associatedCollaterals status of add collateral API response
        - When status = LODGMENT_FAILED then lodged = FALSE
        - When status = LODGED then lodged = TRUE
- Volt to retry the add collateral api in case of below scenario
    - When Add collateral status is success and subStatus is Partial success
    - Retry with associatedCollaterals status of collateral with ‘LODGMENT_FAILED’
        - Stop when Status success and subStatus success AND Status Failed or rejected
    - Frequency : Every 30 min from the time of first add collateral API call

Open points:

- In case of manual lodgement or when lodgement status changed later then DSP provide web-hook but Volt do not listen webhook to change the status.
    - How Volt will identify which funds status to update?
    - DSP should give flag to identify system originated(LSP) or manual lodgement through CC
    - Request source = COMMAND_CENTER means manual lodgement
    - Sync asset mapping using getholding data API when we get manual lodgement web-hook
- When ever Add collateral API is called, DSP every time call **consolidated lien API to check pledge status? - YES**

## User stories / User flow

## Requirements

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