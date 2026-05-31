# UPI Autopay Research Doc

: Nihal Simha M S
Created time: February 4, 2025 11:31 AM
Status: In progress
Last edited: June 19, 2025 3:55 PM

## Overview

UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills.

Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users.

Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products.

## 2. Problem Statements

1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions)
2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks.
3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration.
4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience.
5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations.
6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs.

## 3. Use Cases

1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits.
2. Insurance Premiums – Automates life and general insurance premium collections.
3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments.
4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms.
5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services.

## 4. Autopay Features

1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention.
2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually.
3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication.
4. Pre-Debit Notifications – Notify the user in advance before debits occur.
5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates through their UPI apps.
6. Multiple Authorization Flows – Supports intent-based flow (deep links, QR codes) and collect flow (VPA-based approvals).
7. Same Day Debit - Unlike Nach, Mandates can be presented on the same day as registration.
8. First Debit Within 5 minutes - Once the user accepts the autopay, entities can send PDN & execute the mandate within 5 minutes. 

## 5. User Journey

1. Mandate Registration – The user sets up a recurring payment (amount, frequency, tenure) within a UPI app and authenticates via UPI PIN.
2. Pre-Debit Notification – The platform informs users about the upcoming debit at least 24 hours before execution.
3. Mandate Execution – The amount is automatically deducted from the user’s bank account based on the schedule.
4. Transaction Completion – The platform receives confirmation, and the user gets a notification for successful or failed payments.
5. Mandate Modification/Cancellation – Users can update or cancel mandates anytime through their UPI app.

## 6. Functional Requirements

### A. Creation

- Users initiate mandate setup within their UPI-enabled app.
- Parameters like amount, frequency, start date, and duration are defined.
- Mandate registration is authenticated via UPI PIN.

### B. Updation/Cancellation

- Users can modify mandate details (amount, frequency, etc.) with UPI PIN authentication.
- Mandates can be canceled at any time via UPI apps.
    - Non-revokable mandates are also available for lending use cases.

### C. Presentation

- Platforms notify users before each transaction via pre-debit alerts. (PDN)
- Users receive real-time status updates regarding their payments.

## UPI Autopay Limits & Constraints

- Maximum Amount Per Autopay Transaction – ₹15,000 per transaction (as per NPCI guidelines).
- Maximum Debit Per Day – generally, up to ₹1,00,000 per day (for all UPI transactions combined).
- Frequency Options – Daily, weekly, fortnightly, monthly, bi-monthly, quarterly, half-yearly, yearly.
- Authentication for Setup – Requires UPI PIN authentication only during mandate creation.
- Pre-Debit Notification – Mandatory notification at least 24 hours before the actual debit.
- Mandate Modification – Allowed; users can increase or decrease the amount but must authenticate again with a UPI PIN.
- Mandate Cancellation – Users can cancel at any time through their UPI app.
- Non-Revokable mandates - Based on MCC codes, mandates are non-revokable.
- Failure Handling & Retries – If a transaction fails (e.g., due to insufficient funds), the retry mechanism is determined by the merchant.
- Bank Support – Over 320+ banks support UPI Autopay, but functionality may vary per bank.
- Merchant Categories Supported – Allowed for financial services, utilities, entertainment, education, etc.; restricted for certain categories like gaming and cryptocurrency (as per RBI norms).
- Immediate debit within 5min - Mandate can be presented within 5 minutes of registration.
- Delete the VPA - The user can delete the VPA w/o revoking all the registered mandates.

## 7. NACH vs UPI Autopay

| **Feature** | **NACH (National Automated Clearing House)** | **UPI Autopay** |
| --- | --- | --- |
| Governing Body | NPCI (ECS-based banking infrastructure) | NPCI (UPI-based infrastructure) |
| Authentication | Requires physical/e-sign/API mandate authorization (Takes a minimum of 2 days for activation) | Instant UPI PIN authentication at mandate setup. Instant activation. |
| Cost to Merchants | Higher due to manual processing and setup costs | Lower due to fully digital, automated processing |
| Maximum Amount Per Transaction | 1 Cr (as per NPCI guidelines) | ₹15,000 per transaction (as per NPCI guidelines) |
| Maximum Debit Per Day | No specific daily limit | Up to ₹1,00,000 per day (for all UPI transactions combined) |
| Frequency Options | Daily, weekly, fortnightly, monthly, bi-monthly, quarterly, half-yearly, yearly, adhoc | Daily, weekly, fortnightly, monthly, bi-monthly, quarterly, half-yearly, yearly. adhoc |
| Mandate Setup Time | Takes 1-2 days for approval & processing | Instant setup with UPI PIN |
| Max Tenure | 40 Years | 30 Years |
| Pre-Debit Notification | Notification via SMS or call is mandatory | Mandatory pre-debit notification at least 24 hours before the transaction |
| Mandate Modification | Complex, requires bank approval & manual changes. | Allowed; users can increase or decrease the amount, but must authenticate again with UPI PIN |
| Mandate Cancellation | Requires bank intervention for cancellation | Users can cancel anytime through their UPI app |
| Non-Revocable Mandates | Not applicable | Certain mandates are non-revocable, based on Merchant Category Code (MCC) |
| Bank Support | 40+ banks for API
400+ banks for eSign
1k+ for physical mandates | 320+ banks support UPI Autopay, but features may vary by bank |
| Immediate Debit within 5 Min | Not applicable | A mandate can be presented within 5 minutes of registration |
| VPA Deletion | Not applicable | Users can delete their VPA without revoking all active mandates |
| First Debit | Post registration | At the time of registration, amount will be deducted. |

## Conclusion

UPI Autopay is a revolutionary step towards seamless digital payments, offering unparalleled flexibility and automation. Compared to NACH, it provides faster onboarding, real-time processing, and enhanced user control. By integrating UPI Autopay, businesses, and users benefit from automated, secure, and transparent recurring payments, eliminating the hassles of manual intervention.