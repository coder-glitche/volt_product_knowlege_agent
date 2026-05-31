# CKYC Internal Report

: Surya Ganesh
Created time: March 31, 2025 12:40 PM
Status: Not started
Last edited: April 10, 2025 2:50 PM

# **What problem are we solving?**

The Central Registry of Securitisation Asset Reconstruction and Security Interest (CERSAI) manages the centralized CKYC database for customer KYC verification. Currently, our team lacks visibility into the performance metrics of CKYC application submissions, including success rates, failure reasons, and backlog status.

There is a need for comprehensive monitoring and reporting on CKYC applications to:

1. Track submission success rates
2. Identify common failure reasons
3. Monitor backlogs
4. Analyze trends in application processing
5. Provide actionable insights for process improvements

## Core Issue

Without proper dashboards and reporting, we cannot:

- Effectively track the performance of our CKYC submission process
- Identify bottlenecks in the system
- Make data-driven decisions to improve success rates
- Monitor the health of our integration with Decentro and CERSAI

## Current Issue

1. CKYC Download Failed: This error is due to exhausting the daily download limit (DSP Issue)
2. Record Validation Failed: This is a Decentro level rejection for cases where the pincode is not available in CERSAI’s Master List (DSP Issue)
3. Bulk CKYC Uploading Failed: Failure while uploading data to SFTP, can be due to password expiry (DSP Issue)
4. CKYC Search Failed: This is caused due to CERSAI’s API timeout or CERSAI’s api being intermittently down. (CERSAI Issue)
5. Document Validation And Compression Failed: Failed to compress the document within the limits (Decentro Issue)
6. “The CKYC portal balance is insufficient….“: Caused when the wallet balance for CKYC portal is low. (DSP Issue)
7. “Please enter Applicant Name Update Flag, Personal Details update Flag…”: Record considered for create instead of update (Decentro Issue)

---

# **How do we measure success?**

N/A

---

# **How are others solving this problem?**

N/A

---

# **What is the solution?**

The solution is to develop comprehensive dashboards that provide visibility into CKYC application metrics. These dashboards will track submissions, success rates, failure reasons, and backlogs.

## Requirements overview

The following dashboards need to be created:

## User stories / User flow

As an operations manager, I want to:

- View daily CKYC application submission performance
- Understand failure trends and root causes
- Monitor backlog status
- Track application distribution by status

## Requirements

**I. Total attempts dashboard:**

The dashboard should display:

1. Date
2. Total number of CKYC applications uploaded
3. Total number of applications successful
4. Percentage of applications successful
5. Total amount of backlog of applications
6. Total number of new applications registered (same date)

Sample table structure:

| Date | Applications Uploaded | Applications Successful | Success Rate (%) | Total Backlog | New Applications Registered |
| --- | --- | --- | --- | --- | --- |
| 2025-03-30 | 1,245 | 1,102 | 88.51% | 438 | 1,300 |
| 2025-03-29 | 1,180 | 1,025 | 86.86% | 295 | 1,215 |
| 2025-03-28 | 1,350 | 1,150 | 85.19% | 330 | 1,280 |

This dashboard should include:

- Daily trend chart showing applications uploaded vs. successful over the past 30 days
- Option to view data in daily, weekly, or monthly aggregations
- Ability to filter by date range (last 7 days, 30 days, 90 days, custom)
- Export functionality (CSV, Excel)

**II. Failure metrics on daily basis:**

The dashboard should display:

1. Total number of applications failed for particular reason
2. Reasons for failure
3. Percentage of total number of failed applications
4. Percentage of total number of attempts that day

Sample table structure:

| Failure Reason | Failed Count | % of Total Failures | % of Total Attempts |
| --- | --- | --- | --- |
| CKYC Download Failed  | 58 | 40.56% | 4.66% |
| Record Validation Failed: Pincode not present in the cersai's master pincode collection.  | 32 | 22.38% | 2.57% |
| Bulk CKYC Uploading Failed  | 25 | 17.48% | 2.01% |
| CKYC Search Failed  | 18 | 12.59% | 1.45% |
| Document Validation And Compression Failed  | 10 | 6.99% | 0.80% |

This dashboard should include:

- Pie chart showing distribution of failure reasons for the selected date range
- Filter by failure reason category (document issues, data validation, system errors)

**III. Failure distribution by source:**

The dashboard should display failures categorized by source:

1. Decentro's end (%): 
2. CERSAI's end (%)
3. DSP's end (%)

Sample table structure:

| Date Range | Total Failures | Decentro Failures | Decentro % | CERSAI Failures | CERSAI % | DSP Failures | DSP % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Last 7 days | 748 | 392 | 52.41% | 285 | 38.10% | 71 | 9.49% |
| Last 30 days | 3,250 | 1,755 | 54.00% | 1,138 | 35.02% | 357 | 10.98% |
| Last quarter | 8,932 | 4,645 | 52.00% | 3,215 | 36.00% | 1,072 | 12.00% |

This dashboard should include:

- Stacked bar chart showing the distribution of failures by source over time
- Pie chart showing the overall distribution for the selected time period

**IV. Distribution of all registered users till date:**

The dashboard should display:

1. Number of pending applications (awaiting processing)
2. Number of failed applications (to be re-tried)
3. Number of successfully completed applications
4. Number of applications in other states (if applicable)

Sample table structure:

| Status | Count | Percentage | Trend (vs Last Month) |
| --- | --- | --- | --- |
| Pending T+3 | 2,358 | 8.45% | ↑ 12.5% |
| Pending T+7 | 500 | 10.23% | ↓ 4.2% |
| Pending T+10 | 345 | 34.67% | ↓ 3.5% |
| Failed (To Be Retried) | 4,125 | 14.78% | ↓ 31.2% |
| Successfully Completed | 21,302 | 76.32% | ↑ 5.8% |
| In Progress | 125 | 0.45% | ↔ 0.1% |
| **Total** | 28,755 | **100%** | **↑ 8.3%** |

This dashboard should include:

- Pie chart showing the overall distribution by status
- Trend chart showing changes in distribution over time (monthly view)
- Ability to filter by date range, region, and application type

**V. Data refresh requirements:**

The dashboards should:

1. Report gets generated everyday at 7pm 
2. Allow for date range filtering

---

# **Design**

---

# **Analytics**

N/A

---

# **Timeline/Release Planning**

N/A

---

# **Go to market**

## Marketing

N/A

## Ops & Sales training

N/A

## Frequently asked questions (FAQs)

N/A

---

# **Action items / checklist**

- [ ]  Product
    - [ ]  Finalize dashboard requirements
    - [ ]  Create mockups for dashboards
    - [ ]  Define success metrics
- [ ]  Data & Analytics
    - [ ]  Identify and document data sources
    - [ ]  Design data pipeline
    - [ ]  Implement data transformations
    - [ ]  Build dashboards
    - [ ]  Set up automated data refresh

---

# **Feedback**

[To be filled after initial review]

---

# **Learnings & Next steps**

[To be filled after implementation and initial usage]

---

# **Appendix**

## Technical specifications

### Data sources