# Handling Discrepancies Between Assumed and Actual Limits

In our **Loan Against Mutual Funds (MF)** process, we allow users to act based on certain limits displayed on their dashboard throughout the loan journey. These limits are meant to provide a smooth and consistent experience, ensuring users feel confident as they proceed with their loan requests. Two key terms we deal with are the **Drawing Power (DP)** and the **sanction limit**.

•	**Drawing Power (DP)** is the theoretical maximum amount a user can borrow, based on factors like the NAV, unit price, and LTV of their pledged mutual funds.

•	**Sanction Limit** is the actual borrowing limit we allow users to access through the platform.

We calculate these limits based on the **assumed DP and sanction limit** derived from the formulas and approved lists shared with us by our lending partners. However, in the actual loan processing, the **lender retains the final rights** to determine both the **DP and sanction limit**, since they are the ones disbursing the loan amount. This means that the **assumed DP** and **sanction limit** we show to the user may differ from the **final limits** confirmed by the lender after their internal checks and approvals.

In certain cases, there can be discrepancies. For example, the lender may adjust the list of approved mutual fund units or change the loan-to-value (LTV) ratio during the final review, leading to a lower **DP** or **sanction limit** than what was originally calculated. As a result, a user may initiate a withdrawal request based on the higher, **assumed limit**, but it can get **rejected** once the lender processes the loan and confirms the lower final limits.

To handle these situations, we notify the user if their **withdrawal request exceeds the final approved limits**. The system will automatically **error handle the request** and inform the user of the discrepancy. We will also guide the user to **submit a new withdrawal request** that falls within the actual, lender-approved DP or sanction limit, ensuring that they can successfully access their funds without further delays or confusion.

While these discrepancies can happen due to changes in the lender’s processing, our goal is to keep users informed and ensure that they can quickly adjust their requests to align with the actual limits approved by the lender. This approach minimizes user frustration and maintains transparency throughout the loan process.