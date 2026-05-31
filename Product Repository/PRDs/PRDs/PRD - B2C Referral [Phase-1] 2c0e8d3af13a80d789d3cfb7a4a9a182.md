# PRD - B2C Referral [Phase-1]

: Devansh Kar
Created time: December 5, 2025 4:00 PM
Status: In progress
Last edited: December 10, 2025 8:08 AM

# **What problem are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt does not have any mechanism to leverage its existing loan users base who has experienced the value of Volt Money LAMF product for new user acquisitions.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new users to borrow LAMF from Volt as a trusted brand and limited period reward offers will assist in fast-tracking the loan account completion process.

Both **Referrers** and **Referees** need a seamless, trackable referral experience with transparent rewards.

---

# **How do we measure success?**

**Primary KPI**

- 1000 signups via referral (Alpha)
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

**US 1: As a user, I want to be automatically enrolled into a referral program and applicable rewards for the referral program as per Volt’s rule engine decisions.**

**Acceptance Criteria:**

- User will be eligible for a referral program with applicable conditions basis on rules/ parameters set by backend.
- User should have opened a loan account with Volt. [1st Referral program launch] (Configurable capability, for extending to users at any application stage)
- User must be auto-assigned a unique referral code which should be generated only once per user as soon as he is eligible under any referral program.
- Referral program and its conditions should be applicable and active only during program-active window.
- For users under multiple active referral program, priority parameter should exist for a referral program to decide user eligibility for a particular referral program.

**Frontend:**

- Show referral card (entry point) only to eligible borrowers with applicable banner corresponding to the program. [Phase 1: LMS Dashboard]

**Backend:**

- Auto-generate referral code and unique referral link for all eligible users mapped to/ falling under any referral program (at AccountID level).
- Priority based eligibility to decide the referral program applicable for a user (If a user is eligible under multiple active referral programs).
- Platform attribution as a parameter should be passed for eligibility for users.
- Capability to activate/ deactivate a referral program.

**Parameters** for a referral program config:

```jsx
"platformcode": {"Volt B2C Web","Volt B2C App", "Volt PhonePe"} 
"usertype": {"borrower", "opportunity"}
"stepid": ""
"startdate": "01-01-2025"
"enddate": "31-03-2025"
"bannerid": "banner123"
"numberofmilestonesteps": 25
"milestone1": 5
"milestone2": 25
"referrerrewardtype1": "cash"
"referrerrewardtype1amount": 1000
"referrerrewardtype2":
"referrerrewardtype2amount":
"milestonerewardtype1": "physical"
"milestonerewardtype1amount": "airpods"
"milestonerewardtype2": "physical"
"milestonerewardtype2": "ipad"
"refereereward": 250
"referrerrewardvaliditydays": 30
"refereerewardvaliditydays": 30
```

**A2) Referral Discovery**

**US 2: As a user, I want to get notified about being eligible for Volt’s referral program.**

**Success Criteria:**

- When a user gets eligible for a referral program for the first time, he needs to get notified via external channels — Whatsapp, Push Notifications, SMS at intervals [once every T0, T0+1 day, T0+2 days, T0+4 days, T0+7 days, T0+15 days, T0+30 days]
- When user gets eligible for a referral program for the first time, he needs to get notified via In-App nudges (Nudge architecture- dev effort check).

**Backend:**

- Auto-trigger notifications to referral program eligible users at defined intervals via external channels (Whatsapp - Wati integration) and (SMS - Gupshup integration), and existing PN infra. [T0, T0+1 day, T0+2 days, T0+4 days, T0+7 days, T0+15 days, T0+30 days].
- In-App nudges to be triggered to the user at same intervals as above. (Nudge architecture - dev effort check).

**US 3: As a user, I want to see the a) entry point, b) landing page images/ banners, and c) validity period specific to the referral program/ campaign I am currently eligible for.**

**Success Criteria:**

- User should see the entry point and landing page image/ banner configured corresponding to the active referral program he is eligible for.
- User should be able to see the validity period of referral program/ campaign (if any) he is eligible for on entry point and landing page. [To start the first referral program will be valid from Jan 1st to 31st Mar 2026].

**Frontend:**

- Show image(s)/ banner configured for a referral program that user/ borrower is eligible for at entry point [banner/ card], and landing page. [Phase 1: LMS Dashboard]
- Show validity period [if any] configured for a referral program at the entry point image and landing page placeholder to the eligible user. [Fetched from Referral program table].

**Backend:**

- A table called Banners corresponding to an API endpoint needs to be created with request parameters as image uploads input (jpeg/png format):

**Sample Request-**

```jsx
"entrypoint_image": "xyz.jpeg"
"landingpage_image": "abc.jpeg"
```

**Sample Response-**

```jsx
"bannerid": "BANNER_123"
```

- Validity period of the referral program should be fetched from conditions passed in parameters for an active Referral program. [**US 1 Backend reference**]

**US 4: As a user, I want to get clarity on Terms & Conditions of the referral and reward program/ campaign I am eligible for.**

**Success Criteria:**

- The applicable terms and conditions of the specific referral program a user is eligible for should be reflected on the T&C page/ section of the referral program.

**Frontend:**

- List of text with variable fields within it, which might change for every referral program based on config done in the BE for the specific referral program/ campaign.
- List of T&C includes:
    - Validity of the program
    - Successful referral definition (All loan account opened before {{x}} date and above {{y}} amount)
    - Referee eligibility conditions
    - Rewards eligibility conditions
    - Rewards validity ({{x}} days from reward unlock date : x = 30 for 1st launch

**Backend:**

- All the values of the variable fields in the frontend text of T&Cs should be reflected by configuration data sent from BE for a referral program.

**A3) Referral link sharing method**

**US 5: As a referrer, I want to easily share my referral link/code through WhatsApp, SMS, or Copy unique code and link so that I can invite friends.**

**Success Criteria:**

- Dynamic link must contain/ have mapping to referral code + UTM + channel.
- Share sheet opens natively and must support WhatsApp, SMS, Copy Link. (Mobile and Web) [Check with FE]
- Tracking events-  `referral_link_shared`, `referral_link_clicked` , etc. must fire with metadata. [Check]
- Message template configured for referrer for sending to referee across channels.

**Frontend:**

- UI: “Invite now” button which opens native sheet with WA/SMS/Copy options.
- Display share UI.
- Redirect to respective mobile application (Whatsapp, Gmail, SMS etc.) if shared via Mobile app platforms
- Redirect to webapp links (Web.whatsapp, gmail.com) if opened in browser (desktop/mobile)
- Show copy-to-clipboard success toast.

**Backend:**

- Generate Firebase Dynamic Link with UTMs attribution parameters.
- Maintain mapping: referrer_id → link_click→ timestamp.
- Log events.

**A4) Track Referee Progress**

**US 6: As a referrer, I want a dashboard showing all successful referrals, milestone tracking as well as each referees’ progress in the application journey (Signup → KYC_Completed → Loan_Disbursed) so that I know who is close to earning me rewards.**

**Success Criteria:**

- Show a consolidated view of the successful referrals with “View details” CTA in the landing page to track all referrals.
- Show milestone tracker to the referrer based on each successful referral, and reward unlocked in the landing page.
- Clicking on “View details” will show a page having consolidated view of each referred application by the referrer and their current status/ stage updated at real time. The statuses are namely:
    - Signed Up → KYC Completed → Account opened
- Invalid/ Expired referrals are also marked corresponding to the respective referral. [Universal across all referral programs].
- Users who opened account with < Rs.25000 will be counted in Invalid referral and the messaging for the same should be displayed to the user.
- As soon as the loan amount of opened account of an invalid referee ≥ 25000 via enhancements/ updated DP logic, then it would be updated as a successful referral.
- Whatsapp comm and In-App notification should be triggered to the referrer for each successful referral (referee loan account creation ≥ 25000).

