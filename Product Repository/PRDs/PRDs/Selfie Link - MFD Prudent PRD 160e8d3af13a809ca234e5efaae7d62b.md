# Selfie Link - MFD/ Prudent PRD

: Nihal Simha M S
Created time: December 18, 2024 2:18 PM
Status: Done
Last edited: March 19, 2025 1:38 PM

# **What problem are we solving?**

- Approximately 2.6% of applications(irrespective of platforms) take more than 5 minutes to complete, while 1% of applicants take more than 30 minutes without even entering the deviation flow. This increases the time required for applicants to complete the loan application.
- For Mutual Fund Distributors (MFDs) or MFD software partners completing applications on behalf of users, the problem lies in the **selfie verification step**, where MFDs often either drop off or capture an image of the user displayed on a mobile screen, leading to potential errors or spoofed images.
- Volt’s relationship managers spend 10 to 15 minutes on calls unblocking the MFDs at this step per application.
- MFDs often get confused on the selfie capture screen as they are unsure of what to do when the camera opens.
- The **"Share Link"** CTA, placed at the top of the UI, is not intuitive for MFDs to locate and use effectively.
- The multi-step application process can overwhelm MFD customers, increasing the risk of drop-offs.
- Analysis Sheet - [Redvision funnel analysis](https://docs.google.com/spreadsheets/d/1grDZqA9cTZWLArFjRJZXVUK2_lt6ozcKlz_24u1Y07g/edit?usp=sharing) (Sheet 5)

---

# **How do we measure success?**

- **Reduction in Completion Time**:
    
    Decrease the percentage of users taking more than 5 minutes to complete the selfie step, thereby contributing to a reduction in the overall application completion time.
    
- **Completion Rate for Selfie Step**:
    
    Increase in the percentage of applications that successfully complete the selfie step without dropping off.
    
- **Improved Image Quality**:
    
    Higher compliance with authentic, high-quality user selfies, reducing spoofing or manual interventions.
    

---

# **What is the solution?**

Provide a **shareable link** that MFDs or MFD software partners can use to enable users to complete only the selfie step directly. This ensures that the user is actively involved in the selfie capture, reducing errors and improving image authenticity.

## Requirements Overview:

1. **Shareable Link Generation**:
    
    MFDs or partners should be able to generate a unique link specific to the selfie step.
    
2. **Completion Notification**:
    
    Notify the MFD or partner once the user has completed the selfie step.
    
3. **Error Handling**:
    
    Provide error messages and retry options for users who face difficulties during the selfie capture.
    

## User stories / User flow

- **MFD Workflow**:
    - MFD completes the initial steps of the application.
    - At the selfie step, the Volt provides an option to generate a shareable link.
    - The MFD shares the link with the user via email or SMS.
- **User Workflow**:
    - The user receives the link and completes the selfie step.
    - The system validates the selfie and updates the application status.
- **Completion Workflow**:
    - Post selfie step completion from the user, MFDs can continue the user the application.

## Requirements

### Wireframes(Actual design link is below)

![image.png](Selfie%20Link%20-%20MFD%20Prudent%20PRD/image.png)

### Design Link -

[https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=2432-50015&p=f&t=S3Euttv0yUx9ufRB-0](https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=2432-50015&p=f&t=S3Euttv0yUx9ufRB-0)

**Step 1-** 

![image.png](Selfie%20Link%20-%20MFD%20Prudent%20PRD/image%201.png)

- Enable this screen for the MFD portal and MFD SaaS partners (e.g., Prudent, Redvision, etc.).
- MFD Options for CTAs:
    - Share Link with Customer:
        1. Opens the share link modal.
        2. The share link modal will include a “Copy Link” option.
        3. The shareable link will be shortened and should not contain any PII identifiers.
        4. The link will open in a web browser.
        5. A pre-populated message will be included when sharing the link.
        6. New share modal to be built & will be enabled for web browsers.
    - Capture on This Device:
        1. Allows MFD partners to capture the selfie on the current device, directing them to the selfie capture screen.
        2. If MFD partners wish to share the link instead, they can click on the “Share Link with Customer” CTA, which will open the share link modal.

**Step 2-**

![image.png](Selfie%20Link%20-%20MFD%20Prudent%20PRD/image%202.png)

- This will serve as the landing screen for users who click on the shared link via Volt MFD portal.
- Basic details of the user will be displayed:
    - Applicant's name
    - Masked mobile number
    - Lender logo
- The CTA on this screen will be “Proceed to Selfie Verification.”
- We should be able to control the appearance of Volt logo with a flag.
- The next screen will redirect users to the authentication screen.

![image.png](Selfie%20Link%20-%20MFD%20Prudent%20PRD/image%203.png)

- This screen will be the landing screen for users coming via MFD SaaS partners. For Prudent, Redvision, etc.
- The platform name will be added along with other details.
- Powered by Volt logo will be made available.

**Step 3-**

![image.png](Selfie%20Link%20-%20MFD%20Prudent%20PRD/image%204.png)

- OTP Validation: Users must validate the OTP to proceed with the selfie verification step via the link.
- Masked Mobile Number: The user's mobile number will be displayed in a masked format for security.
- OTP Details: A 6-digit OTP will be sent to the user's registered mobile number.
- Resend OTP: The "Resend OTP" option will be enabled 15 seconds after the initial OTP is sent.
- OTP Regeneration: If the user closes the OTP input bottom sheet and later returns to the screen, the previously generated OTP will no longer be valid, and a new OTP will be triggered automatically.
- Error Handling: For invalid or expired OTPs, an error message will be displayed in red below the OTP input fields.

**Step 4-**

![image.png](Selfie%20Link%20-%20MFD%20Prudent%20PRD/image%205.png)

- Post OTP Verification:
    - Once the OTP is successfully verified, the user will be directed to the selfie verification screen.
- Selfie Capture:
    - Users can proceed to capture their selfie on this screen.
    - Existing screens and flows for selfie capture will be reused to ensure consistency.
- Handling Deviation Flow:
    - Any deviation during the selfie capture process will be managed directly within the link-based journey.
- Link Status Management:
    - The system will handle and update the following statuses for the link:
        1. Pending: Link generated but not yet accessed by the user.
        2. In-Progress: User has accessed the link and initiated the process.
        3. Deviation Flow: Any deviation or exception encountered during the journey.
        4. Completed_via_Link: User successfully completed the journey via the shared link.
        5. Completed_via_Application: User completed the journey through the main application, bypassing the link.
        6. Failed: The process was not completed due to an error or user inaction.

**Step 5-**

![image.png](Selfie%20Link%20-%20MFD%20Prudent%20PRD/image%206.png)

- Post-Selfie Verification Step:
    - After uploading or verifying the selfie, the user will be presented with an option to confirm if they wish to continue with the application process.
    - Depending on the lender, next screen should be decided. For eg- DSP as lender, after selfie verification, additional data screen will be available.
- MFD Partner Notifications:
    - MFD partners will receive a WhatsApp notification immediately when the status transitions into any of the following:
        1. Deviation Flow: To alert the MFD partner about any irregularities or interruptions in the user's process.
        2. Completed_via_link: To notify successful completion of the user's journey.
        3. Failed: To inform the MFD partner about an incomplete or failed attempt.
- MFD SaaS Partner Callbacks:
    - All MFD SaaS partners will be updated through the existing callback mechanisms without requiring any additional configuration or changes.

---

# **Analytics**

- **Click Metrics:**
    - Track the number of users who clicked on the shared link to measure initial engagement.
- **Completion Metrics:**
    - Monitor how many users successfully completed the selfie verification step using the shared link.
- **Screen Engagement:**
    - Capture the time spent on each screen to identify potential drop-off points or areas requiring optimization.
- **Session Duration:**
    - Measure the total session duration from the time the session is initiated (the user clicks on the link) until they reach a **terminal status** (e.g., Completed, Failed, Deviation).

---

## Post Release

- Need to measure, how many users are continuing the application via the link.
- How many users are completing the selfie step via the link?
- How many users dropped off via link?

## Phase 2

While the user is doing the selfie verification step via the link, MFD partners should be able to continue the journey. (The product team is still scoping & validating the approach)

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

# **Learnings & Next Steps**

---

# **Appendix**

## Meeting notes

Message 

“

**Dear [Borrower’s Name],**

As part of the KYC process, please complete the selfie verification step at your earliest convenience. Click the link below to proceed:

🔗 [Insert Verification Link]

This step is essential to finalize your application. If you have any questions, feel free to reach out.

Thank you,

[Partner Name]