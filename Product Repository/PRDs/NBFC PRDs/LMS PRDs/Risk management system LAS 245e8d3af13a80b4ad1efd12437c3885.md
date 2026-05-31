# Risk management system: LAS

Last Edited: May 2, 2026 12:26 PM
PRD ETA: August 6, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

For loans against collateral with dynamically priced assets like:

- Shares
- Mutual funds

It becomes important to ensure that all transactions and exposure given out to user against loans committed by the NBFC, are validated. As of now only the LMS was responsible for doing these validations, but as our systems and products get more complex, there is an additional need for a separate system with logic separation to validate all transactions.

Traditionally, validation of disbursals, top-ups, sell-offs, or withdrawals was handled solely within the LMS (Loan Management System). However, with increasing complexity of the LAS product—such as more volatile collaterals, multiple transaction types, and tighter regulatory risk monitoring—there is a growing need to decouple this logic into a separate system of record and computation.

It becomes important to ensure that all transactions and exposure given out to users against loans committed by the NBFC are validated. As of now, only the LMS was responsible for doing these validations, but as our systems and products get more complex, there is an additional need for a separate system with logic separation to validate all transactions.

---

# **How do we measure success?**

- LTV breach alerting should have 100% coverage (As a percentage of total portfolio) - 

Total outstanding of customers with LTV breaches / Total outstanding (NBFC)

Total value of excess (breach amount) / Total outstanding of customers with LTV breaches
- Number of customers in LTV breach as a percentage of total customers
- Accuracy of risk tracking and validation by RMS

---

# **How are others solving this problem?**

### Traditional Lenders & NBFCs

Most NBFCs manage risk through strong operational controls and large risk teams. Risk is tracked manually using dashboards, EOD price feeds, afnd overrides. This is a reactive, people-heavy approach and doesn’t scale well with volume or complexity. 

### Hedge Funds & Active Managers

At the other end, hedge funds and structured credit desks run automated systems that respond to real-time market data. Exposures are actively adjusted using predictive models and leading indicators. These setups are capital- and engineering-intensive.

### Our Approach

Given our context — approved securities list, small-ticket loans, and rapid disbursal expectations — we’re building a **semi-automated, alert-based RMS**. The idea is to:

- Recompute exposure and LTV every 15 minutes using live market data
- Trigger alerts when thresholds are breached
- Enable ops to act quickly, rather than monitor continuously
- Validate user-side transactions (e.g., disbursals, releases) using up-to-date price

This gives us the automation needed to scale, while retaining manual controls where needed.

---

# **What is the solution?**

The RMS module performs the following responsibilities:

- Ingest and store market data for all pledged securities every 15 minutes.
- Compute real-time LTV (Loan-to-Value) and exposure metrics using pledged quantity and live prices.
- Raise alerts for LTV or exposure breaches.
- Raise alerts to customers on exposure breaches
- Validate user transactions that may impact risk thresholds—like disbursals, release requests, or sell-offs—against real-time metrics before allowing execution.

## CRMS responsibilities:

- Approved script management (Ancillary asks to be also included: Example customer communications, ageing management)
- Collateral price management
- Exposure tracking and breach
- DP management
- Shortfall computation
- Asset classification and concentration monitoring

## **Modules Covered in This PRD**

| Feature |
| --- |
| Market Data Consumption |
| Exposure and LTV Monitoring |

## **System Context**

- **LMS**: Maintains the loan and collateral relationship; updates collateral value once a day.
- **CMS**: Tracks actual pledged quantities and
- **RMS**: Computes real-time LTV and exposure metrics using CMS positions and real-time prices.
- **DP (Depository Participant)**: Sends pledged quantity and status updates.
- **CMOTS: Market Data Feed**: External provider (e.g., NSE/BSE, or a vendor like providing 15-minute EOD-equivalent price refreshes.

### Functional Requirements

| Requirement | Notes |
| --- | --- |
| Fetch prices for all NSE/BSE equities (pledged stocks only) every 15 minutes | Pull from market feed API |
| Support for mapping stock symbols to ISIN and client security IDs | To enable join with CMS and LMS records |
| Maintain a historical price table for every ISIN | For LTV and simulation |
| Handle API rate limits and failures with retries and alerting | Alert on 2 consecutive failures |
| Store timestamped price snapshots with source metadata | Granular traceability for audits |

Sample API response (Proposed) to CMOTS:

```jsx
[
  {
    "isin": "INE002A01018",
    "nse_symbol": "TCS",
    "bse_symbol": "532540",
    "price_timestamp": "2025-08-05T23:30:00",
    "nse_price": 3720.10,
    "bse_price": 3718.00,
    "volatility_flag": {
      "asm": true,
      "gsm": false,
      "mwpl": false,
      "circuit": false
    }
  },
  {
    "isin": "INE001A01036",
    "nse_symbol": "RELIANCE",
    "bse_symbol": "500325",
    "price_timestamp": "2025-08-05T23:25:00",
    "nse_price": 2890.45,
    "bse_price": 2885.00,
    "volatility_flag": {
      "asm": false,
      "gsm": false,
      "mwpl": true,
      "circuit": false
    }
  }
]
```

## Market data consumption and exposure breach:

RMS will consume **real-time price feeds from CMOTS** to track exposure for all active loan accounts. Prices will refresh every 15 minutes. Exposure tracking will run in batch mode based on the latest available ISIN prices. Additionally, **on-demand exposure reports** can be generated for any loan using the most recent market snapshot.

Exposure is computed at the **loan account level** using pledged quantity (from CMS), outstanding principal (from LMS), and real-time prices (from RMS). The system will identify breaches across four key dimensions:

### **Portfolio Shortfall Breach** *(Min LTV-based)*

> Uses a conservative (minimum) LTV to check if DP is sufficient.
> 
> 
> **Formula**:
> 
> `Shortfall = DP (at Min LTV) - POS`
> 
> Triggers if DP does not meet the portfolio-level LTV buffer. (Whenever it is negative)
> 

### **Regulatory Shortfall Breach** *(Max LTV-based)*

> Validates against upper LTV limits as per internal/regulatory guidelines.
> 
> 
> **Formula**:
> 
> `Shortfall = DP (at Max LTV) - POS`
> 
> Triggers if LTV exceeds the regulatory threshold.
> 

### **Collateral Value Breach**

> Flags breach based on market value of pledged collateral.
> 
> 
> **Formula**:
> 
> `Collateral Market Value (CMV) - (Total Outstanding (TOS) + Accrued interest`)
> 
> `DP (at Min LTV) - Total Outstanding (TOS) + Accrued interest`
> 
> Triggers if the current collateral value is insufficient to cover outstanding dues.
> 

