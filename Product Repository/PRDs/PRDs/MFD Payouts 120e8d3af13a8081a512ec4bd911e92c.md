# MFD Payouts

: Naman Agarwal
Created time: October 15, 2024 5:26 PM
Status: In progress
Last edited: October 18, 2024 5:50 PM

# What is context of the problem?

MFDs are major business source for volt and there experience being excellent is a important for volt’s increased sales and AUM. Payouts are a major draw of MFD to the volt platform alongside redemption prevention. We want MFDs to have a great experience getting payouts. 

For Payouts we need 

1. Correct calculations
2. Scheduled payouts  
3. Payout Visibility 

# **What problem are we solving?**

Current challenges

- Programs line Self-line, has no indication to the payout team causing them to miss the cases.
- GST payouts and Editing of the Payout  reports are manual which will create issues for schedule of payout for reports with edits
- MFDs get the report alongside the payouts, they can not keep track of payout date, and resolution the query they have raised
- We don’t create different reports for MFDs with GSTN, requiring manual work for the GSTN MFDs

Notes 

- Incorrect communication is occasionally provided to MFDs regarding their payouts.
    - data on the top report was of august, total sept
- MFDs rely on Relationship Managers (RMs) to report issues, who then pass them on to Murthy for resolution.
    - Payout Maths
        - Selfline
    - Payout Schedule
    - Payout Visibility
    - 
        - MFD selfline- Payout
        - MFD
- The current issue resolution and reconciliation process is manual and inefficient.
- There is a risk of incorrect payouts being sent to MFDs, leading to a lack of control over the payout process.
- Payout delays and inaccuracies remain significant pain points for MFDs. find DATA
- MFDs have no visibility into when their payout will be processed (typically around the 10th of the month), and any issues further delay the process.
- MFDs raise payout-related concerns with RMs, which consumes RM bandwidth that could be better utilized for sales activities.
- Payouts may miss including "Selfline" loans, which are loans taken by the MFD’s own family members with Volt.
- The tech team uploads the payout file to the dashboard, but payouts are sent to MFDs without prior alignment on the payment amount.
- MFDs can download the payout reports from the portal, though many MFDs prefer not to have their employees access these reports.
- Payout issues also affect GST filings. MFDs often raise GST invoices based on the net amount instead of the gross amount. For payouts exceeding ₹15,000, a 5% TDS is applicable, reducing the net amount payable to MFDs.
- The accounts team handles the tax payments.
- The RM team’s bandwidth is consumed for nearly two days due to payout-related tasks.
- The goal is to ensure accurate payouts and proper communication.
- MFDs want to track their payouts with transaction-level details through the dashboard.
- GST calculations are done manually for each MFD, which increases the complexity of the process.
- last month ka payout was on the top
- 

---

# **How do we measure success?**

L1 - 

- number of Activations by MFDs

L2 

- MFD referred by MFDs
- Number of MFD onboarded

L3 

- Number of  Manual edits to Payout reports
- Queries regading MFD payouts

---

# **How are others solving this problem?**

---

# **What is the solution?**

- We will build a table with date and report for MFD on the MFD dashboard >earnings
- MFD will have new report every month, we will mention due date
- MFD can download the payout report in a access controlled way(Email to main Email)
- We will provide a Option to add the GSTN number to MFD (optional for MFDs) and we will process there full payout + GST together.
- MFD can accept or raise issues from the dashboard, Reducing the support bandwidth
- MFD can then see status of there issues on the same dashboard.
- MFD will get steps to receive payouts like adding bank account

Current payout journey 

- Invoice details
    - **Select PAN type**
        - Resident Individual (Self)
        - Resident Individual (Other)
        - Private Limited Company
        - Limited Liability Partnership
    - Enter the **PAN number**.
    - Optionally enter the GST number.
- **Enter Bank Details**:
    - Bank account number.
    - Re-enter bank account number.
    - IFSC (Indian Financial System Code).

PAN number should be linked with Bank account to have payout 

2 core problems :- Payout amount accuracy 

ad hoc transactions 

First we calculate the base payout amount 

then we calculate 

TDS logic >14250 

GST 

- how are AMC provide the payouts
- report status , payment status
- 48 hrs in receiving final confirmation from PG
- payments are in a Dumb DB
- payout structure for the MFDs partners

transactions need to accurate in DB 

Commercials need to be finalised 

two working days after that to complete the 

Transactions - 
- certain  , loans are misssed, 

transaction date are wrong 

- transaction are missed
- SOA amount

pos need to verify , change in pos = 
POS - principle outstanding 

There is no transaction sanity - we have set up a process 

separate bank account for MFD payouts 

- data discrepancies
- we step up  

process note , what is offline ,

base transaction * payout calc*

## Requirements overview (optional)

## User stories / User flow

## Requirements

---

# **Design**

---

# **Analytics**

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