**Frontend:**

- Successful referrals number in a card on landing page with “View details”.
- Milestone tracker for referrer showcasing number of successful referrals and reward unlocked.
- View details section show - Distribution of successful, in progress and expired/ invalid referrals.
- 3 statuses corresponding to each application in In-Progress/ Success state/ Invalid state [Signed Up → KYC Completed → Account Opened]
- If opened account by referee is of amount <25000, then the same messaging should be communicated to the referrer.
- In-App nudge for each successful referral completion.

**Backend:**

- Update status on each event/ stepid completion:
    - Signed Up
    - KYC Completed
    - Account opened
- Maintain referee_status column in the borrower accounts/ opportunities table.
- Integration with Whatsapp to send comms to referrer for successful referral.

**US 7: As a referrer, I want to nudge people at application stage that I have referred, to complete loan application so that I can avail rewards fast.**

**Success Criteria:**

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

**US 8: As a referrer, I want my reward (Cash/ Physical) to get unlocked and tracked as soon as each referee opens a loan account ≥ Rs. 25000 within the validity period of the referral program.**

**Success Criteria:**

- Referee opening account of loan amount ≥ Rs. xxxxx (Rs. 25000) for now within validity period of the program (31st March for the 1st program) will lead to unlocking reward for referrer.
- Enhanced loan amount by referee to ≥ Rs. 25000 within stipulated reward program validity will also be counted as a success referral and both referrer and referee will be eligible for reward even if the previous loan amount of account opened by referee <25000.
- Notification (Whatsapp + In-App) should be triggered to the referrer once a new reward is unlocked.
- Celebration popup with animation for milestone rewards.
- Reward tracker for the referrer should be available under rewards section showing rewards with statuses (Eligible, Expired, Claimed, Processed) and date of expiry.

**Frontend:**

- In-App notification when a reward is unlocked.
- Summary of success rewards amount (Amount + Physical rewards)
- Current status of unlocked reward to be shown (Eligible, Expired, Claimed, Processed).
- Date of expiry to be shown for each unlocked reward.
- Milestone tracker should show unlocked reward.

**Backend:**

- Rewards table should contain all successful referral for a borrower/ opportunity with referrerid should unlock the reward with status “Eligible” or “Expired” and expiry period as (T0+{{x}}) x= 30 days.
- Whatsapp and push notification trigger on unlocking each reward.

**A6) Claim Reward (Normal (Cash) + Milestone)**

**US 9: As a referrer, I want to claim my unlocked cash reward into my bank account and milestone (physical reward) dispatched to my address so that I receive my earnings easily.**

**Success Criteria:**

- Claim All CTA option for users to claim all the rewards/ cash amount.
- Placeholder to enter address for claiming physical/ milestone reward.
- Messaging to the user showing “Your reward will be processed in 24 hours” for normal cash rewards
- Messaging to the user showing “Your reward will be delivered in 7 days” for milestone (physical) rewards
- Reward tracker for the referrer should be available under rewards section showing rewards with statuses (Eligible, Expired, , Claimed, Processed) and date of expiry.
- A file calculating total reward amount + physical reward at a user level should be from backend at the end of the day to Ops.
- A reverse file confirming the UTR of transaction should be uploaded from ops end showing for success rewards at end of next day (T+1)
- Notification (Whatsapp + In-App) should be triggered to the referrer once a new reward is processed.
- Dispatching of physical rewards via delivery partner should be updated along with cash rewards on a weekly basis.

**Frontend:**

- In-App notification when a reward is processed.
- Current status of unlocked reward to be shown (Eligible, Expired)

**Backend:**

- Backend should keep track of claimed rewards and processed rewards based on file uploaded by Ops via mechanism (Sharing UTR and AWBnumber success).
- Whatsapp and push notification trigger on processing each reward.

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