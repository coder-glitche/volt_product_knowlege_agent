# Bajaj VCIP (VKYC) Integration

: Gautam Mahesh
Created time: September 27, 2024 5:30 PM
Status: In progress
Last edited: May 5, 2025 11:56 AM
Owner: Naman Agarwal

[ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md)

[https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225)

[API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md)

[VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md)

# Product Requirements Document (PRD)

![Loan agaisnt MF journey  (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png)

## **Table of Contents**

## **Executive Summary**

Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms.

---

## **1. Objective**

- **Primary Goals:**
    - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols.
    - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates.
    - **Operational Efficiency:** Streamline backend operations and reduce manual interventions.
    - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC.

---

## **2. Challenges**

### **Regulatory and Operational Constraints**

1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory.
2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC.
3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM).
4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj.

### **Technical and User Experience Challenges**

1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms.
2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users.
3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns.
4. **Re-Engagement:** Effectively re-engaging users who abandon the process.

---

## **3. Solution**

### **Proposed Approach**

Loan application Flow 

1. Digilocker
2. BAV
3. Pledge
4. Agreement
5. Mandate
6. VKYC - New
7. Disbursement

Key Points 

- Reduced  top of the funnel drop
- Reduced number of Leads for sales for VCIP step improving sales efficiency

**~~Loan Application Flow:~~**

1. **~~DigiLocker KYC:** Initial KYC verification.~~
2. **~~V-KYC:** Users can either:~~
    - **~~Start Now:** Immediate V-KYC session.~~
    - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~
3. **~~Bank Account Verification (BAV):** Verify bank details.~~
4. **~~Agreement:** Sign loan agreement.~~
5. **~~Mandate Setup:** Set up automatic debit mandate.~~
6. **~~Pledge:** Final pledge of securities.~~
7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~

**~~Key Components:~~**

- **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~
- **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before locking securities.~~
- **~~Robust Re-Engagement Mechanisms:** Automated reminders and support to encourage completion of V-KYC.~~
- **~~Comprehensive Error Handling:** Address potential V-KYC failures with clear guidance and support.~~

**~~Benefits:~~**

- **~~Regulatory Compliance:** Meets all RBI and Bajaj requirements.~~
- **~~User-Centric:** Flexible options enhance user experience and reduce drop-offs.~~
- **~~Operational Efficiency:** Streamlined processes minimize costs and manual efforts.~~
- **~~Competitive Advantage:** Superior KYC process differentiates Volt Money in the market.~~

### Alternate approach

- We keep Develop the BE to enable V-KYC first
- We keep the journey as
    - Digilocker
    - V-KYC
    - BAV
    - Pledge
    - Agreement
    - Mandate
    - Disbursement

Benefits 

- Reduced development effort across BE and SDKs
- Bajaj Loan creation API require Pledge data

---

## **4. Requirements**

### **1. Integration Module**

- **API Integration:**
    - Connect with Bajaj’s V-KYC APIs (`aaa3-bbb3-ccc3-ddd3`).
    - Handle initiation, scheduling, and status tracking of V-KYC sessions.
    - Manage transaction IDs and synchronize with SFDC.

### **2. User Interface (UI) Module**

- Task stepper: TBD
- **V-KYC Scheduling Interface - provided by Bajaj (Testing required)**
- **V-KYC Session Screen -provided by Bajaj (Testing Required)**
- **Error Screens: TBD**

### **3. Backend Processing Module**

- **Real-Time Updates:**
    - Webhook listeners or API polling to receive V-KYC status updates.
    - Update user status upon V-KYC completion or failure.
- **Event Tracking - to trigger Comms**
- **Re-Engagement Logic: TBD**

### **4. Mutual Fund Distributors (MFD) Module**

- **MFD Dashboard Enhancements:**
    - Tools for MFDs to generate and share V-KYC links.
    - Track V-KYC progress within the MFD interface.
- **Training and Resources:**
    - Comprehensive training materials (documentation, video tutorials).
    - Conduct webinars and training sessions for MFDs.
- **Error Handling and Retriggering:**
    - Automated workflows to notify MFDs of V-KYC errors.
    - Enable MFDs to retrigger V-KYC sessions if necessary.

### **5. Error Handling Module**

- **Error Code Management:**
    - Map API error codes to user-friendly messages.
    - Provide clear instructions for resolving each error.
- **Rescheduling and Updates:**
    - Allow easy rescheduling of V-KYC sessions.
    - Update user dashboard in real-time to reflect changes.
- **Technical Issue Mitigation:**
    - Checks for internet connectivity and device permissions.
    - Fallback options for persistent technical issues.
- **User Feedback Collection:**
    - Enable users to report issues directly through the app.
    - Use feedback to identify and address recurring problems.

---

## **5. Success Metrics**

| **Metric** | **Target** | **Measurement Method** | **Priority** |
| --- | --- | --- | --- |
| **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | Critical |
| **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | High |
| **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | High |
| **Average Time to Complete KYC** | 5-7 minutes (DigiLocker) + 3-7 minutes (V-KYC) | Time-stamped process tracking | Medium |
| **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | High |
| **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | High |
| **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | High |

---

## **6. User Stories / User Flow**

### **User Stories**

- **As a new customer**, I want to complete my DigiLocker KYC so that I can proceed with my loan application.
- **As a customer who has completed DigiLocker KYC**, I want the option to complete V-KYC immediately or schedule it for later within 72 hours.
- **As a customer choosing to schedule V-KYC**, I want to select a convenient time slot to minimize disruption to my schedule.
- **As a user encountering technical issues during V-KYC**, I want clear instructions and support to complete the process.
- **As an MFD**, I want to assist my customers by sharing V-KYC links and tracking their completion status.
- **As a customer who has completed V-KYC**, I want to pledge my securities easily to finalize my loan application.
- **As an operations team member**, I want to monitor V-KYC completions and handle any failures efficiently.

### **User Flow**

1. **KYC Initiation Screen:**
    - User is prompted to begin the DigiLocker KYC process.
2. **DigiLocker KYC Process:**
    - User enters Aadhaar number and OTP.
    - Completes DigiLocker KYC verification.
3. **V-KYC Introduction:**
    - After DigiLocker KYC, user is informed about the V-KYC requirement.
    - Options to "Start Now" or "Schedule for Later" are presented.
4. **V-KYC Scheduling:**
    - If "Start Now" is chosen, V-KYC session begins immediately.
    - If "Schedule for Later" is chosen, user selects an available time slot.
5. **Bank Account Verification (BAV):**
    - Verify user's bank account details.
6. **Agreement:**
    - User signs the loan agreement.
7. **Mandate Setup:**
    - Set up automatic debit mandate for loan repayments.
8. **Pledge:**
    - User pledges securities as collateral.
9. **Disbursement:**
    - Loan amount is disbursed post V-KYC completion.
10. **Re-Engagement:**
    - Automated reminders are sent if V-KYC is not completed within the scheduled window.
    - Targeted re-engagement based on user drop-off segments.
11. **Loan Disbursement:**
    - Once V-KYC is successfully completed, the loan is disbursed to the user.

---

## **7. Risks and Dependencies**

### **Risks**

1. **Increased User Drop-Off:**
    - Additional V-KYC step may lead to higher abandonment rates (~40-50% as per industry estimates)
2. **Technical Integration Issues:**
    - Challenges in integrating with Bajaj's V-KYC APIs and ensuring real-time updates.
3. **Operational Delays:**
    - Limited agent availability for V-KYC sessions may cause scheduling conflicts.
4. **Data Security Concerns:**
    - Ensuring secure handling of sensitive KYC data to comply with regulations.
5. **Re-Engagement Effectiveness:**
    - Automated reminders may not sufficiently re-engage all drop-off users.

<aside>
💡

The bigger question to be answered is if we are even OK with the challenges with BFL and make TATA the primary lending partner. Only those not eligible with TATA are routed to BFL or DSP. Once DSP is stabilized, we will route volumes to DSP upfront.

</aside>

### **Dependencies**

1. **Bajaj's V-KYC API:**
    - Reliable and well-documented APIs are essential for seamless integration.
2. **MFD Collaboration:**
    - Effective training and support for MFDs to assist customers with V-KYC.
3. **Technology Stack Compatibility:**
    - Ensuring all systems (B2B, SDKs, core funnel) are compatible with the new V-KYC integration.
4. **Regulatory Approvals:**
    - Obtaining necessary sign-offs and ensuring compliance with RBI guidelines.
5. **User Availability:**
    - Users must be available during working hours to complete V-KYC, which may not always be feasible.

---

## **8. Implementation Plan**

### **Phase 1: Planning and Design**

- **Finalize Integration Details:**
    - Collaborate with Bajaj to understand API requirements and capabilities.
- **User Interface Design:**
    - Develop wireframes and user journey maps.
    - Design error screens, loading indicators, and task routing on the user dashboard.
- **Technical Review:**
    - Conduct a comprehensive review of technical requirements and potential challenges.

### **Phase 2: Development**

- **API Integration:**
    - Connect with Bajaj's V-KYC APIs.
    - Implement initiation, scheduling, and status tracking of V-KYC sessions.
- **Dashboard Enhancements:**
    - Develop the task dashboard and notification systems.
    - Implement scheduling functionalities for V-KYC sessions.
- **Backend Processing:**
    - Set up event tracking and data retrieval mechanisms.
    - Ensure secure storage and handling of KYC data.

### **Phase 3: Testing**

- **Internal Testing:**
    - Validate workflows, error handling, and API integrations.
- **User Acceptance Testing (UAT):**
    - Conduct thorough testing with a select group of users to gather feedback and identify issues.

### **Phase 4: Training and Preparation**

- **MFD Training:**
    - Conduct webinars and provide training materials to MFDs.
- **Staff Training:**
    - Train customer support and operations teams on the new V-KYC process and error handling protocols.

### **Phase 5: Launch**

- **Soft Launch:**
    - Introduce the new V-KYC process to a select user segment to monitor performance and gather initial feedback.
- **Full Rollout:**
    - Expand the V-KYC integration to all users after addressing any issues identified during the soft launch.

### **Phase 6: Post-Launch Monitoring (Ongoing)**

- **Performance Tracking:**
    - Continuously monitor KPIs and adjust strategies as needed.
- **Feedback Implementation:**
    - Collect and implement user feedback to enhance the V-KYC process.

---

## **9. Customer Communication Strategy**

### **Pre-Launch Awareness**

- **Channels:**
    - Email campaigns to existing MFD customers.
    - In-app messages informing users about upcoming changes.

### **In-Process Guidance**

- **Features:**
    - Clear instructions, tooltips, and FAQs integrated within the KYC process.
- **Support:**
    - Easy access to customer support through chat, phone, and email.

### **Customer Segmentation**

Segmenting customers based on their interaction points and drop-off stages allows targeted re-engagement strategies to improve completion rates. The segments are defined as follows:

| **Segment** | **Behavior** | **Potential Issues** |
| --- | --- | --- |
| **Segment 1**: Users Who Complete DigiLocker KYC but Drop Off Before Starting V-KYC | Completed DigiLocker KYC but haven’t started V-KYC. | Lack of urgency, confusion about next steps, distractions. |
| **Segment 2**: Users Who Start V-KYC but Don’t Complete It | Started V-KYC but dropped off midway. | Technical difficulties, time availability, confusing process. |
| **Segment 3**: Users Who Complete V-KYC but Drop Off Before Pledging | Completed V-KYC but haven’t pledged securities. | Uncertainty about pledging, financial concerns, fear of commitment. |
| **Segment 4**: Users Who Fail V-KYC | Attempted V-KYC but failed due to technical or verification issues. | Verification failures (mismatched details, video quality), system glitches. |
| **Segment 5**: Users Who Complete V-KYC and Pledge but Drop Off Before Agreement | Completed V-KYC and pledge but haven’t signed the agreement. | Hesitancy to formalize the loan, concerns about terms. |
| **Segment 6**: Users Who Complete V-KYC, Pledge, and Agreement but Drop Off Before Mandate Setup | Completed V-KYC, pledge, and agreement but haven’t set up the mandate. | Technical issues with mandate setup, confusion about the process. |
| **Segment 7**: Users Who Fail to Complete V-KYC Within 72 Hours | Did not complete V-KYC within the 72-hour window. | Missed working hours, scheduling conflicts, confusion about deadline. |
| **Segment 8**: Users Who Restart V-KYC After Failure or Missed Deadline | Restarted V-KYC after failure or missed deadline. | Discouragement from earlier failure, doubts about completing V-KYC. |
| **Segment 9**: Users Who Are Unavailable During V-KYC Hours (Off-Hours Inactivity) | Unable to complete V-KYC during working hours (9 AM – 6 PM). | Scheduling conflicts, time-zone issues. |
| **Segment 10**: Users Who Have Repeated V-KYC Failures Due to Technical Issues | Repeatedly failed V-KYC due to technical issues. | Frustration, poor video quality, mismatched documents. |

### **Multi-Channel Notifications**

- **Channels:**
    - **Push Notifications:** For active app users.
    - **SMS/Text Messages:** For quick, direct reminders.
    - **WhatsApp:** For a personalized touch.
    - **Emails:** For detailed instructions and reminders.
    - **IVR/Phone Calls:** For direct, human interaction.

[message template ](Bajaj%20VCIP%20(VKYC)%20Integration/message%20template%20126e8d3af13a802bbc4ace531e0ba6e4.md)

### **Engagement Strategies**

- **Segmented Messaging:**
    - Tailored messages based on user drop-off segments to address specific concerns and encourage completion.
- **Reminder Timing:**
    - Send reminders at optimal times to maximize user engagement and completion rates.

### **Feedback Mechanisms**

- **Tools:**
    - In-app surveys and feedback forms to collect user insights.
- **Usage:**
    - Implement enhancements based on collected feedback to continuously improve the V-KYC process.

---

## **10. Training and Change Management**

### **Employee Training**

- **Materials:**
    - PDF guides and video tutorials explaining the V-KYC process.
    - Standard Operating Procedures (SOPs) for handling V-KYC failures and error codes.
- **Focus Areas:**
    - Understanding the new V-KYC workflows.
    - Handling customer queries and troubleshooting common issues.

### **MFD Support**

- **Resources:**
    - Webinars and training sessions for MFDs.
    - Detailed documentation and step-by-step guides to assist customers with V-KYC.
- **Support Channels:**
    - Dedicated support teams for MFDs to address any challenges they face in assisting customers.

---

## **11. Next Steps and Action Items**

1. **Finalize Integration Details with Bajaj:**
    - Confirm technical specifications and capabilities.
    - Address any outstanding API-related questions.
2. **Clarify Outstanding Questions:**
    - Define error handling protocols.
    - Confirm service availability and agent working hours.
3. **Develop User Interface Components:**
    - Design and implement UI changes for the V-KYC flow.
    - Ensure seamless integration with existing user dashboards.
4. **Conduct Comprehensive Testing:**
    - Perform internal testing and UAT to validate workflows and integrations.
    - Address any issues identified during testing phases.
5. **Prepare Communication Materials:**
    - Develop clear and concise communication strategies for customers and MFDs.
    - Create templates for notifications and reminders.
6. **Launch UAT:**
    - Initiate User Acceptance Testing with a select user group.
    - Gather feedback and make necessary adjustments before full rollout.
7. **Post-Launch Monitoring and Feedback:**
    - Continuously monitor KPIs.
    - Implement improvements based on user feedback and performance data.

---

## **12. Appendices**

### **Appendix A: Error Codes**

**DigiLocker API Error Codes:**

- **Unified_API_Error:** General API failure.
- **Bitly_API_Error:** Failure to generate or send the shortened URL.
- **Link Sent Successfully:** DigiLocker link sent successfully.

**V-KYC API Error Codes:**

- **Agent_Not_Available:** No agent available for the V-KYC session.
- **Maker_Result_Rejected:** Initial V-KYC review by the maker was rejected.
- **Audit_Result_Rejected:** V-KYC audit was rejected.
- **KYC_Result_Rejected:** V-KYC was rejected due to KYC issues.
- **Link_Initiated:** V-KYC link initiated successfully.
- **Session_Started:** V-KYC session started but not yet completed.
- **Schedule_Mode_Activated:** V-KYC rescheduled by the user.
- **Audit_Result_Approved:** V-KYC audit approved successfully.

### **Appendix B: Regulatory References**

- **RBI Master Direction – Know Your Customer (KYC) Direction, 2016:** [RBI KYC Guidelines](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566#)

### **Appendix C: User Journey Wireframes**

*(Wireframes to be attached separately or included in the presentation slides.)*

### **Appendix D: SDK Update Requirements**

### **API Integration Updates**

**1. Init OTP for CAS**

- **Endpoint:** `{{baseUrl}}/v1/partner/platform/las/cas/init`
- **Method:** POST
- **Headers:**
    - `Authorization: Bearer <token>`
    - `X-AppPlatform: VOLT_API_INTEGRATION`
    - `requestReferenceId: dc0d8002-d110-4814-aea5-3ddedf17e641`
- **Body:**
    
    ```json
    {
      "pan": "ABCPS3721M",
      "phone": "+919898878414"
    }
    
    ```
    
- **Success Response:**
    
    ```json
    {
      "referenceId": "fbb1b4ac-895e-4bfc-b034-cacecd853811"
    }
    
    ```
    

**2. Verify OTP for CAS**

- **Endpoint:** `{{baseUrl}}/v1/partner/platform/las/cas/verify`
- **Method:** POST
- **Headers:**
    - `Authorization: Bearer <token>`
    - `X-AppPlatform: VOLT_API_INTEGRATION`
    - `requestReferenceId: df6de31c-f0ff-4ed7-b1b2-529b5e3b10ed`
- **Body:**
    
    ```json
    {
      "otp": "984735",
      "referenceId": "fbb1b4ac-895e-4bfc-b034-cacecd853811"
    }
    
    ```
    
- **Success Response:**
    
    ```json
    {
      "status": "SUCCESS"
    }
    
    ```
    

**3. Fetch CAS**

- **Endpoint:** `{{baseUrl}}/v1/partner/platform/las/cas/data/0a44fb22-16a9-4bf5-8925-8a88017144a2`
- **Method:** GET
- **Headers:**
    - `Authorization: Bearer <token>`
    - `X-AppPlatform: VOLT_API_INTEGRATION`
    - `requestReferenceId: 9d8c1759-f7aa-46ff-a7c8-55a77ad28245`
- **Error Handling:** Retry if response code is `PORTFOLIO_RESPONSE_PENDING`.

---

### **Appendix E: Bajaj KYC POD API Documentation**

### **API Summary**

- **Initiate KYC POD**
    - **Endpoint (Production):** `https://bflapimprod.bajajfinserv.in/KYCPOD_API/KYCInit`
    - **Method:** POST
    - **Headers:**
        - `Ocp-Apim-Subscription-Key: <subscription_key>`
        - `MOAuthorization: <token>`
        - `Content-Type: application/json`
        - `Authorization: <Bearer Token>`
    - **Body:** Encrypted JSON as per specifications.
    - **Response:** Encrypted JSON containing `status`, `kycRes`, etc.
- **Get KYC Details**
    - **Endpoint (Production):** `https://bflapimprod.bajajfinserv.in/KYCPOD_API/GetKYCDetails`
    - **Method:** POST
    - **Headers:**
        - `Ocp-Apim-Subscription-Key: <subscription_key>`
        - `MOAuthorization: <token>`
        - `Content-Type: application/json`
        - `Authorization: <Bearer Token>`
    - **Body:** Encrypted JSON with `POD_TRANSACTION_ID` and `VERSION`.
    - **Response:** Encrypted JSON containing KYC data.
- **Document Download**
    - **Endpoint (Production):** `https://bflapimprod.bajajfinserv.in/KYCPOD_API/AzureBlobStorageDownload`
    - **Method:** POST
    - **Headers:**
        - `Ocp-Apim-Subscription-Key: <subscription_key>`
        - `MOAuthorization: <token>`
        - `Content-Type: application/json`
        - `Authorization: <Bearer Token>`
    - **Body:** Encrypted JSON with `Requestid`.
    - **Response:** Document file or JSON with status.

### **Encryption Details**

- **Encryption Algorithm:** AES-256 CBC
- **Keys:** Provided via secure channels upon subscription.

### **Response Structures**

- **Success Response:**
    
    ```json
    {
      "status": "success",
      "statusCode": 200,
      "message": "Done",
      "kycRes": {
        "POD_TRANSACTION_ID": "a10a20dc11f41fa5f395577be1cf645e",
        "KYC_STATUS": "",
        "KYC_MODE": "",
        "LAST_KYC_MODE": "",
        "DFDNA": "",
        "RESPONSE_STATUS": "SUCCESS",
        "RESPONSE_MESSAGE": "DATA FETCHED SUCCESSFULLY",
        // Additional fields...
      }
    }
    
    ```
    
- **Failure Response:**
    
    ```json
    {
      "status": "success",
      "statusCode": 200,
      "message": "Done",
      "kycRes": {
        "POD_TRANSACTION_ID": "8f1f4375d20e28098b21e61caa5db31d",
        "SOURCE_REQUEST_ID": "12012",
        "RESPONSE_STATUS": "Failed",
        "RESPONSE_MESSAGE": "Data Not Found",
        "URL": null
      }
    }
    
    ```
    

---

## **13. Additional Considerations**

### **Defining Objectives**

- **Goal Definition:**
    - Achieve compliance with RBI and Bajaj KYC requirements.
    - Enhance user journey by reducing friction and providing flexibility.
    - Minimize operational costs associated with KYC failures and re-pledging.
- **Specific and Measurable Goals:**
    - Reduce user drop-off rate by 20%.
    - Achieve >90% V-KYC completion rate.
    - Ensure 100% V-KYC completion within 72 hours post DigiLocker KYC.
- **Stakeholder Expectations:**
    - **Compliance Teams:** Ensure all regulatory requirements are met.
    - **Customer Experience Teams:** Maintain or improve funnel conversion rates.
    - **Operations Teams:** Streamline workflows and reduce operational costs.
    - **MFDs:** Equip them with tools and knowledge to assist customers effectively.

### **Identifying Constraints**

- **Technical Constraints:**
    - Dependency on Bajaj's API reliability and performance.
    - Integration challenges with existing systems and platforms.
- **Operational Constraints:**
    - Limited agent availability for V-KYC sessions.
    - Time-bound KYC completion window (72 hours).
- **Regulatory Constraints:**
    - Strict adherence to RBI's KYC and V-KYC regulations.
    - Data privacy and security compliance.
- **Business Constraints:**
    - Coordination with Bajaj and other business partners.
    - Potential impact on existing loan disbursement workflows.
- 

### **Decision Points and Considerations**

1. **Should we allow users to Pledge without completing V-KYC?**
    - **Decision:** No, users must complete V-KYC before pledging.
    - **Rationale:** Ensures compliance and secures pledge only for verified users, reducing operational costs associated with unpledging.
2. **If not, should we move the Pledge to after the Mandate?**
    - **Decision:** Yes, move the Pledge step after the Mandate setup.
    - **Impact:** Ensures V-KYC completion before locking securities, enhancing compliance and reducing operational costs.
3. **What happens after Pledge is moved after the Mandate?**
    - **Flow:**
        - User completes Mandate Setup.
        - User pledges securities.
        - Loan disbursement proceeds after V-KYC confirmation.
    - **Benefit:** Aligns pledge with verified users, reducing the need for costly unpledging processes.
4. **What happens when user comes to the flow outside working hours?**
    - **Challenge:** V-KYC is only available from 9 AM to 6 PM on working days.
    - **Solutions:**
        - **Option 1:** Build an in-house scheduler to allow users to book V-KYC sessions outside standard hours.
        - **Option 2:** Rely on Bajaj’s communication methods, utilizing their available channels for scheduling.
5. **Should we build our own scheduler?**
    - **Decision:** **Yes**, to provide greater control and flexibility.
    - **Pros:**
        - Enhanced user experience with more scheduling options.
        - Ability to extend availability beyond standard hours.
    - **Cons:**
        - Increased development time and resource allocation.
6. **If not, are we okay with Bajaj’s communications?**
    - **Decision:** **No**, due to limitations in flexibility and potential scheduling conflicts.
    - **Alternative:** Explore partial reliance on Bajaj while developing supplementary scheduling features.
7. **If yes, how will we contact users?**
    - **Options:**
        - **IVR Needs Development:** Automated voice reminders can inform users about scheduling.
        - **Push Notifications (PNs) May Be Less Effective:** Limited impact compared to direct communication.
    - **Recommendation:** Combine IVR with other channels like SMS and WhatsApp for comprehensive coverage.
8. **What can go wrong in V-KYCs?**
    - **Potential Issues:**
        - User can drop off mid V-KYC.
        - User cannot initiate V-KYC.
        - User cannot respond to PNs and notifications for V-KYC.
        - User might not have a stable internet connection.
        - User might have device permission issues.
        - Agent might have difficulties in audio/video with the user, leading to V-KYC rejection.
        - User might answer questions incorrectly in VCIP.
        - Failure reporting mechanisms might be inadequate.
9. **How will they tell us about failure?**
    - **Solution:** Implement real-time status updates via webhooks and robust error handling to notify users and support teams promptly.
10. **Mapping the Ideal Journey:**
    - **Collaborate with Bajaj:** Work closely to map the ideal V-KYC journey.
    - **Propose and Build:** Develop the process based on mapped journeys, ensuring alignment with both companies’ workflows.
    - **Stakeholder Communication:** Regular updates and walkthroughs with key stakeholders (Kapi, Shipvansh, Nishast, Business teams).
    - **Kickoff with Tech, Ops, Sales, RMS:** Initiate the project with all relevant teams to ensure coordinated efforts.
    - **Release Note and Training:** Prepare documentation and training sessions for a smooth rollout.
- **Clarifications Pending**
    - **Rescheduling and Updates:**
        - How rescheduling of V-KYC sessions will be communicated and reflected in the system.
    
    - **Error Handling Protocols:**
        - Detailed information on specific error codes and responses from Bajaj’s API.
    - **V-KYC Service Availability:**
        - Confirm working hours and holidays for V-KYC agents to optimize notification timing.
    - **Development Estimates:**
        - Assess the time and resources required for integrating and testing the new V-KYC workflows.
    - **Testing Bajaj's V-KYC API:**
        - Comprehensive testing to understand user, technical, and compliance flows.

### **Current Understandings**

- **Current Process Flow:**
    1. DigiLocker KYC
    2. Bank Account Verification (BAV)
    3. Pledge
    4. Agreement
    5. Mandate Setup
    6. Loan Disbursement
- **Key Insights:**
    - Users need to complete both DigiLocker and V-KYC within a short timeframe.
    - V-KYC introduces new steps that could disrupt the existing user journey.
    - Effective re-engagement is crucial to minimize drop-offs.
- **Challenges Noted:**
    - Potential for increased drop-offs during the transition to V-KYC.
    - Technical and operational complexities in integrating and managing the V-KYC process.

### 

### **Recommended Approach**

**Deferred V-KYC Completion with Scheduling Option:**

- **Rationale:**
    - Provides flexibility for users to complete V-KYC at their convenience within the 72-hour window.
    - Aligns with operational constraints by accommodating agent availability.
    - Reduces immediate friction, potentially lowering drop-off rates.
- **Compliance Assurance:**
    - Ensures all regulatory requirements are met by mandating V-KYC completion before loan disbursement.
- **User Journey Improvements:**
    - Clear communication and reminders enhance user understanding and compliance.
    - Flexible scheduling options cater to diverse user needs and schedules.

---

Archives

[V-KYC Integration with Bajaj](Bajaj%20VCIP%20(VKYC)%20Integration/V-KYC%20Integration%20with%20Bajaj%2011fe8d3af13a80ffb40df5798368ad75.md)

[SDK](Bajaj%20VCIP%20(VKYC)%20Integration/SDK%20127e8d3af13a809ab4dafcb6f02b0b6b.md)

- discuss big ticket sizes , GTM phase
- direct customer, B2B GTM, assisted
- List of partners
- Switch lender
- V-KYC, do we want to take it a blocker
- Do we want to make Tata First lender
- 
-