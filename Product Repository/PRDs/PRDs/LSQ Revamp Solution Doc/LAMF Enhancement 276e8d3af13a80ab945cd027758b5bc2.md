# LAMF Enhancement

## Objective

To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities.

Schema and fields:

| **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** |
| --- | --- | --- | --- | --- |
| Associated Lead |  | Hyperlink | This will be a phone number to redirect to lead |  |
| Mobile Number | mx_Custom_13 | Phone | Volt backend |  |
| Opportunity Name | mx_Custom_1 | String | Volt backend |  |
| Owner | Owner | User | LSQ Automation |  |
| Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES |
| Excepted Closure Date | mx_Custom_8 | DateTime | Not Required |  |
| Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated |
| Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id |
| Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank |
| Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION |
| Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION |
| Name | mx_Custom_3 | String | Not Required |  |
| Campaign | mx_Custom_20 | String | Not Required |  |
| Medium | mx_Custom_21 | String | Not Required |  |
| Term | mx_Custom_22 | String | Not Required |  |
| Content | mx_Custom_23 | String | Not Required |  |
| First Name | mx_Custom_4 | String | Volt backend |  |
| Last Name | mx_Custom_57 | String | Volt backend |  |
| KFIN Limit | mx_Custom_52 | Number | Volt backend |  |
| KFIN CAMS Limit | mx_Custom_54 | Number | Volt backend | Need to be changed to Eligible Limit |
| MFC Limit | mx_Custom_51 | Number | Volt backend |  |
| CAMS Limit | mx_Custom_53 | Number | Volt backend |  |
| PAN | mx_Custom_59 | String | Volt backend |  |
| Lender Name | mx_Custom_27 | Dropdown:DSPTataBajaj | Volt backend | - if in eleavte 2 opportunity |
| Borrower Account Id | mx_Custom_18 | String | Volt backend |  |
| Purpose of Loan | mx_Custom_69 | Dropdown:Home Purchase/ConstructionVacationFamily Function/MarriageConsolidate ongoing loansMedical EmergencyIPOEducation/ Professional CourseBusiness / Working capitalReal Estate InvestmentRe-investment in digital assetsCredit card bill PaymentAuto LoanOthers | not required | not required |
| Follow Up Priority | mx_Custom_68 | Dropdown:Very highHighMediumlow | Automation |  |
| State | mx_Custom_15 | String | Backend |  |
| Zip | mx_Custom_16 | Number | Backend | NOT REQUIRED |
| Email | mx_Custom_12 | Email | Backend |  |
| Date of Birth | mx_Custom_17 | DateTime | Backend | NOT REQUIRED |
| Last Stage |  |  | NOT REQUIRED | NOT REQUIRED |
| Referred by | mx_Custom_42 | Dropdown:CustomerMFDNoneAFFILIATEINDIVIDUALEXTERNAL_MARKETINGPartner PlatformPlatformnullAffiliate | Backend |  |
| Referrer Name | mx_Custom_43 | String | Backend |  |
| Referrer Phone Number | mx_Custom_44 | Phone | Backend |  |
| Referral code | mx_Custom_45 | String | Backend |  |
| Referral Email | mx_Custom_46 | Email | Backend | NOT REQUIRED |
| Referral Platform | mx_Custom_47 | Dropdown:InvestwellVOLT_WEB_APPVOLT_API_UATVOLT_MOBILE_APPSDK_INVESTWELLASSET_PLUSZ_FUNDSVOLT_PARTNER_ANDROID_APPSANKASHMERCURYPHONEPEBHARAT_NXTBHARATNXTINDIFIFREOSWARAJ_FINPROJUPITERADVISOR_KHOJPARKPLUSBHARAT_PEZYPECREDBHARATFUNDS_INDIAVOLT_WEBREDVISIONNIYOTATADIGITALPRUDENTBHARAT_PE_2MYFICM_1INDIALENDSCM_2COMPOUNDEXPRESSLARKCHOICEINFINYTEARM_FINTECHWEALTHFIRSTENVESTOOLKACAPITALNOWTIDE1FLIPKARTINCREDVOLTSETTLECHEQMOOLAAHMOBIKWIKROYALFINSERVCASHESPOCTREESAARATHI |  |  |
| Referrer Account Id | mx_Custom_48 | String | REQUIRED |  |
| Aadhaar Number | mx_Custom_50 | String | NOT REQUIRED |  |
| Opportunity Status | mx_Custom_56 | Dropdown:ActiveDrop-off | BACKEND | Logic :- Activity must be on hours not on days if the activty is not their for more than 24 hours then it is drop off |
| City | mx_Custom_58 | String | BACKEND |  |
| MFC Fetched | mx_Custom_60 | Dropdown:YesNo | NOT REQUIRED |  |
| Lead Type | mx_Custom_26 | Dropdown:CustomerMFD | BACKEND | RENAME THIS |
| Priority | mx_Custom_40 | Number |  | to be picked up later this will be a score post call priority logic is defined |
| Follow Up Count | mx_Custom_62 | Number | Automations | Logic : on every form dispostin the follow up coount iwll increase |
| Platform | mx_Custom_63 | String | Not required | Already populating in Reffered platform |
| PLatform ID | mx_Custom_64 | String | Not required |  |
| Channel | mx_Custom_65 | String | backend | required |
| CAMS Pledged Value | mx_Custom_66 | Number | backend | required |
| KFIN PLedged Value | mx_Custom_67 | Number | backend | required |
| Opportunity Closed bY | mx_Custom_70 | String | automations | required |
| Zero Touch | mx_Custom_71 | Dropdown:YesNo | automations | required |
| Processing Fee | mx_Custom_72 | Number | backend | required |
| ROI | mx_Custom_73 | Number | backend | required |
| Sanction Limit | mx_Custom_74 | Number | backend | ex: dsp - 2 cr and tata - 1 cr please flow backe ndd limit |
| Notes | ActivityEvent_Note | String | backend | required |
| Description | mx_Custom_5 | String | - | to be checked |
| Created by | CreatedBy | User |  |  |
| Created On | CreatedOn | DateTime | backend |  |
| Modified By | ModifiedBy | User | automations | same as earlier |
| Modified On | ModifiedOn | DateTime | automations | same as earlier |
| Excepted Deal Size | mx_Custom_6 | Number | backend | selected loan amount - must be the column nameNew Requirement |
| Actual Deal Size | mx_Custom_7 | Number | not required | eligible limit |
| Product | mx_Custom_10 | Product |  | lamf,lmf temm , lasNew Requirement |
| Alt Phone number | mx_Custom_14 | Phone |  | Not valid scenario - We can't capture two phone number against one customer |
| Current Application Step Id | mx_Custom_24 | String |  | To be checked |
| Initial UTM Campaign Source | mx_Custom_28 | String |  |  |
| Initial UTM Campaign Name | mx_Custom_29 | String |  |  |
| Initial UTM Campaign Medium | mx_Custom_30 | String |  |  |
| Initial UTM Campaign ID | mx_Custom_31 | String |  |  |
| Initial UTM Campaign Term | mx_Custom_32 | String |  |  |
| Initial UTM Campaign Content | mx_Custom_33 | String |  |  |
| Last UTM Campaign Source | mx_Custom_34 | String |  |  |
| Last UTM Campaign Name | mx_Custom_35 | String |  |  |
| Last UTM Campaign Medium | mx_Custom_36 | String |  |  |
| Last UTM Campaign ID | mx_Custom_37 | String |  |  |
| Last UTM Campaign Term | mx_Custom_38 | String |  |  |
| Last UTM Campaign Content | mx_Custom_39 | String |  |  |
| Application Next Step | mx_Custom_41 | Dropdown:Fetch PortfolioPledgePortfolioKYCAgreementLink BankMandatePhoto VerificationSubmit loan applicationLoan approval | not required |  |
| Auto ID | ProspectActivityAutoId | AutoId |  |  |
| MFC Total portfolio value |  |  | Field to be created | New Requirement |
| CAMS Total MF amount |  |  | Field to be created | New Requirement |
| KFIN Total MF amount |  |  | Field to be created | New Requirement |
| First Login timestamp |  |  |  | - exceptation is opportunity creation on must be the time when the cutomer is coming on that particualr request. - this is opportunity created on- lead created on must be woking as currently |
| MFC Pledged value |  |  |  | Need to be added and be worked by backend team(LOS) |
| Referrer Tier |  |  | New Requirement |  |
| Activity Dates |  |  |  |  |
| total Pledge value |  |  |  |  |

