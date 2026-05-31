# [Platform] BRE configurations for approval tasks

: Vaibhav Arora
Created time: December 13, 2024 9:15 AM
Status: Done
Last edited: January 9, 2025 10:54 PM

# **What problem are we solving?**

Requests raised by the users in relation to their loan account and application journey go through STP and non STP flow. Non STP transactions go through an approval mechanism on the command centre.

As we continue to launch the DSP platform across channels, we will require platform and request level checks and rule engines to control approval mechanisms and handle teething phases for launch across channels.

---

# **How do we measure success?**

This capability will help us do controlled launches across channels and partners to control risk while ensuring that scaled up platforms are not impacted with approval mechanisms. 

Larger themes of impact:

- Optimisation of operations bandwidth
- Percentage of requests approved automatically
- Controlled launches and accurate scale ups with partners/channels

---

# **How are others solving this problem?**

NA

---

# **What is the solution?**

Partner and channel level BRE configurations:
We will be building partner and channel level BRE capabilities to define STP and non STP rule engine which will govern the approval of a task.

<aside>
💡

For example: We may approve STP lodgements for Volt while keeping it an approval flow for a new partner like Groww or IndMoney

</aside>

Request level BRE configurations:

We will be building request level rules which will govern if the said request will be going through an STP flow or a non STP flow (checker approval).

Each rule can have a threshold value which can be different at a request/channel level.

<aside>
💡

For example: We have a rule to auto approve lodgement requests with a limit under 10 lakh for Volt and 2 lakhs for Groww

While the parameter here is credit limit, it can be the transaction amount for withdrawal, and repayment amount or date of transaction for repayments (amount and date will be two separate rules)

</aside>

The hierarchy between the two would be in the following order:

- Sourcing channel level checks - Sourcing ID
- Corresponding request level checks - Request type (Withdrawal / Repayment)

## User stories / User flow (core problems)

Our primary stakeholders here our the operations team as well as our partners (LSPs). 

Post introducing platform level and request level BREs, it will become complex for the operations team to gauge why a request has gone through a non STP flow. 

The same will be communicated to the LSP (So that they can manage the lifecycle of the request (and corresponding communication) to the user accordingly.)

**User flow diagram:**

![Screenshot 2025-01-09 at 7.58.21 PM.png](%5BPlatform%5D%20BRE%20configurations%20for%20approval%20tasks/Screenshot_2025-01-09_at_7.58.21_PM.png)

## Requirements

---

Refer the following table for the required configurations:

| **Module** | Sourcing channel | **Rule type** | Governing validation |
| --- | --- | --- | --- |
| Withdrawal | Volt | Withdrawal request beyond a certain amount will go through CC approval | 20,00,000 |
| Withdrawal | Volt | Withdrawal requests more than a certain times a day will go through CC approval | ≥3 |
| Repayment | Volt | Repayment request beyond a certain amount will go will go through CC approval | 10,00,000 |
| Repayment | Volt | Repayment requests more than a certain times a day will go through CC approval | ≥3 |
| Lodgement | Volt | Lodgement requests within a certain period of pledging will go through CC approval | Lodgement requests happening next day of pledging |
| Lodgement | Volt | Lodgement requests beyond a certain amount will go through CC approval | ≥10,00,000 |
| QC | Volt | Pending |  |
| Revocation | Volt | Global flag | All transactions are non STP |
| Closure | Volt | Global flag | All transactions are non STP |
| Mobile update | Volt | Global flag | All transactions are non STP |
| Email update | Volt | Global flag | All transactions are non STP |
| Withdrawal | Groww | Global flag | All transactions are non STP |
| Repayment | Groww | Global flag | All transactions are non STP |
| Lodgement | Groww | Global flag | All transactions are non STP |
| QC | Groww | Global flag | All transactions are non STP |
| Revocation | Groww | Global flag | All transactions are non STP |
| Closure | Groww | Global flag | All transactions are non STP |
| Mobile update | Groww | Global flag | All transactions are non STP |
| Email update | Groww | Global flag | All transactions are non STP |

We will have to start passing two additional values against requests to indicate to the LSPs that a particular request has gone through a non STP flow (as per the BRE) and a description as to why(Task description):

- STP flag
- Task description

Remarks:

| **Tasks** | **Non STP reason** | **Description V1** | **Sample** |
| --- | --- | --- | --- |
| Withdrawal maker description | Withdrawal amount>10,00,000 | Auto-approval withdrawal amount limit exceeded for loan account number: [Loan account number] | Auto-approval withdrawal amount limit exceeded for loan account number: FXLAN1234567 |
| Withdrawal maker description | First withdrawal | First withdrawal approval for loan account number: [Loan account number] | First withdrawal approval for loan account number: FXLAN2345678 |
| Withdrawal maker description | NBFC account limit (100 transactions or 5 Cr) | NBFC disbursement limit exceeded, withdrawal approval required for loan account number: [Loan account number] | NBFC disbursement limit exceeded, withdrawal approval required for loan account number: FXLAN3456789 |
| Withdrawal maker description | Requests raised via command centre | Maker initiated request, withdrawal approval required for loan account number: [Loan account number] | Maker initiated request, withdrawal approval required for loan account number: FXLAN4567890 |
| Withdrawal maker description | Feature flag | Auto-approval disabled, withdrawal approval required for loan account number: [Loan account number] | Auto-approval disabled, withdrawal approval required for loan account number: FXLAN5678901 |
| Repayment maker description | Requests raised via command centre | Maker initiated request, repayment approval required for loan account number: [Loan account number] | Maker initiated request, repayment approval required for loan account number: FXLAN6789012 |
| Sell-off repayment posting maker description | Requests raised via command centre | Repayment received against sale of security: [ISIN] approval required for loan account number: [Loan account number] | Repayment received against sale of security: IN1234567890 approval required for loan account number: FXLAN7890123 |
| Add collateral maker description | Requests raised via command centre | Maker intiated request, lodgement approval required for loan account number: [Loan account number] | Maker initiated request, lodgement approval required for loan account number: FXLAN8901234 |
| Add collateral maker description | Collateral value above 10 lakh | Collateral value above 10 lakh, lodgement approval required for loan account number: [Loan account number] | Collateral value above 10 lakh, lodgement approval required for loan account number: FXLAN9012345 |
| Add collateral maker description | Feature flag | Auto-approval disabled, lodgement approval required for loan account number: [Loan account number] | Auto-approval disabled, lodgement approval required for loan account number: FXLAN0123456 |
| Remove collateral maker description | Requests raised via command centre | Maker initiated request, approval required for removing collateral from loan: [Loan account number] | Maker initiated request, approval required for removing collateral from loan: FXLAN1234567 |
| Remove collateral maker description | Feature flag | Auto-approval disabled, approval required for removing collateral from loan: [Loan account number] | Auto-approval disabled, approval required for removing collateral from loan: FXLAN2345678 |
| Collateral sell-off maker description | Feature flag | Auto-approval disabled, approval required for sale of collateral from loan: [Loan account number] | Auto-approval disabled, approval required for sale of collateral from loan: FXLAN3456789 |
| Excess refund maker description | Feature flag | Auto-approval disabled, approval required for refund of excess from loan: [Loan account number] | Auto-approval disabled, approval required for refund of excess from loan: FXLAN4567890 |
| Mobile change maker description | Approval required for all mobile updates | Mobile number update approval required for loan: [Loan account number] | Mobile number update approval required for loan: FXLAN5678901 |
| Bank account change maker description | Approval required for all bank account updates | Bank account update approval required for loan: [Loan account number] | Bank account update approval required for loan: FXLAN6789012 |
| Emaill address change maker description | Approval required for all email address updates | Email address update approval required for loan: [Loan account number] |  |
| Charges waive off maker description | Approval required for all charge waivers | [Charge name] waiver approval required for loan: [Loan account number] | Processing Fee waiver approval required for loan: FXLAN7890123 |
| Mandate presentation maker description | Approval required for all mandate presentation | Mandate presentation approval required for month [Presentation month] [Presentation year] | Mandate presentation approval required for month Aug 2024 |
| Closure maker description | Feature flag | Auto-approve disabled, approval required for closure of loan: [Loan account number] | Auto-approve disabled, approval required for closure of loan: FXLAN8901234 |
| Closure maker description | Requests raised via command centre | Maker initiated request, approval required for closure of loan: [Loan account number] | Maker initiated request, approval required for closure of loan: FXLAN9012345 |
| Repayment reversal maker description | Approval required for all withdrawal reversals | Approval required for reversal of repayment from loan: [Loan account number] | Approval required for reversal of repayment from loan: FXLAN0123456 |
| Withdrawal reversal maker description | Approval required for all repayment reversals | Approval required for reversal of withdrawal from loan: [Loan account number] | Approval required for reversal of withdrawal from loan: FXLAN1234567 |
| Charge maker description | Requests raised via command centre | Approval required for posting [charge name] to loan: [Loan account number] | Approval required for posting Late Payment Fee to loan: FXLAN2345678 |
| Interest waiver maker description | Approval required for all interest refunds and waivers | Approval required for waiver of interest from loan: [Loan account number] | Approval required for waiver of interest from loan: FXLAN3456789 |
| Interest refund maker description | Approval required for all interest refunds and waivers | Approval required for refund of interest from loan: [Loan account number] | Approval required for refund of interest from loan: FXLAN4567890 |

# **Design**

NA

---

# **Analytics**

- Number of tasks approved per ops agent per day/ per week/ per month
- TAT to approve a task at a partner and at a request type level
- Approval rate of tasks at a request and partner level

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

---