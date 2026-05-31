# NBFC Launch GTM

# Overview

This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective.

# Objective

The broad objectives of launching this in phases are.

- To test the stack end-to-end to ensure accuracy when launched at scale
- To test the process end-to-end to ensure customer experience is met
- To ensure internal users are fully aware of the new flow
- To identify and address any gaps in the flow to ensure minimal impact at scale
- To ensure uptime and reliability of the stack for optimum experience at scale

# Success Criteria

Below are the key funnel metrics that define the CUG program and expected thresholds.

- Lead to Pledge %age - 50%
- Sanction TAT - 15 minutes
- KYC completion %age -
- NACH completion %age -
- Lead to sanction conversion %age -
- Sanction to disbursement %age -
- Disbursement TAT - 2 hours
- Disbursement success rate - At least 95%

Below are the key internal operational metrics that define the CUG program and expected thresholds.

- QC Ops approval TAT - 30 minutes
- Credit deviation approval TAT - 30 minutes
- Checker approval TAT - Not more than 30 minutes from request placed
- QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions)
- Checker approval rate - 95% (At least 95% of maker request should be accurate decisions)

# Phases

We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. 

## Phase 1

**Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | Upto 10 days |  |
| Total number of applications | 100 - 120 |  |
| Sourcing channel | MFD |  |
| Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | 10-15 |  |
| Recommended DP | Upto 10L | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | Yes |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Yes | Only for cases with DP > 20L |
| Mandate registration checker | NA | No physical mandate registration |
| Withdrawal checker | Yes | Only for withdrawals > 20L |
| Repayment checker | Yes |  |
| Mandate presentation checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | No |  |
| Physical mandate registration | No |  |

Product & operations will review each finding and address any issues before opening up for subsequent phases.

## Phase 2.1

**Objective**: To test out our stack at scale with the MFD channel after identifying and addressing any issues in Phase 1.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | Upto 20 days |  |
| Total number of applications | 800 - 100 |  |
| Sourcing channel | MFD |  |
| Partners | Open |  |
| Application split | 50% |  |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | 40 - 50 |  |
| Recommended DP | Upto 50L | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | No |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Conditional | Only for cases with DP > 20L |
| Mandate registration checker | NA | No physical mandate registration |
| Withdrawal checker | Conditional | Only for withdrawals > 20L |
| Repayment checker | No |  |
| Mandate presentation checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | No |  |
| Physical mandate registration | No |  |

## Phase 2.2

**Objective**: To open up our stack to the large B2B partners who want to build custom journeys through our APIs starting with 1 partner.

Below are the points of consideration.

<aside>
💡

To be detailed out

</aside>

## Phase 3.1

**Objective**: To open up our stack to the B2C customer segment after volume ramp up on MFD channel to incorporate any new or incremental findings.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | Upto 10 days |  |
| Total number of applications | 100 - 120 |  |
| Sourcing channel | B2C |  |
| Traffic Split | 20% |  |
| Partners | All | MFD team to share the MFDs for whitelisting |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | 10-15 |  |
| Recommended DP | Upto 10L | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | Yes |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Yes | Only for cases with DP > 20L |
| Mandate registration checker | NA | No physical mandate registration |
| Withdrawal checker | Yes | Only for withdrawals > 20L |
| Repayment checker | Yes |  |
| Mandate presentation checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | No |  |
| Physical mandate registration | No |  |

## Phase 3.2

**Objective**: To open up our stack to the entire MFD channel along with the existing lending partners (BFL & TCL) as well as introduce physical pledging and mandate capabilities.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | 30 days |  |
| Total number of applications | No restrictions |  |
| Sourcing channel | MFD |  |
| Partners | Open |  |
| Application split | 50% |  |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | ~60/day |  |
| Recommended DP | Upto 2CR | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | No |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Conditional | Only for cases with physical pledging |
| Mandate registration checker | Yes | Only for physical mandate registration |
| Withdrawal checker | No | Only for withdrawals > 20L |
| Repayment checker | No |  |
| Mandate presentation checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | Yes |  |
| Physical mandate registration | Yes |  |

## Phase 4.1

**Objective**: To open up our stack to the B2B partners, especially PhonePe to ensure our stack is able to handle all partner workflows for 1 large partner.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | 20 days |  |
| Total number of applications | No restrictions |  |
| Sourcing channel | MFD |  |
| Partners | Phonepe |  |
| Application split | 50% |  |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | ~40/day |  |
| Recommended DP | Upto 2CR | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | No |  |
| Credit deviations check | Yes |  |
| QC/Ops check | No |  |
| Withdrawal checker | No |  |
| Mandate registration checker | No | Not opening up this for partners |
| Repayment checker | No |  |
| Mandate presentation checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | No | Not opening up this for partners |
| Physical mandate registration | No | Not opening up this for partners |

## Phase 4.2

**Objective**: To open up our stack to the entire MFD channel along with the existing lending partners (BFL & TCL) as well as introduce physical pledging and mandate capabilities.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe |  |  |
| Total number of applications | No restrictions |  |
| Sourcing channel | MFD |  |
| Partners | Open |  |
| Application split | 50% |  |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | ~30 |  |
| Recommended DP | Upto 2CR | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | No |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Conditional |  |
| Mandate registration checker | Yes | Only for physical mandate registration |
| Withdrawal checker | No |  |
| Mandate presentation checker | No |  |
| Repayment checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | Yes |  |
| Physical mandate registration | Yes |  |

## Phase 4.3

**Objective**: To open up our stack to the large B2B partners who want to build custom journeys through our APIs across all partners and at scale.

<aside>
💡

To be detailed out

</aside>

## Phase 5.1

**Objective**: To open up our stack to all B2B partners once the stack performs as per expectations for 1-2 partners.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | NA |  |
| Total number of applications | No restrictions |  |
| Sourcing channel | MFD |  |
| Partners | All |  |
| Application split | 50% |  |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | ~100/day |  |
| Recommended DP | Upto 2CR | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | No |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Conditional |  |
| Mandate registration checker | NA |  |
| Withdrawal checker | No |  |
| Mandate presentation checker | No |  |
| Repayment checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | No | Not opening up this for partners |
| Physical mandate registration | No | Not opening up this for partners |

## Phase 5.2

**Objective**: To open up our stack to all MFD platforms once the stack is fully stable and performing as per expectations on MFD channel.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | NA |  |
| Total number of applications | No restrictions |  |
| Sourcing channel | MFD |  |
| Partners | All platforms |  |
| Application split | 50% |  |
| Drawing Power | 25K - 2CR |  |
| Number of applications/day | ~100/day |  |
| Recommended DP | Upto 2CR | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | No |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Conditional |  |
| Mandate registration checker | Yes | Only for physical mandate registration |
| Withdrawal checker | No |  |
| Mandate presentation checker | No |  |
| Repayment checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | Yes |  |
| Physical mandate registration | Yes |  |

## Phase 6

**Objective**: To open up our stack to all channels, partners and platforms after performing upto expectations and augmented by higher limits.

Below are the points of consideration.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Timeframe | NA |  |
| Total number of applications | No restrictions |  |
| Sourcing channel | All |  |
| Partners | All |  |
| Application split | 50% |  |
| Drawing Power | 25K - 5CR |  |
| Number of applications/day | ~300/day |  |
| Recommended DP | Upto 5CR | Can deviate basis business teams’ comfort |

Below is the key capabilities and their aspects.

| Aspect | Consideration | Comments |
| --- | --- | --- |
| Master checker flag | No |  |
| Credit deviations check | Yes |  |
| QC/Ops check | Conditional |  |
| Mandate registration checker | Yes | Only for physical mandate registration |
| Withdrawal checker | No |  |
| Mandate presentation checker | No |  |
| Repayment checker | No |  |
| Customer communications | Yes |  |
| Bureau reporting | Yes |  |
| CKYC reporting | Yes |  |
| NESL reporting | Yes |  |
| Physical pledging | Yes | Not for B2B partners |
| Physical mandate registration | Yes | Not for B2B partners |

# Timelines

[NBFC Go-live](NBFC%20Launch%20GTM/NBFC%20Go-live%2012de8d3af13a802d90f3d9136d943111.csv)