## Opportunity Name

**CREDIT MODIFICATION AGAINST Securities - LAMF**

(also referred to as **LAMF Enhancement Opportunity**)

## Trigger Logic

- Once a **LAMF Opportunity** is successfully created (Loan Active), the **enhancement opportunity** becomes eligible.
- The enhancement is triggered when:
    1. The customer explicitly requests an increased credit limit.
    2. System detects additional pledgeable securities (via new portfolio fetch).

## Flow & Events

1. **Customer Initiates Enhancement**
    - **Trigger**: Customer clicks "Increase Limit" / initiates portfolio re-fetch for enhancement.
    - **Event**:  New Opportunity created
2. **Portfolio Fetch for Enhancement**
    - **Trigger**: System fetches updated portfolio from MFC/CAMS/KFin.
    - **Event**: Portfolio Fetch using MFC / Portfolio Fetch using CAMS / Portfolio Fetch using KFIN
    - **Lead Stage**: *Portfolio Fetch*
3. **Offer Page (Enhanced Credit Offer)**
    - **Trigger**: Enhanced credit terms (new limit, ROI, tenure impact) displayed.
        - **Event**: Offer Page
    - **Lead Stage**: *Offer Page*
4. **Pledge Additional Securities**
    - **Trigger**: Customer pledges additional MF units.
    - **Event**:
        - MFC → MF Pledge using MFC
        - CAMS → MF Pledge using CAMS
        - KFIN → MF Pledge using KFIN
    - **Lead Stage**: Portfolio pledge
5. **Agreement Update**
    - **Trigger**: Customer signs modified agreement (if required by lender).
    - **Event**: Sign agreement Started
    - **Lead Stage**: Sign Agreement
6. **Credit Approval**
    - **Trigger**: Post-sign agreement the credit approval is triggered
    - **Event**: Credit Approval
    - **Lead Stage**: Credit Approval
7. **Loan Created**
    - **Trigger**: Once the credit approval is done, the loan is created, and the updated value will be added to the customer.
    - **Event**: Loan Created
    - **Lead Stage**: *Loan Created*

---

## Business Rules

- Only **one active enhancement opportunity** should exist per LAMF loan at a time.
- Enhancement can only be initiated **after the base LAMF loan is active**.
- If the pledge attempt fails, the opportunity stays in *Enhancement Pledge In Progress*.
- The enhanced limit must be stored as a separate field (enhanced credit limit) alongside the original sanctioned limit for audit purposes.
- Enhancements should **not overwrite the base LAMF opportunity; instead, they** must be a linked but separate opportunity type.

A separate smart view must be created, and automations must be created.

The smart view is as below:

The automations required are as below: