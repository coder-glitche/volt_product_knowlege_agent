# Volt - Shortfall Communication Enhancement – Due Date Based Messaging

Last Edited: March 31, 2026 11:28 AM
PRD ETA: March 9, 2026
PRD Owner: Vaibhav Arora
Status: Completed

# **Background and Context**

Currently, Volt Money sends **shortfall alerts using a “days remaining” format** in SMS, WhatsApp and Email communications.

**Who is facing the problem**

- Customers with active **Loan Against Mutual Funds (LAMF)** accounts experiencing shortfall
- Volt **customer support team**
- Volt **risk and operations teams**

**What is the challenge today**

Shortfall communications currently mention the **number of days left to resolve the shortfall**, instead of clearly communicating the **exact last date by which the account must be regularised**.

This creates confusion because:

- Customers interpret the timeline differently
- Customers attempt repayment **on the last day**
- Payments may **not settle in time**, triggering **collateral sell-off**

This results in customers contacting support claiming they **were not aware of the final resolution deadline**.

**Why this is important**

- RBI regulations require the **RE to regularise the account within 7 days of shortfall**
- Operationally, customers must repay **before the deadline** to allow settlement
- Current communication format leads to:
    - Increased **customer support queries**
    - Poor **customer experience during sell-offs**
    - Higher **dispute probability**

To improve clarity, Volt will move from **“days remaining” communication to a clear due-date based communication format**.

---

# **1. Problem Scope**

## In scope

The following enhancements are included in this release:

- Replace **“days left” communication with an explicit due date**
- Introduce **due_date variable in shortfall communications**
- Update communication templates across:
    - SMS
    - WhatsApp
    - Email
- Introduce **penultimate-day reminder communication**
- Validate and align **overdue date logic with DSP implementation**
- Encourage repayment **before the due date** to allow processing time

Primary users:

- Customers with shortfall in their Volt Money credit line

Secondary users:

- Customer support team handling shortfall related queries
- Risk and collections teams managing collateral sell-offs

---

## Out of scope

The following items are not included in this enhancement:

- Changes to **shortfall calculation logic**
- Changes to **liquidation timelines**
- UI changes inside the Volt customer dashboard

Rationale:

This initiative focuses only on **communication clarity improvements**, without modifying underlying **risk management processes**.

---

# **2. Success Criteria**

### Primary Outcomes

**1. Reduce customer confusion during sell-off events**

- Reduction in **support tickets related to shortfall deadline confusion**

**2. Improve shortfall resolution behaviour**

- Higher percentage of **shortfall payments made before the last day**

**3. Improve communication clarity**

- All shortfall alerts clearly communicate **final resolution date**

---

### Key Metrics

| Metric | Expected Outcome |
| --- | --- |
| Shortfall related support tickets | Reduction post rollout |
| Shortfall repayment before deadline | Increase |

---

# **3. Solution Scope**

## Solution Overview

Volt will update shortfall communications to use a **due date based messaging format instead of days remaining**.

The **overdue date (shortfall resolution deadline)** will be calculated using the existing shortfall logic and passed as a **due_date variable** into all shortfall communication templates.

Additionally, a **penultimate-day reminder communication** will be triggered to encourage customers to resolve the shortfall before the final deadline.

This change will apply across:

- SMS
- WhatsApp
- Email

Additionally, the due date logic will be validated against **DSP's implementation** to ensure consistency.

---

# Detailed Solution Scope

## Communication Template Changes

Shortfall communication templates will use the variable:

`{{due_date}}`

instead of **days remaining**.

The following templates will be updated or introduced.

---

## Initial Shortfall Notification

### Email Template

Sendgrid Template ID: **d-d374076f189a44c891ca966184e7b5af**

Subject: Shortfall Alert

Dear {{customername}},

We've observed a shortfall on your Volt Money credit line account.

Shortfall amount: ₹{{shortfall_amount}}

Last Date to Resolve: {{due_date}}

Meet shortfall

What is shortfall?

Shortfall occurs when the credit limit drops below the outstanding amount due to fall in market value of pledged portfolio.

