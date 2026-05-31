# Product Release Process

# Challenges

Below are the key challenges in the current release process.

- Bugs on production environment impacting customers & users
- Features being rolled out having bugs/issues leading to quality concerns
- Stakeholders have concerns on lack of feature understanding or change
- Customers are impacted or have a poor experience on production due to mismatch in requirements vs. development.
- Number of man-hours spent on bugfixes increase due to functional clarity lacking.

The above challenges arise due to the below elements.

- Features are being rolled out with or without QA sign-off but no product sign-off
- Bugs and fixes are being rolled without product sign-off
- Fixes and changes are being done without any training for stakeholders
- There’s no design sign-off before deploying UI capabilities on production
- No formal release note is being sent to stakeholders

# Proposed Solution

Below are the interventions proposed to solve these challenges.

- All features would go through a product sign-off is there’s any impact on any existing or new functionality.
- All features would go through a design sign-off if there’s any UI/UX impact on any functionalities.
- All bugs or fixes including logic changes that impact any functionality will go through a product sign-off.
- All bugs or fixes including logic changes that impact any functionality will go through a design sign-off for UI/UX features.
- Any feature that won’t meet the product and/or design sign-off criteria will not be allowed to deployed to production.
- All new features, including enhancements and bug-fixes that change flow or logic will require a formal release note and training session.

While the above items are undertaken, the PM should also setup the required monitoring capabilities by setting up reports or dashboard through Analytics on their own.

# Proposed Process

## Sprint Features

Below is the broad process for sprint features.

- Once the requirements are closed for the sprint, program team informs the PM team of the timelines for QA sign-off.
- Product team keeps the test scenarios handy which is shared upfront as part of requirements with tech.
- Program team informs the PM and Designer about the timeline for QA sign-off. PM and designer will review the test scenarios on QA or staging environment.
- PM and/or designer informs the program team if a feature is signed-off and good to go on Jira. If the feature is good to go, it is deployed on production.
- PM and/or designer informs the program team if a feature needs intervention due to bugs or a scenario not being handled. PM informs the program team to either defer the release or go ahead with the release and handle the tweaks as an enhancement.
- PM will also conduct the training for stakeholder before the release happens to ensure there are no surprises and team is well informed. The same will be confirmed on Jira.
- Tech team will proceed with the changes or go ahead with the deployment on production as per the scenario.

## Bugs & Fixes

Below is the broad process for bug fixes.

- Program team or the developer informs the PM and/or the designer about a bugfix that’s being picked up.
- PM evaluates the impact of the fix including the components that require attention from a functional perspective.
- PM picks up the feature post QA sign-off on the bugfix. If the feature isn’t going through a QA route, PM picks up after dev sign-off.
- PM and/or designer informs the program team if a feature is signed-off and good to go on Jira. If the feature is good to go, it is deployed on production.
- PM and/or designer informs the program team if a feature needs intervention due to bugs or a scenario not being handled. PM informs the program team to either defer the release or go ahead with the release and handle the tweaks as an enhancement.
- PM will also conduct the training for stakeholder before the release happens to ensure there are no surprises and team is well informed. The same will be confirmed on Jira.
- Tech team will proceed with the changes or go ahead with the deployment on production as per the scenario.

# Success Criteria

Below is the success criteria for introducing these interventions.

- Number of escalations due to feature changes to reduce by at least 80%
- Number of man-hours saved due to better quality
- Customer and partner satisfaction score to improve
- Increased number of applications due to better CX and stability

# Key Activities

## Product Sign-off

Below are the items to be considered from a product sign-off criteria.

| Aspect | Consideration |
| --- | --- |
| Is the feature behaving as documented in the requirements for positive cases? | Needs to be documented by PM and signed off on Jira. |
| Is the feature behaving as documented in the requirements for negative cases? | Needs to be documented by PM and signed off on Jira. |
| Is the feature not covering a corner case or edge case? | Needs to be documented by PM and have this fixed or deferred depending on the impact. |
| Is the feature being deployed behind a flag or being rolled out to all customers? | Needs to be documented by PM in the requirement and validated. |
| Are there any scenarios that aren’t being handled and needs to be handled offline? | Needs to be documented by PM and communicated to stakeholders. |

## Design Sign-off

Below are the items to be considered from a design sign-off criteria.

| Aspect | Consideration |
| --- | --- |
| Is the feature behaving as documented in the requirements for positive cases? | Needs to be documented by DM and signed off on Jira. |
| Is the feature behaving as documented in the requirements for negative cases? | Needs to be documented by DM and signed off on Jira. |
| Is the feature not covering a corner case or edge case? | Needs to be documented by DM and have this fixed or deferred depending on the impact. |
| Is the feature being deployed behind a flag or being rolled out to all customers? | Needs to be documented by DM in the requirement and validated. |
| Are there any scenarios that aren’t being handled and needs to be handled offline? | Needs to be documented by DM and communicated to stakeholders. |
| Are the color scheme and themes as per the high-fidelity designs? | Needs to be documented by DM and discussed with PM. |
| Are the interactions, fonts and text sizes as per the high-fidelity designs? | Needs to be documented by DM and discussed with PM. |

## Release Timelines

The release timelines will need to be communicated to stakeholders after the PM discusses the timelines with the developer and QA. In addition, the PM also needs to communicate the below items clearly to stakeholders.

| Aspect | Consideration |
| --- | --- |
| Is the feature being rolled out to a specific set of customers? | Document which customers, when and how we are rolling out the features |
| Is the feature being rolled out in a big-bang or a phased manner? | Document the phases for rollout and as well as timelines for each phase of release |
| Is the feature being rolled out on a specific type of asset (web/Android/iOS)? | Document the platform and the timelines when the features are rolled out |

## Release Note

A release note will need to be sent to stakeholders who signed off on the feature as well as the ones who will impacted by the feature. The release note will need to be shared for any new release, enhancement or fix that impacts business or customer experience metrics.

Below are the components of the release note that needs to be covered.

| **Element** | **Consideration** |
| --- | --- |
| What is the problem statement/s? | Detail out the problem statement in 2-3 lines |
| What is the solution we identified? | Detail out the solution in 2-3 lines |
| What will be the impact? | Define the top 2-3 impact metrics  |
| What is the change? | Detail out the user journey or validation in detail |
| What are the next steps? | Detail out the next steps including training, monitoring, etc. |

## Training Note & Session

PMs will need to conduct a detailed training session for stakeholders who signed off on the feature as well as the ones who will impacted by the feature. The training note will need to be shared for any new release, enhancement or fix that impacts business or customer experience metrics.

The training itself will need to be setup before the feature actually goes live and after the PM has signed off on the feature.

Below are the components of the training that needs to be covered in the training session.

| **Element** | **Consideration** |
| --- | --- |
| What is the problem statement/s? | Detail out the problem statement in 2-3 lines |
| What is the solution we identified? | Detail out the solution in 2-3 lines |
| What are the various scenarios? | Detail out the different scenarios and our handling |
| What will be the impact? | Define the top 2-3 impact metrics |
| What is the change? | Detail out the user journey or validation in detail |
| What are the next steps? | Detail out the next steps including training, monitoring, etc. |
| Where is the change happening? | Detail the change/s including screens where the changes are undertaken |
| What is to be communicated to partners/ customers? | Detail out anything that needs to be conveyed to customers or partners |

## Reporting & Monitoring

PMs will be required to setup the required reporting capabilities to ensure that the feature rolled out on production. The monitoring itself needs to be setup to answer the below questions.

- What were the metrics before and after the release?
- Where there any adverse impact on any other metric in the funnel?
- Was the movement in metrics more or less than estimated?
- What was the reason for the movement in metrics?

The metrics can be setup on a sheet as well to identify the impact of the feature. This will need to be moved to a BI tool or an automated reporting mechanism going forward.

<aside>
💡

The metrics being referred to here are only product or business metrics built on top of existing datapoints. If any new datapoints need to be logged, it needs to be covered in the PRD by the Product team.

</aside>

## Activity Timeline

Below is the activity timeline from the date of QA sign-off.

| **Activity** | Timeframe |
| --- | --- |
| Product sign-off | Within 1 working day. Can be extended for large/complex features |
| Design sign-off | Within 1 working day. Can be extended for large/complex features |
| Stakeholder Training | Within 2 working days. Can be extended over multiple sessions/days for large/complex features |
| Release Note | Within 1 working day. Can be extended for large/complex features |
| Reporting | Within 2 working days. Can be extended for large/complex features |

# Tracker

Below is a tracker of the key items under this initiative.

| Activity | ETA | Owner | Status |
| --- | --- | --- | --- |
| Brief the Product & Program team on the initiative | 14th Oct’24 | Gautam Mahesh | Completed |
| Setup the process on Jira for Product Sign-off (LSP) | 16th Oct’24 | Manish Pandey | Pending |
| Setup the process on Jira for Product Sign-off (NBFC) | 16th Oct’24 | Vinay Vyas | Pending |
| Brief the engineering & QA team on the initiative | 16th Oct’24 | Gautam Mahesh | Pending |
| Brief the stakeholders on the initiative | 15th Oct’24 | Gautam Mahesh | Pending |
| Setup adherence process | 18th Oct’24 | Gautam Mahesh | In Progress |

# Open Items

- [x]  Time for training to be agreed upon with stakeholders - @Gautam Mahesh
- [ ]  

# Meeting Minutes

- Design for unhappy paths
- Handling the same scenario for all lenders where applicable
- Success criteria
-