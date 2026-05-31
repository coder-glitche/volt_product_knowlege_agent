# Integrated Sales tool

: Naman Agarwal
Created time: October 10, 2024 4:57 PM
Status: In progress
Last edited: October 14, 2024 2:04 PM

# **What problem are we solving?**

Support systems face significant challenges in managing multi-channel customer queries across B2C, B2B2C, and partner channels. These issues include fragmented communication, difficulty handling diverse customer types, inadequate issue categorization, lack of centralized ticketing, ineffective SLA tracking, absence of real-time performance dashboards, fragmented reporting, delayed follow-ups, communication errors, and no customer feedback mechanisms. These problems lead to decreased customer satisfaction, poor service levels, and reduced operational efficiency.

- We don’t have a way to understand VOLT inbound and outbound at a glance
- We are not able to respond to missed calls from customers and more problematically to high value customers (HV MFD)
- We do not have any way to filter the inbound calls to based on a criteria
- We can’t keep track of 1000 of chat sessions open at any given moment , they are address as the user prompts and agent sees
- We don’t record calls and have little clue on the substance or common issues discussed on the calls/ Chats
- we need to graduate some MFDs to self serve process
- we need to improve number of calls a Agent can take
- we need to handle effect leads effectively
- important leads should be prioritised
- Improve handling
    - Reduce TAT to call back
    - Make call shorter
    - Respond with product tools

---

# **How do we measure success?**

sales efficiency =Active loan generated per support team member 

MFD CSAT = high 

Efficiency = Number of Conversions per Support staff

- Increase conversions
- Decrease cost of conversions in time in support

conversion funnel below 

- cost of conversion  is support is —> cost* (interactions 
* (low quality + high quality ))
- cost —>

support and sales are divided between , support and sales, 

- sales to outbound reach to customer
- support to in bond help the customer
- 

unregistered lead —> registered Lead—> eligibl;e lead—> 
**Digilocker KYC**: Users complete KYC through Digilocker.—>

1. **Bank Account Verification**: The user's bank account is verified.
2. **Pledge**: The loan collateral is pledged.
3. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed.
4. **Mandate**: A mandate is established for loan repayment.
5. **Disbursement**: Loan is disbursed to the user.

—> Servicing 

| **Step** |  | **Total Customers (N)** | **Inbound Calls** | **Outbound Calls** | **WhatsApp Contacts** | **Emails Sent** | **Avg. Time per Call (mins)** |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unregistered Lead |  |  |  |  |  |  |  |  |  |
| Registered Lead |  |  |  |  |  |  |  |  |  |
| Eligible Lead |  |  |  |  |  |  |  |  |  |
| Digilocker KYC |  |  |  |  |  |  |  |  |  |
| Bank Account Verification |  |  |  |  |  |  |  |  |  |
| Pledge |  |  |  |  |  |  |  |  |  |
| KFS + Agreement |  |  |  |  |  |  |  |  |  |
| Mandate |  |  |  |  |  |  |  |  |  |
| Disbursement |  |  |  |  |  |  |  |  |  |
| Servicing |  |  |  |  |  |  |  |  |  |

**Customer Satisfaction (CSAT) Scores:** Higher scores indicate better customer experiences.

•	**First Response Time:** Shorter times reflect quicker support.

•	**Resolution Time:** Faster resolutions enhance customer satisfaction.

•	**SLA Adherence Rates:** Meeting or exceeding SLA requirements shows reliability.

•	**Operational Efficiency Metrics:** Metrics like tickets handled per agent and system uptime.

•	**Reduction in Communication Errors:** Fewer errors signify improved accuracy.

•	**Feedback Collection Rates:** Higher rates indicate better engagement for improvements.

# **How are others solving this problem?**

- **Unified Support Platforms:** Integrating multiple channels into a single interface.
- **CRM Integration:** Linking support systems with Customer Relationship Management tools for better data management.
- **AI-Driven Routing:** Using artificial intelligence to route queries to appropriate agents based on complexity and customer type.
- **Automated Ticketing Systems:** Streamlining query tracking and management.
- **Real-Time Dashboards:** Providing managers with live data on performance metrics.
- **Feedback Tools:** Implementing mechanisms to collect and analyze customer feedback post-resolution.
- **Segmented Support Strategies:** Tailoring support approaches for B2C, B2B2C, and partner channels.

---

# **What is the solution? (potential)**

Implement a centralized, multi-channel support system that unifies all customer interaction channels (email, chat, phone, WhatsApp) into a single platform. This system should support segmentation for B2C, B2B2C, and partner customers, incorporate automated ticketing and routing based on issue complexity and customer type, enforce SLA tracking, provide real-time performance dashboards, and include integrated feedback mechanisms.

- INBOUND
    - Calls
        - Call are routed or provided by Exotell
        - Received calls
            
            
            | Type | Instance | percentage |
            | --- | --- | --- |
            | Incoming | 1595 | 26.14% |
            | Outgoing | 1407 | 23.06% |
            | Missed | 2950 | 48.35% |
            | Rejected | 132 | 2.16% |
            | Blocked | 17 | 0.28% |
        - On a average agents are on call for  3 Hrs (call duration )
    - messages
        - Periscope
            - ~150 chats a day ( at least one message )
        - Wati
            - ~ 50 chats
        

Runo , call 

## Requirements overview (optional)

**Requirements overview (optional)**

•	**Multi-Channel Integration:** Seamlessly connect all customer communication channels.

•	**Centralized Ticketing:** Unified system to track and manage all queries.

•	**Customer Segmentation:** Differentiate support processes for B2C, B2B2C, and partners.

•	**Automated Routing & Prioritization:** Direct queries to appropriate agents based on predefined rules.

•	**SLA Management:** Track and ensure adherence to service agreements.

•	**Real-Time Analytics:** Monitor support performance and identify bottlenecks.

•	**Feedback Collection:** Gather customer insights post-resolution.

## User stories / User flow

**Support Agent:** Access all incoming queries from various channels through a single dashboard, prioritize based on customer type and issue severity, and track resolution status.

•	**B2B2C Partner:** Submit queries with priority handling and receive timely, customized support.

•	**Customer:** Receive consistent and prompt responses across their preferred communication channels with clear resolution updates.

## Requirements

**Functional:**

•	Integration with email, chat, phone, and social media platforms.

•	Role-based access for different customer segments.

•	Automated ticket creation and assignment.

•	SLA tracking and alerts.

•	Real-time reporting and dashboards.

•	Feedback collection post-resolution.

•	**Non-Functional:**

•	Scalability to handle high query volumes.

•	High availability and reliability.

•	Data security and compliance with regulations.

•	User-friendly interface for support agents and managers.

---

# **Design**

The solution features a unified dashboard where support agents can view and manage all customer queries from different channels. The system includes modules for ticketing, customer segmentation, SLA tracking, and analytics. Integration APIs connect with existing CRM and communication tools. The user interface is intuitive, providing quick access to customer histories, priority indicators, and feedback forms. Real-time dashboards display key performance metrics for managers.

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

[/problems](Integrated%20Sales%20tool/problems%2011be8d3af13a80b090ebeb81d055e04d.md)

[](Integrated%20Sales%20tool/Untitled%2011be8d3af13a80c4983eda251545df5f.md)

singrade event sending 

[MFD - interview ](Integrated%20Sales%20tool/MFD%20-%20interview%2011fe8d3af13a80f1a7e5c86e2865d27b.md)