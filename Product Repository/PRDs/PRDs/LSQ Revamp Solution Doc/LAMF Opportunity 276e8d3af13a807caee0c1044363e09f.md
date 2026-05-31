# LAMF Opportunity

The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema.

Below mentioned is the opportunity schema of the LAMF opportunity: 

| **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** |
| --- | --- | --- | --- | --- |
| Associated Lead |  | Hyperlink | This will be a phone number to redirect to lead |  |
| Mobile Number | mx_Custom_13 | Phone | Volt backend |  |
| Opportunity Name | mx_Custom_1 | String | Volt backend |  |
| Owner | Owner | User | LSQ Automation |  |
| Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES |
| Excepted Closure Date | mx_Custom_8 | DateTime | Not Required |  |
| Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated |
| Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id |
| Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank |
| Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION |
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
| Created by | CreatedBy | User |  | Vijay to check |
| Created On | CreatedOn | DateTime | backend | Vijay to check |
| Modified By | ModifiedBy | User | automations | same as earlier |
| Modified On | ModifiedOn | DateTime | automations | same as earlier |
| Excepted Deal Size | mx_Custom_6 | Number | backend | selected loan amount - must be the column nameNew Requirement |
| Actual Deal Size | mx_Custom_7 | Number | not required | eligible limit |
| Product | mx_Custom_10 | Product |  | lamf,lmf temm , lasNew Requirement |
| Alt Phone number | mx_Custom_14 | Phone |  | Not valid scenario - We can't capture two phone number against one customer |
| Current Application Step Id | mx_Custom_24 | String |  | To be checked |
| Initial UTM Campaign Source | mx_Custom_28 | String |  | Vijay to create in LAMF |
| Initial UTM Campaign Name | mx_Custom_29 | String |  | Vijay to create in LAMF |
| Initial UTM Campaign Medium | mx_Custom_30 | String |  | Vijay to create in LAMF |
| Initial UTM Campaign ID | mx_Custom_31 | String |  | Vijay to create in LAMF |
| Initial UTM Campaign Term | mx_Custom_32 | String |  | Vijay to create in LAMF |
| Initial UTM Campaign Content | mx_Custom_33 | String |  | Vijay to create in LAMF |
| Last UTM Campaign Source | mx_Custom_34 | String |  | Vijay to create in LAMF |
| Last UTM Campaign Name | mx_Custom_35 | String |  | Vijay to create in LAMF |
| Last UTM Campaign Medium | mx_Custom_36 | String |  | Vijay to create in LAMF |
| Last UTM Campaign ID | mx_Custom_37 | String |  | Vijay to create in LAMF |
| Last UTM Campaign Term | mx_Custom_38 | String |  | Vijay to create in LAMF |
| Last UTM Campaign Content | mx_Custom_39 | String |  | Vijay to create in LAMF |
| Application Next Step | mx_Custom_41 | Dropdown:Fetch PortfolioPledgePortfolioKYCAgreementLink BankMandatePhoto VerificationSubmit loan applicationLoan approval | not required |  |
| Auto ID | ProspectActivityAutoId | AutoId |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| MFC Total portfolio value |  |  | Field to be created | New Requirement |
| CAMS Total MF amount |  |  | Field to be created | New Requirement |
| KFIN Total MF amount |  |  | Field to be created | New Requirement |
| First Login timestamp |  |  |  | - exceptation is opportunity creation on must be the time when the cutomer is coming on that particualr request. - this is opportunity created on- lead created on must be woking as currently |
| MFC Pledged value |  |  |  | Need to be added and be worked by backend team(LOS) |
| Referrer Tier |  |  | New Requirement |  |
| Activity Dates |  |  |  |  |
| total Pledge value |  |  |  |  |

## The activities passed to this Opportunity are as below:

| **Activity** | **Stage Names** | **Testing Status** |
| --- | --- | --- |
| MFC Limit Fetched | Portfolio Fetch | Done |
| Portfolio Fetch Started | Portfolio fetch by MFC | Done |
| Portfolio Fetch Started CAMS | Portfolio fetch by CAMS | Done |
| Portfolio Fetch Started KFIN | Portfolio fetch by KFIN | Done |
| Offer Page | Credit Offer Page | Done |
| KYC Verification Started | KYC Verification | Done |
| Photo Verification Started | Photo Verification | Done |
| Link Bank Account Started | Link Bank Account | Done |
| Set Up Mandate Started | Setup Mandate | Done |
| Portfolio Pledge Started | Portfolio Pledge | Done |
| MF Pledged Using MFC | Portfolio Pledge MFC | NEED TO TEST |
| MF Pledged Using CAMS | Portfolio Pledge CAMS | Done |
| MF Pledged Using KFIN | Portfolio Pledge KFIN | Done |
| Sign Agreement Started | Sign Agreement | Done |
| Credit Approval | Credit Approval | Done |
| Loan Created | Loan Created | Done |

