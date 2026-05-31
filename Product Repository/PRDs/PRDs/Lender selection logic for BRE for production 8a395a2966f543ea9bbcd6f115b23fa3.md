# Lender selection logic for BRE for production.

: Ameya Aglawe
Created time: September 13, 2024 5:38 PM
Status: Ready for Tech
Last edited: October 11, 2024 4:47 PM

# **What problem are we solving?**

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

I’m not able to find the logic of TATA/BAJAJ based on fetch limit 

### BRE previous logic

**Conditions in Priority Order**

The priority of conditions is determined by their order in the code. Earlier checks have higher priority because they can lead to immediate decisions, short-circuiting the rest of the process. Here's the prioritized list:

1. **Overridden Lender**
    - Highest priority; immediately returns if set.
2. **Hardcoded Tata Assignment**
    - An `if(true)` condition that always assigns to Tata.
    - NOTE: This likely overrides all other logic and should be investigated.
3. **PAN-Aadhaar Seeding**
    - Checks early in the process, assigns to Bajaj if not seeded.
4. **Previous Tata Loan**
    - Checks for closed Tata loans and assigns to Bajaj if found.
5. **Partner Account Check for Tata**
    - Assigns to Tata for specific partner (PAYTM1).
6. **Age Verification**
    - Assigns to Bajaj if age is outside 18-70 range.
7. **Mutual Fund Portfolio Check**
    - Assigns to Bajaj if portfolio is empty.
8. **Lender Limit Computation**
    - Not a decision point, but affects subsequent checks.
9. **High Bajaj Limit Check**
    - Assigns to Bajaj if limit ≥ 1 Crore.
10. **Tata vs Bajaj Limit Comparison**
    - Assigns to Bajaj if Tata's limit is lower than threshold.
11. **Existing Tata Customer**
    - Assigns to Bajaj if user is existing Tata customer.
12. **Partner Account Whitelist for Bajaj**
    - Assigns to Bajaj for specific partner account IDs.
13. **Equifax Credit Score Check**
    - Assigns to Bajaj for scores between 50 and 690.
14. **Platform Check**
    - Assigns to Bajaj if not on specified platforms.
15. **Specific PAN List for Tata**
    - Assigns to Tata for specific PANs.
16. **Probability-based Assignment**
    - Final decision point if all above checks pass.
17. **Default Fallback**
    - Assigns to Bajaj in case of any exceptions.

### BRE latest logic

**1. Overridden Lender**

- If `request.getOverriddenLenderAccountId()` is not blank, the BRE is bypassed, and the overridden lender is assigned.

**2. DSP Phone Whitelisting**

- Condition: `featureFlagUtil.isFlagEnabled(FeatureFlagConfigurationFlag.DSP_PHONE_WHITELISTING, request.getMobileNumber())`
- If enabled and DSP limit <= 20,000,000, DSP is assigned as the lender.

**3. Platform Whitelisting**

- For platform codes "BHARAT_PE" and "NIYO", Bajaj is assigned.
- For platform codes "ZYPE" and "FUNDS_INDIA", Tata is assigned.

**4. Partner Whitelisting**

- If not an existing DSP customer and partner code is "FENIX_UAT":
    - If DSP limit <= 20,000,000, DSP is assigned.

**5. Existing Customer Handling**

- If existing Bajaj customer, Tata is assigned.

**6. One Crore Check**

- Condition: `featureFlagUtil.isFlagEnabled(FeatureFlagConfigurationFlag.ONE_CRORE_CHECK.name(), request.getMobileNumber())`
- If enabled and Bajaj limit >= 9,900,000, Tata is assigned.

**7. Probabilistic Assignment**

- Environment variable `TATA_PROBABILITY` determines the likelihood of Tata assignment (default 100%).
- Random number (0-99) is generated:
    - If < TATA_PROBABILITY, Tata is assigned.
    - Otherwise, Bajaj is assigned.

### Edge Cases and Error Handling

- If any exception occurs during the process, Bajaj is assigned as a fallback.

### Feature Flags

1. DSP_PHONE_WHITELISTING: Controls DSP assignment for specific phone numbers.
2. ONE_CRORE_CHECK: Enables assignment to Tata for high-value loans.

### Notes

- The code uses environment variables and feature flags for configuration.
- Lender limits are computed using `limitEvaluationHelper.computeLimitForLenders()`.
- The system checks for existing customers across different lenders.

![BRE-23 sept BT.png](Lender%20selection%20logic%20for%20BRE%20for%20production/BRE-23_sept_BT.png)

## Requirements overview (optional)

## User stories / User flow

## Requirements

---

# **Design**

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes