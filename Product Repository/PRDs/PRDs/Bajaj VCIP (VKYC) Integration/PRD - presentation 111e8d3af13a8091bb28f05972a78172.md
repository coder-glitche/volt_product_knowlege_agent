# PRD - presentation

@Naman Agarwal 

# **Executive Summary**

Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge.

---

![Loan agaisnt MF journey  (1).png](Loan_agaisnt_MF_journey__(1).png)

# 1. **Objective**

- Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC.

---

# **2. Success Metrics**

Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs):

| Metric | Target | Measurement Method | Current Baseline | Priority |
| --- | --- | --- | --- | --- |
| **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical |
| **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High |
| **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High |
| **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium |
| **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High |
| **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High |
| **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High |

---

# **3. Background / Context**

- **Current Funnel**:
    1. **Digilocker KYC**: Users complete KYC through Digilocker.
    2. **Bank Account Verification**: The user's bank account is verified.
    3. **Pledge**: The loan collateral is pledged.
    4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed.
    5. **Mandate**: A mandate is established for loan repayment.
    6. **Disbursement**: Loan is disbursed to the user.
- **New Flow**:
    1. **Digilocker +Details + Video  KYC**: Users complete Digilocker KYC + Fill details + completes or “Skip for now“ V-KYC (Parallel).
    2. **Bank Account Verification**: The user's bank account is verified.
    3. **Pledge**: The loan collateral is pledged.
    4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed.
    5. **Mandate**: A mandate is established for loan repayment.
    6. **Disbursement**: Loan is disbursed to the use
- **Reason**:
    - Introducing V-KYC following the RBI guidelines

# 4. User stories

1. **Bajaj Assigned as Lender**: User is assigned Bajaj as the lender for their loan.
2. **Digilocker KYC Initiation**: User initiates the KYC process with Digilocker as the first step.
3. **Digilocker KYC Completion in Webview**: User completes Digilocker KYC within a Webview inside the app. 
4. **V-KYC**: User can choose to “continue to V-KYC” or “skip for now” and complete the rest of the steps of the application 
5. **Bank Account Verification**: User verifies their bank account information.
6. **Pledge Securities**: User pledges their securities as collateral for the loan.
7. **Agreement Signing**: User completes the Key Fact Statement (KFS) and agreement signing with Bajaj.
8. **Mandate Setup**: User sets up a repayment mandate.
9. **V-KYC Task Display**: V-KYC task is displayed to the user in parallel after completing the Digilocker KYC step.
10. **Loan Disbursement Block**: The loan disbursement is blocked until the V-KYC is successfully completed.

- **We can create a scheduling of V-kyc on our journey**
- Check permissions , what will fail the V-KYC
- Comms , resolving , scheduling frameworks , coms frameworks
- Can we trigger V-KYC
- Bharat Nishat , Brainstorm , what are the downsides of V-kyc . when should we make pre-requiestise

## Full KYC Specific User Journey

### Initial Digi - KYC Steps

1. User opens the KYC link.
2. Provides consent for KYC.
3. Logs into DigiLocker.
4. Enters UUID (DigiLocker Unique User ID).
5. Enters OTP received on their Aadhaar-registered mobile number.
6. Provides consent to share documents from DigiLocker.
7. User comes out of Bajaj KYC screens  - Break in Full KYC 
    - The KYC journey will be split into two stages to prevent initiating V-KYC during non-working hours (9 AM to 6:30 PM).
    - User will fill in the Details.
    - Incases of existing customers V-KYC will be skipped.
    - User select start V-KYC button on our screens
    - User selects V-KYC timing on  Bajaj screen :
        - **Start Now**: Begins V-KYC immediately, user provides permissions, and starts the call.
        - **Schedule Later**: User selects a slot from the available calendar for scheduling.

### "Schedule Later" Flow

