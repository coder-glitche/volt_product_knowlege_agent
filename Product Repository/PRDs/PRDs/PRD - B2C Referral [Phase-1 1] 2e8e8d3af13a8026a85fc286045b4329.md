# PRD - B2C Referral [Phase-1.1]

: Devansh Kar
Created time: January 14, 2026 5:28 PM
Status: In progress
Last edited: May 27, 2026 4:29 PM

Could you please confirm whether the referral feature should be enabled for both CreditMantri codes (CM_1 and CM_2), or just one? 

@Keyur Lo can you reply?

# **What problem are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt has no mechanism to leverage its existing user base (borrowers who have experienced the value of Volt Money's LAMF product or users who know about the platform), for new user acquisition through word-of-mouth in an organized and trackable manner.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new users to borrow LAMF from Volt as a trusted brand and limited period reward offers will assist in fast-tracking the loan account completion process.

Both **Referrers** and **Referees** need a seamless, trackable referral experience with transparent rewards.

---

# **How do we measure success?**

**Primary KPI**

- 1000 signups via referral in 3 months(Alpha)
- 200 new loan accounts opened in 3 months
- % acquisitions (new signups/ loan account creation) from referral

**Engagement KPI**

- Average referrals per referrer

---

# **How are others solving this problem?**

[https://docs.google.com/spreadsheets/d/1Lnzz3_jr41oLqoVnVCoOFaiiQOtg_KwRjL8qVSIww_A/edit?gid=1237415813#gid=1237415813](https://docs.google.com/spreadsheets/d/1Lnzz3_jr41oLqoVnVCoOFaiiQOtg_KwRjL8qVSIww_A/edit?gid=1237415813#gid=1237415813)

---

# **What is the solution?**

## Requirements

**A) Referrer Requirements:**

**A1) Referral Program eligibility:**

**User Story 1: Eligibility for referral program**

*As a user, I want to be automatically enrolled into the referral program with applicable rewards and T&Cs set as per BE rule engine.*

**Acceptance Criteria:**

1. The user shall be automatically eligible for the Volt referral program (as a referrer) with applicable conditions and rewards based on rules/ parameters set by the Backend referral rule engine.
    
    Details of **Key parameters** set in the BE rule engine are:
    
    - `platform_code` : Volt platform/ partner from which user is originated. The channels would be:
        - Volt B2C
        - Volt B2B redirection partners (PhonePe, CreditMantri, TradeBrains)
        - Volt B2B2C (MFD Partner originated users)
    - `Eligible_cohort`: Users who have opened an active loan account on Volt Money (both TCL, Bajaj, and DSP lender). (Current active loan account  + past active loan account users)
    - `platform_type` : Platform type of the user - Android, iOS, Web
    - `program_start_date`: Start date of the referral program/ campaign.
    - `program_end_date`: End date of referral program. This will also be the date before which a referee must open loan account in order to be eligible for referral rewards (by both referrer and referee). This parameter has update capability and can take null values as well.
    - `referee_min_loan_amount`: Minimum loan amount of first ever loan account opened by referee to be eligible for referral rewards by both referrer and referee. To start with the first program, the value is Rs. 25000.
    - `number_of_milestones`: Indicates number of milestones in a referral program. The value will be set to 2 here.
    - `milestone1`: This indicates the first milestone step/ milestone referral number. The value will be set to 5 here indicating the first milestone is achieved at completion of 5th successful referral.
    - `milestone2`: This indicates the second milestone step/ milestone referral number. The value will be set to 25 here indicating the second milestone is achieved at completion of 25th successful referral.
    - `referrer_reward_type`: Indicates type of normal referrer reward (values: “cash”, “physical”). The value will be set to “cash” here.
    - `referee_reward_type`: Indicates type of normal referee reward (values: “cash”, “physical”). The value will be set to “cash” here.
    - `referrer_reward_value`: Indicates the value of referrer reward. The reward value will be Rs. 1000
    - `referee_reward_value`: Indicates the value of referee reward. The reward value will be Rs. 250
    - `milestonereward1_type`: Indicates type of milestone reward (values: “cash”/ “physical”). The value will be set to “physical” here.
    - `milestonereward1_value`: Indicates the value of milestone reward. The value is set to “Apple Airpods” here.
    - `milestonereward2_type`: Indicates type of milestone reward (values: “cash”/ “physical”). The value will be set to “physical” here.
    - `milestonereward2_value`: Indicates the value of milestone reward. The value is set to “Apple iPad” here.
- The user, if it belongs to B2B2C then partnerid mapping shall also be checked in order to check for eligibility. B2B2C MFD Partners opening any loan account (self line + any other loan account) will not be eligible for B2C referral feature.
- Only active loan account users (Users in LMS journey) shall be eligible for referral program. Foreclosed accounts (falling under LOS journey) won’t be eligible for referral in Phase 1.

**A2) Referral Program Discovery (In-App):**

**User Story 2: In-app discovery**

*As a user, I want to see the entry points for referral and rewards program across different touchpoints in the LMS journey.*

**Acceptance Criteria:**

1. The user should see the entry point components across various touchpoints in the LMS journey in order to access as well as know the details about using the referral feature.
2. The various touchpoints and corresponding entry point component in the LMS journey include:
    
    
    | Touchpoints | Entry point component |
    | --- | --- |
    | Home page of LMS | Banner |
    | Withdrawal request received page (Withdrawal processing) | Banner |
    | Repayment success page | Banner |
    | Bottom Navigation bar | Rewards Icon |

**User Story 3: “New” tag in the bottom nav bar icon**

*As a user, I want to see the “New” tag corresponding to the icon in bottom nav bar in order to be aware of the newly introduced feature.* 

**Acceptance Criteria:**

1. The user should be able to see a tag “New” beside the rewards icon in the bottom nav bar in order to improve discoverability of the newly introduced referral feature.
2. The validity period set for the “New” tag will be till the end date of the referral program.

**A3) Referral Program landing page:**

**User Story 4: Constitution of landing page**

*As a user, I want to view the all the necessary details/ information as well as main actions related to accessing the referral and rewards program in the landing page.*

**Acceptance Criteria:**

1. The user should be able to access/ view all the important and necessary details on the landing page of the referral program: The composition of the landing page providing all the necessary details include the following:
    - Hero image of referral program (This also contains a **component** mentioning the **program validity date** as set in the **backend**)
    - Options to Share link via:
        - Whatsapp
        - Copy link/ Other sharing channels drawer option
    - **Details of normal rewards and milestone rewards:**
        - Cash rewards worth Rs. 1000 per referral
        - Apple Airpods on completion of 5th referral
        - Apple iPad on completion of 25th referral
    - **How referral works?**
        - Share invite link with friends & family
        - Friend opens a loan account
        - You both get rewarded
    - View of value of next reward to get unlocked and number of referrals needed to unlock. (This will also be an entry point to track number of incomplete and successful referrals)
    - [**Terms & Conditions**](PRD%20-%20B2C%20Referral%20%5BPhase-1%201%5D%202e8e8d3af13a8026a85fc286045b4329.md) entry point
    - **FAQs:**
        - <<To add list of faqs here>>

**User Story 5: Terms & Conditions for referral program**

*As a user, I want to get clarity on all the relevant Terms & Conditions of the referral and rewards program.*

**Acceptance Criteria:**

1. The user should be able to view the terms and conditions of the specific referral program he is eligible for to be reflected on the T&C page/ section of the referral program. 
    
    List of **T&Cs** include <<will update full list with fixed and variable list>>:
    
- Validity of the program
- Successful referral definition (All loan account opened before {{x}} date and above {{y}} amount)
- Referee eligibility conditions
- Rewards eligibility conditions
- Rewards validity ({{x}} days from reward unlock date : x = 30 for 1st launch

**A4) Referral link generation and sharing**

**User Story 6: Generation of unique link**

*As a user, I want a unique link and code to be generated for me as soon as I am eligible for a referral program which has event based tracking capability.*

**Acceptance Criteria:**

