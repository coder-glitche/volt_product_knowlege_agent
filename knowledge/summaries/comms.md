# Current State: Comms

> Auto-generated from 49 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Deferring email capture and verification during on
**Status:** Not started | **Last edited:** September 26, 2025 7:05 PM

**Problem:**
are we solving?**

Currently we are observing a drop-off of 15% on average across Volt Channels at Email verification step in 30 day window (Apr ‘25). As email is asked from the user during initial part of onboarding process, the drop-offs are higher and needs to be reduced to <10% across Volt channels.

![image.png](Deferring%20email%20capture%20and%20verification%20during%20on/image.png)

---

**Solution:**
?**

- We are proposing to defer the email verification step to later stage in the funnel i.e. pre-agreement creation in order to reduce user drop-off at the initial stage.
- The idea for deferring the email verification to post pledge and pre-agreement is based on the intent of the user which would be high during the later stage of the funnel compared to asking for email verification at initial stage where the intent is usually low leading to higher drop-offs here.

---

## #2 — Streamlining Support Communication by Segregating
**Status:** In progress | **Last edited:** September 11, 2024 4:31 PM

**Problem:**
are we solving?**

- The support inbox(support@voltmoney.in) is comprising customer issues and automated system notifications regarding pledge configuration, SFDC creation, Pledge failure and Pledge confirmation
- This clutter makes it difficult to efficiently manage and prioritise genuine customer queries.
- As a result, our ability to respond quickly and effectively to customer issues is compromised.

---

**Solution:**
?**

---

## #3 — Email Validation Approach PhonePe
**Status:** Not started | **Last edited:** October 22, 2025 1:32 PM

**Problem:**
are we solving?**

PhonePe captures user email IDs without verification, posing compliance and communication risks. To avoid delaying go-live, an interim solution is needed to ensure basic email validity without enforcing strict verification.

---

**Solution:**
?**

- **Phase 1 (pre-Sept 30):** Use email delivery status as a proxy for verification. Undelivered cases follow a manual Ops-led validation via alternate email + OTP or fallback checks.
- **Phase 2 (post-Sept 30):** PhonePe to implement OTP-based or other standard email verification mechanisms within their frontend journey.

---

## #4 — DSP communication email template
**Status:** Done | **Last edited:** October 21, 2024 4:31 PM

**Problem:**
are we solving?**

NBFC will be sharing important communications to the user triggered by certain events that occur in the user’s loan account. The communication should follow a template (for ease of perusal and identification of content by the user)

List of comms:

https://docs.google.com/spreadsheets/d/1BrvoUyz4SbO_Odc4sTLvFumESJkDQwNS4ZahPu3n36o/edit?gid=0#gid=0

---

**Solution:**
?**

| Element | Consideration | Requirement description |
| --- | --- | --- |
| Header | Required | All email template should have a common header with the DSP finance logo. Date of communication and a description of the communication |
| Call-to-Action (CTA): | Required | Capabilities to place primary and secondary CTAs in the body of the text, the design should be able to support multiple CTAs for the user to click |
| Action-oriented text (e.g., "Apply Now", "View Statement") | Required | Design should support call to action statements, while there would be CTAs, specific text with weights would be required to draw user attention (outside of CTAs) |
| Contact information: | Required | Specific section which contains contact details of the NBFC (if the user wants to reach back the team)

---

## #5 — Bulk email automation
**Status:** Not started | **Last edited:** October 14, 2024 2:40 PM

**Problem:**
are we solving?**

- All emails that are directed to [operations@voltmoney.in](mailto:operations@voltmoney.in) trigger automatic ticket creation and assignment without distinction, leading to delays in addressing urgent queries. Lender query emails sent to [operations@voltmoney.in](mailto:operations@voltmoney.in) are not prioritized due to this.
- Individual lien removal emails are sent manually to BAJAJ along with bulk emails comprising of individual lien removal request, resulting in duplicate data being sent for the same case twice in a day.
- Improving the communication after Pledging and 

**Solution:**
?**

—> Lien Removal and Foreclosure emails should **not be sent** individually to lender(BAJAJ). For sending communications regarding Lien Removal and Foreclosure, we will send bulk reports as follows:

1. Update recipient and CC fields for individual Lien Removal and Foreclosure emails send to Volt:
- Change the recipient from [operations@voltmoney.in](mailto:operations@voltmoney.in) to [support.internal@voltmoney.in](mailto:support.internal@voltmoney.in)
    
    This ensures that tickets are not created for each Lien Removal and Foreclosure request
    

- Remove all other recipients and CCs, keeping [support.internal@voltmoney.in](mailto:support.internal@voltmoney.in) as the sole recipient
    
    This includes removing [las.crm@bajajfinserv.in](mailto:las.crm@bajajfinserv.in) and [l

---

## #6 — New Posidex report template
**Status:** In progress | **Last edited:** November 20, 2024 4:54 PM

**Problem:**
are we solving?**

We are failing to pass required field values to TATA's  Posidex report template, causing Posidex report rejections and user blocks, which needs to be fixed by implementing the new template format with all mandatory fields.

---

**Solution:**
?**

Implementing the new template format sent by TATA with all mandatory fields mapped from the Backend.

---

## #7 — Custom Comms based for Ad-hoc situations v2
**Status:** Not started | **Last edited:** May 29, 2026 4:27 PM

**Problem:**
are we solving?

- High-urgency situations (system down, regulatory events, one-off campaigns) need immediate comms capability outside the automated pipeline. All comms today are system-triggered and their is no functionality in the system to generate ad-hoc customer communications
- Ops/compliance/analytics are dependent on the product team for any ad-hoc communications which needs to be sent.
- It is a very time consuming activity for even the product team as of today to send ad-hoc communications as it requires a lot of data crunching, template mapping and script creation
- Some comms depen

**Solution:**
?

**In scope:**
- Once comms creator has the batch file with all recipient details(with Ids, body and variables) of all recipients. He uses the Actions button and selects "Bulk Send Comms" option in Comms section.
- Maker flow
    - recipient batch file upload (xlsx)
    - remarks window
    - Validation flow
        - System auto-validates the uploaded excel before creating a checker task.
        - **Validation

---

## #8 — [DSP] Additional customer comms (compliance)
**Status:** In progress | **Last edited:** May 28, 2025 12:27 PM

**Problem:**
are we solving?**

Sending additional comms to users to comply with DLG and internal compliance requirements. 

---

**Solution:**
?**

---

## #9 — Higher LTV Product – Customer Communication Framew
**Status:** Pending Review | **Last edited:** May 23, 2026 9:07 PM

# Higher LTV Product – Customer Communication Framework # Background As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings. Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements: 1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow. 2. Customers must be notified once their revised credit limit is successfully updated. 3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey. --- # Proposed Solution ## 1. NBFC (DSP) Communications From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow. The communication will serve the following purposes: - Inform customers regarding successful limit enhancement - Share revised loan documentation for customer reference - Ensure regulatory and audit compliance for executed agreements ### Communication Channels - Email - SMS --- ### DSP Email Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement | | Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 | | Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit | | Attachments | Loan kit (KFS + Amendment) | --- ### DSP SMS Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding successful credit limit enhancement | | Template ID | 1107177910598106787 | | Tempalte Name | LTV_Update_Limit_enhancement_V2 | | Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} | | VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} | --- # 2. LSP (Volt) Communications From the LSP side, communications will focus on: - Promoting the Higher LTV offering to eligible customers -

---

## #10 — Dues Comms Updation
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

## #11 — [IronGrid] Email trigger for ops in case of disbur
**Status:** Not started | **Last edited:** March 31, 2026 8:24 AM

**Solution:**
?

- We raise a send grid email to the ops team as soon as a disbursal is rejected due bank mis-mismatch, so that Ops is notified and they can quickly un-block the customer by contacting lender’s operation team and getting bank account updated at their end.

---

## #12 — Custom Comms based for Ad-hoc situations
**Status:** Not started | **Last edited:** March 27, 2026 2:28 PM

**Problem:**
are we solving?

- All comms today are system-triggered and automated — ops, compliance, and analytics have zero ability to send ad hoc communications without a tech deployment.
- High-urgency situations (system or service down , regulatory events, manual outreach, one-off campaigns) require immediate comms capability that bypasses the automated pipeline.
- Today adhoc communcoation are sent by product using a script, this consumes a lot of product effort
- There are a few communications which are dependent on flows are in itself are not produtised, hence it is challenching to productise commu

**Solution:**
?

---

## #13 — Credit Bureau Reporting Comms
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

## #14 — credit_bureau_reporting_comms_product_note
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - VoltMoney is a Loan Against Mutual Funds (LAMF) LSP operating on DSP Finance’s NBFC lending infrastructure. As part of its regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is manual or absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP

---

## #15 — credit_bureau_reporting_comms_product_note 325e8d3
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note 325e8d3af13a808b82ebe94969cbc741 # credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - .As part of regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP depends on proactive borrower communication at critical account events --- ## **1. Problem scope** ### In

---

## #16 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #17 — Increase Credit Utilization via Whatsapp Drips
**Status:** In progress | **Last edited:** June 3, 2024 1:31 PM

**Problem:**
are we solving?**

- Increase the utilization of allocated credit lines among users.
- Boost AUM/principal outstanding without aggressive promotion or breaching partnership agreements.
- Enhance user engagement and retention through personalized communication.

---

**Solution:**
?**

---

## #18 — Making Mobile & Email Verification Log Optional LO
**Status:** Not started | **Last edited:** July 18, 2025 12:17 PM

**Problem:**
are we solving?**

As per RBI’s CDD guidelines, verifying ~~either~~ the customer’s ~~mobile number or~~ email is mandatory. Currently, LSPs must verify ~~the mobile number and submit mobile verification &~~ email and pass the verification logs via the `mobile_verification_log`/`email_verification_log` APIs respectively. The resulting utility IDs are required in the `Submit Opportunity` API to create the loan application at DSP’s end.

However, some LSPs have highlighted friction in integrating these additional API, noting that both mobile number & email are already verified on their end and c

**Solution:**
?**

To reduce integration friction while maintaining regulatory compliance, we propose making the ~~mobile verification log API &~~ email verification log API optional. Instead, DSP will include a clause in the LSP agreement mandating that LSPs verify the ~~mobile number/~~email  shared with DSP during opportunity creation and ensure that ~~mobile &~~ email verification logs can be furnished offline, on demand, whenever requested by DSP to meet audit and compliance requirements

~~This exemption is **not applicable** if:~~

- ~~The LSP does **not** use DSP’s fund fetch or lien marking APIs, or~~
- ~~The LSP allows the user to update/change the mobile number before initiating DSP’s fund fetch or pledge flow.’~~

---

## #19 — Testing DSP Comms
**Status:** Pending Review | **Last edited:** January 7, 2025 10:11 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #20 — [Email Template] Decoupling of Lodgement and Agree
**Status:** Not started | **Last edited:** January 15, 2025 4:44 PM

**Problem:**
are we solving?**

—> In case of Line Enhancement, the flow is as follows: KYC—>Bank —> pledge —> Agreement

- Two separate communications through email is sent to BAJAJ through email, one after the pledge step and the other after Agreement step.
- Email format sent after the Pledge step(no change in Email format):

<aside>
💡

Hi,

Customer has pledged additional securities. Please refer to the attached file for the lodgement of the MF pledged.

LAN No. : V402ALAS00171774

Expecting confirmation with IVR file (PDF)

MF_Pledged_Portfolio.csv

</aside>

- New Email format sent after the Agreemen

**Solution:**
?**

---

## #21 — Shortfall communication enhancement Ignoring accou
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

## #22 — Phone and Email validation on PLJ
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

**Solution:**
?**

---

## #23 — Comms config - OTP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?

We have experienced multiple instances of **SMS service provider outages**, which have **impacted critical business operations**. Since SMS was our **only channel** for sending OTPs used in **login and transaction verification**, we introduced **WhatsApp** as a **backup channel** to ensure continuity.

However, SMS service disruptions are **intermittent**, and we want to maintain SMS as the **primary channel** for OTP delivery while using **WhatsApp and Email** as **secondary fallback channels** during downtime. This approach will help ensure **seamless user experience** and *

**Solution:**
s:

OTP delivery settings will be **event-driven** and **fully configurable** through AWS Config, allowing dynamic control without requiring code-level changes.

---

## #24 — Comms config
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Comms config Customer loan renewals ```json { "LOAN_RENEWAL_REMINDER_1ST": { "eventInFiltering": { "customerChannel": [ "B2C", "B2B", "B2B2C" ], "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "loan_renewal_1st_day_of_month_v1", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "loan_renewal_1st_day_of_month_v1" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "loan_renewal_1st_day_of_month_v1" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "contactnumber" ] }, "MAIL": { "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_2ND": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "15th_day_of_loan_expiry_v1", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "15th_day_of_loan_expiry_v1" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "15th_day_of_loan_expiry_v1" }, ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "contactnumber" ] }, "MAIL": { "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_LAST_WEEK_DUE": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "20days_to_last_day_amount_due", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "20days_to_last_day_amount_due" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "20days_to_last_day_amount_due" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "outstanding_amount", "contactnumber" ] }, "MAIL": { "templateId": "d-78f7acdde85248798dfda7f480312e31", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP",

---

## #25 — Maker checker for servicing comms
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our servicing communications system has critical reliability issues, resulting in both inaccurate content delivery and inconsistent communication delivery to customers. This impacts our service quality and customer experience.

**Solution:**
?**

---

## #26 — Send partner comms to redvision MFD
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

A new communication configuration is required to handle communications for MFDs operating on B2B platforms (such as RedVision and InvestWell) separately from those on the Volt platform.

---

**Solution:**
?**

---

## #27 — Skip Email verification
**Status:** Not started | **Last edited:** December 29, 2025 11:59 AM

**Problem:**
are we solving?**

Email verification is currently mandatory for loan application creation. However, we’re seeing around 15% **user drop-off** at this step. To reduce friction, we propose letting users **choose their preferred primary communication channel — SMS or Email** — and **skip email verification** for those who select SMS. This allows users who rely on SMS to continue without being blocked by email OTP verification.

---

**Solution:**
?**

---

## #28 — Mobile email dedupe check in case on in-progress m
**Status:** Pending Review | **Last edited:** December 25, 2024 6:42 PM

**Problem:**
are we solving?**

- Users can request a mobile number update (e.g., from P1 to P2) for lenders BFL/DSP.
- The mobile number update involves a processing time (TAT) due to:
    - Maker-checker flow at DSP.
    - Operational flow at BFL.
- During this processing time, if a user:
    - Logs in with the new mobile number (P2), or
    - Fetches their Mutual Fund portfolio using P2,
    a new application is created in our system with P2.
- Once the mobile number update is processed:
    - The system ends up with two accounts linked to the same mobile number (P2).
- This results in complications suc

**Solution:**
?**

**Mobile update in progress**

- User can create a new application through following 3 routes
    - MFC fetch
    - In app login
    - Login through SDKs
- Action for each of these routes
    - MFC fetch - Block the user (UI handling)
        
        ![Screenshot 2024-12-23 at 6.21.21 PM.png](Mobile%20email%20dedupe%20check%20in%20case%20on%20in-progress%20m/Screenshot_2024-12-23_at_6.21.21_PM.png)
        
    - In app login - Block the user (UI handling)
        
        ![Screenshot 2024-12-23 at 6.20.54 PM.png](Mobile%20email%20dedupe%20check%20in%20case%20on%20in-progress%20m/Screenshot_2024-12-23_at_6.20.54_PM.png)
        
    - Login through SDKs - Throw an error in the createCustomer/getCustomer API
        
        ```jsx
        {
            "message": "Lead with the same

---

## #29 — MFD Communications for MFDs and Customers
**Status:** Not started | **Last edited:** December 24, 2024 2:11 PM

**Problem:**
are we solving?**

- unclear and mistimed comms leads to lot of escalations.
- we are sending comms with wrong informations
- Some of the comms are not compliant
- 

---

**Solution:**
?**

---

## #30 — [DSP] Dues collection comms
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

## #31 — Productisation of admin tool Change email address
**Status:** Not started | **Last edited:** August 21, 2024 12:14 PM

**Problem:**
are we solving?**

- When customers need to change their email or mobile number, they need to send the details to the RMs to be updated via registered email. This may cause manual errors at the customer and RMs end due to absence of validation of email and phone number.
- The admin tool for these changes cannot be used in isolation and requires communication with all third parties involved after the Loan account is created.

---

**Solution:**
?**

---

## #32 — Dynamic Contact Us WhatsApp Configuration for Supp
**Status:** Not started | **Last edited:** April 21, 2026 5:20 PM

**Problem:**
are we solving?**

---

Support contact details (WhatsApp and calling numbers) are currently hardcoded across multiple touchpoints (Website, App, Partner Dashboard, and templates).

- This results in high operational effort, as any change requires updates across multiple systems.
- There is a need to centralize these details into a dynamic configuration, enabling updates from a single place for current and future use.

**Solution:**
?**

---

- Introduce a centralized dynamic configuration for Contact Us / WhatsApp details
- Replace all hardcoded instances with config-driven variables
- Ensure all platforms (Partner’s Dashboard, Customer Website and App) fetch this value dynamically
- Create separate variables for different support numbers, as currently multiple numbers are in use :
    - Volt Customer Support WhatsApp Number [ 919611749097 ]
    - Volt Customer Support Calling Number [ 08071174410 ]
    - Partner’s Support Number WhatsApp Number [ 9611749295 ]
    - Partner’s Support Number Calling Number [ 9611749295 ]

**Note** : 

- Update the Volt Customer Support number from existing WhatsApp Number to New WhatsApp Number
    - Existing WhatsApp Number : 919611749097
    - New / Updated Number : 918105574747
- N

---

## #33 — CKYC Comms for Regulatory Compliance
**Status:** Done | **Last edited:** April 17, 2026 2:41 PM

**Problem:**
are we solving?

- Currently, DSP Finance (via Decentro) will search for an existing CKYC record in the CERSAI registry (using PAN) → if found, it downloads the data, compares it, and uploads any updates → if not found, it creates a new CKYC record.
- Regulatory compliance mandates that customers be notified when a CKYC record is created by DSP Finance.
- Currently, there is no automated mechanism to trigger an acknowledgement SMS to customers upon CKYC ID creation.
- Without this flow, DSP Finance risks non-compliance with RBI regulatory notification norms.

---

**Solution:**
?

**In scope:**
- Automated SMS trigger inline within the Decentro web-hook processing flow
- Per-record eligibility check (status == COMPLETED AND ckycReferenceId == null)
- Customer phone number resolution from internal system using fxcid_key
- Dynamo DB logging at per-record level for all outcomes (success, failure)
- Trigger Condition Logic
    - When Decentro’s bulk CKYC web-hook is received, the system insp

---

## #34 — Template (Duplicate this for new PRDs) - PN
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #35 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #36 — MFD comms
**Status:** Unknown | **Last edited:** Unknown

# MFD comms Drive link [https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph](https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph) 1. **6 Day MFD activation plan** – Last modified on Oct 10, 2023, by Ranjan Kumar Singh. 2. **Comms content - MFD drop off during reg...** – Last modified on Aug 29, 2023, by Kapil Nagal. 3. **Comms content - MFD Referral** – Last modified on Jul 24, 2023, by Kapil Nagal. 4. **Comms content - Welcome email to MFD** – Last modified on Mar 18, 2023, by Kapil Nagal. 5. **Mastersheet Volt Money - MFD Comms** – Last modified on Jul 24, 2023, by Kapil Nagal. 6. **partner comms status** – Last modified on May 3, 2023, by Ranjan Kumar Singh. 7. **partnerComm[Signup]** – Last modified on May 1, 2023, by Ranjan Kumar Singh. 8. **Referral activation message** – Last modified on Aug 29, 2023, by Ranjan Kumar Singh. [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) Consumer comms :- [https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing](https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing)

---

## #37 — Product note template evaluation
**Status:** Completed | **Last edited:** Unknown

# Product note template evaluation Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora ### Lifecycle of a feature (Why product note): ```json ┌────────────────────┐ │ │ │ (initial problem, │ │ scope, context) │ └─────────┬──────────┘ │ ▼ ┌──────────────── Grooming / Kickoff ───────────────┐ │ │ │ • Align on scope │ │ • Identify edge cases │ │ • Refine requirements │ └─────────┬───────────────────────────┬─────────────┘ │ │ ▼ ▼ ┌───────────────────┐ ┌────────────────────────┐ │ Design Handoff │ │ Cross-Functional │ │ (UX, flows, │ │ Sign-offs │ │ mocks, journeys) │ │ • Finance │ └─────────┬─────────┘ │ • Compliance │ │ │ • Business Ops │ ▼ └─────────┬──────────────┘ ┌───────────────┐ │ │ │ │ │ Product Note │◄─────────────────┘ └─────────┬─────┘ ▼ ┌───────────────────┐ │ PRD │ │ (final detailed │ │ specifications) │ └─────────┬─────────┘ ▼ ┌──────────────┐ │ Engineering │ │ (breakdown, │ │ estimation, │ │ sprinting) │ └────────────── ┘ ``` ### What is a product note? A product note is a succinct, structured document that brings all stakeholders onto the same page before execution begins. Execution here is function specific: - PRDs for PMs - Low fidelity mockups and high fidelity for Design - System design documents for Engineering team - Development of core product It distils the problem, the scope, the target audience, the desired outcomes, and the key decisions into a single source of truth. Its goal is alignment ensuring everyone understands what we’re solving, why it matters, what success looks like, and what the first version will include. ### Use cases of a product note: **1. What is the problem?** - Clear articulation of the problem statement. (What are we not solving) **2. Who are we solving it for?** - Target audience definition and roll-out strategy. (GTM should be separate from defining the target audience) / Phasing can be a part of the product note however GTM may not be a product note **3. How will we know the problem is solved?** - Success criteria and measurable outcomes. **4. How are we planning to solve it?** - Scope of the solution and key components of the approach. - Entry points (User flow diagram) / Use cases **5. Why does this problem matter now?** - Prioritisation rationale and business/user impact. (Merge with what is the problem?) **6. When will we solve it and who owns what?** - Timeline, milestones, and ownership across teams. (Can be a part of solution scope) **7. How does

---

## #38 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #39 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #40 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #41 — Volt - Overdue Communication Enhancement
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

## #42 — Volt - Shortfall Communication Enhancement – Due D
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

## #43 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #44 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #45 — Bulk Email Sender Setup Guide
**Status:** Unknown | **Last edited:** Unknown

# Bulk Email Sender Setup Guide ## Prerequisites 1. Python 3.8 or higher 2. SendGrid account with API key 3. Dynamic email template set up in SendGrid with variables: Template should use these variables: ``` Subject: Volt: GST Invoice for {{invoice_month}} - {{invoice_number}} ``` - {{current_date}} - {{partner_id}} - {{invoice_month}} - {{partner_name}} - {{file_link}} - {{submission_link}} - {{deadline_date}} - {{invoice_number}} ## Setup Steps ### 1. Environment Setup ```bash # Create a new directory mkdir email-sender cd email-sender # Create virtual environment python -m venv venv # Activate virtual environment # For Windows: venv\\Scripts\\activate # For Mac/Linux: source venv/bin/activate # Install required packages pip install pandas python-dotenv sendgrid ``` ### 2. File Structure ``` email-sender/ ├── venv/ ├── .env ├── emailsender.py ├── invoices.csv └── logs/ ``` ### 3. Environment Variables Create a `.env` file with these variables: ``` SENDGRID_API_KEY=<REDACTED> FROM_EMAIL=no-reply@voltmoney.in TEST_MODE=False CSV_PATH=invoices.csv TEMPLATE_ID=d-5a90b23aa1214f3d87f817bffb91ebd9 BATCH_SIZE=100 DELAY=1.0 MAX_RETRIES=3 ``` ### 4. Input CSV Format Create `invoices.csv` with these columns: ``` email_ID,invoice_date,partner_id,invoice_month,partner_name,file_link,Pre-filled Form URL,invoice_number example@company.com,2024-03-01,PART001,March 2024,John Doe,<https://link-to-file>,<https://form-link>,INV-2024-001 ``` ## Running the Script 1. **Test Mode First** ```bash # Keep TEST_MODE=True in .env python emailsender.py ``` Check logs folder for email_log_[timestamp].csv 2. **Live Mode** ```bash # Change TEST_MODE=False in .env python emailsender.py ``` ## Output & Logs - Script creates a `logs` folder - Each run generates a CSV file: `email_log_YYYYMMDD_HHMMSS.csv` - Log contains: - Timestamp - Email status (SUCCESS/FAILED) - Retry attempts - Error messages if any - All email details ## Troubleshooting 1. **Common Issues** - "Missing required environment variables": Check .env file - "API key invalid": Verify SendGrid API key - "Template not found": Check template_id in .env 2. **SendGrid Template** - Ensure all variables are properly defined - Test template in SendGrid dashboard first 3. **CSV Issues** - Check CSV encoding (should be UTF-8) - Verify all required columns are present - No empty rows/cells in required fields ## Best Practices 1. **Before Sending** - Run in TEST_MODE first - Verify template with test data - Check log file format 2. **Production Use** - Start with small batches - Monitor logs actively - Keep DELAY=1.0 to avoid rate limits ## Support For issues: - Check SendGrid logs for delivery status - Review email_log CSV for error messages - Ensure all template variables match CSV data ## Security Notes - Keep .env file secure - Don't commit .env to version control - Use verified sender emails only

---

## #46 — payout Email
**Status:** Unknown | **Last edited:** Unknown

# payout Email ### Bank account and GSTN *Subject:* Action Required: Confirm Your Bank Account Details and GSTN *Dear <Partner's Name>,* We hope this message finds you well. To ensure timely and accurate processing of your commission payments, we kindly request you to Confirm/Update your bank account details and GSTN (If applicable) in the link below. [Pre-filled Google Form Link] Best regards, Volt Team ## Commission Payout with GST Invoice *Subject:* Your Monthly Commission Statement and GST Invoice for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement and GST invoice attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt *Subject:* Your Monthly Commission Statement for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt

---

## #47 — Term Loan Communications
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

## #48 — Product note template (Duplicate this for use)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Product note template (Duplicate this for use) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics (Conversion rate / Error rate / TAT) - Define post launch good state (Expected behaviour / uptime / SR) - Guardrail metrics (Metrics that should not degrade) --- ## **3. Solution Scope** ### Solution overview - Explain in 2-3 lines the overview of the solution - Explain overview of the solution with key product and system changes - Explain the rationale on scoping/phasing of the solution - Call out scope that has been scoped out and explain the rationale ### Detailed solution scope: - Bullet list of user and system use cases that are supported: - Define all use cases applicable and what are in scope - Core happy path - Key edge cases that must be handled at launch - Consider all the stakeholders that are impacted - Has to answer questions like: - How does this change existing operational SOPs? - How does this change the experience for the end user? - How does this impact sales or onboarding conversations? | Description | Details | | --- | --- | | | | | | | | | | --- ## **5. High level s***ystem, user or process flow* - - Cover the overview of the process or the journey - Include error cases or edge cases (Optional) --- ## **6. Appendix (Optional)** ### Benchmarking: ### User feedback / Calling:

---

## #49 — User Story template
**Status:** Unknown | **Last edited:** Unknown

# User Story template # Guidelines **How should user stories be written?** - Each user story should be atomic — focus on one activity or action. - One feature needs to have multiple user stories for each activity. - For the UPI mandate registration feature, this will be: - Context page. - Mandate registration page. - UPI registration (TPAP). - Post-registration confirmation. - Retry or fallback, if required. - Each user story should be written from a user/customer perspective. - Users can be internal users like sales, support, or operations OR - User can be customer OR - User can be a partner (B2B or LSP) - User stories should document key scenarios and how they will be handled from a UI/UX perspective. - For the UPI mandate feature, this will be: - Mandate registration is pending due to user inactivity. - Mandate registration failure due to user error. - Mandate registration failure due to technical issues. - Mandate registration success. - Delayed confirmation handling. # Template Below is a template for User Stories. - **User Story ID**: this is a unique identifier in a PRD that is linked to a user story. This can be alphanumeric like U1 or US1, etc. - **User Story**: this will be a 1-2 liner that will talk about the user story in question. This will mention what the user is setting out to achieve. - **User requirements**: this will be the detailed requirements, by building which, the user will be able to achieve the requirement. # Example Below is a list of User Stories keeping UPI mandate registration as an example. - **U1**: As a customer, I want to know why a recurring debit needs to be setup so that I can move forward with setting up a mandate. **Flow**: Once the customer has completed the bank account verification step and the bank is verified, the customer is presented a screen to setup a auto-debit (mandate). **Success criteria**: The customer should be able to understand the rationale for an auto-debit and move forward in the journey. **Requirement**: Below are the requirements for this page. - Once the user lands on this page, the user should be conveyed that Volt will setup a mandate to debit the monthly interest. - This will be a common page that will cover both NACH and UPI mandate. - This page will describe that customer’s bank account will