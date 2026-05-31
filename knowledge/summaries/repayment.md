# Current State: Repayment

> Auto-generated from 206 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — PRD - Mandate conversion optimisation via swap in
**Status:** Not started | **Last edited:** September 3, 2025 2:24 PM

**Problem:**
are we solving?**

Currently, the user journey follows **Bank Account Verification → Mandate Setup → Pledge**.

- Users feel hesitant about setting up a **bank mandate before pledging assets**.
- This results in drop-offs at the mandate step, as the user hasn’t yet committed to taking a loan.
- Additionally, mandates are sometimes created for users who **never pledge**, leading to wasted effort, operational overhead, and potential regulatory friction.

We want to reverse the sequence to **Pledge → Bank Verification → Mandate**, so the mandate is only triggered once the user has committed by pl

**Solution:**
?**

Reorder the loan journey flow as follows:

1. **Pledge** (user commits MF units as collateral).
2. **Bank Verification** (fetch & confirm repayment account with penny drop).
3. **Mandate Setup** (NACH/e-mandate/UPI Autopay).

This ensures only committed users proceed to mandate, improving mandate conversion and reducing unused mandates.

---

## #2 — Loan Offer Optimisation experiment for CheQ
**Status:** In progress | **Last edited:** September 2, 2025 5:55 AM

**Problem:**
are we solving?**

Currently we are observing low conversion rate at loan offer page selection for CheQ compared to other B2B partners for (June and Aug month) ~ 7pp lower.

**For ≥10K eligible limit (CheQ):**

| **Step** | **Aug** | **Jul** | **Jun** |
| --- | --- | --- | --- |
| **Loan Offer selection %** | 19% | 29% | 18% |

**For ≥10K eligible limit (Other B2B partners ex CheQ and PP)**

| **Step** | **Aug** | **Jul** | **Jun** |
| --- | --- | --- | --- |
| **Loan Offer selection %** | 25% | 30% | 31% |

For **July** month overview of drop-offs at each stage in the funnel from eligible cre

**Solution:**
?**

---

## #3 — AI Chatbot
**Status:** Not started | **Last edited:** September 1, 2025 10:48 AM

**Problem:**
are we solving?**

Currently the FRT for the response is higher (9+ minutes)
Average resolution time of the chat is 60+ minutes)
No 24 hour service limited hour servicing

---

**Solution:**
?**

The **AI Chatbot Proof of Concept (POC)**, this document outlines the **Phase 1 scope**, focused on backend integration, benchmarking, and foundational design to prepare for future customer-facing deployment via **WATI**.

---

## #4 — Interest calculator - landing page
**Status:** In progress | **Last edited:** October 9, 2024 8:22 PM

**Problem:**
are we solving?**

1. Before applying for Volt LAMF or withdrawals users want an estimate of what is the interest that they will pay.
2. Since alot of user consider Volt LAMF as term loan, they want to get an understanding of how to close the loan in X duration with equal monthly payments. MFDs are asked this query alot as well. 

---

**Solution:**
?**

---

## #5 — DSP Website
**Status:** In progress | **Last edited:** October 8, 2024 7:17 PM

**Problem:**
are we solving?**

As a regulated entity, DSP needs to have a website in its name with basic details. This is required from a regulatory  perspective to disclose key policies, procedures, etc.

In addition, certain borrowers also research the lender they have taken a loan from and would want to reach out for any concern or query.

---

**Solution:**
?**

---

## #6 — Multi Drawdown Term Loan LMS Requirements
**Status:** In progress | **Last edited:** October 30, 2025 2:56 PM

**Problem:**
are we solving?**

The existing OD-based Loan Against Mutual Funds (LAMF) product does not align with the repayment expectations and financial behavior of a large segment of customers. These users are more familiar with **structured EMI-based repayment formats**, as seen in personal loans, home loans, and auto loans. As a result, product comprehension, drawdown confidence, and repayment discipline are negatively impacted when only an OD line is offered.

This gap is particularly visible in:

- Low drawdown rates from sanctioned limits
- Confusion around usage-based interest calculation
- Hesit

**Solution:**
?

Product Overview

We propose a **term-loan-style wrapper** on top of the facility construct to match user expectations and drive better usage. The solution involves:

- **Offering a familiar term-loan onboarding flow** for the first drawdown.
- **Enabling multiple drawdowns** from the same facility, with flexibility in amount and tenure.
- **Allowing re-borrowing** once limits are replenished through repayment.
- **Positioning the product clearly as “term loans with flexibility”**

This hybrid approach is designed to increase adoption, improve credit utilization, and grow customer LTV.

**Product Technical Construct**

A **line-backed, multi-drawdown term loan**, where:

- **Both loan and tranche constructs are exposed to the LSP**.
- DSP manages the **loan** as the credit container; **

---

## #7 — Master collections PRD (NBFC)
**Status:** In progress | **Last edited:** October 3, 2024 1:50 PM

**Problem:**
are we solving?**

There are multiple instruments through which NBFC will acquire funds against outstanding of user’s loan account. Following are the one’s we are moving ahead with V1:

- Repayments (PG/Bank account transfer)
- Withdrawals (Collection of charges against withdrawal - Capitalisation)
- Mandate presentation
- Sell-off of collateral to recover funds (Shortfall/Overdue)

**Collections can be of two types:**

- User initiated (Withdrawal / Repayment / Sell-off)
- NBFC initiated (Mandate presentation (Interest and charges) / Sell-off)

This document unites all of the instruments into

**Solution:**
?**

- Withdrawal (Charges collection against withdrawal)
    
    When a user withdraws from their credit line against their pledged assets, we will identify if there are any associated charges due in the loan account. 
    
    If overdue charges are found, charges will be knocked off and the effective amount will be disbursed to the user
    
- Repayment
    
    When a user makes a repayment, their repayment will be accounted against different ledgers of the loan account as per the configured apportionment strategy
    
    Overdue interest -> Overdue charges -> Shortfall principal -> Due interest -> Due charges -> Principal -> Excess
    
- Mandate presentation (Interest collection)
    
    At the end of the billing cycle, outstanding interest (accumulated over the cycle) and due cha

---

## #8 — Integrated Sales tool
**Status:** In progress | **Last edited:** October 14, 2024 2:04 PM

**Problem:**
are we solving?**

Support systems face significant challenges in managing multi-channel customer queries across B2C, B2B2C, and partner channels. These issues include fragmented communication, difficulty handling diverse customer types, inadequate issue categorization, lack of centralized ticketing, ineffective SLA tracking, absence of real-time performance dashboards, fragmented reporting, delayed follow-ups, communication errors, and no customer feedback mechanisms. These problems lead to decreased customer satisfaction, poor service levels, and reduced operational efficiency.

- We don’t h

**Solution:**
? (potential)**

Implement a centralized, multi-channel support system that unifies all customer interaction channels (email, chat, phone, WhatsApp) into a single platform. This system should support segmentation for B2C, B2B2C, and partner customers, incorporate automated ticketing and routing based on issue complexity and customer type, enforce SLA tracking, provide real-time performance dashboards, and include integrated feedback mechanisms.

- INBOUND
    - Calls
        - Call are routed or provided by Exotell
        - Received calls
            
            
            | Type | Instance | percentage |
            | --- | --- | --- |
            | Incoming | 1595 | 26.14% |
            | Outgoing | 1407 | 23.06% |
            | Missed | 2950 | 48.35% |
            | Rejected | 132 |

---

## #9 — [TL] Shortfall handling
**Status:** Pending Review | **Last edited:** October 1, 2025 1:26 PM

**Problem:**
are we solving?**

---

- We want to implement a robust mechanism to handle shortfall scenarios in term loans. Unlike OD products, term loans involve an outstanding principal amount, which increases the likelihood of shortfalls. This makes it essential to build an efficient and well-defined shortfall handling process specifically for term loans

**Solution:**
?**

---

## #10 — Repayments Error Handling and Changes
**Status:** In progress | **Last edited:** November 6, 2024 1:24 PM

**Problem:**
are we solving?**

Customers are facing issue in receiving repayment confirmation from TATA due to SOA not getting updated from TATA’s end. This results in the below challenges.

- Customer satisfaction (CSAT) impacted
- Reduced retention due to poor customer experience
- Number of customer support tickets increase

These issues arise due to failure to account a successful payment at the Payment Gateway (PG) level to the Statement of Account(SOA) of the user due to an error in the saveLoanReceipt API.

Total failure rate ~ 3%

- Current failure rates for successful transactions is 1.37%
- Fail

**Solution:**
?**

---

## #11 — NBFC Virtual Accounts for Repayments (Alignment)
**Status:** In progress | **Last edited:** November 27, 2024 4:59 PM

**Problem:**
are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

The problems can be further distilled into.

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted
- We want to handle large ticket repayments from customers more seamless, especially for MFD channels wher

**Solution:**
?**

---

## #12 — NLP-736 Timestamp value is not captured with hh mm
**Status:** Not started | **Last edited:** November 19, 2024 7:41 AM

# NLP-736: Timestamp value is not captured with hh:mm:ss due to which the default value 05:30:00 is shown in the UI Command centre search result pages: Client creation date (client search) Expiry date (loan search) Bureau pull date (client details risk section) AML pull date (client details risk section) Mandate expiry date (loan details section) Expiry date (is in small case) KYC expiry date is comming as invalid date Completed on (repayment detail is coming as invalid detail)

---

## #13 — Foreclosure handling for DSP
**Status:** Done | **Last edited:** November 18, 2024 12:09 PM

**Problem:**
are we solving?**

Users at this point in time can raise multiple requests at a time, these transactions can often cause the other to fail. 
For example, if a user, raises a withdrawal which is pending with the NBFC to process, and immediately raises a foreclosure, they will be able to, which may cause dangling transactions to be left at our end.

If a user raises a foreclosure request, when a mandate presentation transaction is still processing for them, and we close the loan account, we will have no way to post the proceeds from the presentation into their loan account. 

To solve for such s

**Solution:**
?**

Types of requests (Money/Collateral/Service):

| Type of request | Foreclosure blocked |
| --- | --- |
| Withdrawal | Yes |
| Repayment | Yes |
| Collateral removal | Yes |
| Collateral addition | Yes |
| Excess refund | Yes |
| Mobile update | No |
| Email update | No |
| Foreclosure | Yes |
| Withdrawal reversal | Yes |
| Repayment reversal | Yes |
| Charge reversal | Yes |
| Interest refund | Yes |
| Mandate presentation | Yes |

For any request which is pending, as per the above sheet, foreclosure request will not be processed instead we will pass an error message to the LSP.

Foreclosure cannot be processed as there is an existing pending request (Request ID: [Request ID]). Please resolve or complete the pending request to proceed with foreclosure.

In case there are multiple pen

---

## #14 — White-labelled Redirection Journey for B2B Partner
**Status:** In progress | **Last edited:** November 14, 2024 7:27 PM

**Problem:**
are we solving?**

Smaller B2B partners want to go live with Volt’s offering but don’t to spend a lot of bandwidth in validating the demand. Hence, they choose to opt for the redirection based offering.

The current redirection based offering presents the below challenges.

- Customers sourced from partners not having trust as they don’t know Volt
- Partners not being comfortable in bringing Volt to the flow
- Customers dropping off on Volt’s homepage
- Partners not opting to go-live with Volt
- Time taken to go-live for partners increase impacting adoption

The above challenges can be attribu

**Solution:**
?**

---

## #15 — Repayment failure handling
**Status:** In progress | **Last edited:** November 12, 2024 1:14 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

---

## #16 — Repayment flow for DSP
**Status:** Pending Review | **Last edited:** November 11, 2024 8:01 PM

**Problem:**
are we solving?**

We offer three payment methods for a user to be able to make a repayment towards their loan via Razorpay:

- UPI
- Debits cards (Rupay)
- Net banking

For net banking, Razorpay assists us with partnering with different banks so that they can offer net banking as a service with our sponsor bank (Yes bank). Currently we are only utilising Razorpay integration as an LSP (via Volt) and do not have a repayment flow on the DSP website. 

To enable large banks like SBI, HDFC, ICICI, IDFC bank, we need to have a repayment flow on the DSP website to meet compliance requirements.

---

**Solution:**
?**

We will build an intermediate repayment flow for users to be able to make a repayment on their loan account on the DSP landing page (to showcase to Banking partners)

---

## #17 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #18 — Replacing the MFD referral messgage
**Status:** Not started | **Last edited:** May 8, 2025 4:10 PM

# Replacing the MFD referral messgage change the Referral message to ” Greetings 🙏 Help your clients meet short-term cash needs without redeeming mutual funds. Use Volt to open a credit line against mutual funds in 5 minutes with trusted lenders such as DSP Finance. Interest rates starting at 10.49. Use this link to empanel now. [https://voltmoney.in/partner?ref=HMWGGX](https://voltmoney.in/partner?ref=HMWGGX) Regards, Naman agarwal” ![Screenshot 2025-04-14 at 1.57.44 PM (1).png](Replacing%20the%20MFD%20referral%20messgage/Screenshot_2025-04-14_at_1.57.44_PM_(1).png) [https://voltmoney.in/partner/referredpartner](https://voltmoney.in/partner/referredpartner) Whatsapp, telegram , copy message

---

## #19 — [Platform] Callbacks for LSP APIs for core servici
**Status:** In progress | **Last edited:** May 29, 2026 6:19 PM

**Problem:**
are we solving?**

There are core transaction and request lifecycles that need to be managed by the LSP. 

Volt as an LSP has built a lot of pollers and CRON jobs at specific days over existing lender APIs to solve for this. However this approach has a lot of challenges.

- Introduces a lot of computational load both at the LSP as well as the lender
- Not very accurate, as logic is based on top of hitting jobs on specific dates and times
- Requires a lot of maintenance at an engineering level across systems

Most of these APIs get data from core systems like the CTMS or the LMS, and this often

**Solution:**
?**

Building callbacks for core servicing flows:

- Due collection (lifecycle)
    - When interest becomes due
    - When mandate is presented
    - When mandate collection is successful
    - When mandate collection fails
    - When interest is settled
- Repayment
    - When a repayment is posted into the user’s loan account
- Shortfall
    - When shortfall is identified (daily job) in a user’s loan account
    - When shortfall updates for a loan account (change in amount/ageing)
    - When shortfall is settled for a user’s loan account
    - When shortfall crosses grace period (due date) and sell-off is initiated for the user
    - When sell off is completed
- Foreclosure
    - When a foreclosure request is approved for the user

---

## #20 — PRD — Term Loan Repayment STP Threshold Update
**Status:** Not started | **Last edited:** May 29, 2026 5:51 PM

**Problem:**
are we solving?

- Current STP repayment thresholds are overly conservative, causing valid low-risk repayments to be unnecessarily routed to NSTP via `REPAYMENT_AMOUNT_LIMIT_EXCEEDED` (>₹15L) and `REPAYMENT_DAILY_COUNT_EXCEEDED` (>4 repayments/day per LAN).
- Jan–May 2026 production data shows minimal breach risk: only 3 of 1,952 customers (0.15%) made repayments above ₹15L (max observed: ₹20.1L), and no LAN exceeded 5 repayments in a day — indicating the limits can be safely relaxed.
- Unlike other LSPs (Razorpay for Volt, PhonePe dashboard for PhonePe), there is no Cred repayment dashboard a

---

## #21 — Sell-off Repayment Reconciliation — Maker Automati
**Status:** Not started | **Last edited:** May 29, 2026 3:39 PM

**Problem:**
are we solving?

- Today, the maker step for sell-off repayment reconciliation is entirely manual: the ops team downloads the bank statement and RTA/MFC payout reports, manually cross-references UTRs and amounts, and then maps each payout row transaction to a CDID before uploading the `bulk_unlodgement_post_sell_off` file into the Command Centre.
- This process is error-prone, time-consuming, and creates a daily dependency on ops/analytics bandwidth before the repayment posting flow can even begin.

**Solution:**
?

**In scope:**
- Daily automated UTR matching between payout reports (KFin, CAMS, MFC) and bank statement.
- Amount validation (BS settled amount vs. report expected deposit amount) at row level.
- Intra-report UTR deduplification before matching.
- PAN → FXLAN → SCRID → CDID key-based resolution per pledge source and repo type.
- CDID uniqueness enforcement with disambiguation logic for repeated sales.
- Row-le

---

## #22 — STP validation for Sell-off Repayment Reconciliati
**Status:** Not started | **Last edited:** May 27, 2026 3:11 PM

**Problem:**
are we solving?

- Today, all sell-off repayment reconciliation(approval) requests initiated via "Bulk Unlodgement Post Sell Off" in the Ops Command Centre go through the NSTP path — every record creates a checker task requiring manual review and approval.
- With an average of 173 requests per day (as of Jan–March 2026), manual processing introduces delay in repayment reconciliation execution.
- Manual processing increases operational bandwidth consumption of OPS team and introduces human-prone errors.
- With the implementation of this feature we will be able to provide task description for ch

**Solution:**
?

**In scope:**
- For all UTRs in input file, UTR existence check against the bank statement.
- Settled Amount retrieval from the bank statement for the matched UTR.
- RTA report matching using the appropriate logic per RTA type — Folio + ISIN + Units + Session ID for KFintech, and Folio + ISIN + Lien Marking Number for CAMS.
- Bank-vs-RTA amount comparison, with auto-posting of matched records into the loan acco

---

## #23 — Phase 0 LTV Tenure Update_LOS
**Status:** Not started | **Last edited:** May 25, 2026 4:26 PM

**Problem:**
are we solving?**

Problem 1: LTV at 45

DSP's LAMF product offers 45% LTV on equity and hybrid funds, compared to 70% LTV offered by banks — making it structurally uncompetitive. This gap limits DSP on three fronts:

- **Existing customers** are under-drawing against already-pledged assets, leaving loan book growth on the table
- **New customers** in lower-ticket segments have sufficient collateral at 70% LTV but fall below viable thresholds at 45%
- **Product parity** with banks cannot be achieved without closing this 25pp LTV gap

Problem 2: Tenure at 3 years

RBI has recently mandated that

**Solution:**
?**

**In scope:**
(Phase 0)

Product

- LTV increase from 45% → 70%
- 6-year tenure migration
- Partner-level LTV configuration
- Updated KFS/Agreement templates

Customer Scope

- New customers
- Existing users still within LOS flow

Platform Scope

- DSP (Fenix)
- LSP integrations
- Volt & its partners

---

## #24 — Jupiter FE requirements
**Status:** Not started | **Last edited:** May 23, 2024 12:54 PM

**Problem:**
are we solving?**

Because we are removing bottom NAV and My account section, we need to move entry point of functionalities to main dashboard, following PRD covers those cases.

---

**Solution:**
?**

---

## #25 — LSQ Chat workflow - Phase 1
**Status:** In progress | **Last edited:** May 22, 2026 2:25 PM

**In scope:**
- Chat-to-ticket mapping for every incoming conversation
- Ticket lifecycle management (Open, Pending, Overdue, Resolved, Closed)
- SLA tracking (First Response Time, Resolution Time, Overdue)
- Automatic ticket creation for non-working hours and holidays
- Assignment of chats only to available agents
- Agent visibility into past chats and existing tickets
- Mandatory disposition capture for every

# LSQ Chat workflow - Phase 1 # **WhatsApp Customer Support – End-to-End Chat Process Note** # **Objective** The objective of this process is to transform WhatsApp-based customer conversations into a **structured, ticket-driven support system** using LeadSquared as the system of record. This process aims to ensure that every customer interaction is: - **Trackable** through ticket creation and lifecycle management - **Actionable** via proper routing, assignment, and SLA-based handling - **Contextual** through unified visibility of past interactions and tickets - **Measurable** using key metrics such as First Response Time (FRT), resolution time, and First Contact Resolution (FCR) - **Insight-driven** through mandatory disposition capture and outcome tracking - **Customer-centric** by enabling timely responses and feedback collection (CSAT) 👉 Ultimately, this enables **end-to-end visibility, operational control, and continuous improvement of customer experience and support performance**. ## Problem Statement (Final) The current WhatsApp-based support system, built on WATI, operates as a **messaging layer rather than a structured support system**, resulting in gaps across **execution, visibility, and performance measurement**. # 1. Execution Gaps - Chats are not systematically classified into open, pending, or closed states - Conversations received during non-working hours and holidays are not reliably captured or prioritized - Chats are assigned without validating real-time agent availability - There is no standardized workflow for handling, resolving, and closing chats Result: Customers experience **delayed responses, missed interactions, and inconsistent support journeys** | **Holiday Break Up** | | | | | | --- | --- | --- | --- | --- | | **Month** | **N** | **Y** | **Grand Total** | **%** | | Jan'26 | 5143 | 649 | 5792 | 11.21% | | Feb'26 | 6809 | 96 | 6905 | 1.39% | | Mar'26 | 5129 | 1399 | 6528 | 21.43% | | **Grand Total** | **17081** | **2144** | **19225** | **11.15%** | ### 2. Visibility & Control Gaps - There is no real-time view of active, unanswered, or overdue conversations - SLA metrics such as First Response Time (FRT) and resolution time are not consistently tracked or enforced - Missed chats (no response within SLA) are not identified or monitored Result: Operations function **reactively**, with limited ability to manage workload or ensure service quality | **Expired chats Break Up** | | | | | --- | --- | --- | --- | | **Month** | **N** | **Grand Total** | **%** | | Jan'26 | 41 | 5792

---

## #26 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #27 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #28 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #29 — Enhancement Of STP NSTP validations for Bulk sell
**Status:** In progress | **Last edited:** May 20, 2026 11:40 AM

**Problem:**
are we solving?**

[STP validation for Bulk Sell off](STP%20validation%20for%20Bulk%20Sell%20off%20336e8d3af13a802c8283d86e576f3220.md)

[E2E Sell-off Productisation V1 ](../LMS%20PRDs/E2E%20Sell-off%20Productisation%20V1%20352e8d3af13a80f9a75bed081dd798f0.md)

Initial STP/NSTP validation for bulk sell off approvals missed key sell-off logic, causing both false NSTP routing and incorrect STP approvals. 

- **Min redemption round-up missed:** Sell-off units are rounded up to meet minimum redemption requirements, increasing sell-off amount vs obligation — ~800/4,000 cases were wrongly pushed to 

**Solution:**
?

**In scope:**
- Per-CDID min_redemption_flag check and delta-tolerance  applied after standard STP formula.
- Replacement of partial overdue with full total_overdue (principal + interest + charges) from get_overdue_detail API in all DPD and Shortfall validation formulas.
- Reading dpd_trigger from fenix_sell_off_collaterals_request and selecting dpd_amount_75_trigger or dpd_amount_21_trigger from get_overdue_de

---

## #30 — Redemption vs LAMF Calculator & Comparison Tool
**Status:** In progress | **Last edited:** May 20, 2025 3:46 PM

# Redemption vs. LAMF Calculator & Comparison Tool ## Problem We’re Solving - Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively. - Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan. - Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal. - Currently, MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds. - Through RRC, we aim to address the following objectives: - Education and awareness about LAMF to out TG - Branding through marketing and organic sharing ## Objectives - Educate and raise awareness around LAMF. - Help clients make **informed financial decisions**. - Arm MFDs with a professional, branded, easy-to-use digital tool. - Drive brand trust through co-branded PDF reports and shareable content. ## User Stories (MFD-Focused) 1. **Fetch & Consent** - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.* 2. **Custom Amount & Instant Comparison** - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”* 3. **Crystal-Clear Visuals** - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.* 4. **Branded Takeaway** - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.* ## 🛠️ Tool Overview & Flow ### 1. **Customer Consent & Details (Screen 1)** - Inputs: Client Mobile Number, Client PAN - Button: “Enter OTP” ### 2. **OTP & Eligibility Fetch (Screen 2)** - Input: OTP - Fetch: MF holdings + Max LAMF limit - Errors:- - Combination is not registered on the MF central - No funds - Available limit is insufficient. ### 3. **Input Desired Amount (Screen 3)** - Display: Max eligible amount (e.g., ₹5,00,000) - Input: Desired amount (editable) - Button: “Compare Redemption vs. LAMF” ### 4. **Comparison View (Screen 4)** Two-column layout: | Parameter | Redeeming MFs |

---

## #31 — STP validation for Bulk Sell off
**Status:** Done | **Last edited:** May 19, 2026 4:09 PM

**Problem:**
are we solving?

- Today, all sell-off requests initiate via the "Bulk Initiate Sell Off"  in the Ops Command Centre and go through the NSTP (Non-Straight-Through Processing) path — every record creates a checker task requiring manual review and approval.
- With average of 193 requests per day (as of Jan-March 2026), manual processing introduces delay in sell-off execution.
- Manual processing increases operational bandwidth consumption of OPS team and introduces human-prone errors.

**Solution:**
?

**In scope:**
- STP validation for Shortfall and DPD sell-off types .
- Auto-approval and dispatch for STP-eligible LANs (no checker task created)
- NSTP routing with reason codes for all non-eligible LANs
- Ongoing sell-off status check before STP approval
- Multi-row LAN aggregation (∑ across ISINs for CMV )and LTV fetch for CMV × (1 − LTV))
    - **Aggregation rule**
        
        > **Important**: A singl

---

## #32 — Dues Comms Updation
**Status:** Not started | **Last edited:** May 15, 2026 4:30 PM

**Problem:**
are we solving?

- Current SMS templates for due reminders, auto-debit alerts, overdue notices lack transparency, as they omit specific charges like collateral sell-off charges and fail to disclose the exact amounts for penal and dishonour charges.
- RBI guidelines require explicit disclosure of all applicable charges and reasons in all such communications.
- This gap creates a risk of non-compliance with RBI transparency and disclosure norms

**Solution:**
?

**In scope:**
- Migrating the existing communication events to the newly drafted SMS templates.
- Dynamo DB logging at a per-record level for all outcomes (success, failure) to maintain a compliance audit trail.

---

