# Multiple mandate presentation [DSP]

: Ranjan kumar Singh
Created time: June 16, 2025 5:35 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

## **1. Objective:**

To improve the collection efficiency from mandate presentations by optimizing the recovery strategy for overdue interest and charges. This includes introducing a second mandate presentation targeting overdue accounts, especially those with insufficient balance issues in the first attempt.

## **2. Problem statement:**

Currently, DSP present a mandate on the 7th of each month to recover interest and charges due from the previous billing cycle. However, this presentation experiences a **~7% bounce rate**, with **~98%** of failures attributed to **insufficient balance**.

While DSP is not initiating fund sell-offs to recover overdue amounts, the same are carried over to the next cycle. We are able to collect about ~37% overdue from previous month’s cycle.

**Update:** DSP has initiated fund sell-offs starting June 2025. Introducing a second mandate presentation will help reduce the number of accounts that proceed to sell-off by enabling earlier recovery of overdue amounts.

## **3. Supporting Data**

### 3.1 Bounce Analysis (March–May)

- **Bounce Rate**: ~7% of total mandates
- **Reason Breakdown**:
    
    
    | Reason | Count | % of Failures |
    | --- | --- | --- |
    | Balance Insufficient | 1,867 | 97.54% |
    | Other (e.g., A/c blocked, KYC) | 47 | 2.46% |
    | **Total** | 1,914 | 100% |

### 3.2 Mandate Presentation Overview(Presentation month = JUNE)

| Status | Count | Amount | Count % | Amount % |
| --- | --- | --- | --- | --- |
| Success | 24,695 | ₹48,226,124.67 | 92.81% | 93.48% |
| Failed | 1,914 | ₹3,362,233.68 | 7.19% | 6.52% |
| **Total** | 26,609 | ₹51,588,358.35 | 100.00% | 100.00% |

### 3.3 Second Presentation Effectiveness

| Month | Customers Overdue Before | Customers Overdue After | Collection % |
| --- | --- | --- | --- |
| March | 61 | 34 | 44.26% |
| April | 205 | 133 | 35.12% |
| May | 468 | 318 | 32.05% |
| **Average** | — | — | **~37%** |

### 3.4 Customer Behaviour Insights

- **65%** of customers who go overdue clear dues within **20 DPD**.
- Suggests high potential for a **second presentation before 20 DPD** instead of letting overdue carry forward into the next billing cycle.
- This strategy can **avoid negative surprises for customers** and avoid fund sell-offs.
- The **hypothesis**: A well-timed second presentation can drive higher recovery and customer satisfaction with minimal operational complexity.

---

# **How do we measure success?**

| Metric | Target/Benchmark |
| --- | --- |
| **Second mandate collection rate** (of eligible overdue accounts) | ≥ **30%** |
| **Overall collection uplift** due to second attempt | ≥ **2–3%** increase |

---

# **How are others solving this problem?**

Both **TCL** and **BFL** have adopted a strategy of **second mandate presentations within the same billing month** to improve recovery rates from failed mandate attempts.

### **Key Observations**

- **Second mandate is focused on overdue accounts**
    - Collection amount(TCL) = Interest overdue + Penal charges + Charges applied in last billing cycle
    - Collection amount(BFL) = Interest overdue
- **Mandate Timing**:
    - **TATA** re-presents mandates on the **15th of each month**
    - **BFL** re-presents mandates **between the 8th and 13th of the month**
- Reported **collection efficiency for second presentations ranges between 30% and 40%** of overdue accounts.

---

# **What is the solution?**

DSP will **initiate a second mandate presentation on 20th of every month** for accounts with overdue interest and charges, targeting recovery from customers who failed the first attempt and not paid overdue amount till [presentation date - file approval date]

## Requirements overview

1. **Second Mandate Presentation Logic**

| **Condition** | **Logic** |
| --- | --- |
| Collection type | adhoc collection |
| File generation | on demand |
| Eligible Accounts | Interest/charges overdue from prior billing cycle |
| Collection Amount | Interest + Charges + Penal charges |
| Amount Threshold | Skip if total due < ₹10 |
| Waiver Logic | Entire amount (interest + charges + penalty) waived if < ₹10 |
| Penal Charges Handling | Charges posted on or after file generation and approval date-time not included in collection amount (due to cutoff timing) |
| Holiday Handling | If 19th is holiday, file prepared and approved on 18th, cutoff adjusts accordingly |

