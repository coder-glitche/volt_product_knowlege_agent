# Centralised issue reporting process

: Ranjan kumar Singh
Created time: July 31, 2024 2:05 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Ranjan kumar Singh, Gautam Mahesh, Lalit Bihani

# **What problem are we solving?**

- We have multiple source of ticket creation
    - WATI + Phone calls : Issue reported by customer or MFDs to inbound team
    - Email: User reports issue on email, internal team send mail to product or tech team to raise the issue/feature enhancement/new requirement.
    - B2B platform: Issue raised by B2B partners on behalf or their customer
    - Product team: Issues identified by the product team
    - Tech team: Issues identified by the tech team
    - Sales/OPS: Issues reported by customer or MFD at time of sales call or while doing the journey
    - Business/Customer success team: Issue identified or new feature requirement by the customer success team
    - Lender requirement: Enhancement or issue reported by the lender
- Issue reported type
    - Bugs
    - Feature enhancement
    - New feature requirement
- We do not have a unified list of bugs reported from all sources.
- There is no mechanism to provide visibility to all stakeholders about the status of bugs, feature enhancement requests, and new feature requirements.
- There is no single point of contact or source of truth through which internal teams can raise issues or track their status.
    - This often results in the same issue being reported through multiple sources, leading to the creation of duplicate tickets.
- Tech and product teams provide requirements to the Ops team to resolve issues operationally with lenders. [Need an Ops owner for this process]
- Product are not able to provide the training to the sales and OPS team after we fix any bugs or any feature enhancement.
    - Sometime product lacks visibility of the bug fixes and its deployment
- Product faces issue at time of prioritisation of the reported issue due to lack of visibility of the impact.
- Duplicate tickets are getting created in JIRA due integration issue with JIRA and ZENDESK

---

# **How do we measure success?**

Some metrics to measure success.

- TAT for ticket resolution to reduce - TBD
- Partner NPS to improve - TBD
- Customer NPS to improve - TBD
- Customer support tickets/application to reduce - TBD
- Number of internal man-hours reduced - TBD
- Internal SAT score to improve - TBD

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Process overview

We are streamlining the handling of product issues, on call and product requirements using Zendesk and JIRA:

1. **Zendesk for Ticket Management**:
    - **Groups**: Sales/Ops and Tech on Call.
    - **Ticket Creation**: Sales/Ops creates tickets for tech issues.
    - **Management**: Tech on Call handles the tickets and adds identified issues to the JIRA backlog or tech TODO.
2. **JIRA for Issue Tracking**:
    - **Logging Issues**: Program/Product Manager logs all issues from various sources to a common JIRA board.
    - Issue segregation: Tech on call classifies the issues into bugs, feature enhancements or even adhoc issue
    - **Prioritization**: Product team prioritizes the backlog in weekly stakeholder meetings and updates all parties.
    - **Sprint Planning**: Prioritized items are added to Product or Tech sprints. This will not include bugs or on-call fixes.
    - **Development and UAT**: Items move to UAT pending for Product team sign-off post-development.
    - **Deployment and Training**: Post-UAT, items are deployed and marked for training if needed.

## Process detailed

- Use Zendesk for Ticket Management:
    1. Create two groups on Zendesk: Sales/Ops and Tech on Call.
    2. Sales/Ops will use Zendesk to create tickets and assign ticket the tech on call.
    3. Tech on Call will manage the tickets on Zendesk instead of ZIRA.
    4. If any tech RCA/bug fixes/feature enhancements are identified during the on-call process, the on-call team will add items to the JIRA board into the backlog or TODO bases on the case.
- Create a common JIRA board managed by the Program Manager:
    1. All issues reported from different sources or identified during on-call will be added to the JIRA board as a backlog.
        1. The Product Manager will be responsible for adding issues reported from any source to the JIRA board.
    2. The Product team will prioritize the backlog from the JIRA board.
        1. The Product team will organize weekly meetings with stakeholders to prioritize the backlog.
        2. The Product team will send prioritized and deprioritized items reports to all stakeholders.
        3. The Product team will inform and communicate any RCAs and their fixes as well to stakeholders.
    3. Once the backlog is prioritized, the Product team will add items into the Product sprint or Tech sprints based on the urgency, effort, and impact of the items.
    4. The Program Manager will add the prioritized list to the tech to-do list.
    5. Separate Scrum meetings will be organized to discuss updates on the development of issues.
    6. Once development is done, the Tech team will add items to the UAT pending list.
        1. The Product team will do the UAT and give sign-off for each item.
    7. The Tech team will deploy and move items to the deployment done list.
    8. The Product team will pick items from the done bucket and categorize them as training required or not required.
    9. Once the training is completed, the Product team will move items to the training done list.
- The Product team is responsible for adding any adhoc requests to the JIRA board and getting those prioritized with the stakeholders.

---

# **Design**

The above process will feed into the design sprint planning as well and influence design sprints directly/indirectly depending on the type of requests/asks.

---

# Reporting

- Weekly bug reported based on source
- No of issue solved based on the priority
- Tracking of metrics as mentioned in success criteria

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

No impact/involvement of marketing.

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Engineering
    - [ ]  
- [ ]  QA
    - [ ]  

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