# MFD Activation Journey

### Objective

To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details.

## Lead Creation Use Cases

The MFD activation journey must accommodate **multiple lead creation sources**, including:

1. **Bulk Uploads** – Admin-led upload of MFD leads in CRM.
2. **Partner Portal Submissions** – MFDs registering directly via the self-service partner dashboard.
3. **Third-Party Integrations** – Leads ingested via B2B partners and platforms such as **Redvision, Investwell, and other aggregator systems**.
4. **Webinars** – Leads generated through online events and webinars.
5. **In-Person Meetups** – Leads generated via offline events, roadshows, or branch interactions.
6. **Referral Programs** – Leads created through referral schemes from existing MFDs or partners.

The mfd activation journey opportunity schema:

| **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** |
| --- | --- | --- | --- | --- |
| Mobile Number | mx_Custom_13 | Phone | Volt backend |  |
| Opportunity Name | mx_Custom_1 | String | Volt backend | MFD Activation Journey |
| Owner | Owner | User | LSQ Automation |  |
| Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: MFD Activation Journey |
| Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:MFD is Activated-> Won, then the actual closure date is updated |
| Partner ID | MX_CUSTOM_94 | strind | Volt backend | Add the partner id |
| Status -> Status Stage | Status | Statusstring | Volt backend | Status = OPEN -> Unregistered/Registered/Empanelled/Partially Activated WON -> ActivatedLOST -> Not a MFD/Closed - Lost / Close Deferred / Invalid / Not Interested |
| Origin | mx_Custom_11 | String | Volt backend | It will be applicable for bulk upload |
| Source | Mx_Custom_3 | Source | Volt backend | Event/ Webinar |
| Name | mx_Custom_3 | String | Volt backend | Event name |
| Campaign | mx_Custom_20 | String | Volt backend | Marketting / WA |
| Medium | mx_Custom_21 | String | Volt backend | WA/ Email |
| Content | mx_Custom_23 | String | Volt backend | Marketing Content |
| First Name | mx_Custom_4 | String | Volt backend |  |
| Last Name | mx_Custom_57 | String | Volt backend |  |
| PAN | mx_Custom_59 | String | Volt backend |  |
| Follow Up Priority | mx_Custom_68 | Dropdown:Very highHighMediumlow | Automation |  |
| State | mx_Custom_15 | String | Volt backend |  |
| Zip | mx_Custom_16 | Number | Volt backend |  |
| Email | mx_Custom_12 | Email | Volt backend |  |
| Referred by | mx_Custom_42 | Dropdown:CustomerMFDNoneAFFILIATEINDIVIDUALEXTERNAL_MARKETINGPartner PlatformPlatformnullAffiliate | Volt backend |  |
| Referrer Name | mx_Custom_43 | String | Volt backend |  |
| Referrer Phone Number | mx_Custom_44 | Phone | Volt backend |  |
| Referral code | mx_Custom_45 | String | Volt backend |  |
| Referral Email | mx_Custom_46 | Email | Volt backend |  |
| Referral Platform | mx_Custom_47 | Dropdown:InvestwellVOLT_WEB_APPVOLT_API_UATVOLT_MOBILE_APPSDK_INVESTWELLASSET_PLUSZ_FUNDSVOLT_PARTNER_ANDROID_APPSANKASHMERCURYPHONEPEBHARAT_NXTBHARATNXTINDIFIFREOSWARAJ_FINPROJUPITERADVISOR_KHOJPARKPLUSBHARAT_PEZYPECREDBHARATFUNDS_INDIAVOLT_WEBREDVISIONNIYOTATADIGITALPRUDENTBHARAT_PE_2MYFICM_1INDIALENDSCM_2COMPOUNDEXPRESSLARKCHOICEINFINYTEARM_FINTECHWEALTHFIRSTENVESTOOLKACAPITALNOWTIDE1FLIPKARTINCREDVOLTSETTLECHEQMOOLAAHMOBIKWIKROYALFINSERVCASHESPOCTREESAARATHI | Volt backend |  |
| Referrer Account Id | mx_Custom_48 | String | Volt backend |  |
| Opportunity Status | mx_Custom_56 | Dropdown:ActiveDrop-off | Volt backend | Logic :- Activity must be on hours not on days if the activty is not their for more than 24 hours then it is drop off |
| City | mx_Custom_58 | String | Volt backend |  |
| Opportunity Type | mx_Custom_26 | Dropdown:MFD | Volt backend |  |
| Priority | mx_Custom_40 | Number | Automations |  |
| Follow Up Count | mx_Custom_62 | Number | Automations | Logic : on every form dispostin the follow up coount iwll increase |
| Platform | mx_Custom_63 | String | Volt backend | NA |
| Platform ID | mx_Custom_64 | String | Volt backend |  |
| Channel | mx_Custom_65 | String | Volt backend |  |
| Opportunity Closed bY | mx_Custom_70 | String | automations | required |
| Zero Touch | mx_Custom_71 | Dropdown:YesNo | automations | required |
| Notes | ActivityEvent_Note | String | Volt backend |  |
| Created by | CreatedBy | User | Volt backend |  |
| Created On | CreatedOn | DateTime | Volt backend |  |
| Modified By | ModifiedBy | User | automations |  |
| Modified On | ModifiedOn | DateTime | automations |  |
| Product | mx_Custom_10 | Product | Volt backend | LAMF/ LAS |
| Alt Phone number | mx_Custom_14 | Phone | Automations |  |
| Initial UTM Trigger Date | mx_Custom_92 | Datetime | Volt backend |  |
| Initial UTM Campaign Source | mx_Custom_28 | String | Volt backend |  |
| Initial UTM Campaign Name | mx_Custom_29 | String | Volt backend |  |
| Initial UTM Campaign Medium | mx_Custom_30 | String | Volt backend |  |
| Initial UTM Campaign ID | mx_Custom_31 | String | Volt backend |  |
| Initial UTM Campaign Term | mx_Custom_32 | String | Volt backend |  |
| Initial UTM Campaign Content | mx_Custom_33 | String | Volt backend |  |
| Last UTM Trigger date | mx_Custom_92 | Datetime | Volt backend |  |
| Last UTM Campaign Source | mx_Custom_34 | String | Volt backend |  |
| Last UTM Campaign Name | mx_Custom_35 | String | Volt backend |  |
| Last UTM Campaign Medium | mx_Custom_36 | String | Volt backend |  |
| Last UTM Campaign ID | mx_Custom_37 | String | Volt backend |  |
| Last UTM Campaign Term | mx_Custom_38 | String | Volt backend |  |
| Last UTM Campaign Content | mx_Custom_39 | String | Volt backend |  |
| Application created timestamp | mx_custom_83 | Datetime | Volt backend | When the partnerAccountId is created |
| Activity Dates | mx_custom_76 | Datetime | Volt backend |  |
| MFD Tier | MX_CUSTOM_95 | string | Volt backend | Phase 2 |
| Empanelment Date | MX_CUSTOM_96 | Datetime | Automations |  |
| Activation Date | MX_CUSTOM_97 | Datetime | Automations |  |
| mailing preferences | MX_CUSTOM_98 | string | Volt backend | It is coming now please check |
| empaneled by | MX_CUSTOM_99 | string | Automations |  |
| activated by | MX_CUSTOM_100 | string | Automations |  |
| Total partner referral Count | mx_Custom_84 | Number | Volt backend |  |
| Total Application Completed Count | mx_Custom_49 | Number | Volt backend |  |
| Total Application Pending Count | mx_Custom_85 | Number | Volt backend |  |
| Total Pending Asset Pledge | mx_Custom_86 | Number | Volt backend |  |
| Total Pending KYC | mx_Custom_87 | Number | Volt backend |  |
| Total Pending Bank Verification | mx_Custom_88 | Number | Volt backend |  |
| Total Pending Agreement | mx_Custom_89 | Number | Volt backend |  |
| Total Pending Mandate | mx_Custom_51 | Number | Volt backend |  |
| Total Referred leads | mx_custom_41 | Number | Volt backend |  |
| Total cases in T-30D | mx_custom_24 | Number | Volt backend |  |
| Total cases in T-30D (Eligible) | mx_custom_6 | Number | Volt backend |  |
| Pending cases in T-30D (eligible only) | mx_custom_7 | Number | Volt backend |  |
| Referrer Tier | mx_custom_5 | string | Volt backend |  |
| Partner Referral links | mx_custom_52 | string | Volt backend |  |
| Customer Referral Links | mx_custom_53 | string | Volt backend |  |
| ARN | mx_custom_54 | string | Volt backend |  |

# PRD: MFD Activation Journey

## Objective

To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details.

---

## Opportunity Activity Flows

1. **Unregistered → Registered → Empanelled**
    - New MFD lead enters as *Unregistered*.
    - On registration, moves to *Registered*.
    - Once empanelment is complete (ARN / payout details verified), moves to *Empanelled*.
2. **Empanelled → Customer Referred → Customer Loan Created (Activated)**
    - An empanelled partner can start referring customers.
    - Each referral creates a *Partially Referred* activity.
    - Once a referred customer successfully takes a loan, the MFD lead moves to *Activated*.
3. **Daily Data Sync / Updates**
    - Partner details (ARN, payout details, referral link, performance metrics) updated daily for reporting & compliance.

## Activity - stage Mapping:

### 1. **Unregistered**

- **Use Cases**:
    - Bulk Upload → Lead created in system as Unregistered.
    - Partner Portal → New user account created as Unregistered until registration is completed.
    - Integrations (Redvision, Investwell, other B2B platforms) → Lead created as Unregistered upon ingestion.
    - Webinars → Lead created post-event registration, initially as Unregistered.
    - In-Person Meetups → Lead created manually by event staff or upload.
    - Referral Programs → Lead created upon referral submission, initially as Unregistered.
- **Stage**: *Unregistered*
- **Frequency**: Once per lead.

### 2. **Registered**

- **Use Cases**:
    - Partner Portal → Registration via portal.
    - Integrations → Automated registration if data contains required details, or manual completion later.
    - Webinars / Meetups / Referrals → Registration happens when lead confirms or is onboarded.
- **Stage**: *Registered*
- **Frequency**: Once per lead.

### 3. **Empanelled**

- **Use Cases**:
    - All sources → Empanelment occurs after verification of ARN, partner details, and compliance checks.
- **Stage**: *Empanelled*
- **Frequency**: Once per lead.

### 4. **Partner Details Updated**

- **Use Cases**:
    - Bulk Upload → Initial details captured during upload.
    - Partner Portal → Details updated during registration.
    - Integrations → Partner details updated from partner system data.
    - Webinars / Meetups / Referrals → Partner details added manually or through follow-up actions.
- **Stage**: *(Attributes, not stage change)*
- **Frequency**: Initially once; daily updates thereafter.

### 5. **Customer Referred**

- **Use Cases**:
    - Applicable only after partner is empanelled.
    - Referral can originate via partner portal, direct submission, integration feeds, or manual input from events/referral programs.
- **Stage**: *Partially Referred*
- **Frequency**: Multiple (per referred customer).

### 6. **Customer Loan Created**

- **Use Cases**:
    - All sources → When a referred customer successfully takes a loan.
- **Stage**: *Activated*
- **Frequency**: Multiple (per customer loan).

### 7. **Daily Partner Details Update**

- **Use Cases**:
    - All sources → Daily updates run for all MFD records irrespective of source.
- **Stage**: *(Attributes update)*
- **Frequency**: Daily.

By linking activities to **specific lead creation use cases**, we ensure:

- Accurate tracking of partner onboarding across different channels.
- Proper attribution of leads to their sources.
- Consistency in CRM stage updates irrespective of lead origin.
- Better reporting of channel performance and partner conversion rates.