1. The user (referrer) will have a unique link and referral code generated as soon as he is eligible for a referral program.
2. The user (referrer) shall be able to view and share **only** the referral link via the [sharing channels](PRD%20-%20B2C%20Referral%20%5BPhase-1%201%5D%202e8e8d3af13a8026a85fc286045b4329.md).
3. The trackable link should redirect the referee to check eligibility page of Volt Money. The link is of the format
[https://voltmoney.in/check-loan-eligibility-against-mutual-funds](https://voltmoney.in/check-loan-eligibility-against-mutual-funds)[/referral?ref_code=ABC123&campaign=referral_v1](https://volt.money/referral?ref_code=ABC123&campaign=referral_v1)
4. When any new user/ lead (referee) enters the phone number and PAN via a referral link ~~and completes the loan journey~~, the unique code of the referrer will be mapped against the phone number and PAN of the referee. (referrerrefereeid field). 
5. When the lead becomes an opportunity then the same (referrerrefereeid) will be mapped to the unique account_id of the user.
6. The referral link should be trackable with the following events (fire events with metadata shared by referral link):
    - Shared: When a referrer shares the referral link with a user. (referral_link_shared)
    - Clicked: When a referee clicks on the referral link. (referral_link_clicked)
    - Check eligibility: When referee enters the mobile number and PAN details ,these will get mapped against the referral link and code [**storing in BE Database**]. Also, the accountid created corresponding to the phone number and PAN combination will be attributed to the same referral link and code
    - ~~Stepids mapped in the LOS journey with the referral link on reaching the steps:~~
        - ~~MF_Fetch~~
        - ~~MF_Pledge_Portfolio~~
        - ~~KYC~~
        - ~~Loan_account_created~~
    - The unique referrer code generated will be of 7 digits of format: REF100000001

**User Story 7: Link sharing capability and method**

*As a referrer, I want to easily share my referral link/code through WhatsApp, SMS, Copy unique code and link, and other sharing apps so that I can invite friends.*

**Acceptance Criteria:**

1. **App and webapp:** The user (referrer) should be able to share the unique referral link with referral message template via 
    - **Primary:** Whatsapp (Directly redirecting to Whatsapp)
    - **Secondary:** Device Apps/ channels shown in the app drawer opened natively (App) which includes (Whatsapp, SMS, Gmail, FB, Instagram, copy link to clipboard) etc. (Not valid for webapp- Only copy link is valid.)
2. An app user on clicking on any channel from the native share sheet is redirected to the corresponding app with message template for sharing saved and automatically popping up in the sharing channel interface.
3. **Web:** The web user (Desktop browser, mobile browser) should be able to share the message template with unique link saved via web redirection to channels —
    - **Primary:** Whatsapp Web
    - **Secondary:** Copy link to clipboard
4. The message template which shall be pre-copied and that can be shared by referrer would be: “HI….”

**A4) Track Referee Progress**

**User Story 8: Progress tracking of referred users**

*As a referrer, I want a dashboard showing all the completed and incomplete referrals, and tracking status of each referees’ progress in the application journey (Signup → KYC_Completed → Application_completed) so that I know who is close to making me earn rewards.*

**Acceptance Criteria:**

- The user should have a consolidated view of the completed referrals and incomplete referrals (with breakup of in-progress, invalid referrals, and expired referrals).
    - Successful referral: When a referee opens a loan account above `referee_min_loan_amount`  (≥ Rs. 25000)
        - List
        - Reward earned corresponding to the successful completion of the referral (Cash, Airpod, iPad, etc.)
    - In-progress referral: When a referee is in the LOS loan application journey but has not completed the first loan application.
        - List
    - Invalid referrals: When signed up referee opens a loan account below `referee_min_loan_amount`
        - List
    - Expired referrals: When a referee does not open a loan account within the program end date.
- ~~The user should be able to view milestone tracker which consists of number of successful referral steps achieved out of total number of steps, and rewards unlocked at each step in the landing page.~~
- The user should be able to view the individual progress of in-progress referrals.
    - Signed Up → KYC Completed → Account opened (Completed)
- The user should be able to view all the invalid and expired referrals across and irrespective of all referral programs he’s been a part of.
    - Invalid: If a referee opens a loan account below Rs. 25000
    - Expired: If a referee opens a loan account beyond the expiry date of the referral program.
