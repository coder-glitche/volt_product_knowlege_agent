# Repayment next step

: Karuna Sankolli
Created time: January 10, 2025 12:33 PM
Status: Not started
Last edited: January 17, 2025 12:25 PM

# Loan Repayment System Redesign

### Current Hypotheses

1. **Hypothesis 1 :** Users expect repayments (interest, shortfall, principal) to be separate since our home screen and other places don’t communicate how they are interconnected.
2. **Hypothesis 2 :** Most of users are familiar with credit card statement model. 

## JTBD problem list

### Job Story 1: Clear Shortfall

"When I am in shortfall, I want to know exactly how much I need to pay so that I can clear my dues easily and get out of shortfall."

**Current Problems:**

- The shortfall card only shows the shortfall amount, hiding the fact that users need to pay shortfall + charges + interest
- Both TATA & DSP use CIP/ICP apportionment logic which requires clearing all dues, but this isn't communicated upfront
- Users encounter unexpected higher payment amounts at the final step, leading to frustration and payment abandonment or doubts

### Job Story 2: Pay Interest

"When I need to pay my interest, I want to understand why I need to pay any additional charges"

**Current Problems:**

- In TATA, users see interest amounts increase in months with additional charges
- The system requires users to clear charges before interest due to apportionment logic, but this requirement isn't explained
- Users are unable to pay just interest when charges are due, contradicting their mental model of separate payments
- These charges and interest come under monthly dues as a concept

### Job Story 3: Make Principal Repayment

"When I want to repay my principal amount, I want to know how my payment will be applied so I can make an informed decision."

**Current Problems:**

- For both TATA & DSP, users with mandates try to repay principal but discover they must first clear out the interest and charges which are scheduled to be cut through mandate.
- The principal repayment screen doesn't explain that the payment will first go towards interest and charges
- Users learn about payment apportionment only after attempting the transaction, leading to canceled payments and frustrated users.
- Users are not aware that principal is being repaid early and isn’t due for 3 years.

### Job Story 4: Understand Payment Structure

"When I look at my home screen, I understand the payments are separate since they show up as separate components, But its in reality an interconnected system."

**Current Problems:**

- The home screen shows interest, shortfall, and principal as separate cards, suggesting they can be paid independently
- This display contradicts the actual interconnected payment system where all components affect each other
- Users form incorrect mental models about payment flexibility, leading to confusion when they try to make payments

## Data from credit bureau to check  Hypothesis 2

[Cibil details](https://docs.google.com/spreadsheets/d/1P9bZpr2kpuLuSubhBGbdIurRyvR3cZuADPAw6nhkIXU/edit?usp=drivesdk)

### Data I need from credit bureau

- % of loan type distribution of our users. [How many have credit cards, PL, Overdraft, etc]
- City
- State
- Avg credit card usage

### Analysis based on data and takeaways

**Major takeaways:**

1. From over 72 loan account types, credit card is the most popular loan account type with 15.42%. We can infer based on this that they must be familiar with the credit card mental models including that of releasing statements with monthly dues, overdue interest, annual joining fees and so on. We could use this insight to educate our users better by drawing parallels in our education efforts.
2. On avg around users have ~2 active personal loans apart from LAMF. So personal loans can also be another source of inspiration for education.
3. Only 3% of this user set had overdraft loans.
4. Tier 3 cities show highest average loan amount (₹6.24 lakhs), Customers in Tier 3 cities have higher loan requirements but potentially fewer options, creating an opportunity for specialized mutual fund-backed loan products.
5. Tier 1 cities follow with ₹4.89 lakhs average
6. Tier 2 and 4 cities show lower average loan amounts

### Data I need from support team

1. % of queries on repayment for LMS
2. What are some common questions users ask when they call?
3. What language do they prefer communication in?
4. Are there any common patterns you have noticed between types of users and their queries?

### Next Steps

- [ ]  User flows for all cases of repayment
- [ ]  Wireframes
- [ ]  Design

### [OLD] Doc

## Problem Summary

This summary outlines the redesign of Volt's loan repayment system to align with users' mental models, specifically exploring the credit card monthly statement generation model as a potential approach.

- Clearly communicate repayment structure
- Leverage existing mental models so that user easily understands and remembers

## Key Objectives

1. Improve user understanding of loan repayment accounting and  reduce confusion around apportionment logic
2. Streamline all repayment flows // Problem 
3. Increase repayment success rates // Problem 
4. Address shortfall education gaps //  Problem 
    1. Do people prefer communication in Hindi
5. Improve information hierarchy on home for all alerts, dues and withdrawal card //  Problem

## Areas Requiring Clarity

### 1. User Mental Model Validation

- **Current Assumption**: Users are familiar with credit card statement mental model
- **Questions to Address**:
    - What percentage of our users have credit card experience?
    - How do users currently perceive the relationship between principal, interest, and shortfall?
    - What specific aspects of credit card statements resonate with users?

### 2. Apportionment Logic

- **Current State**: CIP & ICP (Charges, Interest, Principal) apportionment affects all repayment types
- **Key Questions**:
    - Impact of proposed apportionment for DSP?
    - User comprehension of current apportionment system
    

### TATA

- CIP
    - Charges
        - Processing fee/ Joining fee charged on your statement | one time
            - First withdrawal or Statement
        - Event based
            - Line enhancement
            - Lien removal charge
        - Penal
            - penal charges
            - Daily penal charge
    - Interest
        - Accrued interest
    - Principal
        - Revolving credit line
        - End of the tenure
        - Partial/ Full repayment
        - Shortfall

## Validation Plan

### 1. Quantitative Analysis

- **User Behavior Data**
    - Analyze repayment patterns in current system
    - Track support ticket categories and frequencies
    - Measure drop-off points in repayment flows
- **Success Metrics**
    - Reduction in support tickets related to repayment
    - Increase in successful first-time payments
    - Decrease in payment-related session abandonment
    - Improved user satisfaction scores

### 2. Qualitative Research

- **User Interviews**
    - Current mental models around loan repayment
    - Experience with credit card statements & secured and unsecured loans
    - Pain points in existing system
    - ~~Prototype testing of new approaches~~
- **Support Team Insights**
    - Common user confusions
    - Frequently asked questions
    - Resolution patterns
    - Feature requests

### 3. A/B Testing Strategy

- **Phase 1: Home Screen Components**
    - Test consolidated vs. separate card designs
    - Measure engagement with different information hierarchies
    - Evaluate impact on support requests
- **Phase 2: Repayment Flows**
    - Compare completion rates between old and new flows
    - Measure time to complete payments
    - Track error rates and corrections
    - No of users who need help during flows

### 

## Solution

## Approach Analysis

### Approach 1: Unified Repayment View

**Pros:**

- Single source of truth for all repayment information
- Reduces cognitive load on users
- Clearer representation of total amount due
- Simplified navigation

**Cons:**

- May overwhelm users with multiple about individual components of interest, shortfall and principal
- Could make principal repayment always visible increasing chances of early principal repayment

### Approach 2: Enhanced Separate Components

**Pros:**

- Maintains familiar interface for existing users
- Clearer breakdown of different payment types
- Easier to implement incrementally
- More flexible for future modifications

**Cons:**

- Doesn't address core confusion about interconnected payments
- May perpetuate current mental model issues
- Requires additional education efforts

## Implementation Phases

### 3. Component Integration

- **Questions to Address**:
    - Should repayment information be consolidated or kept separate?
    - How to handle real-time updates of interdependent amounts?
    - What level of detail should be shown on the home screen?

### Phase 1: Home Screen Redesign

**Focus Areas:**

- Withdrawal card optimization
- Interest display
- Shortfall notifications
- Alert system refinement

**Success Criteria:**

- 20% reduction in payment-related support tickets
- 15% increase in first-time payment completion
- 25% reduction in payment flow abandonment

### Phase 2: Shortfall Flow Optimization

**Focus Areas:**

- Clear presentation of total amount due
- Improved explanation of apportionment
- Generalised payment process i.e from viewing amount, entering amount to summarising repayment

**Success Criteria:**

- 30% reduction in shortfall-related confusion
- 25% increase in shortfall clearance rate
- 40% reduction in related support tickets

### Phase 3: Early principal repayment + Interest statement repayment

**Focus Areas:**

- Principal payment experience
- Enhanced understanding with repayment apportionment
- Improved payment confirmation
- Improved distinction between Dues and early repayment

**Success Criteria:**

- 35% improvement in user satisfaction
- 50% reduction in payment-related support tickets
- 30% increase in on-time payments

## Risk Analysis and Mitigation

### Technical Risks

- **Complex System Integration**
    - Mitigation: Phased rollout with thorough testing
    - Fallback mechanisms for critical functions

### User Risks

- **Learning Curve**
    - Mitigation: In-app education and guided tours
    - Progressive disclosure of complex features

### Business Risks

- **Payment Delays**
    - Mitigation: Clear communication of changes
    - Temporary support increase during transition

## Next Steps

1. Initiate user research to validate mental model hypothesis
2. Begin technical feasibility assessment
3. Create prototype for initial user testing
4. Develop detailed metrics tracking plan
5. Schedule stakeholder reviews for approach selection

## Problems with the current system

- Users lack visibility into how their payments are accounted for across components (principal, interest, charges)
- Users are surprised by payment amount changes due to apportionment in cases like
    - For TATA & DSP: When user is in shortfall and they have interest and charges due. The card outside will show only shortfall amount but the amount to be paid will be shortfall + charges + interest since both have CIP or ICP apportionment logic.
    - For TATA: User is confused when interest amount increases in some months when there they have additional charges due. Those months users are unsure why they have to repay charges before the can repay interest.
    - For TATA & DSP: When users have mandate set up and they want to repay principal amount but cannot since they have to first clear their dues. Here the principal repayment first clears the interest and charges and then moves on to principal and the current principal repayment screen does not give this communication of apportionment anywhere before user makes the principal repayment.
    - User expectations of separate payment components on home of interest, shortfall and principal conflict with the actual interconnected system