**2. Workflow**

**2.1 Account Selection & File Generation**

- Ops to generate the presentation file on CC
    - Monthly collection can only be once in a month, adhoc collection can be multiple
    - Monthly collection will be scheduled for all LSPs
    - Adhoc collection can be filtered at a sourcing channel level
- Identify eligible accounts with overdue components
- File Batching has to done at presenter level
- Only whitelisted LSPs are included for presentation by DSP
- OPs to approve presentation on 18th/19th

**2.2 Mandate Presentation (20th)**

- Present for approved accounts
- Communicate with customer and LSPs

**2.3 Post-Presentation Handling**

- **Success:** Repayment posted and overdue cleared
- **Failure:** No dishonor charge applied; prepare for fund sell-off

**2.4 Sell-Off (If Mandate Fails Again)**

- Create sell-off Task/request → Upload file → Initiate → Post settlement & notify user
- Else, recover in next mandate cycle

**Action items for OPS team**

1. Prepare presentation file for overdue amount → Generate presentation file → File will be generated for Account in overdue(as of date/time) → Approve file for presentation → Mandate presentation will be scheduled.
2. DSP ops to share the list of accounts with LSPs so that they can inform customer about the second presentation.
3. Share the list of **overdue accounts with failed second mandate** with LSPs, indicating that DSP will initiate **fund sell-off** for these accounts. - **Out of scope**

**Action items for Tech:**

1. **Presentation File Generation (Post CC Request):**
    - Upon request from the CC , generate the second mandate presentation file.
    - The file should be generated using the logic outlined in points 2(a), (b), and (c) below.
    - File batching should be done **at the  presenter level**.
        - Scope consideration: In future we can introduce loan level filters, or customer level filters, classification level filters (SMA0/SMA1/SMA2)
            
            <aside>
            💡
            
            SMA = **Special Mention Accounts** are a regulatory framework defined by the **RBI**  to identify and monitor incipient stress in loan accounts **before they turn into NPAs (Non-Performing Assets)
            
            EXAMPLE:**
            
            | **Category** | **DPD** | **Description** |
            | --- | --- | --- |
            | **SMA-0** | 1–30 days | Payments overdue up to 30 days. Early warning signal. |
            | **SMA-1** | 31–60 days | Payments overdue between 31 and 60 days. Moderate risk |
            | **SMA-2** | 61-90 Days | Payments overdue between 61 and 90 days. High risk. |
            | **NPA** | 91+ days | Payments overdue for more than 90 days. Classified as Non-Performing Asset. |
            </aside>
            
    - For LSPs whitelisted by DSP for mandate presentations via Digio, scheduling has to be done for those account only. (Volt / Groww / Indmoney / ETMoney)
    - For LSPs managing their own mandate presentations, share the eligible account file with them. (PayTM)
        - LSP can get the mandate collection batch by hitting API
            - API end point: ***{**{LMS-ORCH-BASE-URL}}/lms/api/mandate/management/v1/batch/detail*
        - LSPs to use the Get API to fetch the presentation file once file is approved by DSP ops
        - The current API is designed to handle only the first mandate presentation. We need to enhance it to also support retrieval of the latest **approved or scheduled** mandate file, so that LSPs can access the most up-to-date data for re-presentation.
        - Refer to attached document to understand the current behaviour: https://docs.google.com/document/d/1YFoz4zD6Cnn95Fp-VlGUQ2w12sf9UbtS5XMBQsqqnu4/edit?usp=sharing

