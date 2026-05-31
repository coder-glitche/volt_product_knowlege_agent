# MNRL Validation - GTM Rollout for LSPs

**Context**

As per the RBI mandate, financial institutions must verify customer mobile numbers against the Mobile Number Revocation List (MNRL) - a DoT dataset of deactivated, fraud-flagged, or cybercrime-linked numbers. 

Numbers tied to LEA-reported cybercrime, fake/forged documents, or TSP internal flags must be blocked from proceeding to loan creation.

LSPs do not need to implement MNRL checks themselves. DSP handles all validation, data sync, and compliance reporting. LSPs only need to handle the rejection response gracefully in their integration.

**What gets blocked and why ?**

Numbers appear in MNRL for multiple reasons. DSP will block loan creation due to these reasons:

- LEA-reported cybercrime: number flagged by law enforcement for cybercrime activity
- DoT fake/forged cases: number associated with fraudulent or forged documentation
- TSP internal analysis: flagged by telecom operator through internal fraud detection

**Where checks happen in the journey ?**

There are two validation touchpoints:

1. Create Opportunity - OpportunityID is not created if blocked.
2. Submit Opportunity - LoanID is not created if blocked.

**What LSPs need to do ?**

LSPs have no action required on the MNRL validation itself, DSP manages that entirely. 

What LSPs must do:

- Handle the `USER_BLACKLISTED_MNRL_CHECK` error code at both the Create Opportunity and Submit Opportunity endpoints
- LSPs can display the blocking message to the user on UI

**Rejection response - at both endpoints**

When a user's number is blocked, DSP returns an HTTP 400 at both `/opportunity` and `/opportunity/{id}/submit`:

```
{
  "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK",
  "message": "User blacklisted due to MNRL check",
  "statusCode": "400"
}
```

LSPs should look for `fenixErrorCode === "USER_BLACKLISTED_MNRL_CHECK"` and render the blocking UI accordingly.

**What error message should LSPs need to show on UI ?** 

Message Copy : *Sorry, your application currently doesn’t meet lenders eligibility criteria. You can always try again later*.