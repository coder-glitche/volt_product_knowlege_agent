# LSQ Requirements for UTM Attribution

: Vijay Kumar S
Created time: August 28, 2025 11:53 AM
Status: Not started
Last edited: August 28, 2025 11:55 AM

## Objective

Enable LSQ (LeadSquared) to **store, track, and act upon attribution data** for each MFD by capturing both **initial UTM** and **last UTM**. Ensure every UTM update creates **activities and follow-up tasks** for better engagement tracking.

## Data Flow

1. **Event Logging**
    - Each time an MFD clicks on a campaign link or engages with a communication containing UTMs, the event is logged with:
        - MFD phone number (identifier)
        - UTM parameters (`campaign_id`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`)
        - Timestamp of event
        - Activity context (page visited, registration, activation milestone, etc.)
2. **MFD Matching**
    - The backend matches the UTM event to the MFD via phone number.
    - If no MFD record exists, UTM data is stored and linked upon registration.
3. **Stack Ranking of UTM Events**
    - UTM events are ranked by **timestamp**.
    - Two attribution markers are defined:
        - **Initial UTM** = first UTM triggered (never overwritten).
        - **Last UTM** = most recent UTM triggered (always updated).

## Data Storage in LSQ

1. **Custom Fields (Lead Record)**
    - Store **Initial UTM** and **Last UTM** parameters in dedicated custom fields (see earlier table).
2. **Activity Logging (Mandatory)**
    - For every **Initial UTM capture** → create an **Activity** in LSQ:
        - Activity Name: *“Initial UTM Recorded”*
        - Fields: UTM parameters, timestamp, campaign type.
    - For every **Last UTM update** → create an **Activity** in LSQ:
        - Activity Name: *“Last UTM Updated”*
        - Fields: UTM parameters, timestamp, campaign type.
3. **Follow-Up Task Creation (Linked to Last UTM)**
    - Each time a **Last UTM** is updated:
        - A **Follow-up Task** must be automatically created for the assigned RM/Owner.
        - Task Type: *“Follow-Up on Campaign Lead”*
        - Due Date: Based on **Last UTM Activity timestamp** (e.g., +24 hours).
        - Linked to the same MFD Lead.
    - This ensures **freshest campaign interaction → RM engagement**.
4. **Last Activity Field Update**
    - Each **Last UTM Activity** must also update the **system’s Last Activity Date field** in LSQ.
    - This allows LSQ’s native filters/reports to stay accurate.

## Rules & Logic

1. **Initial UTM**
    - Captured once on first campaign click.
    - Not overwritten.
    - Activity logged → *“Initial UTM Recorded”*.
2. **Last UTM**
    - Updated on every new campaign click.
    - Always overwrites previous Last UTM fields.
    - Activity logged → *“Last UTM Updated”*.
    - Follow-up Task created → *“Follow-Up on Campaign Lead”*.
    - Last Activity Date updated.

---