1. **Mandate Presentation Request Creation (Eligible Accounts):**
    
    ### a. **Eligibility Criteria:**
    
    - Loan accounts created in the **last billing cycle**, with any **overdue interest and/or charges** as of the presentation file generation date.
    - **Charges include**:
        - Penal charges (posted till the file generation date)
        - Bounce charges
        - Note: Charges like Lien marking posted in current month will be not included in collection amount (Any charges posted in the current billing cycle)
    
    ### b. **Collection Amount:**
    
    - Sum of: **Interest + Charges + Penal Charges**
    
    ### c. **Minimum Threshold Rule (Applicable to All Presentations):**
    
    - Do not generate mandates presentation for total amounts **less than ₹10**.
    - **Waiver Handling:**
        - Currently, only the **interest** component is waived for skipped mandates (≤ ₹10).
        - **Expected behaviour** is to waive the **entire amount** (interest + charges + penalties) to avoid pending balances.
        
        **Current Behavior:**
        
        - Mandate Amount = ₹9 (Interest: ₹3 + Charges: ₹4 + Penalty: ₹2) → Skipped
        - Only ₹3 (Interest) waived
        - ₹6 (Charges + Penalty) remains due
        
        **Expected Behavior:**
        
        - Mandate Amount = ₹9 (Interest: ₹3 + Charges: ₹4 + Penalty: ₹2) → Skipped
        - Entire ₹9 waived → **No pending balance**

**d.Minimum Threshold Rule (Applicable to All Presentations):** 

- Since we are presenting mandate on 20th, we need to prepare presentation file on 19th.
- Penal charges for 19th will apply on 19th Midnight and hence penal charges for 19th will be not included in the collection amount.
    1. If 19th are holiday and presentation file is prepared and approved on 18th
- Penal charges are being post at midnight and **will not be included** in the collection amount of second presentation. Job to post penal charges continues as per current process. Penal charges from 18th or 19th onward will be collected in **next month’s mandate**

---

1. Post mandate presentation
    1. If mandate is successful, post the collection and settle the overdue amount
    2. If mandate presentation is failed, for this presentation **dishonour charges will be not applied**.
    3. Presentation status will be communicated with the LSP through Webhook
        1. Refer to attached document and point number (2): https://docs.google.com/document/d/1YFoz4zD6Cnn95Fp-VlGUQ2w12sf9UbtS5XMBQsqqnu4/edit?usp=sharing

### **Communication requirement:**

1. **Auto-debit notification:**

## MAIL

| **When to send?** | Once the presentation file is prepared and scheduled for presentation |
| --- | --- |
| **Subject** | Auto-debit notification: Outstanding dues for Loan Account {{loan_account_number}} |
| **Body** | Dear {{CustomerName}},

We attempted to collect your outstanding dues recently through auto-debit, but the attempt was unsuccessful.

To help you avoid penal charges or portfolio sell-off, we’ll be making a second auto-debit attempt on {{due_date}}.

🔹 Total Amount Due: ₹{{due_amount}}
🔹 Auto-debit Date: {{due_date}}
🔹 Bank Account: {{bank_name}} xxx{{account_last4digit}}

Amount Break-up:
• Interest: ₹{{interest_due}}
• Charges: ₹{{charges_due}}

Please Note:

The auto-debit can happen anytime during the day on {{due_date}}. Kindly ensure that your account has sufficient balance throughout the day to avoid bounce charges from your bank.

If you’ve already made the payment, the auto-debit will still be processed. The collected amount will be adjusted against your outstanding loan balance.

In case the second attempt also fails and your dues remain unpaid beyond {{due_date}}, we will initiate a portfolio sell-off to recover the overdue amount.

Best regards,
Team DSP Finance |
| **Key variables** | • {customerName}: User first name
• {customerName} : First name of the customer 
• {due_date}: 20th June 2025
• {due_amount} : total dues = interest due + charges due + overdue
• {interest_due} : interest due 
• {charges_due} : charges due 
• {overdue} : overdues 
• {bank_name}: Registered bank account
• {account_last4digit} : last 4 digits of bank account number
• {supportNumber} : DSP support mobile number 
• {supportEmail} : DSP support email ID 
• {date} : Current date 
• {clientId} : DSP client ID 
• {{loan_account_number}} : DSP FXLAN |
| **Email template** | d-48ab205fd2994200b46762d600df4f4b |

## User stories / User flow

## Requirements

---

# **Design**

---

# **Analytics**

- Number of account mandate presented for
- Collection rate
- Bounce rate
- Bounce reason

Note: Data has to be shared by Shreyas

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