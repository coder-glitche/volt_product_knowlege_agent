# VKYC Integration PRD

: Parikshit Kumar
Created time: February 24, 2026 12:33 PM
Status: In progress
Last edited: April 23, 2026 9:30 AM

# **What problem are we solving?**

We need to implement a regulatory-compliant, secure, and operationally resilient agent-assisted Video KYC(vKYC) process for LAMF customers that:

- Ensures completion within RBI-prescribed timelines (72-hour KYC window)
- Handles real-world Internet instability (call drops, reconnects)
- Maintains audit-grade recording integrity
- Enables structured governance via agent and auditor layers
- Enforces geo-validation (India-only compliance)
- Provides tamper-proof audit trails
- Prevents fraud via face match and SOP-based verification

Without this system:

- VKYC may breach regulatory timelines
- Call drops may cause data fragmentation
- Audit integrity may be compromised
- Fraud detection may weaken
- Agent decisions may lack oversight
- Geo non-compliance risks regulatory penalties

# **How do we measure success?**

### Regulatory Metrics

- % vKYC completed within 72-hour window
- 3-day KYC breach rate
- 100% sessions with geo-validation logged
- 100% sessions with consolidated video recording

### Operational Metrics

- vKYC completion rate
- Funnel level drop-off rate
- Call drop recovery rate
- Average session duration
- Rejoin success rate within reconnect window

### Governance Metrics

- Auditor override rate
- Zero missing recordings

### Risk & Fraud Metrics

- Face match failure detection rate
- Geo-outside-India detection rate
- No fragmented video records

# What is the Solution?

We will implement a DSP-orchestrated, Hyperverge-powered, DSP agent-assisted vKYC lifecycle with the following pillars:

### 1. Regulatory Control Layer

- Enforce 72-hour KYC validation before session start
- Re-KYC if KYC completed > 72 hours
- 24-hour link validity post first initiation

### 2. Resilient Session Management

- Configurable reconnect window
- 24-hour rejoin logic
- Session state tracking (Active / Interrupted / Finalized / Expired)

### 3. Consolidated Recording Integrity

Hyperverge must:

- Stitch all video fragments
- Deliver a single consolidated video file
- Include continuous timeline metadata
- Ensure audit-grade integrity

### 4. Agent-Led Structured Verification

- Live image capture (agent-controlled)
- PAN capture (agent-controlled)
- 3-way face match:
    - Live vs PAN
    - Live vs Aadhaar
    - PAN vs Aadhaar
- SOP-driven security questions
- Structured decision submission

### 5. Dual Governance Model

- Agent decision layer
- Independent auditor override layer
- Separate dashboards
- Immutable audit logs

### 6. Geo & Metadata Compliance

Hyperverge must provide:

- Call start/end time
- Latitude/Longitude
- Within India validation flag
- Face match scores
- OCR PAN extraction
- Device metadata
- Consolidated video file

Delivery via encrypted method

# Requirements/User Flow

## VKYC Initiation Trigger

There can be different trigger points for VKYC initiations, listing them down below:

### 1. Right after Digilocker KYC is completed (early in journey)

### Pros

Regulatory Safety

- 72-hour window is easily manageable
- Very low risk of KYC expiry
- Clean compliance positioning

Early Intent Filtering

- Only serious users move forward
- Improves quality of downstream funnel

Cost Savings

If users drop here:

- No mandate setup cost
- No pledge processing cost
- No agreement stamping cost

## Cons

High Drop-Off Risk

- vKYC is a high-friction stage
- Customer has not yet seen:
    - Final loan offer
    - Mandate setup
    - Agreement details
- Emotional commitment is low

CAC Inefficiency

- You spend acquisition cost upfront
- Large % may drop before monetization

Funnel Shrinkage

- Top-of-funnel significantly reduces
- Will impact disbursement volumes

### 2. VKYC trigger just before KFS & Agreement step

### Pros

High Customer Commitment

- User has:
    - Added bank
    - Set up mandate
    - Pledged MFs
- Psychological lock-in is strong

Higher Completion Probability

- Users at this stage are high intent
- Lower vKYC abandonment rate

### Cons

72-Hour Breach Risk

- Customers may take their own sweet time to move ahead in the journey before reaching the post Pledge step

Re-KYC Risk

If 72-hour window breached:

- Customer must redo KYC
- Creates friction
- Customer frustration

