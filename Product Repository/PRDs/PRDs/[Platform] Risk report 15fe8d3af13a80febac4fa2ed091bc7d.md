# [Platform] Risk report

: Vaibhav Arora
Created time: December 17, 2024 7:56 AM
Status: Done
Last edited: December 20, 2024 2:26 PM

# **What problem are we solving?**

As an NBFC it is important to keep a keen eye on potential risk to the organisations, these risks can be in terms of:

- Financial risk (overdue customers)
- Operational risk (Customers without active mandate set ups)
- Compliance / Regulatory risk (Customers with high AML risk / Bureau risk / Expiring KYC)

We need to solve for visibility of the same so that the risk operations team can actively track and monitor potential risk to the organisation and accordingly take necessary measures.

---

# **How do we measure success?**

Particular problem is subjective in nature, however is of core importance to the organisation.

---

# **How are others solving this problem?**

Most organisations have reports and alerts sent to the team at regular cadence to identify, monitor, and mitigate potential risks to the organisation.

---

# **What is the solution?**

We will be building a risk report, which will be scheduled to the risk operations team at a regular cadence. 

The operations team will also be able to generate this report via the command centre and download it for internal tracking. This report will be access controlled and will only be able to be tracked by the risk team.

Correspondingly we will be introducing a new role, “Risk operations” which will have access to a basic approval access and additionally will have access to the risk report within the report section.

## Requirements

Report format:

| **Section** | **Parameter** | **Description** | **Value** |  |
| --- | --- | --- | --- | --- |
| Loan details | Name - Full name of the customer as per PAN | Name of the customer as per PAN | Name as per PAN | Available |
| Loan details | Name - Full name of the customer as per OVD | Name of the customer as per OVD | Name as per Aadhaar | Not available (Will have to get from LOS) |
| Loan details | Customer ID - FX client external reference ID | External reference ID for customer | FXCID | Available |
| Loan details | LAN - FXLAN account external reference ID | External reference ID for the loan | FXLAN | Available |
| Loan details | Product Type - LAS | Product type for the particular loan | Loan against securities | Available |
| Loan details | Max credit limit (Sanction limit) | Sanctioned limit given to the user at the time of doing the application | Sanctioned limit | Available |
| Loan details | Loan start date | Loan start date | Loan start date | Available |
| Loan details | Loan maturity date | Loan maturity date | Loan maturity date | Available |
| Loan details | Loan Status | Loan Status | Active / Closed / Frozen | Available |
| Exposure details | Pledged Collateral (Amount) | Total amount of collateral pledged against the loan | Value of the total pledged collateral (this is not DP) but value of the total collateral that is pledged against the loan. Sum(NAV*All pledged units) | Not available |
| Exposure details | Blocked Collateral (Amount) | Total amount of pledged collateral blocked in the loan | Sum(NAV*All blocked units) | Not available |
| Exposure details | Drawing Power | Drawing Power | Drawing Power | Available |
| Exposure details | Principal Outstanding | Principal Outstanding | Principal Outstanding | Available |
| Exposure details | Accrued interest | Accrued interest | Accrued interest | Available |
| Exposure details | Interest Due | Interest Due | Interest outstanding | Available |
| Exposure details | Service Charges Due | Service Charges Due | Service Charges Due (Charges due for the customer excluding penal charges) | Available |
| Exposure details | Penal Charges Due | Penal Charges Due | Penal charges due for the customer | Available |
| Exposure details | Next Due Date | Next due date for the customer (7th of next month) | Next due date for the customer (7th of next month) | Not available |
| Exposure details | Principal Overdue | Principal Overdue | Principal Overdue | Integration pending |
| Exposure details | Interest Overdue | Interest Overdue | Interest Overdue | Integration pending |
| Exposure details | Service Charges Overdue | Service Charges Overdue | Service Charges Overdue | Integration pending |
| Exposure details | Penal Charges Overdue | Penal Charges Overdue | Penal Charges Overdue | Integration pending |
| Exposure details | Overall DPD | Overall DPD | Days past due for the customer | Integration pending |
| Exposure details | Shortfall Amount | Shortfall Amount | Shortfall Amount | Available |
| Exposure details | Shortfall Aging | Shortfall Aging | Shortfall Aging | Available |
| Exposure details | Sell-off status | Flag that indicates if there is a pending but not terminal sell off request active for the customer | If a request exists, which has not failed or completed send "Pending" else "NA" | Available |
| Mandate Details: | Mandate Presentation Status | Flag that indicates if there is a pending but not terminal mandate collection request active for the customer | If a request exists, which has not failed or completed send "Pending" else "NA" | Available |
| Mandate Details: | Registration Status | Mandate status | Status of the mandate registered in the loan account Active/Inactive | Available |
| Mandate Details: | UMRN | Unique mandate reference number | Unique mandate reference number stored at the time of loan application | Available |
| Mandate Details: | Mandate start date | Mandate registration start date | Mandate registration start date | Available |
| Mandate Details: | Mandate end date | Mandate registration end date | Mandate registration end date | Available |
| Mandate Details: | Mandate max amount | Mandate max amount | Mandate max amount | Available |
| Mandate Details: | Mandate frequency | Mandate frequency | Mandate frequency | Available |
| Mandate Details: | Last presentation status / bounce reason (for current mandate) | Presentation status of the last mandate collection attempt on the user's loan account | Get the latest mandate collection request and share the status for the sameShould be a terminal status Completed/Failed | To be checked |
| Risk classification (Optional): | KYC risk classification | KYC risk classification stored at the time of loan creation | KYC risk classification stored at the time of loan creation | Available |
| Risk classification (Optional): | KYC date | Date when KYC was done for the customer | Date when KYC was done for the customer | Available |
| Risk classification (Optional): | KYC expiry date | Date when KYC will get expired for the customer (dependent on risk status of KYC) | Currently this is stored as a date, 2 years after KYC for the user | Available |
| Risk classification (Optional): | AML risk classification | AML risk classification stored at the time of loan creation | AML risk classification stored at the time of loan creation | Available |
| Risk classification (Optional): | AML pull date | Date when AML was pulled for the user | Stored in Finflux | Available |
| Risk classification (Optional): | AML provider | Provider used to pull AML details for the customer | Trackwizz | Available |
| Risk classification (Optional): | Credit risk classification | Credit risk classification stored at the time of loan creation | Credit risk classification stored at the time of loan creation | Available |
| Risk classification (Optional): | Bureau pull date | Date when Bureau details was pulled for the user | Date when Bureau details was pulled for the user | Available |
| Risk classification (Optional): | Bureau provider | Provider used to pull bureau details for the customer | Transunion | Available |
|  |  |  |  |  |

Operations team should be able to download and access this report as and when required via the command centre. z

The nature of the report is complete, that is it gives status for all loans. In future we may have to limit this to only active and frozen loans.

**Automated reports:**

Risk operations team will get this report daily, in the morning automatically at 10 AM to the following email addresses.

- shreyas.hebbar@dspfin.com
- admin@dspfin.com

---

# **Design**

Reports section in the command center: (@Karuna Sankolli)

- Should have capabilities to have multiple reports (and classifications within which there can be multiple reports)
- Should be access controlled
- User should be able to open section only if they have access, otherwise they should see an error message
- User
    - Generate report only by certain IDs
    - Download the report
    - Entry point to get the report
    - External and Internal reporting
    - Enable access to different types of reports
    - SQL Queries : Preset tables : Overall Loan view :  Internal data reporting and tracking
    - Data centre

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