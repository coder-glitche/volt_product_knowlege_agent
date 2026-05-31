# Product Note: Separating Portfolio Pledge and Asset Pledge Steps in LSQ

: Naman Agarwal
Created time: February 19, 2025 1:05 PM
Status: Not started
Last edited: February 21, 2025 3:29 PM

# Product Note: Separating Portfolio Pledge and Asset Pledge Steps

## Current Behavior

Currently, the system combines two distinct steps - MF Portfolio Pledge (offer page) and Asset Pledge - into a single step labeled as `ASSET_PLEDGE_STEP` in the CRM event mapping. This creates ambiguity in tracking and managing these separate processes.

## Problem Statement

The current implementation:

1. Does not distinguish between portfolio pledge (offer page) and actual asset pledge steps
2. Sales agents have hard time understanding is the application is on offer or pledge for calling 
3. Creates confusion in the application flow tracking
4. Reduces granularity in analytics and monitoring

## Proposed Solution

Separate the current combined step into two distinct steps:

1. **Portfolio Pledge** (`PORTFOLIO_PLEDGE_STEP`)
    - Represents the offer page where customers view their eligible portfolio
    - Maps to `MF_PLEDGE_PORTFOLIO` in application flow
2. **Asset Pledge** (`ASSET_PLEDGE_STEP`)
    - Represents the actual asset pledging process
    - Maps to `ASSET_PLEDGE` in application flow

## Implementation Changes Required

1. Update CRM event mapping in `getCRMEvenTypeForStepStart`:

```java
case MF_PLEDGE_PORTFOLIO -> CRMEventType.PORTFOLIO_PLEDGE_STEP;
case ASSET_PLEDGE -> CRMEventType.ASSET_PLEDGE_STEP;

```

1. Update DB schema to reflect new step definitions:
    - Add `PORTFOLIO_PLEDGE` as a distinct step after `MF_FETCH_PORTFOLIO`
    - Keep `ASSET_PLEDGE` in its current position in the flow

## Expected Benefits

1. Improved tracking and analytics 
2. Better user journey mapping
3. Better lead prioritisation in outbound

## Migration Plan

1. Understand current Lead stage update activity send to LSQ
2. Create new step definitions in DB
3. Verify the changes in LSQ
4. (Backfill)

## Next Steps

1. PN :- Tech Review