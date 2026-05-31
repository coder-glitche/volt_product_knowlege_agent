# Term Loan: Unpledging

**Pre Loan A/C creation:**

1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 
2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. 

Customer won’t bear any charge(In V0) for getting their collaterals unpledged. 

In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans.

 

**Post Loan A/C creation:**

- Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure.
- If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically.
- If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise:

1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 

2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2.

3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below.

- Partial Unpledging: Customers can only initiate partial unpledging of the collaterals through the LSP app in case they have repaid some EMIs of Tranche/s or foreclosed Tranche/s. The logic based on which we will allow partial unpledging of funds is:
- Minimum DP to be maintained post unpledging = Total Amount Payable across all Tranches and the Loan
- Here Total Amount Payable includes all the overdue, due and scheduled principals, overdue, due and scheduled interests and charges 
- Based on the above logic, the customer should be able to raise request for unpledging of collaterals worth an LTV value of: (Current DP - Minimum DP Post Unpledging)
- User can raise multiple partial unpledge requests given the above condition is satisfied. If an unpledge request is already in progress then the second request will fail.

Once the customer raises the partial unpledging request/s from the LSP app to DSP it will either go through the STP or nSTP flow, described below.

- Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2.

- The STP or non STP checks and processes in case of Term Loans will remain the same as that of OD product. The checks are as follows:
- Any unpledge request of Collateral Value more than 20 Lacs will go through the non-STP process otherwise it will go through the STP process.
- In case a customer raises more than 2 unpledge requests in a single day it will be routed to the non-STP flow otherwise it will go through the STP process.
- In case of STP process the collaterals for which unpledging request was raised they get automatically unpledged through the system. In case of any issue the unpledging request gets rejected.
- In case of non-STP process the Ops team has to approve the request for the unpledging and once approved the collaterals gets automatically unpledged through the system. In case of non approval the unpledging request gets rejected.