## #33 — Term Loan LOS requirements
**Status:** In progress | **Last edited:** May 14, 2026 10:50 AM

**Problem:**
are we solving?**

- **Low awareness of line-based lending products:** Most Indian consumers do not understand the concept of a reusable credit line or overdraft (OD)-style borrowing.
- **Poor use of the product as a one-time loan:** Even when users opt in, they typically draw down only once and never return, leading to poor utilization of the approved credit limit.
- **Lack of lifecycle borrowing behavior:** Users do not engage in multiple drawdowns or reborrowing after repayment, resulting in limited customer lifetime value (LTV).
- **Ineffective product positioning:** The existing product f

**Solution:**
?**

Product Overview

We propose a **term-loan-style wrapper** on top of the line construct to match user expectations and drive better usage. The solution involves:

- **Offering a familiar term-loan onboarding flow** for the first drawdown.
- **Enabling multiple drawdowns** from the same line, with flexibility in amount and tenure.
- **Allowing re-borrowing** once limits are replenished through repayment.
- **Positioning the product clearly as “term loans with flexibility”**

This hybrid approach is designed to increase adoption, improve credit line utilization, and grow customer LTV.

**Product Technical Construct**

A **line-backed, multi-drawdown term loan**, where:

- **Both loan and tranche constructs are exposed to the LSP**.
- DSP manages the **loan** as the credit container; **e

---

## #34 — DSP PhonePe PG Integration for PhonePe
**Status:** In progress | **Last edited:** March 8, 2025 1:25 PM

**Problem:**
are we solving?**

- Recording PG repayments from PhonePe offline will take considerable time and effort for our operations team
- Reconciling PG repayments from PhonePe will take time and will impact the SLAs from a customer experience perspective
- Delay in posting transactions will impact our accounting and result in backdated transactions, opening up a backdoor for a lot of issues

---

**Solution:**
?**

DSP will expose an API to accept payments through PG on PhonePe UI.

---

---

## #35 — [Platform] Unpledging of unlinked funds bulk appro
**Status:** Pending Review | **Last edited:** March 5, 2025 10:35 AM

**Problem:**
are we solving?**

There can arise scenarios where the user pledges securities with the NBFC and changes their mind and does not end up taking a loan with the NBFC. 

As per an RBI regulation, the REs are supposed to release all the original movable / immovable property documents and remove charges registered with any registry within a period of 30 days after full repayment/ settlement of the loan account. ([Link](https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=12535&utm_source=chatgpt.com))

While the regulation does not explicitly mention the scenario where the loan is not tak

**Solution:**
?**

We will be making a bulk operations maker, which will allow the NBFC operations agent to upload a file (at a security / ISIN / Lien reference number level). 

Bulk (file based) checker task for validation of the bulk unpledging file by the operations team (Manual verification of the initially lodged file)

NBFC currently supports unpledging requests only at a loan account level, a loan account is created only when the origination process (loan application) is completed by the user. We will be creating an opportunity level unpledging workflow (using step functions) to support the complete unpledging process.

Each bulk maker job (like bulk lodgement) will create independent unpledging requests at an opportunity level, these independent requests will be present in the applications secti

---

## #36 — Credit Bureau Reporting Comms
**Status:** Pending Review | **Last edited:** March 19, 2026 11:57 AM

**Problem:**
are we solving?

- DSP Finance is required by RBI regulations to report borrowers with outstanding interest dues to credit bureaus.
- Currently, **no communication is sent to borrowers at the time of reporting** — creating a regulatory compliance gap and leaving borrowers unaware of adverse credit events being filed against them.

- As reporting frequency increases from **2x/month (15th, EOM) to 4x/month (9th, 16th, 23rd, EOM) from July 1, 2026**, the gap scales without an automated solution in place.

---

**Solution:**
?

---

## #37 — Improving Mandate Conversions
**Status:** In progress | **Last edited:** March 17, 2026 4:46 PM

**Problem:**
are we solving?

- **Drop offs** in API-based eNACH mandates (due to vendor, bank or customer issues).
- **Drop-offs during Digio SDK invocation** due to performance/UI issues or trust gap.
- **Lack of modern mandate options** like UPI Autopay, which offers faster setup and better UX.
- **Inflexibility in fallback options**, e.g., esign/physical not clearly surfaced or too complex.
- **No recovery mechanisms**: Failed mandates are not followed up with retries, reminders, or alternate suggestion
- Problem identification
    - Digio SDK does not get invoked when the user chooses to set up autopa

**Solution:**
?

---

## #38 — Product note Co-lending foreclosure - Deprecated -
**Status:** In progress | **Last edited:** March 15, 2026 8:49 PM

**In scope:**
- Designing a **safe and consistent foreclosure experience** for co-lended LAMF loans
- Ensuring customers interact with **only one loan experience**, despite multiple lender loans
- Enabling DSP to **orchestrate foreclosure end-to-end** while respecting lender-level closures
- Validations and error handling
- CC Maker checker for foreclosure processing
- Foreclosure repayment settlement(handling 

# Product note: Co-lending foreclosure - Deprecated - ignore ## **Background and Context** - **Who is facing the problem** - Customers foreclosing co-lended loan. - DSP Operations, Vol and DSP Support, Tech Ops teams handling servicing - TCL NBFC operations and finance teams managing their loan books - **What is the challenge / what is broken today** - In a co-lending setup, a single customer loan is split across **two NBFCs (DSP 10%, TCL 90%)** - Customers expect a **single foreclosure action**, while lenders require **independent loan closure and settlement** - Without a clearly designed orchestration: - Foreclosures risk becoming partially completed - Example: Foreclosure can partially succeed—closing one lender’s loan while the other remains open—and if collateral is released at that point, one lender is left with an unsecured loan, which is a major regulatory risk. - Ops teams face manual reconciliation and escalations - **Why is it important / what is impacted** - Foreclosure is a **high-trust moment** in secured lending - Any error directly impacts: - Customer trust and NPS - Regulatory compliance around pledge release - DSP’s credibility as the servicing NBFC - As co-lending is a **new product vertical**, getting this wrong early creates long-term operational debt. --- ## **1. Problem scope** ### In scope - Designing a **safe and consistent foreclosure experience** for co-lended LAMF loans - Ensuring customers interact with **only one loan experience**, despite multiple lender loans - Enabling DSP to **orchestrate foreclosure end-to-end** while respecting lender-level closures - Validations and error handling - CC Maker checker for foreclosure processing - Foreclosure repayment settlement(handling of accrued amount and excess management) and accounting **Primary users** - Retail customers foreclosing co-lended loans **Secondary users** - DSP operations and DSP Finance team - Volt sales and support teams - Volt Tech Ops - TCL NBFC Ops & Finance teams ### Out of scope - Payouts --- ## **2. Success Criteria** - ### Primary outcomes - Customers can foreclose co-lended loans through **one clear and predictable flow** - Repayments are getting posted without and disputes, All three loans are getting closed, collaterals are getting released and NOC is provided to the users. - Minimal manual intervention for standard foreclosure cases ### Key success metrics - Foreclosure completion success rate ≥ **99%** - Average foreclosure TAT ≤ **1 business day** - Ops/manual intervention rate ≤ **5% of cases** ### Post-launch good state - Foreclosure journey live and

---

## #39 — Virtual Accounts for LSPs
**Status:** Pending Review | **Last edited:** June 20, 2025 11:32 AM

**Problem:**
are we solving?**

---

- Currently partner LSPs are looking for an alternate payments methods than the payment like because -
    - They have an existing UI flow ready to support VA accounts (SmallCase)
    - They want to provide a back-up repayment option in case payment link is down

**Solution:**
?**

- DSP will expose APIs that enable each partner LSP to retrieve a virtual account (VA) number uniquely mapped to a customer’s loan account. Instead of embedding the VA generation logic within each LSP’s system, this design centralizes the logic at DSP’s end. As a result, if DSP ever modifies the way VAs are generated—due to regulatory, operational, or technical changes—no updates are required on the LSP side.
- This decouples the VA logic from partner implementations and ensures long-term scalability, consistency, and ease of maintenance across all integrations.
- LSPs will get the status of VA repayment through the repayment order status update web hook

---

## #40 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #41 — UPI Autopay Product note
**Status:** In progress | **Last edited:** July 9, 2025 12:24 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

---

## #42 — Tata Video KYC Integration V0
**Status:** In progress | **Last edited:** July 3, 2025 10:08 AM

**Problem:**
are we solving?**

Tata Capital mandated the VKYC process to be completed for each new customer from 1st April 2025. With larger vision and deeper potential partnerships in the horizon, restarting the business with Tata Capital is required.

To do so, we need to implement Tata  Capital’s VKYC in our journey flow.

---

**Solution:**
?**

Implementation of VKYC will cause significant rise in the drop-offs. With alignment from Tata, we can open the account without the customer completing the VKYC but it is mandatory for the customer to complete VKYC before raising a disbursement request.

For the initial launch (and till we observe stabilized funnels) we would be involving our Support team to help customers before and after (in cases of rejection/incomplete VKYC) with clear instructions and hand holding.

This is for the V0 launch only.

 

Note:

Tata’s Business Hour: 9AM - 6pm

[Activation: LSQ Task Creation](Tata%20Video%20KYC%20Integration%20V0/Activation%20LSQ%20Task%20Creation%20224e8d3af13a80c982dacebab3d9b6b0.md)

---

## #43 — Razorpay PG SDK integration DSP (1)
**Status:** Ready for Tech | **Last edited:** July 29, 2025 2:16 PM

**Problem:**
are we solving?**

As an LSP we have integrated with lender repayments flow via web integrations where the repayment pages are loaded as screens (web-view) and open the URLs in the web-view (Android and iOS) or as tabs replacing Volt’s URL (Web). 

In parallel, we rely on backend for the status of the user sessions via deep checks. This process is not optimal and often causes the following issues:

1. Blank screen opens (link comes from backend via lenders) 
2. Delayed status (backend is dependent on lender for status, client application gets status from backend)
3. Web hook drops - Amount get

**Solution:**
?**

We will be integrating React Native SDK for Android and iOS to improve user experience while they make repayments as a client side integration with Volt.

**Documentation:**

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/) (Android)

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/) (iOS)

---

## #44 — Razorpay PG SDK integration DSP
**Status:** Ready for Tech | **Last edited:** July 29, 2025 2:15 PM

**Problem:**
are we solving?**

As an LSP we have integrated with lender repayments flow via web integrations where the repayment pages are loaded as screens (web-view) and open the URLs in the web-view (Android and iOS) or as tabs replacing Volt’s URL (Web). 

In parallel, we rely on backend for the status of the user sessions via deep checks. This process is not optimal and often causes the following issues:

1. Blank screen opens (link comes from backend via lenders) 
2. Delayed status (backend is dependent on lender for status, client application gets status from backend)
3. Web hook drops - Amount get

**Solution:**
?**

We will be integrating React Native SDK for Android and iOS to improve user experience while they make repayments as a client side integration with Volt.

**Documentation:**

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/) (Android)

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/) (iOS)

---

## #45 — Repayment Lifecycle Tracking
**Status:** Not started | **Last edited:** July 22, 2024 10:29 AM

**Problem:**
are we solving?

- Users currently are not able to see the status of their transactions once a repayment is done till it is settled by the lender in their statement of accounts.
    - Users are not able to see the updated credit limit and the transaction and want to know the status of the transaction.
        - Payment takes 1-2 days to get updated in the loan account (Then it gets visible to the user)
    - This makes them follow up with our Ops/Support teams via support channels to confirm if their payment was received by us.
    - This consumes a lot of time for the support team and is crea

**Solution:**
?

We are solving this problem for the user by the following ways:

- Add a pending transaction in transactions section with status in progress till the time it is settled by the lender (transactions section - ledger)
    - [**Transaction status management**](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
- On payment success screen in the flexi pay screen, communicate to the user the steps and timeline for the settlement with the lender.
    - [UI and cases that need to be handled](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
    - [Accounting and Settlement](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
- Actively sharing the status of the transaction made by the user (Transaction Success/ Transaction settled) 

---

## #46 — Implementing UTR dedupe for repayment postings
**Status:** Pending Review | **Last edited:** July 14, 2025 3:52 PM

**Problem:**
are we solving?**

---

- We currently do not perform a deduplication (dedupe) check on incoming repayment requests from Lending Service Providers (LSPs), which poses a risk of **duplicate repayment postings**. This issue becomes critical as we scale with more LSPs like PayTM and PhonePe initiating repayments through their own Payment Gateways (PGs).
- Additional complexity arises because **UTR (Unique Transaction Reference) numbers are only unique at the bank level**, not globally. Hence, simply using UTR for deduplication is not sufficient and can lead to false positives or missed duplicates

**Solution:**
?**

---

## #47 — [Platform] BRE configurations for approval tasks
**Status:** Done | **Last edited:** January 9, 2025 10:54 PM

**Problem:**
are we solving?**

Requests raised by the users in relation to their loan account and application journey go through STP and non STP flow. Non STP transactions go through an approval mechanism on the command centre.

As we continue to launch the DSP platform across channels, we will require platform and request level checks and rule engines to control approval mechanisms and handle teething phases for launch across channels.

---

**Solution:**
?**

Partner and channel level BRE configurations:
We will be building partner and channel level BRE capabilities to define STP and non STP rule engine which will govern the approval of a task.

<aside>
💡

For example: We may approve STP lodgements for Volt while keeping it an approval flow for a new partner like Groww or IndMoney

</aside>

Request level BRE configurations:

We will be building request level rules which will govern if the said request will be going through an STP flow or a non STP flow (checker approval).

Each rule can have a threshold value which can be different at a request/channel level.

<aside>
💡

For example: We have a rule to auto approve lodgement requests with a limit under 10 lakh for Volt and 2 lakhs for Groww

While the parameter here is credit limit, it can

---

## #48 — Product note LMS integration with Tally
**Status:** Ready for Tech | **Last edited:** January 8, 2026 9:27 AM

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users
- **Manual ERP Posting Dependency**:
    
    Accounting entries are generated in Finflux (LMS) but are **manually transformed and uploaded into Tally**, creating operational dependency on the Finance team.
    
- **High Risk of Errors and Duplicates**:
    
    Manual handlin

# Product note: LMS integration with Tally ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? Most businesses record transactions across multiple ledgers to accurately classify income, expenses, assets, and liabilities arising from each business event such as product sales, and discounts. For us as an NBFC, core business transactions include interest posting, charge application, payouts against sanctioned limits, and customer repayments. Given the regulated nature of lending, NBFC accounting processes are subject to direct regulatory scrutiny by the RBI. It is therefore critical that accounting is accurate, automated, system-driven, and free from manual intervention. Currently, accounting entries are generated in the LMS and then manually transformed and posted into the ERP. This manual handoff introduces operational and control risks. This gap was highlighted as a key vulnerability in our statutory audit and must be addressed as a priority. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users - **Manual ERP Posting Dependency**: Accounting entries are generated in Finflux (LMS) but are **manually transformed and uploaded into Tally**, creating operational dependency on the Finance team. - **High Risk of Errors and Duplicates**: Manual handling increases the risk of: - Duplicate ledger postings - Incorrect ledger mapping - Debit / credit sign errors - Partial or missed uploads **Lack of Idempotency & Control**: There is currently: - No system enforced idempotency for ERP postings - No way to prevent re-posting of the same transaction - Limited ability to trace an LMS transaction to a Tally voucher **Delayed and Unpredictable TAT**: Posting timelines depend on: - Manual availability of the Finance team - Ad-hoc batch preparation and uploads This leads to **inconsistent turnaround times** **Access control**: Current workflows do not consistently enforce: - System-driven approvals - Clear separation between generation, validation, and posting of accounting entries. ### Out of scope - - Call out on items out of scope - Rationale for exclusion - Manual Reconciliation: Reconciliation between LMS (Finflux) and ERP (Tally) is currently manual and time-intensive, requiring cross-system data pulls and comparisons. This will be picked as an enhancement once the current release is stabilised. ETA to be confirmed - Delayed

---

## #49 — [NBFC] DSP Finance Website (Aug25)
**Status:** In progress | **Last edited:** January 7, 2026 6:34 PM

**Problem:**
are we solving?**

DSP Fin website currently meets the basic expectations in terms of content and regulatory requirements. That said, it still doesn’t measure upto competitor websites like BFL, TCL or NBFC websites like Navi, CRED, Piramal, etc. 

Now that we need to do a PR and work with external partners (Banks, rating agencies, etc), we need to polish up the website to ensure it conveys trust and confidence.

The new version would also have a basic customer servicing activities like ability to request for a SOA, disbursement or even do repayment.

---

**Solution:**
?**

---

## #50 — Testing DSP Comms
**Status:** Pending Review | **Last edited:** January 7, 2025 10:11 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #51 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #52 — Axis bank e-collect API integration for virtual ac
**Status:** Done | **Last edited:** January 5, 2025 1:42 PM

**Problem:**
are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

Problems are divided between two key stakeholders:

- NBFC (operations/business/product)
- Customers

NBFC 

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted (Reconciliation also becomes very tough as

**Solution:**
?**

DSP will be integrating with Axis bank ([refer this for benchmarking exercise](NBFC%20Virtual%20Accounts%20for%20Repayments%20(Alignment)%2034ec85249bc046dba5145ac1ea16858d.md)) e-collect APIs to create, validate and accept VA payments from customer.

Steps for accepting a VA payment:

- NBFC gets a e-collect code
- NBFC appends a unique reference number (for each loan) and shares the virtual account with the customer (total length has to be less than or equal to 28 characters where first 6 characters would be the e-collect code).
    - To make the bank account more readable, we can optimise the account number 
    
    Benchmarking: (Two possible ways alphanumeric and numeric)
        - Account number: VCKYCDSPFINA8072 (CKYC)
        IFSC code: IBKL0000011
        - Account number: 2

---

## #53 — [Platform] Mandate collection BRE optimisation
**Status:** Done | **Last edited:** January 30, 2025 5:01 PM

**Problem:**
are we solving?**

There are multiple ways through which an NBFC can collect dues from customers:

- Accepting direct user initiated payments (VA/PG)
- Collecting payments via debiting user’s bank accounts (mandate)
- Invoking securities to clear dues (Sell off)

All repayment methods have different use cases and scenarios in which they are triggered. Mandate collection repayments are done for the following use case:

- User convenience and financial health: Amount is automatically deducted from the user’s bank account and ensures that their loan account does not become overdue
- NBFC portfoli

**Solution:**
?**

- We will be integrating with the Finflux (LMS) overdue API which gives us due level information:
    - Due type (Interest / Charge / Penal charge / Interest overdue)
    - Due amount
    - Due from
    - Due date
- Based on this information we will run a BRE to select which dues are eligible for collection via mandate from the user:
    - Any due where due date is below the last day of the billing cycle is of the type (interest + charges + penal charges) is eligible for collection.
- We will rename the bounce charges to make them dishounour charges to make it explicit for the user that since their account is in an overdue state, they are being charged an overdue fee.

Charge short name: DC (Deployed in UAT)
- Users will only be charged an dishounour charges if there was an interest o

---

## #54 — B2B Platform Dashboard v1
**Status:** Pending Review | **Last edited:** January 29, 2025 10:56 AM

**Problem:**
are we solving?**

There are around 8 B2B platforms (partners) giving business to Volt. As of now, all of them are being serviced offline by the program team (Keyur) like giving visibility of applications, reports, etc. This results in the below challenges.

- Poor perception of Volt by the partner
- Risk of data being shared outside the required accesses
- Possible chance of incorrect data being shared
- Considerable man-hours spent in generating and managing reports
- Partners’ operations/business teams can’t self-service themselves
- Enterprise partners like TDL expect a complete dashboard 

**Solution:**
?**

---

## #55 — [Platform LSP] All transactions requirements
**Status:** Done | **Last edited:** January 22, 2025 6:38 PM

**Problem:**
are we solving?**

As a platform we provide multiple APIs so that our consumers in this case:

- Internal operations team
- Loan service providers (Volt / Indmoney / Groww)

Are able to consume and accordingly process the required information in an efficient manner. It is important that we provide the right amount of information for the following reasons:

- Optimise computation and processing of information at the consumer end
- Avoid polling and high frequency calls for information to our system
- Ensuring important information is shared with the consumer (to avoid downstream effects to our 

**Solution:**
?**

We will be building capabilities for LSP/CC to show the following details:

- Withdrawal requests (with status of transactions)
- Repayment requests (with status of transactions)
- Repayment orders (to show failed or pending transaction orders)
- All completed transactions API (Statement API)

| Transaction | Description | Debit/Credit | Transaction initiation source | How will it be consumed via CC/LSP |
| --- | --- | --- | --- | --- |
| Withdrawal | Withdrawals made by the user | Dr | User | Withdrawal requests + all transactions |
| Repayment - (PG) | Repayments made by the user  | Cr | User | Repayment requests + all transactions |
| Repayment - (Mandate collections) | Mandate collection made by the NBFC | Cr | NBFC  | All transactions |
| Repayments - (Sell off) | Invocation coll

---

## #56 — [LSP] Total outstanding amount correction and over
**Status:** Not started | **Last edited:** January 21, 2025 7:32 AM

**Problem:**
are we solving?**

For a loan account there are certain particulars that are maintained to understand what is the total due that the user has against their loan account. They are described as follows:

- Principal outstanding: This is sum of the amount that the user has withdrawn minus the repaid (as partial principal repayments) to the NBFC
- Interest due - This is the amount that is due for the user from the previous billing cycle, calculated as accruals based on their principal outstanding at a daily level (currently we follow a daily accrual model)
- Charges due - This is the sum of all ou

**Solution:**
?**

- We will start passing the overdue amount details to the LSP as well as on the command centre so that it can be shown to the user in an intuitive manner
- We will be updating our revocation request validation to avoid any collateral risk to the NBFC (move from TOS to TOS + Overdue amount)
- We will add additional parameters in the foreclosure API so that the same can be passed to the user at the time of foreclosing the account

---

## #57 — Yes bank e-collect API integration for virtual acc
**Status:** Done | **Last edited:** January 20, 2026 3:53 PM

**Problem:**
are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

Problems are divided between two key stakeholders:

- NBFC (operations/business/product)
- Customers

NBFC 

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted (Reconciliation also becomes very tough as

**Solution:**
?**

DSP will be integrating with Yes bank ([refer this for benchmarking exercise](NBFC%20Virtual%20Accounts%20for%20Repayments%20(Alignment)%2034ec85249bc046dba5145ac1ea16858d.md)) e-collect APIs to create, validate and accept VA payments from customer.

Steps for accepting a VA payment:

- NBFC gets a e-collect code
- NBFC appends a unique reference number (for each loan) and shares the virtual account with the customer (total length has to be less than or equal to 28 characters where first 6 characters would be the e-collect code).
    - To make the bank account more readable, we can optimise the account number 
    
    Benchmarking: (Two possible ways alphanumeric and numeric)
        - Account number: VCKYCDSPFINA8072 (CKYC)
        IFSC code: IBKL0000011
        - Account number: 22

---

## #58 — Repayment next step
**Status:** Not started | **Last edited:** January 17, 2025 12:25 PM

# Repayment next step # Loan Repayment System Redesign ### Current Hypotheses 1. **Hypothesis 1 :** Users expect repayments (interest, shortfall, principal) to be separate since our home screen and other places don’t communicate how they are interconnected. 2. **Hypothesis 2 :** Most of users are familiar with credit card statement model. ## JTBD problem list ### Job Story 1: Clear Shortfall "When I am in shortfall, I want to know exactly how much I need to pay so that I can clear my dues easily and get out of shortfall." **Current Problems:** - The shortfall card only shows the shortfall amount, hiding the fact that users need to pay shortfall + charges + interest - Both TATA & DSP use CIP/ICP apportionment logic which requires clearing all dues, but this isn't communicated upfront - Users encounter unexpected higher payment amounts at the final step, leading to frustration and payment abandonment or doubts ### Job Story 2: Pay Interest "When I need to pay my interest, I want to understand why I need to pay any additional charges" **Current Problems:** - In TATA, users see interest amounts increase in months with additional charges - The system requires users to clear charges before interest due to apportionment logic, but this requirement isn't explained - Users are unable to pay just interest when charges are due, contradicting their mental model of separate payments - These charges and interest come under monthly dues as a concept ### Job Story 3: Make Principal Repayment "When I want to repay my principal amount, I want to know how my payment will be applied so I can make an informed decision." **Current Problems:** - For both TATA & DSP, users with mandates try to repay principal but discover they must first clear out the interest and charges which are scheduled to be cut through mandate. - The principal repayment screen doesn't explain that the payment will first go towards interest and charges - Users learn about payment apportionment only after attempting the transaction, leading to canceled payments and frustrated users. - Users are not aware that principal is being repaid early and isn’t due for 3 years. ### Job Story 4: Understand Payment Structure "When I look at my home screen, I understand the payments are separate since they show up as separate components, But its in reality an interconnected system." **Current Problems:** - The home

---

## #59 — [Final] End use capture of transactions
**Status:** Pending Review | **Last edited:** January 15, 2026 5:13 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

- **Capture end use during each withdrawal**
    - **Pros**: Enables granular tracking of the specific purpose behind each withdrawal, offering clear visibility into usage patterns.
    - **Cons**:
        - Complicates the mapping between repayments and disbursements, especially when multiple withdrawals have different declared purposes.
        - Involves higher development effort, as UI changes (e.g., dropdowns on withdrawal screens) would be required.
- **Incorporate tweaks in the end use declaration within the loan agreement [Prioritised]**
    - **Pros**: Minimal engineering effort, as no changes to withdrawal screens are needed.
    - **Cons**: Limits visibility into actual usage at a transaction level, which may reduce data fidelity for downstream analysis or compliance.

---

## #60 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #61 — [CC] Showcase the reason for freezing on CC
**Status:** Not started | **Last edited:** February 4, 2025 6:15 PM

**Problem:**
are we solving?**

Account freezing or suspension is a temporary restriction that prevents an account holder from accessing specific or all account features. This occurs for several reasons:

- Suspicious activity detection
- Policy violations
- Legal requirements
- Payment issues
- Security concerns

We have the operations team, risk team and the development team who can place an account under suspension or frozen state. 

The frozen state **also** occurs when an active account undergoes foreclosure procedure so as to prevent the user from initiating any debit transactions.

When an account g

**Solution:**
?**

We allow the maker to add a reason to freezing of an account. This reason is taken as a service request and we will be storing this in our database.

When we fetch the reasons for the freezing of an account and showcase it as a separate column on the CC when a specific loan id if fetched.

Categorising the reasons for freezing into 2 major categories:

1. Suspicious Activity
2. Credit Risk includes (these individual options which can be selected):
    1. Invalid collateral addition or valuation
    2. Incorrect Repayment addition
    3. Invalid bank account
3. Foreclosure 

The Maker via the CC can select anyone of the above reasons for freezing (feature to select the reason is already available). The account will be immediately frozen and the reason should be visible to the the opera

---

## #62 — [LSP] Document upload support for maker
**Status:** Done | **Last edited:** February 3, 2025 8:55 AM

**Problem:**
are we solving?**

We have made developed maker tasks which enable the operations team to perform certain actions on to the loan accounts of the user and support them with their needs or solving for operational use cases.

For example:

- Reversing a charge
- Posting a charge
- Reversing a repayment
- Posting a repayment
- Suspending a loan account
- Un suspending a loan account
- Bank account update

However, all operations performed by the operations team, impact the user experience and accordingly should be done carefully, most of these requests have to be either linked to a user request, o

**Solution:**
?**

---

## #63 — [Platform] Handling of below 1 Rs transactions for
**Status:** Done | **Last edited:** February 3, 2025 8:48 AM

**Problem:**
are we solving?**

When a user makes repayment to their loan account for either part payment or foreclosing their account, or initiates a sell off there can arise scenarios where the user’s account goes into excess.
This excess if the account is not under foreclosure, is automatically refunded via a daily CRON job that identifies loan accounts in excess, and initiates a payout of an amount equal to excess to regularise the account.

However there can arise scenarios, where this amount is less than Rs 1, if such an amount is found in excess, the corresponding payout for the account fails, as Ca

**Solution:**
?**

We will be making enhancements in our excess job and foreclosure job to solve this problem:

- Excess job will only have accounts where excess amount will be greater than 1
- If an account has an active foreclosure request, or a pending disbursement, it will not be eligible for an excess refund and will be ignored in the excess refund job
- We will be creating transaction type “excess_adjustment” for excess refund transactions, the same will be passed as a type when doing a excess transaction
- We will be setting up transaction type accounting events for excess refund for two scenarios:
    - Excess refund below 1 Rs (liability transfer)
        - Excess COA (liability): Debit
        Excess refund liability: Credit
    - Excess refund above and equal to 1 Rs
        - Excess COA (lia

---

## #64 — Product note - DRPS
**Status:** In progress | **Last edited:** February 25, 2026 11:01 AM

**In scope:**
**

- Enable users to **download an updated repayment schedule(on 100% loan)** that reflects:
    - Disbursals
    - Part payments (principal / interest / charges)
    - Interest based on actual utilisation
    - Loan meta data [ROI, Credit limit, Sanction limit, Interest due, Charges due, Principal due, LAN]
    - Should reflect any change in ROI during loan tenure
- Ensure schedule is **regenera

# Product note - DRPS ## **Background and Context** - **Who is facing the problem** - End customers using LAMF with multiple/single disbursals and part repayments - Customer support & operations teams - NBFC has to provide DRPS to borrower due to regulatory requirement. - **What is the challenge today** - Repayment schedules are **static** and was generated at the time of Agreement sign - Any transaction post generation (disbursal, part payment, interest payment) makes the schedule **outdated** - Users rely on SOA or support teams to understand: - Updated interest dues - Final maturity amount - Remaining principal and cash flow expectations - **Why this is important** - LAMF is a **dynamic credit line**, not a fixed EMI loan - Mismatch between schedule vs actual dues creates: - User confusion understanding the EMI - A real-time repayment schedule improves **transparency, self-service, and confidence** - **It’s a regulatory requirement to provide dynamic schedule post disbursal and repayment to borrower.** <aside> 💡 **What is Dynamic repayment schedule (DRS/DRPS)** **Dynamic Repayment Schedule (DRS)** is a **continuously recalculated repayment plan** that reflects the **current and actual state of a loan**, instead of a fixed, one-time schedule. Unlike traditional EMI schedules, a DRPS is an **updated document that changes whenever the loan balance is impacted by a transaction**, ensuring alignment with actual utilisation and repayments. *In simple terms:* A Dynamic Repayment Schedule shows **what borrower owe, how it is calculated, and how it changes** — based on everything that has *actually happened* on **borrowers** loan till now. </aside> --- ## **1. Problem Scope** ### **In scope** - Enable users to **download an updated repayment schedule(on 100% loan)** that reflects: - Disbursals - Part payments (principal / interest / charges) - Interest based on actual utilisation - Loan meta data [ROI, Credit limit, Sanction limit, Interest due, Charges due, Principal due, LAN] - Should reflect any change in ROI during loan tenure - Ensure schedule is **regenerated dynamically** after every transaction - Provide a **single source of truth** aligned with system calculations - **Data type:** JSON and PDF - API to generate the DRP [Download feature to enable at LSP end] **Primary users** - LSPs → LAMF customers **Secondary users** - Customer support teams - Relationship managers / partners - Internal ops and reconciliation teams ### **Out of scope** - Real-time in-app visualisation (non-download view) *Rationale: Phase-1 focuses on downloadable schedule* - Manual override or

---

## #65 — Customer Lifecycle Tracking - Lien Unmarking → Rep
**Status:** In progress | **Last edited:** February 24, 2024 2:31 PM

**Problem:**
are we solving?**

- 

---

**Solution:**
?**

- Actively communicating the stages of the respective request to the user on the app.
    - Using lender APIs to automatically capture status of the user’s request and breaking down the process into steps to reduce operational load as well as aligning the user on the development of their request.
- Making the request in progress banner less apparent in the user journey to avoid creating artificial urgency in the mid of the user. (Lien removal)
- End state for foreclosure requests when loan is closed (application closed → user should be able to initiate a new journey)

---

## #66 — Shortfall communication enhancement Ignoring accou
**Status:** Pending Review | **Last edited:** February 23, 2025 8:17 PM

**Problem:**
are we solving?**

A sell off is the process of invocation of a lien on a user’s security. That is when the lender or the pledgee, invokes their right to redeem the units of a security pledged by the user with the lender.

There are two types of sell off:

- Lender initiated sell off
    - Lender initiates sell off of securities to recover outstanding amount (30 DPD)
    - Lender initiates sell of to regularise the user’s loan account (shortfall)
- User requested sell off
    - User requests a sell off due to inability to fulfil their commitments towards the credit line

Lifecycle of a sell of

**Solution:**
?**

We will be ignoring accounts under shortfall under the following condition:

V1: If an account has a non terminal collateral sell off transaction (hit collateral transactions API)

V2: If an account has an active sell off follow the following condition:

If Sum of all sale value of all collaterals ((Units blocked for sell off)*NAV(for corresponding ISIN at the time of raising sell off)) < Regulatory shortfall then include in the shortfall communication else ignore

---

## #67 — Check eligibility overhaul
**Status:** Not started | **Last edited:** February 22, 2024 8:34 AM

**Problem:**
are we solving?**

In context of Check limit page we are solving the following problems

1. UI/UX Problems: 
    1. CTA copy signifies that this is an eligibility test which means not everyone is eligible for loan. 
    2. The main headline occupies too much space. Pushes the form down and deviates user attention from the form. The current headline conveys very little. 
    3. Too much space on the main scroll is left unused. Nothing except the form and headline is visible in the first fold. Pushes trust markers and education content down. 
    4. CTAs that are of now use to user at this stage

**Solution:**
?**

---

## #68 — Verify interest and charges revamp
**Status:** Not started | **Last edited:** February 21, 2025 12:28 PM

**Problem:**
are we solving?**

1. One day conversion rate of Verify interest and charges page is ~46%
2. Most users are dropping off this screen because of the following problems:
    1. Users think that this is the last page of the application.
        1. “Mutual fund lock ho jayega”
        2. “Loan ho jayega agar aagay jayegay”
    2. Benefits are not properly communicated. key benefits such as
        1. One time processing fee
        2. OD
        3. Interest only EMI
        4. Unlimited withdrawals and repayments are not shown to the user
    3. User thinks that the “Pledge Funds” value is too hig

**Solution:**
?**

---

## #69 — Line enhancement Loan renewal BRE
**Status:** Not started | **Last edited:** February 19, 2026 7:15 PM

**Problem:**
are we solving?**

1. Line enhancement and loan renewal fees BRE changes
2. Fee and charges verification for fresh application, line enhancement and loan renewal for both lender

**Solution:**
?**

---

## #70 — Bajaj PG
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- We need to integrate the **BAJAJ Payment Gateway** to streamline the collection of principal and interest repayments.
- Currently, with our **CC Avenue integration for BAJAJ repayment collection**, the repayment accounting process is manual, causing delays in reflecting repayments in the Statement of Account (SOA).
- By integrating the **BAJAJ Payment Gateway**, the repayment accounting process will be automated and realtime, similar to how it functions with the **TATA Payment Gateway**.

---

**Solution:**
?**

---

## #71 — Foreclosure payment handling (EOD) repayment in fo
**Status:** Done | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

BAJAJ:

- When user foreclose the loan on Volt UI after 6 PM, we do not consider interest of same days in Net dues payable.
- This led the foreclosure rejection from the lender end.

TATA:

- We do not ask user to pay accrue penal charges and due to this foreclosure are getting rejected.

---

**Solution:**
?**

---

## #72 — Interest, shortfall, renewal table on partner dash
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- MFDs lack visibility regarding their customers' interest details, shortfall occurrences, and loan status.
    - MFDs inquire about the interest status, mandate status and interest calculation.
    - MFDs do not inform their customers about the shortfall, resulting in escalation from the customer's end.
- B2B2C customers depend on advisors to oversee their loan accounts, resulting in reduced attention to direct reminders sent by Volt.

---

**Solution:**
?**

---

## #73 — Annual Maintenance Charges (AMC)
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**DSP offers a credit line facility to users for a tenure of 3 years.** Maintaining this credit line involves ongoing costs including customer servicing, technology infrastructure, portfolio monitoring, and operational overheads.

To ensure the long-term sustainability of the offering and continue delivering high-quality service, **we propose introducing an Annual Maintenance Charge (AMC)**. This will serve as a recurring revenue stream to offset the costs associated with account maintenance and user support throughout the lifecycle of the credit line.

---

**Solution:**
?**

We will be applying AMC on the user’s loan account. AMC will be applied at the end of every year(should be calculated based on account opening date). The same will be added in the product construct.

AMC is Non-contingent charge: will be charged unconditionally whether there is 100%  utilization also.

---

## #74 — Capture foreclosure reasons from customer
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We experiencing an increasing trend in loan foreclosures, which negatively impacts AUM and retention. 

Here are the reason for foreclosure we have identified so far based on the user calling and collecting the feedback from the sales and support team:

**PRODUCT POSITIONING e(Priority 0)**

- We position ourselves as a **short term requirement**, so when the user's requirement is fulfilled the user looks to close the loan.

**LIEN REMOVAL CONFUSION (Priority 0)**

- Users don't understand how to release their collateral and hence assume that account closure is the only way 

**Solution:**
?**

- **Product Education Through FAQs - Phase 2**
    - Create categorized FAQs to address basic product queries and prevent foreclosures caused by product understanding gaps
    - Resources:
        - FAQ Management System: [[Link](FAQ%20Management%20System%20189e8d3af13a8003a2a5ff6abd88b33f.md)]
        - FAQ Content Document: [[Link](https://docs.google.com/document/d/1ojvtyjkUJdytxImRudTC5hqS6BpokB3HF8LjXxxa1W0/edit?usp=sharing)]
- **Targeted Intervention for Foreclosure Requests - Phase 1**
    - Collect specific reasons for foreclosure request
    - Present contextual benefits and alternatives based on selected reasons
    - Guide users to better solutions than foreclosure
- **Operations Team Review Process - Phase 1**
    
    A. Initial Review
    
    - Operations/Customer Succe

---

## #75 — Charges only handling for collection - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

**Solution:**
?**

---

## #76 — Comms config
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Comms config Customer loan renewals ```json { "LOAN_RENEWAL_REMINDER_1ST": { "eventInFiltering": { "customerChannel": [ "B2C", "B2B", "B2B2C" ], "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "loan_renewal_1st_day_of_month_v1", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "loan_renewal_1st_day_of_month_v1" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "loan_renewal_1st_day_of_month_v1" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "contactnumber" ] }, "MAIL": { "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_2ND": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "15th_day_of_loan_expiry_v1", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "15th_day_of_loan_expiry_v1" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "15th_day_of_loan_expiry_v1" }, ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "contactnumber" ] }, "MAIL": { "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_LAST_WEEK_DUE": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "20days_to_last_day_amount_due", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "20days_to_last_day_amount_due" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "20days_to_last_day_amount_due" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "outstanding_amount", "contactnumber" ] }, "MAIL": { "templateId": "d-78f7acdde85248798dfda7f480312e31", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP",

---

## #77 — Foreclosure and lien removal request validation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

**Solution:**
?**

---

## #78 — Foreclosure repayment - Handle PenalInterestAccrue
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- In foreclosure request we have not handled the “PenalInterestAccruedNotDue” field in the calculation of net payable amount which is leading to the rejection of foreclosure request.

---

**Solution:**
?**

- Include the "PenalInterestAccruedNotDue" field in the calculation of the net payable.
- Display the "PenalInterestAccruedNotDue" amount on the UI.
    - The backend (BE) needs to send this field with its value to the frontend (FE), so the FE can display it on the UI and use it to calculate the amount shown to the user.
    - Outstanding interest amount should include the value of “PenalInterestAccruedNotDue”

---

## #79 — Handle excess amount in foreclosure request [TCL]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- There are no handling of excess amount for TATA customer in foreclosure flow

---

**Solution:**
?**

- When user loan account are in excess and user want to foreclose the loan then we should initiate the withdrawal for the amount equal to excess amount and once withdrawal is success then initiate the foreclosure request.
- How to identify if user account are in excess:
    - In the foreclosure details, If netPayable are in Negative then we can say that user loan account has a excess amount.
    - If NetPayable are Positive then user has to repay the amount and if NetPayable amount is in Negative then we need to raise the withdrawal amount equal to the NetPayable amount.
- Prerequisite: Need to handle “PenalInterestAccruedNotDue”
    - PRD link: [https://www.notion.so/volt-money/Foreclosure-repayment-Handle-PenalInterestAccruedNotDue-10ae8d3af13a8023b658d2852b6477f4?pvs=4](https://www

---

## #80 — Interest feature handling for TCL
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

TCL has changed the interest posting date from 1st of every month to 3rd of every month and currently interest lifecycle is handled based on 1st a posting date.

Now since TCL will post the interest on 3rd, any interest repayment made during 1st to 3rd(till interest is not posted) will get settled as Overdue interest → Overdue charges → Principal. 

---

**Solution:**
?**

1. Create interest in Volt system using admin action by upload the interest + charges due sheet manually.
2. Do not allow user to repay the interest on and before 3rd of the month via APP.
3. Do not nudge users to pay the interest amount in comms content when interest is due.
4. Payment summary page to be updates for TCL customers
    1. If users are repaying the amount b/w 1st to 3rd the settlement logic shown on the UI needs to be updated accordingly.
5. Lien removal and foreclosure Sanity needs to be done

---

## #81 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #82 — Maker checker for servicing comms
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our servicing communications system has critical reliability issues, resulting in both inaccurate content delivery and inconsistent communication delivery to customers. This impacts our service quality and customer experience.

**Solution:**
?**

---

## #83 — Multiple mandate presentation [DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**Solution:**
?**

DSP will **initiate a second mandate presentation on 20th of every month** for accounts with overdue interest and charges, targeting recovery from customers who failed the first attempt and not paid overdue amount till [presentation date - file approval date]

---

## #84 — Partner MFD Dashboard PRD (LAS Servicing)
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt currently provides a **LAMF Servicing Dashboard** for partners (MFDs) to view and manage completed loan applications.

With the launch of **LAS (Loan Against Shares)**, we need to **extend the Partner Dashboard** to:

- Support **LAS servicing & monitoring**
- Provide **cross-product visibility** (LAMF + LAS)
- Maintain consistency, data integrity, and usability across both products

**Solution:**
?**

Volt will **extend its existing Partner (MFD) Dashboard** to support **LAS (Loan Against Shares)** servicing with:

- **Full cross-product visibility** across **LAMF and LAS**
- Ability for partners to **manage LAS loan accounts on behalf of customers**
- Enable **servicing communication** for LAS

This extension ensures that MFDs can seamlessly service both **LAMF and LAS portfolios** through a **single, unified platform**, driving operational efficiency, improved customer experience, and higher LAS adoption.

---

## #85 — Project Elevate - LMS
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

BFL has restricted our customer to increase the credit limit.

---

**Solution:**
?**

Implement a system that enables customers to create additional loan accounts with DSP when they need higher credit limits, while providing a seamless experience to manage multiple credit lines within our platform.

Same solution should work to migrate TCL customer

---

## #86 — Repayment flow optimisation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

---

- When users repay amounts through the FlexiPay flow, the repayment is allocated towards charges (when due) and interest repayment (when due) for TCL and DSP customers. However, users are not explicitly informed about how their repayment is distributed across charges, interest, and principal, leading to confusion after payment completion.
    - The interest amount and status are not updated if the repayment is made through the FlexiPay flow.
    - Users are not informed that auto-debit will still be executed if repayment is made between the 1st of the month and the due 

**Solution:**
?**

---

## #87 — Rounding of Accrued Interest before Posting bill a
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**In scope:**
**

- Rounding logic implementation before **posting accrued interest** on billing date.
- Update interest posting jobs to use the rounded value.
- Update ledger to reflect the rounded amount.
- Audit log and internal reporting to capture both actual accrued and posted amount for reconciliation.
- Penal should only apply on overdue interest amount >100

---

## #88 — SYNC shortfall status with Principal & shortfall r
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our current shortfall management process is manual and inefficient:

1. We rely on lender-provided spreadsheets for shortfall data
2. Updates are made only once daily through the admin tool by the ops team
3. The app continues showing shortfall notifications even after customers have repaid, leading to:
    - Poor user experience
    - Increased customer complaints
    - Unnecessary escalations

---

**Solution:**
?**

---

## #89 — Setup new and fix existing MIS for lender BFL and
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Setup new and fix existing MIS for lender BFL and TCL

---

**Solution:**
?**

---

## #90 — Shortfall experience optimisation
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- When users experience a shortfall and fail to meet it on time, lenders sell the funds on the 7th day by 12 PM. However, our app UI and communications indicate that users have 7 days to meet the shortfall.

---

**Solution:**
?**

- We need to ask user to meet short-fall within 6 days instead of 7 days
- Portfolio will be sold-off on 7th day
- Repayment of shortfall has to be done on or before 6th days before 6 PM

---

## #91 — Show interest virtual bank account to BFL customer
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Customers are using the Principal Virtual Account displayed on the Volt app for BFL customers to make their interest repayments.
- Since customers are unaware that the displayed bank account is for principal repayments only, they are mistakenly making interest payments, assuming it will cover the interest balance.
- As a result, these repayments are being allocated against the principal, leaving the interest overdue, which leads to sell-offs and customer escalations.

---

**Solution:**
?**

---

## #92 — TCL Dynamic repayment schedule
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

To meet compliance requirements, we need to introduce a new functionality that enables TCL customers to download their repayment schedule directly from the app.

---

**Solution:**
?**

We will implement a dynamic repayment schedule generation and download feature that integrates with TCL's API to provide customers with up-to-date repayment schedules.

**Implementation Strategy:**

- **Phase 1**: Direct UI download with real-time API integration
- **Phase 2**: Email delivery option based on API performance analysis

---

## #93 — TCL foreclosure API integration
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We are currently using the `getSummary` API to fetch foreclosure details for TCL loans. However, this approach is resulting in multiple issues that are affecting both user experience and operational efficiency.

**Solution:**
?**

<aside>
💡

The scope of this PRD is to first solve the foreclosure flow and then address the loan expiry experience.

Phase 2 will be picked up separately 

</aside>

To address the limitations of the current `getSummary` API, the following solutions have been implemented by TCL:

1. **Dedicated Foreclosure API**
    - TCL has developed a **new Foreclosure API** specifically to fetch foreclosure-related details.
    - This API will returns only the necessary data which are required to raise the foreclosure.
    - This API will also work for Expired loans.
2. **Enhancement to Receipt Posting**
    - Changes have been made to the **Receipt Post API** to allow manually posting of payments which **are not yet due**.
3. **Accurate Net Payable Calculation**
    - Once the not-due amount is 

---

## #94 — Untitled
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Untitled ```mermaid flowchart TD A[User Login] --> B{Account Status Check} B --> C[Only LAS Account] B --> D[Only LAMF Account] B --> E[Both Accounts] B --> F[No Accounts] %% Only LAS Flow C --> C1[LAS Dashboard] C1 --> C2{User Action} C2 --> C3[View Account Details] C2 --> C4[Make Repayment] C2 --> C5[Top Up Collateral] C2 --> C6[Apply for LAMF] C2 --> C7[View Statements] C6 --> G[LAMF Application Flow] G --> G1[Document Upload] G1 --> G2[Verification] G2 --> G3[Approval/Rejection] G3 --> |Approved| H[Dual Account User] G3 --> |Rejected| C1 %% Only LAMF Flow D --> D1[LAMF Dashboard] D1 --> D2{User Action} D2 --> D3[View Account Details] D2 --> D4[Make EMI Payment] D2 --> D5[Top Up Collateral] D2 --> D6[Apply for LAS] D2 --> D7[View Statements] D6 --> I[LAS Application Flow] I --> I1[Collateral Setup] I1 --> I2[Verification] I2 --> I3[Approval/Rejection] I3 --> |Approved| H I3 --> |Rejected| D1 %% Both Accounts Flow E --> H[Unified Dashboard] H --> H1{Account Selection} H1 --> H2[LAS View] H1 --> H3[LAMF View] H1 --> H4[Combined View] H2 --> H5{LAS Actions} H5 --> H6[LAS Account Details] H5 --> H7[LAS Repayment] H5 --> H8[LAS Top Up] H5 --> H9[Switch to LAMF] H3 --> H10{LAMF Actions} H10 --> H11[LAMF Account Details] H10 --> H12[LAMF EMI Payment] H10 --> H13[LAMF Top Up] H10 --> H14[Switch to LAS] H4 --> H15{Combined Actions} H15 --> H16[Cross-Account Summary] H15 --> H17[Unified Repayment] H15 --> H18[Portfolio Analysis] H15 --> H19[Recommendations] %% No Accounts Flow F --> F1[Welcome Screen] F1 --> F2{Product Selection} F2 --> F3[Apply for LAS] F2 --> F4[Apply for LAMF] F2 --> F5[Learn More] F3 --> J[LAS Onboarding] F4 --> K[LAMF Onboarding] %% Common Flows C4 --> L[Repayment Flow] D4 --> L H7 --> L H12 --> L H17 --> M[Multi-Account Repayment] L --> L1[Select Amount] L1 --> L2[Choose Payment Method] L2 --> L3[Confirm Payment] L3 --> L4[Payment Processing] L4 --> L5{Payment Result} L5 --> |Success| L6[Success Screen] L5 --> |Failed| L7[Error Handling] M --> M1[Allocate Amount] M1 --> M2[Choose Payment Method] M2 --> M3[Confirm Split Payment] M3 --> L4 C5 --> N[Top Up Flow] D5 --> N H8 --> N H13 --> N N --> N1[Select Collateral Type] N1 --> N2[Enter Amount/Quantity] N2 --> N3[Verify Collateral] N3 --> N4[Confirm Top Up] N4 --> N5[Processing] N5 --> N6{Result} N6 --> |Success| N7[Success Screen] N6 --> |Failed| N8[Error Handling] %% Support & Help C1 --> O[Help Center] D1 --> O H

---

## #95 — Volt Apps & Web Multiple Loan Handling - Launching
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

DSP Finance is launching **LAS (Loan Against Shares) for B2B2C customers**. 

To enable customers to seamlessly manage their LAS loan accounts, we need to build a **scalable, modular, and user-friendly loan servicing experience** within the Volt platform.

The servicing module must support:

1. **LAS loan management** — for customers availing loan against shares
2. **LAMF loan management** — for existing customers availing loan against mutual funds
3. **Unified product** — for users holding **both LAS and LAMF**, offering an intuitive, consistent experience across products 


**Solution:**
?**

Volt will provide a **modular loan account management system** that supports:

1. **LAS-only servicing**
2. **LAMF-only servicing**
3. **Hybrid servicing (both LAS + LAMF[Multi-lender])**
    1. Support of multiple loan type(OD, TL) under the umbrella of different product type (LAMF, LAS)
4. **Cohesive communication and notification design for both products**
    1. **Messages are clearly distinguished yet work seamlessly together, preventing confusion for users managing multiple loan products⁠**

---

## #96 — UPI Autopay Evaluation
**Status:** In progress | **Last edited:** February 12, 2025 6:14 PM

# UPI Autopay Evaluation # Overview UPI Autopay is a digital payment solution introduced by NPCI to enable seamless, recurring payments through Unified Payments Interface (UPI). It allows users to set up automatic debits for subscriptions, EMIs, utility bills, insurance, and other recurring expenses without manual intervention. Merchants can integrate UPI Autopay to ensure frictionless collections, improve customer retention, and reduce payment failures. Key evaluation criteria include commercials, performance metrics, ease of integration, reconciliation processes, and support availability. Comparison across providers like PhonePe and Razorpay helps determine the best solution based on reliability, cost, and performance. # PhonePe Evaluation Report [PhonePe UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/PhonePe%20UPI%20Autopay%20Evaluation%20190e8d3af13a80a59b09d18401c8fd89.md) | **Criteria** | **Priority** | **Expectations** | **Comments** | | --- | --- | --- | --- | | Commercials for registration | High | | Need to confirm | | Commercials for presentation | High | | Need to confirm | | Settlement timelines | High | T+0 / T+1 | Needs confirmation | | Registration API performance | High | 95p TAT < 100ms | Not explicitly stated in docs, need benchmarks | | Pre-debit API performance | High | 95p TAT < 100ms | Needs performance validation | | Presentation API performance | High | 95p TAT < 100ms | Needs performance validation | | Ease of integration | High | Yes (2 weeks - 2 devs) | APIs are well-defined, should be achievable | | Post-integration support | High | PhonePe support required | Need clarity on support SLAs | | SDKs available | High | Java, Python | APIs are also available | | Registration modes | High | - Intent - QR - Collect | Intent and Collect supported, QR we need to convert | | Debit & Pre-debit orchestration | High | Managed by PhonePe & Merchant can also handle | APIs allow merchant to trigger debit | | Registration Error Codes | High | Not provided in documentation | Need list from PhonePe | | Pre-debit Error Codes | High | Not provided in documentation | Need list from PhonePe | | Presentation Error Codes | High | Not provided in documentation | Need list from PhonePe | | Transaction reconciliation | High | MIS reports for presentation | | | Settlement reconciliation | High | MIS reports for settlement | | | Registration reconciliation | High | MIS reports for registration | | | Mandate Expiry Handling

---

## #97 — End to end API Documentation
**Status:** Not started | **Last edited:** February 12, 2025 5:50 PM

**Problem:**
are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

**Solution:**
?**

---

## #98 — [Platform] Enabling alternate mandate registration
**Status:** Done | **Last edited:** February 1, 2025 7:49 PM

**Problem:**
are we solving?**

As a part of the application flow, users have to register a mandate. While it is not mandatory, it is convenient for both the lender as well as the user to do so.

- **Convenient EMI Payments**: A mandate ensures automatic deduction of EMIs from the borrower's account, reducing the risk of missed payments.
- **Assurance for the Lender**: It provides the lender a reliable mechanism for repayment.

The mandate registration process requires the user to authenticate the registration on their bank account, NPCI allows the user to do so via three methods:

1. E-NACH 
    1. Debit 

**Solution:**
?**

We will be utilising Digio’s flow to initiate mandate registration flow for the user/LSP. LSP will be able to control which registration method is to be used in the mandate registration request.

LSP be able to pass the preferred method of mandate set up to the request post which the request will go through a whitelist. 

Each LSP will have the methods of mandate registration whitelisted for them (If they can use E-NACH/ Aadhaar E-sign/ Physical NACH) for the user mapping with source code.

Fenix will also share a bank whitelist with the LSPs for them to able to gauge which bank account is activated and available for the corresponding registration method.

Basis the selection, Fenix will invoke the specfic flow for the LSP by modifying a request parameter for Digio

<aside>
💡

Importa

---

## #99 — TATA PG dulplicate refNo validations
**Status:** In progress | **Last edited:** December 9, 2024 5:43 PM

**Problem:**
are we solving?**

We're addressing a critical payment reconciliation issue where:

1. The bank occasionally generates duplicate reference numbers for two different payments.
2. This leads to failed accounting of repayments in the statement of accounts(SOA) of the customer in TATA for repayments with SUCCESSFUL transaction status from the TATA Payment Gateway.

---

**Solution:**
?**

---

## #100 — [Platform] Mandate presentation request optimisati
**Status:** Done | **Last edited:** December 31, 2024 11:49 AM

**Problem:**
are we solving?**

We are solving three problems via this enhancement:

- Mandate presentation UTR entries for the destination bank (User) are very general. Since the amount is deducted automatically from the user’s bank account, it often gets difficult to track why the amount was deducted (across services and products) while analysing bank account statements.
- Currently reconciliation for mandate presentations is built on top of item ids (shared by Digio) to us in response and also passed as a parameter in the report.

---

**Solution:**
?**

P1:

- We will be passing custom narrations in the user’s bank account statement
DSP Finance NACH debit for LAN: FXLAN534324

and UTR in the user’s loan account statement:
Loan repayment received against sale of security: IN9876543210 for account number: FXLAN6789012 with Ref ID:

P2:
We will be passing enrichment values in the presentation request for Digio to assist reconciliation with operations team

---

## #101 — Show accrued interest on UI
**Status:** Not started | **Last edited:** December 26, 2024 5:50 PM

**Problem:**
are we solving?**

- Users are not able to track their interest before the due date of their interest cycle
    - Users are not able to plan their withdrawals and repayments basis accrued interest on their line (it is an important decision making parameter for them)
    - Ops team estimates this basis the current POS of the user and gives approximate answers
    - Users also like to estimate their monthly interest basis accrued interest and current POS and are currently not able to do it to resolve their queries

![Screenshot 2024-05-30 at 5.13.21 PM.png](Show%20accrued%20interest%20on%20UI/Sc

**Solution:**
?**

Users will be able to track the accrued interest accumulated over the month on the dashboard

---

## #102 — Test campaign for MFDs
**Status:** Not started | **Last edited:** December 25, 2024 10:43 AM

# Test campaign for MFDs # Re-engagement Campaign Message Templates 1. **Segment Definition:** - Create 3 segments based on time since empanelment: [https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing) - Recent (0-30 days): 807 partners - Mid-term (31-90 days): 1,244 partners - Long-term (90+ days): 9,763 partners 1. **Experiment Design:** - Split each segment into 3 groups: - Control Group (20%) - Treatment Group A (40%): Personalized WhatsApp/SMS - Treatment Group B (40%): WhatsApp/SMS + Email follow-up 1. **Intervention Plan:** - Treatment A: - Day 1: Initial WhatsApp message with personalized activation link - Day 3: SMS reminder with key benefits - Day 7: Final WhatsApp message with time-limited incentive - Treatment B: - Day 1: WhatsApp message + Email with detailed activation guide - Day 3: SMS reminder + Email success stories - Day 7: Final WhatsApp + Email with time-limited incentive # Re-engagement Campaign Message Templates ## Recent Partners (0-30 days) ### Treatment A (WhatsApp/SMS Only) **Day 1 - WhatsApp:** ``` Hi {partner_name}, Help your clients keep their investments growing! 📈 With Volt Money, your clients can: • Get instant credit against MF holdings • Access funds in just 5 minutes • Keep their investment journey uninterrupted Try it now: {partner_dashboard_link} Need help? Chat with us Mon-Sat (9:30 AM - 8 PM) ``` **Day 3 - SMS:** ``` {partner_name}, stop redemptions today! Your clients can get credit against MFs in 5 mins while keeping their investments intact. 2000+ partners trust Volt Money. Start here: {partner_dashboard_link} ``` **Day 7 - WhatsApp:** ``` Hi {partner_name}, Your clients need quick funds? Help them avoid redemption with Volt Money! ✨ Special offer: Extra 5% commission on your first 5 client referrals Get started: {partner_dashboard_link} Questions? We're here to help! ``` ### Treatment B (WhatsApp/SMS + Email) **Day 1 - Email:** Subject: Stop Client Redemptions with Instant Credit Solutions ``` Dear {partner_name}, Are your clients considering redemption for short-term needs? Volt Money has a better way! Help Your Clients: 1. Keep Their Investments Growing 2. Get Credit in 5 Minutes 3. Meet Urgent Cash Needs 4. Stay on Track for Long-term Goals Join 2000+ partners who are helping clients preserve their wealth. Try It Today: 1. Visit your dashboard: {partner_dashboard_link} 2. Share with your first client 3. Watch their portfolio stay intact Our expert team is available Monday through Saturday (9:30 AM - 8 PM) to assist you. Best regards, Team Volt Money ``` ## Mid-term Partners (31-90 days)

---

## #103 — [Platform] Risk report
**Status:** Done | **Last edited:** December 20, 2024 2:26 PM

**Problem:**
are we solving?**

As an NBFC it is important to keep a keen eye on potential risk to the organisations, these risks can be in terms of:

- Financial risk (overdue customers)
- Operational risk (Customers without active mandate set ups)
- Compliance / Regulatory risk (Customers with high AML risk / Bureau risk / Expiring KYC)

We need to solve for visibility of the same so that the risk operations team can actively track and monitor potential risk to the organisation and accordingly take necessary measures.

---

**Solution:**
?**

We will be building a risk report, which will be scheduled to the risk operations team at a regular cadence. 

The operations team will also be able to generate this report via the command centre and download it for internal tracking. This report will be access controlled and will only be able to be tracked by the risk team.

Correspondingly we will be introducing a new role, “Risk operations” which will have access to a basic approval access and additionally will have access to the risk report within the report section.

---

## #104 — [LSP] DSP VA
**Status:** Not started | **Last edited:** December 2, 2024 8:10 PM

# [LSP] DSP VA - What amount to show? - If we are showing only that then how are we expecting user to make the repayment of interest/prinicpal - Can be done like TCL? - Can we get the outstanding amount changed as total outstanding - BFL - DSP - TCL - Can we show the breakdown - Apportionment logic should be shown if we showing only one amount & only one bank account? - Will have to show break down? - Pull up numbers for bank transfer and importance of showing it expanded

---

## #105 — Single drawdown Term Loan LMS Requirements
**Status:** In progress | **Last edited:** August 9, 2025 11:23 AM

**Problem:**
are we solving?**

- **Low awareness of line-based lending products:** Most Indian consumers do not understand the concept of a reusable credit line or overdraft (OD)-style borrowing.
- **Lack of lifecycle borrowing behaviour:** Users do not engage in re-borrowing after repayment, resulting in limited customer lifetime value (LTV).

---

**Solution:**
?**

Product Overview

We propose a vanilla **term-loan-style wrapper** on top of the line construct to match user expectations and drive better usage. The solution involves:

- **Offering a familiar term-loan onboarding flow** for the first drawdown
- **Allowing re-borrowing** once limits are replenished through repayment.

This hybrid approach is designed to increase adoption and grow customer LTV.

**Product Technical Construct**

A **line-backed, single-drawdown term loan**, where:

- DSP creates and manages the line & loan internally for eligibility and lifecycle logic.
- **Only the loan construct is exposed to the LSP**, appearing as a standard term loan.
- Only one single **active** loan drawdown is supported at a time in this construct ie loan = line at any pt in time
- Future draw

---

## #106 — Cashfree PG integration
**Status:** Pending Review | **Last edited:** August 5, 2025 3:56 PM

**Problem:**
are we solving?**

---

- Our current payment infrastructure depends entirely on Razorpay as the sole gateway for processing repayment transactions. This creates a critical single point of failure - if Razorpay experiences service disruptions, our entire repayment collection system becomes unavailable (users are not comfortable with VA payments), directly impacting cash flow and customer experience.
- Several of our partner LSPs are hesitant or unwilling to implement Cashfree PG integration due to various business considerations, including competitive concerns and strategic partnerships.

**Solution:**
?**

---

## #107 — [DSP] Dues collection comms
**Status:** Done | **Last edited:** August 22, 2025 3:28 PM

**Problem:**
are we solving?**

- Currently DSP is not sending collection related communications to the user -
    - ***Poor customer experience :*** This leads to user being unaware of the due dates, leading to them missing the payments, incurring bounce/penal charges
    - ***Business risk :*** This puts DSP finance (as an NBFC) at an compliance risk, as it is mandatory for NBFCs to send collections related communications to the user as per RBI regulations

---

**Solution:**
?**

---

## #108 — Productisation of admin tool Change email address
**Status:** Not started | **Last edited:** August 21, 2024 12:14 PM

**Problem:**
are we solving?**

- When customers need to change their email or mobile number, they need to send the details to the RMs to be updated via registered email. This may cause manual errors at the customer and RMs end due to absence of validation of email and phone number.
- The admin tool for these changes cannot be used in isolation and requires communication with all third parties involved after the Loan account is created.

---

**Solution:**
?**

---

## #109 — NBFC NACH Mandate Limit Change
**Status:** Ready for Tech | **Last edited:** August 13, 2025 6:31 PM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

**Solution:**
?**

---

## #110 — [Platform] Validation to Stop Un-pledging, closure
**Status:** Done | **Last edited:** April 4, 2025 2:21 PM

**Problem:**
are we solving?**

Account freezing or suspension is a temporary restriction that prevents an account holder from accessing specific or all account features. This occurs for several reasons:

- Suspicious activity detection
- Policy violations
- Payment issues
- Security concerns

We have the operations team, and risk team who can place an account under suspension or frozen state. 

The frozen state **ALSO** occurs when an active account undergoes foreclosure procedure so as to prevent the user from initiating any debit transactions while the account closure is in process.

Freezing an account

**Solution:**
?**

We will be adding some validations to stop foreclosure and un-pledging of the manually frozen accounts.

The foreclosure check will include:

1. If the account is active/expired, freeze it and continue the foreclosure process
2. In case if an account is frozen before the initiation of the foreclosure by the user, it has to be rejected.

The un-pledging check will include:

1. If the account had been frozen, don’t go forward with the un-pledging
2. If is active, then continue with the pledging

---

## #111 — E2E Sell-off Productisation 34ae8d3af13a80928d80d8
**Status:** Not started | **Last edited:** April 30, 2026 5:35 PM

**Problem:**
are we solving?

- Today, sell-off execution is a fully manual, analytics-dependent process — ops teams rely on daily risk reports, manually compute DPD and shortfall sell off amounts, select funds, prepare maker file, and initiate sell-offs via the Command Centre.
- With an average of 193 sell-off requests per day (Jan–March 2026) and a peak of upto 4000 DPD requests (as on 21st Apr 2026), this introduces significant delay between trigger and execution.
- Any error in selecting accounts for sell off , sell off amount computation, fund selection, or file preparation by analytics and ops direct

**Solution:**
?

**In scope:**
- Daily automated identification of shortfall-eligible LANs (`shortfall_ageing >= 7`) and DPD-eligible LANs (DPD > 75 trigger 1st and then 21st-of-month trigger)
- Shortfall amount and DPD amount computation per LAN using get overdue detail API and shortfall ageing data
- Ongoing sell-off detection from `fenix_sell_off_collaterals_request` and appropriate skip/adjustment logic
- 5% execution buffe

---

## #112 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #113 — Product Note – DRPS (Final Version – Unified Forma
**Status:** Ready for Tech | **Last edited:** April 22, 2026 7:17 PM

**In scope:**
- Credit Line products only
- Monthly frequency
- Single unified schedule table
- JSON + PDF output

Term Loans are out of scope.

---

# Product Note – DRPS (Final Version – Unified Format) # 1. Background & Context ## Who is facing the problem - End customers using LAMF (Credit Line / LAS) - Customer support & operations teams - NBFC (regulatory requirement to provide updated repayment schedule) --- ## What is the challenge today - Static schedules become outdated after: - Disbursement - Part repayment - ROI change - Charge application - Users depend on SOA to understand updated dues. - No single structured month-wise forward view aligned with current POS. --- ## Why this is important LAMF is a **dynamic demand loan**, not a fixed EMI loan. A Dynamic Repayment Schedule must: - Reflect actual utilisation - Reflect historical interest accrual - Provide predictive view till closure - Be aligned with system ledger - Be audit-reconcilable --- # 2. Problem Definition DRPS must: 1. Reflect actual historical data till generation timestamp. 2. Reflect projected dues till closure date. 3. Be aligned to: - Current POS - Current ROI - Closure date (currentTermEndDate) 4. Include non-contingent charges prospectively. 5. Use a **single continuous table format**. --- # 3. Solution Scope ## In Scope - Credit Line products only - Monthly frequency - Single unified schedule table - JSON + PDF output Term Loans are out of scope. --- # 4. DRPS Structure There will be **one unified repayment schedule table**. Older rows = system-derived actuals. Future rows = system-computed projections. The format remains identical for all rows. --- # 5. Repayment Schedule Columns (Final – As Per New Requirement) | Column | Description | | --- | --- | | Repayment Date | Month-end date (7th of next month for due logic; last row = closure date if mid-month) | | Outstanding principal (Opening) | Principal outstanding at start of period | | Principal payable/Prepayment | Principal component (only non-zero in closure row unless repayment exists historically) | | Outstanding principal (Closing) | Opening − Principal (interest does not reduce principal) | | Instalment | Interest + Charges (Last instalment principal will be included in instalment) | | Interest payable/Paid | Interest for that period (actual for past, computed for future) Middle of the month accrued interest for interest until now + calculate future interest based on current ROI | | Charges payable/Paid | Retro charges for past; Non-contingent charges for future (AMC charge) | No instalment type column. --- # 6.

---

## #114 — Admin tool migration to Appsmith
**Status:** In progress | **Last edited:** April 14, 2025 2:14 PM

**Problem:**
are we solving?**

- The support and ops teams currently rely on two separate tools (admin tool & service dashboard) to handle customer queries and unblock the customer
- The admin tool requires extensive training since its actions are standalone, lacking context on their use cases, and limitations
- Access control, error handling, education, high effort

---

**Solution:**
?**

---

---

## #115 — VA Repayment Handling [Volt LMS]
**Status:** Not started | **Last edited:** April 10, 2025 10:50 AM

**Problem:**
are we solving?**

Currently, Volt cannot create the Virtual Account (VA) repayment requests, resulting in an inability to track and post repayments made through Virtual Accounts. This creates a gap between DSP Finance's successful repayment processing and Volt's internal payment posting system, leading to potential reconciliation issues and incomplete financial records.

---

**Solution:**
?**

We will implement a webhook integration system that receives repayment notifications from DSP Finance when a customer successfully makes a repayment via their Virtual Account. The system will map the FXLAN (Fenix Loan Account Number) provided in the webhook to our internal creditId, allowing us to properly post and track these repayments in our database.

---

## #116 — Check eligibility overhaul
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

In context of Check limit page we are solving the following problems

1. UI/UX Problems: 
    1. CTA copy signifies that this is an eligibility test which means not everyone is eligible for loan. 
    2. The main headline occupies too much space. Pushes the form down and deviates user attention from the form. The current headline conveys very little. 
    3. Too much space on the main scroll is left unused. Nothing except the form and headline is visible in the first fold. Pushes trust markers and education content down. 
    4. CTAs that are of now use to user at this stage

**Solution:**
?**

---

## #117 — Website meta description change
**Status:** Unknown | **Last edited:** Unknown

# Website meta description change Benchmarking for: Deliver crisp view of our offering to the user while maintaining/improving SEO Person: Saksham Srivastava **Lalit’s pointers:** most trusted platform to get instant loan (overdraft) against MF and shares. Very low interest rate of 9-11% | No preclosure charges | 100% digital 5 minute process | Funds in 4 business hours 1. Trust 2. Preclosure charges 3. Quick and easy process Benchmarking | Page | Headling | Meta description | Remarks | | --- | --- | --- | --- | | Smallcase | Loan against mutual funds | Low-interest ***loan against*** MF — Need ***loan*** for personal use? Get 10.75% PA ***loan against mutual funds*** on smallcase. Try now. Flexible Repayment terms. No Credit Score needed. No Foreclosure charges. | - Tries to explain the complete functionality - Personal use add comparison point for the use. - The | | SBI | Get Loan Against Mutual Fund Units Online in India | Get ***Loan Against Mutual Fund*** Units Online in India at SBI. Look for various features which contain the minimum & maximum amount, interest rates & renewals. | | | HDFC Bank | **Loan Against Securities** | Get up to 80% of the value of your ***securities against*** a wide range of collaterals, including shares, ***mutual funds***, life insurance policies, bonds, etc. | - LTV mentioned can be a key attraction | | Bajaj Finserv | **Loan Against Mutual Funds (LAMF) up to Rs. 5 crore** | Apply for a ***Loan Against Mutual Funds*** with a minimum fund value of Rs. 50000, and get a loan limit of up to Rs. 5 crores at attractive rates. | | | ICICI Bank | [**Insta Loan Against Mutual Funds | Online Loans**](https://www.icicibank.com/personal-banking/loans/loan-against-securities/mutual-funds) | Now avail of Insta ***Loan Against Mutual Funds*** in just a few minutes! You can now avail of paperless and instant liquidity against your mutual funds through ... | | | FundsIndia | [**Loan Against Mutual Funds, Eligibility, Benefits and Features**](https://www.fundsindia.com/loan-against-mutual-funds) | Raise instant funds online with ***loan against mutual funds*** at just 9% p.a Interest rate. 100% digital process with Mirae Asset Financial Services. | | | Volt Money | [**Volt Money | Instant loan against mutual funds and stocks**](https://voltmoney.in/) | Get credit line/OD limit ***against mutual funds*** starting at 9.95% per annum with trusted lenders in less than 5 minutes. | | Following are the options for headline

---

## #118 — Coms strategy
**Status:** Unknown | **Last edited:** Unknown

# Coms strategy @Naman Agarwal Creating a comprehensive **Communications (Comms) Review Plan** is essential to ensure that all outbound communications are effective, targeted, and free from errors that could lead to customer confusion or dissatisfaction. Below is a structured plan addressing your requirements, along with best practices and industry references to guide implementation. [MFD comms ](Coms%20strategy/MFD%20comms%20120e8d3af13a808297c1f3ec8ab11109.md) --- ## **1. Identify All Outbound Communications** ### **1.1. Inventory of Outbound Channels** - **Email Campaigns:** Promotional, transactional, newsletters. - **SMS Notifications:** Alerts, reminders, confirmations. - **Push Notifications:** Mobile app alerts. - **WhatsApp Messages:** Customer support, updates. - **Social Media Posts:** Announcements, engagements. - **In-App Messages:** User guidance, feature updates. - **Direct Mail:** Physical correspondence for critical communications. ### **1.2. Catalog Existing Communications** - **Create a Communication Matrix:** List all outbound messages, their purpose, channels used, frequency, and responsible teams. - **Regular Audits:** Schedule periodic reviews to update the communication matrix. --- ## **2. Define Trigger Conditions** ### **2.1. Event-Based Triggers** - **Transactional Events:** Payment confirmations, account changes. - **Behavioral Triggers:** Abandoned cart, inactivity alerts. - **System Events:** Downtime notifications, maintenance alerts. ### **2.2. Customer Lifecycle Triggers** - **Onboarding:** Welcome messages, setup guides. - **Milestones:** Anniversary messages, loyalty rewards. - **Churn Prevention:** Re-engagement campaigns. ### **2.3. Define Clear Criteria** - **Specific Conditions:** Clearly outline what event or behavior triggers each communication. - **Thresholds:** Set limits (e.g., number of failed transactions before sending a warning). --- ## **3. Identify Target Customers** ### **3.1. Segmentation** - **Demographics:** Age, location, gender. - **Behavioral Data:** Purchase history, engagement level. - **Psychographics:** Interests, values. ### **3.2. Data Collection and Analysis** - **CRM Systems:** Utilize customer relationship management tools to gather and analyze customer data. - **Behavioral Analytics:** Track and interpret customer interactions across channels. ### **3.3. Continuous Updating** - **Dynamic Segmentation:** Regularly update customer segments based on new data. - **Feedback Loops:** Incorporate customer feedback to refine target groups. --- ## **4. Crafting the Message Text** ### **4.1. Clarity and Conciseness** - **Clear Language:** Avoid jargon; use simple, direct language. - **Concise Messaging:** Communicate the essential information without unnecessary details. ### **4.2. Personalization** - **Use Customer Names:** Personalize messages to increase engagement. - **Tailored Content:** Customize messages based on customer segment and behavior. ### **4.3. Actionable Instructions** - **Next Steps:** Clearly outline what the customer should do next. - **Links and Resources:** Provide direct links for actions like payment or support. ### **4.4. Compliance and Sensitivity** - **Regulatory Compliance:**

---

## #119 — Copy Plugin
**Status:** Unknown | **Last edited:** Unknown

# Copy Plugin # ✅ Product Requirements Document: Volt Copy Assistant (Figma Plugin) ## 📌 Overview **Volt Copy Assistant** is a Figma plugin for designers and product managers working on the Volt Money app. It helps improve UX copy across product flows by offering tone-corrected, compliant, and user-friendly rewrites using Google Gemini's AI API — directly within Figma. --- ## 🎯 Core Objectives - Improve fintech UX copy with tone-aligned suggestions - Reduce copywriting guesswork for product designers - Ensure consistency with Volt's design principles (Clarity, Helpfulness, Simplicity, Transparency, Accessibility) - Save time by suggesting, editing, and replacing copy inside Figma --- ## 🧩 Plugin Actions ### 🔹 When a text layer is selected: - Show the original text in an editable input box - Let the user select a tone or context (e.g., CTA, Error, Tooltip, Instructional) - On clicking “Suggest Rewrite”, send the text + tone to Gemini API - Show AI-generated suggestion in a preview area - Allow one-click replacement of the Figma text layer with the suggestion ### 🔸 When **no text layer is selected**: - Show a clear message: “Please select a text layer to get started” - Disable suggestion and replace buttons --- ## 💡 Key Features | Feature | Description | | --- | --- | | **Text input** | Auto-populated from selected Figma text layer | | **Tone/context selector** | Dropdown to choose tone (e.g., Clear & Formal, Conversational, Empathetic) | | **Suggest button** | Triggers Gemini API call and returns rewrites | | **Preview suggestion** | Displays new copy in plugin UI | | **Replace button** | Replaces selected layer’s text with suggested rewrite | | **Fallback logic** | If Gemini fails, show “Something went wrong. Please try again.” | --- ## 🧱 UI Layout (Plugin Panel) | Section | Description | | --- | --- | | Header | “Volt Copy Assistant” with logo (optional) | | Original Text | Textarea (pre-filled from selected layer) | | Context Selector | Dropdown: Error, CTA, Tooltip, Instruction | | Suggest Button | Click to call Gemini | | Suggestion Output | Textarea showing new UX copy | | Replace Button | Click to update Figma layer | --- ## 🔌 External APIs & Data - **Gemini API (Google)** `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent` Authentication via API Key: AIzaSyANJ1RcD5FBIAzxndjvjkZdcmjWDJxl2OA - **Prompt Template (example):** `"You're a UX writer for an Indian fintech app. Rewrite the following copy in

---

## #120 — Copy system for Volt
**Status:** In progress | **Last edited:** Unknown

# Copy system for Volt Charter: Design Initiatives # Context Aim to keep copy clear and build guidelines for people to jusde copy by. [UX Writing for Indian Fintech Users (Volt) – Research & Guidelines](Copy%20system%20for%20Volt/UX%20Writing%20for%20Indian%20Fintech%20Users%20(Volt)%20%E2%80%93%20Resea%20211e8d3af13a808785a4dc9775a26443.md) [Copy Plugin](Copy%20system%20for%20Volt/Copy%20Plugin%2021be8d3af13a8084af15c2492f81eebc.md) [Volt Plugin Knowledge Base](Copy%20system%20for%20Volt/Volt%20Plugin%20Knowledge%20Base%2025de8d3af13a802abbd7d4ab8d9b20d2.md) # Process - [x] Define Volt’s principles for copy based on best practices - [x] Understand compliance and legal requirements from Indian fintechs - [x] Make the prompt for copy json with tone, ux writing principles and Gemini API Key - [x] Build copy on cursor - [ ] Test & Improve # Research Volt’s Design Fundamental Pillars 1. Simplicity 2. Speed 3. Transparency 4. Helpful **Fundamentals of UX Writing (for fintech apps)** At its core, UX writing is about: ✅ **Guiding** users through tasks: What to do ✅ Making **complex information simple**: Information clarity ✅ **Building trust** and confidence: Reassurance ✅ Ensuring **accessibility**: Less jargon more simple words # Figma

---

## #121 — Information Architecture
**Status:** Deprioritised | **Last edited:** Unknown

# Information Architecture Charter: Design Initiatives # Jobs to Be Done What are the **core jobs** a user comes to Volt to *get done*? ## Before taking a loan - Check loan eligibility? - Understand repayment - Understand how ## After taking a loan - How to withdraw? - What is the remaining balance? - Track disbursal? - Understand how interest is calculated? - What are the repayment options? -

---

## #122 — Product Note Post limit fetch optimisation
**Status:** Unknown | **Last edited:** Unknown

# Product Note : Post limit fetch optimisation # Objective - This is **post-credit limit fetch, pre-KYC**. - User already knows eligibility → now reviewing loan terms. - Goal: Maximise conversion from this page to KYC initiation. # Current journey ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png) # Funnel metrics ## Overall Funnel [Only Eligible Users] ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png) ## First time success rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png) ## Median time to convert of overall funnel ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png) ## P75t and P90th conversion time ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png) ## MF Fetch Anchor Page Analysis ## Median time to convert from step 1 to 2 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png) ### No. of users who clicked on ‘Mutual Funds Fetched Card’ In LOS i.e new users ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png) In LOS + LMS combined ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png) ### No. of users to clicked on back button after being eligible ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png) - ### No. of users to clicked on back from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png) ### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png) ### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png) ### Refresh portfolio on MFC Anchor page ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png) ## Set Credit Limit Page Analysis ## Median time to convert from step 2 to 3 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png) ## No of users who clicked on edit limit pencil icon ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png) ## Loan Offer Page Analysis ## Median time to convert from step 3 to 4 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png) ### Loan offer page CTA clicked ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png) ### No. of users who clicked prepayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png) ### No. of users who clicked withdrawal and repayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png) ### No. of users who clicked charges expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png) ### No. of users who clicked info icon on loan tenure ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png) ### No. of users who clicked info icon on interest rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png) ### No. of users who clicked info icon on credit limit ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png) ## WATI Chats queries [https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system) --- # Insights **Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**. - Users get eligibility but hesitate at credit limit setup - Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. - Image ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png) - Rest refresh portfolio(~6-7%) and some hit back button. - While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs **Possible reasons of the drop-offs**

---

## #123 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #124 — Repayment summary screen
**Status:** Developed | **Last edited:** Unknown

# Repayment summary screen Assign: Karuna Sankolli Charter: LMS Pod - [x] Call with Ranjan & Amey - [x] Brainstorm component design - [x] Alignment on flow - [x] Alignment on wires - [ ] Call with Lalit [https://embed.figma.com/design/axnRcEvkbu75kd0uaWsF9B/Repayment-flow?node-id=789-4149&node-type=section&t=cCjoDqDjyalAcG3w-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/axnRcEvkbu75kd0uaWsF9B/Repayment-flow?node-id=789-4149&node-type=section&t=cCjoDqDjyalAcG3w-11&embed-host=notion&footer=false&theme=system)

---

## #125 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #126 — E2E Sell-off Productisation V1
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?

- Today, sell-off execution is a fully manual, analytics-dependent process — ops teams rely on daily risk reports, manually compute DPD and shortfall sell off amounts, select funds, prepare maker file, and initiate sell-offs via the Command Centre.
- With an average of 193 sell-off requests per day (Jan–March 2026) and a peak of upto 4000 DPD requests in a single day(on 21st Apr 2026), this introduces significant delay between trigger and execution.
- Any error in selecting accounts for sell off , sell off amount computation, fund selection, or file preparation by analytics an

**Solution:**
?

**In scope:**
- Daily automated identification of shortfall-eligible LANs (`shortfall_ageing >= 7`) and DPD-eligible LANs (DPD > 75 trigger 1st and then 21st-of-month trigger)
- Shortfall amount and DPD amount computation per LAN using get overdue detail API and shortfall ageing data
- Ongoing sell-off detection from `fenix_sell_off_collaterals_request` and appropriate skip/adjustment logic
- 5% execution buffe

---

## #127 — BRD Enhancements to Schedule & Derived Details Pro
**Status:** Completed | **Last edited:** Unknown

# BRD: Enhancements to Schedule & Derived Details Processing for OD (Loan Against Mutual Funds) Last Edited: December 11, 2025 2:41 PM PRD Owner: Vaibhav Arora ## **1. Problem Statement** Our OD product relies heavily on Finflux’s **schedule** and **schedule-derived details** for: - Accurate repayment allocation - DPD computation - Interest/charge tracking - Reconciliation, reporting (internal and external) Currently, certain system behaviours in the LMS lead to **incomplete or incorrect schedule updates**, which introduces reconciliation gaps and incorrect ageing/DPD calculations. We need Finflux to enhance how the LMS **creates, updates, and settles obligations** and **populates derived details** whenever specific transactions occur. --- ## **2. Context: How It Should Work (High Level)** - Any due created on a line (interest, charge, fee, penalty) should create an **obligation** in the schedule. - Currently we do not get the source transaction that created that obligation, we require source transaction to be mapped with the schedule ID so that we can directly map the transactions that created the corresponding schedule - When a transaction settles that obligation, the schedule and derived details should reflect: - obligation met - amount accounted - linkage to the transaction identifier - timestamps for audit - For OD products, interest accrues daily and becomes due only under certain events (billing, foreclosure (clear dues) etc.). Finflux already follows this pattern for regular repayments. The gaps occur only for specific transaction types listed below. --- ## **3. Issues & Required Enhancements** --- ## **3.1 Issue 1: *Clear Dues (used for Foreclosure) does not update schedule or derived details*** ### **Current Behaviour** - During foreclosure, Fenix performs a **“clear dues”** transaction to make the accrued interest due for the line: - Accrued-but-not-yet-due interest is first made due. - Finflux then settles this newly created due using excess funds when the clear dues API is hit - However: - The **schedule table is not updated** to reflect the new temporary obligation. - The **obligation is not marked as met**. - **Derived details** are not populated with the settlement transaction. ### **Impact** - Reporting discrepancies (interest recognised vs. interest settled). - Incorrect DPD because obligations appear “unmet”. ### **Required Behaviour** Finflux should: 1. **Create an obligation** in the schedule whenever clear-dues makes an amount due (accrued interest or any charge). 2. **Immediately settle the obligation** and mark: - obligation_met = true - obligation_met_on = timestamp 3. **Populate derived details** with: - linkage to the

---

## #128 — Charge details on Command centre
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently we have the following charges that we apply on customer loan accounts:

- Processing fee (Account opening)
- Margin pledge (When user pledges more securities)
- Dishonour (When user fails to clear their dues by the 8th of the next month (Due date))
- Penal charges (Applied daily for every day the customer remains in an overdue status (Interest is overdue))

Out of the 4 charges, the first three (barring penal charges) are applied via Fenix (internal LMS) while the fourth charge (Penal charges) are applied directly via Finflux (external LMS).

Our operations team, d

**Solution:**
?**

---

## #129 — Charge reversal enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Today, waiving or refunding charges for a user is manual, operationally intensive, and people-dependent process. Not only does this make it error prone, it introduces friction across internal teams and impacts customer experience. The key issues we’re addressing include:

---

**Solution:**
?**

We will be creating a charge waiver task for command centre which will behave in the following manner:

- If a charge is completely outstanding, that is the amount that was applied has not been collected from the user, will be waived.
- If a charge is completely paid/collected from the user, we will be passing a credit note to the user’s loan account

<aside>
🚨

If a charge is partially paid/collected, we will not allow it to be waived or refunded - (Validation error). - We will now be passing a credit note for this as well

</aside>

- If a charge is partially paid/collected, we will not allow it to be waived or refunded - (Validation error).

We will be creating a new payment type called “CREDIT_NOTE” this repayment will not have a corresponding money transaction associated with it.

---

## #130 — Charge reversal enhancement V2
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Today, waiving or refunding charges was manual, operationally intensive, and people-dependent. With the charge reversal enhancement now built and deployed, we have eliminated dependency on engineering/backend intervention, reduced friction for internal teams, and improved customer resolution time.

This PRD documents the final implemented solution — including the maker/checker workflow, credit note processing, validations, accounting flows, and the enhancements required to support charges with no GST and the productisation manual JV transaction posting

---

**Solution:**
?**

All components below are **implemented and live**.

We have created a **Charge Refund Maker/Checker workflow** that behaves as follows:

- **If a charge is completely outstanding** → it is waived.
- **If a charge is completely collected/paid** → a **Credit note** is issued to the loan account.
- **If a charge is partially collected** → a **Credit note** is issued to the loan account.

A new repayment type **“Credit note”** is now supported in LMS.

This repayment *does not* trigger any cash movement. Operations uses this type for reconciliation visibility.

The first set of supported use cases now live:

- Processing fees
- Margin pledge charges
- Dishonour fees
    
    (All as configured under ADHOC charges)
    

---

---

## #131 — Colending Disbursement and Charge knock off
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Designing a **system-level mechanism** to:
    - Handle **charge knock-off as part of the disbursement workflow**
    - Support **capitalised charges** that are:
        - Part of borrower POS
        - Owned by a specific lender
    - Correctly split:
        - Disbursements
        - Repayments
        - Outstanding balances
- Applicable for:
    - **Initial disbursement**
    - **Future disbu

# Colending: Disbursement and Charge knock off Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - **Internal teams**: Engineering, Finance, Ops, Risk, Product - **Partners**: DSP (originator / servicer), TCL (co-lender) - **Indirectly**: End customers (via statements, repayments, redraw behaviour) - **What is the challenge today** - Processing fees and other charges are **knocked off at disbursement**, but: - These charges are collected via disbursements by doing a short disbursement - Economically **owned by a specific partner (DSP)** - Current POS and split logic assumes: - A **single POS** - A **static co-lending ratio (10 / 90)** - This leads to: - Incorrect partner settlements - Over / under-recovery for lenders - Increasing complexity as multiple disbursements and future charges are introduced - **Why this is important** - Incorrect allocation impacts: - **Partner trust and reconciliation** - **Revenue recognition** - **Audit and regulatory confidence** - As the product evolves (OD-like behaviour, multiple charges), ad-hoc fixes will **compound risk and tech debt** - This needs a **foundational, extensible solution** --- ## **1. Problem Scope** ### In scope - Designing a **system-level mechanism** to: - Handle **charge knock-off as part of the disbursement workflow** - Support **capitalised charges** that are: - Part of borrower POS - Owned by a specific lender - Correctly split: - Disbursements - Repayments - Outstanding balances - Applicable for: - **Initial disbursement** - **Future disbursements** in OD / revolving facilities - **Multiple charge types** knocked off at disbursement (processing fee today, others in future) owned by different lenders. - Primary users: - Finance & Ops teams (reconciliation, settlement) - Engineering (LMS, accounting, settlement flows) - Secondary users: - Sales & onboarding teams (clear explanation of net disbursal vs loan amount) - Risk & Audit teams --- ### Out of scope - Interest accrual logic changes - Interest continues to follow existing borrower-level rules - Customer-facing UI redesign - No changes to how the customer views the loan, beyond correctness - Partner commercial renegotiation - Assumes existing ownership rules are final - Bureau reporting changes - Borrower-facing loan remains the single source for external reporting **Rationale**: These are orthogonal concerns and would delay solving the core accounting and settlement correctness problem. --- ## **2. Success Criteria** ### Primary outcomes 1. **Correct economic settlement** - Partner recoveries exactly match agreed ownership

---

## #132 — Corporate action - Data feed
**Status:** Completed | **Last edited:** Unknown

# Corporate action - Data feed Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # Corporate Actions Data Feed ## Overview To support monitoring of securities pledged as collateral, we have reviewed a **Corporate Actions data feed sourced from BSE end-of-day bulletins**. This feed provides information on **events and disclosures that may impact the value, structure, or tradability of securities**. The data is consumed daily and can be used by the Risk team to monitor portfolio changes and identify events that may require action. The data covers the following broad categories: - Corporate action events - Company structural changes - Market disclosures - Large market transactions - Insider activity - Liquidity indicators --- # 1. Corporate Action Events This dataset contains information about **corporate actions declared by listed companies** that may affect the number of shares, price, or entitlement of shareholders. Typical corporate actions include: - Dividends - Stock splits - Bonus issues - Rights issues - Buybacks - Capital restructuring events For each event, the feed provides key reference dates such as: - **Record Date** – Date used to determine shareholder eligibility - **Ex-Date** – Date after which the security trades without the entitlement - **Cum Date** – Date before which investors must hold shares to be eligible - **Effective Dates** – Time period during which the action is applicable In addition, where applicable, the feed also provides: - Dividend amount or payout value - Share conversion ratios (e.g., split or bonus ratios) - Share quantity adjustments - Offer price or premium for rights issues These events are critical for adjusting **collateral valuation and share quantities** in pledged portfolios. --- # 2. Corporate Action Classification A separate master dataset provides the **mapping of corporate action identifiers to the specific event type** (e.g., dividend, split, bonus). This allows systems to interpret the corporate action feed and determine the **nature of the event impacting a security.** ---

---

## #133 — Credit note PRD
**Status:** Pending review | **Last edited:** Unknown

**Problem:**
are we solving?**

Today, waiving or refunding charges for a user is manual, operationally intensive, and people-dependent process. This introduces friction across internal teams and impacts customer experience. The key issues we’re addressing include:

---

**Solution:**
?**

We will be creating a new payment type called “CREDIT_NOTE” this repayment will not have a corresponding money transaction associated with it. Operations team will use the payment type to identify the transactions and accordingly handle in reconciliation.

The first use case that we will be covering will be the refunds of adhoc charges placed by the NBFC:

- Processing fees
- Margin pledge charges
- Dishonour fees`

---

## #134 — Dishonour charge enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Dishonour charges are applied to user loan accounts when monthly dues are not paid before the 7th of the month. However, the current application is tied to the outcome of mandate presentation, which results in inconsistent charge application across accounts.

**Problems Identified**

1. **Missed Charges Due to No Mandate:**
    
    Dishonour charges are **not applied** to users who do not have an active mandate (e.g., revoked mandates), even if they miss their due date.
    
2. **Incorrect Charges Despite Repayment:**
    
    Users who have already paid their dues manually

**Solution:**
?**

To make the application of dishonour charges **independent of the mandate presentation process** by introducing a post-due date review mechanism that ensures charges are applied fairly and consistently based on actual repayment behaviour.d

<aside>
⚠️

In case mandate is revoked or does not exist, if the collection amount is less than 10 Rs, it should be waived

</aside>

---

## #135 — LAS CMS Confiscation and sale of securities
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

When securities are lien marked in favour of DSP Finance, it also gives the capability to the NBFC to invoke the lien to redeem the securities, this gives the proceeds from the sale of securities to the NBFC which is posted in the security holder’s loan account.

The following reasons are why there is a need for this capability:

- If the user goes into a shortfall, and is unable to regularise (DP>POS) their loan account within a stipulated time period (7 working days as defined by RBI), the NBFC is required to invoke securities to regularise the account
- If the user is ove

**Solution:**
?**

- **PMR-based validation** – Since no lien verification API is available, removal will rely on accurate and timely ingestion of PMR data.
- **Derived removal requests** – The system will generate internal removal requests from PMR entries and reconcile them against originator-reported transactions.
- **Reconciliation-first approval** – confiscation will only be approved once checker confirms task on Command centre
- **Exception handling** – Any mismatches between pledged securities and PMR entries will be flagged for manual resolution.
- **Lifecycle management**: Management of add collateral request via CMS (Removal)

---

## #136 — LAS LMS Product Note
**Status:** Completed | **Last edited:** Unknown

# LAS LMS Product Note Last Edited: March 16, 2026 4:03 PM PRD Owner: Vaibhav Arora ## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds** --- ### **Overview** This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds). Key principles: - A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**. - **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices. - All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency. --- ## **1. MONEY TRANSACTIONS** --- ### **1.1 Disbursement (Forward + Reverse)** - **Forward Disbursement:** - Triggered post approval and sufficient DP validation (LMS) - RMS validates real-time prices (every 15 minutes). - LMS validates EOD price consistency - Both systems must independently confirm DP sufficiency. - On success: disbursement request is sent to TSP; loan status updated. (Cashfree) - **Reverse Disbursement:** - Used in cases of failed payout - Transaction reversed, collateral DP recalculated. --- ### **1.2 Repayment (Forward + Reverse)** - **Forward Repayment:** - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA) - LMS receives repayment; validates against due and excess amounts. - **Reverse Repayment:** - Applicable when repayment fails due to banking errors or incorrect credit. - LMS adjusts ledger and reverses credit. --- ### **1.3 Excess Refund** - LMS calculates overpayment (e.g., duplicate repayment, excess interest). - Refund is initiated after checking **updated DP position** via (RMS + LMS) - Final payout initiated via TSP only when RMS confirms buffer post-refund. --- ### **1.4 Charge Application (Forward + Waiver + Refund)** - **Forward:** - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers. - **Waiver:** - Ops-triggered waiver requests. - **Refund:** - Charge reversed, and refund processed. (Credit note) --- ## **2. SERVICING** --- ### **2.1 Closure** - Triggered after full repayment and complete collateral release. - LMS validates: - Zero principal (LMS) - No pending charges (LMS) - No open collateral pledges (CMS) - Closure confirmation sent to DP, TSP, and customer. --- ### **2.2 Renewal** - Applicable for LAMF/LAS products with fixed-term limits. - At maturity, a renewal window opens. --- ### **2.3 Mobile / Email / Bank Account Update

---

## #137 — LMS Multiple sell off requests
**Status:** Completed | **Last edited:** Unknown

# LMS: Multiple sell off requests Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time. Operationally, this breaks in real-world scenarios where: - Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level - Failed invocations do not cover the **entire overdue or shortfall** - Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed). This leads to: - Manual workarounds by the engineering team to support the use case - Delays in curing shortfall / overdue - Risk of exposure breach if sell-off cannot be retriggered in time - Risk of incorrect updates by the engineering team --- ## 2. Problem Statement **Ops raises a sell-off request for multiple securities.** - Some invocations succeed - One or more invocations fail or get stuck (e.g. CAMS / KFIN issues) - Proceeds received are **insufficient to cover the shortfall** - System blocks Ops from raising another sell-off request due to an existing non-terminal request This creates a deadlock where: - Exposure remains unresolved - Ops cannot act despite legitimate need - Manual intervention becomes necessary --- ## 3. Current Sell-Off Flow (As-Is) 1. **Sell-off Initiation** - Ops raises sell-off via **Bulk Maker** at **collateral level** - Requests are consolidated at **loan level** - A single sell-off request is created per loan 2. **Blocking Logic** - Selected units are blocked in LMS - Blocked units stop contributing to **Drawing Power (DP)** 3. **Threshold Calculation** ``` AvailableThreshold= DP - POS - COS - IOS - Accrued Interest ``` - Blocking ensures: - No excess collateral release - No further disbursement beyond safe exposure 4. **Invocation Flow** - RTA APIs (CAMS / KFIN) invoked - RTAs pass requests to AMCs - AMC sells securities 5. **Settlement & Reconciliation** - Proceeds credited to NBFC bank account - Settlement TAT: 2–3 working days - Ops reconciles proceeds via bulk operation - Proceeds mapped to collateral sell-off requests - Amount posted to respective loan accounts in LMS --- ## 4. Key Issue in Current Design - System enforces **single non-terminal

---

## #138 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #139 — PPSL UPI mandate presentation
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
The scope of this enhancement includes:

- Supporting UPI mandate registration through PPSL for PayTM-originated users
- Enhancing LOS mandate registration APIs to support explicit provider tagging
- Allowing PayTM to explicitly pass `provider = PPSL`
- Persisting provider information within LOS
- LMS consuming provider metadata from LOS
- LMS routing mandate presentation based on provider
- Suppo

# PPSL UPI mandate presentation Last Edited: May 25, 2026 10:00 PM PRD ETA: May 25, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** PayTM currently uses the existing DSP Finance (Fenix) mandate registration and presentation stack for both NACH and UPI mandates, where mandate registration is facilitated via Digio and mandate presentation is managed through DSP Finance workflows. PayTM intends to migrate mandate registration for a subset of users to the internal PPSL mandate stack. The primary motivation behind this change is to significantly improve the end-user registration experience by enabling native invocation of the UPI intent flow directly through the PayTM ecosystem. This removes dependency on external redirection-heavy flows and improves TPAP handoff reliability during mandate registration. Historically, the PPSL UPI mandate presentation workflow differed from the existing Digio-integrated flow: - Digio workflow: - Single consolidated API call - Automatically registers PDN and presents mandate together - Mandatory condition that mandate presentation occurs more than 24 hours in the future - PPSL workflow (earlier implementation): - PDN scheduling and mandate presentation were independent APIs/workflows - Required additional orchestration effort from LMS/LOS PPSL has now aligned its APIs and shared updated documentation enabling the required orchestration compatibility. However, this introduces an operational and technical challenge: - Certain PayTM customers will continue using Digio mandates - New customers may register mandates using PPSL - LMS presentation logic must identify which mandate provider was used during registration to correctly invoke downstream presentation workflows Currently, LOS internally maintains provider mapping through a provider column, however the external mandate registration APIs used by LSPs do not allow explicit provider selection. This creates ambiguity for LMS while determining presentation routing. To solve this, the mandate registration APIs will be enhanced to allow PayTM to explicitly pass the mandate provider during registration. --- # **1. Problem Scope** ## In Scope The scope of this enhancement includes: - Supporting UPI mandate registration through PPSL for PayTM-originated users - Enhancing LOS mandate registration APIs to support explicit provider tagging - Allowing PayTM to explicitly pass `provider = PPSL` - Persisting provider information within LOS - LMS consuming provider metadata from LOS - LMS routing mandate presentation based on provider - Supporting coexistence of: - Legacy Digio mandates - PPSL mandates - Maintaining the existing UPI mandate presentation logic at LMS layer: - Loan account level presentation creation - Collection batch item generation - Existing downstream presentation

---

## #140 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #141 — Product Note Penalty migration to Fenix (Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

This enhancement addresses the following problems.

# Product Note: Penalty migration to Fenix (Colending) Last Edited: April 14, 2026 4:02 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, penal charges for overdue loan accounts are computed by an **automated job in Finflux**. This job runs daily at 4 AM and applies penalties when interest becomes overdue. These charges are stored as **applicable charges in Finflux** and surfaced to downstream systems primarily through foreclosure simulations. This architecture introduces several operational and product limitations. **Who is impacted** - Operations teams - Product and engineering teams - Finance and customer support teams - Borrowers indirectly (through slower issue resolution) **Challenges in the current setup** 1. **Limited product control** Penal charge computation logic currently resides inside Finflux jobs. Any change to the logic requires dependency on Finflux configuration and third party coordination. 2. **Limited configurability** The current implementation applies a **flat penalty of ₹10 per day**, whereas the Key Fact Statement (KFS) requires **slab-based penalty computation based on overdue amount**. (This is a compliance observation) 3. **No operational control** Since penalties are not created as **transactions inside Fenix (internal LMS)**: - Operations cannot **waive or refund penalties directly** - Charge-level audit and tracking are difficult 4. **Colending complexity** In Loan-90 / Loan-10 structures, penalties must be **orchestrated across loan legs**. The Finflux-driven penalty logic does not provide sufficient control to ensure accurate charge allocation across colending loans. 5. **Foreclosure simulation dependency** Foreclosure calculations rely on Finflux charge simulations. This makes enhancements difficult and increases dependency on an external system for a critical borrower-facing calculation (Finflux). Additionally, the current system lacks a **generalised framework for defining and applying loan charges**. Future charges such as **Annual Maintenance Charges (AMC)** or other contingent fees would require ad-hoc implementations. This enhancement addresses these limitations by: - Migrating **penal charge computation to Fenix** - Introducing a **generic Applicable Charges framework** - Enabling **charge-level operational controls** - Supporting **future charge types such as AMC** --- # **1. Problem Scope** ## **In Scope** This enhancement addresses the following problems. ### **Migration of penalty computation to Fenix** Daily penal charge computation will move from **Finflux jobs to Fenix**, eliminating system dependency and enabling full product control. ### **Penalty pricing enhancement** Penalty logic will be enhanced from **flat charges to slab-based pricing**, as defined in the KFS. ### **Minimum overdue threshold** Penalties will only be applied when: Overdue Amount ≥ ₹10 This

---

## #142 — Product note Excess refund Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Enable **excess refund flow compatible with both loan types**:
    - DSP loans (auto-adjust + withdrawal allowed)
    - Co-lending loans (parked excess, no withdrawal)
- Introduce:
    - **Maker-checker flow for excess refunds**
    - **Validation layer to compute refundable excess**
- Enable:
    - Manual refund by Ops
    - Automated daily refund via CRON
- Stakeholders:
    - Primary: Ops, Fi

# Product note: Excess refund Colending Last Edited: April 7, 2026 3:38 PM PRD ETA: March 26, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - NBFC Ops & Finance teams - Customers (end borrowers) - LMS / Payments systems - **What is the challenge** - In the current system: - Excess funds in a loan are: - **Auto-adjusted against dues** - **Available for withdrawal** - However, in **co-lending loans**: - Excess: - **Cannot be used for withdrawal** - **Cannot auto-adjust against dues (parked excess)** - This creates: - Customer dissatisfaction (funds blocked) - Operational dependency on batch refunds - Regulatory and reconciliation sensitivity (escrow flows) - **Why is it important** - Excess funds belong to the borrower → must be returned timely - Blocked excess reduces trust and impacts CX - Co-lending construct mandates **controlled fund flows** - Need a **unified system** that works for both: - DSP 100% loans - Co-lending loans --- ## **1. Problem scope** ### In scope - Enable **excess refund flow compatible with both loan types**: - DSP loans (auto-adjust + withdrawal allowed) - Co-lending loans (parked excess, no withdrawal) - Introduce: - **Maker-checker flow for excess refunds** - **Validation layer to compute refundable excess** - Enable: - Manual refund by Ops - Automated daily refund via CRON - Stakeholders: - Primary: Ops, Finance - Secondary: Customers --- ### Out of scope - Enabling: - Real-time auto-adjustment of excess for co-lending (future scope) --- ## **2. Success Criteria** ### Key outcomes - **Timely refund of excess** for co-lending loans - **Zero incorrect refunds** (over/under refund) - Reduced dependency on manual ops intervention ### Metrics - % excess refunded within T+1 (target: >95%) - Excess refund error rate (target: <1%) - Manual intervention rate (should reduce over time) ### Post-launch good state - Excess: - Not withdrawable (co-lending) - Automatically refunded via system or ops - Ops: - Can trigger instant refunds via maker-checker ### Guardrails - No: - Over-refunding beyond eligible excess - Refunds during foreclosure / invalid states - Impact on repayment posting / accounting --- ## **3. Solution Scope** ### Solution overview We will introduce a **unified excess refund framework** with: - **Validation engine** → determines refundable excess - **Maker-checker flow** → enables controlled manual refunds - **Daily CRON** → ensures timely automated refunds System behavior will differ based on loan type: - DSP loans

---

## #143 — Product note Foreclosure (Colending)
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure (Colending) Last Edited: May 19, 2026 2:47 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across **Loan 90 and Loan 10 in the Colending Loan Management System (CLMS)**. ### Who is impacted - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting ### What is broken today Foreclosure today largely operates based on **Loan 100 balances**, while the actual liabilities exist across **Loan 90 and Loan 10**. This creates several limitations: 1. **Incorrect foreclosure simulation** Foreclosure amounts may be computed using only Loan 100 data without validating Loan 90 and Loan 10 balances. 2. **Pending transaction inconsistencies** Foreclosure may be initiated even when **pending transactions exist in CLMS**, leading to inaccurate payoff calculations. 3. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring that: - Loan 90 and Loan 10 are closed - All charges and interest are posted - Excess settlement is completed 4. **Penalty and applicable charge dependency** Applicable charges (such as penal charges) may be applied after repayment due to **daily charge jobs**, which may cause foreclosure attempts to fail if charges are posted after repayment. 5. **Incorrect collateral release timing** Securities may be released before confirming that **both loan legs are closed**, which introduces risk. ### Why this is important Foreclosure is a **regulatory and customer-sensitive workflow**. Incorrect sequencing may lead to: - Incorrect payoff amounts shared with borrowers - Operational rework due to partial closures - Accounting mismatches across loan legs - Risk of releasing collateral before loan closure creating financial exposure for the NBFC This PRD defines a **colending foreclosure workflow** that ensures: - Correct payoff simulation - Transaction sequencing across loan legs - Controlled collateral release - Accurate excess settlement. --- # **1. Problem Scope** ## **In Scope** ### **Colending foreclosure simulation** Foreclosure simulation will incorporate balances from: - Loan

---

## #144 — Product note Foreclosure V2 for Colending
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure V2 for Colending Last Edited: April 24, 2026 7:43 AM PRD ETA: April 7, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across Loan 90 and Loan 10 in the Colending Loan Management System (CLMS). --- ### **Who is impacted** - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting --- ### **What is broken today** 1. **Incorrect foreclosure simulation** Foreclosure amounts are often computed using Loan 100 without fully reconciling Loan 90 and Loan 10 balances. 1. **Pending transaction inconsistencies** Foreclosure may be initiated even when pending transactions exist in CLMS, leading to incorrect payoff calculations. 1. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring: - Loan 10 and Loan 90 are closed - All dues and interest are settled - Excess is correctly handled 1. **Penalty and applicable charge dependency** Charges (such as penal charges) may be posted after repayment due to system jobs, leading to foreclosure failures. 1. **Incorrect collateral release timing** Collateral may be released before confirming closure of underlying loan legs. 1. **Excess handling gap in colending** - Excess is parked in Loan 100 - Excess does not auto-settle dues or accrued interest - There is no native way to use excess during foreclosure This leads to: - Incorrect net payable shown to users - Failed foreclosure despite sufficient excess - Manual intervention for settlement - Reconciliation gaps --- ### **Why this is important** Foreclosure is a **high-intent and customer-sensitive journey**. Incorrect handling leads to: - Poor customer experience - Increased operational workload - Financial and accounting mismatches - Risk of incorrect collateral release This PRD ensures: - Accurate payoff computation - Deterministic transaction sequencing - Proper utilization of excess - Correct closure and refund handling --- # **1. Problem Scope** ## **In Scope** ### **1. Colending foreclosure simulation** Foreclosure simulation will compute payoff using: -

---

## #145 — Product note Interest rate change handling
**Status:** Pending review | **Last edited:** Unknown

# Product note: Interest rate change handling Last Edited: March 19, 2026 9:51 PM PRD ETA: March 19, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** In the current co-lending construct between DSP (NBFC) and TCL (co-lender), loans are originated and managed across multiple representations within the LMS: - **Loan 90 (TCL Book):** Represents TCL’s capital contribution and is controlled externally by TCL, including interest rate decisions. - **Loan 10 (DSP Book):** Represents DSP’s capital contribution and follows DSP’s internal benchmark and pricing logic. - **Loan 100 (Customer-facing Loan):** A composite loan created in the LMS, reflecting the borrower’s obligation and used for repayment schedules, accruals, and customer communication. The effective interest rate for the borrower is derived as a **weighted average of the underlying lender rates based on capital contribution**: - 90% → TCL (Loan 90) - 10% → DSP (Loan 10) However, from a system and implementation perspective: - The LMS treats **Loan 100 as an independent loan** with its own benchmark and ROI. - Interest rates are currently configured using **benchmark + spread constructs defined at an organizational level**. - There is **no native support for dynamic weighted rate computation** across multiple lender loans within the LMS. --- ### **Problem Statement** As part of ongoing co-lending operations: 1. **Independent Rate Changes by Lenders** - TCL may revise its interest rates (benchmark or spread) independently. - DSP may also revise its own benchmark rates. - These changes directly impact the **effective blended ROI** applicable to the borrower. 2. **Lack of Native Synchronization** - Since Loan 90, Loan 10, and Loan 100 are maintained separately: - Rate changes in Loan 90 (TCL) do not automatically reflect in Loan 100. - Loan 100 must be **manually or systematically updated** to maintain parity with the blended rate. 3. **Risk of Misalignment** - If Loan 90 and Loan 100 are not updated in sync: - Incorrect borrower interest may be charged. - Accruals and repayment splits between lenders may become inconsistent. - Downstream systems (accounting, reconciliation, reporting) may break. 4. **Operational Complexity** - Current benchmark configuration is **organization-wide**, not contract-specific. - With multiple co-lending partners, each having: - Different benchmarks - Different spreads - Different rate change cycles → A single benchmark approach does not scale. --- ### **Constraints** - Loan 100 **must exist as a physical loan in the LMS** and cannot be treated as a derived construct. - LMS

---

## #146 — Product note Razorpay PG integration Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Enable **dynamic MID selection** for PG repayments:
    - Colending loans → escrow-linked MID (at a contract level - Makes it extendable to multiple MIDs for multiple colending relationships)
    - Non-colending loans → DSP MID
- Store:
    - **MID at contract level**
- Fetch:
    - API credentials via **secret manager (not stored directly)**
- Ensure:
    - All Razorpay operations use the **sam

# Product note: Razorpay PG integration Colending Last Edited: April 7, 2026 3:38 PM PRD ETA: March 26, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - NBFC (DSP) – Product, Engineering, Finance - Co-lenders (e.g., TCL) - Payment partner (Razorpay) - LSPs (Volt) and end customers - **What is the challenge** - Current PG integration uses a **single MID (merchant account)** for all repayments - For **co-lended loans**, regulations require: - Funds to be collected directly into a **designated escrow account** - In Razorpay: - **MID determines settlement account** - Each MID has **separate API credentials** - System today: - Does not differentiate between **colending vs non-colending loans at MID level** - **Why is it important** - Regulatory requirement → escrow-based fund flow - Incorrect MID usage → funds settle to wrong account - Breaks reconciliation and lender settlement - Scaling issue → multiple co-lenders = multiple MIDs --- ## **1. Problem scope** ### In scope - Enable **dynamic MID selection** for PG repayments: - Colending loans → escrow-linked MID (at a contract level - Makes it extendable to multiple MIDs for multiple colending relationships) - Non-colending loans → DSP MID - Store: - **MID at contract level** - Fetch: - API credentials via **secret manager (not stored directly)** - Ensure: - All Razorpay operations use the **same MID context**: - Order creation - Payment fetch - Payment validation - Stakeholders: - Primary: Engineering, Finance - Secondary: Razorpay, LSPs --- ### Out of scope - Changes to: - Razorpay API contracts (no change) - SDK integration at frontend (Volt continues as-is) - Multi-MID fallback logic within a single contract - Changes to repayment lifecycle or LMS posting --- ## **2. Success Criteria** ### Key outcomes - **100% correct routing of PG funds** to escrow for colending loans - **Zero reconciliation issues** due to incorrect MID usage - Seamless experience for LSP and end user (no UX changes) ### Metrics - % of PG transactions using correct MID (target: 100%) - Payment success rate (no degradation post rollout) - Reconciliation mismatches due to MID errors (target: 0) ### Post-launch good state - MID selection is: - Fully automated - Invisible to end user - All Razorpay flows work unchanged ### Guardrails - No increase in: - Order creation failure rate - Payment verification failures - API latency --- ## **3. Solution Scope** ###

---

## #147 — Product note Virtual account handling for Colendin
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Enable **dynamic credit account routing** for VA collections based on:
    - Loan → Contract → Escrow account mapping
- Enhance **Validate API response** to return:
    - Correct **credit account (escrow / DSP account)**
- Support:
    - Colending loans → Escrow routing basis contract configuration
    - Non-colending loans → DSP account routing
- Store and manage:
    - **Contract-level credit 

# Product note: Virtual account handling for Colending Last Edited: April 7, 2026 3:38 PM PRD ETA: March 25, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - NBFC (DSP) – Product, Ops, Finance teams - **What is the challenge** - In the current Virtual Account (VA) setup, all repayments are credited to a **single DSP collection account** - However, for **co-lended loans**, regulations mandate that: - Funds must flow into a **designated escrow account** (not DSP’s own account) - Yes Bank’s existing integration: - Identifies VA → calls our **Validate API** - Credits funds to a **pre-configured account** - This creates a gap: - System today does **not dynamically decide the destination account** - No linkage between **loan → colending contract → escrow account** - **Why is it important** - Regulatory non-compliance if funds are credited to incorrect accounts - Incorrect fund flows → breaks lender settlement and reconciliation - Operational risk → manual reversals, audit failures - Scaling issue → multiple co-lenders require dynamic routing --- ## **1. Problem scope** ### In scope - Enable **dynamic credit account routing** for VA collections based on: - Loan → Contract → Escrow account mapping - Enhance **Validate API response** to return: - Correct **credit account (escrow / DSP account)** - Support: - Colending loans → Escrow routing basis contract configuration - Non-colending loans → DSP account routing - Store and manage: - **Contract-level credit account mapping (DSP 100% should also be a contract)** - Stakeholders: - Primary: Ops, Finance, Lending Systems - Secondary: Yes Bank, LSPs, Customers --- ### Out of scope - Changes to: - VA generation logic (e-collect code remains same: 301301) - Checker workflows (remain unchanged), credit account should be added as a parameter in the checker task - Notify API structure (only extended usage, not redesigned) - Advanced validations: - Name match, whitelist accounts (Currently live - Remains unchanged) - Multi-account routing within a single contract - One contract can have one bank account as part of the proposed set up. --- ## **2. Success Criteria** ### Key outcomes - **100% compliance** with escrow routing for co-lending loans - **Zero misrouted transactions** (DSP vs Escrow) - **Seamless bank integration** without additional retries/failures ### Metrics - % of VA transactions correctly routed to escrow (target: 100%) - Validate API success rate (pass rate without checker approval > 98%) - Reconciliation

---

## #148 — Razorpay SDK enhancement for Colending
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

- Unified Razorpay integration across:
    - DSP loans
    - Colended loans
- Support for:
    - SDK-based flow
    - Payment link flow
- Dynamic resolution of:
    - MID
    - Razorpay client_id
- Contract-level PG configuration
- Frontend enablement for SDK invocation

**Primary users**

- LSP engineering teams (Volt FE + BE)
- DSP LMS / PG systems

**Secondary users**

- End customers
- Ops

# Razorpay SDK enhancement for Colending Last Edited: April 22, 2026 6:29 PM PRD ETA: April 22, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** Today, LSPs (e.g. Volt, CRED, PhonePe) can integrate with DSP for repayments via multiple payment gateway (PG) options: - DSP internal PG - Razorpay - Cashfree - Native PG managed by LSP (direct settlement) ### **Current Challenge** With **colending**, regulatory guidelines mandate: - Funds must flow into **escrow accounts** - This leads to **different MIDs**: - DSP loans → DSP current account MID - Colending loans → Escrow MID For Razorpay SDK: - `client_id` is tied to MID - SDK invocation becomes **MID dependent** ### **What is broken today** - LSPs need **loan-type aware logic** - Multiple client IDs → complex integration - Breaks abstraction: > DSP vs Colending loans should be indistinguishable > ### **Why this matters** - Colending is a key growth lever - Repayment friction directly impacts: - Conversion - Partner experience - Slows onboarding of new LSPs --- ## **1. Problem Scope** ### **In scope** - Unified Razorpay integration across: - DSP loans - Colended loans - Support for: - SDK-based flow - Payment link flow - Dynamic resolution of: - MID - Razorpay client_id - Contract-level PG configuration - Frontend enablement for SDK invocation **Primary users** - LSP engineering teams (Volt FE + BE) - DSP LMS / PG systems **Secondary users** - End customers - Ops / reconciliation teams --- ### **Out of scope** - Supporting multiple PGs for colending (Razorpay only) - Changes to settlement / reconciliation - Native LSP PG flows --- ## **2. Success Criteria** ### **Primary outcomes** - Single integration for all loan types - SDK invocation fully abstracted - No increase in payment failures ### **Post-launch good state** - 100% repayments via unified API - No loan-type branching at LSP - 99.9% uptime ### **Guardrails** - No reconciliation mismatch - No incorrect MID usage - No increase in disputes --- ## **3. Solution Scope** ### **Solution Overview** Introduce **contract-driven PG abstraction** where: - `create repayment order API` determines: - PG (Razorpay) - MID - client_id - LSP consumes a **single API** - SDK invocation is **agnostic to loan type** --- ### **Core Design** ### **1. API Enhancement** **Endpoint** ``` POST /repayment/order/v1 ``` **Enhancements** - Add: `paymentGateway` - Populate: `paymentGatewayOrderId` (for SDK) --- ### **2. Contract-Level Configuration** | Field | Description | | ---

---

## #149 — Risk management system LAS
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

For loans against collateral with dynamically priced assets like:

- Shares
- Mutual funds

It becomes important to ensure that all transactions and exposure given out to user against loans committed by the NBFC, are validated. As of now only the LMS was responsible for doing these validations, but as our systems and products get more complex, there is an additional need for a separate system with logic separation to validate all transactions.

Traditionally, validation of disbursals, top-ups, sell-offs, or withdrawals was handled solely within the LMS (Loan Management Syste

**Solution:**
?**

The RMS module performs the following responsibilities:

- Ingest and store market data for all pledged securities every 15 minutes.
- Compute real-time LTV (Loan-to-Value) and exposure metrics using pledged quantity and live prices.
- Raise alerts for LTV or exposure breaches.
- Raise alerts to customers on exposure breaches
- Validate user transactions that may impact risk thresholds—like disbursals, release requests, or sell-offs—against real-time metrics before allowing execution.

---

## #150 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #151 — Tally ERP Integration
**Status:** Completed | **Last edited:** Unknown

# Tally ERP Integration Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # **Tally Journal Voucher API Contract (Sample Document)** This document outlines the proposed API contract for pushing journal voucher entries from the LMS/ERP system to Tally. Each journal voucher corresponds to a single **transaction event**, containing one or more **ledger-level debit/credit lines** with consolidated amounts. --- ## **1. API Overview** ### **Endpoint** (To be shared by the vendor) ### **Purpose** Push a complete journal voucher entry at a transaction type level to Tally for accounting purposes. --- ## **2. Request Structure (Batch Journal Posting)** The API will support **batch posting** of journal vouchers. Each request will contain an **array of transactions**, where each object represents one complete journal voucher. ### **2.1 Journal Voucher Batch Payload** ```json [ { "transaction_type": "string", "narration": "string", "voucher_date": "YYYY-MM-DD", "tally_txn_id": "1234564534432", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" } ] }, { "transaction_type": "string", "narration": "string", "tally_txn_id": "1234564534433", "voucher_date": "YYYY-MM-DD", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" }, { "ledger_name": "Sample3", "debit": "number", "credit": "number" } ] } ] ``` --- ### **Field Description** | Field | Type | Description | | --- | --- | --- | | transaction_type | string | Preconfigured transaction type (ex: PAYIN, PAYOUT) | | tally_txn_id | string | Unique transaction identifier used as **dedupe key** | | voucher_date | date | Voucher posting date | | narration | string | Narration mapped to transaction type | | ledger_entries | array | List of debit/credit ledger lines | --- ### **Ledger Entry Object** | Field | Type | Description | | --- | --- | --- | | ledger_name | string | Name of the ledger in Tally | | debit | number | Amount debited (zero if not applicable) | | credit | number | Amount credited (zero if not applicable) | --- ## **3. Transaction Type Samples** Below are examples for each transaction type based on provided data. --- ## **3.1 ADD_FEE** **Narration:** Being fee income recognition ```json { "tally_txn_id": "<unique-id>", "transaction_type": "ADD_FEE", "voucher_date": "2025-01-01", "narration": "Application of fee on loan account", "ledger_entries": [ {"ledger_name": "Fees receivable", "debit": 7109825, "credit": 0}, {"ledger_name": "Income from Fees", "debit": 0, "credit": 6025269}, {"ledger_name": "CGST Payable", "debit": 0, "credit": 90382}, {"ledger_name": "SGST Payable", "debit": 0, "credit":

---

## #152 — Term loan gaps
**Status:** Unknown | **Last edited:** Unknown

# Term loan gaps Last Edited: July 24, 2025 5:10 PM PRD Owner: Vaibhav Arora ### **Spend & Convert Enhancements** - Support for **flat PF (Processing Fee)** values in spend and convert requests. - Allow **knockoff remarks** to be passed in the spend and convert payload. - Support passing **different charge types** and **collecting multiple charges** in a single spend and convert request. --- ### 🧾 **Repayment Logic** - Enable both **loan-level and line-level repayments** to co-exist for term loans. - Mark **repayment at loan level** as a current **gap** in configuration. - Support **EMI-level repayments**. - Include **apportionment details** in the repayment response (internal checks needed). - Support **loan-level excess refunds**. - **Excess amounts**: - Should remain **parked** after due generation (do not auto-settle dues via FIFO). - At **line level**, should **increase available limit**. --- ### 🧮 **Due/Bill Generation** - Bills should be generated **independent of the due generation job**—on demand. --- ### 📆 **Schedule and Simulation** - Provide a **preview schedule API** without needing to create a line. - Enable **tranche-level simulation API** for a given date. - All **date fields** must be passed as **EPOCH timestamps**. --- ### 🧠 **Tagging & Status Configurations** - SMA tagging should be **configurable**. - **NPA to be tracked at client level**, while **SMA is tracked at loan level**. --- ### 📉 **Interest & Limit Management** - Support **interest rate updates** on loans. - **Limit replenishment** should only occur when the **underlying loan is fully closed**, whether via EMI or part-payment.

---

## #153 — Transaction Sequencing & Transaction Workflows for
**Status:** Completed | **Last edited:** Unknown

**In scope:**
This document defines the **transaction orchestration logic across all supported transaction types**.

Specifically it covers:

# Transaction Sequencing & Transaction Workflows for Co-Lending LMS Last Edited: March 19, 2026 9:44 PM PRD ETA: March 10, 2026 PRD Owner: Vaibhav Arora # Background and Context DSP Finance is implementing a **co-lending structure between DSP and TCL** where a single customer loan is operationally represented by **three loan accounts inside the LMS**. The loan accounts are structured as follows: - **Loan 100** → Customer facing orchestration loan (Finflux) - **Loan 90** → TCL lender loan (Swiffy LMS) - **Loan 10** → DSP lender loan (Finflux) All **customer-facing interactions and repayments occur on Loan 100**, while lender accounting and settlement must be reflected in the **individual lender loan books**. This PRD introduces the need for **systematic orchestration across multiple loan books** to ensure: - lender accounting reconciliation - schedule consistency - correct split of repayments - ransaction ordering - correct DP (Drawing Power) management --- ### Transaction Categories The system processes two categories of transactions. --- ## Money Transactions These impact loan balances or receivables. Examples: - Disbursement - Repayment - Refund / Disbursement reversal - Charge application - Charge knock off - Interest posting - Credit note adjustments - Waivers - Excess payment handling - Excess refunds - Clear dues transactions --- ## Collateral Transactions These impact collateral and **DP calculations**. Examples: - Add collateral - Remove collateral - Sell-off collateral Collateral operations may also **trigger money transactions**, such as: - Margin pledge charges - Invocation charges - Repayment from sell-off proceeds --- # Current Challenge The LMS currently processes transactions **independently per loan account** without orchestration across lender books. This introduces several operational risks in a co-lending structure. --- ## 1. Transaction Ordering Risk Example sequence: Repayment → Interest posting → Charge posting If these are processed **in different orders across lender loan books**, the share calculations become inconsistent. --- ## 2. Money Flow vs Accounting Mismatch Customer funds move through **escrow accounts**, while lender receivables are maintained in the LMS. Without deterministic orchestration: - escrow balances may move - lender books may not reconcile --- ## 3. Collateral and Money Transaction Race Conditions Example: Sell-off collateral and repayment arriving simultaneously. This may result in: - incorrect DP recalculation - incorrect sell-off triggers - incorrect available limit. --- ## 4. Partial Transaction Failures Example: Loan 100 disbursement succeeds but lender loan posting fails. This creates **partial system states** that break reconciliation. --- # Why Solving This

---

## #154 — Volt - Overdue Communication Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
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
    - lender sell-off timelin

# Volt - Overdue Communication Enhancement Last Edited: April 3, 2026 11:14 AM PRD ETA: March 9, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Volt Money sends overdue payment alerts to customers when **interest dues are not paid by the scheduled repayment date** for their Loan Against Mutual Funds (LAMF). These communications are sent across: - SMS - WhatsApp - Email The purpose of these communications is to ensure customers are aware that: - Their **interest payment is overdue** - **Penal charges are being applied** - Failure to repay may lead to **portfolio sell-off by the lender** Currently, the communication does not clearly encourage customers to **make payment before the lender sell-off deadline**, which can result in customers attempting payment **on the last day**. Because payment settlement may take time, last-day payments can still result in **security sell-off**, leading to: - Customer confusion - Customer disputes - Increased support queries Additionally, communications do not explicitly guide customers to **make payment at least one day prior to the sell-off date**. To improve clarity and reduce disputes, Volt will update overdue communications to **explicitly instruct customers to make payment at least one day before the lender sell-off date**. **Important:** This enhancement will apply **only to DSP as a lending partner** and will **not apply to BFL or TCL portfolios**. --- # **1. Problem Scope** ## In scope The following enhancements are included in this release: - Update overdue communication copies to include **clear repayment instructions** - Explicitly instruct customers to **pay at least one day before the sell-off date** - Update communication templates across: - SMS - WhatsApp - Email - Improve clarity around: - overdue payment - penal charges - lender sell-off timeline Primary users: - Customers with **interest overdue on Volt Money LAMF accounts** Secondary users: - Customer support teams handling repayment queries - Risk and collections teams managing overdue accounts --- ## Out of scope The following items are not included in this enhancement: - Changes to **overdue calculation logic** - Changes to **sell-off trigger logic** - Changes to **penal charge calculation** - Changes to **repayment workflows in the Volt app** - Changes to overdue communications for **BFL and TCL portfolios** Rationale: This initiative focuses only on **communication clarity improvements**, without modifying underlying **collections or risk processes**. --- # **2. Success Criteria** ### Primary Outcomes **1. Reduce disputes during sell-off events** Customers clearly understand the **repayment deadline

---

## #155 — Volt - Shortfall Communication Enhancement – Due D
**Status:** Completed | **Last edited:** Unknown

**In scope:**
The following enhancements are included in this release:

- Replace **“days left” communication with an explicit due date**
- Introduce **due_date variable in shortfall communications**
- Update communication templates across:
    - SMS
    - WhatsApp
    - Email
- Introduce **penultimate-day reminder communication**
- Validate and align **overdue date logic with DSP implementation**
- Encourage r

# Volt - Shortfall Communication Enhancement – Due Date Based Messaging Last Edited: March 31, 2026 11:28 AM PRD ETA: March 9, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, Volt Money sends **shortfall alerts using a “days remaining” format** in SMS, WhatsApp and Email communications. **Who is facing the problem** - Customers with active **Loan Against Mutual Funds (LAMF)** accounts experiencing shortfall - Volt **customer support team** - Volt **risk and operations teams** **What is the challenge today** Shortfall communications currently mention the **number of days left to resolve the shortfall**, instead of clearly communicating the **exact last date by which the account must be regularised**. This creates confusion because: - Customers interpret the timeline differently - Customers attempt repayment **on the last day** - Payments may **not settle in time**, triggering **collateral sell-off** This results in customers contacting support claiming they **were not aware of the final resolution deadline**. **Why this is important** - RBI regulations require the **RE to regularise the account within 7 days of shortfall** - Operationally, customers must repay **before the deadline** to allow settlement - Current communication format leads to: - Increased **customer support queries** - Poor **customer experience during sell-offs** - Higher **dispute probability** To improve clarity, Volt will move from **“days remaining” communication to a clear due-date based communication format**. --- # **1. Problem Scope** ## In scope The following enhancements are included in this release: - Replace **“days left” communication with an explicit due date** - Introduce **due_date variable in shortfall communications** - Update communication templates across: - SMS - WhatsApp - Email - Introduce **penultimate-day reminder communication** - Validate and align **overdue date logic with DSP implementation** - Encourage repayment **before the due date** to allow processing time Primary users: - Customers with shortfall in their Volt Money credit line Secondary users: - Customer support team handling shortfall related queries - Risk and collections teams managing collateral sell-offs --- ## Out of scope The following items are not included in this enhancement: - Changes to **shortfall calculation logic** - Changes to **liquidation timelines** - UI changes inside the Volt customer dashboard Rationale: This initiative focuses only on **communication clarity improvements**, without modifying underlying **risk management processes**. --- # **2. Success Criteria** ### Primary Outcomes **1. Reduce customer confusion during sell-off events** - Reduction in **support tickets related to shortfall deadline confusion** **2. Improve shortfall resolution behaviour** -

---

## #156 — [Platform] Decoupling of dishonour fees with manda
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently our dishonour charge application is coupled with mandate presentation, what that means is basis certain error codes that we get from Digio (presentation vendor), we either apply or do not apply dishonour charges

However that leaves the following gap, for customers where mandate was not registered, and presentation does not happen, we are not able to apply dishonour charges (which should have been applied).

How does scenarios arise where mandate is not registered for the user:

- User revokes existing mandate (cancels)
- User registers via Aadhaar Esign or Physica

**Solution:**
?**

We will be setting up a job on Finflux which will apply dishonour charges (Rs 590 - - 500 + GST) to users with interest overdue on the 8th of next month (Interest for January was posted on 1st Feb and was due on 7th Feb, dishonour fees if applicable will be posted on 8th Feb at 2 AM)

We will remove charge application logic from our mandate presentation workflow, mandate presentation will only post or not post transactions based on the status received from the vendor (extendable to current implementation with PhonePe)

---

## #157 — [Platform] Foreclosure handling to support Volt fo
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

A loan account has the following particulars:

- Charges due
- Penal charges due
- Interest due
- Principal oustanding
- Interest accrued not due
- Excess

Whenever a user makes a repayment, it goes through a set apportionment strategy:

Interest overdue → Charges overdue → Interest due → Charge due → Principal outstanding → Excess

Note that the repayments cannot settle interest accrued as it is not due, interest accrued is posted at the end of the billing cycle (becomes due) and then can be settled either via making repayments or via mandate presentation to the user’s loan

**Solution:**
?**

We will allow the LSP to pass an optional parameter called (Is foreclosure payment) in the create repayment order request.

<aside>
🚨

Please note that we will not be validating the amount (and if it satisfies foreclosure validations) for the account

</aside>

For this repayments, there will be an additional step in the payment workflow for the following validation:

- If Excess amount ≥ Accrued interest and TOS=0, clear dues
- If Excess amount < Accrued interest or TOS≠0 then do not clear dues

<aside>
⚠️

Please note that these payments will not go through a checker approval workflow

</aside>

---

## #158 — [Platform] Mandate collection enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Our LAMF credit line product follows a balloon repayment model, which essentially means that the customer is only obligated to pay the interest as per their principal outstanding (which is accrued daily and posted monthly). 

There are multiple ways through which a user can pay this amount:

- Making a repayment on their lo ch the NBFC automatically deducts the amount from the user’s bank account)

What amount is collected from the user’s account?

- Charges due + Penal charges due + Interest due are collected on the 7th via mandate presentation

As we are a platform, there 

**Solution:**
?**

We will be enhancing our current mandate presentation workflow to support the use case where an LSP will control the mandate presentation for the users and will have the following capabilities:

- Get mandate collection file: Mandate collection file which is generated every month and then approved by the operations team will be available as a file (csv) through a get API (for all eligible loan accounts for presentation) to the LSP with approval status
- Mandate collection posting API: LSP will have the capability to pass the mandate collection response to the user (broadly there can be the following scenarios)
    - Mandate was presented and collected successfully (Success)
    - Mandate was presented but failed (Fail)
    - Mandate was not presented (Pending) - LSP will not call the 

---

## #159 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #160 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #161 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #162 — BRE Phase 2++ Items
**Status:** Unknown | **Last edited:** Unknown

# BRE Phase 2++ Items ## User stories / User flow 1. Customer fetches the funds through MFC or CAMS or KFin from our end on any of the supported assets basis the funds fetched on [app.voltmoney.in](http://app.voltmoney.in) OR 2. Customer visits the Volt [website](https://voltmoney.in/check-loan-eligibility-against-mutual-funds?utm_source=nl&utm_medium=whatsapp&utm_campaign=welcome) to check the eligibility using MFC fetch and fetches the limit after entering the OTP. 3. DSP provides the limit basis the LTV configured at LSP’s end and derives the complete offer amount. 4. LSP calculates the offer amount (drawing power) into below buckets. 1. ≥25K : the BRE runs keeping DSP, BFL and TCL as lender as per the %age configured 2. 10K - 25K: LSP allocates DSP as the sole lender for now 3. <10K: LSP rejects the customer 5. LSP informs the customer on UI that its not eligible if the credit limit is <10K. This will be messaged something like ‘We regret to inform you that you aren’t eligible for a loan at this stage.’ 6. If the customer is eligible with DSP, they proceed with the offer screen (Select credit limit) on the LSP UI. 7. If the eligible lender allocated as per the BRE is BFL or TCL, the flow will continue to next step on the offer screen (Select credit limit) on the LSP UI. | **Parameter** | **Value** | **Comments** | | --- | --- | --- | | Credit limit | ≥ 25000 AND ≤2,00,00,000 | Beta: lower limit will be 25KPost Beta: we will change this to 10K | | Funds whitelisted | As per the DSP approved list | | | Channel | B2C webAndroid appiOS app | Not to be enabled on MFD, MFD platform, B2B partners. Default lender: TATA for Beta. Post beta: DSP | | Split on B2C (≥ 25K) | 10% | This number will be increased as we ramp up post beta | | Split on B2C (10K - 25K) | 100% | Ticket size : 10L. Whitelisted MFDs - phase 1. 100 loans with master checker flag on. | | Split on B2B2C | | Phase 1 - Ticket size : 10L. Whitelisted MFDs. 100 loans with master checker flag on.Phase 2 - Remove checkers for repayment and withdrawal upto 10L. QC/Ops. Whitelisted MFDs upto 50% of volumes. No age deviations. 1000 loans.Phase 3 - B2C with checkers as Phase 2. B2B2C - 100% (need to take a call

---

## #163 — problems
**Status:** Unknown | **Last edited:** Unknown

# /problems To effectively document the problems you’re facing with **Wati**, **Exotel**, **Zendesk**, and **1. Wati (WhatsApp Integration)** **Problem**: Lack of visibility and tracking of WhatsApp communications • **Details**: Wati handles a high volume of inbound customer queries, but there is no systematic way to track query status (open, pending, resolved). This leads to issues where agents miss or forget to follow up on important customer queries. • **Impact**: Queries often go unresolved, causing delays in customer service and frustrating customers, particularly MFDs who rely on quick resolutions to onboard and serve their clients. • **User Story**: *As an agent, I am overwhelmed by the volume of WhatsApp messages coming in. There is no mechanism to mark whether I’ve responded to a message or if it’s still unresolved, which leads to missed follow-ups and unhappy customers.* **2. Exotel (Call Management)** **Problem**: Inefficient call tracking and follow-up system • **Details**: Exotel manages inbound calls, currently there is a manul batch process to send the list of the customer with missed calls to support team to reachout through Exotell portal. we need more real time way to track whether queries have been resolved after a missed calls. Agents cannot easily see if the customer issue requires follow-up or if it has been addressed fully during the initial call. • **Impact**: Critical customer issues often require additional attention but get lost after the first call, resulting in unresolved problems, repeat calls, and customer dissatisfaction. • **User Story**: *As an agent, I receive many customer calls, but there’s no system to track whether their issues were fully resolved. Without follow-up reminders or logs, important cases are forgotten, and customers have to call back multiple times.* **3. Zendesk (Ticketing System)** **Problem**: Fragmented ticketing and lack of SLA tracking • **Details**: While Zendesk manages tickets across multiple channels (email, chat, etc.), it does not integrate well with other tools like Wati or Exotel. This leads to fragmented reporting and ticketing, where some queries are logged in Zendesk but others (from WhatsApp or calls) are not. Additionally, there is no clear tracking of SLAs for different customer segments (e.g., MFDs vs. direct customers). • **Impact**: Incomplete visibility of customer queries and SLA breaches result in delays, lost tickets, and poor prioritization of high-value customers. • **User Story**: *As a service manager, I cannot track SLAs for different customer types, which leads to some high-priority issues being neglected.

---

## #164 — SEO Text
**Status:** Unknown | **Last edited:** Unknown

# SEO Text A Loan against mutual funds (LAMF) allows you to borrow money by using your mutual fund units as collateral. Volt Money’s loan against mutual funds calculator can help you estimate the interest costs associated with this financing option. **What is a loan against mutual funds (LAMF)?** A loan against mutual funds (LAMF) is a secured loan where you pledge your mutual fund units as security to borrow money. The lender will determine the maximum loan amount you can qualify for based on a Loan-to-Value (LTV) ratio. This ratio represents the percentage of your mutual fund's market value that the lender is willing to lend against. You are then issued a credit limit which functions like a bank overdraft facility, where you are charged interest only on the amount you withdraw from this credit limit. **How to get a loan against mutual funds?** With Volt Money, you can get loan against mutual funds in 4 simple steps: 1. Check credit limit: We’ll evaluate your mutual fund portfolio & confirm credit limit. Check your credit limit from here. 2. Instant KYC: Complete digital KYC process. No paperwork required! 3. Pledge your assets: Mark your mutual funds as a security with a trusted lender. 4. Withdraw money: Withdraw & repay as per you requirement. No hidden charges. **How interest is calculated on loan against mutual funds?** Loan against mutual fund works like a bank overdraft limit, where you are only charged interest on the amount you withdraw. Interest is calculated daily and is deducted on a particular date every month. Interest calculation works on the following formula: Daily interest = P*(R/365) Monthly interest = Daily interest*N P = Principal outstanding on the day R = Annual rate of interest N = Number of days in a month Example: Suppose you withdraw ₹50,000 from Volt Money credit line at an interest of 10.49%. The daily interest rate would be calculated as (10.49% / 365) = 0.0287% per day. If the limit is utilized for 30 days, the interest accrued would be: *Interest = ₹50,000 × 0.0287% × 30 = ₹43.05* You can also make part payments to reduce your principal outstanding and thus reducing your interest payable. **Why Volt money’s overdraft like credit limit is better than a loan?** 1. Flexibility: With Volt money’s credit limit, you only pay interest on the amount you actually use, and you can repay it

---

## #165 — Volt Ops Requirements The child ticket will be cre
**Status:** Unknown | **Last edited:** Unknown

# Volt Ops Requirements The child ticket will be created and assigned to Volt Ops. Ticket Schema: The ticket can be replicated with a click using the option of Capture properties from parent ticket. Additional Tags required are as follows, and the mapping against the parent tags: | **Parent Tag** | **Child Tag** | | --- | --- | | account_opening | 1. pending_account_opening2. account_opening_/_lodgement_delayed | | lodgement | 1. pending_lodgement2. lodgement3. lodgement_issue4. account_opening_/_lodgement_delayed | | enhancement | 1. pending_account_enhancement 2. pending_enhancement | | disbursal | 1. pending_disbursal2. withdrawal_issue3. withdrawal_rejected4. unable_to_place_withdrawal5. manual_manual_disbursement | | foreclosure | 1. unable_to_submit_foreclosure2. foreclosure3. foreclosure_pending4. foreclosure_success_but_account_not_closed5. expired_loan | | lien_removal | 1. foreclosure_success_but_lien_not_removed2. lien_removal3. unable_to_submit_lien_removal4. lien_removal_pending5. lien_removal_success_but_lien_not_removed | | repayment | 1. repayment_issue2. repayment_not_accounted3. offline_repayment4. repayment_screen_not_opening | | service_request | 1. servicerequest-others2. service_request3. interest_certificate4. interest_calculation5. noc6. excess_refund | | details_update | 1. details_update2. customer_details_update3. bank_account_update4. email_id_update5. phone_number_update | | voluntary_sell_off | 1. voluntary_sell_off2. sell_off_dispute3. sell-off_request | | customer_drop_off | 1. customer_dropoff2. customer_doesn_t_want_to_continue | | shortfall | 1. sell_off_dispute2. shortfall_issue3. short_fall | | interest | 1. interest_/_charge_dispute 2. interest_amount_incorrect 3. interest_and_charges | | renewal | 1. renewal |

---

## #166 — LSQ BRD For MFD Activations
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently, MFD leads entering through multiple channels lack a unified onboarding and activation process. This results in:

- Productivity Loss
    - Data inconsistencies
    - Delayed activation due to a low follow-up mechanism
    - Fragmented visibility across different channels of leads
- The Activation Process is currently ad hoc and dependent on Google Sheets for tracking
- Enhance the follow-up mechanism

---

---

## #167 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #168 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #169 — Term Loan Apportionment Logic
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Apportionment Logic - Apportionment is the distribution of a paid sum of money across multiple components of a loan/tranche in order to knock off/settle these components. - Apportionment logic will be based in the order of IPC. - In case of a single tranche apportionment the order will be: Interest Overdue>Principal Overdue>Interest Due>Principal Due>Charge. In case there are multiple EMIs of the Tranche which are overdue then apportionment will start from the oldest EMI overdue. - In case of multiple tranches apportionment the order will be: Oldest EMI overdue(Interest>Principal)>Oldest EMI due(Interest>Principal)>Charges. In case of EMIs overdue across multiple tranches the oldest EMI across tranches will be apportioned first then the apportioning will be done for the next oldest EMI across the tranches and so on so forth. In case all the overdue EMIs are cleared/apportioned the next apportioning will be done for the oldest due EMI and once the oldest due EMI is apportioned then apportioning of the next oldest due EMI will be done and so on so forth. Once all the overdue and due EMIs are apportioned across tranches, apportionment of charges will start and it will also be done based in the order of the oldest charge getting apportioned first i.e. in the chronological order. - If after the apportionment of all the components there is an excess which remains then we will ask the user to select the tranche wherein the excess will be adjusted. The excess adjustment will happen in a way that either the Tenure of the Tranche is reduced or the EMI of the Tranche is reduced based on the user’s selection. Default option(in case user does not select) will always be to reduce the tenure keeping the EMI same for the oldest Tranche.

---

## #170 — Term Loan Charges
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Charges 1. No fees will be charged to users for the below scenarios : - Mandate bounce charges - Daily penal charges on interest overdue - Security sell-off charges 2. Business would need visibility on the below scenarios : - How many customers bounced with sourcing channel CRED (at Opportunity ID level) - No of days the EMI was overdue at Opportunity ID level for sourcing channel CRED - No of customers where security sell-off occurred along with sell-off amount and Opportunity ID mapping 3. No communication to be sent from DSP to CRED customers for any penal charges (even if the penal charges are equal to zero)

---

## #171 — Term Loan Communications
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Customers availing a **Term Loan under Loan Against Mutual Funds (LAMF)** must have timely, contextual, and transparent communication regarding their loan lifecycle.

- Customers often don’t receive clarity on loan disbursement, repayment schedules, EMI due dates, tranche-level updates, and closure status.
- Absence of structured communication increases inbound queries to customer support, delays repayments, and lowers customer trust.
- Regulatory and compliance requirements mandate that lenders provide customers with certain communications (e.g., SOA, NOC, repayment reminde

**Solution:**
?**

A structured, automated, and multichannel communication framework for **Term Loan against LAMF**, covering the entire lifecycle:

---

## #172 — Term Loan Customer Statements
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Customers availing term loans against mutual funds will want to have a clear visibility of their **collateral, loan obligations, tranche-level details, and closure status**. These statements will help in solving the below:

- Customer confusion on pledged securities and their valuation.
- Lack of transparency around principal outstanding, EMI dues, and charges at the loan and tranche level.
- Difficulty in obtaining official proof of loan closure (No Dues Certificates).
- Increased customer support queries and operational overhead for servicing teams.

We need a standardized

**Solution:**
?**

We will design and deliver **five standard customer statements** for the Term Loan Against Mutual Funds product in V0:

1. **Holding Statement**
    - We will be providing this to the customer so that they are informed about their Holdings with us.
2. **Statement of Accounts (Loan and Tranche)**
    - These documents will help the customer with an understanding about their Dues and transactions.
3. **Loan and Tranche No Dues Certificates (NOC) - Loan and Tranche**
    - When a Loan or a Tranche is closed/foreclosed we will be providing these statements.

---

Documents which CRED shares with their customers in their current product:

At loan level:

- sanction letter
- ⁠holding document

At each Tranche level:

- Loan agreement
- ⁠ key fact statement

If Tranche is closed

- NOC docum

---

## #173 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #174 — Term Loan Disbursement
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Disbursement ### First Drawdown Based on the Submit opportunity status the subsequent flow will be decided: **Submit Opportunity Failure:** - Loan and Tranche Account won’t be created and LSP will have to re-trigger the request **Submit Opportunity Success(Disbursal Success):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. - Our payout partner acknowledges the request and initiate the payout from their end. - Once the amount gets debited from our bank account we get a debit success response. - Post the debit from our Bank Account the amount will get credited to the customer’s bank account. This is when we get a credit success response. - Once we receive a credit success response we will be posting the disbursal in the ledger and accordingly a Tranche account will be opened. - Based on the disbursal amount, tenure and interest rate the repayment/EMI schedule gets generated. **Submit Opportunity Success(Disbursal Failure):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. There are multiple scenarios once the disbursal/payout request is triggered from our systems: 1. The request is not triggered resulting in an instant failure of the disbursement. In such a case we need to retry initiating the request until it gets triggered to the Payout partner. 2. The request is triggered from our system but due to the Payout partner system being down we get an error resulting in disbursement failure. In such a case we need to re-trigger the request at the same time we receive the error from our payout partner or we can wait for sometime before re-triggering the request. 3. The request is received by the payout partner and the same is acknowledged through a response but the debit from our bank account does not happen and we get a debit failure response. In such a case we need to re-trigger the disbursal request(Depends on tech handling, if we are not able to handle this in V0 then we can mark the disbursal as failure and inform the LSP of the same for them to re-trigger the request and we unblock

---

## #175 — Term Loan Excess Handling and Refund
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently, all repayments (via VA or PG) can result in excess funds being received from the borrower due to multiple reasons such as pre payments, duplicate transactions, or rounding differences.

Without a clear and automated excess handling logic, this can lead to:

- Incorrect allocation of payments across tranches or dues.
- Customer confusion and complaints regarding refund timelines.
- Operational inefficiencies due to manual intervention in refund processing.
- Incorrect accounting treatment if prepayment or refund rules are not consistently applied.

We aim to design

**Solution:**
?**

---

## #176 — Term Loan Foreclosure
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

For Borrowers:

•	Interest burden: Reduces overall interest paid over the loan/tranche tenure.

•	Debt-free sooner: Achieves financial freedom earlier than planned.

•	Flexibility: Allows reallocation of capital or freeing up of credit limits.

For Lender/Business:

•	Reduces credit risk: Full repayment eliminates the risk of future defaults.

•	Recycling capital: Frees up capital for new disbursements, improving portfolio turnover.

---

**Solution:**
?**

---

## #177 — Term Loan Mandate Repayments
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

- **Collections Reliability:**
    
    In Term Loans, fixed EMI dates require timely collections. Manual payments or ad-hoc transfers are prone to delays, user forgetfulness, and operational leakage.
    
- **Operational Efficiency:**
    
    Manual chasing of repayments increases Ops load, costs, and NPA risk.
    
- **Customer Experience:**
    
    Users don’t want to remember EMI dates or perform repetitive actions each month. Mandates automate this and prevent missed-payment penalties.
    
- **Regulatory Alignment:**
    
    NPCI/NACH mandates ensure collections hap

**Solution:**
?**

---

## #178 — Term Loan Manual Repayments(PG)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

For Borrowers:

•	Multiple payment options: Cards, UPI, netbanking, etc.

•	On-demand payments: Can make ad-hoc part-payments, overdue clearance, or foreclosure instantly.

•	Better experience: Real-time confirmation and receipts. 

•	Convenience: Removes friction of doing manual transfers for loan repayment.

For Lenders:

•	Improved collections efficiency: Easier for customers to pay resulting in fewer missed EMIs.

•	Faster settlement: PGs provide quick transaction processing.

•	Reduced operational cost: Less manual reconciliation vs cheque/DD payments.

•	Scalable: Hand

**Solution:**
?**

---

## #179 — Term Loan Manual Repayments(VA)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Customers rely on LSP app or automated mandate flows for repayments. However, some customers may want to make repayments directly to DSP (e.g., via bank transfer). There is no simple mechanism for customers to pay directly outside the LSP ecosystem.

Without a Virtual Account (VA) option:

- Customers lack flexibility in repayment methods.
- Ops team faces reconciliation challenges for direct transfers.

---

**Solution:**
?**

Enable repayments via static Virtual Accounts (VA) mapped per customer. Customers can transfer funds directly to DSP, and the repayment will be posted in the Loan Management System (LMS) with appropriate apportionment, re-amortisation, or foreclosure handling.

---

---

## #180 — Term Loan Prepayments and Excess Handling
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
Are We Solving?**

- Customers need to be provided with an option to pay their EMIs as and when they want in order to avoid higher delinquencies and bad customer experience.
- Customers needs a structured way to prepay specific tranches/EMIs in their term loans.
- This creates customer dissatisfaction, potential regulatory risk, and inefficient fund management for the lender.
- Without proper foreclosure/prepayment support, customers may:
    - Face higher effective interest costs.
    - Avoid early repayment, reducing lender’s portfolio efficiency.

**Problem Statement:**

We need to design a

**Solution:**
?**

---

## #181 — Term Loan Sell off
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
Are We Solving?**

- When customers miss repayment obligations / goes into shortfall / goes into high risk category, the lender faces credit risk exposure and delayed recovery of dues.
- Without a transparent process, collateral liquidation may lead to:
    - Operational inefficiencies.
    - Customer disputes regarding how proceeds are applied.
    - Regulatory compliance gaps.
- There is a need for a standardized, rule-based collateral sell-off mechanism to ensure timely recovery and clear apportionment of proceeds

---

**Solution:**
?**

---

## #182 — Term Loan Unpledge Eligibility API(Post loan creat
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently, LSPs do not have visibility into how much of a customer’s pledged portfolio is eligible for unpledging at any given point in time.

When users initiate an unpledge request through the LSP interface, they may encounter errors or rejections if:

- The requested unpledge amount exceeds the eligible limit (based on outstanding loan value, haircut, or margin requirements)

This leads to:

- Poor user experience — users get rejected after attempting unpledge.
- Increased operational load — repeated support queries and failed attempts.
- Inefficient system calls — LSPs m

**Solution:**
?**

We will provide an Eligibility API for Unpledging that LSPs can call before initiating an unpledge request. The API will return aggregate eligibility (amount-wise) for the LSP to inform to their customers on their app. The eligible amount based on which the user will be able to unpledge their funds will be calculated as detailed below:

$Maximum Unpledge Eligible Amount = Drawing Power - Principal Dues - Interest Dues - Outstanding Loan Principal(Not due) -  Outstanding Interest for Upcoming EMI across all Tranches(Not Due) + Total Excess$

The API we need to provide will include the following mandatory parameter:

loanAccountId

The response we need to provide based on the API call will include the following mandatory parameters:

loanAccountId
maxUnpledgeEligibleAmount

The Maximum 

---

## #183 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #184 — Repayment_Schedule_3900 (4)
**Status:** Unknown | **Last edited:** Unknown

# Repayment_Schedule_3900 (4) ![](Repayment_Schedule_3900%20(4)/image1.png) --- Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) --- RANJAN SINGH S/O: Dinesh Singh,shivalya bhawan,Sector, 03,nandgawn,Singrauli,Singrauli,Madhya, Pradesh,486887 Singrauli- 486887,Madhya Pradesh 7980565882 ranjan.singh@voltmoney.in --- Branch Name DELHI - RAJENDRA PLACE Product Type LAS Customer Name RANJAN SINGH Currency INR Loan Account No. 3900 Frequency Monthly Rate of Interest per annum [%] 10.19 Loan Status Active Loan Amount [Rs.] 315.00 Total Installment [Rs.] Total Tenure (in month) 12 Balance Installment [Rs.] Loan Sanctioned Amount [Rs.] 50,500.00 Charges Outstanding 0.00 Loan maturity date 07-Oct-2026 [Rs.] Available Amount for 49,998.00 Interest Rate type Floating Disbursement [Rs.] ![](Repayment_Schedule_3900%20(4)/image2.png) --- | | | --- | | Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) | | Installment no . /TypeDue Date / Transaction DateOpening Balance [Rs.]Installment Amount [Rs.]Principal [Rs.]Interest [Rs.]Closing Balance [Rs.]Efftect Rate(%)Transaction TypeF07-Oct-2025407.000.000.000.00407.0010.19Facility DateD13-Oct-2025407.000.000.000.0010,407.0010.19DisbursementD17-Oct-202510,407.000.000.000.0030,407.0010.19DisbursementD20-Oct-202530,407.000.000.000.0045,407.0010.19DisbursementD27-Oct-202545,407.000.000.000.0049,907.0010.19Disbursement131-Oct-202549,907.00196.840.00196.8449,907.0010.19P17-Nov-202549,907.000.000.000.0049,906.0010.19Part Payment230-Nov-202549,906.00417.900.00417.9049,906.0010.19P02-Dec-202549,906.000.000.000.0030,326.0010.19Part PaymentD08-Dec-202530,326.000.000.000.0031,326.0010.19DisbursementP09-Dec-202531,326.000.000.000.0030,325.0010.19Part PaymentP29-Dec-202530,325.000.000.000.0030,315.0010.19Part Payment331-Dec-202530,315.00268.280.00268.2830,315.0010.19P02-Jan-202630,315.000.000.000.00315.0010.19Part Payment431-Jan-2026315.0011.160.0011.16315.0010.19528-Feb-2026315.002.520.002.52315.0010.19631-Mar-2026315.002.790.002.79315.0010.19 | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) | | | | | | | | | | | | | | | | | Terms and Condition: The dynamic repayment details provided above are for reference only. Please refer to the Statement of Account (SOA) for actual payments, receipts, and dues. The repayment schedule is drawn from the latest facility date. Interest dues will be basis actual utilisation during the month. The “Available loan amount for disbursement” will be restricted to the net of sanctioned amount and loan amount. | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #185 — Analytics requirement Foreclosure
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Foreclosure | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of foreclosure requests | (count of total requests made today) | | | | | | | | | | Number of requests automatically closed | (count of requests made and closed today) | | | | | | | | | | Number of requests pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(settled_on - created_on) | | | | | | | | | | % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.foreclosurerequests ### Field: foreclosurerequests: created_on - When request was created Collections: closed_on - When request was closed automatically Request status ### Table: admin_action_audit admin action name: To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #186 — Analytics requirement Repayment
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Repayment | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of repayments | (count of total repayments made today) | | | | | | | | | | Number of transactions automatically settled | (count of repayments made and settled today) | yesterday | | | | | | | | | Number of transactions pending settlement | (Count of repayments made today but pending settlement) | | | | | | | | | | Average settlement TAT | For payments settled today avg(settled_on - created_on) - difference of hours | | | | | | | | | | % repayments settled automatically | % of payments that were settled automatically today (identify payments settled manually via admin action) | | | | | | | | | | | | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.collections ### Field: Collections: created_on - When payment was created Collections: settled_on - When payment was settled automatically Payment_status (If equals to settled - payment was settled either using admin action or automatically) ### Table: admin_action_audit (Credits) admin action name: UPDATE_COLLECTION_STATUS To identify which collections were settled manually Format: Email with CSV attached Sample query: ```sql SELECT CAST(collections.created_on AS DATE) as transaction_date,collection_status,count(*) FROM collections LEFT JOIN credits ON collections.credit_id = credits.credit_id WHERE lending_partner_id = 'Bajaj' AND CAST(collections.created_on AS DATE) <= current_date - INTERVAL '2' DAY AND CAST(collections.created_on AS DATE) >= current_date - INTERVAL '30' DAY AND collection_status not in ('REQUESTED','CANCELLED','FAILED') group by collection_status,CAST(collections.created_on AS DATE) order by 1,2 ``` Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #187 — Analytics requirement Revocation request
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Revocation request | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of revocation requests | (count of total revocation requests made today) | | | | | | | | | | Number of revocation requests automatically closed | (count of requests made and settled today) | | | | | | | | | | Number of revocation pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours | | | | | | | | | | % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credit_applications.default.revocationrequests ### Field: revocationrequest: created_on - When payment was created revocationrequest: settled_on - When payment was settled automatically revocation requests status (If equals to closed - request was closed either using admin action or automatically) ### Table: admin_action_audit admin action name: CLOSE_REVOCATION_REQUEST To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #188 — Sameer Minde Vaibhav (1)
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav (1) Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #189 — Transactions Key Mapping
**Status:** Unknown | **Last edited:** Unknown

# Transactions Key Mapping: We shorten Bajaj transaction strings to make them more legible and to format it better in the SOA: | **Bajaj Key** | **Volt derived value** | | --- | --- | | Loan amount disbursed | Withdrawal | | LAS PROCESSING FEES | Processing fee | | Processing fees collected | Processing fee | | Repayment received | Principal repayment | | Cancellation of Disbursement for LAS | Withdrawal failed | | Reversal of Principal amount | Withdrawal failed | | Interest Posting | Interest repayment | | Interest received | Interest repayment | | Charges Posting for LAS Recurring Amount adjusted against Disbursement | Adjustment - Disbursement | | Interest for the period | Interest Repayment | | Round off | Round off | | LAS NACH BOUNCE CHARGES | Bounce Charges | | Processing fees | Processing Fee | | Penal Interest | Penal Interest | | Loan receipt Manual Posting of Interest | Interest Repayment | | Amount received towards Sale of Shares | Sell-Off | | PF Rebook | Processing Fee | | PF Reversal | Processing Fee | | Advance Interest | Interest Repayment |

---

## #190 — How banks and NBFCs manage rounding of interest an
**Status:** Unknown | **Last edited:** Unknown

# How banks and NBFCs manage rounding of interest and charges, and how they handle accounting in these cases. ## **1. Regulatory & Industry Context** ### RBI Guidelines: RBI doesn’t dictate **how to round**, but it **expects fairness, transparency, and precision** in: - Customer charging - Auto-debit recovery - Tax invoicing - Reconciliation of ledgers So, banks and NBFCs need to: - Ensure **customers aren’t overcharged** - Match debits with invoices/statements - Maintain proper **audit trail** and **variance accounting** if rounding is applied --- ## 2. Rounding Methods Used by Banks & NBFCs | Type | Common Use Case | Real-world Examples | | --- | --- | --- | | **No Rounding (Post exact value)** | Charges with GST, floating interest | HDFC Bank, Axis Bank, Bajaj Finance (on fees), most NBFCs | | **Round to Nearest Rupee** | Interest on EMI loans, penal charges | SBI, ICICI Bank, Fullerton | | **Round Up (Conservative)** | Micro loans, prepaid cards | Some gold loan NBFCs | | **Cumulative Rounding** | Long tenure loans | Used in housing finance | --- ## 3. Detailed Accounting Treatment by Banks/NBFCs ### **A. Exact Posting (No Rounding)** ### Use Case: - Processing fees + GST - Penal charges ### System Flow: 1. Fee computed: ₹100 2. GST @18% = ₹18 3. Total = ₹118.00 (posted and debited as-is) ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹118.00 | | | Processing Fee Income | | ₹100.00 | | GST Payable (Output) | | ₹18.00 | ✅ Matches invoice and is tax compliant --- ### **B. Round at Posting (Nearest Rupee)** ### Use Case: - Accrued interest - EMI interest - Installment schedules ### Example: - Accrued Interest: ₹199.48 → Rounded: ₹199 - Accrued Interest: ₹199.50 → Rounded: ₹200 ### System Flow: - Round value **at the point of debit** ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹200.00 | | | Interest Income | | ₹199.48 | | **Rounding Reserve GL (Internal)** | | ₹0.52 | > 🔸 If we round down, the 0.52 may be debited to an expense account. > ### Why Rounding Reserve GL? To track small deltas between system-calculated interest and posted amount. ✅ Fair

---

## #191 — PhonePe UPI Autopay Evaluation
**Status:** Unknown | **Last edited:** Unknown

# PhonePe UPI Autopay Evaluation API Documentation & Integration - [Link](https://developer.phonepe.com/v1/reference/subscription-v2-authorization) **List of APIs** 1. Authorization API 1. This API is used to generate the auth token to access the rest of the APIs. 2. The auth token is valid for 1 hour. 3. If the auth token is re-generated within 1 hour, the old token will not expire. - Request ```json curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --data-urlencode 'client_id=' \ --data-urlencode 'client_version=1' \ --data-urlencode 'client_secret=' \ --data-urlencode 'grant_type=' ``` - Response ```json { "access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "encrypted_access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "expires_in": 3600, "issued_at": 1738669002, "expires_at": 1738672602, "session_expires_at": 1738672602, "token_type": "O-Bearer" } ``` 1. Validate VPA API 1. This API is used to validate the user's VPA. 2. Returns, valid & name of the user. 3. We should ask PhonePe team to share the bank account number & IFSC associated with this VPA. This will help us to limit mandate registration only on verified bank accounts. - Request ```json { "type": "VPA", "vpa": "nihaltest1@ybl" } ``` - Response ```json { "valid": true, "name": "<Name of User>" } ``` 1. Intent 1. This API is used to create the intent link for autopay. 2. amount - this parameter defines the amount to be deducted at the time of registration. 3. maxAmount - this amount defines the maximum amount the mandate is registering for. 4. Android - Generic intent URI will be provided. 5. iOS - Tpap specfic URI will be generated. Only Gpay, PhonePe & Paytm is supported. This will be a drawback as we can’t give users the power to choose the app. - Request ```json { "merchantOrderId": "MOTEST5", "amount": 300, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST5", "authWorkflowType": "TRANSACTION", "amountType": "FIXED", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_INTENT", "targetApp": "com.phonepe.app" } }, "deviceContext" : { "deviceOS" : "ANDROID" } } ``` - Response ```json { "orderId": "OMO2502041725138147510236", "state": "PENDING", "intentUrl": "ppesim://mandate?pa=VOLTMONEYUAT@ybl&pn=SUBSCRIBEMID&am=300&mam=&tr=OM2502041725138157510738&utm_campaign=SUBSCRIBE_AUTH&utm_medium=VOLTMONEYUAT&utm_source=OM2502041725138157510738" } ``` 1. Collect 1. This API is used to send the collect request for mandate setup. 2. In collect request, all the VPAs are supported. Even Gpay, SuperMoney VPAs are supported. - Request Body ```json { "merchantOrderId": "MOTEST6", "amount": 200, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST6", "authWorkflowType": "TRANSACTION", "amountType": "VARIABLE", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_COLLECT", "details": { "type": "VPA", "vpa": "nihaltest1@ybl" } } } } ``` - Response ```json { "orderId": "OMO2502041727154877510267", "state": "PENDING" } ``` 1.

---

## #192 — I want to loan from my Mutual Fund but how and how
**Status:** Solutioning pending | **Last edited:** Unknown

# """I want to loan from my Mutual Fund but how and how to repayment the loan amount, how much interest etc...""” Classification: UX issue Notes: User wanted to know about the specifics of the loan before applying on the landing page PRD/Solution mapping: Pending Platform: Wati Reference Link/ID: 917908790799 Status: Solutioning pending

---

## #193 — User repaid on a working day within business hours
**Status:** Solutioning pending | **Last edited:** Unknown

# User repaid on a working day within business hours yet the payment got settled the next day with Tata Classification: Tata repayment settlement Notes: Discussion in progress with Tata PRD/Solution mapping: PRD ready Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13077 Status: Solutioning pending

---

## #194 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #195 — Content
**Status:** Unknown | **Last edited:** Unknown

# Content 1. Title: Loan offer 2. Hero details: 1. Selected loan amount. 2. Credit limit available. 3. Benefits: 1. Trusted lender Tata capital 2. Unlimited withdrawals 3. Repay principal anytime 4. Pay interest only on what you withdraw 5. Monthly Interest only EMI of only ₹862 for ₹1,00,000 withdrawal at 10.49% interest (Interest should be communicated upfront) 4. Charges: 1. Interest rates: 10.49% p.a. 2. Early repayment/ foreclosure: Free 3. Withdrawals: within 4 hours 4. One time processing fee (excl. GST): ₹840 1. Processing fee is charged once in the whole term 5. Stamp duty (as per registration state): ₹260 6. Term: 36 months (Renewal available) 5. CTA: 1. Withdraw in 4 steps

---

## #196 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements ![Untitled](Design%20requirements/Untitled.png) ![Untitled](Design%20requirements/Untitled%201.png) 35% users drop off from the loan summary(Verify interest and charges page) Problems we have identified: 1. Users think that this is the last page of the application. 2. Benefits are not properly communicated. 3. User thinks that the PF is too high. Things that we want to communicate with this page: 1. Highlight selected credit limit, remove selected mutual funds: This might be reminding the users that they are pledging alot of MFs for the limit that they are getting. 2. Show maximum credit limit (maybe). 3. Unlimited withdrawals, repay anytime: Communicate benefits. 4. Pay interest only on the amount you use: Communicate benefits. 5. Monthly interest only EMIs, we can show this for 1,00,00 withdrawal and user can change it to see the IOEMI change: This will quantify the interest that they have to pay 1. 10.49% might feel high but IOEMI will be low for default sum of 1,00,000 2. This will communicate that they only have to pay interest on the sum withdrawn 6. Provided by our trusted lender Tata Capital: User trust 7. Highlight zero hidden charges before showing the charges: User should know that we are transparent with our charges. 8. Other details to be in bottom 25% of the screen: [Content ](Design%20requirements/Content%20aa1bb6ecad904d00b07393fa73ff756a.md)

---

## #197 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: rate of interest, foreclousure, processing fees, lein removal, repayment, additional top up, stocks, Kevin (Servicing): Instant disbursals, Delays, Unpledging and Forclosure. ELSS funds are possible for TATA, Schedule the loan disbursal time, Mahesh: Interest, How it works, Repayment. phone pe traffic is greater than influencers, Reconstruct their houses. Names: Main areas of concerns Naveen: Portfolio value, Location. I dont feel like I am doing the Pledging step Requirement : Urgency. Pay somebody, reinvest, NFO Bugs on app vs web

---

## #198 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Process kaise hoga, loan disbursal process, their commission, Referral program Kevin (Servicing): 10% buffer for Bajaj Mahesh: Repayment queries, How is my interest calculated, Stop growing, ownership changed, low ticket sizes, Dont need the loan right now, they want to check limit. Names: Common questions Naveen: - Processing fee channel - Transparency KYC - Fetch and Setting during this time we dont see the interestv or fees

---

## #199 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: interest rate, stocks, physical presence, commission | Convinience, One platform, Easy, Visibility, RM, Groups, iN HOUSE TECH, Mahesh: Reducing rate of interest, 10 hours Customer care, Balloon repayment. Names: USPs Naveen: 70-80% are cross checking Interest rate, PF reduce, dedicated product

---

## #200 — User Research Framework
**Status:** Unknown | **Last edited:** Unknown

# User Research Framework ### User research guide ## **Step 1 : Defining Purpose & Objectives** Define the goals of the research to ensure alignment across stakeholders. The research objective should answer - What decision do you need to make for which you need data through user research? - What assumptions are you trying to validate - What would success of this user research look like ## **Step 2 : Target the right and varied User Segments** To ensure comprehensive insights, target varied user groups based on relevant characteristics. Use the following parameters to define your user cohorts: 1. **By User Personas:** - Leverage pre-defined personas representing key demographics, behaviors, or motivations. - Example: - **Persona A**: New users exploring the product. - **Persona B**: Long-term users engaging with advanced features. 2. **By Task-Based Segmentation:** - Categorize users based on their interactions with specific features or tasks: - **Completion:** Users who successfully completed the task. - **Abandonment:** Users who started the task but dropped off. - **Non-Starters:** Users who never attempted the task. ## Step 3 : Selecting the right Research Method Select methods tailored to your objectives and audience. | **Stage** | **Method** | **Purpose** | Examples | Focus on | | --- | --- | --- | --- | --- | | **Exploration** | User Interviews | Discovering Needs and Pain Points | Amazon or Airbnb uses exploratory research when entering new markets or identifying adjacent user needs | Understand attitudes, motivations, and unmet needs. | | | Surveys | | | Gather quantitative preferences at scale. | | **Validation** | Usability Testing | Testing Solutions for Effectiveness | Google routinely conducts rapid validation for its features using A/B testing | Test ease of use for loan application processes. | | | Surveys | | | Assess clarity of repayment terms and options. | | **Tracking** | Behavioral Analytics | Monitoring User Interactions | Facebook employs tracking through behavioral analytics to refine its News Feed algorithm, using live user data rather than pre-launch tests | Identify friction points in user flows (e.g., drop-off rates). | ### Good articles on user research [Defining the Objectives of User Research](https://www.interaction-design.org/literature/article/defining-the-objectives-of-user-research) [How to conduct user research: A step-by-step guide](https://designstrategy.guide/ux/ux-research-guide/) [The Key Factors Driving Silicon Valley Companies' Success - Attorney Aaron Hall](https://aaronhall.com/the-key-factors-driving-silicon-valley-companies-success/) ## Parameters for types of research **Exploration Type:** Discovering Needs and Pain Points - Motivations - Aspirations - Influences - Context

---

## #201 — V0 1 for User Research
**Status:** Unknown | **Last edited:** Unknown

# V0.1 for User Research Hypothesis (Investment profile, Debt profile, Evaluation criteria, Repayment behaviour ## What do we need to know about our users 1. Basic details - Age range - Location type (urban/suburban/rural) - Occupation - Family situation (single, married, dependents) 2. Financial Profile - Asset types they own (stocks, bonds, crypto, etc.): - Asset value range - Income level - Existing debt obligations - Investment experience level - Financial goals and priorities 3. Evaluation Behavioural - How do they evaluate on taking loans - Research habits before financial decisions - Level of detail needed for decision-making - Key questions they need answered - Required reassurances about the process 4. Motivations & Goals - Primary reason for seeking a loan - Urgency for loan - Preferred loan amount range - Plans for using the loan - Long-term financial objectives - What makes them choose asset-backed loans over traditional loans 5. Pain Points & Fears - Concerns about using assets as collateral - Trust issues - Knowledge gaps about lending processes - Previous negative experiences with loans 6. Information Needs - Types of content they consume - Preferred learning style about financial products 7. Journey Touchpoints - How they discovered Volt - Research methods used - Key decision factors - Support needed during the application process ## Questionnaire: User Calls [20] ### Warm-Up Questions 1. How did you hear about Volt money? 2. How has your experience been using volt? 3. What do you do, must have been a long day? 4. When and how did you start investing in Mutual Funds? ### **Exploring Financial Interests and Habits** 1. When and how did you start investing in Mutual Funds? - "Walk me through how you chose that particular fund?" - "What other investment options did you consider at that time? 2. How often do you plan your finances? 1. Do you do it every year, month or daily? 2. What tool do you use to track the same 3. Tell me about the last unexpected expense/financial emergency you faced? - "Walk me through exactly what you did to handle it?" - "What options did you consider?" - "How did you decide which option to go with?" 4. When was the last time you used an asset (like gold, FD, shares) i.e break our FD, Shares or MF? 5. Which banks do you currently have relationships with, and how would you

---

## #202 — User Persona Research
**Status:** ** Married with family responsibilities | **Last edited:** Unknown

# User Persona Research [V0.1 for User Research](User%20Persona%20Research/V0%201%20for%20User%20Research%206d63c60255e247f1a2d7a8b49d5a3bbd.md) [User Research Framework](User%20Persona%20Research/User%20Research%20Framework%20adba50e539a84bf8be27f3377b94ba29.md) ## Why do we need user personas - Empathise our user while designing products - Help target their goals, needs, aspirations and pain points - Make user centric product decisions ## Hypothesis ### Established Investor # Meet Rajesh Gupta - The Established Business Owner ## Demographics - **Age:** 44 years old - **Location:** Tier 1 city (Mumbai/Delhi/Bangalore) - **Profession:** Business Owner - **Income Level:** Upper middle class to affluent - **Family Status:** Married with family responsibilities ## Financial Profile - **Loan Requirements:** ₹7.35L (average for business customers) - **Primary Loan Purpose:** Working capital for business - **Investment Portfolio:** Active mutual fund investor - **Existing Loans:** Has a car loan and possibly a home loan - **Financial Behavior:** Financially aware but prefers quick solutions ## Digital Behavior - **Social Media Usage:** Moderate user of Facebook and Linkedin - **Content Consumption:** Actively watches financial/business content (56%) - **Preferred Platforms:** Newsletters (31%), Facebook (28%), YouTube (21%) - **Financial Influencers:** Follows personalities like Rachna Ranade, Akshat Srivastava ## Pain Points & Needs - **Time Sensitivity:** Needs immediate access to funds (74% unplanned loans) - **Process Friction:** Avoids traditional banks due to lengthy processes (69% don't approach banks first) - **Alternative Consideration:** Considers personal loans (41%) or borrowing (23%) before LAMF - **Social Constraints:** Hesitant to borrow from personal network despite considering it ## Decision Making Behavior - **Planning:** Generally makes quick, unplanned financial decisions for business needs - **Research:** Limited research into alternatives due to urgency - **Priority:** Views liquidating mutual funds as last resort but values speed and convenience - **Motivation:** Driven by immediate business requirements rather than personal expenses ## Product Expectations - **Core Needs:** Quick disbursement, minimal documentation - **User Experience:** Expects digital-first, seamless experience - **Post-Service:** Wants clear visibility of loan status, EMIs, and interest calculations - **Communication:** Prefers digital updates but appreciates timely reminders for payments ## Quote "Quick process, bethe bethe kaam ho gaya" (The work was done while sitting in one place) ### New Investors # Meet Aditya Shah - The Tech-Savvy Growth Seeker ## Demographics - **Age:** 28 years old - **Location:** Tier 1 city (Bangalore/Mumbai) - **Profession:** Senior Software Engineer at a tech startup - **Income:** ₹18-25 LPA - **Living Situation:** Single, lives independently in a rented apartment ## Financial Profile - **Investment Portfolio:** - Started investing 3-4 years ago - 60% equity mutual

---

## #203 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #204 — NBFC B2B LSP Stack
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP Stack # Press Release DSP Finance, a non-banking lender licensed by RBI and part of the DSP group has recently gone live with its retail lending portfolio of Loan against Mutual funds. DSP Finance has been in the news recently for acquiring a majority stake in Volt Money, one of India’s pioneers in the LAMF space as well as the one of the biggest in the market. DSP Finance intends to leverage Volt’s product, distribution as well as technology platform to roll out a suite of products across retail and corporate lending which aims to help individuals and businesses leverage their financial assets better for a better financial profile. DSP Finance has recently been onboarded on Volt Money as one of its lending partners for the Credit line facility offered to individuals. As the business volumes ramps us in this segment, DSP Finance intends to work with other leading online and offline platforms in the country to offer LAMF products. In addition to the current offering of the on-demand loan, DSP Finance intends to offer term loans through its platform where its LSP partners can offer multiple credit products within their app. DSP Finance’s latest offering ‘DSP Flash’ aims to help platforms embed credit offerings into their ecosystem through plug n play APIs and SDKs. These capabilities span the entire credit offerings spanning credit line and term loans against mutual funds as well as securities. DSP finance’s offering not just focusses on customer journey but post servicing as well as operational reconciliation, thus providing an entire suite of offerings compared to most players who offer application related capabilities and rely on offline processes for customer experience. DSP Finance’s capabilities allow platforms to help retain their customers better and at the same time, monetize their base. DSP Finance’s offerings in the credit space comes at a highly flexible yet affordable pricing structure compared to the traditional unsecured loan offerings as well as EMIs against credit cards. This win-win strategy allows platforms to build their own customer experience and ensure trust while DSP Finance focusses on the core activities spanning risk assessment, CDD, compliance and operations as per RBI’s DLG guidelines. --- # FAQs ## External FAQs ## Internal FAQs - **Who will be our target segment for the Flash offering?** Our Target segment for the Flash offering will largely be large online and offline platforms who are

---

## #205 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can

---

## #206 — Invoice & Payment Process
**Status:** Unknown | **Last edited:** Unknown

# Invoice & Payment Process # Challenges Currently, Volt and its NBFC partner, DSP works with multiple partners spanning SaaS and bank partners for multiple tech related services. Most of these vendors work on postpaid model where they invoice us on a monthly level. This results in multiple challenges. - Dependencies on key people (Lalit, Ankit) to approve each invoice - Delay in processing payment resulting in bad experience for vendors - Possibility of not paying the right amount due to lack of reconciliation - Poor support from partners due to delayed payment processing The primary reason for the same is a lack of a documented process. # Solution