# OP - Selloff and Withdrawal request mismatch

We provide loans against pledged Mutual Funds (MFs), offering customers a credit limit based on the Loan-to-Value (LTV) ratio of their pledged funds. Typically, if a customer pledges Rs. 200,000 worth of MFs at an LTV of 0.5, they receive a credit limit of Rs. 100,000. The process works seamlessly until the customer initiates a selloff request for part of their pledged funds.

The challenge arises when a customer requests to sell off a portion of their pledged funds—let’s say Rs. 50,000. This should reduce both the pledged amount and the available credit limit accordingly. However, the process of completing the selloff and reducing the lien on the pledged amount is currently manual and takes time, as it is handled via email or WhatsApp. During this period, the customer still sees their original credit limit in the app, which can lead to issues.

The core problem here is not simply a delay in syncing data, but rather the risk of **conflicting requests**. While the selloff is being processed, the customer may attempt to raise a withdrawal request based on their old credit limit, which is no longer valid. By the time this request reaches the lender, the selloff has reduced the customer’s available limit, and the withdrawal request fails because it exceeds the updated limit.

To prevent this, we need to ensure that the system doesn’t allow contradictory actions during this process. **Customers should not be able to submit a withdrawal request while a selloff request is still being processed.**

### **Proposed Solution:**

The solution is straightforward: the system should block the customer from raising any withdrawal requests while the selloff is in progress. This ensures that the customer cannot make a request based on an outdated credit limit that will result in a failed transaction. By preventing contradictory requests, we create a more efficient process that reduces frustration and enhances the customer experience.

During the manual processing of the selloff, we can also empower our operations team to **manually adjust the customer’s credit limit** in the system. This proactive step ensures the app reflects the anticipated reduction in the limit, preventing the customer from attempting to withdraw more than they can. Once the selloff is finalized and confirmed by the lender, the system will restore the updated limit, ensuring that all future transactions are based on the correct, available credit.

**New Workflow suggestions:**

1.	Blocking **Selloff Request Submission**: When a customer initiates a selloff, the system automatically prevents any withdrawal requests from being raised until the selloff is complete. This eliminates the possibility of a failed withdrawal due to conflicting limits.

2.	**Manual Limit Adjustment**: While the selloff is being processed manually, the operations team can update the credit limit in the system to reflect the anticipated new limit. This ensures that the customer sees accurate information and prevents invalid withdrawal attempts.