- External comms and In-App notification should be triggered to the referrer for each successful referral (referee loan account creation ≥ 25000) as per the nudge framework [sheet](https://docs.google.com/spreadsheets/d/1ER_k948fp1JHXpOYwwWf1cER5BrBvNbjHVjsryVNlw0/edit?usp=sharing)

**User Story 9: Nudge capability to referees**

*As a referrer, I want to nudge people at application stage that I have referred, to complete loan application so that I can avail rewards fast.*

**Acceptance Criteria:**

- The user (referrer) shall be able to nudge the referees who are progressing in the loan application journey but have not successfully completed the journey.
- On clicking on the nudge action, the user will be redirected to Whatsapp with a pre-copied message and link to app.voltmoney.in

**Message:**

**B) Referee Requirements**

**B1. Referral redirection**

**US 10:** *As a referee, when I click a referral link, I want to get redirected to check eligibility page of Volt Money* **(**[https://voltmoney.in/check-loan-eligibility-against-mutual-funds](https://voltmoney.in/check-loan-eligibility-against-mutual-funds)**)**

**Acceptance Criteria:**

- The referee will be redirected to [voltmoney.in](http://voltmoney.in) check eligibility page on clicking on the referral link.
- Attribution of referrerid to referee account happens when the referee enters the phone number and PAN details to check his eligibility.
- When the referee turns from lead to borrower, the accountid corresponding to the phone number and PAN is also mapped against the referral link and code.
- Referee would be able to see a banner on top of the check eligibility page which mentions:
    - Reward amount: “Earn reward worth Rs.250 on opening loan account with Volt.”
    - Offer validity: Offer expires on “31t Mar, 2026”
- When a referral lead converts to an opportunity and enters [app.voltmoney.in](http://app.voltmoney.in) journey, he shall be able to view a banner in the homepage that mentions:
    
    “You have been referred. Complete your loan application above Rs. 25000 to earn Rs. 250. | Expires in {{x}} days”
    

**~~B2. Referree landing page~~**

**~~US 11:** *As a referee, I should be able to view that I have joined the Volt Money platform via referral with xx referrer code and yy name and eligible for reward on completing loan journey.*~~

**~~Acceptance Criteria:~~**

- ~~Referrer code and referree name attributed and visible on landing page/ home screen.~~
- ~~Info regarding Reward amount should be visible on completing loan journey.~~
- ~~If a user joins the Volt app via multiple referral links, then the latest referral code and referrer name should be attributed to the user until the user completes the pledge step. (Freezing referrerrefereeid post pledge step).~~
- ~~If a user has already completed pledge once via any other platform or volt and then again joins app via a referral link he won’t be eligible as a referee~~

**~~Frontend Requirements:~~**

- ~~Show referral code and referrer name on the homepage to referee.~~
- ~~Messaging to the user regarding earning reward amount Rs. xx on completing loan journey.~~

**~~Backend Requirements:~~**

- ~~Post pledge attribution to freeze the final referrerrefereeid.~~
- ~~Ineligibility condition for being a referee if a user has already completed pledge.~~

**C1: Nudges across lifecycle**

**US12:**  **As a user (referrer/ referee), I should get nudges from Volt across various touchpoints in order to be aware of the newly launched referral program and use the feature to refer one or more friends**

**Acceptance Criteria:**

1. The user will get notified about the newly launched referral program from Volt across various touchpoints in the lifecycle. The exhaustive list is mentioned in the [nudge framework](https://docs.google.com/spreadsheets/d/1YCbzXnTaOECPHkanXjUBM_IPv30cU8A5J1CI4Lgewt4/edit?gid=1191106196#gid=1191106196)

---

# **Design**

### Messaging and nudge framework

| # | Trigger | Message Name  | WhatsApp Copy | WATI Message BODY  | Note | Link to image | Text Messages  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | User clicks “Invite” | referral_share_message_with_image | 
Hey! I’ve been using Volt Money to get instant loan without selling my mutual funds💡

You can also check your loan eligibility in minutes and get ₹250 cashback on opening a loan account of ₹25,000 or more.

Check here: [link] 

Takes ~15 seconds, no impact on credit score | Hey! I’ve been using Volt Money to get instant loan without selling my mutual funds💡

You can also check your loan eligibility in minutes and get ₹{{cashback_amount}} cashback on opening a loan account of ₹{{minimum_loan_amount}} or more.

Check here: {{Link}}

Takes only ~{{time_in_seconds}} seconds, no impact on credit score |  | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=1437-698&t=oJZFrJ4CUW8TzFb0-11k |  |
| 2 | User clicks “Remind” | referral_reminder_message_with_image_ | Hey! You’re just one step away from ₹250 cash reward 💸

Takes less than 5 mins to claim it: [Link] | Hey! You’re just one step away from ₹{{cashback_amount}} cash reward 💸 

Takes less than {{duration_in_minutes}} mins to claim it: {{link}} . | Do not send it to ineligible folks? | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=3461-3373&t=oJZFrJ4CUW8TzFb0-11 |  |
| 3 | Campaign launch (all users) | referral_program_launch_with_image__ | **Introducing Volt Referrals !**

Now earn exciting rewards every time you refer a friend to Volt 

💰 ₹1,000 for every successful referral
🎁 ₹250 for your friend

And the rewards keep getting bigger:
🎧 AirPods on 5 referrals
📱 iPad on 25 referrals

Start sharing now: [link] | **Introducing Volt Referrals !**

Now earn exciting rewards every time you refer a friend to Volt 

💰 ₹1,000 for every successful referral
🎁 ₹250 for your friend

And the rewards keep getting bigger:
🎧 AirPods on 5 referrals
📱 iPad on 25 referrals

Start sharing now: [https://voltmoneyin.page.link/xzq5](https://voltmoneyin.page.link/xzq5) |  | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=1580-821&t=lvGA0ZwBLNfVFJfj-11 | Introducing Volt Referrals! Now earn exciting rewards every time you refer a friend to Volt, earn Rs.1,000 for every successful referral, while your friend gets Rs.250 too. And the rewards keep getting bigger, get AirPods on completing 5 referrals and an iPad on 25 referrals. Start sharing now: [https://voltmoneyin.page.link/xzq5](https://voltmoneyin.page.link/xzq5) |
| 4 | Reminder Message [ to be shared Biweekly] | reminder_message_biweekly_ | Volt Referral Program is Still LIVE !

Every successful referral brings you closer to exciting rewards 🚀

💰 ₹1,000 per successful referral
🎁 ₹250 for your friend

Plus unlock milestone rewards:
🎧 AirPods on 5 referrals
📱 iPad on 25 referrals

Start sharing now: [link]

 | Volt Referral Program is Still LIVE !

Every successful referral brings you closer to exciting rewards 🚀

💰 ₹1,000 per successful referral
🎁 ₹250 for your friend

Plus unlock milestone rewards:
🎧 AirPods on 5 referrals
📱 iPad on 25 referrals

Start sharing now: [https://voltmoneyin.page.link/xzq5](https://voltmoneyin.page.link/xzq5)

 | Should be shared to all LMS users Biweekly | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=1580-821&t=lvGA0ZwBLNfVFJfj-11 | Volt Referral Program is still LIVE! Earn Rs.1,000 for every successful referral while your friend gets Rs.250 too. Unlock exciting milestone rewards like AirPods on 5 referrals and iPad on 25 referrals. Check your Volt App and start referring now! |
| 5 | User activates loan | postactivation_nudge_with_image_ | 🎉 You’re all set on Volt!

Invite your friends and earn ₹1,000 for each one who gets started 💰 and they get ₹250 too 😉.

And it gets better:
🎧 AirPods at 5 referrals
📱 iPad at 25 referrals

Start sharing: [link] . | 🎉 You’re all set on Volt!

Invite your friends and earn ₹1,000 for each one who gets started 💰 and they get ₹250 too 😉.

And it gets better:
🎧 AirPods at 5 referrals
📱 iPad at 25 referrals

Start sharing: [https://voltmoneyin.page.link/xzq5](https://voltmoneyin.page.link/xzq5) | New users who signs up on volt  | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=1580-821&t=lvGA0ZwBLNfVFJfj-11 | You are all set on Volt! Invite your friends and earn Rs.1,000 for every successful referral while they get Rs.250 too. Unlock AirPods on 5 referrals and an iPad on 25 referrals. Check your Volt App and start referring now!
 |
| 6 | Referral successful | reward_unlocked_with_image | 🎉 You just unlocked ₹1,000!

Your friend has successfully activated their Volt account 💰Keep going!

Share more: [link] . | 🎉 You just unlocked ₹{{reward_unlocked_amount}}! 

Your friend has successfully activated their Volt account💰Keep going! 

Share more: {{link}} . |  | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=3461-3426&t=oJZFrJ4CUW8TzFb0-11 |  |
| 7 | Referral successful | reward_unlocked_airpods_with_image | 🎉 You just unlocked Apple Airpods!

Congratulations on completing 5 referrals! All the details for your Airpods will be sent to you soon. Keep an eye out.

Share more: [link] . | 🎉 You just unlocked {{apple_first_milestone}}! 

Congratulations on completing {{number_of_referral}} referrals! All the details for your {{first_milestone}} will be sent to you soon. Keep an eye out. 

Share more: {{link}} . |  | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=3461-15380&t=oJZFrJ4CUW8TzFb0-11 |  |
| 8 | Referral successful | **reward_unlocked_ipad_with_image** | 🎉 You just unlocked Apple iPad!

Congratulations on completing all milestones for our referral program! We are truly grateful for your contribution. All the details for your reward will be sent to you soon. 

Keep an eye out. | 🎉 You just unlocked {{apple_second_milestone}}!

Congratulations on completing all milestones for our referral program! We are truly grateful for your contribution. All the details for your reward will be sent to you soon. 

Keep an eye out. |  | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=3461-15398&t=oJZFrJ4CUW8TzFb0-11 |  |
| 9 | Refree 250 | reward_of_250_unlocked_with_image_ | 🎉Congratulations! 

You just won ₹250 cashback on completion of your loan application journey! 

All the details for your reward will be sent to you soon. Keep an eye out.
 | 🎉Congratulations! 

You just won ₹{{cashback_amount}} cashback on completion of your loan application journey! 

All the details for your reward will be sent to you soon. Keep an eye out. |  | https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=3461-3373&t=oJZFrJ4CUW8TzFb0-11 |  |
| 10 | Chase | referee_has_a_friend_with_status__signed_up___ | Looks like your friend, {name} just signed up! Remind them to complete their application soon to unlock your referral rewards! 

Offer valid only till: [DD/MM/YYYY]

Remind now - [Link to refer and now page]  | Looks like your friend, {{name}} just signed up! Remind them to complete their application soon to unlock your referral rewards! 

Offer valid only till: {{date}} 

Remind now - {{refer_now_page}} . |  |  |  |

### Copies for all statues

| **Status** | **To show or not** | **If yes, copy** |
| --- | --- | --- |
| Non eligible limit | yes | “Loan amount is less than ₹25,000 and hence this referral cannot be considered valid. T&C” |
| User already registered | yes | “This user is already registered with us please go through the T&C for further details”  |
| No active campaign  | nope |  |
| Referer not eligible for camp | nope |  |
| Campaign expired | yes | “User did not complete the loan application before the expiry date.” |
| Mapped with partner | nope |  |

https://www.figma.com/design/83PThQ37QfFdmvKFYYbuXf/Referral?node-id=117-122&p=f&t=XBsG82aT5ueY9BK8-0

---

# **Analytics**

---

**Amplitude events:**

Following are the list of **amplitude** events:

**Frontend:;**

[https://docs.google.com/spreadsheets/d/18FeTUwnTQ2_6Fe1R-GO_OAzQtWZusXBRkz37UdUTcuI/edit?gid=20280672#gid=20280672](https://docs.google.com/spreadsheets/d/18FeTUwnTQ2_6Fe1R-GO_OAzQtWZusXBRkz37UdUTcuI/edit?gid=20280672#gid=20280672)

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