- When the user chooses to schedule V-KYC for later, the selected time is received on a callback URL from Bajaj.
- The task "Complete Video KYC" will be displayed to the user as a pending action.
- The user can complete the V-KYC at any time; they are not bound by the scheduled slot.
- Once V-KYC is completed, the scheduled time is removed from the calendar.
- Users receive notifications 30 minutes, 10 minutes, and 5 minutes before their scheduled V-KYC time if they have not yet completed the process.

## V-KYC Placement Strategy

- V-KYC should be positioned to minimize drop-offs while maintaining a seamless user experience.
- Two potential places for introducing V-KYC in the Bajaj KYC flow:
    1. **After DigiLocker KYC** (recommended)
    2. **After the Agreement**

### Key Considerations:

- **DigiLocker KYC** is a prerequisite for starting V-KYC.
- V-KYC is mandatory before loan disbursement.
- V-KYC can only be completed during agent working hours (9 AM to 6:30 PM).
- Customers may need multiple attempts to complete V-KYC.

### Recommended Approach:

- **V-KYC after DigiLocker** with flexibility for users to complete it anytime before disbursement:
    - This avoids customer dissatisfaction, which might occur if V-KYC is introduced after the agreement when the user is expecting a payout.
    - Making V-KYC a parallel task after DigiLocker gives the user ample time during working hours to complete the process.
    - It aligns with the user’s expectation of completing the KYC steps in sequence.
    - Introducing a parallel task is technically new in the loan journey but offers more flexibility to the user.

## **V-KYC Scenarios**

- **Scenario 1**: User completes V-KYC within 72 hours of Digilocker KYC, and the process proceeds without any issues.
- **Scenario 2**: User completes V-KYC after 72 hours of Digilocker KYC. In this case, Digilocker KYC must be re-triggered, and a new transaction ID must be updated in Bajaj's SFDC system.
- **Scenario 3**: User fails V-KYC. In such cases, the V-KYC process can be retrigered up to 3 times. If the user fails all attempts, they will be moved to an operations bucket and will need to submit offline documents.

**Considerations for Improved User Flow**:

- If an e-PAN (electronic PAN) is provided during Digilocker KYC, users do not need to re-submit the PAN during V-KYC. This reduces redundancy and improves efficiency.
- If the video KYC is interrupted due to technical issues (e.g., connectivity), the process should be re-initiated promptly, with a notification to the user providing clear instructions on how to proceed.

## MFD Flows

- MFDs cannot complete V-KYC on behalf of their customers.
- MFDs can share a link to the customer for the web app, where the customer logs in to complete the V-KYC.
- MFDs can also share a direct V-KYC link with the customer. This direct link will reduce user confusion and ensure that MFDs are aware that V-KYC might not be available outside working hours.
- V-KYC access will be blocked from the MFD dashboard.
- The parallel task of completing V-KYC will be modified  to allow MFDs to share the V-KYC link directly with customers.

### Current Selfie Capture Process

1. MFD shares the link with the customer.
2. Customer receives the link, opens it, and logs in by verifying their phone number with an OTP.
3. The customer continues the application, completes KYC, and provides camera permissions.
4. Customer clicks the "Click Selfie" button, captures, and uploads the selfie.
5. Once the selfie is verified, the customer proceeds to the next steps.

### New V-KYC Process

1. After the customer completes DigiLocker KYC via the MFD, the Video KYC link is generated.
2. MFD shares the Video KYC link with the customer.
3. Customer receives the link and opens it.
4. Customer logs in using the pre-filled number and enters the OTP.
5. The V-KYC page opens, and the customer can proceed to complete the V-KYC.
6. MFD dashboard will be able to progress to next steps

## BAJAJ KYC POD API

Subscription Key

DIGILOCKER: - ‘aaa5-bbb5-ccc5-ddd5’

V-CIP - 'aaa3-bbb3-ccc3-ddd3'

---

## 5. **Risks and Dependencies**

- **Dependencies**: Integration with Bajaj's V-KYC API, and Webview compatibility testing.
- **Risk**: Increased user drop-offs if the V-KYC process is not intuitive or convenient.
- **Open Dependencies**:
    - Confirm with Bajaj regarding address verification via API.
    - Testing required for Webview compatibility and usability for Digilocker KYC.
    - Assess potential technical limitations of Bajaj's KYC POD API and whether adjustments are required to streamline V-KYC processing.

---

### 6. **Next Steps**

- Test and add all the steps
- Finalize the integration details with Bajaj.
- Design UI changes for the V-KYC flow.
- Develop and test the customer journey thoroughly.
- Confirm with Bajaj's development team regarding address verification and transaction ID updates.
- Follow up with market research findings on alternative V-KYC solutions and assess their applicability.

### **7. Competitive Analysis**

**Industry Practices:**

- **Minimal KYC (Min-KYC)**: Some lenders like Tata and Navi use offline XML/Digilocker flows without V-KYC.
- **Full KYC without V-KYC**: Lenders like InCred and Cashe rely on offline XML/Digilocker with liveliness checks.
- **Full KYC with V-KYC**: Larger lenders implement full V-KYC sessions with agents.

**Insights:**

- **Customer Experience**: Lenders offering flexible V-KYC scheduling see higher completion rates.
- **Best Practices**: Clear communication, user-friendly interfaces, and efficient support significantly reduce drop-offs.

**Opportunity:**

By implementing a customer-friendly V-KYC process with flexible scheduling and strong support, Volt Money can outperform competitors and enhance customer loyalty.

---

### **8. Stakeholder Impact Analysis**

**Customers:**

- **Benefits**: Flexible scheduling, clear instructions, and minimized process disruption.
- **Challenges**: Adjusting to the new requirement of a video call with an agent.

**Mutual Fund Distributors (MFDs):**

- **Benefits**: Access to training and tools to assist customers.
- **Challenges**: Adapting to a process where customers need to complete V-KYC themselves.

**Internal Teams:**

- **Operations**: Need to manage new workflows and ensure compliance.
- **Customer Support**: Increased queries initially but reduced over time with effective communication.
- **Development**: Integration with Bajaj 's APIs and system adjustments.

---

### **9. Implementation Plan**

---

**Phase 1: Planning and Design** 

- **Finalize Integration Details**: Collaborate with Bajaj to understand API requirements.
- **User Interface Design**: Develop wireframes and user journey maps.
    - Handling of KYC - rejects - error screen - send for review
    - Handling of KYC API failure - Support
    - Loading screens for V-kyc response
    - Task routing on user dashboard
    - stepper, Half done task state , pending
- **Tech review**

**Phase 2: Development** 

- **API Integration**: Connect with Bajaj's V-KYC APIs.
- **Dashboard Enhancements**: Implement the task dashboard and notifications.
- **Backend Processing**: Set up events

**Phase 3: Testing** 

- **Internal Testing**: Validate workflows, error handling,
- **User Acceptance Testing (UAT)**

**Phase 4: Training and Preparation**

- **MFD Training**: Conduct webinars and provide training materials.
- **Staff Training**: Prepare customer support and operations teams.

**Phase 5: Launch** 

- **Soft Launch**: Introduce the new process to a select user segment.
- **Full Rollout**: Expand to all users after resolving initial issues.

**Phase 6: Post-Launch Monitoring (Ongoing)**

- **Performance Tracking**: Monitor KPIs and adjust strategies accordingly.
- Feedback: Implement enhancements based on user feedback.

---

### **10. Customer Communication Strategy**

- **Pre-Launch Awareness**: Notify existing MFD customers about upcoming changes via email and in-app messages.
- **In-Process Guidance**: Provide clear instructions, tooltips, and FAQs during the KYC process.
- **Multi-Channel Notifications**: Use SMS, email, and WhatsApp for reminders and updates.
- **Support Accessibility**: Ensure easy access to customer support through chat, phone, and email.
- **Feedback Mechanisms**: Collect customer feedback to identify pain points and areas for improvement.

# 

### 11. Estimates

We are awaiting to tech review  create detailed Jira tickets 

---

### **12. Training and Change Management**

- **Employee Training**:
    - PDF, Video to explain V-KYC Process. SOP for Error codes
    - V-KYC fail Change lender flow SOP
- **MFD Support**:
    - RM can educate MFDs

---

### **13. Next Steps and Action Items**

- **Clarify Open Questions**:
    - **API Details with Bajaj**: Finalize technical specifications and capabilities.
    - **Error Handling Protocols**: Obtain detailed error codes and responses.
    - **Service Availability**: Confirm V-KYC agent working hours.

---

### **14. Appendices**

## **Appendix A: Error Codes**

**DigiLocker API Error Codes:**

- **Unified_API_Error**: General API failure.
- **Bitly_API_Error**: URL generation/sending failure.
- **Link Sent Successfully**: DigiLocker link sent.

**V-KYC API Error Codes:**

- **Agent_Not_Available**: No agent available.
- **Maker_Result_Rejected**: Initial review rejected.
- **Audit_Result_Rejected**: Audit rejected.
- **KYC_Result_Rejected**: KYC issues.
- **Link_Initiated**: V-KYC link sent.
- **Session_Started**: V-KYC session in progress.
- **Schedule_Mode_Activated**: V-KYC rescheduled.
- **Audit_Result_Approved**: Audit approved.

## **Appendix B: Regulatory References**

- **RBI Master Direction – Know Your Customer (KYC) Direction, 2016**: [Link](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566#)

## **Appendix C: User Journey Wireframes**

*(Wireframes to be attached separately or included in the presentation slides.)*

---

### **Conclusion**

Implementing V-KYC is a strategic imperative for Volt Money to comply with RBI regulations and enhance our competitive position. By focusing on customer experience, stakeholder engagement, and meticulous planning, we aim to integrate V-KYC seamlessly into our processes. This initiative aligns with our mission to provide efficient financial solutions and positions us for sustained growth.

- V-kyc , failes

| [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers |
| 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end |
| 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification |  |
| 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address |  |
| 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call |  |  |
| 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team |  |  |
| 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response |  |  |
| 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC.
 - If the user chooses "Do V-KYC later" or skips, start at the end. 
- Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and require more development time. | - Keep the existing flow until the Mandate and Agreement steps.
- Trigger V-KYC after the Agreement as a new step. 
- Add V-KYC to the stepper. 
- Pros: Easier to develop. 
- Cons: Frustration after agreement and document steps; stepper may look complicated.  |  |
| 9 | B2B2C, For MFD to get V-KYC of Users |  |  | MFD can send link to the users to get the V-KYC from customer |  |  |
|  | B2B |  |  | In case we have do not permissions in the Partner journey then we need to send comms to user to get V-KYC, Our SDK permissions - getting from saagar |  |  |
|  | UAT TESTING  |  | V-KYC till agent call is working. As no agents are provided in UAT we are unable to have a end to end test  |  |  |  |

- bajaj unpledges after a month , we don’t get any updates form bajaj
- User is very likely to escalate in cases where there money is pledged
- we need to have. more nimble comms strategy

we have set pledge to be a step after things which can be rejected as users need to be invested to complete the process. 

decision points

should we allow users to Pledge without completing V-KYC ?

if not, then should we move the Pledge to after the mandate

What happens after pledge is moved after the mandate ?

what happens when user comes to the flow outside working hours ?

should we build own scheduler ?

if not then are we ok with bajaj’s comms?

If yes then how will be contact users? IVR need dev, PNs will be less effective 

what can go wrong in V-KYCs ?

- User can drop off mid v-kyc
- user can not initate V-kyc
- User can not respond to PN and notifications for V-KYC
- user might not have the stable internet connection
- user might have device permission issues
- Agent might have difficulties in Audio, video of the user , rejecting V-kyc
- user might answer questions wrong in VCIP
- How will they tell us about failure
- map the ideal journey , bajaj and propose, build
- Mail to kapi , shipvansh, nishast , business , walk through them
- kick off with tech , ops, sales , rms,
- release note and training

Ideal flow 

- user has to do V-KYC , they completes it
- user has to do v-kyc , they reschule it , when user reschedule they have. a list of slots they select the slot and we remind them of the slot booked , iuser can somplete the

- V-KYC is a addtinal step that user has to take in bjajaj lender flow
- we provide loan agaisnt securities with lending partner bajaj
- user has to complete there KYC to get the loan
- current steps are
    - Digiloacker KYC (Half KYC) + user details
    - bank account verification
    - Pedging of secureities
    - agreement
    - manadate setup on account
    - disbursement after bajaj confirmation
- Pledging is moved ealier to achive a buyin form customer to complete the application
- is user drops off or want to unpledge then it a very expensive operational process to remove pldge and is dpendant on bajaj. user can’t use or sell those securioties in the intrim
- we placed pledge to just after major rejection reasons for a cusotmer
- we are advised to include v-kyc beofre pledge ,
- user cannot take a disbursment before the V-kyc is comlete
- User has to complete v-kyc with 72 hrs of digiglocker , in working hours 9 am to 6 pm
- if user misses 72 hrs from digiloacker then we have to do digiloacker + vkyc again
- if user is not completing the Vkyc instantly we have to reengage them and have them complete vkyc
- we need to increase buyin form cusotmers as well so that they don’t drop off
- we also don’t want user to wait after mandate and pledge for disbusremeennt
- we need to handle the Vkuyc failures

Identify the current friction points for customers (time limits, re-engagement).

- V-kyc is not avaible 24/7 , need 9 am to 6 pm on bank working days

Ensure all stakeholders (you, Bajaj, and the customer) are clear on roles and timelines.

- stekholder
    - volt
    - bajaj
    - Partner SDKs
    - Ops team
    - sales team
    - support team
    - tech team
- smoother transitions for V-KYC
    - Bajaj V-kyc can be similar to digilicker as current , then for V-kyc has 2 opriotns of start now (avaible during work hours) and schedule later,—> book slots .

Drop-off rates at various points, especially around the DigiLocker to V-KYC stage.-  no idea, as V-kyc is not live yet , we can get the data from digiloacker to pledge 
•	

- How often do pledges occur but V-KYC is missed?-  not supposed to happen but 05%
•	Costs associated with un-pledging and delays. - no cost , operation cost of agent , minimum 3 days max 7 days

| current  | proposed earlier |  | Proposed  |  | alternate 1 |  | alternate 2  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | pros:-  provide ample time for VCIP, 
cons- have to un-pledge for dropped off customers. |  | pros: reduced ops costs , cons , reduced customer buy-in  |  | pros, forces customer to complete VCIP, but more drop-off if in off working hrs / customer unavailable ,  |  | pros no parallel tasks , but customer drop off incases of non availability and off work ours  |
| Digilocker  | digilocker  |  | Digilocker  |  | Digilocker  |  | Digilocker |
| bank account verification  | Bank account verification  | V-kyc  | Bank account verification  | V-kyc  | Bank account verification  | V-kyc  | V-kyc  |
| Pledge | Pledge | V-kyc  | agreement | V-kyc  | Pledge |  | Bank account verification  |
| agreement  | agreement | V-kyc  | mandate  | V-kyc  | agreement |  | Pledge |
| mandate  | mandate  | V-kyc  | Pledge |  | mandate |  | agreement |
| disbursement | disbursement |  | disbursement |  | disbursement |  | mandate |
|  |  |  |  |  |  |  | disbursement |

**1. Segment Users Based on Drop-Off Points**

Each stage of your loan process has its own unique challenges, so it’s essential to create **user segments** based on where they drop off. Different stages require different approaches.

•	**Segment 1**: Users who complete **DigiLocker KYC** but drop off before starting V-KYC.

•	**Segment 2**: Users who start **V-KYC** but don’t complete it.

•	**Segment 3**: Users who complete **V-KYC** but drop off before **pledging**.

•	**Segment 4**: Users who finish the process but experience delays before **disbursement**.

## Engagement channels

- **Push Notifications** (Mobile App): Ideal for customers who actively use your app.
- **SMS/Text Messages**: Quick, direct reminders for time-sensitive steps like V-KYC, pledging, or agreement completion.
- **WhatsApp:** More conversational, allowing a personalized touch. WhatsApp can provide a convenient method for users who may prefer this channel for interaction.
- **Emails**: Best for detailed reminders with clear instructions on how to continue. Emails are effective for explaining steps, highlighting benefits, and even offering incentives.
- **IVR or Phone Calls**: Automated IVR reminders or a phone call from customer service can provide a direct, human touch for users who haven’t responded to digital reminders.

**Segment 1: Users Who Complete DigiLocker KYC but Drop Off Before Starting V-KYC**

**Challenges:**

These users have started the process but may be unaware of the urgency or importance of V-KYC. They need a **friendly nudge** to take the next step.

**Engagement Messages:**

•	**Push Notification**:

•	“You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes!”

•	**SMS/Text**:

•	“Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link]”

•	**WhatsApp**:

•	“Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC]”

•	**Email**:

•	Subject: **[Name], Your Loan is Almost Ready! Complete V-KYC to Continue**

•	Body: “Hi [Name], great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC]”

•	**IVR/Phone Call**:

•	“This is a reminder from [Company]. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist.”

**Segment 2: Users Who Start V-KYC but Don’t Complete It**

**Challenges:**

These users may have encountered **technical difficulties** or **time constraints**. They started the V-KYC but didn’t finish it, so they need **quick support** and encouragement to resume.

**Engagement Messages:**

•	**Push Notification**:

•	“Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link]”

•	**SMS/Text**:

•	“Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link]”

•	**WhatsApp**:

•	“Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link]”

•	**Email**:

•	Subject: **Complete Your V-KYC Now for a Faster Loan Approval**

•	Body: “Hi [Name], you’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help.”

•	**IVR/Phone Call**:

•	“This is a reminder from [Company]. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish it? Contact us for any assistance you need.”

**Segment 3: Users Who Complete V-KYC but Drop Off Before Pledging**

**Challenges:**

These users have gone through the verification process but haven’t pledged their securities. This might be due to **uncertainty** or a lack of commitment, so they need reassurance about the process and clear calls to action.

**Engagement Messages:**

•	**Push Notification**:

•	“You’re one step away from securing your loan, [Name]! Pledge your securities now and finalize your application. [Link]”

•	**SMS/Text**:

•	“Hi [Name], your V-KYC is complete! Now pledge your securities to finalize your loan process. It’s quick and easy! [Link]”

•	**WhatsApp**:

•	“Hey [Name], congrats on completing your V-KYC! Just one more step—pledge your securities to move forward. Need more info or help? We’re here for you. [Link]”

•	**Email**:

•	Subject: **You’re Almost There! Pledge Your Securities to Secure Your Loan**

•	Body: “Hi [Name], great news—you’ve successfully completed V-KYC! Now, all that’s left is to pledge your securities to finalize the process. Once you do that, your loan disbursement is just around the corner. [Link to pledge] Have questions? Reach out to our team for support.”

•	**IVR/Phone Call**:

•	“This is a reminder from [Company]. Your V-KYC is complete, and we just need you to pledge your securities to finish your loan application. Need assistance? Contact us!”

Here is the customer segmentation table for V-KYC along with what to communicate with them at each stage:

| **Segment** | **Behavior** | **Potential Issues** | **Message to Communicate** |
| --- | --- | --- | --- |
| **Segment 1: Users Who Complete DigiLocker KYC but Drop Off Before Starting V-KYC** | Completed DigiLocker KYC but haven’t started V-KYC. | Lack of urgency, confusion about next steps, distractions. | "Complete your V-KYC to move closer to loan disbursement! It's a quick and important step for loan approval." |
| **Segment 2: Users Who Start V-KYC but Don’t Complete It** | Started V-KYC but dropped off midway. | Technical difficulties, time availability, confusing process. | "You're almost there! Continue your V-KYC to get one step closer to securing your loan. Need assistance? We're here!" |
| **Segment 3: Users Who Fail V-KYC** | Attempted V-KYC but failed due to technical or verification issues. | Verification failures (mismatched details, video quality, etc.), system glitches. | "We noticed some issues with your V-KYC. Don't worry, here's how to fix it and try again!" |
| **Segment 4: Users Who Complete V-KYC but Drop Off Before Pledging** | Completed V-KYC but haven’t pledged securities. | Uncertainty about pledging, financial concerns, fear of commitment. | "Pledge your securities to finalize your loan. It's safe, secure, and moves you closer to disbursement." |
| **Segment 5: Users Who Complete V-KYC and Pledge, But Don’t Complete the Agreement** | Completed V-KYC and pledge but haven’t signed the agreement. | Hesitancy to formalize the loan, concerns about terms. | "Just one more step! Review and complete the agreement to finalize your loan approval." |
| **Segment 6: Users Who Complete V-KYC, Pledge, and Agreement, But Drop Off Before Mandate Setup** | Completed V-KYC, pledge, and agreement but haven’t set up the mandate. | Technical issues with mandate setup, confusion about the process. | "Set up your bank mandate to allow smooth loan disbursement. Here’s how to do it easily." |
| **Segment 7: Users Who Complete V-KYC and Mandate Setup, But Drop Off Before Loan Disbursement** | Completed everything but awaiting disbursement. | Lack of clarity on disbursement timing, operational delays. | "Your loan disbursement is almost complete. Here's when to expect it!" |
| **Segment 8: Users Who Fail to Complete V-KYC Within 72 Hours** | Did not complete V-KYC within the 72-hour window. | Missed working hours, scheduling conflicts, confusion about deadline. | "Time is running out! Schedule your V-KYC now to avoid starting the process again." |
| **Segment 9: Users Who Complete DigiLocker KYC but Abandon V-KYC After Missing the 72-Hour Window** | Missed 72-hour window and abandoned V-KYC. | Frustration, overwhelmed by the process, lack of motivation. | "It’s easy to restart your V-KYC! We’ll help you complete it and move forward with your loan." |
| **Segment 10: Users Who Restart V-KYC After Failing or Missing the Deadline** | Restarted V-KYC after failure or missed deadline. | Discouragement from earlier failure, doubts about completing V-KYC. | "You’re doing great! Let’s get your V-KYC done smoothly this time. Need help? We’re here!" |
| **Segment 11: Users Who Complete V-KYC but Delay Resuming the Loan Process** | Completed V-KYC but are unresponsive or not progressing the loan process. | Lack of urgency, personal distractions, disinterest. | "Don’t lose your progress! You’re almost done, finalize your loan now for quick disbursement." |
| **Segment 12: Users Who Are Unavailable During V-KYC Hours (Off-Hours Inactivity)** | Unable to complete V-KYC during working hours (9 AM – 6 PM). | Scheduling conflicts, time-zone issues. | "Can’t do V-KYC during working hours? Schedule a convenient time for your V-KYC now." |
| **Segment 13: Users Who Have Repeated V-KYC Failures Due to Technical Issues** | Repeatedly failed V-KYC due to technical issues. | Frustration, poor video quality, mismatched documents, technical issues. | "Let’s fix those technical issues and get your V-KYC done right. Here’s a guide for a smooth process!" |

These messages are designed to address user-specific concerns at each stage and guide them toward completing their loan application successfully.

when it comes and how it comes