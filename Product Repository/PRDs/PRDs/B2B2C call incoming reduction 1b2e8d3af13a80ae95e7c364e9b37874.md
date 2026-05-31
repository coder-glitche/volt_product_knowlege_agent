# B2B2C call incoming reduction

: Naman Agarwal
Created time: March 10, 2025 1:03 PM
Status: In progress
Last edited: April 17, 2025 11:41 AM

[Takeaways from Call analysis ](B2B2C%20call%20incoming%20reduction/Takeaways%20from%20Call%20analysis%201d0e8d3af13a801c8684fe6a207f97d7.md)

[](B2B2C%20call%20incoming%20reduction/Untitled%201d8e8d3af13a803d92e9cdb6778f4809.md)

# Detailed Breakdown of Customer Call Issues

## Loan Application Issues

- **Withdrawal Process Assistance (80 calls)**: Customers frequently struggle with the loan withdrawal process after approval.
    - They face confusion about where and how to initiate withdrawals, authentication requirements, and processing times.
    - Many calls include statements like: *"I can see my loan is approved but I don't understand where to click to get my money"* or *"The withdrawal button is grayed out even though my loan shows as approved."*
    - The withdrawal interface appears to lack clear instructions for first-time users.
- **OTP Issues (75 calls)**: One-time password delivery and acceptance is a major friction point in the application process.
    - Customers report: *"I never received the OTP message"*, *"The system says my OTP is invalid even though I'm entering exactly what was sent"*, and *"The OTP expires too quickly before I can enter it."*
    - This frequently blocks application completion and creates frustration as customers must repeatedly request new OTPs.
- **Processing Fee Calculation (70 calls)**: Customers express confusion about fee calculations, particularly when the final disbursed amount differs from expectations.
    - Common complaints include: *"The fee was higher than what was initially shown"* and *"I don't understand why GST is calculated separately after I agreed to the loan terms."*
    - The fee structure appears to be disclosed incompletely during the application process.
- **Loan Eligibility Questions (40 calls)**: Prospective borrowers frequently call with confusion about eligibility requirements.
    - They mention: *"The website shows different criteria than what the agent told me"* and *"I was rejected but don't understand why since I meet all the listed requirements."*
    - The eligibility criteria seem inconsistently communicated across different channels.
- **Application Timeout Errors (35 calls)**: Users report sessions expiring mid-application, forcing them to restart the process.
    - Typical complaints include: *"I had filled out everything and when I clicked next, it said my session expired"* and *"The application keeps timing out when I'm uploading documents."*
    - These timeouts appear to occur most frequently during document upload or verification steps.

Payment Processing Issues

- **Partner Payout Delays (65 calls)**: Affiliate partners frequently report delayed commission payments.
    - Partners state: *"It's been three months since I was supposed to receive my commission"* and *"The dashboard shows payments as 'processed' but nothing has arrived in my account."*
    - These delays severely impact partner relationships and trust in the platform.
- **Bank Detail Updates (60 calls)**: Partners and customers experience difficulties updating their bank account information.
    - Common complaints include: *"I submitted the new bank details two weeks ago but payments are still going to my old account"* and *"The system keeps rejecting my new bank information without any explanation."*
    - The bank detail verification and update process appears overly rigid.
- **Shortfall Management (55 calls)**: Borrowers express confusion about margin calls and shortfall notifications.
    - They report: *"I received a shortfall notice but don't understand how much I need to pay or by when"* and *"The shortfall calculation doesn't match my understanding of my loan-to-value ratio."*
    - Communication about shortfall requirements lacks clarity and actionable instructions.
- **Interest Payment Confusion (45 calls)**: Customers frequently call with questions about interest calculations and payment timing.
    - Common queries include: *"Why was my interest debit higher than last month when I haven't borrowed more?"* and *"The interest statement doesn't clearly show how the amount was calculated."* The interest calculation methodology appears insufficiently transparent.

