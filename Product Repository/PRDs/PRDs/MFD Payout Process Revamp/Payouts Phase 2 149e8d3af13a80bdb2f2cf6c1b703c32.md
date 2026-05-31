# Payouts Phase 2

Issues

1. 1. **Uncertain Base Transaction Data:** Due to challenges in maintaining updated transaction tables with lender APIs, the ETA for receiving accurate base transaction data is unpredictable, often delaying payouts. This process needs to be initiated at the beginning of each month.
2. 2. **Commercials in Credit Application:** The Analytics team has noted difficulties due to the absence of commercials as a parameter in credit applications. Currently commercials for Platforms and Base are hardcoded
3. 3. **GST Invoice Generation:** There is no structured process for GST invoice creation, causing partners to send ad hoc invoices, which are frequently inaccurate, leading to approval delays.
4. 4. **Unmapped Transactions:** Approximately 20k transactions lack a mapped recipient, creating further reconciliation challenges.
5. 5. **Lack of Accessible MFD Account Balance Data:** We do not have comprehensive account balance data, affecting accurate calculations. We need to provide better Partner level account visibility to the Support team and platforms.
6. 6. **HSBC Reconciliation Process:** The current reconciliation process with HSBC could be improved due to unrelated transactions in the account.
7. 7. **Dedicated Support for Payout Issues:** There is no dedicated team member or specific contact for payout-related queries or a dedicated email portal for these issues.
8. 8. **Ad-hoc payments:** There were ad-hoc payments based on partner requests without the required details to be reckoned.
9. 9. **Communication challenges:** In past we have shared Comms with wrong Details to the Partners raising a lot of tickets and Current commission statement could be better.Proposed Phase 1 Solution: GST Invoicing Process

Tasks identified 

- Document the current table creation process end to end
    - Review and identify bugs and callout limitations
- Parter commercials to be moved to a config instead of the a hardcoded values
- Resolve 20k Unmapped trasctions
    - get a more accurate count
    - find and resolve the audit challanges
- Build DB for the balance amounts
- HSBC API integration
- Dedication individual for Payouts - with accounts and Data background
- Build communication Scripts inhouse and have the team

Other challanges - 

- Currently all the process after tables is on Puneets personal laptop and is very risky. we don’t have any backup
- We need to move to just supporting the Email channel for payouts and payouts related query. We will depo the MFD dashboard.
- we need a dedicated person for payouts as the all the calcualations and comms , auditing , and reconsilling is ad hoc and have to be balanced with other tasks
-