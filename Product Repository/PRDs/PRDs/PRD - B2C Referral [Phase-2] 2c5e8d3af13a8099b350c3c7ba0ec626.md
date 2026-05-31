# PRD - B2C Referral [Phase-2]

: Devansh Kar
Created time: December 10, 2025 8:12 AM
Status: In progress
Last edited: January 14, 2026 5:28 PM

# **What problem are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt has no mechanism to leverage its existing user base (borrowers who have experienced the value of Volt Money's LAMF product or users who know about the platform), for new user acquisition through word-of-mouth in an organized and trackable manner.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new users to borrow LAMF from Volt as a trusted brand and limited period reward offers will assist in fast-tracking the loan account completion process.

Both **Referrers** and **Referees** need a seamless, trackable referral experience with transparent rewards.

---

# **How do we measure success?**

**Primary KPI**

- 1000 signups via referral in 3 months(Alpha)
- % acquisitions (new signups/ loan account creation) from referral

**Engagement KPI**

- Average referrals per referrer
- Reward claim rate

---

# **How are others solving this problem?**

[https://docs.google.com/spreadsheets/d/1Lnzz3_jr41oLqoVnVCoOFaiiQOtg_KwRjL8qVSIww_A/edit?gid=1237415813#gid=1237415813](https://docs.google.com/spreadsheets/d/1Lnzz3_jr41oLqoVnVCoOFaiiQOtg_KwRjL8qVSIww_A/edit?gid=1237415813#gid=1237415813)

---

# **What is the solution?**

## Requirements

**A) Referrer Requirements**

**A1) Referral Program eligibility**

**User Story 1: Eligibility for referral program**

*As a user, I want to be automatically enrolled into a referral program with applicable rewards and T&Cs configured from BE specific to the referral program.*

**Acceptance Criteria:**

1. The user shall be automatically eligible for a referral program (as a referrer) with applicable conditions and rewards based on rules/ parameters set by config in BE via a POST API endpoint which creates a new referral program. 
    
    `POST <baseURL>/api/v1/referralprogram`
    
    The request body sent to the API endpoint to create a new referral program will have config parameters as follows:
    
    **Sample Request:**
    
    ```jsx
    "platform_code": {"Volt B2C" "Volt PhonePe", "Volt B2B2C"} 
    "platform_type": {"Web", "Android", "iOS"}
    "user_type": {"borrower", "opportunity"}
    "step_id": ""
    "cohort_id": "CH1003"
    "program_start_date": "01-01-2026"
    "program_end_date": "31-03-2026"
    "banner_id": "banner123"
    "referrer_min_loan_amount": ""
    "referee_min_loan_amount": 25000
    "number_of_steps": 25
    "number_of_milestones": 2
    "milestone1": 5
    "milestone2": 25
    "rewards":
    	{
    		"referrer_reward_type": "cash"
    		"referrer_reward_value": "1000"
    		"referee_reward_type": "cash"
    		"referee_reward_value": "250"
    		"milestonereward1_type": "physical"
    		"milestonereward1_value": "airpods"
    		"milestonereward2_type": "physical"
    		"milestonereward2_value": "ipad"
    		"referrer_reward_claim_validity_date": "30-06-2026"
    		"referee_reward_claim_validity_date": "30-06-2026"
    		"reward_final_transfer_date": "15-07-2026"
    	}
    	"priority": -200
    	"isActive": "True"
    ```
    

**Sample Response:**

```jsx
"referral_program_id": "RP1001" 
	"isActive": "True"
```

Details of **Key request parameters** in the config:

- `platform_code` : Volt platform/ partner from which user is originated. The channels would be:
    - Volt B2C
    - Volt B2B redirection partners (PhonePe, Other partners with Volt having rights for the users)
    - Volt B2B2C (MFD Partner originated users)
- `platform_type` : Platform type of the user - Android, iOS, Web
- `user_type`:
    - Type of user in the Volt loan journey. This has values-
        - “borrower”: Any Volt user with an active/ past active loan account with Volt.
        - “opportunity”: Volt user in any LOS application stage (post signup)
        - “cohort”: Any cohort with selected account_ids mapped to a cohort_id
- `step_id:` Applicable for user in Volt LOS journey mapped to current step_id . It can take null values which indicates to any signed up user/ opportunity on Volt channel(s).
- `cohort_id`: A unique id mapped to a sheet of selected accountids uploaded in `cohortapi` endpoint. It can take null values.
- `program_start_date`: Start date of referral program
- `program_end_date`: End date of referral program. This will also be the date before which a referee must open loan account in order to be eligible for referral rewards. This parameter has update capability and can take null values as well. The initial value for the first referral program is 31st March 2026. (TBD)
- `banner_id`: Indicates banner_id used/ generated from `banners` api end point which configures banner used for a referral program.
- `referrer_min_loan_amount`: Minimum loan amount opened by referrer to be eligible for referral. It can take null values indicating no minimum loan amount criteria is present for referral program eligibility.
- `referee_min_loan_amount`: Minimum loan amount of first ever loan account opened by referee to be eligible for referral rewards by both referrer and referee. It can take null values indicating no min loan amount eligibility criteria is present. To start with the first program, the value is Rs. 25000
- `max_`referrals: Max number of steps in a referral reward program.
- `number_of_milestones`: Indicates number of milestones in a referral program.
- `milestone1`: first milestone step
- `milestone2`: second milestone step
- `referrer_reward_type`: type of normal referrer reward (values: “cash”, “physical”).
- `referee_reward_type`: type of normal referee reward (values: “cash”, “physical”).
- `referrer_reward_value`: value of referrer reward: (amount for type: cash, name of “physical” reward)
- `referee_reward_value`: value of referee reward: (amount for type: cash, name of “physical” reward)
- `milestonereward1_type`: type of milestone reward (values: “cash”/ “physical”).
- `milestonereward1_value`: value of milestone reward (amount for type: cash, name of “physical” reward).
- `referrer_reward_claim_validity_date`: Final date to claim referrer reward. Initial value will be 30th June 2026
- `referee_reward_claim_validity_date`: Final date to claim referee reward. Initial value will be 30th June 2026
- `reward_final_transfer_date` : Final transfer date of all the claimed rewards to be shown in T&C page. The initial value for the first referral program is 15th July 2026
- `priority`: decides priority of a referral program/ cohort, a user is enrolled to incase a user is eligible under multiple referral programs/ cohorts.
- `isActive`: “true”/ “false” (indicates program is active / inactive).

b. The following parameters of a referral program, a user is eligible for can be updated via a PUT API endpoint as and when decided by Volt.

`PUT <baseURL>/api/v1/referralprogram` 

- `program_end_date`
- `referrer_reward_claim_validity_date`
- `referee_reward_claim_validity_date`
- `reward_final_transfer_date`

**Sample Request:**

```jsx
"referral_program_id": "RP1001" 
"program_end_date": "05-05-2026"
"referrer_reward_claim_validity_date": "05-07-2025"
"referee_reward_claim_validity_date": "05-07-2025"
"reward_final_transfer_date": "15-08-2025"
	"isActive": "True"
```

**Sample Response:**

```jsx
"referral_program_id": "RP1001" 
	"isActive": "True"
```

c. The user gets automatically unenrolled from a referral program when the Volt deactivates it via a DELETE API endpoint.

- Entry point banner of referral program will be disabled if a user (account_id) is not enrolled to any referral program.

`DELETE <baseURL>/api/v1/referralprogram` 

**Sample Request:**

```jsx
"referral_program_id": "RP1001" 
	"isActive": "False"
```

**Sample Response:**

```jsx
"referral_program_id: RP1001 is deactivated"
Status: 200
```

**User Story 2: Cohort eligibility for referral program**

*As a user, I want to be automatically enrolled into a referral program as a part of selected cohort selected by Volt with applicable rewards and T&Cs configured from BE specific to the referral program.*

**Acceptance Criteria:**

1. The user shall automatically be a part of selected cohort as decided by Volt Money through uploading a spreadsheet (excel) with list of `account_ids` of the user via a POST API endpoint which creates a new cohort. 
    
    `POST <baseURL>/api/v1/cohort`
    
    Example: `POST voltmoney.in/api/v1/cohort`
    
    The sample request body sent to the API endpoint will be an excel sheet consisting of a single column **account_id**  with entries as list of account_ids via a placeholder to upload file and making the activity status of cohort as “true” and mentioning the priority order of the cohort.
    
    **Sample Request:**
    
    **Excel sheet upload placeholder**
    
    ```jsx
    
    "isActive": "True"
    "priority": -200
    ```
    

