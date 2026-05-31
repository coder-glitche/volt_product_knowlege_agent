# Corporate action - Data feed

Last Edited: March 19, 2026 9:44 PM
PRD Owner: Vaibhav Arora
Status: Completed

# Corporate Actions Data Feed

## Overview

To support monitoring of securities pledged as collateral, we have reviewed a **Corporate Actions data feed sourced from BSE end-of-day bulletins**. 

This feed provides information on **events and disclosures that may impact the value, structure, or tradability of securities**. The data is consumed daily and can be used by the Risk team to monitor portfolio changes and identify events that may require action.

The data covers the following broad categories:

- Corporate action events
- Company structural changes
- Market disclosures
- Large market transactions
- Insider activity
- Liquidity indicators

---

# 1. Corporate Action Events

This dataset contains information about **corporate actions declared by listed companies** that may affect the number of shares, price, or entitlement of shareholders.

Typical corporate actions include:

- Dividends
- Stock splits
- Bonus issues
- Rights issues
- Buybacks
- Capital restructuring events

For each event, the feed provides key reference dates such as:

- **Record Date** – Date used to determine shareholder eligibility
- **Ex-Date** – Date after which the security trades without the entitlement
- **Cum Date** – Date before which investors must hold shares to be eligible
- **Effective Dates** – Time period during which the action is applicable

In addition, where applicable, the feed also provides:

- Dividend amount or payout value
- Share conversion ratios (e.g., split or bonus ratios)
- Share quantity adjustments
- Offer price or premium for rights issues

These events are critical for adjusting **collateral valuation and share quantities** in pledged portfolios.

---

# 2. Corporate Action Classification

A separate master dataset provides the **mapping of corporate action identifiers to the specific event type** (e.g., dividend, split, bonus).

This allows systems to interpret the corporate action feed and determine the **nature of the event impacting a security.**

---