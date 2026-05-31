# Design process + requirements

: Vinit Pramod Sarode
Created time: December 5, 2024 10:51 AM
Status: Not started
Last edited: December 17, 2024 7:00 PM

# Why

- Enable leveraging design for problem solving during PRD discovery state.
- Avoid using up design bandwidth on unclear requirements only to have to redo designs or get deprioritised
    - Streamline design process: set expectations for requirements.
    - To provide clear, documented requirements (stakeholders aligned) before design starts work.
- Design bandwidth getting used up in ad-hoc tasks without clear understanding of the problem statement.
    - Can’t allocate time to work on planned design projects.

# How

### 10-50-90 feedback process 💡

The 10-50-90 feedback process creates structured checkpoints for feedback that align with different stages of design maturity, helping prevent costly late-stage revisions.

- **10%** - Reviewing initial concepts and direction
    
    To ensure we’re solving the right problem and heading in a promising direction before investing too much time
    
- **50%**
    
    Core design elements are taking shape but there's still flexibility to make meaningful changes.
    
- **90%**
    
    The design is nearly finished. This final review focuses on refinements and polish rather than major changes. It's about catching small issues and ensuring everything meets quality standards before finalising the design.
    

### Why?

- Sets clear expectations on what kind of feedback is valuable at each stage
- Reduces wasted effort by catching misalignments early.

[How To Use the "10/50/99" Approach to Give Feedback | HackerNoon](https://hackernoon.com/how-to-use-the-105099-approach-to-give-feedback-1y8433l0)

# Design process for major projects

| Stage | Steps | Notes |
| --- | --- | --- |
|  | Review problem statement | In this stage Product <> Design will:
-  Understand problem statement : Get a detailed understanding on scope, expectations, ETA

- Supporting data: Who are we building for, what do they need to do, why this problem statement
- Impact : How many users are facing this problem

- Data points : Information required to be displayed or used in screens, PDFs, or any other mediums we are designing for |
|  | Make user flow | What all tasks need to accomplished by the user |
|  | Make wireframes | Identify all edge cases, drop-off flows, error states, happy flows |
|  |  |  |
| 10% | Walkthrough PRD + approach | Tech + product + design alignment on screen/flow
- Aligned on routes, data availability, limitations

Clear alignment necessary to avoid having to rework high fidelity UI  |
|  | Work on feedback |  |
|  | Work on high fidelity UI |  |
| 50% | Review UI with product + tech | - Review components, UI feedback
- Copy ideation |
|  | Work on feedback |  |
|  |  |  |
| 90% | Final copies, icons, illustrations |  |
|  | Hand-off ready file | Review design hand-off checklist |

### ⚠️ Important note:

- Avoid same day / next day requirements unless absolutely necessary.
- Always keep documented requirements and keep them updated as they get modified
    - Helps in easier KT to other designers incase of bandwidth crunch.

---

**Example for Major Project**

**Problem Statement**

As an NBFC, Volt must send CKYC (Central KYC) reports to the central repository to comply with regulatory requirements. To ensure accuracy, checkers need a structured process to verify data before approving and sending batch email reports. The current manual workflow is inefficient and prone to errors, requiring a streamlined solution for batch approval and compliance.

**Impact of the Problem**

- Achieve 100% compliance with CKYC submission deadlines.
- Ensure zero errors in approved batches sent to the central repository.

**Data Points**

**Must-Haves:**

- **Batch Information**:
    - Batch ID: Example: *BATCH00123*.
    - Total Records: Example: *100*.
    - Status: Example: *“Pending Approval” or “Approved”*.
- **Record Details for Each Entry**:
    - Customer Name: Example: *Ravi Mehta*.
    - CKYC Number: Example: *CKYC200123456*.
    - Maker and Checker Status: Example: *Maker: Verified, Checker: Approved*.
- **Email Details**:
    - Email Template with Batch Summary.
    - Recipients: Central Repository Email Address (e.g., *ckyc@centralrepo.gov*).

**Good-to-Haves:**

- Automated Notifications for Pending Batch Reviews.
- Filters for Prioritizing Batches by Submission Deadline.

| Data point | Value | Priority | Use-case |
| --- | --- | --- | --- |
| Total commission | 8000 | P0 | This info needs to be highlighted so the user feels good seeing the total amount |
| Active customers | #number 4 | P0 |  |
| Commission table  |  |  |  |
| Period | Sep (month) | P1 | To help users see a monthly summary, MFDs use this data to compare their monthly earnings. |

**Tasks users need to be able to do**

1. **Checker**:
    - Review the batch, approve/reject individual records, and add comments if needed.
    - Approve the email report for submission to the central repository.

**Example for Minor Project

Problem Statement**

MFDs of Volt currently lack a clear way to track their monthly earnings from the platform. Current format is hard to read and understand. We need to build a feature that generates monthly earning statements, summarising earnings and key details in an easily understandable format.

**Data Points**

- **User Information**:
    - Name: Example: *Sunita Ramesh*.
    - User ID: Example: *USR1023*.
- **Earnings Summary**:
    - Total Earnings for the Month: Example: *₹15,000*.
    - Date Range: Example: *1st to 31st December 2024*.
- **Breakdown of Earnings**:
    - Sources of Earnings: Example: *Interest Benefits, Cashback, Referrals*.
    - Amount per Source: Example: *₹10,000 (Interest), ₹3,000 (Cashback), ₹2,000 (Referrals)*.
- **Payment Details**:
    - Total Payouts: Example: *₹12,000 (Paid on 5th December 2024)*.
    - Pending Amount: Example: *₹3,000*
    

**Logical Arrangement:**

1. **Header**: User name, ID, and date range.
2. **Earnings Summary**: Total earnings and payouts.
3. **Detailed Breakdown**: Earnings by source, payment details, and pending amounts.