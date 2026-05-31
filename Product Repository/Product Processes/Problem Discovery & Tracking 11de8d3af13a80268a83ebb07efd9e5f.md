# Problem Discovery & Tracking

# Challenges

Currently, Volt’s Product team is solving problems across the board at different stages. In addition, the team gets requirements from stakeholders spanning business, operations, partners, etc. This results in multiple challenges.

- Lack of a consolidated view of all items
- Lack of visibility of multiple things on the PM’s plate
- Man-hours spent in tracking items across business, product and tech
- Lack of clear communication/ updates to stakeholders
- Lack of visibility of sprint plan and the aligned features.

A lot of this is happening due to the below reasons.

- PMs are using Notion to document basic PRDs. However, all detailed requirements and its tracking is happening on Jira.
- PMs use google sheets to maintain trackers for each features which becomes a challenge as there’s no one-stop visibility
- Design team doesn’t have complete visibility and a lot of misses happen post a feature being picked up for development or at PRD review stage.
- Calling out blockers and tracking various open items across multiple items becomes a challenge due to lack of holistic visibility.
- Sprint goals and plans are maintained on excel which isn’t fully linked to Jira which becomes tough to visualize end-to-end.

# Proposed Solution

Below is the proposed solution.

- Use Google sheets for stakeholder alignment
- Use Jira (PSB board) for all problem discovery items
- Use Notion for PRDs and detailing out requirements
- Use Jira for writing detailed requirements (user stories)

The rationale for using Jira is that helps track items under development as well as items that don’t need tech intervention. In addition, Jira has all the required capabilities to track complex items like project tracker, creating list of items, etc

# Proposed Process

Below is the proposed process.

- Stakeholder discusses a problem statement OR the PM/PD finds a problem
- PM/PD documents the item on Jira on the PSB board as one of the items.
    - **Epic**: a large project that requires multiple items for completion
    - **Story**: a story level item that requires only task level items
    - **Task**: a single task like sign-off from stakeholders, bug, etc.
- PM/PD can add multiple items and keep adding comments as well as move tasks to different statuses
- PM/PD should aim to segregate problems into 2 buckets.
    - Problem discovery, identification, sign-off and prioritization
    - Solution discovery, identification, sign-off and prioritization
- The outcome of solution will be the actual requirements that will be aligned with tech
- PM can tag an item into one of the sprints.
    - **Product sprint**: if an item is still in discovery stage which might or might not go into tech bucket (tech sprint). This will include design items as well
    - **Tech sprint**: if an item is solutioned and signed-off by stakeholders and the same needs to go into
- All statuses of tasks will be reviewed on Jira board and the PM/PD can callout a blocker or dependency
- Epic to be created at charter level - @Gautam Mahesh

## Proposed States

Below are the proposed states to be used on Jira.

| Stage | Status | Scenario |
| --- | --- | --- |
| Problem Discovery | To-Do | Default status. When a problem needs to be picked up for detailing |
| Problem Discovery | Problem Conceptualization | When the problem is still not clear and needs to be being conceptualized |
| Problem Discovery | Problem Statement WIP | When the problem is still being worked upon and needs clarity |
| Problem Discovery | Problem Statement Scoped | When the problem is clear and scoped out or identified |
| Problem Discovery | Problem Statement Signed Off | When the problem statement/s is signed-off by stakeholders |
| Solution Discovery |  |  |
|  |  |  |
|  |  |  |

# Success Criteria