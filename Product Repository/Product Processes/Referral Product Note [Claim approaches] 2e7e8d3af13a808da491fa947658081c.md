# Referral Product Note [Claim approaches]

## **Background and Context**

- 
    - Who is facing the problem (users, internal teams, partners)
        - **Existing Volt users (borrowers / opportunities)**
            
            Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same.
            
        - **New potential users (referees)**
            
            They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. 
            
        - **Business team**
            
            Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users
            
    - What is the challenge that they are facing? What is broken today?
        - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more.
        - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism.
        - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner.
    - Why is it important? or What is getting impacted?
        - **High CAC** from paid channels continues to scale.
        - We miss out on **trust-led growth** from existing users.
        - Drop-offs in referee journey remain high due to lack of motivation.
        - Poor operational scalability risks future campaign launches.
        - Inability to experiment with referral-led growth limits topline impact.

---

## **1. Problem scope**

### In scope

- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

### Out of scope

- 
    - Call out on items out of scope
    - Rationale for exclusion

---

## **2. Success Criteria**

- 
    
    Top 2-3 **clear outcomes that we are looking to achieve**.
    
    - Key success metrics
        - First 1000 referral signups
        - # of successful referrals (loan account opened above Rs.25000)

---

## **3. Solution Scope**

### Solution overview

- 
    
    We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program .
    
    The solution includes:
    
    - Backend-driven eligibility and program rules
    - Clear user-facing referral journeys
    - Lifecycle-based nudges
    - Automated referral and unlocked rewards tracking
    - Seamless reward claim journey
    - Ops and LSQ visibility

### Detailed solution scope:

- 
    
    Mentioned are the pointers below covered in the solution scope:
    
    | **Description** | **Details** |
    | --- | --- |
    | Referral eligibility | Backend determines eligibility of user for referral program using parameters like: platform, user type (opportunity/ borrower), step of journey, program start date, program end date, reward conditions, priority of active referral program etc. |
    | Referral discovery | Different modes of user discovery for referral program:
    - Touchpoints in LOS and LMS journey
    - Outreach via channels like Whatsapp, SMS and PN |
    | Referral sharing | Unique referral link shareable with message template via WhatsApp, SMS, other sharing apps in mobile via app, and copy link method (web + app) |
    | Attribution | Referee attribution with first Sign up via referral link |
    | Progress tracking | Referrer can view and track successful referrals and referee’s progress in the loan journey (for in-progress referrals) |
    | Rewards (cash) | Cash reward will get unlocked both for referrer and referee on referee’s successful loan application journey above Rs. 25000 within given validity of referral program launch. |
    | Milestones | Physical rewards unlocked as bonus at different milestone points configured (5 and 25) |
    | Reward validity | Common Expiry date for claiming all rewards. |
    | Claim and Payout | - Capturing bank account details of the user, manually verifying it, and disbursing cash amount with updating status in DB.
    - Address capturing via Google form for physical Milestone rewards and delivering the reward as per set SOP |
    | Nudges | Event-based nudges across WA, PN, SMS |
    - **Core happy path**
        - User becomes eligible and sees referral entry point.
        - User shares referral link.
        - Referee signs up and progresses through loan journey.
        - Referrer is able to track the journey of the referees post signing up.
        - Referrer is able to nudge them when needed to complete the loan journey
        - Loan account is opened by referee above given limit.
        - Rewards unlock for referrer and referee which are trackable with current status of reward.
        - Manual Payout of Claimed Cash rewards with manual verification of bank account details submitted by users and updating status in the DB; Milestone rewards fulfilled as per address information collected.
    - Key **Terms & Conditions** for 1st referral program**:**
        - Minimum loan amount of the first time loan account opened by referee should be Rs 25,000/- (Variable in system)
        - Cash rewards need to be claimed within 90 days post the reward is unlocked inside the Volt Money app.
        - Referrer should be a signed up user on Volt Money (on platforms - B2C, B2B PhonePe redirection, B2B2C users).
        - User should not be already signed up with Volt Money or its associated partners at any previous point of time for being eligible as a referee.
        - Referee needs to complete the loan journey within validity period of the referral program. (31st March 2026) [Variable in backend]
        - Referral reward is eligible for LAMF OD product account openings only (Not LAS OD or LAMF/LAS Term loans)
        - Reward program is valid for a period of 3 months from start (Let's say 1st Jan'26 - 31st Mar'26, This will help to create user urgency for referrals by making the reward program time bound)
        - If a referee has signed up via multiple referral links, then successful referral attribution will be valid only for first link through which he signed up.
        - If a new referral program with new rewards conditions begin from a new date, then both referrer and referee will be attributed to new terms & conditions applicable for the program.

---

## **5.  High level s***ystem, user or process flow*

- 
    
    
    **A) Referrer User flow: Discovery → Share → Track → Unlock reward (Referee loan account opening success) → Claim reward**
    
    - **Discovery:**
        - **Entry point:**  User/ Referrer is able to access the referral program via:
            - Discovery touchpoints configured in both LOS and LMS journeys as mentioned in the [sheet](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=0#gid=0).
            - External channel nudges and outreach for referral program via Whatsapp, PNs and SMS, exhaustive framework for which is mentioned in the [sheet](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=0#gid=0)
    - **Landing page:**
        
        Landing page of the program has the following components:
        
        - Hero banner
        - Steps for referral (How does the program work?)
            - Share link with friends
            - They open loan account above Rs. 25000
            - Both you and your friend win rewards
        - Channel support for Link sharing
            
            **App (Android and iOS)**
            
            - Primary method: Whatsapp share
            - Secondary method: Other sharing channels/ apps present in device via native sheet opening (Copy link, SMS, gmail, Meta platforms etc.)
            
            **Web:**
            
            - Primary method: Share via Whatsapp web link redirection
            - Secondary method: Copy link to clipboard
        - [Tracker](Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) for referrals and rewards (with entry point for detailed tracking of all referrals and rewards unlocked with current status)
        - Milestone levels tracker with reward (no. of completed/ total milestone steps)
        - T&C link
            
            [Key **Terms & Conditions** for 1st referral program**:**](Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) 
            
        - [Validity period of r](Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md)eferral program
        - Validity period to claim rewards
    
    - **Tracking mechanism details:**
        
        Referrer shall be able to track:
        
        - **Referrals**
            - Successful referrals (Success: Referees who successfully opened loan account above Rs. 25000)
                - Count
                - List
            - In progress referrals (In progress: Opportunity created but loan application NOT completed)
                - Count
                - List
                - Status for each referral in the list (Values to be supported in a linear progression format are:)
                    - Signed Up
                    - KYC Completed
                    - Application completed
                - Nudge (”Follow up”) action (CTA) beside each “in-progress” referral to send a follow up message via Whatsapp.
        - **Rewards**
            - Tracking of Unlocked rewards (across their lifecycle): Rewards which get unlocked on completion of each successful referral.
                - Overall view of ‘Total rewards’ (Sum of cash amount + Physical) unlocked  for ‘Cash + Physical’ rewards. The details will be subdivided into following 2 sections:
                    1. Total ‘Cash rewards’ (Sum of cash amounts) earned view which are in “[active](Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) “status with “Claim” action. This will further include:
                    - List of individual cash reward amounts unlocked with **date** of unlock.
                    - Current status of each individual reward unlocked
                        - Active: The rewards which are active but not yet claimed.
                        - Processing: Rewards which are already claimed but not settled
                        - Transferred: Rewards which are settled
                        - Expired: Rewards which are already expired and no action can be taken on them.
                        - Failed: Rewards corresponding to which transaction failed
                    
                     b. Milestone (Physical) rewards section with action to claim for “active” status. This will also include:
                    
                    - List of physical rewards unlocked with date of unlock on completing milestone.
                    - Current status of physical reward:
                        - Active
                        - Processing
                        - Transferred
                        - Expired
                - Tracking of payouts/ settlement of claimed rewards. There shall be a separate section which shall track cash rewards payout transaction details:
                    1. Cash rewards payout list: This will contain list of all transactions processed with total amount, date and transaction status:
                        1. Success
                        2. Failed
            - Tracking of locked rewards:
                - View of the next reward that is locked (Cash/ physical) and number of referrals needed to unlock it.
            - Milestone rewards and journey progress tracking:
                - Overview of number of steps completed out of total steps in the referral milestone journey present.
                - No. of steps needed to unlock milestone reward.
            
        
        **Claiming journey and mechanism:**
        
        **Approach 1:**
        
        1. Cash reward claim:
            - When a reward gets unlocked and is of status “active”, the claim action gets activated.
            - Based on availability of bank details of the user (referrer/ referee):
                - **Case 1:** If bank details of the user are not available with Volt, then there will be a placeholder trigger for capturing the following users’ bank details:
                    - Bank A/C No.
                    - IFSC Code
                    - Beneficiary name
                - **Case 2:** If bank details of the user already exist with Volt, then the bank details will be pre-filled in the placeholder trigger.
                    - If user enters another bank account number then in the “referrals” table bank account, beneficiary and ifsc details will be updated.
            
             On user confirming,  BE will update the bank account details against referrer in “referral” table in DB and a nudge will be triggered communicating successful “processing” of rewards by certain date (05th July) [both in-app and external].
            
            - **Admin action:**
                - Business/ Ops team can download the latest report of cash rewards to settle based on the cycle of payouts decided as per SOP.
                - The downloadable file should have the following fields from BE with unique entries:
                    
                    
                    | account_id | referrer_id | referrer_referee_id | reward_ids (array) | bank_account_no | ifsc_code | amount | beneficiary_name | bank_account_verified | transaction_status | reward_type | address | pincode | UTR | delivery_status |
                    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
                    |  |  |  | {RWD110, RWD 111, RWD 112} |  |  | 3000 |  |  |  |  |  |  |  |  |
                - After business team approves the detailed sheet based on reward_type as “cash”, analytics team will run script as per the current process to verify the bank accounts via penny drop for the accounts which are not verified with Volt already.
                - The same sheet with verified accounts will be shared with Admin/ Ops to manually process the payment.
                - After processing of payment, a reverse sheet of the format below will be shared with the ops team to map the transaction status against the main downloaded sheet via admin action:
                
                | UTR | bank_account_no | ifsc | beneficiary_name | status | amount |
                | --- | --- | --- | --- | --- | --- |
                - Sheet of the same format as downloaded, shall be uploaded again via admin action for backend to consume:
                
                | account_id | referrer_id | referrer_referee_id | reward_ids (array) | bank_account_no | ifsc_code | amount | beneficiary_name | bank_account_verified | UTR | transaction_status | reward_type |
                | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
                |  |  |  | {RWD110, RWD 111, RWD 112} |  |  | 3000 |  |  |  |  |  |
                - Backend after consuming the sheet will update the status against each reward in the “rewards” table in DB to status “Transferred” or “Failed”
                - Notification will be sent to the user as per the [nudge](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=1824995158#gid=1824995158&range=A1:H7) framework via external channels (Whatsapp), along with in-app and web nudges.
                
            
            b. Physical milestone reward:
            
            - For a physical milestone reward with status: “active”, claim action will get activated.
            - Placeholder will be triggered to capture address details of the user:
                - Address
                - Pincode
            - The address details are passed to BE which shall be saved in the “referrals” table and and a nudge will be triggered communicating successful “processing” of rewards by certain date (05th July) [both in-app and external].
            - **Admin action:**
                - Business/ Ops team can download the latest report of physical rewards to settle based on the cycle decided as per SOP.
                - The format will be same as discussed in the cash payout table where admin can separate the physical rewards via reward_type parameter.
                
                | account_id | referrer_id | referrer_referee_id | reward_ids (array) | bank_account_no | ifsc_code | amount | beneficiary_name | bank_account_verified | transaction_status | reward_type | address | pincode | UTR | delivery_status |
                | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
                |  |  |  | {RWD110, RWD 111, RWD 112} |  |  | 3000 |  |  |  |  |  |  |  |  |
                - Once the business team approves, as per SOP set, fulfilment with respective vendor will be done.
                - Post fulfilment is successful, Ops team will manually update the sheet with delivery_status column and upload it in the same [format](Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) as downloaded via admin action.
                - BE will consume the sheet and update the statuses (”Transferred”) against physical rewards in “rewards” table.
                - Notification will be sent to the user as per the [nudge](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=1824995158#gid=1824995158&range=A1:H7) framework via external channels (Whatsapp), along with in-app and web nudges.
            - Claim CTA will be disabled if there is no rewards eligible for claiming (”processing” status) or expired reward.
            
             
            
        
        **B) Referree User flow: Click → Signup → Loan → Unlock and track → Claim**
        
        **Discovery (Click + Signup):**
        
        - User discovers Volt via invite link shared by referrer and signs up with Volt.
        - User is shown a banner in the which confirms that the user is a referee (that is joined Volt via referral link)
            - hero card in LOS homepage and
            - across the LOS journey with the following nudge template
            - ({{Name/ Number}} referred you. Please complete loan application journey by {{date}} to win Rs. 250 cash).
        
        **Reward Tracking and claiming mechanism:**
        
        - On opening loan account above Rs. 25000, referee will be able to track rewards under “Rewards” section in homepage bottom nav bar/ accessing rewards via referral program entry point. (Unified reward interface for both referrer and referee for easy tracking and claiming journey.)
        - The [tracking](Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) details of rewards, notification channel with status of reward, expiry date and [claiming](Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) flow will be same as referrer as it is a cash reward.
        - The nudge flow to referee is as per the framework [sheet](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=1824995158#gid=1824995158&range=A1:H7)
        - **Ops and LSQ visibility:**
            - Once a user signs up via referral link a column with referee_referrerid, phone number and name of referrer is passed from BE corresponding to the referee user to AppSmith and LSQ.
            - Total Rewards earned and processed columns are also passed on to Appsmith for ops team visibility.
            
    

---

## **6.  Design**

https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=117-122&p=f&t=XBsG82aT5ueY9BK8-0

## **6.  Appendix (Optional)**

### Benchmarking:

### User feedback / Calling: