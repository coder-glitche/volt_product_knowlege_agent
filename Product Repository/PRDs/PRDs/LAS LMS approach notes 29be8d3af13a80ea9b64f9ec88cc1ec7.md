# LAS LMS approach notes

: Ranjan kumar Singh
Created time: October 29, 2025 3:12 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# Summary:

We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics.

For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience.

Key considerations:

No changes for users who have only a LAMF (Loan Against Mutual Funds) account.

No changes in the loan servicing experience for users with only an LAS account.

For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface.

## LMS service scenarios

### Customer with only LAMF account

1. No change in existing behaviour, flow and configurations

### Customer with only LAS account

Expected changes in existing modules

| **Modules** | Requirements | Edge cases scenarios | Action items |
| --- | --- | --- | --- |
| Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed
2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI
2. Non STP flow
3. Partial pledge confirmation
4. Partial lodgement | 1.Account status life cycle
2. Account status scenarios |
| Disbursal | 1. No change in existing user experience(UI/UX)
2. LAS specific Validations will be applicable 
3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: 
- Based on Account status
- Min amount allowed
2. TAT BRE for LAS
3. Lifecycle management on UI + comms |
| Principal Repayment | No change |  |  |
| Transactions | No change |  |  |
| Lien removal | 1. Lien removal entry point: No change
2. Pledged collateral list: LAS specific Data points
3. Un-pledge request validation: No change
4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific)
 | - Data points to show collateral details
- Allowable qty criteria
- Rejections cases |  |
| Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA |  |
| Collateral history | No change |  | Need to check the copy and data points |
| Foreclosure | No change |  | 1. To review UI copy  |
| FAQs | 1. LAS specific FAQs |  | 1. Configure product specific FAQs
2. FAQs content for LAS |
| Interest collection | No change |  |  |
| Shortfall | No change |  |  |
| Service request - [Phone, Email, Bank/Mandate update] | 1. Phone update: No change
2. Email update: No change
3. Bank and mandate update: Bank and mandate are at line level, Bank and mandate can be separate for LAMF and LAS | - Comms handling in cases of two separate bank account linked with two loans |  |
| Loan details | No change |  |  |
| Help and support | No change |  |  |
| Profile | Account details: No change
Bank and mandate: Loan account specific Bank and mandate display and setup flow |  |  |
| Loan servicing comms | 1. LAS specific comms content: Template will be separate for LAMF and LAS
2. LAS specific Comms config: Introduce Filtering based on product type
3. LAS specific comms approval flow: Separate events and task for LAS, Separate files for approval
4. Redirections: 
- For interest and shortfall user will land on the dashboard product page using deep-link
- We need to create separate deep-link for LAMF and LAS so that users can land on product specific page |  |  |
| UI Notifications | Interest notification: No change
Shortfall notification: No change
Drop-off notification: No change | 1. If user has two loan account 
- Interest is due/overdue in both the account
- Shortfall in both account
- Interest Due/Overdue and shortfall in both account |  |

### Customer with both LAMF and LAS account

Notes:

Ongoing application - User will not be able to see ongoing application in their LAS Journey
Scenarios of notifications
Account opening lifecycle tracking (scenarios)
Collateral management
Add collateral - Open to discussion
Remove collateral
PRD discussion
Communications - PRD - Deeplinking - Product specific
Statements - Check FF statements

- Notes: 29 OCT
    - Not solving for critical notification
    - Loan product listing product data points

- Eligibility check - Limit of collateral being released should be less then equal to TOS - Accrued interest [No buffer]
- Lien verification and lodgement validation before lien removal using PMR report
- PSN - Pleadge sequence number
- RQ - Release quantity
- IQ: Invoked qty
- Revocation is not through API → but transnet account [Manually]
- PRM we will get on market working hours - Need to create BRE
- Lien removal → Units selections can’t be in decimal