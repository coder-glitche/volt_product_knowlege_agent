# Project Elevate - LMS

: Ranjan kumar Singh
Created time: March 6, 2025 3:26 PM
Status: Not started
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

BFL has restricted our customer to increase the credit limit.

---

# **How do we measure success?**

- Number of BFL customers who create DSP accounts
    - After foreclosing loan with BFL
    - Without closing loan with BFL
- User satisfaction for dual-account management
- 0% error in sending loan servicing comms

---

# **How are others solving this problem?**

---

# **What is the solution?**

Implement a system that enables customers to create additional loan accounts with DSP when they need higher credit limits, while providing a seamless experience to manage multiple credit lines within our platform.

Same solution should work to migrate TCL customer

## 1. Detailed Requirements

### 1.1 Multi-Lender Account Creation

### User Stories

- As a BFL customer reaching credit limit, I want to be informed about DSP credit options so I can access more funds.
- As a customer, I want a simple way to apply for a DSP account so I don't have to re-enter information I've already provided.
- As a platform user, I want clear information about having multiple lenders so I understand the implications.

### Functional Requirements

- System identifies BFL customers approaching/at their credit limits
- Targeted in-app notifications and emails about DSP credit options
- Streamlined DSP application process with pre-filled information
- Clear disclosure about maintaining multiple lender relationships
- Automated eligibility check for DSP accounts

### 1.2 Multi-Account Management Interface

### User Stories

- As a customer with multiple credit lines, I want to easily switch between accounts so I can manage them efficiently.
- As a user, I want to clearly see which lender account I'm using so I don't get confused.
- As a customer, I want consistent servicing options across lenders so my experience remains seamless.

### Functional Requirements

- Account switcher in prominent UI location
- Visual differentiation between BFL and DSP accounts (color coding, icons)
- Consistent interface for common actions across both lender accounts:
    - Repayments
    - Disbursals
    - Lien removal
    - Line enhancement
    - Foreclosure
- Account summary page showing combined and individual credit availability

### 1.3 Multi-Account Communications

### User Stories

- As a customer with multiple accounts, I want communications to clearly indicate which account they relate to.
- As a user, I want consistent notification preferences across accounts so I can manage communications efficiently.

### Functional Requirements

- Lender identification in all communications (email, SMS, push notifications)
- Account-specific transaction confirmations
- Unified notification settings with per-account options
- Event-based communication templates for each lender
- Personalized communications strategy based on customer's usage of multiple accounts

## 2. Technical Architecture

### System Components

- Account Relationship Manager: Links customer profiles to multiple lender accounts
- Lender API Integration: Unified interfaces for BFL and DSP
- Communication Engine: Templatized messaging with lender context
- Eligibility Engine: Determines DSP qualification based on BFL history

### Data Model Changes

- Customer profile expansion to support multiple active credit lines
- Transaction attribution to specific lender accounts
- Communication logs with lender identification

## 3. User Experience Design

### Key Design Principles

- Clear account differentiation
- Consistent servicing flows
- Transparent lender identification
- Seamless account switching

Design requirement - PnC

| Scenario | Applicable for TCL | Applicable for BFL | Applicable for DSP |
| --- | --- | --- | --- |
| Zero POS | Y | Y | Y |
| Zero Net payable | Y | Y | Y |
| Net payable <0 [Excess] | Y | Y | Y |
| Zero POS & Interest >0 | Y | Y | Y |
| Zero POS & charges >0 | Y | Y | Y |
| POS >0 | Y | Y | Y |
| Pending renewals + Renewal in progress | Y | N | N |
| Interest due | Y | Y | Y |
| Interest overdue | Y | Y | Y |
| Both account has interest due | Y | Y | Y |
| One account has interest due and one has a overdue | Y | Y | Y |
| Portfolio sell-off initiated because of non repayment of interest/shortfall | Y | Y | Y |
| Only charges due | Y | Y | Y |
| In shortfall | Y | Y | Y |
| Both account has a shortfall | Y | Y | Y |
| One account shortfall aging is > another account | Y | Y | Y |
| Loan expired | Y | N | N |
| Loan foreclosure in progress | Y | Y | Y |
| Loan foreclosed | Y | Y | Y |
| Lien removal in progress | Y | Y | Y |
| Withdrawal in progress | Y | Y | Y |
| Repayment in progress | Y | Y | Y |
| POS of lender 1 > POS of lender 2 | Y | Y | Y |
| Credit line Aging Lender 1 > Aging of lender 2  | Y | Y | Y |
| Line enhancement in progress | Y | N | Y |

### Key Screens

- Account switcher interface
- Multi-account dashboard
- Lender-specific transaction flows
- Communication preferences for multiple accounts

Design link: https://www.figma.com/design/rSibJt7yGBXWJvLrcieIdt/Project-elevate?node-id=47-3239&t=jgOW0ETuKQU9g2qk-1

## 4. Analytics Requirements

### Event Tracking

- Account switch frequency
- Feature usage across lenders
- Conversion from BFL to DSP
- Communication engagement by lender

Amplitude events:

| Journey | User Action | Event name | Event property | Expected value | User property |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

### Reports

- Multi-lender usage patterns
- Credit utilization across lenders
- Cross-lender behavior analysis
- Communication effectiveness by lender

## 5. Go-to-Market Strategy

### Marketing Plan

- Targeted campaigns for BFL customers approaching limits
- Educational content on benefits of multiple credit lines
- Case studies showcasing increased financial flexibility

### Customer Support Training

- Multi-account troubleshooting procedures
- Lender-specific policy differences
- Handling account-specific questions
- Escalation paths for each lender

## 6. Timeline and Release Planning

### Phase 1: Multi-Lender Foundation (4 weeks)

- DSP account creation for eligible BFL customers
- Basic account switching capability
- Lender identification in communications

### Phase 2: Enhanced Management (4 weeks)

- Improved account dashboard
- Consistent servicing flows
- Advanced communication preferences

### Phase 3: Optimization (2 weeks)

- Analytics-driven improvements
- Personalized multi-account recommendations
- Enhanced cross-lender features

## 7. Risk Assessment and Mitigation

### Potential Risks

- Confusion between multiple accounts leading to servicing issues
- Inconsistent policies between lenders causing customer dissatisfaction
- Increased support load from multi-account management questions

### Mitigation Strategies

- Clear visual differentiation between accounts
- Comprehensive education on lender differences
- Enhanced support training for multi-account scenarios
- Proactive communication about account-specific policies

## 8. Success Criteria and Measurement

### Launch Criteria

- 90% of test users can successfully navigate between accounts
- Support team demonstrates 95% accuracy in multi-account troubleshooting
- All communications correctly identify associated lender account

### Post-Launch Evaluation

- Customer satisfaction metrics for users with multiple accounts
- Reduction in credit limit increase requests
- Retention improvement for multi-account users
- Support ticket volume related to account confusion

## 9. FAQs

1. **Will having multiple lender accounts affect my credit score?**
Each lender may perform a credit check, which could have a temporary impact on credit scores.
2. **Can I transfer balance between BFL and DSP accounts?**
No, these are separate credit facilities with different lenders.
3. **Will my repayment due dates be the same for both accounts?**
Due dates are set by each lender and may differ.
4. **How do I choose which account to use for a transaction?**
You can select your preferred account before initiating a transaction.
5. **Can I close one account while keeping the other active?**
Yes, each account can be managed independently.

## 10. Action Items

### Product

- [ ]  Finalize feature specifications for multi-account switching
- [ ]  Define lender-specific service flows
- [ ]  Develop communication strategy for multi-account users

### Business

- [ ]  Finalize terms with DSP for BFL customer onboarding
- [ ]  Develop support playbook for multi-account scenarios
- [ ]  Create educational content explaining multiple lender relationships

### Design

- [ ]  Create UI mockups for account switching interface
- [ ]  Develop visual system for lender differentiation
- [ ]  Design multi-account dashboard layout

### Engineering

- [ ]  Evaluate architecture changes needed for multi-lender support
- [ ]  Estimate development effort for account switching mechanism
- [ ]  Assess integration requirements with DSP systems

## 11. Appendix

### Meeting Notes

[To be populated as meetings occur]

Suspend all Bajaj application > Create DSP application

What is user drop-off and do not want to continue and user are not eligible since BFL account is suspended

Txn API are on borrower account

Backfill of all primary credit id

Foreclosure are on borrower id

Bank account change is not allowed

How to handle phone and email change

How to create interest and Shortfall - Arpit and Rishi

How to handle new foreclosure flow

How to handle comms and new comms implementation 

Do not allow to open DSP account when POS is 0

Nudge user based on AUM

- PF offer
- ROI offer

Amplitude