**Sample Response:**

```jsx
"cohort_id": "CHT1001" 
	"isActive": "True"
```

b.  The user gets automatically unenrolled from a cohort when the Volt deactivates the cohort entirely via a DELETE API endpoint.

`DELETE voltmoney.in/api/v1/cohort` 

**Sample Request:**

```jsx
"cohort_id": "CHT1001" 
	"isActive": "False"
```

**Sample Response:**

```jsx
"cohort_id: CHT1001 is deactivated"
Status: 200
```

c. The newly generated cohort_id on passing as a parameter in the POST Referral Program API request body makes the program eligible for the specific cohort.

**A2) Referral Program Discovery**

**User Story 3: User notification for referral eligibility (External to app)**

*As a user, I want to get notified about being eligible for Volt’s referral program.*

**Acceptance Criteria:**

1. When a user gets eligible for a referral program (as a referrer) for the first time, he shall get notified about it via channels — Whatsapp, SMS and Push Notifications at intervals specified in the nudge framework [sheet](https://docs.google.com/spreadsheets/d/1ER_k948fp1JHXpOYwwWf1cER5BrBvNbjHVjsryVNlw0/edit?usp=sharing).

**User Story 4: In-app discovery and validity information of referral program**

*As a user, I want to see the a) entry point banner, b) landing page hero images/ banners, and c) validity period specific to the referral program/ campaign I am currently eligible for upfront.*

**Acceptance Criteria:**

1. The user should see the entry point banner and landing page image/ banner configured corresponding to the active referral program he is eligible for.
2. The user should see the validity period of referral program/ campaign (if any) he is eligible for on entry point and landing page upfront. [To start the first referral program will be valid from Jan 1st to 31st Mar 2026].
3. The banner that the user sees is according to the parameter “banner_id” configured from BE for a referral program, a user is eligible for.

**API Details:**

A new banner is created via an API endpoint:

`POST <baseURL>/api/v1/banners`

This has input fields as image type [jpeg/ png] with placeholder to upload banner images. upto 10 MB

- entrypoint_image: Image that will be utilised in the entry point banner across all touchpoints in LOS and LMS.
- landingpage_image: Image/ banner that will be utilised in the hero image of the landing page of the referral program.

**Sample Request-**

**entrypoint_image upload placeholder**

**landingpage_image placeholder**

```jsx

"isActive": "True"
```

**Sample Response-**

```jsx
"bannerid": "BANNER_123"
"isActive": "True"
```

d. The newly generated banner_id on passing as a parameter in the POST Referral Program API request body reflects the specific banners to the user who are eligible for the specific referral program.

