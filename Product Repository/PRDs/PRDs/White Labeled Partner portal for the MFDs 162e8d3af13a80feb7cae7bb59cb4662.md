# White Labeled Partner portal for the MFDs

: Naman Agarwal
Created time: December 20, 2024 3:29 PM
Status: Ready for Tech
Last edited: January 22, 2025 12:46 PM

### **1. Objective**

To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience.

### **Problems to Solve**

Investwell has two modes of integration with Volt 

**MFD Portal  - investwell.voltmoney.in**

- The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience.
- KYC and Selfie capture journey steps get stuck

**User facing Application**

- Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey

Overall

- SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide
- MFD’s having stuck are unlikely to come back
- Users might issue in journey on KYC or mandate steps

### **Target Users**

- **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers.
- **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem.

### **Requirements**

### **Login and Signup**

- **Access Control:**
    - Auto-login from the Invest well MINT platform.
- **User Journey:**
    - MFDs log in directly via custom Investwell-branded login.
    - Access to the new dashboard in a new browser tab.

![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png)

### **Dashboard Features**

**Application Management:**

- Create, track, and manage loan applications.
- Credit limit checks  in 15 seconds.
- Pending applications with page-nation
- interest , renewals, shortfalls, dashboard
- Completed applications

**Branding** 

- Removal of Volt logos where feasible (except certain unavoidable pages).
    - 

**Stability** 

- SDK implementation for improved customer LAMF journey experience.
- Enhanced stability over the existing URL redirection.

 

Dashboard /portal

- Ability to create application
- Ability to check Credit limit
- Ability to send the application links
- Ability to service the customers
    - List of registered customer and their status
    - Download SOA
    - See Interest , shortfall, renewal details
    - Un-utilised credit limits

- ~~Partner profile~~
- Customer management features:
    - Customer registration
    - Customer Journey
    - Eligibility check tool
    - ~~Customer portfolio viewing~~
    - Shortfall
    - Renewall
    - Interest payment
    - all partner customers
- ~~Marketing resources:~~
- IFA tools
    - ~~Capital gain statement viewing~~
    - ~~Interest calculator~~
- Support channels
    - Call
    - ~~Collected SOA~~
    - ~~Raise service ticket~~
    - ~~Earnings~~
- ~~Referral program~~
    - ~~AUM redemption savings tracking~~

**Phase 2** 

- FAQs ( For LAMF and journey )
- Customer portfolio reasons for the limit

@Debashish Roy @Rishi Prasanth 

# Notes below (Working)

Investwell<>Volt Integration today 

- VOLT partner dashboard
- Features
    - Auto Login from Mint
    - MFDs can create and track LAMF applications
- Issues
    - The portal is no longer Supported with Updates as it was a Fork of the Main line Volt Partner portal.
    - Due to not receiving Updates to handle the LAMF journey changes , user face issues with stuck steps and looping redirections

![image (27).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/image_(27).png)

We would like to discuss Alternates to the current implantation to provide Invest well partner Best in class tools for LAMF creation right from the MINT platform 

New Option

We Will provide a Custom but current version of the volt Partner dashboard

- Features
    - MFD will be able to auto login as current to the new portal
    - MFD will be able to create applications just like the Volt empanelled MFDs
    - Will be Support will continuously with updates and Bug Fixes
    - Similar features to Current for the initial implementation
- PS:- the New Portal Might contain VOLT branding on some screens. It’s not feasible to remove the Volt Logo and text from each and every page of the Portal and application process

This portal will help MFD to Easily create LAMF applications and stop redemption

Option 2 

We can provide APIs for the Partners to create there Own Experience in FE, 
this offers more customisablity for Increased integration effort on the Investwell side 

Feature :- Investwell MINT customer side get a LAMF 

Currently Investwell Mint offers Customers of MFD a option to take LAMF and do the LAMF journey from the MInt platfroms. The current implementation is a URL redirection.

for better customer experience and stabilty we recommend Integrting our SDKs for the Mint Platforms. Our SDKs are well used by our many B2B partners like Phonepe and will in total 1 week of effort to integrate accross Mint platfroms

Dear [Recipient],

We are excited to share a significant upgrade to the Volt Partner Dashboard, designed to enhance the experience for Investwell partners on the MINT platform. This new solution is tailored to better meet your needs and ensure seamless operations.

### **Why the Change?**

The current dashboard has served its purpose but does not align with the evolving needs of Investwell. To provide a superior experience, we’re transitioning to a customized version of the Volt Partner Dashboard that offers advanced capabilities and long-term support.

---

### **Feature Comparison: Current vs. Upgraded Dashboard**

| **Feature** | **Current Dashboard** | **Upgraded Dashboard** |
| --- | --- | --- |
| **Access** | Auto-login from MINT. | Auto-login remains intact for seamless partner access. |
| **Application Tracking** | MFDs can create and track LAMF applications. | MFDs can create, track, and manage applications with enhanced stability and ease of use. |
| **Updates and Maintenance** | No updates or support due to technical limitations. | Continuous updates, regular bug fixes, and feature enhancements ensure optimal performance. |
| **LAMF Journey** | Prone to issues like stuck steps and looping redirections. | Reliable and intuitive LAMF journey for smoother partner interactions. |
| **Visibility** | Limited insights into customer shortfalls, interest payments, and renewals. | Comprehensive visibility into customer shortfalls, interest payments, and eligible renewals. |
| **Branding and Customization** | Static branding with no customization options. | Tailored solutions that can include Investwell-specific branding. |
| **Customer Experience** | Stability concerns with URL redirection for LAMF journeys. | Direct SDK integration ensures reliability and a superior customer experience. |

---

### **How the New Dashboard Benefits Investwell**

- **Better Usability:** The new dashboard is designed for enhanced ease of use and faster workflows for your MFDs.
- **Future-Proof:** With regular updates and support, this solution ensures long-term stability and reliability.
- **Improved Insights:** Gain access to better visibility on customer data to help partners make more informed decisions.
- **Streamlined Integration:** The upgraded solution fits seamlessly into the MINT platform with minimal disruptions.

---

### **Next Steps**

We’re ready to assist you with this transition and ensure Investwell partners have access to this improved toolset. Let us know how we can support you in moving forward.

Best regards,

[Your Name]

---

This approach makes the new platform sound like an inevitable, positive upgrade rather than a forced change, while focusing on benefits and the smooth transition. Let me know if you'd like further refinements!

---