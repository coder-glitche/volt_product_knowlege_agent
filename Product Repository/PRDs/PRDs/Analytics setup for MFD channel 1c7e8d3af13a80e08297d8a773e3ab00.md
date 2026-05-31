# Analytics setup for MFD channel

: Naman Agarwal
Created time: March 31, 2025 11:58 AM
Status: In progress
Last edited: April 10, 2025 11:11 AM

**Problem Statements:**

1. **Source Identification:**
    - We currently lack detailed data to distinguish the source platform/interface for applications. Examples include:
        - Partner Portal Web vs. Partner App
        - Customer App vs. specific SDKs
2. **SDK Tracking:**
    - We cannot accurately identify which SDK version or type was used by a partner platform for an application.
3. **TAT Calculation:**
    - Relying on the audit table for TAT is not ideal for analyzing detailed stage performance.

---

### **Proposed Solutions:**

1. **Source Markers:**
    - Add unique markers/attributes to application records to identify the origin:
        - Volt Partner Portal (Desktop)
        - Volt Partner Portal (Mobile Web)
        - Volt Customer Web
        - Volt Customer Mobile App (iOS/Android)
        - Volt Partner Mobile App (iOS/Android)
        - SDK (Identify SDK Type/Partner)
        - Device Type (where applicable)
        - Application step level - Source (e.g., in the MFD channel where both Partner and Customer may complete steps)
2. **Dedicated TAT Metrics:**
    - Implement fields/timestamps to capture:
        - Add Created add of the step , to capture the the First time stage change
        - **Overall TAT:** From Lead Creation/Customer Registration to Loan Complete status.
        - **Stage-Level TAT:** Track start times for each key state to calculate the duration spent in each stage (e.g., Start of State A → Start of State B).
3. **Logging for FE UI related bugs:**
- Tracking sluggishness on the website
- If the Elements fail to load or are stuck