How to meet shortfall?

To meet the shortfall, you can repay the shortfall amount or pledge additional securities.

Note: As per RBI regulations, the shortfall must be resolved within 7 days.

To avoid any risk of collateral sell-off, please ensure the payment is completed at least one day before the due date so it can be processed in time.

Regards,

Team Volt Money

---

### SMS Template

(To be registered on **DLT**)

URGENT - Rs. {shortfall_amount} shortfall in your loan against mutual funds. Repay shortfall amount before {due_date} to avoid security sell-off. - VOLT

---

### WhatsApp Template

WATI Template ID: **shortfall_v7**

*SHORTFALL ALERT!*

Dear {{customername}},

We've observed a shortfall on your Volt Money credit line account.

Shortfall amount: *₹{{shortfall_amount}}*

Last Date to Resolve: *{{due_date}}*

*What is shortfall?*

Shortfall occurs when the credit limit drops below the outstanding amount due to fall in market value of pledged portfolio.

*How to meet shortfall?*

To meet the shortfall, you can repay the shortfall amount or pledge additional securities.

*Note:* As per RBI regulations, the shortfall must be resolved within *7 days*.

To avoid any risk of collateral sell-off, please ensure the payment is completed at least *one day before* the due date so it can be processed in time.

For any query, feedback or support, call us or whatsapp us at {{contact_number}}.

---

## Penultimate Day Reminder (1 Day Before Deadline)

This communication will be triggered when **days_left_to_resolve = 1**.

### Email Template

Sendgrid Template ID: **d-96ff16230ee94317a51c27fc187f9922**

Subject: Shortfall Notice – Immediate Action Required

Dear {{customername}},

Your credit limit has dropped below the outstanding amount.

Tomorrow is the last day to meet a shortfall due of ₹{{shortfall_amount}}.

To meet the shortfall, you can repay the shortfall amount or pledge additional securities.

Shortfall amount: ₹{{shortfall_amount}}

Last date to meet shortfall: {{due_date}}

Meet shortfall

Note: According to RBI regulations, it is mandatory to meet shortfall within 7 days. Please ensure the payment is made today to avoid any risk of collateral sell off.

Regards,

Team Volt Money

---

### WhatsApp Template

WATI Template ID: **las_shortfall_last_day_v3**

Shortfall Notice – Immediate Action Required

Dear {{customername}},

A shortfall exists on your loan against shares account {{loan_account_number}}.

To meet the shortfall, you can repay the shortfall amount before 4 PM today.

Shortfall amount: *₹{{shortfall_amount}}*

Expected sell-off value: *₹{{sell_off_amount}}*

Call us or whatsapp us at {{contactnumber}} for any query or feedback.

---

### System Changes

| Description | Details |
| --- | --- |
| Shortfall due date logic | Validate existing logic against DSP implementation |
| Communication payload | Add `due_date` variable |
| Template updates | Replace `days_remaining` with `due_date` |
| Additional trigger | Penultimate-day reminder communication |
| Channels | SMS, WhatsApp, Email |

---

# **5. High Level System Flow**

1. CRMS detects **shortfall due to drop in collateral value**
2. System calculates **shortfall amount and resolution deadline**
3. System generates **due_date variable**
4. Communication service triggers **initial shortfall alerts** via:
- SMS
- WhatsApp
- Email
1. **Penultimate-day reminder** is triggered when **days_left = 1**
2. Customer receives notification showing **explicit last date to resolve**
3. If shortfall is not resolved by the due date:
- Risk system may trigger **collateral sell-off**

---

# **6. Appendix**

## Benchmarking

Most LAS providers and broker platforms use **explicit deadline-based communication instead of days remaining**, including:

- ICICI Direct
- Zerodha
- Groww

This reduces **dispute probability during collateral liquidation events**.

---

## Customer Support Feedback

Customer support has reported **frequent queries after sell-offs**, where customers claim they were unaware of the **exact deadline** to resolve the shortfall.

Moving to **due-date communication** improves transparency and reduces ambiguity in regulatory timelines.