Operational Complexity

- Requires strong timer management
- Real-time expiry alerts
- Backend re-KYC handling

Cost Risk

- If customer fails vKYC at end:
    - Mandate cost wasted
    - Pledging cost wasted

### 3. Shift KYC towards later half of journey (e.g., after pledge), then trigger vKYC immediately after KYC.

### Pros

Best Regulatory Alignment

- vKYC triggered immediately after KYC.
- 72-hour rule easily satisfied.

High Customer Intent

- KYC is done when customer is already invested in journey.
- Drop-offs reduced.

Reduced Re-KYC Risk

- No long idle gap between KYC and vKYC.

Funnel Efficiency

- Customer already committed to loan.
- Higher completion rate.

### Cons

Journey and Tech Change

- Journey restructuring required
- Re-ordering flow logic
- State management impact

LSP Coordination Required

- All LSPs must:
    - Reorder flow
    - Re-test entire journey
- High operational friction

Rollout Timeline Risk

- Significant development effort
- QA impact

**Suggestion: Triggering VKYC before KFS and Agreement step**

## **Prerequisites for Call Initiation**

### **Trigger Point**

- vKYC is triggered either post Digilocker KYC completion or successful pledging(**To be discussed and finalized**). In MFD we can keep the trigger just before withdrawal.
- User is redirected to a DSP-controlled vKYC initiation screen.

### **BRE (Business Rules Engine) Validation**

Before initiating vKYC, the system must validate:

### **Time-Based Rule**

- vKYC must be initiated within 71 hrs 30 mins of Aadhaar fetch timestamp.

### **Outcomes**

| Condition | Action |
| --- | --- |
| Within 71h 30m | Proceed with vKYC |
| Beyond 71h 30m | Redirect to Digilocker KYC (via Digio) |

### **Compliance Constraint**

- Entire vKYC lifecycle must complete within 72 hours of Aadhaar fetch
    - Includes:
        - Video call
        - Auditor approval
- Buffer rule:
    - Call initiation allowed only till 71 hrs 30 mins
    - Remaining 30 mins buffer for audit completion

### **Digilocker KYC Flow in case of BRE check failure**

If BRE fails:

- Customer is redirected to Digilocker KYC
- Upon successful KYC:
    - vKYC journey is re-triggered
    - Flow resumes based on agent availability or scheduling option comes in

### **Session Creation**

Upon BRE success:

DSP sends to Hyperverge:

- Aadhaar photo
- DigiLocker PAN details
- Aadhaar fetch timestamp
- Workflow ID
- Transaction ID
- Answers of in-call questions

Post this the session is initiated.

### Business hours

Business hours is defined as the period/duration between which DSP VKYC agents and auditors will be available for conducting the VKYC process. It is related to the shift timings of the Agents and Auditors which will be decided by the Business once the VKYC team is hired. It will take into account Weekly business holidays and calendar holidays. 

1. If a customer attempts to do the VKYC journey during the business hours then they will be able to do so in real time.

1. If a customer attempts to do the VKYC journey during non business hours then they will get the option to schedule their call basis the BRE check and the Agents availability.

## **Information & Entry Screen**

When the customer starts the VKYC session then they will land on the Information Page where the instructions to be followed will be displayed:

![IMG_0999.jpg](VKYC%20Integration%20PRD/IMG_0999.jpg)

The above screen will be customized according to DSP requirements and it will have the below layout:

***“Welcome to Video KYC***

*You’ll soon be connected to one of our executives*

***Checklist***

1. ***Access Permissions(Camera, Microphone, Location)***
2. ***Please be seated in a place with good lighting***
3. ***Please ensure good and stable Internet Connectivity***

***Consent box(I agree to proceed with video verification process)***

***Start Journey CTA”***

(Note: No scheduling option CTA will be provided if the journey is done during business hours)

## **Scheduling Logic**

If the session is started by the customer outside business hours then the layout will be as follows:

***“Welcome to Video KYC***

*Currently none of our Video KYC Agents are online please click on the “Schedule” option below to schedule your Video KYC*

***Schedule VKYC CTA”***

Below is the default Hyperverge screen for VKYC call scheduling 

![IMG_1022.png](VKYC%20Integration%20PRD/IMG_1022.png)

Basis DSP requirements the above screen will be customized to show only slots basis the following: 