e. The referrer should be able to see the entry point for referral program across various touchpoints as mentioned in the [sheet](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=1824995158#gid=1824995158).

**User Story 5: Terms & Conditions for referral program**

*As a user, I want to get clarity on Terms & Conditions of the referral and reward program/ campaign I am eligible for.*

**Acceptance Criteria:**

1. The user should be able to view the terms and conditions of the specific referral program he is eligible for to be reflected on the T&C page/ section of the referral program. 
    
    List of **T&Cs** include <<will update full list with fixed and variable list>>:
    
- Validity of the program
- Successful referral definition (All loan account opened before {{x}} date and above {{y}} amount)
- Referee eligibility conditions
- Rewards eligibility conditions
- Rewards validity ({{x}} days from reward unlock date : x = 30 for 1st launch

**A3) Referral link generation and sharing**

**User Story 6: Generation of unique link**

*As a user, I want a unique link and code to be generated for me as soon as I am eligible for a referral program which has event based tracking capability.*

**Acceptance Criteria:**

1. The user (referrer) will have a unique link and referral code generated as soon as he is eligible for a referral program.
2. The user (referrer) shall be able to view and share **only** the referral link via the [sharing channels](PRD%20-%20B2C%20Referral%20%5BPhase-2%5D%202c5e8d3af13a8099b350c3c7ba0ec626.md).
3. When any new user (referee) signs up via the link ~~and completes the loan journey~~, the unique code of the referrer will be finally mapped against the account_id of the referee. (referrerrefereeid field)
4. The referral link should be trackable with the following events (fire events with metadata shared by referral link):
    - Shared: When a referrer shares the referral link with a user. (referral_link_shared)
    - Clicked: When a referee clicks on the referral link. (referral_link_clicked)
    - Downloaded (Deeplinking with firebase): When a referee downloads the app with attribution of the link with query parameters.  (app_installed)
    - Signed Up: When referee signs up with mobile number details (This will finally capture the phone number mapped against the referral link/ code) [Post this **storing in BE**]
    - Stepids mapped in the LOS journey with the referral link on reaching the steps:
        - MF_Fetch
        - MF_Pledge_Portfolio
        - KYC
        - Bank Account verification
        - Mandate
        - Asset_pledge
        - Agreement
        - Loan_account_created
    - The sharable link with query parameters is of the format:
    
    [https://app.voltmoney.in/referral?ref_code=ABC123&campaign=referral_v1](https://volt.money/referral?ref_code=ABC123&campaign=referral_v1)
    
    - The unique code generated will be of 7 digits of format: REF1001

**User Story 7: Link sharing capability and method**

*As a referrer, I want to easily share my referral link/code through WhatsApp, SMS, Copy unique code and link, and other sharing apps so that I can invite friends.*

**Acceptance Criteria:**

1. **App:** The user (referrer) should be able to share the unique referral link with refer message template via 
    - **Primary:** Whatsapp (Directly redirecting to Whatsapp)
    - **Secondary:** Device Apps/ channels shown in the share sheet opened natively (App) which includes (Whatsapp, SMS, Gmail, FB, Instagram, copy link to clipboard) etc.
2. An app user on clicking on any channel from the native share sheet is redirected to the corresponding app with message template for sharing saved and automatically popping up in the sharing channel interface.
3. **Web:** The web user (Desktop browser, mobile browser) should be able to share the message template with unique link saved via web redirection to channels —
    - **Primary:** Whatsapp Web
    - **Secondary:** Copy link to clipboard
4. ~~Tracking events-  `referral_link_shared`, `referral_link_clicked` , etc. must fire with metadata for a referral link shared by a referrer. <<Check with dev>>~~

**A4) Track Referee Progress**

**User Story 8: Progress tracking of referred users**

*As a referrer, I want a dashboard showing all successful and invalid referrals, and milestone tracking of each referees’ progress in the application journey (Signup → KYC_Completed → Application_completed) so that I know who is close to earning me rewards.*

**Acceptance Criteria:**

- The user should have a consolidated view of the successful referrals and breakup of in-progress, and invalid eferrals.
    - Successful referral: When a referee opens a loan account above `referee_min_loan_amount`  (≥ Rs. 25000)
        - Count
        - List
    - In-progress referral: When a referee is in the LOS loan application journey but has not completed the first loan application.
        - Count
        - List
    - Invalid referrals: When signed up referee opens a loan account below `referee_min_loan_amount` or does not complete loan account within the program end date.
        - List
- The user should be able to view milestone tracker which consists of number of successful referral steps achieved out of total number of steps, and rewards unlocked at each step in the landing page.
- The user should be able to view the individual progress of in-progress referrals.
    - Signed Up → KYC Completed → Account opened
- The user should be able to view all the invalid and ~~expired~~ referrals across and irrespective of all referral programs he’s been a part of.
- Referees who opened account with < Rs.25000 will be counted in Invalid referral and the messaging/ info for the same should be displayed to the user.
- External comms and In-App notification should be triggered to the referrer for each successful referral (referee loan account creation ≥ 25000) as per the nudge framework [sheet](https://docs.google.com/spreadsheets/d/1ER_k948fp1JHXpOYwwWf1cER5BrBvNbjHVjsryVNlw0/edit?usp=sharing)

**User Story 9: Nudge capability to referees**

*As a referrer, I want to nudge people at application stage that I have referred, to complete loan application so that I can avail rewards fast.*

**Acceptance Criteria:**

- Reminder nudge CTA corresponding to In-progress application referrals.
- Whatsapp redirection on clicking on Reminder nudge with message template.

**Frontend:**

- Successful referrals number in a card on landing page with “View details”
- View details section show - Distribution of successful, in progress and expired/ invalid referrals.
- 3 statuses corresponding to each application in In-Progress/ Success state [Signed Up → KYC Completed → Account Opened]

**Backend:**

- Update status on each event/ stepid completion for a referee (unique referral code mapped) and send to frontend:
    - Signed Up
    - KYC Completed
    - Account opened

**A5) Unlock Rewards, tracking and notification**

**User Story 10: Tracking and notification of unlocked rewards**

*As a referrer, I want my reward (Cash/ Physical) to get unlocked and tracked as soon as each referee opens a loan account ≥ Rs. 25000 within the validity period of the referral program.*

**Acceptance Criteria:**

- The user should be able to track rewards in the rewards section with details as mentioned below:
- Tracking of Unlocked rewards (across their lifecycle): Rewards which get unlocked on completion of each successful referral.
    - Overall view of ‘Total rewards’ (Sum of cash amount + Physical) unlocked  for ‘Cash + Physical’ rewards. The details will be subdivided into following 2 sections:
        1. Total ‘Cash rewards’ (Sum of cash amounts) earned view which are in “[active](../../Product%20Processes/Referral%20Product%20Note%202cfe8d3af13a80b485fff3273928ebca.md) “status with “Claim” action. This will further include:
        - List of individual cash reward amounts unlocked with **date** of unlock.
        - Current status of each individual reward unlocked
            - Active: The rewards which are active but not yet claimed.
            - Claimed: Rewards which are already claimed but not settled
            - Transferred: Rewards which are settled
            - Expired: Rewards which are already expired and no action can be taken on them.
            - Failed: Rewards corresponding to which transaction failed
        
         b. Milestone (Physical) rewards section with action to claim for “active” status. This will also include:
        
        - List of physical rewards unlocked with date of unlock on completing milestone.
        - Current status of physical reward:
            - Active
            - Claimed
    - Tracking of payouts/ settlement of claimed rewards. There shall be a separate section which shall track cash rewards payout transaction details:
        1. Cash rewards payout list: This will contain list of all transactions processed with:
            - Total amount
            - Date of success/ failure
            - Transaction status: Success or failed
            - Transaction reference id
            - Bank account no.
            - IFSC code
    - Tracking of locked rewards:
        - View of the next reward that is locked (Cash/ physical) and number of referrals needed to unlock it.
    - Milestone rewards and journey progress tracking:
        - Overview of number of steps completed out of total steps in the referral milestone journey present.
        - No. of steps needed to unlock milestone reward.

**A6) Claim Reward (Normal (Cash) + Milestone)**

**User Story 10: As a referrer, I want to claim my unlocked cash reward into my bank account and milestone (physical reward) dispatched to my address so that I receive my earnings easily.**

**Acceptance Criteria:**

1. Cash reward claim:
    - When a reward gets unlocked and is of status “active”, the claim action gets activated.
    - Based on availability of bank details of the user (referrer/ referee):
        - **Case 1:** If bank details of the user are not available with Volt, then there will be a placeholder trigger for capturing the following users’ bank details:
            - Bank A/C No.
            - IFSC Code
            - Beneficiary name
        - **Case 2:** If bank details of the user already exist with Volt, then the bank details will be pre-filled in the placeholder trigger with action to confirm. (Valid for For first time popup confirmation only)
    
    On user confirming,  BE will update the bank account details against referrer in “referral” table in DB and a nudge will be triggered communicating successful “processing” of rewards.
    
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
        
        | account_id | referrer_id | referrer_referee_id | reward_ids (array) | bank_account_no | ifsc_code | amount | beneficiary_name | bank_account_verified | UTR | transaction_status | reward_type | failure_reason |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        |  |  |  | {RWD110, RWD 111, RWD 112} |  |  | 3000 |  |  |  |  |  |  |
        - Backend after consuming the sheet will update the status against each reward in the “rewards” table in DB to status “Transferred” or “Failed”.
        - If failure reason is due to wrong bank account details namely:
            - Account is closed
            - Beneficiary name differs
            - IFSC number mismatch
            - Account does not exist
        - Notification will be sent to the user as per the [nudge](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=1824995158#gid=1824995158&range=A1:H7) framework via external channels (Whatsapp), along with in-app and web nudges.
        
    
    b. Physical milestone reward:
    
    - For a physical milestone reward with status: “active”, claim action will get activated.
    - Placeholder will be triggered to capture address details of the user:
        - Address line 1
        - Address line 2
        - Pincode
    - The address details are passed to BE which shall be saved in the “referrals” table and and a nudge will be triggered communicating successful “processing” of rewards by certain date (05th July) [both in-app and external].
    - **Admin action:**
        - Business/ Ops team can download the latest report of physical rewards to settle based on the cycle decided as per SOP.
        - The format will be same as discussed in the cash payout table where admin can separate the physical rewards via reward_type parameter.
        
        | account_id | referrer_id | referrer_referee_id | reward_ids (array) | bank_account_no | ifsc_code | amount | beneficiary_name | bank_account_verified | transaction_status | reward_type | address | pincode | UTR | delivery_status |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        |  |  |  | {RWD110, RWD 111, RWD 112} |  |  | 3000 |  |  |  |  |  |  |  |  |
        - Once the business team approves, as per SOP set, fulfilment with respective vendor will be done.
        - Post fulfilment is successful, Ops team will manually update the sheet with delivery_status column and upload it in the same [format](../../Product%20Processes/Referral%20Product%20Note%202cfe8d3af13a80b485fff3273928ebca.md) as downloaded via admin action.
        - BE will consume the sheet and update the statuses (”Transferred”) against physical rewards in “rewards” table.
        - Notification will be sent to the user as per the [nudge](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=1824995158#gid=1824995158&range=A1:H7) framework via external channels (Whatsapp), along with in-app and web nudges.
    - Claim CTA will be disabled if there is no rewards eligible for claiming (”processing” status) or expired reward.
    
     
    

**B) Referee Requirements**

**B1. Referral redirection**

**US 1: As a referee, when I click a referral link, I want to get redirected to a) playstore/ appstore (app.voltmoney.in) or Volt Money app (if already have app installed)**

**Success Criteria:**

- Redirection to Playstore/ Appstore (app.voltmoney.in) if app not installed.
- If app is installed, directly open the app.
- Attribution of referrerid to referee account

**Frontend Requirements:**

- Redirection logic to playstore/ appstore (mobile platform) and [app.voltmoney.in](http://app.voltmoney.in) if opened via web/ browser platforms.

**Backend Requirements:**

- Attribution of accountid created for referee to referrerrefereeid field.

**B2. Referree landing page**

**US 2: As a referee, I should be aware that I have been referred by referrer with xx referrer code and yy name and eligible for reward on completing loan journey.**

**Success Criteria:**

- Referrer code and referree name attributed and visible on landing page/ home screen.
- Info regarding Reward amount should be visible on completing loan journey.
- If a user joins the Volt app via multiple referral links, then the latest referral code and referrer name should be attributed to the user until the user completes the pledge step. (Freezing referrerrefereeid post pledge step).
- If a user has already completed pledge once via any other platform or volt and then again joins app via a referral link he won’t be eligible as a referee

**Frontend Requirements:**

- Show referral code and referrer name on the homepage to referee.
- Messaging to the user regarding earning reward amount Rs. xx on completing loan journey.

**Backend Requirements:**

- Post pledge attribution to freeze the final referrerrefereeid.
- Ineligibility condition for being a referee if a user has already completed pledge.

**B3. Journey Tracking and reminder mechanism for Referee Reward (₹xx)**

**US 3: As a referee, I want to track number of steps remaining and get reminder to open account and earn referee reward ₹250 upon loan account creation so that I feel appreciated and complete the loan journey.**

**Success Criteria**

- Stepper visibility of steps remaining to unlock reward
- Nudge at important steps for steps remaining to earn reward.

**Frontend Requirements**

- Show referee a stepper to unlock reward in the stepper screen
- Nudge user after each step to steps remaining to unlock reward

**Backend Requirements**

- -

**B4. Unlocking and claiming reward**

**US 3: As a referee, I want to get notified about unlocking rewards, check my unlocked rewards and claim them.**

**Success Criteria**

- Nudge referee on unlocking rewards via Whatsapp and In-App
- Notify referee when reward amount is successfully processed.
- Total reward earned will be trackable by referee under rewards section.

**Frontend Requirements**

- Rewards section for referee positioning [Check with design]
- In-app nudgeand whatsapp for rewards unlocked and claiming when processed successfully.

**Backend Requirements**

- Claiming mechanism same as referrer story

---

# **Design**

https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=117-122&p=f&t=XBsG82aT5ueY9BK8-0

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes