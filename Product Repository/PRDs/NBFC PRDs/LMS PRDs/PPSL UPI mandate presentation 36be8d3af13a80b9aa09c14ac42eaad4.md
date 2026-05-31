# PPSL UPI mandate presentation

Last Edited: May 25, 2026 10:00 PM
PRD ETA: May 25, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

## **Background and Context**

PayTM currently uses the existing DSP Finance (Fenix) mandate registration and presentation stack for both NACH and UPI mandates, where mandate registration is facilitated via Digio and mandate presentation is managed through DSP Finance workflows.

PayTM intends to migrate mandate registration for a subset of users to the internal PPSL mandate stack. The primary motivation behind this change is to significantly improve the end-user registration experience by enabling native invocation of the UPI intent flow directly through the PayTM ecosystem. This removes dependency on external redirection-heavy flows and improves TPAP handoff reliability during mandate registration.

Historically, the PPSL UPI mandate presentation workflow differed from the existing Digio-integrated flow:

- Digio workflow:
    - Single consolidated API call
    - Automatically registers PDN and presents mandate together
    - Mandatory condition that mandate presentation occurs more than 24 hours in the future
- PPSL workflow (earlier implementation):
    - PDN scheduling and mandate presentation were independent APIs/workflows
    - Required additional orchestration effort from LMS/LOS

PPSL has now aligned its APIs and shared updated documentation enabling the required orchestration compatibility.

However, this introduces an operational and technical challenge:

- Certain PayTM customers will continue using Digio mandates
- New customers may register mandates using PPSL
- LMS presentation logic must identify which mandate provider was used during registration to correctly invoke downstream presentation workflows

Currently, LOS internally maintains provider mapping through a provider column, however the external mandate registration APIs used by LSPs do not allow explicit provider selection. This creates ambiguity for LMS while determining presentation routing.

To solve this, the mandate registration APIs will be enhanced to allow PayTM to explicitly pass the mandate provider during registration.

---

# **1. Problem Scope**

## In Scope

The scope of this enhancement includes:

- Supporting UPI mandate registration through PPSL for PayTM-originated users
- Enhancing LOS mandate registration APIs to support explicit provider tagging
- Allowing PayTM to explicitly pass `provider = PPSL`
- Persisting provider information within LOS
- LMS consuming provider metadata from LOS
- LMS routing mandate presentation based on provider
- Supporting coexistence of:
    - Legacy Digio mandates
    - PPSL mandates
- Maintaining the existing UPI mandate presentation logic at LMS layer:
    - Loan account level presentation creation
    - Collection batch item generation
    - Existing downstream presentation orchestration

### Primary stakeholders

- PayTM onboarding/product teams
- LOS team
- LMS team
- Collections and repayment orchestration systems
- End customers registering UPI mandates

### Secondary stakeholders

- Operations teams
- Customer support teams
- Partner reconciliation teams

---

## Out of Scope

The following items are explicitly excluded from this scope:

- Migration of existing Digio mandates to PPSL
- Changes to mandate presentation retry logic
- Changes to collection batching logic
- NACH mandate presentation workflow changes
- Changes to repayment allocation logic
- Changes to existing LMS collection orchestration framework
- Any UI redesign beyond provider invocation capability

### Rationale

The objective of this phase is limited to enabling provider-aware registration and presentation routing while minimizing changes to existing stable repayment and collection systems.

---

# **2. Success Criteria**

## Primary outcomes

### 1. Improved UPI mandate registration success rates

Expected outcome:

- Higher completion rate for UPI mandate registration due to native TPAP invocation through PPSL

Success metrics:

- Increase in UPI mandate registration conversion
- Reduction in user drop-offs during mandate authorization

---

### 2. Accurate provider-aware mandate presentation routing

Expected outcome:

- LMS correctly identifies and routes presentations to:
    - PPSL workflows
    - Digio workflows

Success metrics:

- 100% correct provider-based routing
- Zero incorrect presentation attempts due to provider mismatch

---

### 3. No degradation to existing repayment and presentation flows

Guardrail metrics:

- Existing Digio flows remain unaffected
- No increase in mandate presentation failures
- No increase in reconciliation discrepancies
- No impact to repayment TATs
- LMS batch generation uptime and success rates remain stable

---

# **3. Solution Scope**

## Solution Overview

The solution introduces provider-aware mandate registration and presentation orchestration for PayTM-originated UPI mandates.

LOS APIs will be enhanced to accept an optional `provider` parameter during mandate registration. PayTM will explicitly pass `PPSL` for mandates registered through the PPSL stack. LOS will persist this metadata and LMS will consume it during presentation orchestration to determine the appropriate mandate presentation workflow.

The downstream UPI mandate presentation logic at LMS remains unchanged, including:

- Loan account level presentation creation
- Collection batch item generation
- Existing presentation orchestration mechanisms

This minimizes operational risk while enabling coexistence of multiple mandate providers.

---

## Detailed Solution Scope

| Description | Details |
| --- | --- |
| Provider-aware mandate registration | LOS mandate registration APIs enhanced with optional `provider` field |
| Provider persistence | LOS stores provider metadata against mandate |
| Provider routing | LMS fetches provider details from LOS before presentation |
| PPSL mandate handling | LMS routes PPSL mandates to PPSL presentation workflows |
| Digio mandate handling | Existing Digio presentation workflows continue unchanged |
| Existing LMS orchestration | Loan account presentation logic and collection batch creation remain unchanged |
| Hybrid provider support | Same PayTM tenant can support both Digio and PPSL mandates |
| Backward compatibility | Existing API consumers continue functioning without changes |

---

## Supported User & System Use Cases

### Happy Path

1. User initiates mandate registration from PayTM
2. PayTM invokes PPSL-native UPI intent flow
3. PayTM calls LOS mandate registration API with:
    - Mandate details
    - `provider = PPSL`
4. LOS validates and stores mandate
5. LMS fetches mandate + provider details
6. LMS creates:
    - Loan account level presentation
    - Collection batch items
7. LMS routes presentation to PPSL workflow
8. Mandate gets presented successfully

---

### Existing Digio Flow (No Change)

1. Existing Digio mandates continue registration
2. Provider remains Digio/default
3. LMS routes presentation through existing Digio orchestration

---

### Edge Cases

| Edge Case | Expected Handling |
| --- | --- |
| Provider not passed | Existing/default routing logic continues |
| Unsupported provider value | LOS validation failure |
| Mixed provider mandates under same tenant | LMS routes based on mandate-level provider |
| Existing Digio mandates | No migration/change required |
| PPSL presentation failure | Existing retry/error handling applies |
| Future dated start date | Validation failure |
| Mandate amount lower than sanctioned amount | Validation failure |

---

# **Mandate Registration API Changes**

## Submit Mandate API

### Endpoint

`POST /los/api/v1/opportunities/{opportunityId}/mandates`

### Purpose

Registers a mandate against a loan opportunity.

---

## API Enhancement

An optional `provider` field will be introduced.

### Supported Values

- `PPSL`
- Existing/default provider values

### Usage

PayTM must explicitly pass:

`provider = PPSL`

for mandates registered through the PPSL stack.

---

## Validations

| Validation | Rule |
| --- | --- |
| UMRN / UMN | Mandatory |
| Mandate expiry date | Mandatory |
| Mandate start date | Cannot be future dated |
| Mandate frequency | Only `ADHOC` supported |
| Mandate amount | Must be >= sanctioned loan amount |
| Mandate type | Must be supported type |
| Provider | Optional but validated if passed |

---

## Supported Mandate Types

- `UPI_MANDATE`
- `ESIGN_MANDATE`
- `PHYSICAL_MANDATE`
- `API_MANDATE`

---

## Request

```
{
  "bankAccountVerificationId":"URBANK3275665731",
  "startDate":"2024-09-20",
  "endDate":"2039-09-20",
  "mandateType":"UPI_MANDATE",
  "mandateAmount":"50000",
  "mandateFrequency":"ADHOC",
  "umrn":"UMRN123456789",
  "provider":"PPSL"
}
```

---

## Field Definitions

| Field | Type | Description |
| --- | --- | --- |
| bankAccountVerificationId | String | Reference ID from bank verification |
| startDate | Date | Mandate start date |
| endDate | Date | Mandate expiry date |
| mandateType | String | Mandate type |
| mandateAmount | Decimal | Maximum debit limit |
| mandateFrequency | String | ADHOC |
| umrn | String | Unique Mandate Reference Number |
| provider | String | Mandate registration provider |

---

## Response

```
{
  "utilityReferenceId":"URMNDT9479288882",
  "status":"APPROVED",
  "subStatus":"MANDATE_SUCCESS"
}
```

---

# **5. High Level System / Process Flow**

## PPSL Mandate Registration & Presentation Flow

1. User initiates UPI mandate registration from PayTM
2. PayTM invokes PPSL-native intent flow
3. PPSL completes mandate authorization
4. PayTM calls LOS mandate registration API
5. LOS validates:
    - UMRN
    - dates
    - amount
    - frequency
    - provider
6. LOS stores mandate + provider metadata
7. LMS fetches mandate details from LOS
8. LMS creates:
    - Loan account level presentation entries
    - Collection batch items
9. LMS checks provider:
    - If PPSL → invoke PPSL presentation workflow
    - Else → invoke Digio/default presentation workflow
10. Presentation execution continues through existing LMS collection orchestration

---

## Error Handling

| Scenario | Handling |
| --- | --- |
| Invalid provider | LOS validation failure |
| Missing mandatory fields | API rejection |
| Unsupported mandate type | API rejection |
| Presentation failure | Existing retry mechanisms |
| LOS-LMS sync delay | Existing reconciliation/retry mechanisms |

---

# **6. Appendix**

## Benchmarking / Observations

### Existing Digio limitations

- Non-native TPAP handoff
- Increased user drop-offs during intent switch
- Dependency on consolidated presentation orchestration
- Reduced flexibility in provider-level routing

### PPSL benefits

- Native PayTM ecosystem invocation
- Better UPI app handoff experience
- Improved mandate registration UX
- Better operational ownership within PayTM ecosystem

---

## Operational Notes

- Operations teams do not require SOP changes
- LMS presentation creation process remains unchanged
- Existing reconciliation and collection flows remain intact
- Support teams may require visibility into provider-level mandate tracking for debugging and issue resolution