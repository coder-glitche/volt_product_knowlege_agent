# PRD: MFD Performance Metrics & Earnings Display

: Naman Agarwal
Created time: May 19, 2025 12:43 PM
Status: Not started
Last edited: May 21, 2025 12:46 PM

## **1. Introduction**

This feature will give empanelled MFDs a clear, transparent, and motivating view of their performance related to the *Volt Money* program offered by Volt. The dashboard will show:

- Their sourced **MF Loan AUM**
- Applicable **trail income rate**
- **Trail income earned**
- **Account opening bonuses**

The goal is to make it simple for MFDs to understand how their efforts are driving their earnings.

---

## **2. Goals & Objectives**

### **Primary Goal**

To clearly display an MFD’s Volt Money performance, including MF Loan AUM, trail income, and incentives.

### **MFD User Objectives**

- Understand how MF Loan AUM translates into income or Increase visibility to the MFDs
- Track progress toward higher income tiers
- See a breakdown of earnings and new account bonuses
- View historical trends and performance

### **Business Objectives**

- Encourage MFDs to grow MF Loan AUM
- Boost Volt Money customer acquisition
- Reduce support queries about commissions

## **Success Metrics**

- MFD Monthly visits to partner portal
- MFD Repeat rate
- MFD Avg number of applicaitons per month
- upward move in MFD LAMF AUM Buckets

---

## **3. User Stories**

- *As an MFD*, I want to view my current MF Loan AUM so I know my payout tier.
- I want to know my current trail income rate based on slabs.
- I want to see how close I am to the next earning tier.
- I want to track monthly/quarterly/yearly trail income.
- I want to verify bonuses for each new LAMF line opened.
- I want a full summary of earnings: trail income + bonuses.
- I want to view historical performance trends.
- I want to quickly reference the trail income slab table.

---

## **4. Feature Breakdown & UI/UX**

### **4.1 Main Dashboard: Volt Money Performance Overview**

**Key Metrics:**

| Metric | Example | Tooltip |
| --- | --- | --- |
| **Current AUM** | ₹12.5 Cr | Outstanding principal under Volt Money |
| **Trail Rate** | 0.55% | Based on current AUM slab |
| **Trail Income (This Month)** | ₹57,291 | Clarify if based on daily accrual, etc. |
| **New Accounts (MTD)** | 5 | From Onboarding CRM |
| **Bonus Earned (MTD)** | ₹1,000 | ₹200 x new accounts |
| **Total Earnings (MTD)** | ₹58,291 | Trail + Bonus |

**Progress Bar:**

Shows current AUM and amount needed to reach next slab (e.g., ₹2.5 Cr more to reach 0.60%).

---

### **4.2 Commission Slab Display**

| MF Loan AUM | Trail Income Rate |
| --- | --- |
| 0 – 10 Cr | 0.50% |
| 10 – 15 Cr | 0.55% |
| 15 – 20 Cr | 0.60% |
| 20 – 30 Cr | 0.65% |
| > 30 Cr | TBD |

---

### **4.3 Earnings Breakdown**

**Filters:** Select period (MTD, last month, custom).

**Details:**

- Monthly trail accruals based on Application level
- MF Loan AUM at the time of calculation
- Bonus details (masked customer ID, date, ₹200/bonus)

---

### **4.4 Historical Performance Charts**

- MF Loan AUM over time (monthly/quarterly)
- Trail Income over time (monthly/quarterly)
- New accounts opened trend

---

##