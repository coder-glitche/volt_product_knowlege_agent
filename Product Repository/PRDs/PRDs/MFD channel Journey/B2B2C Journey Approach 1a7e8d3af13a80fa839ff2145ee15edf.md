# B2B2C Journey Approach

- MFDs need a **quick and simple way** to check a customer's limit and initiate an application.
- MFDs want **clear next steps** for the customer, depending on their status:
    - If it is **new**, create an application.
    - If **in process**, continue the application.
    - If Active application then if **interest is due**, handle repayment, shortfall, or charges.

TAT DSP 

| Channel | B2C | B2B2C | overall volt  | B2C | B2B2C | overall volt  |
| --- | --- | --- | --- | --- | --- | --- |
| **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** |
| KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 |
| MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 |
| MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 |
| KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 |
| KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 |
| KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 |
| KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 |
| BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 |
| DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 |
| ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 |
| LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 |
| CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 |

## Enhancing existing Journey

- MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue.
- MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually.
- Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking).
    - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple visible steps.
- Maintaining **consistency across platforms** is essential for **efficient support and issue resolution**.
- Major challenges in the MFD faced in the LAMF journey are similar to Issues faced by customers [Customer vs MFD](Customer%20vs%20MFD%201ade8d3af13a80db9004d15ffda8d14d.md)
- MFDs also rely on their employees to **complete applications on behalf of customers**. So we need to keep the journey beginner friendly

## **Creating a New MFD-Focused Journey**

- MFD wants to see the Detailed view of the funds of the customer
    - We can make the Fetched folio screen **Optimised for Desktop**
    - This process is **not perceived as difficult** in the current journey as per feedback provided by MFDs.
- MFD wants to complete the application quickly
    - MFD can save time by p**re-filling customer Information** like Bank account and KYC details
    - Time savings are minimal as the KYC details are drop-down
    - **The father’s name can be pre-filled** for 40-50% of the cases from Digio/C-kyc, and the **Mother’s name** can be removed, reducing time even when the customer is on a call.
    - We are fetching the Bank account Details from MFC fetch.
- MFD wants the user to complete some steps of the application
    - Selfie link is a big issue for MFD as customers are not physically present with them.
    - MFD can share a link to the customer to complete the application.
- MFD wants to complete the application step async with the customer in case some are pending on the customer
    - The LAMF journey consists of **four major semi-independent steps**, apart from the final agreement:
        1. **Fetch → Offer → Pledge**
        2. **KYC → Photo Verification**
        3. **Bank Account Verification → Bank Mandate**
        4. **KFS → Agreement**
    - **The Bank Mandate was moved to later steps** since its TAT is the highest, and user buy-in is highest toward the end.
    - **The pledge step was moved to the end** to minimize operational overhead and reduce costs related to **unpledging units**.