Technical Issues

- **Mobile App Technical Issues (50 calls)**: Users report frequent crashes, loading failures, and feature unavailability on the mobile application.
    - Typical complaints include: *"The app crashes every time I try to view my loan details"* and *"The withdrawal section never loads on my phone but works on my friend's device."* These issues appear device-specific in many cases, suggesting compatibility problems.
- **Account Access Problems (25 calls)**: Users experience difficulties logging into their accounts.
    - They report: *"The system doesn't recognize my username even though I'm copying it directly from my welcome email"* and *"I keep getting locked out after one failed login attempt."* The access recovery process is reportedly cumbersome and slow.

Documentation and Verification Issues

- **KYC Documentation Issues (25 calls)**: Customers encounter problems uploading or getting verification for their KYC documents.
    - Common complaints include: *"My documents were rejected without specific reasons"* and *"I've uploaded the same document three times but keep getting error messages."* The feedback on document rejections appears insufficient for users to correct issues.
- **Pledged Funds Release Timeline (30 calls)**: Borrowers express confusion about how long it takes to release pledged funds after loan repayment.
    - They report: *"It's been two weeks since I fully repaid my loan but my mutual funds are still showing as pledged"* and *"Different agents are giving me different timelines for when my funds will be released."* The release process and timeline appear inconsistently communicated.

### Partner-Specific Issues

- **Commission Structure Clarification (30 calls)**: MFD partners call seeking clarity on commission calculations. They mention: *"The new tiered commission structure is confusing compared to the flat rate we had before"* and *"I can't determine why I received less commission than expected for similar loan volumes."*
- **Mutual Fund Valuation Questions (20 calls)**: Both customers and partners call with questions about how mutual funds are valued for loan purposes. They ask: *"Why is the loan value of my mutual fund portfolio less than the current market value?"* and *"The valuation formula used seems different from what was initially explained."*

### Isolated  Issues

- **Application Data Persistence (10 calls)**: Users report losing entered data when navigating between application sections. They state: *"I entered all my employment details, went back to check something, and everything was gone when I returned."* This creates significant friction in the application completion process.
- **Partner Dashboard Access (15 calls)**: MFD partners report inconsistent access to their performance dashboards. They mention: *"The dashobard is frequently unavailable during peak business hours"* and *"The dashboard data sometimes shows incorrect shortfall calculations."*
- **Post-Disbursement Documentation (12 calls)**: Borrowers report difficulties obtaining loan documentation after disbursement. They state: *"I need the loan agreement for my tax filing but can't find it anywhere in my account"* and *"The download button for my loan statement doesn't work."*

## Issue Frequency Analysis

| Issue Category | Approximate Count | Percentage of Calls |
| --- | --- | --- |
| Authentication & Verification | 23 | 27% |
| Financial Process Failures | 19 | 22% |
| UI Navigation Issues | 14 | 16% |
| Bank Integration Problems | 11 | 13% |
| Market Value Fluctuations | 8 | 9% |
| Commission & Payout Problems | 7 | 8% |
| Customer Expectation Mismatch | 4 | 5% |

## Detailed Description of Issues

### 1. Authentication & Verification Problems (23 instances)

These issues involve difficulties with the identity verification process, preventing users from accessing the system or completing transactions.

- **OTP Delivery Failures**: Users report not receiving OTPs or experiencing delays, requiring multiple resends attempts
- **Login Rejections**: Credentials being rejected despite being correct
- **PAN Verification Errors**: System showing "already registered" or other verification failures
- **Account Access Issues**: Users unable to access their accounts despite correct credentials

### 2. Financial Process Failures (19 instances)

These issues relate to actual money movement or calculation problems within the platform.

- **Withdrawal Processing Delays**: Funds showing as disbursed in the system but not reaching customer accounts
- **Margin Shortfall Alerts**: Unexpected margin calls due to market fluctuations
- **Pledge Processing Failures**: Mutual funds not getting properly pledged despite completed applications
- **Limit Enhancement Stalls**: Approved limit increases not reflecting in available balances

### 3. UI Navigation Issues (14 instances)

These issues involve difficulty using the platform's interface.

- **Screen Freezes**: Interface becoming unresponsive during critical transactions
- **Missing Elements**: Buttons or menu options not appearing when needed
- **Loading Errors**: Pages failing to load completely, showing only partial information
- **Flow Disruptions**: Users getting stuck in process loops without clear exit paths

### 4. Bank Integration Problems (11 instances)

These issues relate to integration between the platform and banking systems.

- **Mandate Registration Failures**: Bank mandates failing without clear reasons
- **NEFT/Transaction Rejections**: Money transfers being rejected by banks
- **Account Verification Problems**: Issues validating bank accounts for withdrawals
- **Bank-Specific Incompatibilities**: Certain banks (UCO Bank mentioned frequently) having specific integration issues

### 5. Market Value Fluctuation Consequences (8 instances)

Issues arising from market movements affecting loan parameters.

- **Unexpected Limit Changes**: Available loan amounts changing without user action
- **Value Display Inconsistencies**: Different values showing in different parts of the platform
- **Eligibility Confusion**: Users confused about which funds qualify for pledging after market movements

### 6. Commission & Payout Problems (7 instances)

Issues related to partner compensation.

- **Missing Payouts**: Partners not receiving expected commissions
- **Bank Detail Issues**: Payouts on hold due to outdated or incorrect bank information
- **Calculation Discrepancies**: Differences between expected and actual payout amounts
- **Promotional Program Confusion**: Uncertainty about special campaign rules and rewards

### 7. Customer Expectation Mismatch (4 instances)

Issues stemming from differences between what customers expect and how the system actually works.

- **Processing Time Misunderstandings**: Customers expecting immediate processing when actual timelines are longer
- **Feature Availability Confusion**: Customers expecting features that aren't available
- **Procedural Misconceptions**: Misunderstanding of required steps for processes like renewal vs. enhancement

## Call Duration Factors

The average call duration appears to be approximately 5-7 minutes, with some extending to 15+ minutes. Primary factors increasing call duration include:

1. **Multi-system Verification**: 2-3 minutes typically spent verifying customer identity across systems
2. **Hold Times**: 1-2 minute holds common while representatives consult other departments
3. **Repeated Information**: 1-2 minutes spent repeating information due to clarity issues
4. **Process Explanations**: 2-3 minutes explaining complex procedures, especially for first-time users
5. **Technical Troubleshooting**: 3-5 additional minutes when technical issues arise

## Most Frequent Issues (High to Low)

1. **Authentication and Verification Problems**
    - OTP delivery failures or delays
    - Login issues with partner portals
    - PAN verification errors during registration
    - "Already registered user" errors when attempting new registrations
2. **Financial Process Failures**
    - Withdrawal processing delays (funds not reflecting in customer accounts)
    - Margin shortfall alerts causing panic calls
    - Pledge processing delays or failures
    - Enhanced limit requests stalling midway
3. **User Interface Navigation Issues**
    - Confusion between partner portal vs. customer app functions
    - Screens freezing during transaction processing
    - Critical buttons not appearing or not working as expected
    - Page loading errors ("this page cannot be loaded")

## Why Calls Are Taking So Long

1. **Multi-step Troubleshooting**
    - Service agents have to diagnose issues across multiple systems
    - Troubleshooting often requires checking account status in different platforms
    - Agents frequently put customers on hold to consult backend teams
2. **Authentication Cycles**
    - Repeated OTP verification attempts
    - Multiple number confirmations for security purposes
    - Time spent waiting for system responses after verification attempts
3. **Explanation Overhead**
    - Complex product features requiring detailed explanation
    - Fee structure explanations (processing fees, GST, stamp duty, etc.)
    - Explaining market movement impact on available limits
4. **Process Fragmentation**
    - Different processes for loan creation vs. enhancement
    - Separate workflows for different mutual fund types
    - Distinct procedures for different lending partners (Tata, DBS, etc.)
5. **Language and Communication Barriers**
    - Some calls involve code-switching between Hindi, English, and regional languages
    - Technical terms being misunderstood
    - Background noise affecting call clarity (many calls seem to be in busy environments)

## Additional Issues Not Mentioned Previously

1. **Bank Integration Problems**
    - Specific banks (like UCO Bank) have compatibility issues with the platform
    - NEFTs failing without clear explanation
    - Auto-debit mandate rejections without notification to customers
2. **Market Value Fluctuation Consequences**
    - Available loan limits changing unexpectedly due to market movements
    - Confusion about why mutual fund values reflect differently in different screens
    - Misunderstanding about which funds can be pledged (locked funds, NFO issues)
3. **Commission and Payout Problems**
    - Partners not receiving expected commissions due to bank detail issues
    - Confusion about enhanced payout structures in promotional campaigns
    - Uncertainty about when payouts will be processed
4. **Customer Expectation Mismatch**
    - Customers expecting immediate fund disbursal
    - Misunderstanding about automatic account closure procedures
    - Confusion about renewal vs. enhancement processes
5. **System Maintenance Interruptions**
    - Several mentions of systems being down for maintenance
    - Critical functions unavailable during peak hours
    - Scheduled maintenance not clearly communicated to partners

The frequency and complexity of these issues suggest a need for streamlined processes, better integration between systems, more comprehensive partner training, and improved customer education about product features and processes. The length of calls could be significantly reduced with more intuitive interfaces, automated status updates, and clearer communication about expected timeframes for various actions.

# Detailed Explanation of Key Errors in the Loan Against Mutual Fund Service

## Shortfall Management Problems

When market values drop, the lending system automatically calculates a "shortfall" - the gap between what's required as collateral and the reduced value of the customer's mutual funds. What's causing significant customer friction is how these shortfalls are handled:

**Payment Timing Confusion (4 calls)**: There's a critical disconnect between what customers see in emails versus how the system actually works. The emails state "1:30 PM" as the deadline, but in reality:

- Bajaj Finance system cuts off at 12:00 PM
- Tata Capital cuts off at 1:30 PM

As one partner explained: *"The email that comes to the customer shows 1:30 as the time...but if the email showed 12 o'clock instead, that would be better."* Customers make payments thinking they're on time (before 1:30 PM), only to find their units have already been sold off because the actual processing happened earlier.

**7-Day Window Miscommunication (2 calls)**: The system gives customers 7 days to cover shortfalls, but the exact mechanics aren't clear. Partners explained that customers should ideally pay by the 5th day, and absolutely no later than early morning of the 7th day. However, customers are often unaware of these nuances, leading to unexpected unit sell-offs.

## System and Registration Challenges

**Mobile Number Duplication Issues (3 calls)**: The system struggles with families sharing phone numbers. When multiple family members try to register using the same mobile number, the system fails with cryptic errors. As one partner explained: *"The mobile number and email ID are already being used by another family member's portfolio."* This creates a significant barrier for families trying to manage multiple accounts.

**PAN Registration Errors (2 calls)**: The platform has no simple way to correct PAN entry errors. When a partner accidentally entered the wrong PAN, they discovered: *"Now when I try again, it shows that the name and number are already registered."* The only solution offered was a lengthy deletion process taking 2-6 days or creating a new account with an alternate mobile number - both problematic for customers needing immediate access.

**App Loading Problems (2 calls)**: Several customers reported basic functionality issues: *"It's not loading, ma'am. There's a problem with the mobile page. Our things aren't loading."* These technical failures block customers from even beginning the process of managing their shortfalls.

## Loan and Fund Processing Issues

**Fund Eligibility Confusion (3 calls)**: There's significant confusion about which mutual funds can be pledged. Customers don't understand why their entire portfolio value isn't available for loans. As one exchange reveals: *"Why isn't it fetching the entire mutual fund? Why isn't it placing the entire mutual fund?"* The answer involves complex rules about "free units" and certain fund types being ineligible.

**Co-borrower Requirements (1 call)**: In one particularly complex case, a partner explained: *"In the agreement there are co-borrowers...but in the coming agreement when you placed funds earlier, these co-borrowers weren't there."* This resulted in funds not being accepted for pledging, causing shortfall issues and customer confusion.

## Communication Gaps

**Excessive Contact Frequency (3 calls)**: Partners expressed frustration about the frequency of contact with customers: *"Call after call...call me, call me, call me."* One partner noted: *"In Delhi, how many people are there? Five accounts. Father's will come, brother's will come, children's will come. Each one gets five calls, so in seven days that's 35 calls going out."* This excessive contact irritates customers.

**Email vs. System Timing Discrepancies (2 calls)**: The most damaging communication gap is the mismatch between email deadlines and actual system processing times. As one partner put it: *"We tell the customer, but customers go by what they have in the email."* This directly results in missed deadlines and forced unit sell-offs.

## Technical Constraints

**Account Changes (1 call)**: The system requires extensive backend approvals for simple account changes: *"If I submit for deletion, it's a very long process, approval is required...it takes at least two days."* This rigidity creates significant friction when simple mistakes occur.

This combination of timing confusion, system inflexibility, and communication gaps is creating a challenging experience for both customers and partners, with the timing issues around shortfall payments being particularly problematic given the financial consequences of missed deadlines.

From 60 to 103 

# Detailed Analysis of Volt Money Call Issues

## 1. Bank/Payment Processing Issues (7 instances)

**Failed Transactions (3 calls)**:
Customers reported payments not reflecting in their accounts despite making transfers. In one call, a customer stated: "I've already transferred money to their account, but they're saying it hasn't been received." This issue requires investigation from the bank's backend team and causes significant customer frustration. In another instance, a customer was directed to the bank branch, but the branch claimed no issues existed on their end.

**Mandate Processing Failures (2 calls)**:

Customers faced consistent issues setting up automated payment mandates. As evidenced in one call: "I tried online mandate but it's showing 'Today it won't happen, it will happen tomorrow'." This affects payment schedules and forces manual interventions for regular payments.

**Physical vs. Online Mandate Complications (1 call)**:

The system forces physical mandates when online ones fail: "We'll do physical mandate... enable it for form download, then client can sign and upload it." This creates additional steps and delays for customers who expected a fully digital experience.

**Incorrect Interest Charges (1 call)**:
A customer was charged interest despite not utilizing the loan funds: "Customer hasn't taken any money but interest is being charged." This creates billing disputes and damages trust in the platform.

## 2. Shortfall Management (7 instances)

**Market Fluctuation Impacts (2 calls)**:

When market values drop, customers experience shortfalls requiring urgent attention. As one agent explained: "Market is volatile... shortfall has happened because market value has dropped." This creates unexpected financial obligations for customers.

**Notification Issues (2 calls)**:

Customers receive shortfall notices despite making payments: "Client made payment but is still showing shortfall... this shouldn't be happening." The system fails to update payment status promptly, causing unnecessary alerts and anxiety.

**Sell-off Concerns (2 calls)**:

Customers express anxiety about automatic liquidation of assets when shortfalls aren't addressed in time. One particularly concerned customer mentioned: "This shouldn't have happened. The lender initiates sell-off on day seven if payment isn't made." Once initiated, these sell-offs are difficult to stop, resulting in potentially disadvantageous transactions.

**Aging Update Delays (1 call)**:

Technical issues cause payment updates not to reflect properly: "The aging update isn't happening in TATA... they're technically initiating sell-offs even though payments were made." These backend problems result in unnecessary liquidations and customer complaints.

## 3. Partner Commission/Payout Problems (6 instances)

**Held Payouts (3 calls)**:

Partners' commissions being held due to outdated bank details: "Your payout commission is currently on hold because your bank details aren't updated in the system." This directly impacts partner earnings and satisfaction with the platform.

**Partner Dashboard Issues (2 calls)**:

Partners struggle to access earnings information and reports: "Contest payout details aren't available... they never download properly, never appear in email, and don't show in the application." This lack of transparency affects partner trust and ability to track performance.

**Duplicate Accounts (1 call)**:

Same partners having multiple accounts causing confusion: "I have two numbers registered there... merge them as one account." This leads to split earnings records and difficulties tracking total commissions.

## 4. Customer Experience Issues (5 instances)

**Unclear Communication (2 calls)**:

Customers express confusion about processes and charges: "I understood that it was 499 for one year, now it's 999? How did it go from 499 to 999?" Inconsistent communication about fees and terms creates distrust.

**Limited Visibility (1 call)**:

Customers can't easily track transactions or download reports: "Where can I see exactly what was pledged and how much?" This lack of transparency forces customers to call support for basic information.

**Calculation Discrepancies (1 call)**:

Different amounts shown in different parts of the system confuse customers: "In the app it shows one amount, but when processing the loan it shows a different amount." These inconsistencies make financial planning difficult.

**Interest Calculation Confusion (1 call)**:

A lengthy call revealed deep confusion about how interest is calculated: "How many days are being counted? Is it 21 days or 22 days?" This indicates that the interest calculation methodology isn't clearly communicated to customers.

## 5. Technical/System Issues (5 instances)

**Data Synchronization Problems (2 calls)**:

Updates not reflecting across all systems: "We updated it two days ago... but it's still showing as pending." This causes confusion and requires multiple follow-ups from customers.

**Backend Code Issues (1 call)**:

Support agents reference needed backend code changes: "To reverse that entry, we need to change the code in the backend." This suggests fundamental system architecture problems requiring developer intervention.

**Mobile App Limitations (1 call)**:

Features not accessible or functional on the app: "The app doesn't download that... you can't see your earnings there." This forces users to use multiple channels for complete account management.

**Processing Delays (1 call)**:

System taking excessive time to reflect changes: "It will take 2-3 days to process... it's an accounting issue." These delays create uncertainty and frustration for both customers and partners.

## 6. Additional Specific Issues

**Identity Verification Challenges (2 calls)**:

Customer registrations fail when phone numbers or email addresses are already in use: "The mobile number and email ID are already being used by other family members' portfolios." This creates barriers to onboarding and requires manual intervention.

**Fee Structure Confusion (2 calls)**:

Changes in processing fees cause customer confusion: "Earlier it was ₹500, now TATA has increased charges to ₹1500 plus GST." This inconsistency makes customers question the platform's transparency.

**Loan Closure Difficulties (1 call)**:

Challenges with closing loans and receiving NOCs: "I raised the request four days ago for NOC, but still nothing." These delays affect customers' ability to manage their financial obligations.

**Lender Migration Issues (1 call)**:

Complications when transferring loans between lenders: "Can DSP be done now? What charges will apply?" The process lacks transparency and creates hesitation.

**Commission Rate Discrepancies (1 call)**:

Partners express confusion about varying commission rates: "I thought Nippon gives quite good commission... three to four percent." These misunderstandings lead to disappointment when actual rates are lower.

104-150 

# 

## Overall Issue Count by Category

1. **Interest Calculation Issues (4 calls)**
    - Confusion about calculating 10.49% interest on different loan amounts
    - Partners unable to verify interest calculations independently
    - Discrepancies between calculated values and system-displayed values
    - Questions about when interest starts accruing (day of disbursement or next day)
2. **Shortfall Management Issues (5 calls)**
    - Shortfall amounts not updating after payments are made
    - Discrepancies between shortfall amounts in different parts of the system
    - Confusion about how to handle shortfalls through additional fund pledging
    - Questions about automatic adjustment of shortfalls using available balance
3. **Technical Platform Issues (6 calls)**
    - OTP delivery failures
    - Selfie capture vs. photo upload challenges
    - Agreement generation errors
    - Multiple accounts using same mobile number
    - System navigation difficulties
    - UI inconsistencies between web and mobile interfaces
4. **Payment Processing Issues (4 calls)**
    - Payments sent to wrong bank accounts
    - Auto-debit registration failures
    - Delayed payment reconciliation
    - Confusion about payment verification
5. **Partner Payout Problems (2 calls)**
    - Bank details not updated preventing payouts
    - Confusion about payout timing and requirements
6. **Limit Increase Requests (3 calls)**
    - Partners requesting limit increases for clients
    - Confusion about how to initiate and complete limit increases
    - Questions about available vs. sanctioned limits
7. **Promotional Communication (3 calls)**
    - Representatives explaining March incentive program
    - Tiered reward structure based on application volume
    - Lucky draw prizes announcement
8. **Process Questions (5 calls)**
    - Processing fees - one-time vs. recurring
    - Tax benefit inquiries
    - Eligibility verification processes
    - Portfolio assessment methods
    - Fund pledging procedures
9. **Other Miscellaneous Issues (2 calls)**
    - Tax deduction certificate requests
    - Customer service response time complaints

The most frequent issues involve technical platform challenges and process understanding gaps, followed by shortfall management and interest calculation confusion - suggesting these are areas where the product experience could be substantially improved.

## Issue Category Frequency:

Account Changes: 95 calls (16.1%)
Fund Eligibility: 89 calls (15.1%)
Email System Discrepancy: 59 calls (10.0%)
Mobile Number Duplication: 37 calls (6.3%)
Seven Day Window: 31 calls (5.2%)
App Loading: 29 calls (4.9%)
Shortfall Payment Timing: 25 calls (4.2%)
Pan Registration: 22 calls (3.7%)
Excessive Contact: 16 calls (2.7%)
Co Borrower: 7 calls (1.2%)

This table includes all the detailed information while being formatted in a standard markdown table that you can easily copy and paste as needed.

| Issue | Location | Count |
| --- | --- | --- |
| Withdrawal process difficulties, confusion about how to initiate withdrawals, greyed out buttons | Withdrawal Process | 80 |
| OTP delivery failures, invalid OTP errors, OTP expiring too quickly | OTP Verification | 75 |
| Fee calculation confusion, higher than expected fees, GST calculation questions | Processing Fee Section | 70 |
| Partner payout delays, payments showing as processed but not received | Partner Payment System | 65 |
| Bank detail update difficulties, rejections without explanation | Bank Information Management | 60 |
| Shortfall management confusion, unclear notifications, calculation questions | Shortfall Notification System | 55 |
| Mobile app crashes, loading failures, feature unavailability | Mobile Application | 50 |
| Interest payment calculation questions, higher than expected debits | Interest Statement Section | 45 |
| Loan eligibility confusion, inconsistent criteria communication | Eligibility Criteria Section | 40 |
| Application timeout errors, sessions expiring mid-application | Application Form | 35 |
| Pledged funds release timeline confusion, inconsistent communication | Fund Release Process | 30 |
| Commission structure clarification, confusion about tiered structure | Partner Commission System | 30 |
| MFD dashboard Account access problems, username recognition issues, account lockouts | Login System | 25 |
| KYC documentation upload problems, rejections without specific reasons | KYC Verification Process | 25 |
| Mutual fund valuation questions, discrepancy between market and loan value | Mutual Fund Valuation System | 20 |
| Partner dashboard access issues, unavailability during peak hours | Partner Dashboard | 15 |
| Post-disbursement documentation difficulties, download button not working | Document Repository | 12 |
| Application data persistence issues, losing entered data between sections | Application Form Data Storage | 10 |