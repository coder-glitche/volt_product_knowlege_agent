# [Platform] Mandate collection BRE optimisation

: Vaibhav Arora
Created time: January 16, 2025 6:29 AM
Status: Done
Last edited: January 30, 2025 5:01 PM

# **What problem are we solving?**

There are multiple ways through which an NBFC can collect dues from customers:

- Accepting direct user initiated payments (VA/PG)
- Collecting payments via debiting user’s bank accounts (mandate)
- Invoking securities to clear dues (Sell off)

All repayment methods have different use cases and scenarios in which they are triggered. Mandate collection repayments are done for the following use case:

- User convenience and financial health: Amount is automatically deducted from the user’s bank account and ensures that their loan account does not become overdue
- NBFC portfolio health: It is important that NBFC has a good collection rate on its products and little to no NPA

To be able to make mandate collections we have currently implemented a job that runs after the billing cycle, identifies the interest due + charges due for a loan account and creates an approval file which can then be approved or rejected by the operations team via the command centre.

However there are certain gaps in the job which needs to be fixed:

1. Accounts which are opened after the billing cycle but still have charges outstanding (primarily due to account opening charges) are also included in the BRE. 
2. Accounts which have multiple charges posted (Even charges which were posted after the billing cycle are included in the BRE)

This introduces significant issues both for the user, as well as for the NBFC.

1. Charges which should not be collected from the mandate cycle are being collected, against which a higher balance will have to be maintained by the user, increasing the potential of the mandate failing and users getting a overdue charge applied on their loan account
2. If users are charged unfairly, they may reach out to regulatory authorities complaining about unethical collection practices by the NBFC causing both reputational and financial risk to the organisation
3. Users may foreclose loan, ruining customer experience and retention for DSP Finance/Volt.

---

# **How do we measure success?**

- Validity of mandate collection file raised to operations (Number of regenerations of mandate presentation file month on month) - For reasons associated with inaccurate due generation
- # of user tickets on confusion of the amount deducted from their bank account via mandate collections
- Number of bounce transactions due to insufficient balance in user’s accounts

---

# **How are others solving this problem?**

NBFCs usually maintain a different due date at a particular level (interest due/charge due/interest overdue) to ensure only due collections are collected via mandate from the user. 

NBFCs also collect charges upfront from the user in a few onboarding flows, or from the 1st EMI (for term loans) or the subsequent disbursement (knock off).

---

# **What is the solution?**

- We will be integrating with the Finflux (LMS) overdue API which gives us due level information:
    - Due type (Interest / Charge / Penal charge / Interest overdue)
    - Due amount
    - Due from
    - Due date
- Based on this information we will run a BRE to select which dues are eligible for collection via mandate from the user:
    - Any due where due date is below the last day of the billing cycle is of the type (interest + charges + penal charges) is eligible for collection.
- We will rename the bounce charges to make them dishounour charges to make it explicit for the user that since their account is in an overdue state, they are being charged an overdue fee.

Charge short name: DC (Deployed in UAT)
- Users will only be charged an dishounour charges if there was an interest outstanding, and the same was failed to collect based on a set of specific error codes from the mandate presentation
- To ensure operations team and LSPs are able to approve and track this effectively, we will be enhancing our collection request details to contain particular level information across communication methods:
    - Approval task for ops to approve - P0
    - Mandate collection webhook to LSP - P1 (Statement generation + When ops generates the mandate collection)
    - Mandate collection details section on CC - P1

Error codes:

| Error message | Description |
| --- | --- |
| Bank account closed | Bank account of the user is closed or inactive |
| Insufficient balance | Bank account does not have insufficient balance for the mandate presentation to happen |
| A/c Blocked or Frozen | Bank account of the user is either blocked or frozen by their bank  |
| Payment Stopped by Drawer | User blocked the mandate collection |
| Returned as per customer request | User asked to return the mandate collection |
| KYC Documents Pending | User’s KYC for their bank account is incomplete |
| Documents Pending for Account Holder turning Major | User’s KYC for their bank account is incomplete |
| Account inoperative | User’s bank account is inoperative |
| Dormant account | User’s bank account is in a dormant state due to non usage |
| A/c in Zero Balance/No Transactions have Happened, First Transaction in Cash or Self Cheque | User’s bank account is in a zero balance state |
| Small account, First Transaction to be from Base Branch | User has not had any transaction in their bank account |
| Amount Exceeds limit set on Account by Bank for Debit per Transaction | Mandate collection amount breaches the limit set by the user/bank of the user’s bank account |
| Account reached maximum Debit limit set on account by Bank | Mandate collection amount breaches the limit set by the user/bank of the user’s bank account |
| Customer Insolvent / Insane | Customer’s bank account is in an insolvent state |
| Customer to refer to the branch | Some issue with the bank account of the user |
| Transaction has been cancelled by user | Mandate collection was cancelled by the user |
| Invalid Aadhaar Format | User’s KYC is invalid |
| Inactive Aadhaar | User’s KYC is invalid |
| Aadhaar mapping does not exist/Aadhaar number not mapped to IIN | User’s KYC is invalid |

## Requirements overview (optional)

## User stories / User flow

## Requirements

We will be integrating with the Finflux Overdue API which will give us particular level information to handle the aforementioned BRE for mandate collection;

```json
Sample response:
{
	"fenixLoanAccountId": "FXLAN63928439",
	"totalOverdueAmount": 3132.6,
	"totalChargesDue": 2947.64,
	"totalPenalChargeDue": 70,
	"totalPrincipalDue": 0,
	"totalInterestDue": 114.96,
	"overdueDetails": [
		{
			"dueOn": 1734978599999,
			"startingOn": 1734892200000,
			"endingOn": 1734978599999,
			"principal": 0,
			"interest": 0,
			"charge": 1178.82,
			"penalCharge": 0,
			"chargeIdentifier": "PROCESSING_FEES"
		},
		{
			"dueOn": 1736274599999,
			"startingOn": 1734945729554,
			"endingOn": 1735669799999,
			"principal": 0,
			"interest": 0,
			"charge": 1178.82,
			"penalCharge": 0,
			"chargeIdentifier": "PROCESSING_FEES"
		},
		{
			"dueOn": 1736274599999,
			"startingOn": 1736188200000,
			"endingOn": 1736274599999,
			"principal": 0,
			"interest": 0,
			"charge": 590,
			"penalCharge": 0,
			"chargeIdentifier": "BOUNCE_CHARGES"
		},
		{
			"dueOn": 1736447399999,
			"startingOn": 1736361000000,
			"endingOn": 1736447399999,
			"principal": 0,
			"interest": 0,
			"charge": 0,
			"penalCharge": 20,
			"chargeIdentifier": "PENAL_OVERDUE_CHARGES"
		},
		{
			"dueOn": 1736533799999,
			"startingOn": 1736447400000,
			"endingOn": 1736533799999,
			"principal": 0,
			"interest": 0,
			"charge": 0,
			"penalCharge": 10,
			"chargeIdentifier": "PENAL_OVERDUE_CHARGES"
		},
		{
			"dueOn": 1736620199999,
			"startingOn": 1736533800000,
			"endingOn": 1736620199999,
			"principal": 0,
			"interest": 0,
			"charge": 0,
			"penalCharge": 10,
			"chargeIdentifier": "PENAL_OVERDUE_CHARGES"
		},
		{
			"dueOn": 1736706599999,
			"startingOn": 1736620200000,
			"endingOn": 1736706599999,
			"principal": 0,
			"interest": 0,
			"charge": 0,
			"penalCharge": 10,
			"chargeIdentifier": "PENAL_OVERDUE_CHARGES"
		},
		{
			"dueOn": 1736792999999,
			"startingOn": 1736706600000,
			"endingOn": 1736792999999,
			"principal": 0,
			"interest": 0,
			"charge": 0,
			"penalCharge": 10,
			"chargeIdentifier": "PENAL_OVERDUE_CHARGES"
		},
		{
			"dueOn": 1736879399999,
			"startingOn": 1736793000000,
			"endingOn": 1736879399999,
			"principal": 0,
			"interest": 0,
			"charge": 0,
			"penalCharge": 10,
			"chargeIdentifier": "PENAL_OVERDUE_CHARGES"
		}
	]
}
```

Instead of loan summary, Dues API will be called via the CRON job to create the collection request, the collection request should also store particular level data, which will then be propagated to the operations team / LSP

<aside>
💡

Our present logics of skipping (due to unavailability of an active mandate and waive off will still work at an batch item level)

</aside>

We will be calling this mandateCollectionBatchItemParticular, following will be the type of particulars:

- Penal charge (Charges posted within or before the billing cycle)
    - Charge (Charges posted within or before the billing cycle)
- Interest due (Interest posted within for the current billing cycle)
- Interest overdue (interest posted for the previous billing cycle(s))

Updated approval batch file at a particular level:

[https://docs.google.com/spreadsheets/d/1mk0UUn2fySN99kcZeK5t5Sk3akJsYjZ413I2B99_0f0/edit?gid=1086316367#gid=1086316367](https://docs.google.com/spreadsheets/d/1mk0UUn2fySN99kcZeK5t5Sk3akJsYjZ413I2B99_0f0/edit?gid=1086316367#gid=1086316367)

The same will be propagated to the LSP via collection request:

```json
Sample JSON for collection webhook:

  "event_type": "MANDATE_COLLECTION",
  "data": {
    "loan_account_id": "FXLAN63928439",
    "collection_details": {
      "total_collection_amount": 3132.60,
      "collection_date": "2025-01-07",
       "billing_cycle_start_date": "2025-01-01",
       "billing_cycle_end_date": "2025-01-31",
      "breakdown": {
        "interest_due": 114.96,
        "charges": {
          "processing_fees": 2357.64,
          "bounce_charges": 590.00
        },
        "penal_charges": 70.00
      }
    }
  }
}
```

---

# **Design**

@Karuna Sankolli (Can we come up with Command centre designs to show to the ops agent)

- Mandate collections section in the loan details page (Solve for discovery)
- Mandate collections details screen (to show granular information)

---

# **Analytics**

- #  of regenerations of mandate collection file at a billing cycle level
- # number of mandate overdue charges posted for users due to the aforementioned reasons

---

# **Timeline/Release Planning**

It is important to solve this before the next billing cycle arrives for our customers, we are tracking to solve this in the first week of the next sprint cycle - 20th Jan and implement before the 6th of February 2025)

Will add detailed ETA 

---

# **Go to market**

- Business alignment - 18th Jan
- Tech estimation - 20th Jan
- High level release timeline - 27th Jan
- Operations training - 3th Feb
- First attempt - 6th Feb

## Marketing

NA

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