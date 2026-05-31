# Volt - Overdue Communication Enhancement

Last Edited: April 3, 2026 11:14 AM
PRD ETA: March 9, 2026
PRD Owner: Vaibhav Arora
Status: Completed

# **Background and Context**

Volt Money sends overdue payment alerts to customers when **interest dues are not paid by the scheduled repayment date** for their Loan Against Mutual Funds (LAMF).

These communications are sent across:

- SMS
- WhatsApp
- Email

The purpose of these communications is to ensure customers are aware that:

- Their **interest payment is overdue**
- **Penal charges are being applied**
- Failure to repay may lead to **portfolio sell-off by the lender**

Currently, the communication does not clearly encourage customers to **make payment before the lender sell-off deadline**, which can result in customers attempting payment **on the last day**.

Because payment settlement may take time, last-day payments can still result in **security sell-off**, leading to:

- Customer confusion
- Customer disputes
- Increased support queries

Additionally, communications do not explicitly guide customers to **make payment at least one day prior to the sell-off date**.

To improve clarity and reduce disputes, Volt will update overdue communications to **explicitly instruct customers to make payment at least one day before the lender sell-off date**.

**Important:**

This enhancement will apply **only to DSP as a lending partner** and will **not apply to BFL or TCL portfolios**.

---

# **1. Problem Scope**

## In scope

The following enhancements are included in this release:

- Update overdue communication copies to include **clear repayment instructions**
- Explicitly instruct customers to **pay at least one day before the sell-off date**
- Update communication templates across:
    - SMS
    - WhatsApp
    - Email
- Improve clarity around:
    - overdue payment
    - penal charges
    - lender sell-off timeline

Primary users:

- Customers with **interest overdue on Volt Money LAMF accounts**

Secondary users:

- Customer support teams handling repayment queries
- Risk and collections teams managing overdue accounts

---

## Out of scope

The following items are not included in this enhancement:

- Changes to **overdue calculation logic**
- Changes to **sell-off trigger logic**
- Changes to **penal charge calculation**
- Changes to **repayment workflows in the Volt app**
- Changes to overdue communications for **BFL and TCL portfolios**

Rationale:

This initiative focuses only on **communication clarity improvements**, without modifying underlying **collections or risk processes**.

---

# **2. Success Criteria**

### Primary Outcomes

**1. Reduce disputes during sell-off events**

Customers clearly understand the **repayment deadline and processing buffer**.

**2. Improve overdue repayment behaviour**

More customers make payments **before the final sell-off date**.

**3. Improve communication clarity**

Overdue notifications clearly communicate:

- overdue amount
- penal charges
- sell-off risk
- repayment timeline

---

### Key Metrics

| Metric | Expected Outcome |
| --- | --- |
| Overdue related support tickets | Reduction post rollout |
| Overdue payments before sell-off date | Increase |

---

# **3. Solution Scope**

## Solution Overview

Volt will enhance overdue communications by updating messaging across all channels to explicitly instruct customers to **complete payment at least one day before the lender sell-off date**.

This ensures customers have adequate time for payment processing and reduces the risk of **unintended portfolio liquidation**.

Communication templates across **SMS, WhatsApp, and Email** will be updated accordingly.

Operational updates:

- **Email template updated directly in Sendgrid**
- **WhatsApp template updated in WATI**
- **SMS template will require DLT registration**

This enhancement applies **only to DSP loan accounts**.

---

# Detailed Solution Scope

## Overdue Communication Templates

The following templates will be used for overdue notifications.

---

## SMS Template

(To be registered on **DLT**)

Payment of Rs. {due_amount} for your Volt Money loan is overdue.

Repay before {lender_sell_off_date} to avoid security sell-off. Please ensure payment is made at least one day prior to allow processing. - VOLT

---

## WhatsApp Template

WATI Template Name: **interest_overdue_lamf**

*PAYMENT OVERDUE*

Dear {{customername}},

Payment of *₹{{due_amount}}* for your Volt Money Loan Against Mutual Funds ({{loan_account_number}}) is overdue.

*Important information:*

- Penal charges of *@{{penal_charge}}* are currently applicable on the overdue amount.

• If the overdue amount is not cleared by *{{lender_sell_off_date}}*, the lender may initiate **portfolio sell-off** to recover the dues.

• If your mandate is active, the lender may reattempt **auto-debit from your bank account between the 10th and 20th of the month**.

To avoid any risk of security sell-off, please ensure the payment is completed **at least one day before {{lender_sell_off_date}}** so it can be processed in time.

If you have already paid, please ignore this message.

---

## Email Template

(Sendgrid template updated directly)

Subject: Payment Overdue – Immediate Action Required

Dear {{customername}},

Payment of **₹{{due_amount}}** for your Volt Money credit line (Loan Account: **{{loan_account_number}}**) is overdue.

To avoid defaulting, please make the payment using the Volt Money app.

**Important:**

- Penal charges of **@{{penal_charge}}** are currently being applied on the overdue amount.
- Failure to repay by **{{lender_sell_off_date}}** may lead to **portfolio sell-off** to recover the dues.

To avoid any risk of security sell-off, please ensure the payment is completed **at least one day before {{lender_sell_off_date}}** so it can be processed in time.

If you have already paid, please ignore this message.

Regards,

Team Volt Money

---

### System Changes

| Description | Details |
| --- | --- |
| Email template | Updated directly in Sendgrid (no code change required) |
| WhatsApp template | Updated in WATI (interest_overdue_lamf) |
| SMS template | Requires DLT registration |
| Code changes | None required for template update |
| Applicability | DSP lender accounts only |

---

# **5. High Level System Flow**

1. System detects **interest overdue on loan account**
2. Overdue communication is triggered
3. Notifications are sent through:
- SMS
- WhatsApp
- Email
1. Customer receives overdue notification including:
- overdue amount
- penal charges
- lender sell-off date
- repayment instructions
1. Customer repays overdue amount via Volt app
2. If overdue amount is not cleared by the lender sell-off date:
- Lender may initiate **portfolio sell-off**

---

# **6. Appendix**

## Customer Support Feedback

Customer support teams have reported frequent queries from customers who:

- attempt repayment **on the last day**
- are unaware that **processing delays may still result in sell-off**

Updating communications to encourage **T-1 payment** reduces confusion and improves repayment behaviour.