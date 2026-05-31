# NSDL PAN Verification — Non-STP Rejection Handling

: Priyamvada S
Created time: May 24, 2026 1:22 PM
Status: Not started
Last edited: May 28, 2026 3:16 PM

**What problem are we solving?**

## **Background & Context**

As a RE, DSP is required to perform PAN verification through an authorised entity as part of its KYC compliance process. Prior to this initiative, PAN verification against an authorised source (NSDL) was not part of the application workflow.

To address this regulatory requirement, we integrated the NSDL PAN Verification API into our application flow after the KYC step. The integration was first launched in shadow deployment — meaning the API is called in the backend, but verification failures do not block applications from proceeding. This allowed us to baseline the real-world failure rate before enabling hard enforcement.

## **How NSDL PAN Verification currently works (shadow deployment)**

After digital KYC is completed, our backend calls the NSDL PAN Verification API with three inputs:

- PAN number — provided by the customer or LSP in the application journey
- Name — taken from the PAN document available via DigiLocker, or from Aadhaar if PAN is not available via DigiLocker
- Date of Birth — sourced from Aadhaar

If the initial call fails due to a name mismatch, we have two sequential fallback sources:

1. **Bank account name:** After KYC, a bank account verification step returns the account holder name. This name is passed to the NSDL API as the second attempt.
2. **Credit bureau name:** At the post-mandate or submit opportunity stage (when we do our credit bureau pull), the customer’s credit bureau name is extracted and passed to the NSDL API as the third attempt.
3. **LSP name (optional):** LSPs may optionally pass the customer’s PAN name in the KYC init API. If provided and all three preceding sources have failed, the backend passes this name to the NSDL API as the fourth and final attempt before routing to non-STP.

**Current gap this PRD addresses:** In shadow deployment, the NSDL API is called across all name sources, but even when all fail, applications are not blocked — they proceed as normal. This means the regulatory requirement for PAN verification is not yet enforced. This PRD defines what happens when we move to production enforcement: if all automated sources fail NSDL verification, the application is routed to a manual ops review workflow rather than being rejected outright. If ops review also fails to resolve the mismatch, the application will be rejected. In other words, production deployment introduces real consequences for NSDL failures, with an ops safety net before a terminal rejection.

# **How do we measure success?**

- % of applications routed to NSDL non-STP
- % of NSTP applications approved by Ops
- % of NSTP applications rejected by Ops

# **What is the solution?**

## **Requirements Overview**

When all available NSDL verification sources (Aadhaar name, bank account name, credit bureau name, and LSP name if provided) fail, the application will be routed to the non-STP workflow for manual ops review, rather than being automatically rejected. This change is introduced at the Submit Opportunity stage.

## **Backend: Submit Opportunity validation**

- At the Submit Opportunity stage, introduce as part of the ‘deviation’ checks a new validation check: if NSDL PAN Verification status = FAILED across all sources (including LSP name, if provided), route the application to the Ops checker workflow
- This will  create a new ‘checker task’ in the Command Centre (
- All three names collected during verification must be persisted and pushed to the Command Centre task for ops review.

## **Command Centre: New data section for non-STP cases**

In the Command Centre, a new checker task called ‘NSDL PAN Verification’ is to be created for applications that have NSDL verification failed. This task will contain the following sections

Section 1: Deviation details

‘1.To be reviewed’ subsection

- Name received from Aadhaar
- Name received from credit bureau
- Name received from bank account
- Name received from LSP (if provided by LSP in KYC init API)

2.Review available names with supporting document

- Supporting document: PAN
- Note: PAN image name need to match with alteast name from any one of the sources
1. .Review Aadhar name with available names from other sources

Section 2: Opportunity details

- Customer Photo
- Reference ID : NSDL taks reference id (Format eg: NSDL1334456789)
- Name
- Mobile
- Email
- PAN
- Opportunity ID
- Created On

Section 3: Document review pane

The document viewer in Command Centre should display KYC & PAN document.

## **Ops agent actions — two approval paths**

The ops agent has two options to approve NSDL PAN verification manually:

**Option 1: PAN image match (if PAN available from DigiLocker)**

If the PAN document is available from DigiLocker (visible in the Command Centre document section), the agent manually compares the name printed on the PAN document with any one of the three names shown in the NSDL PAN Verification Data section. If at least one name matches, the agent approves NSDL PAN verification manually.

**Option 2: Cross-name match (if PAN not available from DigiLocker)**

If the PAN document is not available from DigiLocker, the agent checks whether the Aadhaar name matches either the credit bureau name or the bank account name. If at least one of these two matches, the agent approves NSDL PAN verification manually.

**If both checks fail at ops review:** The ops agent will reject the application. 

Note: Based on shadow deployment data, approximately 0.1% of total applications fail all available NSDL verification sources. Of these, a manual review of sampled cases shows every case passing at least one of the two ops checks — meaning we do not currently anticipate any rejections at the ops review stage. However, rejection remains a defined outcome. Should rejection cases appear in sufficient volume in production, a further fallback flow will be scoped in the future

# **User stories / User flow**

## **End-to-end user flow**

**Step 1: KYC completion**

Customer completes digital KYC via DigiLocker. Backend receives Aadhaar name (and PAN name if PAN is available via DigiLocker).

**Step 2: NSDL verification — Source 1 (Aadhaar / DigiLocker name)**

Backend calls NSDL PAN Verification API with PAN number + Aadhaar name + DOB. If pass → application continues normally. If fail due to name mismatch → proceed to Source 2.

**Step 3: Bank account verification → NSDL verification — Source 2**

Customer completes bank account verification. Backend receives the account holder name. Backend re-calls NSDL API with bank account name. If pass → application continues normally. If fail → proceed to Source 3.

**Step 4: Credit bureau pull → NSDL verification — Source 3**

At post-mandate or submit opportunity stage, credit bureau pull is performed. Backend extracts credit bureau name. Backend re-calls NSDL API with credit bureau name. If pass → application continues normally. If fail → proceed to Source 4 (LSP name, if provided by LSP in KYC init API), or trigger non-STP routing if no LSP name was supplied.

**Step 4b: LSP name → NSDL verification — Source 4 (if LSP name provided)**

If the LSP passed a PAN name in the KYC init API, the backend re-calls the NSDL API with this name. If pass → application continues normally. If fail → trigger non-STP routing. If no LSP name was provided, this step is skipped and non-STP routing is triggered directly after Source 3 failure.

*Note (Volt-specific): As Volt performs Decentro PAN fetch step prior to KYC as part of its application journey. The customer’s PAN name is retrieved at that point, and Volt passes this name in the KYC init API for all applications. Volt users therefore always have Source 4 available as a fallback.*

**Step 5: Checker task  at Submit Opportunity**

At Submit Opportunity stage, validation checks NSDL PAN Verification status. Status = FAILED → checker task created.  All name sources and PAN number are pushed to the task.

**Step 6: Ops agent review in Command Centre**

Ops agent opens the checker ask. Reviews the NSDL PAN Verification Data section (PAN number, Aadhaar name, bank account name, credit bureau name, and LSP name if provided).

Agent follows one of two paths:

- Option 1: PAN image available via DigiLocker → agent matches PAN image name against any one of the available name sources → if match found, approve.
- Option 2: PAN image not available → agent checks if Aadhaar name matches credit bureau name OR bank account name → if match found, approve.

If approved: LOS application unblocked in  submit opp workflow

**If rejected:** Application is rejected and Ops agent enters the rejection remarks in the ‘remakrs window’

DSP is required to communicate the rejection reason to the LSP so that the LSP can surface appropriate messaging to the customer in their UI. The rejection reason code and message to be shared with the LSP on NSDL ops rejection is:

- **Fenix code:** NSDL_PAN_VERIFICATION_FAILED;
- Fenix_message: NSDL PAN verification failed

# **Requirements**

## **Backend**

- Introduce NSDL PAN Verification status check as a validation gate at the Submit Opportunity stage.
- If NSDL status = FAILED (after all three sources), trigger deviation flow
- Persist all name sources used during verification (Aadhaar name, bank account name, credit bureau name, and LSP name if provided) and PAN number against the application record.
- Pass these data points to the Command Centre task on  deviation task
- On ops rejection, share the rejection reason code (PAN_VERIFICATION_FAILED) and rejection message to the LSP via the existing rejection notification mechanism

## **Design**

**DSP Changes**

Design changes are limited to the Command Centre ops tool. No customer-facing UI changes are required on DSP’s side.

**Command Centre : ‘NSDL PAN Verification’ checker task**

- New checker task : ‘NSDL PAN Verification ’ — displayed only for applications with NSDL verification status as ‘failed’
- Fields: PAN number, name from Aadhaar, name from bank account, name from credit bureau, name from LSP (displayed only if provided) — displayed as labelled read-only rows.
- Action: Approve / Reject NSDL PAN Verification — two buttons accessible to the ops agent within this section.
- Action: Remarks pop up

Design: 

![image.png](NSDL%20PAN%20Verification%20%E2%80%94%20Non-STP%20Rejection%20Handling/image.png)

[nsdl_pan_verification (1).html](NSDL%20PAN%20Verification%20%E2%80%94%20Non-STP%20Rejection%20Handling/nsdl_pan_verification_(1).html)

 **Volt Changes (LSP UI)**

When DSP rejects an application following a failed NSDL PAN ops review, DSP communicates the rejection to Volt via an error code. Volt must handle this error code and display appropriate UI copy to the customer.

**Error code received from DSP**

**NSDL_PAN_VERIFICATION_FAILED**

Volt to display the following error (full screen):

- Primary copy: “Unable to process your application”
- Secondary copy: “You’re not meeting the lender’s criteria”

Design: [Here](https://www.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-Ad-Hoc-tasks?node-id=1278-2&p=f&t=he1f85BcYrRTPziU-0)

[https://www.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-Ad-Hoc-tasks?node-id=1278-2&p=f&t=he1f85BcYrRTPziU-0](https://www.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-Ad-Hoc-tasks?node-id=1278-2&p=f&t=he1f85BcYrRTPziU-0)

# **Analytics**

DSP requirements(BE): [Here](https://docs.google.com/spreadsheets/d/1POA-6Ei420RvyeDxFg02L9BaPrKX0CA_7YhZP7uroB8/edit?userstoinvite=mohit.pareek%40voltmoney.in&sharingaction=manageaccess&role=writer&gid=191427461#gid=191427461)

Volt requirements(FE): [Here](https://docs.google.com/spreadsheets/d/1eZiOG4lnSelVgtZdYDCMJiQ87lxbxNofeB6cGQwzM44/edit?gid=842622648#gid=842622648)

# **Go to market**

### **Ops & Sales training**

- Ops team training required before go-live: agents must understand the two approval paths and when to apply each.

### Rollout Plan

- **Phase 1 — 10% rollout:** Enable production enforcement for 10% of users across Volt and Fenix, monitoring the key metrics.
- **Phase 2 — 100% rollout:** Expand to all users if Phase 1 is stable.

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)