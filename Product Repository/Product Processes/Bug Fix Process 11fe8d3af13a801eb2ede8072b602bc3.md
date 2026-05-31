# Bug Fix Process

# Challenges

Currently, Volt’s platform is being constantly modified to suit the requirements of new initiatives and business scenarios. As we grow rapidly, we need to streamline our bug-fix process to drive higher quality across the board.

- Increased man-hours spent on fixing issues
- Customers escalating about functional or technical issues
- Partners escalating about functional or technical issues
- Increased number of bugs being reported
- Lack of a feedback loop or learning from each bug

The above challenges arise due to the below elements.

- Bugs and fixes are being rolled without product sign-off
- Bugs and fixes are being rolled without design sign-off
- Bugs aren’t religiously analyzed for RCAs
- Product team isn’t involved or doesn’t drive bug fixes
- Stakeholders ask oncall for enhancements or even new features

# Proposed Solution

Below are the interventions proposed to solve these challenges.

- Streamline the reporting process from multiple sources (TBD).
- Oncall dev unblocks the customer quickly where feasible.
- Oncall dev identifies the RCA.
- All reported issues are categorized into features, enhancements or bugs.
- Bugs are prioritized and addressed as per impact and routed through release process.
- Features and enhancements are prioritized and addressed as per impact and routed through sprint process.

Link to [Product Release Process](Product%20Release%20Process%2011de8d3af13a80b78dabe101e9ec7d8b.md).

# Proposed Process

Below is the proposed process to address these challenges.

- Oncall dev receives the ticket from any one of the sources of reporting.
- Oncall dev unblocks the customer through a quick-fix or moving the application forward where possible.
- Oncall dev classifies the ask into one of the buckets on Jira and tags the program manager after conducting a detailed RCA after the quick fix.
    - **New feature**: this could be anywhere from a large feature to a small feature but is a capability that doesn’t exist in the system and needs product intervention.
    - **Enhancement**: this could be a tweak in the logic or minor scenario handling for an existing feature and needs product intervention.
    - **Bug fix**: this could be an issue at Volt’s end due to a technical or functional issue and impacts users.
- All new features and enhancements are tagged to the respective PM on Jira.
- PM evaluates the ask and prioritizes it as part of the backlog.
- PM informs the stakeholder about the timelines when picked up by tech.
- All bugs are classified by the oncall dev into one of the below buckets.
    - **Functional issues**: this is due to miss of a scenario from a scoping or development perspective which results in a functional impact.
    - **Techno-functional issues**: this is due to the miss of a technical implementation or a technical issue that results in a functional impact.
    - **Technical issues**: this is due to a code or infra or data level issues or a technical implementation miss but has no functional impact.
- All bugs that are classified as functional issues or techno-functional issues are addressed by the engineering team as a fix.
- All bugs that are fixed and signed off by QA/Dev are reviewed and signed off by the concerned PM as mentioned in the [Product Release Process](Product%20Release%20Process%2011de8d3af13a80b78dabe101e9ec7d8b.md) document.
- The PM confirms that the bug can be deployed to production and informs the stakeholders of the same.

# Success Criteria

Below are the ways to measure the success of this initiative.

- Reduction in the number of man-hours spent in addressing internal & external queries.
- Reduction in the number of bugs due to a better feedback loop.
- Improvement in funnel performance due to addressing bugs better.
- Improvement in customer/partner satisfaction score.

# Tracker

Below is a tracker of the key items under this initiative.

| Activity | ETA | Owner | Status |
| --- | --- | --- | --- |
| Align with Priyesh and Program team on the initiative |  | Gautam Mahesh | Completed |
| Brief the Product & Program team on the initiative |  | Gautam Mahesh | Completed |
| Setup the process on Jira for Product Sign-off (LSP) |  | Manish Pandey | Pending |
| Setup the process on Jira for Product Sign-off (NBFC) |  | Vinay Vyas | Pending |
| Brief the engineering & QA team on the initiative |  | Gautam Mahesh | Pending |
| Brief the stakeholders on the process |  | Gautam Mahesh | Pending |
| Setup adherence process |  | Gautam Mahesh | In Progress |

- Can we put in a TAT for cases to 3rd parties? Fetch is the highest frequency
- Put an escalation matrix for 3rd parties?
- SLAs for each scenario by partner
-