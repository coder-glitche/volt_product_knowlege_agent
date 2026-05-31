# Term Loan: Unpledge Eligibility API(Post loan creation)

# **What problem are we solving?**

Currently, LSPs do not have visibility into how much of a customer’s pledged portfolio is eligible for unpledging at any given point in time.

When users initiate an unpledge request through the LSP interface, they may encounter errors or rejections if:

- The requested unpledge amount exceeds the eligible limit (based on outstanding loan value, haircut, or margin requirements)

This leads to:

- Poor user experience — users get rejected after attempting unpledge.
- Increased operational load — repeated support queries and failed attempts.
- Inefficient system calls — LSPs must attempt unpledge blindly, often resulting in unnecessary API hits to RE systems.

The Unpledge Eligibility API will provide LSPs a way to pre-inform customers of their eligible unpledge value before they initiate the unpledge request.

---

# **How do we measure success?**

**Primary success metrics:**

Low failure in unpledge requests due to ineligibility.

Reduction in customer support queries related to unpledge failures.

Improved end-to-end unpledge success rate across LSPs.

---

# **How are others solving this problem?**

Market players offering Loan Against Mutual Funds (e.g., HDFC Bank, ICICI Bank, Bajaj Finance) typically provide eligibility indicators to their front-end systems via internal APIs.

- Some provide fund-wise margin and eligible value APIs to their digital channels.
- Others compute eligibility dynamically based on outstanding loan, NAV fluctuations, and haircut values but do not expose this data to third-party LSPs, leading to fragmented user experiences.

Our approach aims to differentiate by empowering LSPs directly with eligibility details — enabling consistent and transparent unpledge journeys across all channels.

---

# **What is the solution?**

We will provide an Eligibility API for Unpledging that LSPs can call before initiating an unpledge request. The API will return aggregate eligibility (amount-wise) for the LSP to inform to their customers on their app. The eligible amount based on which the user will be able to unpledge their funds will be calculated as detailed below:

$Maximum Unpledge Eligible Amount = Drawing Power - Principal Dues - Interest Dues - Outstanding Loan Principal(Not due) -  Outstanding Interest for Upcoming EMI across all Tranches(Not Due) + Total Excess$

The API we need to provide will include the following mandatory parameter:

loanAccountId

The response we need to provide based on the API call will include the following mandatory parameters:

loanAccountId
maxUnpledgeEligibleAmount

The Maximum Unpledge Eligible Amount will be derived from a stretchy api which Finflux is building. This stretchy api will contain all the tranche schedules for a loan. We will be using these tranche schedules to calculate the amount and share it with Cred.

Unpledge Eligibility API Validations:  

1. If the Max Unpledge Eligible amount is zero or positive we will be sharing the same with the LSP. (We won’t be deciding if any fund’s unit qualifies for unpledging or not)
1. If the Loan account is in shortfall then the max unpledge eligible amount will be negative. In this case we need to send to the LSP a message in the API that ‘The Loan Account is in Shortfall’.
2. If the loan account is frozen then we will need to send in the API a message that ‘The Loan Account is frozen, unpledging can’t be done’.

LSPs will be able to get the Collateral details from the Get Collateral Mapping API which they will be using to provide a UI view for the user and accordingly users will select the fund/fund units to unpledge and submit the unpledge request. 

The LSP will then call the Create Remove Collateral Request API and pass the required collaterals along with the collateral details for them to be unpledged.