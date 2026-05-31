# Term Loan: Disbursement

### First Drawdown

Based on the Submit opportunity status the subsequent flow will be decided:

**Submit Opportunity Failure:**

- Loan and Tranche Account won’t be created and LSP will have to re-trigger the request

**Submit Opportunity Success(Disbursal Success):**  

- Loan Account is created and Disbursement workflow is triggered.
- Once the Disbursement workflow is triggered we will block the DP of the user.
- The Disbursement/Payout request is then sent to our Payout partner.
- Our payout partner acknowledges the request and initiate the payout from their end.
- Once the amount gets debited from our bank account we get a debit success response.
- Post the debit from our Bank Account the amount will get credited to the customer’s bank account. This is when we get a credit success response.
- Once we receive a credit success response we will be posting the disbursal in the ledger and accordingly a Tranche account will be opened.
- Based on the disbursal amount, tenure and interest rate the repayment/EMI schedule gets generated.

**Submit Opportunity Success(Disbursal Failure):**

- Loan Account is created and Disbursement workflow is triggered.
- Once the Disbursement workflow is triggered we will block the DP of the user.
- The Disbursement/Payout request is then sent to our Payout partner.

There are multiple scenarios once the disbursal/payout request is triggered from our systems:

1. The request is not triggered resulting in an instant failure of the disbursement. In such a case we need to retry initiating the request until it gets triggered to the Payout partner.
2. The request is triggered from our system but due to the Payout partner system being down we get an error resulting in disbursement failure. In such a case we need to re-trigger the request at the same time we receive the error from our payout partner or we can wait for sometime before re-triggering the request. 
3. The request is received by the payout partner and the same is acknowledged through a response but the debit from our bank account does not happen and we get a debit failure response. In such a case we need to re-trigger the disbursal request(Depends on tech handling, if we are not able to handle this in V0 then we can mark the disbursal as failure and inform the LSP of the same for them to re-trigger the request and we unblock the customer’s DP).
4. The request is received by the payout partner and we get a debit success confirmation but we get a credit failure response. Then in such a case we need to mark the disbursement request as failed and accordingly inform the LSP for them to re-trigger the request. The Loan account is open in such a scenario but the Tranche account is not opened. The DP of the user gets unblocked.

### **Subsequent Drawdown**

- User can take a subsequent drawdown by either  pledging more collateral or via  AL replenishment through ongoing tranche closure. If only few EMIs are closed of the first Tranche then user won’t be able to take a subsequent drawdown.
- Each drawdown generates a new Tranche under the same Loan/Facility.
- Loan-level summary reflects cumulative outstanding and due status.
- The disbursement process/flow will be same as the First Drawdown flow.

### Processing Fee Handling

- Processing Fee will be at a Tranche level.
- Based on the Processing fee range that we will pass to the LSP they will return a certain value of processing fee which will lie in the above passed range. The value passed by the LSP will be validated at our end if it lies in the specified range. Based on the validation we will either proceed with the disbursement or fail the disbursement with the specific error.
- Once the disbursement is successful we will be passing to Finflux the loan amount, tenure and interest rate.
- The loan amount that will be booked will be Disbursement Amount + Processing Fee. This loan amount will be used to create the EMI schedule.
- The processing fee is booked at the time of disbursal.

## Repayment Schedule(RPS)

- EMI schedule = [Principal + Interest] amortized over the selected tenure.
- The EMI calculation will be done based on the PMT schedule
- When the disbursal date is not equal to the EMI due date then Broken Period Interest. We will be defining a Cut-off date for the Broken Period Interest calculation.
- The cut-off date for BPI is 20th of the month. This value should be configurable.
- EMI rounding rule: round off to nearest INR
- The interest calculations will be done based on: Actuals/365 method
- RPS can be exposed per-tranche or consolidated at loan level.
- Consolidated RPS follows FIFO order of loan creation.
- RPS calculation is provided in the below attached sheet

## Bill Date and Due Date Handling

### V0

- Bill date is the date when the billing happens for the amount to be paid by the customer on the due date. Here interest calculations happen from the Previous due date to (Current Due date-1).
- Due date is the date which the user selects on the LSP app and is the date when the Mandate will be presented. Post this date the amount/EMI to be paid becomes overdue(In case of no grace period). Due dates can be different for different users but one user will have a single due date for all their tranches.
- Currently for V0 the Bill Date and the Due Date will be the same.
- Based on user selection the Due Dates can vary between 2nd to 7th of the month. One user will have a single due date for all their tranches but different users can have different due dates. Cred is yet to to come back on fixing a single due date across users for V0 release.

### V1

- We should be able to configure different Bill Date and Due date into Finflux and the repayment schedule which will be generated will be based on the Due date and not the Bill Date.