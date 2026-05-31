# Mandate Limit Change for LSPs

## **Context**

In the Loan Against Mutual Funds (LAMF) journey, customers complete the Registration → Selfie → KYC process → Fetch their Funds →Select a Credit Limit→Add and Verify Bank account and are required to register a mandate. Currently, the mandate amount is fixed at **₹10 lakhs**, irrespective of the actual loan/limit sanctioned. This often creates friction for customers with smaller credit lines, leading to:

- Drop-offs at the mandate step
- Customer confusion & higher support queries
- Lower overall funnel conversion

To address this, we conducted an **A/B test** across Volt journeys with three mandate structures:

1. Fixed ₹10 lakh (Control)
2. 20% of selected limit (Test 1)
3. 100% of selected limit (Test 2)

**Result:** Test 2 (100% of selected limit) showed the **highest mandate completion rate.** The jump in conversion rate which we observed was ~500 basis points compared to the other two cohorts.

---

## Benefits (for LSP & Customers)

### LSP:

**Higher Conversion** – Familiarity with the amount led to higher conversion as tested internally.

**Reduced Queries** – Lower customer support tickets related to high mandate value.

### Customer:

**Customer Trust** – Avoids mismatch between Selected Limit and Mandate authorization amount.

**Improved UX** – Intuitive mandate journey for end customers.

---

## **Proposed Change for LSP**

- A minor change in the Create Mandate/Mandate Init API in order to ****have **Mandate value = 100% of the selected loan limit** (capped at ₹10 lakh).
- DSP will handle the rest of the process (mandate creation, presentation, and maintenance).

---

## API Changes

API: [https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)

Current API Parameters: 

```
		"opportunityId"
    "bankAccountVerificationId"
    "endDate"
    "mandateType"
    "mandateAmount"
    "redirectionUrl"
```

Parameter which needs to be added and passed: “selectedLimit”

New API request:

curl --location '[https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)' \
--header 'Content-Type: application/json' \
--header 'X-SourcingChannelCode: Code Provided by DSP' \
--header 'X-Signature: Signature generated from the authentication script' \
--header 'X-Timestamp: Timestamp generated from the authentication script' \
--data '{
"opportunityId": "OPP8724213445",
"bankAccountVerificationId": "URBANK4674555244",
“selectedLimit”: “40000”
"endDate": "2039-09-20",
"mandateType": "API_MANDATE",
"mandateAmount": "10000000",
"redirectionUrl": "[https://www.voltmoney.in](https://www.voltmoney.in/)"
}'

---

## **Next Steps for LSPs**

1. **Integration Update**: Pass the selected loan limit in DSP’s Create mandate API.
2. **Testing**: Validate mandate creation and completion in staging.
3. **Rollout**: Intimate release plan with DSP to move to production.

---