# LAS: Collateral management system

Last Edited: July 28, 2025 8:43 PM
PRD ETA: June 27, 2025
PRD Owner: Vaibhav Arora
Status: Completed

# **What is CMS?**

The Collateral Management System (CMS) will act as the central infrastructure for managing pledged shares for a Loan Against Shares (LAS) product.

It will interface with the Loan Origination System (LOS), Loan Management System (LMS), and Depository Participant (DP) — SHCIL — to manage the full lifecycle of collateral from validation to lien marking, valuation, revocation, and reconciliation.

It will also include risk management via real-time LTV monitoring, handling of corporate actions, and tools for operations teams.

[CMS system architecture](https://claude.ai/public/artifacts/b5a68c3c-4705-4c9d-b34b-52a1d6bb8ec4)

---

# Why do we need a CMS?

A **Collateral Management System (CMS)** is essential for a **Loan Against Shares (LAS)** product because collateral (in the form of pledged shares) is **the core security** backing the loan. 

Without an automated, secure, and integrated system to manage this collateral, the business is exposed to **operational risk, financial risk, and regulatory gaps**.

1. Centralised tracking and management of collaterals: Currently all collaterals are managed by the LMS which makes it very risk prone: A CMS ensures each step is trackable, audit-logged, and consistent with external systems (DP/SHCIL) and internal ones (LMS/LOS).

2. CMS constantly monitors Loan-to-Value (LTV) ratios. If share prices fall, LTV breaches can be automatically flagged (exposure tracking), triggering margin calls or partial lien revocation.

3. Logic separation from LMS: CMS has a lot of collateral management intelligence which should be LMS agnostic, this will make our LMS very modular and easily replaceable since majority of the complexity of collateral management will be handled via CMS.

---

# **How are others solving this problem?**

The approach to collateral management for Loan Against Shares (LAS) varies widely across the lending ecosystem, largely depending on a company’s scale, tech maturity, and risk appetite. Broadly, solutions fall into two categories:

### 1. **Tightly Coupled CMS-LMS Systems (Usually Vendor-Provided)**

Some lenders use **end-to-end lending platforms** where the CMS is embedded within the LMS — often provided by a third-party vendor. These platforms offer:

- Pre-integrated lien workflows
- Basic LTV tracking
- Unified borrower and collateral view

### 2. **No CMS — Operations-Led Collateral Tracking**

Most early-stage or mid-sized lenders operate without a dedicated CMS. Instead, they rely on:

- Manual **ops processes** to initiate and track lien/revocation files
- **Excel sheets or shared dashboards** to monitor pledged ISINs and LTVs
- Basic **custom reports from LMS** to monitor pledged assets

---

# Responsibilities of a CMS

[CMS responsibilities](LAS%20Collateral%20management%20system/CMS%20responsibilities%2021fe8d3af13a80919de0dfe03557e6a4.csv)