- Agent availability
- KYC validity window (Hyperverge will be using the Aadhar fetch timestamp to check this)

The CTA of ***click “here” to join back the queue*** will be removed. 

## **Permission & Pre-Queue**

Below are the mandatory permissions which the customer will be required to provide in order to proceed with the VKYC call:

- Camera
- Microphone
- Location

If any of the above permissions are not allowed then a pop-up will be shown to allow the specific permission. If allowing through the pop-up still not works then:

- Hyperverge shows enablement steps for each permission
- User is blocked from proceeding in the journey until all the permissions are granted

Below are the screens for each permission denied screen along with enablement steps:

**Camera:**

![IMG_1005.png](VKYC%20Integration%20PRD/IMG_1005.png)

![IMG_1023.png](VKYC%20Integration%20PRD/IMG_1023.png)

![IMG_1024.png](VKYC%20Integration%20PRD/IMG_1024.png)

![IMG_1025.png](VKYC%20Integration%20PRD/IMG_1025.png)

![IMG_1026.png](VKYC%20Integration%20PRD/IMG_1026.png)

**Microphone:**

![IMG_1007.png](VKYC%20Integration%20PRD/IMG_1007.png)

![IMG_1008.png](VKYC%20Integration%20PRD/IMG_1008.png)

**Location:**

![IMG_1010.png](VKYC%20Integration%20PRD/IMG_1010.png)

![IMG_1011.png](VKYC%20Integration%20PRD/IMG_1011.png)

![IMG_1012.png](VKYC%20Integration%20PRD/IMG_1012.png)

![IMG_1013.png](VKYC%20Integration%20PRD/IMG_1013.png)

After all permissions are granted successfully the below screen will appear:

![IMG_1014.png](VKYC%20Integration%20PRD/IMG_1014.png)

## **Pre-Queue Validation**

- Internet connectivity check by Hyperverge

![IMG_1016.png](VKYC%20Integration%20PRD/IMG_1016.png)

![IMG_1017.png](VKYC%20Integration%20PRD/IMG_1017.png)

![IMG_1018.png](VKYC%20Integration%20PRD/IMG_1018.png)

## **Queue Entry**

- Customer enters queue
- Agent dashboard notified

![IMG_1019.png](VKYC%20Integration%20PRD/IMG_1019.png)

1. The CTA of: ***Alternatively “schedule your call” for a later time** will be removed for DSP use case.*
2. The countdown timer in our case will be of 20 seconds but the call will get initiated if the Agent accepts it before the 20 seconds completion.

# **During Call Initiation**

## **Agent Allocation**

- Based on round-robin logic
- Only available agents eligible
- Agent manually accepts request

## **Call Acceptance**

- Once agent accepts:
    - Session locked
    - Call initiated
- Customer is connected
- Agent prepares for verification
- Recording setup initialized

# **Call Initiation**

## **Video Call Setup**

- Two-way video enabled
- Both cameras must remain ON
- Audio must be active

## **Automatic Capture by Hyperverge**

System captures:

- Full video recording
- Call start timestamp
- Geo-coordinates
- Within India validation flag

## **Call Drop Handling**

### **Scenario: Call Drop**

Causes:

- Internet issues
- Device shutdown
- App/browser failure

### **Handling Logic**

- In case of call drop due to any of the above scenarios the customer will be allowed to rejoin the call till **1 min** from the drop.(Note: Navi provides 15 seconds to rejoin)
- If the customer rejoins the call within 1 min the call will be started from the beginning.
- If the 1 min limit is breached then the customer must reinitiate the VKYC journey from the app/web.
- Previous partial session is not valid for compliance.

## Agent Verification Flow

### Introduction

Agent:

- Introduces self
- Confirms consent
- Confirms audio clarity

### Live Image Capture

- Agent captures live photo
- System validates clarity

### PAN OCR Validation

OCR validation will be executed basis the Digilocker PAN details shared initially by DSP to Hyperverge during the session creation.

If the customer’s Digilocker PAN fetch was not successful then they won’t be channeled through the Co-lending journey.

### 2-Way Face Match

Hyperverge system compares:

- Live Photo vs Aadhaar

### SOP Security Questions

Agent asks predefined questions to the customer. The questions are listed below and will need to get configured on Hyperverge:

1. Customer’s name
2. Customer’s DoB
3. Customer is salaried or self employed

~~Agent marks verified/not verified basis the answer given by the customer. If there is any deviation which between the actual answers and the answers given by the customer then the deviation is logged.~~

## Agent Decisioning

Agent selects either of the below options on the Hyperverge dashboard post the completion of the call:

- Approve
- Reject

Mandatory:

- Notes
- Rejection reason

Session ends

This call will then go to an Auditor for review post which the final status gets locked.

Recording stored by Hyperverge will be shared with DSP along with the Geo-tagging, Date-timestamp and Within India Validation.

## **Post Call Status**

After video call ends:

Customer sees on the screen:

**“Pending for Approval”**

- This remains until auditor decision

## Auditor Review

There will be a separate Auditor Dashboard

Auditor can:

- View consolidated recording
- View image
- View match scores
- View geo data
- View Within India validation
- View timestamp

Auditor action will override agent’s action

Auditor actions:

- Approve
- Reject (Retriable)
- Reject (Non-Retriable)

## **Final Status Outcomes**

| Scenario | Status | Next Step |
| --- | --- | --- |
| Approved | Successful | Customer notified |
| Rejected (Retriable) | Reattempt VKYC | Restart flow (BRE applies) |
| Rejected (Non-Retriable) | VKYC Rejected | End journey |

Audit log captures:

- Auditor ID
- Timestamp
- Reason for rejection

## **Buffer Window Handling**

If initiated near 71h 30m:

- 30-minute buffer applies

### Cases:

1. Call completed within buffer → Auditor must approve within remaining time
2. Call consumes full buffer →
    - Status: “VKYC Duration Expired”
    - Customer redirected to Digilocker KYC

## **Expiry Handling**

If 72-hour window breached:

- vKYC marked Expired
- Customer redirected to:
    - Digilocker KYC (via Digio)
- Post KYC:
    - vKYC flow re-triggered

## **Recording Requirement**

- Hyperverge must provide:
    - Final consolidated recording
    - Covering entire successful session

## **Status Persistence**

- All statuses to be stored in DSP backend via Hyperverge webhooks

Includes:

- All Events during call
- Agent decision
- Auditor decision
- Timestamps
- Final status

### App/Web handling post call completion

Once the VKYC call is completed the customer will be moving ahead in the loan journey and will land on the KFS/Loan Agreement page. We will be keeping a VKYC completed check during submit opportunity workflow to check if the VKYC is successfully completed or not. 

1. If it was completed successfully then the loan account of the customer will be opened. 
2. If it failed and is retriable then the VKYC journey will be triggered again basis the BRE check. 
3. If it failed and is not retriable then the customer will be displayed the following message: **“Loan Account can’t be opened because your VKYC is Rejected”**

## **Customer Communication**

Triggered via:

- SMS
- Email

For:

- Success
- Retry
- Rejection
- Expiry

# Dashboard Requirements

## Agent Dashboard

- Queue view
- Accept button
- Capture controls
- Match score display
- Geo flag indicator
- Reconnect status
- Session expiry countdown
- Decision submission

## Auditor Dashboard

- Recording playback
- Image preview
- Geo validation
- Risk score visibility
- Override control
- Agent performance tagging

## Command Centre

- During Account Creation task we will have a new parameter which the Ops team will verify. This will be the “VKYC” parameter. The values of the parameter can be: Successful, Rejected, Pending for approval and Re-initiate.
- During the Withdrawal task which will be created there will be a new parameter addition which the Ops team will verify. This will be “VKYC” parameter. The values of the parameter can be: Successful, Rejected, Pending for approval and Re-initiate. The withdrawal will be approved only if the VKYC is successful.

# Hyperverge Deliverables

Post-session:

- Single consolidated video file
- Call start & end timestamp
- Customer latitude & longitude
- Captured Image
- India validation flag
- Face match scores
- Risk flags
- OCR PAN details
- Device metadata (if available)

Delivery:

- Encrypted method

## Hyperverge Webhook Handling

[VKYC Webhook Events.pdf](VKYC%20Integration%20PRD/VKYC_Webhook_Events.pdf)

# **Analytics Requirements**

[https://docs.google.com/spreadsheets/d/1szGQtJaXtWLCWIM9AlS5oxb3oqkD6L2Hh_7u18UX2IM/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1szGQtJaXtWLCWIM9AlS5oxb3oqkD6L2Hh_7u18UX2IM/edit?usp=sharing)