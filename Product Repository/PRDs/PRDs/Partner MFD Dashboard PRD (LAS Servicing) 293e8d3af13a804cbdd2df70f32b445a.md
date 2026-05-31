# Partner / MFD Dashboard PRD (LAS Servicing)

: Ranjan kumar Singh
Created time: October 21, 2025 5:16 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

- Scoping rough
    
    BAJAJ:
    Web: We open the URL in the same tab replacing Volt's URL.
    Android/iOS: We navigate to another screen which is a webview and open the url in the WebView.
    TATA:
    Web: We open the URL in the same tab replacing Volt's URL.
    Android/iOS: We open in inApp browser.
    

# **What problem are we solving?**

Volt currently provides a **LAMF Servicing Dashboard** for partners (MFDs) to view and manage completed loan applications.

With the launch of **LAS (Loan Against Shares)**, we need to **extend the Partner Dashboard** to:

- Support **LAS servicing & monitoring**
- Provide **cross-product visibility** (LAMF + LAS)
- Maintain consistency, data integrity, and usability across both products

### **In-Scope**

- LAS product integration in partner dashboard
- Enhanced filters, sorting, and search
    - In V0: We will include Product type inside the Filters
- Product-type tagging and segregation
- Action CTAs (view details, view as client, share client link)
- LAS servicing segmentation (Interest Due, Renewal Due, Shortfall, etc.)
- Partner communication templates (alerts, Servicing reminders, sharing links)

### **Out-of-Scope**

- Commission or payout
- Nudge on completed application page if customer is in shortfall for LAS
- Nudge for LAS if not eligible for Enhancement

---

# **How do we measure success?**

**Success metric:**

