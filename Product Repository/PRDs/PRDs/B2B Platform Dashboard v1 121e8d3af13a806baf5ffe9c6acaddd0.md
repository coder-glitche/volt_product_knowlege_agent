# B2B Platform Dashboard v1

: Gautam Mahesh
Created time: October 16, 2024 1:23 PM
Status: Pending Review
Last edited: January 29, 2025 10:56 AM
Owner: Gautam Mahesh

# **Objective**

The platform dashboard aims to provide B2B partners with a centralised, self-service tool to monitor the performance of the Loan Against Mutual Fund (LAMF) product, manage customer and application data, track support tickets, and generate reports. This dashboard will enhance operational efficiency, improve partner satisfaction, and reduce manual interventions.

# **What problem are we solving?**

There are around 8 B2B platforms (partners) giving business to Volt. As of now, all of them are being serviced offline by the program team (Keyur) like giving visibility of applications, reports, etc. This results in the below challenges.

- Poor perception of Volt by the partner
- Risk of data being shared outside the required accesses
- Possible chance of incorrect data being shared
- Considerable man-hours spent in generating and managing reports
- Partners’ operations/business teams can’t self-service themselves
- Enterprise partners like TDL expect a complete dashboard for tracking

The above challenges arise from multiple reasons.

- Not all partners subscribe to all our webhooks
- Analytics is involved in generating reports for each partner
- All reporting is on Google sheets resulting in errors, etc

---

[White Labeled Partner portal for the MFDs](White%20Labeled%20Partner%20portal%20for%20the%20MFDs%20162e8d3af13a80feb7cae7bb59cb4662.md) 

# **How do we measure success?**

Below are the metrics we would measure.

- Number of applications processed.
- Applications per B2B partner.
- Percentage of completed applications.
- Reduction in man-hours due to self-service capabilities.
- Partner satisfaction score.

---

# **How are others solving this problem?**

Most lenders have a partner portal that provides the partner with detailed capabilities like-

- Application view
- Application completion
- Servicing capabilities
- Portfolio Value
- Report Download
- Commissions accrued
- Payouts
- Partner servicing (raising tickets, Whatsapp chat, etc)

---

# **What is the solution?**

## Requirements overview

The platform dashboard will be a self-service portal enabling partners to manage leads, track customer applications, monitor transactions, and generate reports, all while maintaining robust security via role-based access.

### **Key Features:**

- **Homepage**: Overview of partner performance with Volt.
- **Ongoing Applications**: View and track active applications and their stages.
- **Completed Applications**: Monitor completed applications and repayment statuses.
- **Lead Management**: Track and manage leads with filtering and export options.
- **Support Ticket Management**: Integrated Zendesk view for tickets raised by customers(not in current scope)
- **Transaction Management**: Monitor foreclosure, lien removal, disbursal, and repayment requests.
- **Reports & Analytics**: Generate reports with filters and export options.
- **Role-Based Access Control (RBAC)**: Secure, role-based access for different user types.(not in current scope)

## User stories / User flow

1. The partner is onboarded into Volt's platform, and users are created against email IDs.
2. The partner user logs into the dashboard using email and password.
3. The user lands on the **Homepage**, which displays:
    - Portfolio overview.
    - Key metrics.
4. The user can navigate to:
    - Ongoing Applications to track current applications.
    - Completed Applications to view settled loans and repayments.
    - Leads Management to filter and manage leads.
    - Support Tickets to view and resolve customer issues.(not in current scope)
    - Reports & Analytics to generate and export reports.

---

## Requirements

### Login Page

1. Partner should be able to login to Platform Dashboard.
2. Volt to create the login credentials & share it with partners.
3. For one partner, login credentials will be created for 2 users.
4. Once partner logs in, partner specific data to be populated.
    1. Eg- For Phonepe, only Phonepe data to be shown. One to one mapping.

## **Homepage**

### Capabilities

1. Business Metrics (Top Section):
    - Total disbursed loan value.
    - Total disbursed loans count.
    - AUM of loans.
2. User Cohort Metrics (Middle Section 1):
    - Total sanctioned loans value.
    - Total sanctioned loans count.
    - CTA: Redirects to the Ongoing Applications page.
3. Product Conversion Metrics (Middle Section 2):
    - Total customers with due principal.
    - Total customers with due interest.
    - CTA: Redirects to the Completed Applications page.
