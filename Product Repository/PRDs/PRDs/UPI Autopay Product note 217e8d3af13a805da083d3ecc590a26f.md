# UPI Autopay Product note

: Parikshit Kumar
Created time: June 19, 2025 2:21 PM
Status: In progress
Last edited: July 9, 2025 12:24 PM

# Overview

UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills.

# **What problem are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

# How it works

## Pre-Requisite

- DSP is onboarded with a PA/PG like Digio/PhonePe/PayU
- DSP receives a VPA in the format dspfin.ppl@ybl (PhonePe)
- DSP’s VPA will be created with MCC code 7322 (loan repayments)
- DSP’s bank account is mapped to the PA/PG from a settlement perspective

## Registration

- Parameters like amount, frequency, start date, and duration are defined at a customer/loan level
- Platform initiates a setup ****request ****via UPI AutoPay
- Customer chooses to set up mandate from one of the **3 modes** offered(Intent mode, Collect mode and QR Scan mode)
- Intent mode: User selects a UPI app(PhonePe/PayTm/GPay, etc) installed on their phone and based on the deep linking user is redirected to the UPI app for mandate authorisation
- Collect mode: User provides their VPA/UPI ID and the mandate setup request is triggered to the users UPI app which they can then open up and authorise the mandate
- QR Scan mode: User scans the QR code of the mandate and get all the UPI apps on their mobile to complete the registration with. This mode is ideal for desktop flows
- In the intent mode, the customer clicks on the UPI specific on app-specific link and is redirected to the relevant UPI app (PhonePe/PayTm/GPay, etc) to complete the registration.
- In the QR mode, the customer chooses on the UPI app of their choice and scans the QR code to complete the registration.
- In the collect mode, the customer enters the VPA (UPI ID) and navigates to the UPI app to complete the registration.
- User **authorizes the mandate** using UPI PIN irrespective of the app chosen.
    - Not all UPI apps support UPI mandate registration.
- Mandate is registered with **NPCI’s Mandate Management System (MMS)**

## Presentation

- Platforms notify users before each transaction via pre-debit notifications (PDN)
- These PDNs need to be sent to the users atleast 24 hours before the auto-debit
- The auto-debit is executed
- Users receive real-time status updates regarding their payments
- Against a single mandate, multiple debits can be initiated capped to 1L/day

## Settlement

- DSP’s PA/PG partner settles the funds to DSP on a T+1/same day basis the commercial agreement
- DSP’s PA/PG partner settles the funds to DSP on a T+1/same day to different bank accounts at the same MID (VPA) level or single bank account

# UPI Autopay Limits and Constraints

- Maximum Amount Per Autopay Transaction – ₹15,000 per transaction (as per NPCI guidelines)
- Maximum Debit Per Day – generally, up to ₹1,00,000 per day (for all UPI transactions combined: P2P + P2M)
- Frequency Options – OneTime, Daily, weekly, fortnightly, monthly, bimonthly, quarterly, halfyearly, yearly and AsPresented
- Authentication for Setup – Requires UPI PIN authentication only during mandate creation.
- Pre-Debit Notification – Mandatory notification to be sent at least 24 hours before the actual debit
- Mandate Modification – Generally allowed but in our MCC(7322) its not allowed from user’s end
- Mandate Cancellation – Generally allowed but users cannot cancel the mandate in our case as we fall in the 7322(Loan repayments) MCC code
- Non-Revokable mandates - Generally allowed but based on our MCC code, our mandates are non-revokable from user’s end
- Failure Handling & Retries – If a transaction fails (e.g., due to insufficient funds) we can do multiple retries, the retry mechanism is determined by the merchant
- Bank Support – Over 330+ banks support UPI Autopay, but functionality may vary per bank
- Merchant Categories Supported – Allowed for financial services, utilities, entertainment, education, etc.; restricted for certain categories like gaming and cryptocurrency (as per RBI norms)
- Immediate debit - We can perform an auto-debit during registration
- Delete the customer VPA - The user can delete the VPA but it will not revoke any of their registered mandates
- Delete the merchant VPA - In such a case all the active mandates associated with that merchant VPA will get deactivated or revoked. In case a merchant VPA is about to get deleted or deactivated then migration of all the active mandates against that VPA needs to be migrated.

