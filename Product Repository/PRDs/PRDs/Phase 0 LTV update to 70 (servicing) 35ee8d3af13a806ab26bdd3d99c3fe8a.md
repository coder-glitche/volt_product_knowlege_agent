# Phase 0 : LTV update to 70 (servicing)

: Ameya Aglawe
Created time: May 12, 2026 10:55 AM
Status: Pending Review
Last edited: May 15, 2026 5:47 PM

# **Background and Context**

- Existing customers on the LTV 45 product currently do not have a standardized flow for migrating to the higher LTV 70 product.
- LSPs require a structured mechanism to:
    - Check customer eligibility for higher LTV products
    - Generate and validate eligible offers
    - Capture revised commercial terms like ROI, tenure, AMC and enhancement charges
    - Submit and operationalise the contract update
- Multiple parallel business initiatives including tenure increase, AMC charge application, PTC and Put/Call related changes are also coupled on this migration framework.
- Operations teams currently do not have a centralized approval and visibility workflow for such loan contract updates.
- Without validations and approval workflows:
    - Incorrect offers may get accepted
    - Invalid ROI or fee configurations may get processed
    - Loan contract inconsistencies can occur
    - Operational tracking and auditability become difficult

---

# **1. Problem Scope**

## In scope

- Enable LSPs to support migration of existing customers from LTV 45 to LTV 70 product
- Eligibility validation for existing contracts basis current holdings
- Offer generation with configurable commercial ranges:
    - ROI
    - AMC charges
    - Limit enhancement charges
    - Tenure
    - Eligible LTV
- Validation of selected offer parameters before offer acceptance
- Loan contract/KFS/agreement generation for updated contract
- Service request creation for operational approval
- Checker approval workflow in Command Centre
- Visibility enhancements in Command Centre for:
    - Request details
    - Loan details
    - Collateral details
    - Loan kit
- Customer communications
- Handling edge cases
    - Parallel add collateral request
    - Add collateral request post service request

### Primary users

- LSPs
- Operations team
- Internal business teams

### Secondary users

- Existing loan customers migrating to higher LTV product

## Out of scope

- Automatic/STP approval of service requests
- New loan onboarding journeys
- Manual contract modification outside APIs
- Automated handling of parallel collateral addition requests

### Rationale for exclusion

- Approval workflow requires operational oversight in initial phases
- Scope is restricted to existing contract enhancement use cases
- Parallel request orchestration will initially follow controlled N-STP handling

---

# **2. Success Criteria**

- Successful migration of eligible LTV 45 customers to LTV 70 product through API-driven workflow
- Reduction in operational dependency for manual contract validations
- Accurate validation of:
    - ROI ranges
    - Fee ranges
    - LTV configurations
    - Tenure ranges

### Key success metrics

- Service request success rate
- Offer acceptance success rate
- Contract generation success rate
- Checker approval TAT
- Reduction in invalid offer configurations

### Post-launch expected state

- LSPs can independently complete end-to-end LTV upgrade journey
- All approved requests correctly update customer collateral limits
- Operational teams get complete audit visibility within Command Centre

### Guardrail metrics

- No incorrect collateral limit updates
- No unauthorized ROI/fee overrides
- No degradation in existing collateral addition flows
- No contract generation failures post offer acceptance

---

# **3. Solution Scope**

## Solution overview

- LTV update for existing customers will be implemented as a service request-based workflow initiated by LSPs. The workflow enables eligibility validation, offer generation, offer acceptance, loan contract generation and operational approval for migrating customers from LTV 45 to LTV 70 product.
- The service request framework is being designed as an extensible platform that can support future use cases like sanction limit updates and other contract modification journeys.
- Operational approval will be managed through Command Centre checker workflows to ensure controlled rollout and auditability.

---

## Detailed solution scope

### Supported use cases

- Existing customer eligibility validation for higher LTV product
- Offer generation for eligible contracts
- Validation of selected commercial parameters
- Loan contract and KFS generation
- Service request creation and approval
- Collateral limit enhancement post approval
- Command Centre visibility for operations teams
- Handling of concurrent collateral addition requests

---

## High-level API workflow

| Description | Details |
| --- | --- |
| Check eligibility | LSP calls `checkEligibleContracts` API using `fenix_loan_account_id` |
| Eligibility response | API validates current contract and returns eligible contract type and updated drawing power |
| Generate offer | LSP calls Offer Generation API with loan account ID, product name and assets |
| Offer response | API returns eligible funds, LTVs, ROI ranges, AMC ranges, enhancement fee ranges and tenure ranges |
| Accept offer | LSP submits selected fund-level LTV, fees and ROI configuration |
| Offer validation | Fenix validates ROI, fees and LTV configurations |
| Offer acceptance response | Offer ID returned upon successful validation |
| Generate contract | LSP calls Generate Loan Contract API with Offer ID and loan account ID |
| Contract response | API returns KFS Utility ID and Agreement Utility ID |
| Submit service request | LSP submits service request with loan account ID, KFS Utility ID and Agreement Utility ID |
| Operational approval | Checker task created in Command Centre for approval |
| Final contract update | Upon approval, customer collateral limit gets updated |

---

## API level deep dive

### 1. `checkEligibleContracts` API

### Request input

- `fenix_loan_account_id`

### Functional behaviour

- Validates existing loan contract
- Checks eligibility for higher LTV product
- Calculates updated drawing power basis higher LTV

### Sample response

| Field | Sample value |
| --- | --- |
| Contract type | `LTV_70` |
| Updated drawing power | `10,000` |

---

### 2. Offer Generation API

### Request input

- `fenix_loan_account_id`
- `productName`

### Response output

- Eligible funds
- Eligible LTVs
- ROI ranges
- AMC charge ranges
- Limit enhancement fee ranges
- Tenure ranges

---

### 3. Accept Offer API

### Request input

- Selected funds
- Fund level LTV
- ROI
- AMC charges
- Enhancement fees
- Tenure

### System validations

- ROI range validation
- Fee range validation
- LTV validation
- Fund eligibility validation

### Response output

- `offer_id`
- credit limit
- fund value
- funds with respective LTV
- charges
- fees
- ROI
- tenure

---

### 4. Generate Loan Contract API

### Request input

- `offer_id`
- `fenix_loan_account_id`

### Response output

- `KFS_utility_id`
- `agreement_utility_id`

---

### 5. Submit Service Request API

### Request input

- `fenix_loan_account_id`
- `KFS_utility_id`
- `agreement_utility_id`

### Functional behaviour

- Creates service request
- Creates checker approval task in Command Centre

### Final outcome

- Post checker approval, collateral limit gets updated as per revised contract

---

# **4. Command Centre Checker Task Scope**

## Task name

- Service request approval

---

## Left panel visibility

### Request details

- Request ID
- Service request type: Limit enhancement
- Requested on
- Rate of interest
- Existing collateral limit
- Additional collateral limit
- Updated collateral limit
- Limit enhancement charges
- AMC charges
- Substatus
- Maker name
- Maker remarks
- Maker created on

### Collateral details

- ISIN
- Asset type
- Collateral subtype
- Folio
- Value
- Existing LTV
- Existing limit
- Updated LTV
- Updated limit

---

## Right panel visibility

### Client details

- Existing client information module

### Loan details

- Loan details
- Loan contract visibility
    - Contract names as per existing contracts
        - DSP LTV45
        - DSP-TCL LTV45
        - DSP LTV70

### Transactions

- Existing transaction visibility module

### Collaterals

- Existing collateral details
- Fund-level LTV visibility

### Loan kit

- KFS document
- Agreement document

---

# **5. High Level System / Process Flow**

1. LSP checks customer eligibility for higher LTV
2. Fenix validates existing contract and returns eligible upgrade details
3. LSP generates eligible offers
4. Customer selects preferred offer configuration
5. LSP accepts offer using validated commercial inputs
6. Fenix validates selected configuration and generates Offer ID
7. Loan contract and agreements are generated
8. LSP submits service request
9. Checker task gets created in Command Centre
10. Operations team reviews and approves request
11. Existing collateral limit gets updated to revised LTV contract
12. Communications is sent to the customer 

---

## Edge case handling

### Parallel collateral addition request

### Problem

An add collateral request is raised while an LTV update service request is already in progress.

### Solution

If a service request exists in non-terminal state:

- Add collateral request will move through N-STP approval flow
- Checker remarks:

> Service request with ID : {{service_request}} for the loan in progress, collateral addition approval required for loan account number : {{lan}}
> 

---

### LTV to be picked during add collateral request

### Problem

Overridden LTVs may have been applied for specific funds during previous loan application or enhancement journeys. During subsequent add collateral requests, the same funds may get lodged at a lower/default LTV instead of the highest previously approved LTV, resulting in incorrect collateral limit calculations.

### Solution

During add collateral request processing:

- System will check whether the funds being lodged were part of any previous add collateral request for the same loan
- If present, the system will fetch the historical LTV associated with those funds
- System will compare:
    - LTV in latest add collateral request
    - Maximum historical LTV for the same fund across previous requests

### Validation logic

| Scenario | Final LTV considered |
| --- | --- |
| Latest request LTV ≥ historical maximum LTV | Use latest request LTV |
| Latest request LTV < historical maximum LTV | Use historical maximum LTV |

### Expected behaviour

- Funds should never get lodged at an LTV lower than previously approved LTV for the same loan
- Existing collateral limit benefits for customers should remain preserved across enhancement journeys
- Prevents unintended reduction in collateral eligibility due to default LTV fallback

---

## Volt LTV Update Journey

### Journey overview

For Volt customers, the entry point for the LTV update journey will be a dedicated LTV update banner surfaced within the app. The visibility and eligibility of this banner will be powered through the `checkEligibleContracts` API along with additional business-level eligibility logic.

The journey enables eligible customers to seamlessly upgrade from LTV 45 to LTV 70 through a guided digital flow involving offer confirmation, agreement signing and service request creation.

Designs : https://www.figma.com/design/uztYv9y1Rzk6AAHpKWVB3L/Multi-loan-offer?node-id=5018-8937&t=bTjjETXK2ZKQjF6Z-0

---

## Customer journey flow

| Step | Description | Backend/API interaction |
| --- | --- | --- |
| LTV update banner visibility | Eligible customers are shown LTV update banner on app surfaces | `checkEligibleContracts` API + business eligibility logic |
| Customer taps banner | Customer enters LTV update flow | NA |
| Loan offer page | Eligible enhanced limit, ROI, tenure, AMC and charges are displayed | Generate Offer API |
| Customer confirms offer | Customer accepts selected offer configuration | Accept Offer API |
| KFS & Agreement signing | Customer reviews and signs updated contract documents | Generate Loan Contract API |
| Service request status screen | Customer redirected to status/confirmation screen after submission | Submit Service Request API |

---

## Detailed flow behaviour

### 1. LTV update banner

### Functional behaviour

- Banner visibility will depend on:
    - Eligibility response from `checkEligibleContracts`
    - Business configurations
    - Product rollout conditions
- Banner will act as the primary CTA for existing customers eligible for LTV enhancement

### Expected outcome

- Only eligible customers see upgrade journey entry point
- Reduces customer confusion and unnecessary journey attempts

---

### 2. Loan offer page

### Functional behaviour

Once customer enters the flow:

- Generate Offer API will be triggered
- UI values displayed to customer will be derived from:
    - Generate Offer API response
    - Business-configured defaults and overrides

### Values shown to customer

- Updated collateral limit
- Additional eligible limit
- ROI
- Tenure
- AMC charges
- Limit enhancement charges

---

### 3. Offer confirmation

### Functional behaviour

- Customer confirms selected offer
- Volt triggers Accept Offer API with:
    - Selected ROI
    - Charges
    - Tenure
    - Fund-level LTV configuration

### System validations

- ROI validation
- Fee validation
- LTV validation
- Offer eligibility validation

### Expected outcome

- Valid offer gets locked with generated Offer ID

---

### 4. KFS & agreement signing

### Functional behaviour

- Volt generates updated KFS and Agreement documents
- Customer reviews and signs updated contract

### Backend interaction

- Generate Loan Contract API

### API response

- KFS Utility ID
- Agreement Utility ID

---

### 5. Service request creation

### Functional behaviour

- Post successful signing, Volt submits service request
- Customer is redirected to service request status screen

### Backend interaction

- Submit Service Request API

### Expected outcome

- Checker approval task created in Command Centre
- Customer can track request submission state
- Post approval, collateral limit gets updated to revised LTV contract

---

### 6. Business configuration driven terms selection

### Overview

Certain commercial values shown during the LTV update journey will not be directly consumed from Fenix APIs and will instead be derived using business-configured logic shared by the business team.

These configurations are intended to support dynamic pricing and commercial strategies during the LTV migration journey.

---

### Example use case

Business may define rules such as:

- Increase existing loan ROI by 0.25%

---

### ROI computation logic

To support configuration-driven ROI computation for new products such as LTV 75:

- Volt will first fetch the current ROI of the customer's active loan account from Fenix
- Business-configured logic will then be applied on top of the fetched ROI
- Computed ROI will be used while:
    - Displaying offer details to customers
    - Calling Accept Offer API

---

### Sample flow

| Step | Description |
| --- | --- |
| Fetch existing loan details | Volt fetches current ROI from Fenix |
| Read business configuration | Business-defined rule fetched from configuration |
| Compute updated ROI | Example: Existing ROI + 0.25% |
| Display updated offer | Computed ROI shown on offer page |
| Submit offer acceptance | Computed ROI passed in Accept Offer API |

---

### Expected behaviour

- ROI computation remains centrally configurable without code-level changes
- Business teams can dynamically control pricing strategies
- Volt maintains compatibility with Fenix-side ROI validations
- Final computed ROI must always lie within min/max ROI ranges returned by Offer Generation API

---

### Validation handling

Before Accept Offer API submission:

- Volt must validate that computed ROI:
    - Is within allowed ROI range returned by Generate Offer API
    - Adheres to applicable business rules
    - Matches customer-visible offer values

If computed ROI falls outside eligible ranges:

- Offer acceptance should be blocked
- Appropriate fallback/error handling should be triggered internally