## The smart views which will be created for the LAMF opportunity are as below:

| **B2C & B2B Opportunitues** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Opportunity created date** | **Lead Name** | **Phone number** | **Fetched Eligible Limit** | **Opportunity Type** | **Owner of opportunity** | **Platform** | **Lead Stage** | **Last Activity** | **User activity date** | **Last Disposition** | **Last sub disposition** | **Outbound attempted** | **Outbound connected** | **Opportunity Status** | **Follow up Date** |  |  |  |
|  |  |  |  |  |  |  |  |  |  | xyz | xyz | Yes/No | Yes/No | Open/Lost/Won |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **B2B2C--> Customer lead as opportunity** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Opportunity created date** | **Lead Name** | **Phone number** | **Fetched Eligible Limit** | **Opportunity Type** | **Owner of opportunity** | **MFD Name** | **MFD Phone** | **MFD Tier** | **Pending cases in T-30D (eligible only)** | **Platform** | **Lead Stage** | **Last Activity** | **User activity date** | **Last Disposition** | **Last sub disposition** | **Last connected date** | **Opportunity Status** | **Follow up Date** |
|  |  |  |  | B2B |  |  |  | Super Gold/Gold/Silver/Bronze |  |  |  |  |  | xyz | xyz |  | Open/Lost/Won |  |

In the lamf opportunity is created on the mfc limit fetched :
here is the list of activities which will be created for the lamf opportunity:

### 1. **Portfolio Fetch**

**MFC Limit Fetched**

### **Scenario 1 :**

- **When triggered**: After PAN verification, system calls MFC to fetch eligible limit.
- **Purpose**: Establishes the maximum loan value customer can avail based on portfolio with MFC.
- **Event**: MF Fetched Using MFC
- **Lead Stage**: Portfolio Fetch/ Opportunity Capture
- **Why important**: This is the first confirmation that customer is eligible for a loan.
    - This is the trigger for the opportunity capture
- Fields to be updated are :
    - **MFCEligibleCreditLimit** : Ex: 25000 (Limit of the customer)
    - **MFCTotalPortfolioValue** : Ex: 35000 (Total Value of the customer)

### Scenario 2:

- **When triggered**: Once customer chooses to proceed, system starts fetching mutual fund portfolio.
- **Purpose**: Get complete MF portfolio from RTA’s (CAMS/KFin).
- **Event**: MF Fetched Using CAMS
- **Lead Stage**: Portfolio fetch using CAMS
- Fields to be updated are :
    - **CAMS Eligible Limit :** Ex: 25000 (Limit of the customer)
    - **CAMS Total MF Amount:** Ex: 50000 (Total Value of the customer)

### Scenario 3:

- **When triggered**: Once customer chooses to proceed, system starts fetching mutual fund portfolio.
- **Purpose**: Get complete MF portfolio from RTA’s (CAMS/KFin).
- **Event**: MF Fetched Using KFIN
- **Lead Stage**: Portfolio fetch using KFIN
- Fields to be updated are :
    - **KFIN Eligible Limit** : Ex: 25000 (Limit of the customer)
    - **KFIN Total MF Amount  :** Ex: 35000 (Total Value of the customer)

In addition, we need to update the field **Total Eligible Limit** as per the following logic:

- **Scenario 1: MFC Limit Fetch**
    
    Total Eligible Limit = MFCEligibleCreditLimit
    
- **Scenario 2: CAMS + KFIN Fetch**
    
    Total Eligible Limit = CAMS Eligible Limit + KFIN Eligible Limit
    

### **Opportunity Capture:**

- **When triggered**: Once customer Completes the successful fetch.
- **Purpose**:  Creation of the opportunity in the LSQ to mark the start of the customer journey
- **Event**: Opportunity Capture
- **Lead Stage**: Portfolio Fetch/Portfolio fetch using KFIN/Portfolio fetch using CAMS

After a successful portfolio fetch, only **one LAMF opportunity** should be created, even if multiple fetches are performed for the same phone number.

The opportunity must capture the following fields:

| Opportunity Name | Loan Against Mutual Fund |
| --- | --- |
| Stage | Portfolio fetch |
| Mobile Number | +91-9900713057 |
| Borrower Account Id | 4c69f666-2e28-4ac1-b6f6-ce997106a84e |
| Current Application Type | CREDIT_AGAINST_SECURITIES_BORROWER |
| Lender Name | DSP |
| Referred By | None |
| Referral PlatformV | VOLT_WEB_APP |
| Total Eligible Limit | 44400 |
| Opportunity Status | Active |
| Opportunity Type | Customer |
| Platform Id | 6d450a88-8312-4398-b7a6-65b27bd5b980 |
| Channel | B2C |
| Notes |  |
| UpdateEmptyFields | TRUE |
| DoNotChangeOwner | TRUE |
| Lead Source | Organic |
| Search By | Phone |

### **Offer Page (Credit Offer Page)**

- **When triggered**: After portfolio is successfully fetched, system shows loan offer (limit, tenure, ROI, etc.).
- **Purpose**: First customer-facing credit proposition.
- **Event**: Offer Page
- **Lead Stage**: Offer page
- **Why important**: This particular screen shows the customer the eligible limit and the ROI and the tenure of the loan so all this details is important

### **KYC Verification Started**

- **When triggered**: User clicks “Start KYC” after reviewing offer.
- **Purpose**: Begin CKYC/Digilocker verification to validate identity.
- **Event**: KYC Verification Started
- **Lead Stage**: KYC Verification
- The additional field which will be updated using the KYC verification are as below:
    - First name
    - Last name

### **Photo Verification Started**

- **When triggered**: During KYC, user uploads/takes selfie with liveliness detection.
- **Purpose**: Face match against PAN/Aadhaar photo.
- **Event**: Photo Verification Started
- **Lead Stage**: KYC Verification

### **Link Bank Account Started**

- **When triggered**: After KYC, user provides bank details for disbursal and repayment.
- **Purpose**: Verify bank account ownership via penny-drop/NetBanking.
- **Event**: Link Bank Account Started
- **Lead Stage**: Portfolio Pledge
- **Why important**: Ensures disbursement goes to the right account, mandatory for mandate setup.

### **Set Up Mandate Started**

- **When triggered**: Once bank is linked, user sets up eNACH/eMandate.
- **Purpose**: Create auto-debit authorization for EMI repayment.
- **Event**: Set up Mandate Started
- **Lead Stage**: *Mandate In Progress*
- **Why important**: Without mandate, loan cannot be disbursed. It’s a core risk control step.

### 9. **Portfolio Pledge Started**

- **When triggered**: User initiates pledge of MF units.
- **Purpose**: Secure loan by pledging portfolio as collateral.
- **Event**: Portfolio Pledge Started
- **Lead Stage**: *Portfolio Pledge*
- **Why important**: This is the collateralization step — ensures lender has security against the loan.

### **MF Pledged Using MFC / CAMS / KFIN**

- **When triggered**: Pledge confirmation received from respective RTA.
- **Purpose**: Capture source system that successfully pledged units.
- **Events**:
    - MFC → MF Pledge using MFC
    - CAMS → MF Pledge using CAMS
    - KFIN → MF Pledge using KFIN
- **Lead Stage**: Portfolio *Pledge*
- **Why important**: Confirms collateral is locked, making customer eligible for loan approval.

### **Sign Agreement Started**

- **When triggered**: User opens and e-signs loan agreement (Aadhaar/OTP).
- **Purpose**: Legal binding contract between lender and borrower.
- **Event**: Sign Agreement Started
- **Lead Stage**: **Sign Agreement**
- **Why important**: Without agreement, loan disbursal cannot happen legally.

### **Credit Approval**

- **When triggered**: Underwriting engine validates all steps (KYC, pledge, mandate) and approves loan.
- **Purpose**: Internal approval confirmation before loan creation.
- **Event**: Credit Approval
- **Lead Stage**: Credit Approval
- **Why important**: This is the last internal checkpoint before creating the loan account.

### **Loan Created**

- **When triggered**: Loan account successfully created in LMS and disbursal instruction is placed.
- **Purpose**: Marks conversion of lead into a customer with active loan.
- **Event**: Loan Created
- **Lead Stage**: Loan Created
- **Why important**: Final milestone — indicates successful loan journey completion.

**IMP :** The development for the MFD Details must be shared to the Analytics team as we currently do not have MFD tiering in the backend :

<aside>
💡

Post development of the MFD tiering the data will be added in the opportunity.
The MFD tiering development must be taken up separately and the logic to be shared by business and sales.

</aside>

The required data is as below :

1. MFD wise tiering
2. MFD AUM
3. MFD Phone number
4. MFD Leads/Applications
5. Total Referred till date
6. Total Converted till date
7. Platform - (Redvision /Invest well / Volt web app)

The Automation required post development will be captured here :