### Execution Mode

- **Scheduled batch run** every 15 minutes with market data refresh - P1
- **API-based on-demand** trigger for ad hoc exposure report generation - P0

### Triggering of reports:

Enable operations or risk teams to **manually trigger** the **exposure calculation batch job** from the Command Centre. This will fetch the latest market prices, recompute exposures and LTVs across all active loan accounts, and persist output for downstream access and alerting.

| Requirement | Description |
| --- | --- |
| Trigger RMS Exposure Batch | A trigger action should be available in the Command Centre UI to initiate exposure computation across all active loans |
| Job Status Tracking | The job should have statuses: `Pending`, `Running`, `Completed`, `Failed` — visible in CC |
| Timestamped Execution | Every batch run should store a timestamp and ID so that the output can be tied to a specific run |
| Input Price Snapshot | Each batch run should use the latest available 15-min price batch from RMS database at the time of trigger |
| Access Control | Only authorized roles (e.g. Risk Ops, Admin) should be able to trigger the batch |
| Audit Logging | Every trigger (manual or API) should be logged with user, timestamp, and parameters used |
| Alert Routing Toggle | Trigger should optionally enable/disable post-computation alerts — useful for dry runs or simulations |

## **Loan Account-Level Exposure Breach Report**

This table calculates and flags exposures at the **loan account level**, considering pledged collateral quantities, market prices, and distributed POS (Principal Outstanding).

### **Formula Notes**:

- Collateral market value (CMV) = DP Quantity × Market Price
- LTVR = POS / Total Collateral Value

| Loan ID | Customer ID | Total DP | CMV (₹) | TOS (₹) |  POS (₹) |  LTVR (%) | Max Allowed LTV (%) | Ageing | LTV Breach |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FXLAN1234 | FXCID3423 | 1,500 | ₹6,75,000 |  | ₹4,00,000 | 59.26% | 50% |  | Yes |
| FXLAN5678 | FXCID3423 | 800 | ₹2,40,000 |  | ₹1,00,000 | 41.67% | 60% |  | No |

## **Collateral-Level Exposure Breach Report**

This table calculates exposure per **collateral (ISIN)** across the portfolio, aggregating the POS distributed to each collateral based on its contribution to the total DP value.

### **Allocation Logic**:

- For each loan with multiple collaterals:
    - POS is split proportionally based on CMV of each collateral.
- Exposure Breaches flagged:
    - Shortfall: Pledged Quantity < Required Quantity
    - Collateral LTV > Max LTV allowed
    - Concentration > Configured Limit

| FXLAN | Category | ISIN | Security Name | Total Pledged Qty | Market Price (₹) | CMV (₹) | Allocated POS (₹) | LTV amount | LTVR (%) | Max Allowed LTV (%) | Shortfall Qty | Concentration (%) | Breach Type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FXLAN1234 | Cat A | INF200K01XY2 | HDFC Bank | 10,000 | ₹450 | ₹45,00,000 | ₹28,00,000 |  | 62.22% | 50% | 2,000 | 15% | LTV + Shortfallrue |
| FXLAN1234 | Cat B | INF789Z01PO4 | Reliance | 4,000 | ₹2,700 | ₹1,08,00,000 | ₹50,00,000 |  | 46.30% | 60% | 0 | 45% | NoneFalse |

![image.png](Risk%20management%20system%20LAS/image.png)

---

# **Design**

NA

---

# **Analytics**

NA

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

### Traditional Lenders & NBFCs

Most NBFCs manage risk through strong operational controls and large risk teams. Risk is tracked manually using dashboards, EOD price feeds, and overrides. This is a reactive, people-heavy approach and doesn’t scale well with volume or complexity.

### Hedge Funds & Active Managers

At the other end, hedge funds and structured credit desks run automated systems that respond to real-time market data. Exposures are actively adjusted using predictive models and leading indicators. These setups are capital- and engineering-intensive.

### Our Approach

Given our context — approved securities list, small-ticket loans, and rapid disbursal expectations — we’re building a **semi-automated, alert-based RMS**. The idea is to:

- Recompute exposure and LTV every 15 minutes using live market data
- Trigger alerts when thresholds are breached
- Enable ops to act quickly, rather than monitor continuously
- Validate user-side transactions (e.g., disbursals, releases) using up-to-date risk metrics

This gives us the automation needed to scale, while retaining manual controls where needed.