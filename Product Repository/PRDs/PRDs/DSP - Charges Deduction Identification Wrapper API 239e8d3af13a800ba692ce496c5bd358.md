# DSP - Charges Deduction Identification Wrapper API for LSPs

: Ranjan kumar Singh
Created time: July 23, 2025 3:37 PM
Status: Not started
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

- Scoping rough
    
    BAJAJ:
    Web: We open the URL in the same tab replacing Volt's URL.
    Android/iOS: We navigate to another screen which is a webview and open the url in the WebView.
    TATA:
    Web: We open the URL in the same tab replacing Volt's URL.
    Android/iOS: We open in inApp browser.
    

# What problem are we solving?

Lending Service Providers (LSPs) receive charges data(in loan summary API) but cannot easily identify which charges will be deducted from the loan disbursal amount (net disbursal) and which will not. The existing API lacks explicit categorisation or clear indication, leading to confusion and incorrect communication to customers about the deduction of charges.

## How do we measure success?

- 100% clear classification of charges returned to LSPs as either deducted from disbursal or not.
- Reduction in support tickets or clarifications requested by LSPs customer regarding charge deductions.
- LSPs successfully integrate and consume the new wrapper API without issues.

---

## How are others solving this problem?

---

—NA—

## What is the solution?

Create a **wrapper API** that:

- Use FinFlux Charges API “Get Account Charge Api”.
    - UAT URL: [https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/revolving-credit-lines/000000049/charges](https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/revolving-credit-lines/000000049/charges)
- Uses a **configurable mapping** of `chargeIdentifier` and/or `chargeId` to determine if a charge is deducted from disbursal.
- Returns two clean, separate lists:
    - **deductedFromDisbursal**
    - **notDeductedFromDisbursal**
- Provides a clear, consistent API response optimized for LSP consumption.
- Supports easy updates to the mapping without any changes at FinFlux end.

## Requirements overview (optional)

- Backend service (Fenix) to call LMS (FinFlux) get account charge API and transform output.
- Config-driven logic for charge classification (match by chargeId/chargeIdentifier).
- Standard JSON response with separate arrays for deducted and non-deducted charges.
- Error handling & authentication.
- Documentation for LSPs on using the new API.

## User stories / User flow

**As an LSP developer**,

I want to call a single API endpoint to get the loan charges for an account,

So that I can easily identify which charges reduce the disbursal amount and which do not.

**User flow**:

1. LSP calls wrapper API with loan account ID.
2. Wrapper API calls LMS API and fetches charge data.
3. Wrapper classifies charges by checking each charge against the configured mapping.
4. Wrapper returns charges split into two clear lists to LSP.
5. LSP uses the data to display correct charge deductions to customers.

## Requirements

- API endpoint (sample): `GET /api/charges/:creditId`.
- Ability to configure mapping of charges considered deducted by either `chargeId` or `chargeIdentifier`.
- Response format example:
    
    `json{
      "deductedFromDisbursal": [ */* charges */* ],
      "notDeductedFromDisbursal": [ */* charges */* ]
    }`
    
- Convert `dueDate` and `appliedDate` arrays to ISO date strings in response.
- Handle LMS(FinFlux) API errors and return appropriate HTTP error codes.
- Logging of requests and errors.

**FinFlux Charges API details:**

End point: https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/revolving-credit-lines/000000049/charges

Response:

```json
[
    {
        "chargeIdentifier": "PF1",
        "chargeId": 2,
        "name": "Processing Fee",
        "dueDate": [
            2024,
            5,
            31
        ],
        "appliedDate": [
            2024,
            5,
            31
        ],
        "humanReadableFormat": "100 Flat",
        "taxBasicComponentData": [],
        "amount": 100,
        "isPenalty": false,
        "outstandingChargeAmount": 0,
        "accountChargeIdentifier": "e54b3e34-01ed-4162-9e0d-4b08d885ed0f",
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "PCD",
        "chargeId": 41,
        "name": "Penal Charge day wise",
        "dueDate": [
            2024,
            7,
            17
        ],
        "appliedDate": [
            2024,
            7,
            17
        ],
        "humanReadableFormat": "25 Flat",
        "taxBasicComponentData": [],
        "amount": 500.22,
        "isPenalty": true,
        "outstandingChargeAmount": 450.22,
        "accountChargeIdentifier": "75931721-0ab9-41e4-938b-7fb3e14c3907",
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "LC",
        "chargeId": 43,
        "name": "Legal Charges",
        "dueDate": [
            2024,
            7,
            17
        ],
        "appliedDate": [
            2024,
            7,
            17
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 500.22,
        "isPenalty": false,
        "outstandingChargeAmount": 400.22,
        "accountChargeIdentifier": "fc0017f6-bf94-4fc0-aaee-6f38494c6cc2",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "MP",
        "chargeId": 54,
        "name": "Margin Pledge Charge",
        "dueDate": [
            2024,
            7,
            24
        ],
        "appliedDate": [
            2024,
            7,
            24
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 590.26,
        "isPenalty": false,
        "outstandingChargeAmount": 590.26,
        "accountChargeIdentifier": "20bbebdf-837d-4be5-a076-d5774dac6d85",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "MP",
        "chargeId": 52,
        "name": "Margin Pledge Charge",
        "dueDate": [
            2024,
            7,
            21
        ],
        "appliedDate": [
            2024,
            7,
            21
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 590.26,
        "isPenalty": false,
        "outstandingChargeAmount": 590.26,
        "accountChargeIdentifier": "6e0c5e35-e6ab-4b93-843d-d7f59121ee43",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "MP",
        "chargeId": 48,
        "name": "Margin Pledge Charge",
        "dueDate": [
            2024,
            7,
            19
        ],
        "appliedDate": [
            2024,
            7,
            19
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 500.22,
        "isPenalty": false,
        "outstandingChargeAmount": 500.22,
        "accountChargeIdentifier": "cf72a47b-2317-462a-b8ee-e8a6ad385519",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "CC",
        "chargeId": 58,
        "name": "Collection Charge",
        "dueDate": [
            2024,
            7,
            25
        ],
        "appliedDate": [
            2024,
            7,
            25
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 590.26,
        "isPenalty": false,
        "outstandingChargeAmount": 590.26,
        "accountChargeIdentifier": "87e0c8ae-0631-4951-b21f-4c0d6a7856b2",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": false
    },
    {
        "chargeIdentifier": "CC",
        "chargeId": 47,
        "name": "Collection Charge",
        "dueDate": [
            2024,
            7,
            19
        ],
        "appliedDate": [
            2024,
            7,
            19
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 590.26,
        "isPenalty": false,
        "outstandingChargeAmount": 590.26,
        "accountChargeIdentifier": "b6b55cda-f365-4931-88f4-995314a6906b",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "CC",
        "chargeId": 46,
        "name": "Collection Charge",
        "dueDate": [
            2024,
            7,
            18
        ],
        "appliedDate": [
            2024,
            7,
            18
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 590.26,
        "isPenalty": false,
        "outstandingChargeAmount": 590.26,
        "accountChargeIdentifier": "fd6dddf7-51c5-409b-ac90-0e57ef0aa35c",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "CC",
        "chargeId": 45,
        "name": "Collection Charge",
        "dueDate": [
            2024,
            7,
            18
        ],
        "appliedDate": [
            2024,
            7,
            18
        ],
        "humanReadableFormat": "500 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 500.22,
        "isPenalty": false,
        "outstandingChargeAmount": 500.22,
        "accountChargeIdentifier": "06d12bcb-44d5-4202-94f0-b989e4892a97",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    },
    {
        "chargeIdentifier": "LR",
        "chargeId": 42,
        "name": "Loan Renewal Fees",
        "dueDate": [
            2024,
            7,
            17
        ],
        "appliedDate": [
            2024,
            7,
            17
        ],
        "humanReadableFormat": "1499 Flat",
        "taxBasicComponentData": [
            {
                "name": "CGST",
                "percentage": 9,
                "taxComponentType": "CGST",
                "narration": "9.000000 % CGST",
                "taxComponentId": 4
            },
            {
                "name": "SGST",
                "percentage": 9,
                "taxComponentType": "SGST",
                "narration": "9.000000 % SGST",
                "taxComponentId": 5
            },
            {
                "name": "IGST",
                "percentage": 18,
                "taxComponentType": "IGST",
                "narration": "18.000000 % IGST",
                "taxComponentId": 1
            },
            {
                "name": "UTGST",
                "percentage": 9,
                "taxComponentType": "UTGST",
                "narration": "9.000000 % UTGST",
                "taxComponentId": 6
            }
        ],
        "amount": 500.22,
        "isPenalty": false,
        "outstandingChargeAmount": 500.22,
        "accountChargeIdentifier": "998c4b2d-edfc-460a-ade0-903acba47a06",
        "taxGroupId": 2,
        "isChargeImpactingAvailableLimit": true
    }
]
```

**Expected sample response from wrapper API:**

```json
{
  "deductedFromDisbursal": [
    {
      "chargeIdentifier": "PF1",
      "chargeId": 2,
      "name": "Processing Fee",
      "dueDate": "2024-05-31",
      "appliedDate": "2024-05-31",
      "amount": 100,
      "isPenalty": false,
      "outstandingChargeAmount": 0
    }
  ],
  "notDeductedFromDisbursal": [
    {
      "chargeIdentifier": "PCD",
      "chargeId": 41,
      "name": "Penal Charge day wise",
      "dueDate": "2024-07-17",
      "appliedDate": "2024-07-17",
      "amount": 500.22,
      "isPenalty": true,
      "outstandingChargeAmount": 450.22
    }
  ]
}
    {
      "chargeIdentifier": "PCD",
      "name": "Penal Charge day wise",
      "dueDate": 1751673600000,
      "appliedDate": 1751673600000,
      "amount": 500.22,
      "isPenalty": true,
      "outstandingChargeAmount": 450.22,
      "isChargeDeductedFromDisbursalRequest": false
    }
```

## Design

—NA—

## Analytics

- Track API usage metrics (calls per account, success/failure rates).
- Monitor error types logged.
- Usage by different LSP partners for adoption measurement.

## Timeline/Release Planning

| Week | Tasks |
| --- | --- |
| 1 | - Finalize API design and mapping rules. |
| 1 | Develop backend wrapper API. |
| 1 | Testing: unit, integration with LMS(FinFlux) API. |
| 2 | LSP UAT & documentation delivery. |
| 2 | Production rollout and monitoring setup. |

## Go to market

## Marketing

- Provide sample API integration docs and quickstart guides to LSPs.

## Ops & Sales training

—NA—

## Frequently asked questions (FAQs)

- **Q:** How do you decide which charges are deducted?
    
    **A:** By matching the charge’s `chargeIdentifier` or `chargeId` against a configurable business mapping.
    
- **Q:** Can the mapping change over time?
    
    **A:** Yes, it can be updated without backend redeployments.
    
- **Q:** What if a charge is missing in the mapping?
    
    **A:** It will default to "not deducted from disbursal."
    
- **Q:** Can we extend the API to support bulk queries?
    
    **A:** This can be scoped for future phases.
    

## Action items / checklist

- [x]  Product
- [x]  Define mapping and classification rules
- [x]  Business
- [x]  Approve charges mapping strategy
- [x]  Design
- [x]  API design and response format
- [x]  Development
- [x]  Build wrapper API
- [ ]  Testing
- [ ]  Prepare test cases and perform tests
- [ ]  Documentation for LSP
- [ ]  Go-live preparation and monitoring setup

## Feedback

*To be collected post UAT and initial rollout.*

## Learnings & Next steps

- Analyze LSP adoption and clarify further enhancements needed (e.g., bulk requests, field filtering).

## Appendix

## Meeting notes

- Discussed the ambiguity in LMS charge flags for disbursal deduction.
- Business agreed on fixed mapping approach by charge identifiers.
- Tentative timeline agreed as 5 weeks delivery.
- LSPs eager for simplified API.

If you want, I can also help generate the API spec or sample code next!