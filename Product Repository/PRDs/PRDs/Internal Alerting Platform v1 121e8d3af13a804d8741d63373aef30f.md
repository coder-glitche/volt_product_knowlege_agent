# Internal Alerting Platform v1

: Gautam Mahesh
Created time: October 16, 2024 12:31 PM
Status: Ready for Tech
Last edited: November 25, 2024 4:56 PM

# **What problem are we solving?**

Volt works with multiple 3rd parties (lenders, public repositories and vendors) to help power its journeys. While this helps expedite development and reduces development effort, it does indeed induce additional points of failure like performance degradations and downtimes (scheduled & unscheduled). 

The impact of these can be seen across acquisition, conversions and retention.

- Customers not able to complete the journey due to disruptions impacting conversions
- Partners not happy with Volt’s platform due to disruptions impacting business
- Customers give poor rating to Volt impacting acquisition and retention

This can be attributed to the below challenges.

- Internal teams not informed about any performance degradations or downtimes proactively
- Internal teams are aware of downtimes from partners or customer escalation
- Partners are not informed about any performance degradations or downtimes proactively
- Customers aren’t aware of downtimes and when they can resume an application

---

# **How do we measure success?**

The success of this initiative can be mentioned by the below metrics.

- Funnel conversion %age to improve
- Customer satisfaction score to improve
- Partner satisfaction score to improve
- Number of man-hours reduced
- Number of support tickets and queries resolve
- TAT for detecting any downtime/ degradation to be < 1 minute

---

# **How are others solving this problem?**

Players solve this problem through one of the ways.

- Building a generic alerting platform that captures the performance of the platform as well as other internal and external services
- Convey any changes in platform performance to internal stakeholders through tools like Slack or Email
- Convey any changes in platform performance to external stakeholders on their own through tools like Slack, Whatsapp, Email, etc.
- Convey any changes in platform performance to external stakeholders through tools like Instatus which can be subscribed to by external partners

There are low-code data aggregation and workflow tools like n8n that can be leveraged to integrate with 3rd party tools like Slack, Email, etc.

---

# **What is the solution?**

## Requirements Phase 1

Below are the key requirements we are looking to roll out in Phase 1.

- Volt logs all the status codes and error codes of the APIs under scope
- Volt considers only 5xx and 4xx error codes for the APIs under scope
- Volt considers specific error codes for the APIs under scope for monitoring
- Product team to have a detailed view in the list format of all the alerts set-up & the configuration at one place.
- Triggered alert to be sent to assigned channel. Channel will be set at alert level.
- Alert to run in a 2 categories-
    - Standalone - Without comparing with previous time slot data, alert will be sent to slack channel as per the configs.
    - Comparative - If alert category set to comparative, then data will be compared with previous time slot & current time slot. Based on the set rule for status, alert will be sent.
- Product team to have the ability to control the status thresholds. Variables to be set at individual alerts we are configuring.
    - Operational - (Api success % falls between 100 - 90)
    - Degraded Performance - (Api success % falls between 89 - 50)
    - Major Outage - (Api success % falls between 49 - 0)
    
    **Note:** If API % is 89.7% these numbers will not belong to any group mentioned above. Need to round off the API%.
    
- Product team to have a control to enable or disable the alerts in a real-time.
- Based on the set rule, auto tagging to be done in the slack messages.
    - If status goes from operational/ degraded performance to major outage, respective poc to be tagged in the alert.
    - If status goes from major outage to operational, respective poc to be tagged in the alert.
- Product team should be able to set the frequency in minutes at alerts level.
- Parameters to be sent via slack are
    - API Name
    - Status
    - Total Hits
    - User error counts —> all 4XX http status codes
    - Provider error counts —> all 5xx http status codes
    - API success % —> Key metric which decides the status. API success % = ((Total hits - User errors) / Total hits) × 100
    - From timestamp —> Time of data considered for analysis.
    - To timestamp —> Time of data considered for analysis.
- Product team to have a ability to turn-off the alerts at the set time. This is at alerts level.
    - Alert should not run between the time frame of 10PM to 6AM. Numbers are variables.

## API List

Below are the list of APIs which require alerting to be built out.

| API | Phase |
| --- | --- |
| MFC Fetch | Phase 1 |
| CAMS Fetch | Phase 1 |
| KFin Fetch | Phase 1 |
| Digilocker APIs | Phase 1 |
| PAN validation | Phase 1 |
| BFL KYC POD | Phase 1 |
| Account opening (BFL) | Phase 1 |
| KFS + Agreement generation (BFL) | Phase 1 |
| Agreement generation (TCL) | Phase 1 |
| CAMS Pledge | Phase 1 |
| KFin Pledge | Phase 1 |
| Withdrawal request (TCL) | Phase 1 |
| Withdrawal request (BFL) | Phase 1 |
| Mobile OTP generation | Phase 1 |
| Mobile OTP verification | Phase 1 |
| Bajaj PG | Phase 1 |
| Tata PG | Phase 1 |
| Selfie check | Phase 2 |

## Alerting Process

Below will be the process for us to act internally on the alerts generated.

| Event | POC | Action |
| --- | --- | --- |
| Internal Downtime | Oncall Dev | Dev to reach out to relevant folks to get the platform up and running |
| 3rd party downtime | Product Manager (PM) | PM to reach out to the relevant 3rd party for resolution |
| Internal Performance Degradations | Oncall Dev | Dev to reach out to relevant folks to get the platform as per performance standards |
| 3rd party Performance Degradations | Product Manager (PM) | PM to reach out to the relevant 3rd party for resolution |

**Note**: 3rd party here includes lenders like BFL and TCL as well.

# **Design**

---

# **Analytics**

Below are the metrics that 

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

- To be setup

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  To finalize the scope of Phase 1 rollout
    - [ ]  To finalize the scope of Phase 2 rollout
- [ ]  Business
    - [ ]  -
- [ ]  Operations
    - [ ]  To train the operations & support teams on Phase 1 rollout

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