4. Filters for Metrics View: Daily, weekly, monthly, yearly, and till-date.
5. Visual Representations:
    - Total leads vs eligible leads (% eligible).
    - Lead conversion % (completed loans / total eligible leads).
    - Average eligible loan amount.

## Applicant Details

1. Ability to search the user based on Volt Customer Code & Phone number.
2. Datas to be fetched & have it in separate sheets in same screen:
    1. Application Details —> phonepe(minimum details)
    2. Loan Details —> phonepe(minimum details)
    3. Pledged details
    4. Disbursement Details
    5. Repayment Details 
    6. Interest Details
3. Entire history of the user will be fetched. 

## Ongoing Applications

### **Banner**

- **Metrics**:
    - Total sanctioned loan value.
    - Total sanctioned loans count.

### **Application Table**

1. **Fields**:
    - Partner account ID (external ID passed by the partner).
    - Volt application ID.
    - Customer name.
    - ~~Customer mobile number.~~
    - Available credit limit (not sanctioned credit limit).
    - Status (include detailed statuses: Portfolio fetch pending, Offer confirmation pending, KYC pending, Bank mandate pending, Pledging pending, Agreement signing pending).
    - Lead created timestamp.
    - Lead updated timestamp. etc.
2. **Search Options**: Partner can filter the data or search for specific user.
3. **Filter Options**: Partner should be able to filter any column.
4. **Download Reports**:
    - Filter-based downloads (CSV/XLSX).
5. **Pagination**: Default 20 records per page.

## Completed Applications

### **Hero Banner**

- **Metrics**:
    - Total disbursed loan value.
    - Total disbursed loans count.
    - Total active loans.
    - Total loans with due payments.

### **Application Table**

1. **Fields**:
    - Partner application ID.
    - Volt application ID (Opportunity ID).
    - Loan account number.
    - Customer name.
    - Customer mobile number.
    - Sanctioned credit limit.
    - Utilized credit limit.
    - Available credit limit.
    - Outstanding amount (principal only).
    - Loan created timestamp.
    - Maturity date.
2. **Sub Tabs**:
    - All Customers.
    - Interest Due.
    - Shortfall.
    - Renewal.
    - Foreclosed.
    - Inactive.
3. **Search Options**: Partner can filter the data or search for specific user.
4. **Filter Options**: Partner should be able to filter any column.
5. **Download Reports**:
    - Filter-based downloads (CSV/XLSX).
6. **Pagination**: Default 20 records per page.

### Disbursement Details

1. **Fields:**
    1. Withdrawal request timestamp
    2. Withdrawal status
    3. Withdrawal amount
    4. Withdrawal settled timestamp
    5. ~~Transaction UTR number.~~ —> Need to discuss(also don’t have this info)
    6. Withdrawal ETA 
2. **Search Options**: Partner can filter the data or search for specific user.
3. **Filter Options**: Partner should be able to filter any column.
4. **Download Reports**:
    - Filter-based downloads (CSV/XLSX).
5. **Pagination**: Default 20 records per page.

### Repayment Details

1. Fields: 
    1. Repayment amount
    2. Repayment success timestamp
    3. Repayment status
    4. ~~Transaction UTR~~
    5. Repayment type (Principal repayment, Interest repayment, Both Principal +Interest repayment)
2. **Search Options**: Partner can filter the data or search for specific user.
3. **Filter Options**: Partner should be able to filter any column.
4. **Download Reports**:
    - Filter-based downloads (CSV/XLSX).
5. **Pagination**: Default 20 records per page.

### Pledged Details

1. **Fields:**
    1. Pledged portfolio value
    2. Pledge success timestamp
    3. Credit limit
    4. List of pledged mutual funds along with below details
    - ISIN number
    - Pledged MF units
    - Pledged MF value
    - Credit limit
    - Asset Repository (CAMS / Karvy)
2. **Search Options**: Partner can filter the data or search for specific user.
3. **Filter Options**: Partner should be able to filter any column.
4. **Download Reports**:
    - Filter-based downloads (CSV/XLSX).
5. **Pagination**: Default 20 records per page.

---

# **Roadmap**

- Trendline metrics: M-o-M, W-o-W.
- Initiate customer actions: SOA, holding statements.
- Funnel metrics & error insights.
- Raise & track support tickets.
- Role-based access.
- Partner earnings & payouts view.
- Reports: Loan trends, lead conversion analysis.
- CRM integration for streamlined support.

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes