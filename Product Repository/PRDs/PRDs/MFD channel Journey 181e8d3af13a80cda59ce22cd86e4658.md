# MFD channel Journey

: Naman Agarwal
Created time: January 20, 2025 11:59 AM
Status: In progress
Last edited: March 18, 2025 3:22 PM

Goals 

- Reduce RM dependency per application by 50%
- Increase application within 20 min TAT to 20%

## Problem statements

![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png)

![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png)

### **Portal Layout**

1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them.

### **Registering Customers**

1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility."

### **Fetch**

1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility).
2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number.
3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue.
4. We don’t show in-eligible funds in the app journey.
5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 
6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey.

### **Offer Page**

1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page.
2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds.
3. MFDs want to understand why certain funds are ineligible and call RMs for clarification.
4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP
5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 
6. Approved ISIN tool, approved list of isin share to aMFD

### **KYC**

1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's Aadhaar and OTP, causing delays. This lack of awareness makes it difficult to coordinate with customers, who must be available, when the application begins.
2. MFDs need to know the required documents beforehand to avoid delays in retrieving the Aadhaar number.

### **Selfie Link**

1. MFDs must be physically present with the customer or send them a web/app link for live photo capture, causing challenges with customer availability and requiring extra effort to explain the process.
2. MFDs are often unsure about the live photo step and end up calling RMs for guidance. MFD don’t read the text or find the Graphics clear enough.
3. Camera permission issues arise when MFDs or customers haven’t granted access in the browser. If the permission popup is blocked, no notification is shown.
4. MFD uploads live photos that are not matching the Digilocker image. we need to make it clear that the Photo should be of the person with Aadhar.

### **Additional Details**

1. MFD has the data but they have to wait for KYC and selfie to complete for This step can be pre-filled by the MFD.
2. Mother's name is often unavailable in the documents MFDs have on hand, increasing customer dependency and application time.

### **BAV**

1. Indicate that the bank account used should have sufficient funds, must not be a joint account, and should match the applicant’s name.

### **Mandate**

1. Customers are confused by the fixed ₹10 lakh mandate limit - small loan borrowers find it too high, while large loan borrowers misinterpret it as an upfront payment requirement. We need to explore setting mandate limits equal to individual loan amounts.
2. Some mistakenly believe they need to pay immediately because the mandate flow resembles a payment process.
3. Customers attempt Aadhaar-based mandates even when their bank account isn’t linked to Aadhaar.
4. Compatibility issues with certain bank accounts, like joint and company accounts

[Mandate failure analysis](MFD%20channel%20Journey/Mandate%20failure%20analysis%20185e8d3af13a807e8a66c553c54ce362.md)

### Pledge

- We want to Pledge funds as early as possible to get the Buy-in from the customers

[B2B2C Journey Approach ](MFD%20channel%20Journey/B2B2C%20Journey%20Approach%201a7e8d3af13a80fa839ff2145ee15edf.md)

[Customer vs MFD](MFD%20channel%20Journey/Customer%20vs%20MFD%201ade8d3af13a80db9004d15ffda8d14d.md)

# Potential solutions

Phase 1 

- Show all ineligible funds in the LAMF journey with Reasons of the in eligibility on a fund level.
- Make MFC fetch step as Register and Condense first steps to Offer page to 3
    - Enter PAN and Mobile number
    - OTP
    - Offer page (After waiting )

## **Registering Customers**

Problems in Registering Customers for MFD 

1. MFD has different types of customers that want to check the offer or want to take a loan directly 
2. NEW MFD finds it difficult to navigate the Dashboard to add a customer and then resume their application. 

1. User stories 
    1. MFD can have two types of customers 
        1. With Intent to create Application - MFD wants to directly move to Application
        2. With the  Intent to understand the offer - MFD wants to check the limit

1. We should have one page for all the customers added by MFD instead of pending and completed applications 
2. We should have a Check limit of 15 seconds with the History of the Fetch below for quick access

Register customer

| Current ****journey  | **Proposed** Journey |
| --- | --- |
| Add Phone number  | Add phone number |
| OTP | Add PAN number |
| Email | MFC summary fetch OTP |
| Email SSO or OTP | Offer page |
| PAN |  |
| DOB |  |
| Verify PAN |  |
| Fetch  |  |
| OTP |  |
| Unlock limit |  |
| Set Limit |  |
| Offer page |  |

Register Customer from MFC fetch 