| **Category** | **Metric** | **Definition / Measurement** | **Target / Benchmark** | **Insight / Purpose** |
| --- | --- | --- | --- | --- |
| **Partner Activation** | **Active Partner %** | (# of MFDs with at least 1 LAS customer ÷ total onboarded MFDs) × 100 | ≥ 40 % within 1st quarter | Measures adoption and engagement of partners for LAS product |
| **Partner Portfolio Scale** | **LAS Portfolio Value (MFD Channel)** | Total LAS AUM (loan book value) originated or serviced via MFDs | ₹ X Cr within 3 months | Indicates product–market fit and partner contribution |
| **Partner Engagement** | **Avg. Actions per Partner / week** | (# of dashboard actions – view details, share link, eligibility check – ÷ active partners) | Baseline + 20 % MoM | Shows whether partners actively use servicing tools |
| **Customer Activation (B2B2C)** | **LAS Account Activation Rate** | (# of LAS accounts disbursed ÷ # of LAS accounts opened via partners) × 100 | ≥ 70 % | Conversion from account creation to first drawdown |
| **Servicing Adoption** | **% of LAS clients viewed by partners post-disbursal** | (# of LAS clients whose account was accessed by partner in servicing dashboard ÷ total LAS clients via that partner) × 100 | ≥ 80 % | Validates partner involvement in post-loan servicing |
| **Operational Efficiency** | **Partner-related LAS support tickets per 100 customers** | (# of LAS servicing tickets raised by partners ÷ # of LAS customers managed by partners) × 100 | ≤ 5 | Indicates dashboard usability & process clarity |
| **Communication Effectiveness** | **Share Link CTR (Partner-to-Client)** | (# clients clicking shared LAS links ÷ total links shared by partners) × 100 | ≥ 25 % | Measures end-user engagement from partner communication |
| **Revenue Impact** | **% of LAS Book through Partner Channel** | (LAS disbursed via MFD ÷ total LAS disbursed) × 100 | ≥ 50 % | Quantifies business contribution of B2B2C route |
| **Partner Retention** | **Returning Partner Rate** | (# of partners originating LAS in multiple months ÷ partners with ≥ 1 LAS in month 1) × 100 | ≥ 60 % | Measures sustainability of partner engagement |
| **System Reliability** | **Partner Dashboard Uptime / API Success Rate** | % of successful LAS API calls on MFD dashboard | ≥ 99 % | Ensures partner-side stability |

**Guardrail Metrics (for MFD Channel LAS Launch):**

| **Category** | **Metric** | **Definition / Measurement** | **Threshold / Guardrail Intent** |
| --- | --- | --- | --- |
| **LAMF Stability** | **LAMF Dashboard Error Rate** | (# failed API calls for LAMF ÷ total calls) × 100 | ≤ 1 % variance from pre-LAS baseline → ensure LAS rollout doesn’t break existing LAMF servicing |
| **Partner Support Load** | **Partner Support Ticket Volume** | Delta % in partner support tickets (week over week) | ≤ 10 % increase post-launch; signals training or UX issues |
| **Customer Experience** | **Incorrect / Mis-tagged Communication Events** | % of LAS notifications sent with wrong product tag | 0 % – strict guardrail |
| **Data Accuracy** | **Mismatch Rate (Credit Limit / Outstanding)** | (# of data mismatches between LMS & dashboard) ÷ total accounts | ≤ 0.5 % → ensure reliable display |
| **Cross-Product Integrity** | **Duplicate Loan View Incidents** | # of customers appearing under both LAS & LAMF incorrectly | ≤ 0.1 % of customers |
| **Comms Queue Stability** | **Event Delivery Success (Partner Alerts)** | % of partner notifications delivered successfully | ≥ 99 % |
| **Regulatory / Compliance** | **Client PII Exposure / Audit Errors** | # of PII leaks or audit issues on partner dashboard | 0 incidents |

---

# **How are others solving this problem?**

---

# **What is the solution?**

Volt will **extend its existing Partner (MFD) Dashboard** to support **LAS (Loan Against Shares)** servicing with:

- **Full cross-product visibility** across **LAMF and LAS**
- Ability for partners to **manage LAS loan accounts on behalf of customers**
- Enable **servicing communication** for LAS

This extension ensures that MFDs can seamlessly service both **LAMF and LAS portfolios** through a **single, unified platform**, driving operational efficiency, improved customer experience, and higher LAS adoption.

## Requirements overview (optional)

- Integrate **LAS account data** from LMS APIs into the existing partner dashboard.
- Maintain **common structure and UI** for both LAMF and LAS.
- Enable **segmentation** (Interest Due, Renewal Due, Shortfall).
- Introduce **product-level badges and filters**.
- Allow **cross-product visibility and actionability**.
- Support **data accuracy and stability guardrails**.

## User Stories & Acceptance Criteria

**Unified completed application customer view:**

| **User Story** | **Acceptance Criteria** |
| --- | --- |
| As an MFD, I should be able to view all my clients (LAS + LAMF) in one place | Unified table listing all customers with product tags (LAS / LAMF) |
| As an MFD, I should be able to filter clients by product type, Lender and account status | Filters work dynamically and show count badges (e.g., LAS: 10, LAMF: 5) |
| As an MFD, I should be able to search by name, phone, Email or loan account number | Search returns results across both LAS and LAMF datasets |
| As an MFD, I should see key account metrics: Total Limit, Available Limit, Outstanding Amount |  |
| As an MFD, I should see each client’s status (Active, Closed)  | Inside the View clients details page |

**Product-Type Differentiation:**

| **User Story** | **Acceptance Criteria** |
| --- | --- |
| As an MFD, I should clearly see which product each client belongs to | Product column shows “LAMF” / “LAS” tag |
| As an MFD, I should be able to toggle between “All Customers”, “LAS Customers”, and “LAMF Customers” | Tab selection dynamically loads filtered datasets |
| As an MFD, I should be able to view multiple accounts of same user (e.g., LAS + LAMF) | Separate row entries for each product-account combination |

**Customer Segmentation & Alerts:**

| **User Story** | **Acceptance Criteria** |
| --- | --- |
| As an MFD, I should see segmented lists for interest due, renewal due, and shortfall customers | Count badges visible on tabs; click filters data |
| As an MFD, I should be able to view clients nearing shortfall or overdue interest | Highlighted rows or color badges |

**Detailed Client View:**

| **User Story** | **Acceptance Criteria** |
| --- | --- |
| As an MFD, I should be able to click “View Details” to open loan-level summary | Opens right-side modal showing credit details |
| As an MFD, I should be able to “View as Client” | Redirects to PLJ |
| As an MFD, I should be able to “Share Client Link” |  |

## Requirements

- Unified API integration for multi-product servicing (LAMF + LAS).
- Dynamic tab configuration by product type and servicing category.
- Contextual nudges for LAS shortfall.
- Backward compatibility with existing LAMF dashboard.
- Partner comms via configurable template engine.

---

# **Design**

1. **Completed application view:**
    - Loan type is multi select dropdown
    - By default all loan type will be selected

![Screenshot 2025-10-22 at 12.07.10 PM.png](Partner%20MFD%20Dashboard%20PRD%20(LAS%20Servicing)/Screenshot_2025-10-22_at_12.07.10_PM.png)

1. **Customers with Interest due  view:**

![Screenshot 2025-10-22 at 12.14.27 PM.png](Partner%20MFD%20Dashboard%20PRD%20(LAS%20Servicing)/Screenshot_2025-10-22_at_12.14.27_PM.png)

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

- How do partners check LAS eligibility for existing LAMF clients?

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