## NACH vs UPI Autopay

| **Feature** | **NACH (National Automated Clearing House)** | **UPI Autopay** |
| --- | --- | --- |
| Governing Body | NPCI (ECS-based banking infrastructure) | NPCI (UPI-based infrastructure) |
| Authentication | Requires physical/e-sign/API mandate authorization(API mandate get set up on T+1 in most cases) | Instant UPI PIN authentication at mandate setup. Instant Activation |
| Cost to Merchants | Higher due to manual processing and setup costs | Lower due to fully digital, automated processing |
| Maximum Amount Per Transaction | 1 Cr (as per NPCI guidelines) | ₹15,000 per transaction (as per NPCI guidelines) |
| Maximum Debit Per Day | No specific daily limit | Up to ₹1,00,000 per day (for all UPI transactions combined) |
| Frequency Options | Daily, weekly, fortnightly, monthly, bi-monthly, quarterly, half-yearly, yearly, adhoc | Daily, weekly, fortnightly, monthly, bi-monthly, quarterly, half-yearly, yearly. adhoc |
| Mandate Setup Time | Takes 1-2 days for approval & processing | Instant setup with UPI PIN |
| Max Tenure | 40 Years | 30 Years |
| Pre-Debit Notification | Notification via SMS or call is mandatory | Mandatory pre-debit notification at least 24 hours before the transaction |
| Mandate Modification | Complex, requires bank approval & manual changes. | Allowed; users can increase or decrease the amount, but must authenticate again with UPI PIN |
| Mandate Cancellation | Requires bank intervention for cancellation | Users can cancel anytime through their UPI app(Not applicable for our MCC 7322) |
| Non-Revocable Mandates | Not applicable | Certain mandates are non-revocable, based on Merchant Category Code (MCC). Not revocable for our MCC 7322 |
| Bank Support | 40+ banks for API
200+ banks eSign
400+ for physical mandates | 330+ banks support UPI Autopay, but features may vary by bank ([Link](https://www.npci.org.in/what-we-do/autopay/list-of-banks-and-apps-live-on-autopay)) |
| Immediate Debit within 5 Min | Not applicable | A mandate can be presented within 5 minutes of registration |
| VPA Deletion | Not applicable | Users can delete their VPA without revoking all active mandates |
| First Debit | Post registration | At the time of registration, amount can be deducted. |

# Approach

### OD Product (DSP 100%)(Proposed logic)

- In case of OD product we mostly debit the per month interest for the drawn facility and the charges on the facility(if any).
- Based on the data almost 99% of our users across multiple channels(B2C, B2B, B2B2C Channels) have a DP of less than or equal to 15 Lakhs. Based on the data we will have the below approach.
- Users with selected offer equal to or less than 5 lakhs should only be provided with the option to set up UPI mandates. If these users try and enhance their facility to more than 5 lakhs then a re-mandate should be done.
- Users with selected offer between 5 lakhs and 15 Lakhs should be provided with both the options of eNACH and UPI autopay with the recommended option being eNACH. If they try to enhance their facility then a re-mandate should be done.
- Users with selected offer greater than 15 lakhs should only be provided the option of setting up a NACH mandate.

### OD Product (DSP Co-Lending)

- We can setup a VPA with anyone of the below approaches.
    - DSP’s name : dspfinance.dig@ybl OR
    - Joint name: dsptcllamf.dig@ybl
- We can even use a dedicated VPA for co-lending with our PG partner (Digio/PhonePe)
- Settlements can be routed to the joint collections escrow at a debit level (Digio)

### Term Loan(DSP 100%)(Pending)

- In case of Term Loan product, before the mandate setup process we will get to know the tenure for which the user is opting the Tranche for.
- If the EMI amount for the first tranche in such a case comes to be more than 15k then such a user will be provided with an option to only setup an eNACH mandate.
- If the EMI amount for the first tranche in such a case comes to be less than 15k then we will provide the option to the user to setup a UPI mandate only. If such a user takes subsequent drawdowns from us then if the aggregated EMI amount

# Flow