MFD could register customers fromthe  Customers page or Check Limit page 

Customers page 

- Add New Customer

Check limit 

### **Application**

- Listing required documents before initiating the application.
- Reordering steps to complete non-customer-dependent tasks first, followed by customer-dependent steps.
- Allowing individual steps to be separate, shareable, and re-triggerable for completion.

- Problems
    
    ## **Fetch**
    
    1. MFD want to know why some funds are not visible or eligible after fetch 
    2. RMs have to spend 10-15 min getting MFD to pull MFC detailed fetch and explain fund by fund the reasons of non - eligibility.
    2 fetch points: Check eligibility &  CAMS/KFIN fetch - MFDs call RMs to explain the difference shown in the limit from both the fetch points
    3. MFDs get confused between multiple options to Fetch  
    4. The process to Change the Number to fetch Funds is unintuitive to MFD
    
    ## Mandate
    
    - Customers are concerned about the 10 lakhs Mandate amount.
    - People have general concerns about Mandate such as do they need to pay something at that step.
    - The overall mandate failure rate is 27.15% (1,168 failures out of 4,302 total mandates) for  DSP (since inception).
    
    ## **Photo verification**
    
    - MFD mentions to RMs
        - What needs to be done here
        - Is there an alternative
        - How to take a selfie
    - The camera permission popup is disabled, causing the step to be stuck.
    - Photo verification requires either the customer to be present with the MFD or They have to complete the step using Volt Web or the mobile app journey.
    
    ## KYC documents
    
    - We need to mention a List of documents that MFD needs to Keep Handy before starting the application like an Aadhaar card.
    - **Incoming Call summary from RM**
        - Data for 21, and 22 Dec incoming calls
            
            
            | Category | Sub-Category | Count | Percentage |
            | --- | --- | --- | --- |
            | New Application | Assisted Journey | 275 | 30.1% |
            | New Application | Issue In Journey | 136 | 14.9% |
            | New Application | FAQs | 121 | 13.2% |
            | New Application | Lender Change | 42 | 4.6% |
            | Post Loan | Withdrawal Issue | 65 | 7.1% |
            | Post Loan | Repayment Issue | 52 | 5.7% |
            | Post Loan | Unpledge/Unlien Query | 33 | 3.6% |
            | Post Loan | Enhancement Query | 33 | 3.6% |
            | Post Loan | Renewal | 25 | 2.7% |
            | Post Loan | Mandate Issues | 5 | 0.5% |
            | Others | - | 120 | 13.1% |
            | Payout Related | Payout Related | 6 | 0.7% |
            | **Total** |  | **914** | **100%** |
    
    - MFDs are Lost after onboarding and have to be Guided By RMs to create applications. The IA is nonintuitive as MFD are unable to understand when an Application is in Pending or Completed.
        - Partner Activation data
            
            
            | Total Empaneled Partners | 14,255 |
            | --- | --- |
            | Active Partners | 2567 |
            | Activation Rate | 18.00% |
            | **TAT Distribution Activation** | 96 days |
            | Same Day (0) | 314 |
            | 1-7 days | 601 |
            | 8-15 days | 195 |
            | 16-30 days | 217 |
            | 31-60 days | 237 |
            | 60+ days | 1003 |
            - AHT of Ashik ~ 30 min
    - We are getting a lower limit due to Users having multiple numbers
        
        
        | **Eligible Portfolio /Total fetched portfolio %** | **portfolio_count** |
        | --- | --- |
        | **100%** | 217896 |
        | **90-99%** | 39957 |
        | **80-89%** | 23727 |
        | **70-79%** | 17478 |
        | **60-69%** | 14159 |
        | **50-59%** | 12844 |
        | **40-49%** | 9843 |
        | **30-39%** | 8975 |
        | **20-29%** | 8861 |
        | **10-19%** | 8909 |
        | **Below 10%** | 88537 |
        | 78.80% (Overall) | 451310 |
        
        | **category_name** | **portfolio_count** | % |  |
        | --- | --- | --- | --- |
        | **0 mobile numbers** | 272423 | = |  |
        | **1 mobile number** | 265902 |  |  |
        | **2 mobile numbers** | 155333 |  |  |
        | **3 mobile numbers** | 8114 |  |  |
        | **4 mobile numbers** | 72 |  |  |
        | **5+ mobile numbers** | 0 |  |  |
        
    - MFDs Use Mobile apps and we don’t have an IOS app
        
        
        | platform_category | Unique Users | Unique Partners |
        | --- | --- | --- |
        | VOLT_MOBILE_APP   | 2028  | 225 |
        | VOLT_PARTNER_ANDROID_APP | 422 | 275 |
        | VOLT_WEB_APP | 3095     |  236 |
        | Users with Both Platforms | 335 |  |
        | Android-Only Users | 87 |  |
        | Users Preferring Android | 136 |  |
        | iPhone_Users_With_Android_App | 43 |  |
    
    - Notes from Lalit
        - Benchmark with AMCs and familiar journeys (e.g., IFA Express).
        - Add MFD requirements like line unification details in steps.
        - Explore simplifying Fetch and Pledge to 2 steps.
        - Create an MFD dashboard for application stage (Eg KYC pending -2).
        - Identify issues in steps like Pledge and KYC where MFDs depend on customers.
        - Redesign customer flow from add to loan completion.
        - Gather insights on MFD mobile usage.
        - Enable async steps for non-customer-dependent tasks.
        - Highlight issues faced by MFDs during applications.
        - Allow MFDs to complete journeys in one call with customers.
        - Get feedback from the Redvision team. - done
            
            **Redvision Priorities**
            
            1. Volt journey is performing well.
            2. Add MFD controls: select lender, limit management, photo verification  and DigiLocker link.
            3. Enable disbursement by MFD with Investor consent.
            4. Provide payouts (commissions) API. We had a API enabled 6 months ago 
            5. Redvision will Integrate with MFC CAS summary API.
            6. Track where users drop off and enable them to resume their journey.
            7. Optimize offer pages with 3-year average forecasts.
            8. Get APIs to get the fund performance, then Highlight cost savings
        - Display pending customer tasks on the MFD dashboard.
        - Collect detailed technical issues faced by MFDs.
        
        [Product log issues](MFD%20channel%20Journey/Product%20log%20issues%2018fe8d3af13a80289841d8ac4e6a2add.md)
        
    
    ## MFD Journey issues
    
    ## Sign up
    
    - Signed up but forget which number used to Signup
    
    ## Onboarding
    
    - MFDs want to understand the Payout details
    - Password not set initially
    - The current user flows on the MFD dashboard is confusing to the MFD and they are lost , requiring RMs to spend time to move the applications ahead
    - MFD first tries to Register customer due the Register customer being the first action in the centre of the dashboard.
    - Incases of the MFD employees accessing the portal Employees need to ask for the OTP from the main person to see account.
    - If a MFD has multiple accounts then they can’t see their applications together. MFD usually have 2-3 numbers
    
    ## Account management
    
    **Login**
    
    - Logging into the Volt Dashboard via the website requires remembering which phone to use.
    - Employees are unsure about the login process.
    - Demo videos are outdated and contribute to confusion.
    
    **Account Changes**
    
    - Changing phone numbers or email IDs is not intuitive.
    
    **Customer Addition**
    
    - MFDs check customer credit limits, but using TATA as a lender results in lower limits than the DSP potential.
    
    ## **Customer Application**
    
    **Offer Page**
    
    - MFDs want the option to select lenders.
    - Applicants are unclear of the benefits of LAMF compared to Redeeming funds
    
    **KYC**
    
    - **Live Photo:** Collecting live photos from users is time-consuming and challenging.
    - **Additional Documents:** Fields like "Mother’s Name" are difficult to fill due to insufficient document availability for MFD.
    - MFD need to told what document to prepare to reduce time
    
    **Pledge**
    
    - Pledging fails for some of the funds.
    - ~~If a fetch was done a few days prior, MFDs close the error popup instead of refreshing the portfolio. RMs often need to guide them back to refresh.~~
    - NAV discrepancies between DSP AMFII and Finflux cause differences in initial and logement limits.
    - ~~Pledging less than ₹25,000 is not allowed .Issue specific to Shortfall~~
    
    **Mandate** 
    
    - Mandate
        - Bank issues
        - DC expired, not valid
        - Net banking not available
        - Bank not accepting Mandate
    
    **Portal Layout**
    
    - Update the "Complete Application" CTA in pending applications to "Resume Application" to better reflect user intent.
    
    Send link 
    
    - If the user Click on Sign in or download app then the customer is not assigned to MFD.
    
    Learning 
    
    - MFD are not aware of the SOA and Holding account statement is available in dashboard
    - MFD are not aware of finding the Payout details
    
    Tech issues 
    
    - Cache issues
    - Slow performance
    - Error 400 at KYC step (+917507862591 MAHESH JUPALLI)
- Define
    - MFD struggle with customer management due lack of clear flow from add customer to application completion.
    - MFD want to have the details on the Why some funds are not visible or eligible and current process require RM to explain.
    - MFD is dependent on customer availability to process application
    - Lack of clear visibility on requirement and remaining Steps for an application
    - MFD want to be more in control as they have to make discions on behalf of the customer
    - Basic use case like unpleadging and  Getting disbursal to customer account is Unclear to MFDs
- Develop
    - MFDs don’t think in terms of loan applications they think in terms of Customers. We shall change the flow to reflect the same
    
    Requirements 
    
    - MFD shall have one page to Add and track all their customers.
    - MFD shall be able to save customer details without triggering OTP at first.
    - MFD shall be able to track and take action of the stage of the customer application
    - MFD shall provide the PAN and phone number to add a customer
    - Customers could be in different stages like
        - No limit fetched - CTA { Check limit , see details }
        - Limit Fetch - CTA {Continue loan application, see details  }
        - Loan Created - CTA { Manage loan, see details  }
        - Loan Completed - CTA { Renew application , See Details }
    - MFD shall see the entire customer details on the customer details page
    - MFD shall find it easy to navigate between application steps and change the details as required
    - The Older applications for the customer will be saved within the customer details page
    
    MFD Jobs to be Done
    
    - Empanel on volt
    - Login to the Volt platform
    - Register customer
    - Check customer eligibility
    - Create Customer application
    - Manage customer loan
    - Manage Shortfall or interest due
    - Foreclose account
    - Repayment on customer's behalf
    
    Domains 
    
    - Dashboard
        - Dashboard with Quick CTAs
        - Marketing cards
        - Quick stats on the AUM, Customers
        - Context-aware CTAs for the pending Applications and Alerts for customers for shortfall or interest due, Mandate issues
    - Customers
        - Consolidated view of all the customers for the MFD
            - Consolidate view will show all the customer MFDs have checked or added
        - Customers Detailed View
    
- Scenarios
    - MFD receives requests from Customers
    - MFD logs in to VOLT - Issues
    - MFD checks the Check limit
    - MFD enters the PAN and mobile number
    
    PAN 
    
    - Invalid
    - No Funds
    
    Mobile Number 
    
    - Invalid
    - No OTP
    - No funds
- If there are no funds on the number then the customer has to change the number with the Model
- We can check the PAN for correctness and Funds

- The MFD will have to add OTP from the customer
- The MFD shall see the Waiting screen for the MFC fetch
- Then they will see the Offer page
- on the offer page
    - Limit found
        - If Funds are all eligible then no change
        - If some portfolios have Funds which are registed to different number then we need to move them to the Registered number. (Amount of funds, API for changing Fund’s numbers)
        - 
    - Limit not eligible
    - Get more portfolio

### Suggested changes to the MFD portal dashboard

# VOLT Partner Portal (Doc)

Volt partner portal provides MFDs access to Volt LAMF products with a powerful CRM to manager customers and their Credit application-related services. 

Volt provides the complete lifecycle management of a LAMF application for its MFD partners 

Requirement for MFD partner portal access

- Valid Indian Phone Number
- ARN number(optional)   [https://www.partners.assetplus.in/post/what-is-an-amfi-registration-number-arn](https://www.partners.assetplus.in/post/what-is-an-amfi-registration-number-arn)
- E-mail ID
- Mobile or Laptop device with Internet connection

Portal availability

- Desktop Web (Recommended), Mobile web, Android app, IOS app(upcoming)
- Web access: 24*7
- Support: 10 am to 7 pm Mon to Sat. (Bank holidays applicable)

Portal features 

- MFD Volt Partner account
- Customer Credit application management
- IFA tools
- Commissions Dashboard

## MFD Volt Partner Account

### Registration

Registered partner will be Empanelled with Volt 

Mode of registration 

- Volt partner dashboard
    - Go to https://www.voltmoney.in/partner
    - Choose Empanel with us
    - Fill in the Basic contact details (Basic phone number verified by OTP)
    - Fill in your full name, email ID, city, and company name.
    - Provide ARN number (optional)
- Through Create Partner Account APIs

**What does registration provide?**

Registration provides the New Partner with a unique Partner_id. This ID is used to track the Application created by Partner for the Customer Credit management and commission tracking

- Partner account ID
- Referral code

**How will the Login work with Multiple phone numbers?**

- Currently, we only provide one number to access the account and for the MFD it acts as their user ID as well

How will the Login work for Multiple Employees?

How will the login work for partners registered to Volt through other Platforms?

- NEW:- We allow Users to add a Unique USER ID and Password after they have registered
- Making ARN mandatory

### Onboarding

We want to restructure the Dashboard a step a step-by-step onboarding of MFD and an intuitive flow 

MFD Dashboard: Levels of Engagement and Tasks

**Action step:** Use this revised structure to streamline MFD engagement tracking and ensure clarity in reporting and task allocation.

| **Task Category** | **Specific Tasks** | **Key Features/Actions** |
| --- | --- | --- |
| **Onboarding** | - Phone number and account creation | - Capture ARN number, initiate reach-out calls |
|  | - OTP and password setup | - Ensure GSTN information is collected |
| **Learning Tools** | - Tutorial for LAMF sections | - Highlight CTA for ease of navigation |
| **Customer Registration** | - Register a customer | - Provide CTA at the top for quick access |
|  | - Understand LAMF |  |
|  | - Check credit limits (15 sec) |  |
| **Application Process** | - Start a new customer application | - Track pending applications |
|  | ~~- Encourage customers to download Volt application and share the download link~~ |  |
|  | - Complete the first application (guided assistance available) |  |
| **Credit Management** | - Register additional customers | - Ensure subsequent applications are completed |
| **Account Management** | - Assist with first payout |  |
| **Engagement** | - Encourage MFDs to refer other MFDs |  |
| Credit servicing  |  |  |

---

### Partner Accounts

A partner once registered has their Partner account in Volt. Use account management features for availing commissions, change details, change access rules 

Personal Details 

- Change in the Mobile Number
- Change in the Email ID
- ARN number

Commission details 

- PAN details
- Company Bank account number with IFSC
- NAME as per Bank account
- Bank account Type - Individual /Corporate/ Joint
- GSTN -  Optional
- Company Name - (Pre-filled )

Access details 

- User ID
- Password

### Partner Commission

Payouts 

## Customer Credit application management

### Add Customer

Provide basic details of the customer to get the journey started 

- Add a user phone number
- Add user PAN number
- Add Customer Name

Process after Customer Add

- Dedupe check
    - User has no prior account
    - The user has a prior account with Volt without a partner show Platform with application status. Take user OTP. - *This is to reduce a lot of MFD calls to change attribution with the consent ofthe  user*
    - User has a prior account with Volt with a partner ID, then shows thatthe  customer is already registered. - RMs will have to change basis the Situation
    - The user has an active application - then MFD Will not get the commission application, without connecting with RMs
- Select customer Type (WIP)
    - Retail
    - business
    - HNI
    - Family

### Check customer limit

- MF Central Limit fetch - Detailed view
    
    We show all the funds the user has Associated with the PAN number. If the MF units are associated with two Numbers then - Show how to merge them 
    
    - MF Central Service Request Hyperlink
- We want to show the Exhaustive list of folios to the Customer
- The folio linked to the Entered number is eligible for the Limit.
- MFD should be able to see the folios fetch and why they are not being counted towards the Limit Fetch.
- The initial limit is fetched using Tata as a lender as of today we will be moving to DSP

The mobile number to check Funds, the Applicant's phone number, andthe  number with assets could be different.

- Here MFD can enter a number

Credit application journey 

Steps 

MFD

- KYC_PAN_VERIFICATION -
- CHECK_CUSTOMER_ELIGIBILITY
- KYC_ADDITIONAL_DETAILS
- KYC_SUMMARY
- CIBIL_CHECK
- BANK_ACCOUNT_VERIFICATION
- TATA_MANDATE
- ASSET_PLEDGE
- SIGN_DESK_ESIGN

user required 

- MF_FETCH_PORTFOLIO
- MF_PLEDGE_PORTFOLIO
- KYC_DOCUMENTS
- KYC_PHOTO_VERIFICATION
- TATA_MANDATE

OTP required 

- Phone number for Login
- Email OTP
- Fetch (MFC, KFIN, CAMS)
- KYC
- Mandate (Debit card, Netbanking , Aadhar-2)
- Pledge - 2
- Agreement -1

Questions

- % of applications coming from Valid Or available ARN

### Complete Customer application

### Disbursement

### Repayment

### Foreclosure

### Shortfall / Fines

## Rough

### **RM Feedback & Onboarding Issues**

- Users prioritize payout, loan amount, EMI, and tenure (preferably one year).
- Concerns: Volt’s existence, charges, joint accounts (business/family), GST billing, selfie link, multiple MFD numbers.
- Flow Issues:
    - Eligibility check should come before customer registration.
    - Pending applications should prevent duplicate registrations.
    - Save and pre-fill phone numbers on the portal.
    - Simplify "Continue loan application" step.
- KYC: Mother's name availability, borrower availability constraints, fund sourcing (KFIN, etc.).

### **Enhancements & Dashboard Fixes**

- Clearer CTA for managing limits, statements, and customer details.
- MFDs struggle with login due to multiple phone numbers.
- Need an option to update phone numbers (requested frequently).
- Charges table should be added to the dashboard.
- Refresh customer portfolio feature.

### **MFD Account & Customer Management**

- **Account Creation & Management**: Sign-up, onboarding, login, phone number handling.
- **Customer Flow**:
    1. Check credit limit → Get loan → Complete application
    2. Steps: Phone number, PAN, DOB, credit check, KYC, pledge, mandate, agreement, BAV.
- Issues: PAN verification constraints, background verification, customer dependency (OTP, KYC, selfie, etc.).
- Stepper with links for better navigation.

### **Scenarios & Open Issues**

- PAN verification alternatives (MFC fetch).
- Eligibility & fund lien concerns (locked ELSS).
- Process clarity for admin actions (funds, RTA fetch, number change restrictions).
- MFD Jira tickets pending.
- Agreement delays.

### **Volt Partner Portal PRD**

- **Goals**: Reduce RM dependency, improve application speed, increase MFD activation.
- **Features**:
    - Unified customer dashboard
    - Streamlined application with async steps
    - Enhanced fetch & fund eligibility explanations
    - Intelligent offer system (DSP-first calculation)
- **Technical Needs**:
    - Multi-tenant support, sub-3s response, 99.9% uptime, mobile optimization
- **Success Metrics**:
    - 50% RM dependency reduction, 20% of applications in 20 min, 40% faster handling

### **Outstanding Questions & Issues**

- Pledge process post-fetch: Try with 5% applications?
- Credit limit misunderstanding: Users expect full disbursal.
- BAV Issues: Joint holders, salary/current accounts, must be savings.
- Mandate issues: ₹10L limit, STP handling, CAM pledging.
- Technical issues: APR not explained, phone verification (black screen), penny drop failure.
- Jio Finance interest rate: 9.99%.
- Fund mismatch between CAMS & KFIN.

Details needed For a Credit application 

| Details | MFD | Customer  | RM | Required |
| --- | --- | --- | --- | --- |
| P1 Phone number  | Number | OTP  | - | yes |
| Email verification | Email | OTP | - | optional for comms |
| PAN  | PAN card |  | - | can verify in the MFC fetch step  |
| DOB | PAN card |  | - |  |
| Fetch mobile number | P2 number, Merge Folios | OTP |  |  |
| Fetch step |  | OTP | Fetched fund details  |  |
| Set limit | yes |  |  |  |
| Accept offer | Yes  |  | Change lender |  |
| KYC | Aadhar | OTP, PIN |  |  |
| KYC summary  | Yes |  |  |  |
| Additional details  | Marital status |  |  |  |
|  | Qualification |  |  |  |
|  | Father’s name | mother’s name (DSP) |  |  |
|  | Pourpose |  |  |  |
|  | Occupation |  |  |  |
|  | Source of income |  |  |  |
|  | Income range |  |  |  |
|  |  | Live selfie |  |  |
| BAV | Bank account  |  |  |  |
|  | IFSC |  |  |  |
|  |  |  |  |  |
| Mandate | DC | OTP |  |  |
|  | Net banking details  | OTP |  |  |
|  |  |  |  |  |
| Pledge |  | OTP |  |  |
|  |  |  |  |  |
| Agreement  |  | OTP (Tata) |  |  |
|  |  |  |  |  |
| Document upload  |  |  |  |  |
|  |  |  |  |  |
| First withdrawal |  |  |  |  |

[MFD Login data](MFD%20channel%20Journey/MFD%20Login%20data%201aee8d3af13a805abb1cfad51a286260.md)