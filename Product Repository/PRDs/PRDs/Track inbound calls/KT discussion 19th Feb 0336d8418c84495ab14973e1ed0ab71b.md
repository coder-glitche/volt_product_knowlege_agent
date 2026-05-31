# KT discussion 19th Feb

## Flows

- MFDs number
- Customer number

MFD flow

- Pre-empanelment
    - Outbound → Labdhi
    - Inbound → OE team
- Post empanelment
    - Outbound → OE team
    - Inbound → OE team (lead owner)
- RM
    - RM

**Leadsquared tracking**

- **Inbound call picked**
    - **Inbound call task with disposition**
- **Backup lead owner**
    - Check team / attribute
    - Backup assignee should have lead access
- Missed call task
    - Outside business hours
    - No Assignee available
    - Assigned but not picked
- Inbound call activity / duration / activity

**Other questions**

- If lead doesn’t exist?

**Notes:**

- whats will happen if we change role/team name on LSQ, how switch case will work - Discuss in exotel
- Need to check if we are saving owner details of all lead on volt DB - Need to check with ENOSH
- If no lead found on LSQ then what will happen in case of exotel inbound, create lead and assign to team based on lead origin
- Exotel inbound call - lead info modal should open on LSQ dashboard
- If outside of business hours, create missed call task
- If unanswered, create task for lead owner
- Labdi teams call should assign to Volt Onboarding team
- Ask Exotel to share BRD and take sign-off from Volt
- What will be ETA on Exotel to implement solutions