# Unpledge - Stocks selection logic

Last Edited: March 19, 2026 9:44 PM
PRD Owner: Ranjan kumar Singh
Status: Completed

# Overview:

In LAS unpledge flow users to **unpledge stocks by entering a target value**, while the system automatically selects stocks optimally based on Collateral Value and **eligibility constraints**.

User should be able to enter an **unpledge amount(Collateral Value)**, and the system must automatically pick stocks starting from **lowest stocks value → highest stocks value**, selecting whole units only, and **rounding DOWN** when calculating units.

The system must ensure that the **total credit value released does not exceed the Eligible Limit**, which depends on Drawing Power (DP), Total Outstanding (TOS), and accrued interest.

Shorting of pledge stocks list : Highest Stocks Value to Lowest stocks value

---

# **How do we measure success?**

| Metric | Expected Outcome |
| --- | --- |
| unpledge failure rate | Less then 10% per day |
| Manual stock selection | Less then 10% Users  |
| Accuracy of unpledge calculation | - No of request initiated VS  raised successfully
- Rejection rate due to value mismatch |

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

### **Step 1 — Input**

User enters **Amount to unpledge** on UI (e.g., ₹4,000).

### **Step 2 — System Fetch**

The system retrieves:

- Pledged stocks
- NAV × Units × LTV (credit limit of each stocks)
- Total Drawing Power (DP = 3241)
- Total Outstanding (TOS)
- Accrued Interest

### **Step 3 — Eligibility Check**

```
Summation(Units × NAV × LTV) ≤ Drawing power − Total outstanding − Accrued interest
```

If user tries to unpledge more than eligible limit → show validation error.

### **Step 4 — Auto-Selection**

### Sorting Rule

Sort pledged stocks by:

**Total Stock Value = NAV × Units (ascending order)**

### Auto-selection Flow

Iteratively select stocks in sorted order until:

- Stock fully unpledged OR
- Required amount satisfied

If full unpledge exceeds required amount → **partial unpledge allowed** with rounding down units.

### **Step 5 — UI**

Show:

- Selected stocks
- Units chosen
- Total value selected
- Remaining difference (if any)
- Eligibility message if amount cannot be met exactly

### **Step 6 — User confirms**

Backend validates again and proceeds with unpledge.

## Requirements

# Eligibility Check

User can unpledge **UP TO**:

```
Eligible Limit = Drawing Power – Total Outstanding – Accrued Interest
```

For each stock:

```
Stock Credit limit Value = Units × NAV × LTV
```

Condition to allow unpledge:

```
Σ(Units × NAV × LTV of selected stocks) ≤ Eligible Limit

```

If exceeded → reject.

# **Stock Selection Logic**

### **Input Data (Example Pledged Stocks)**

| Stock | NAV | Units | Total Value | LTV | Credit Value |
| --- | --- | --- | --- | --- | --- |
| Yes Bank | 12 | 6 | 72 | 0.60 | 43.2 |
| Groww | 300 | 2 | 600 | 0.70 | 420 |
| BSE | 1000 | 1 | 1000 | 0.50 | 500 |
| JSW Energy | 340 | 4 | 1360 | 0.55 | 748 |
| HDFC Bank | 34 | 100 | 3400 | 0.45 | 1530 |
| TOTAL |  | 113 | 6432 |  | 3241.2 |

> Sorted lowest → highest based on Total Value:
> 
> 
> **Yes Bank → Groww → BSE → JSW Energy → HDFC Bank**
> 

Now system selects in that order until request is satisfied and eligibleLimit is not breached.

### **Selection strategy**

Iterate from **lowest → highest stock value**, and for each stock:

1. Calculate `unitsNeeded = floor(remainingAmount / NAV)`
2. If `unitsNeeded == 0` → move to next stock
3. If `unitsNeeded > availableUnits` → reduce to availableUnits
4. Eligibility rule check:

```
If totalCreditReleased + (units × NAV × LTV) > eligibleLimit:
    reduce units until eligible
```

1. Select final `units`
2. Update:

```
remainingAmount -= units × NAV
totalCreditReleased += units × NAV × LTV
```

Stop when `remainingAmount ≤ 0` or no more stocks available.

### Rounding rule

- **Always round down units (no fractional units)**

## Example/Scenario:

### **Example A: User enters ₹10,000**

Step 1: Check total available value:

```
Total pledged value =
HDFC (3400) + BSE (1000) + JSW (1360) +
Yes Bank (72) + Groww (600) = 6,432

```

User wants **₹10,000**

But **₹6,432 < ₹10,000 → Not possible**

🔹 **Final Outcome:** User cannot request unpledge of ₹10,000 because pledged value is insufficient.

---

### **Example B: User enters ₹2,000**

Assumptions:

```
Eligible Limit = 1,241
Selection priority = sorted by total stock value low → high

```

Sorted order: Yes Bank (72) → Groww (600) → BSE (1000) → JSW (1360) → HDFC (3400)

---

### **1. Yes Bank (NAV 12, Units 6)**

UnitsNeeded = floor(2000 / 72 per total stock) = 27 → more than available → take all units

Value released = 6 × 12 = **72**

Credit = 6 × 12 × 0.6 = **43.2**

Remaining = 2000 – 72 = **1928**

Cumulative credit = **43.2 ≤ 1241 → OK**

---

### **2. Groww (NAV 300, Units 2)**

UnitsNeeded = floor(1928 / 600 per total stock) = 3 → exceeds available → take all 2 units

Value released = 2 × 300 = **600**

Credit = 600 × 0.7 = **420**

Remaining = 1928 – 600 = **1328**

Cumulative credit = 43.2 + 420 = **463.2 ≤ 1241 → OK**

---

### **3. BSE (NAV 1000, Units 1)**

UnitsNeeded = floor(1328 / 1000) = **1**

Value released = 1 × 1000 = **1000**

Credit = 1 × 1000 × 0.5 = **500**

Remaining = 1328 – 1000 = **328**

Cumulative credit = 463.2 + 500 = **963.2 ≤ 1241 → OK**

---

### **4. JSW Energy (NAV 340, Units 4)**

UnitsNeeded = floor(328 / 1360 per total stock) = **0** → skip

---

### **5. HDFC Bank (NAV 34)**

UnitsNeeded = floor(328 / 34) = **9 units**

Credit = 9 × 34 × 0.45 = **137.7**

Cumulative credit = 963.2 + 137.7 = **1100.9 ≤ 1241 → OK**

Remaining = 328 – 306 = **22**

---

🔹 **Result for ₹2,000 request**

| Stock | Units Selected | Value |
| --- | --- | --- |
| Yes Bank | 6 | ₹72 |
| Groww | 2 | ₹600 |
| BSE | 1 | ₹1000 |
| HDFC | 9 | ₹306 |
| **Total** | — | **₹1,978 (closest possible to ₹2,000)** |

Exact ₹2000 not possible due to unit constraints (no decimals).

Request will be processed for **₹1,978**.

---

### **Example C: User enters ₹4,000**

Eligible Limit remains **₹1,241**

---

Start selection (low → high value order):

| Stock | Total Value |
| --- | --- |
| Yes Bank | 72 |
| Groww | 600 |
| BSE | 1000 |
| JSW Energy | 1360 |
| HDFC Bank | 3400 |

---

### **1. Yes Bank (72)**

Take all 6 units → Value = 72

Credit = 43.2

Remaining = 4000 – 72 = **3928**

Cumulative credit = **43.2**

---

### **2. Groww (600)**

Take both units → Value = 600

Credit = 420

Remaining = 3928 – 600 = **3328**

Cumulative credit = 43.2 + 420 = **463.2**

---

### **3. BSE (1000)**

Take full 1 unit → Value = 1000

Credit = 500

Remaining = 3328 – 1000 = **2328**

Cumulative credit = 463.2 + 500 = **963.2**

---

### **4. JSW Energy (1360)**

Take full 4 units? → Value = 1360

Credit = 1360 × 0.55 = **748**

Check eligibility:

963.2 + 748 = **1711.2 → exceeds 1241 → NOT allowed**

Skip JSW.

---

### **5. HDFC Bank (3400)**

Take all 100 units? → Value = 3400

Credit = 3400 × 0.45 = **1530 → exceeds limit → restrict units**

Compute allowed maximum units:

```
units = floor((eligibleLimit - cumulativeCredit) ÷ (NAV × LTV))
units = floor((1241 – 963.2) ÷ (34 × 0.45))
units = floor(277.8 ÷ 15.3)
units = floor(18.17)
units = 18 units

```

Value released = 18 × 34 = **₹612**

Remaining = 2328 – 612 = **1716**

Cumulative credit = 963.2 + (18 × 34 × 0.45 = 275.4) = **1,238.6 (≤ 1241)** ✔

---

🔹 **Final Outcome for ₹4,000 request**

| Stock | Units Selected | Value |
| --- | --- | --- |
| Yes Bank | 6 | ₹72 |
| Groww | 2 | ₹600 |
| BSE | 1 | ₹1000 |
| HDFC Bank | 18 | ₹612 |
| **Total** | — | **₹2,284** |

No other stocks can be added without exceeding eligibility.

System selects **₹2,284 instead of ₹4,000** due to eligibility & unit constraints.

---

### 🔥 Summary of All Examples

| User Input | Possible? | Final Value Selected | Reason |
| --- | --- | --- | --- |
| ₹10,000 | ❌ Not possible | ₹6,432 max | Pledged value insufficient |
| ₹2,000 | ⚠️ Partially | ₹1,978 | Unit rounding & eligibility limits |
| ₹4,000 | ⚠️ Partially | ₹2,284 | Eligibility limit reached |

# **Error Handling & Edge Cases**

## **1. User enters more amount than available stock value**

Show blocking error:

> “You don’t have enough pledged value to unpledge this amount.”
> 

---

## **2. User enters amount exceeding DP eligibility**

Check:

```
sum(selected_stock_credit) ≤ DP - TOS - Interest

```

If violated:

> “You cannot unpledge stocks beyond your eligible limit.”
> 

---

## **3. Rounding down leads to under-selection**

If after selection:

```
total_selected_value < user_requested_value

```

Show non-blocking info message:

> “Based on available units, the closest value we can unpledge is ₹3812.”
> 

And allow user to proceed.

---

## **4. User requests small value that cannot select even 1 unit**

Example: user wants ₹5

But minimum NAV is ₹12

Show:

> “Minimum unpledge unit is 1 share of the lowest-priced stock.”
> 

---

## **5. User enters negative or zero values**

Error message:

> “Please enter a valid unpledge amount.”
> 

---

# API Response Format (Example)

{
"user_requested": 4000,
"value_selected": 3812,
"rounding_loss": 188,
"stocks_selected": [
{
"symbol": "HDFC Bank",
"units": 100,
"value": 3400
},
{
"symbol": "JSW Energy",
"units": 1,
"value": 340
},
{
"symbol": "Yes Bank",
"units": 6,
"value": 72
}
]
}

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