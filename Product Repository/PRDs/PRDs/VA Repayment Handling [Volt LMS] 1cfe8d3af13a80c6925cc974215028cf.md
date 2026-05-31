# VA Repayment Handling [Volt LMS]

: Surya Ganesh
Created time: April 8, 2025 7:08 PM
Status: Not started
Last edited: April 10, 2025 10:50 AM

# **What problem are we solving?**

Currently, Volt cannot create the Virtual Account (VA) repayment requests, resulting in an inability to track and post repayments made through Virtual Accounts. This creates a gap between DSP Finance's successful repayment processing and Volt's internal payment posting system, leading to potential reconciliation issues and incomplete financial records.

---

# **How do we measure success?**

N/A

---

# **How are others solving this problem?**

N/A

---

# **What is the solution?**

We will implement a webhook integration system that receives repayment notifications from DSP Finance when a customer successfully makes a repayment via their Virtual Account. The system will map the FXLAN (Fenix Loan Account Number) provided in the webhook to our internal creditId, allowing us to properly post and track these repayments in our database.

## User stories / User flow

1. Customer makes a repayment through their Virtual Account
2. DSP Finance processes the repayment in their system
3. Upon successful processing, DSP Finance sends a webhook notification to Volt
4. Volt receives the webhook and validates the payload
5. Volt maps the external identifiers to internal records
6. Volt creates a completed collection request with the appropriate details
7. Repayment is recorded as "SETTLED" in Volt's database

## Requirements

The following is the sample webhook being sent by DSP team after the repayment is credited to the DSP’s collection account via the customer’s Virtual Account

```json
{
	"status": "SUCCESS",
	"subStatus": null,
	"eventDetails": {
		"amount": 5000,
		"status": "SUCCESS",
		"subStatus": null,
		"utrNumber": "UTR12345678997998",
		"makerNotes": null,
		"completedOn": 1737484352859,
		"requestedOn": null,
		"statusNotes": "Repayment request is successful",
		"payInOrderId": null,
		"repaymentMode": "VIRTUAL_ACCOUNT",
		"requestSource": "SYSTEM",
		"lmsTransactionId": "6aa42cf9-f3a0-419c-b460-0cc40699d5e3",
		"paymentTimestamp": 1737463908000,
		"collateralDetailId": null,
		"fenixLoanAccountId": "FXLAN38839493",
		"repaymentRequestId": "RPRID467516893247",
		"soaStatementRemark": "Repayment received for loan account number: FXLAN38839493 with Ref ID: UTR12345678997998",
		"accountingTimestamp": 1737463908000,
		"workflowExecutionId": "8a817b4c94835960019488eb4a7f0038",
		"paymentGatewayOrderId": null,
		"linkedRepaymentOrderId": "RPOID6tot77695341518",
		"paymentTypeForRepayment": "VA",
		"lmsReversalTransactionId": null,
		"repaymentAttributionType": null,
		"reversalAccountingTimestamp": null,
		"soaStatementRemarkIfReversed": null
	},
	"eventTimestamp": 1737484352863,
	"fenixRequestId": "RPRID467516893247",
	"fenixRequestType": "REPAYMENT_REQUEST_STATUS_UPDATE",
	"fenixLoanAccountId": "FXLAN38839493"
} 
```

The following fields will be mapped from the webhook payload to our internal collection request record:

| **Internal Volt Fields** | **Source from Webhook** | **Notes** |
| --- | --- | --- |
| creditId | Derived from fenixLoanAccountId ("FXLANXXXXXXX") | Use vdl_credits table to map FXLAN to internal creditId |
| collectionId | workflowExecutionId |  |
| collectionType | "Check SOA" | Default value for VA repayments |
| collectionStatus | "SETTLED" | Default value for VA repayments as they are already completed |
| totalAmountDue | nil | No total amount due is definable for VA payments |
| paymentDate | paymentTimestamp | Convert timestamp to appropriate date format |
| createdOn | nil | No creation timestamp is definable for VA payments |
| lastUpdatedOn | paymentTimestamp | Convert timestamp to appropriate date format |
| pgResponse | soaStatementRemark |  |
| lenderCollectionId | linkedRepaymentOrderId |  |
| minAmountDue | nil | No minimum amount is definable for VA payments |
| actualAmountCollected | amount |  |
| transactionId | utrNumber |  |
| paymentGateway | "Virtual Account" | Default value for VA repayments |
| requestedOn | nil | No requested timestamp is definable for VA payments |
| completedOn | paymentTimestamp | We receive the timestamp when the repayment was successful |

### Validation Requirements

1. Ensure mandatory fields are present in the webhook payload
2. Validate the status field is "SUCCESS" before processing
3. Verify the fenixLoanAccountId exists in our system
4. Validate amount is a positive number
5. Ensure timestamps are in valid format

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