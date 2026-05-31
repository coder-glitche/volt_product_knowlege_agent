# PRD — Term Loan Repayment STP Threshold Update

: Yogesh D
Created time: May 28, 2026 11:44 AM
Status: Not started
Last edited: May 29, 2026 5:51 PM

# What Problem are we solving?

- Current STP repayment thresholds are overly conservative, causing valid low-risk repayments to be unnecessarily routed to NSTP via `REPAYMENT_AMOUNT_LIMIT_EXCEEDED` (>₹15L) and `REPAYMENT_DAILY_COUNT_EXCEEDED` (>4 repayments/day per LAN).
- Jan–May 2026 production data shows minimal breach risk: only 3 of 1,952 customers (0.15%) made repayments above ₹15L (max observed: ₹20.1L), and no LAN exceeded 5 repayments in a day — indicating the limits can be safely relaxed.
- Unlike other LSPs (Razorpay for Volt, PhonePe dashboard for PhonePe), there is no Cred repayment dashboard available to Ops for independent transaction validation. Every NSTP repayment task escalates to the manager before it can be approved — creating a hard operational dependency that delays repayment posting and consumes avoidable bandwidth.

# How do we measure success?

- STP conversion rate : With enhancement of limit the stp conversion rate is set to reach 100%
- Visibility to OPS : The repayment count will be made visible to checker is checker task description along with updated limit amount.

# Solution

Two config changes — applies to all LSPs on the term loan STP path

| Config Key | Current | New |
| --- | --- | --- |
| stp-flow.repayment.amount.limit | 1500000 (₹15L) | 3500000 (₹35L) |
| stp-flow.repayment.count.limit | 2 | 6 |

All other STP checks and config keys remain unchanged.

## Data Basis (Jan–May 2026)

**Amount threshold:**

| Metric | Value |
| --- | --- |
| Total customers | 1,952 |
| Customers who made repayment > ₹15L | 3 (0.15%) |
| Max repayment amount observed | ₹20,11,340 |
| Proposed new limit | ₹35L (~74% headroom above observed max) |

Only 0.15% of the customer base ever triggered the amount breach. These are legitimate high-value repayments being held for no risk-based reason.

**Count threshold:**

| Repayments/day | Unique LANs |
| --- | --- |
| 3 | 32 |
| 4 | 7 |
| 5 | 4 |
| > 5 | 0 |

No LAN exceeded 5 repayments/day in the entire period. Raising the limit to 5 captures all observed behaviour in STP.

**Expected STP conversion rate post-change: 100%**

## NSTP Checker Task Description Update

For the rare repayments that still breach the new thresholds, the checker task description is updated to include amount and count context — so checkers have what they need without any external dashboard.

| Reason Code | Task Description |
| --- | --- |
| `REPAYMENT_AMOUNT_LIMIT_EXCEEDED` | Repayment of ₹{repayment_amount} for {LAN} exceeds the STP limit of ₹35L. Approval required. |
| `REPAYMENT_DAILY_COUNT_EXCEEDED` | Repayment of ₹{repayment_amount} for {LAN} is the {nth} repayment today, exceeding the STP daily limit of 5. Gateway order link available for verification. Approval required. |