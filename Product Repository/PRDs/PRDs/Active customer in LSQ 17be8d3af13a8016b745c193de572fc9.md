# Active customer in LSQ

: Naman Agarwal
Created time: January 14, 2025 5:13 PM
Status: In progress
Last edited: February 27, 2025 3:11 PM

### **Problem Statement**

1. There is a significant delay in conversion between lead creation and the customer's decision to take a loan. Data shows that **40% of PhonePe customers complete their application more than 30 days after lead creation**.
    - The current LSQ setup is optimized for leads ready to take a loan immediately after account creation, but not for delayed conversions.
2. We lack a robust mechanism to identify customers returning after an extended period (e.g., 30+ days) to re-fetch data and reconsider taking a loan, which means that sales team is not calling the Leads with eligible limits that registered few weeks ago.
3. The Sales and RM teams often reach out to customers at inconvenient times, such as when they are not actively engaged with their applications or are preoccupied with other tasks. This increases conversion time and creates user frustration.

We want to have a sales process similar to that of Policy bazaar, as the customer is visiting the platform they are get sales call.

## Metrics

- Sales call to active customers
- Conversion rate of active customers vs In-active customers
- Cohort long term conversion rate

### **Expected Impact**

- Improved loan application conversion rates.
- Enhanced efficiency in Sales and RM team outreach.
- Reduced user frustration by aligning engagement efforts with customer activity.

### **Proposed Solutions**

- Implement a parameter to identify and track customer engagement on the platform.
- **Criteria for Active_lead Users**:
    - A user is considered "Active_lead" if:
        - They are browsing any section of the Volt platform (Web/App)
        - They have a session duration exceeding **30 seconds**.
    - Updates to LSQ on  user activity will be triggered:
        - When a new session starts and is on for more than 30 sec
        - No more than three **times per day per user due to the API constraints**.
        - If the User is eligible for LAMF and do not have loan created
- **Integration with LSQ**
    - Send the user activity parameter as a **Customer Platform_Active Timestamp** to LSQ.
    - LSQ will prioritise and manage leads based on this timestamp, enabling:
        - Focused outreach to active users.
        - Support for users stalled at critical stages like Fetch.
    - Agents will see the Last active time as lead detail and have a view with Last active time as a Column
    

### **Additional Requirements**

- Estimate the number of Active parameter updates required to determine the **QPS  limits** for LSQ. 132/minute