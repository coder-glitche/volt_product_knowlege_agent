# Offer page:- Limit too low

: Naman Agarwal
Created time: February 10, 2025 11:59 AM
Status: In progress
Last edited: February 28, 2025 3:51 PM

[MFCentral CAS API Response Structure Analysis](Offer%20page%20-%20Limit%20too%20low/MFCentral%20CAS%20API%20Response%20Structure%20Analysis%201a6e8d3af13a80cf9118d9fa17dfd4e7.md)

### Overview

LAMF helps borrowers access financing by offering a **credit line**, where the credit limit is determined as a **percentage of the eligible portfolio value** at the time of the offer. The **eligible portfolio** is retrieved via APIs from mutual fund custodians' RTAs or their joint venture, MF Central.

### **Objective**

This document aims to:

- Define the process for fetching all **folios associated with an investor**.
- List all possible reasons for **folio ineligibility**.
- Outline processes for converting **ineligible folios into eligible ones**.
- Address **borrower visibility issues** related to folio details.

## **Success Criteria**

1. **First-Time Right Credit Limit %** – This measures customers who fetch their limits once and proceed to take a loan.
2. **Conversion Rate** – Tracking the transition from the offer page to loan creation.
3. **Reduction in Inbound Queries** – Decreasing customer support inquiries regarding missing funds or eligibility issues.

## **Current MFD Process & Challenges**

### **Current Process**

- MFDs initiate applications and check the credit limit for the customer.
- If the **limit appears low**, they contact RMs for clarification.
- RMs advise them to perform a **detailed MFC fetch** to get a comprehensive list of associated funds.
- RMs compare the fetched data with the **summary API** and identify missing funds.
- If funds are missing, RMs request AMC statements from MFDs to determine why certain folios are ineligible.

This process **consumes significant RM bandwidth (15–30 minutes per case).**

### **Key Challenges**

1. **Mismatch in Credit Limit Calculation**
    - **Detailed API** does not include **lien-eligible units**, and custom logic applied can be inaccurate.
    - Summary API provides accurate limit but we don’t show the Total portfolio of the user.
    - This discrepancy **causes customer confusion and increases inbound queries**.
2. **Customer Reluctance to Borrow**
    - If the limit appears **too low**, MFDs hesitate to proceed with the loan.
3. **High RM Bandwidth Utilization**
    - RMs spend **significant time** explaining the credit limit and Funds ineligibility.
    - 16 % of inbound calls were for assisted journeys (966 calls),  where the majority of the issues were Limit related.
    - RMs can spend upwards of 30 mins in collecting and analysing AMC statements and mentioning in-eleigiblity reasons to MFDs
4. **Lack of Visibility for Ineligible Funds**
    - The current journey only shows **eligible funds**, which may be significantly lower than a customer's total portfolio.
    - **DMAT holdings, locked, and liened units are not displayed**, leading to perception issues.
5. **Limitations in the MFC Detailed API**
    - It provides a **full transaction history** for up to **15 years** but does not always accurately reflect the **current portfolio**.
    - **Funds registered under different phone numbers** in Fund values.
6. **Common Customer Portfolio Issues (Identified by RMs)**
    - Funds registered under different **mobile numbers**.
    - **KYC issues**.
    - **Email mismatches**.
    - **Minor funds** impacting eligibility.

Potential solutions 

| S. no | Issues | solutions  |  |
| --- | --- | --- | --- |
| 1 | Low portfolio amount | Show the Whole portfolio in the Journey from only eligible funds |  |
| 2 | RM bandwidth | Removing Detailed API to summary for Accurate Limit  |  |
| 3 | Reason for Ineligible funds | Add FAQ or Info in the In-eligible funds section for the reasons  |  |

## Moving Eligibility check in 15 sec from Detailed to summary

- MFDs currently check a customer’s limit using the **Detailed API** in the Partner Portal.
- The limit provided is **often incorrect** because the Detailed API **does not include lien-eligible units**.
- When the MFD starts an application and proceeds to the fetch step, the **calculated limit differs** from the one initially shown in the Detailed API.
- The **Detailed API was originally used** for eligibility checks because it fetches **all customer funds**, including those linked to **other phone numbers**.
    - However, after analyzing **18 PANs** with both **Summary and Detailed pulls**, the deviations were **not** caused by funds being linked to different phone numbers.
    - Instead, the discrepancies resulted from **how different unit types were stored as portfolio units**.
- To eliminate **limit discrepancies**, we are **switching from the Detailed API to the Summary API** for eligibility checks.

# In- Eligible funds in the B2C journey

### **User Flow**

1. **User fetches funds** via **MFC Summary API**.
2. Funds may be ineligible due to:
    - **Lender-specific approved fund lists**.
    - **Lien eligibility rules**, such as:
        - Already **liened** funds.
        - **ELSS lock-in periods**.
        - **Minor-held funds**.
3. Users will see **two categories** of funds:
    - **Eligible funds**.
    - **Ineligible funds**.
4. The **fund amounts will be displayed at the fund level**.
5. If **the total units are> lien-eligible units**, the fund will appear in both sections:
    - **Eligible units = Lien-eligible units × NAV**.
    - **Ineligible units = (Total - Lien-eligible) × NAV**.
6. General ineligibility reasons will be displayed, as the API does not provide detailed reasons.
7. **Ineligible funds will be visually separated** (e.g., greyed out).
8. Data for **ineligible funds will be sourced from the MFC Summary API**.

📌 **Figma Link:** [MFD Partner Flow](https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/MFD-partner-flow?node-id=6146-7252&t=t3aY1JpgxbYaEbn1-0)

## Offer page

Questions pending 

1. User fetches from KFIN/CAMs
    1. How can we De dedupe check the funds between RTAs and MFC?

Pledge 

- show updated list on pledge?