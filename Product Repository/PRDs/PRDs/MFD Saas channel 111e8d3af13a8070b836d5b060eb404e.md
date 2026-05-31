# MFD Saas channel

: Naman Agarwal
Created time: September 30, 2024 5:29 PM
Status: Not started
Last edited: October 8, 2024 6:02 PM

we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity

- this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities
- We want to manage these partners as they are a high leverage way to get new clients in crease AUM
- this will provide compitive advantage and Distribution
- We need to solve the product stack for the SAAS partners, MFDs, Clients/customers
- we need to support Potenttial custoomer with education and details about the product
- we need to suppoirt Live incase or error or bloackages in the funnel
- we need to support in case of Servicing requests

currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , 

Saas compaines like redvision etc 

”

”

| In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. |
| --- | --- | --- | --- |
| Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) |
| MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) |
| Partner dashboard revamp | Shivansh | P1 | -Display correct pos, aum , total earning . A overall summary on every fields-Milestone for reaching next income slab |
| WATI Communication | Shivansh | P0 | -Every chat on wati to be tagged to a user-Chat should have an opening and closing time-CTA -Resolution on chat completion |
| Replicating tiles/field in RedVision UIAskVisibility of customer transactions to be made available to MFDs | Shivansh | P1 | MFDs cannot see customers transaction. The visibility regarding interest/payment due is not visible to MFD |

### **Problem Statement**

Currently, our Mututal fund  Distribution (MFD) partners face significant challenges in managing their customer relationships effectively. They lack comprehensive visibility into key customer metrics such as interest details, occurrences of shortfalls, and the status of loans. Specifically:

- **Information Gaps:** MFDs frequently need to inquire about interest statuses, mandate registrations, and interest calculations but don't have direct access to this information.
- **Customer Communication Issues:** MFDs often fail to inform customers about shortfalls, leading to escalations and dissatisfaction.
- **Dependency on Advisors:** B2B2C customers rely heavily on advisors to monitor their loan accounts, which diminishes the effectiveness of direct reminders sent by Volt, our platform.

### **Success Metrics**

To ensure we’re effectively addressing these issues, we’ve outlined several key performance indicators:

- **Timely Interest Repayment:** We aim to see repayments of interest occur on time, reducing the need for outbound reminder calls.
- **Reduction in Calls and Queries:** By providing better visibility and automated communications, we expect a decrease in both outbound calls and inbound queries related to shortfalls.
- **Lower Portfolio Sell-Offs:** Enhanced communication and transparency should lead to fewer instances of portfolio sell-offs.
- **Increased Loan Renewals:** We anticipate an uptick in loan renewals before their expiration dates, indicating better customer engagement and satisfaction.

### **Solution Overview**

Our solution focuses on creating a comprehensive dashboard for MFDs that consolidates all necessary customer information in one place. Here’s a high-level overview of the proposed features:

1. **Interest and Charges Table:** A detailed table displaying current month due interests and charges, complete with filtering options by mandate status, interest status, and lender name. Users can search, sort, and paginate through records efficiently.
2. **Shortfall Management:** A dedicated table for shortfall amounts with aging details, enabling MFDs to sort and filter based on due dates and lender names. This section includes educational content about shortfalls and predefined WhatsApp messages tailored to different shortfall scenarios.
3. **Loan Renewals:** A table that tracks loan renewals, allowing users to filter by lender name and status. It includes benefits of loan renewals and predefined messages based on the loan status, such as active, expired with outstanding amounts, etc.
4. **Communication Tools:** Integrated WhatsApp messaging with predefined templates based on various statuses, ensuring consistent and timely communication with customers.
5. **User-Friendly Navigation:** Tabs and deep links across all platforms (web and Android) to ensure seamless navigation and accessibility of information.

### **User Stories**

From a user perspective, the dashboard should allow MFDs to:

- **Comprehensive View:** Access a unified list of all customers, including those with shortfalls, pending interests, or renewals.
- **Efficient Navigation:** Easily switch between different categories of customers via tabs, each displaying the total count and relevant information.
- **Effective Communication:** Send tailored WhatsApp messages directly from the dashboard, ensuring personalized and situation-specific interactions with customers.
- **Persistent State:** Maintain the selected tab state even after page reloads, enhancing user experience and efficiency.

### **Detailed Requirements**

The solution encompasses several detailed requirements to ensure functionality and usability:

- **Filtering and Searching:** Robust filtering options across all tables, allowing MFDs to sort and search for specific customer details efficiently.
- **Pagination:** Each table will support pagination with 50 records per page to handle large datasets without compromising performance.
- **Educational Content:** Informative modals explaining key concepts like shortfalls and the benefits of loan renewals to aid MFDs in better managing customer interactions.
- **Actionable Insights:** Each customer row will include actionable buttons for viewing details, sharing information, or communicating via WhatsApp, facilitating proactive customer management.

### **Design and User Interface**

The design phase has been outlined with a link to our Figma prototype, ensuring that the user interface is intuitive, responsive, and aligns with our overall user experience goals. The interface will cater to both web and Android platforms, ensuring accessibility and ease of use across devices.

### **Analytics and Monitoring**

To track the effectiveness of our solution, we’ll implement Amplitude events such as:

- **Tab Clicks:** Monitoring interactions with different customer categories.
- **Engagement Metrics:** Tracking how often MFDs use features like filtering, searching, and sending messages.

These analytics will provide insights into user behavior and help us refine the platform further.

### **Go to Market Strategy**

While the PRD currently outlines placeholders for the go-to-market strategy, including marketing plans, operations, and sales training, these sections will be developed to ensure a smooth launch and effective adoption of the new dashboard by our MFD partners.

### **Action Items and Next Steps**

We’ve outlined a checklist to ensure all aspects of the project are addressed, spanning product development, business alignment, and design. This structured approach will help us stay on track and meet our project milestones effectively.

### **Feedback and Continuous Improvement**

The document includes sections for feedback and learnings, emphasizing our commitment to continuous improvement. By gathering insights from users post-launch, we can iteratively enhance the platform to better meet their needs.

### **Appendix**

An important note in the appendix clarifies that for different lenders, the due amounts may vary. For instance, TATA users need to pay both interest and charges, whereas BAJAJ users are only required to pay interest. This distinction is crucial for accurate financial tracking and customer communication.

---

In summary, this PRD outlines a comprehensive solution aimed at empowering our MFD partners with better visibility and control over their customer interactions. By addressing the current pain points and implementing robust features, we aim to enhance customer satisfaction, reduce operational inefficiencies, and drive better financial outcomes for both our partners and customers.”