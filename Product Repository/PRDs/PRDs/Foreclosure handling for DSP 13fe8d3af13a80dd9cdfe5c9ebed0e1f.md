# Foreclosure handling for DSP

: Vaibhav Arora
Created time: November 15, 2024 5:29 PM
Status: Done
Last edited: November 18, 2024 12:09 PM

# **What problem are we solving?**

Users at this point in time can raise multiple requests at a time, these transactions can often cause the other to fail. 
For example, if a user, raises a withdrawal which is pending with the NBFC to process, and immediately raises a foreclosure, they will be able to, which may cause dangling transactions to be left at our end.

If a user raises a foreclosure request, when a mandate presentation transaction is still processing for them, and we close the loan account, we will have no way to post the proceeds from the presentation into their loan account. 

To solve for such scenarios, we will be blocking foreclosure requests from the LSP under certain conditions, and will give them the corresponding reason for not allowing the same. 

The LSP can then correspondingly render a UI to inform the user for the same.

---

# **How do we measure success?**

This is a sanity item, to improve the functionality of the system we should track the following items

- Number of requests in a non terminal state on closed loan accounts
- Number of failed foreclosures due to already existing requests
- Acceptance rate of foreclosure requests (Number of requests that got accepted / Total foreclosure requests)

---

# **How are others solving this problem?**

- We are able to raise requests with Bajaj and Tata such errors are handled operationally

---

# **What is the solution?**

Types of requests (Money/Collateral/Service):

| Type of request | Foreclosure blocked |
| --- | --- |
| Withdrawal | Yes |
| Repayment | Yes |
| Collateral removal | Yes |
| Collateral addition | Yes |
| Excess refund | Yes |
| Mobile update | No |
| Email update | No |
| Foreclosure | Yes |
| Withdrawal reversal | Yes |
| Repayment reversal | Yes |
| Charge reversal | Yes |
| Interest refund | Yes |
| Mandate presentation | Yes |

For any request which is pending, as per the above sheet, foreclosure request will not be processed instead we will pass an error message to the LSP.

Foreclosure cannot be processed as there is an existing pending request (Request ID: [Request ID]). Please resolve or complete the pending request to proceed with foreclosure.

In case there are multiple pending requests, pass the latest one as a response to the LSP