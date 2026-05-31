# Volt Focused VKYC Journey Alignment

With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC.

This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey).

- Brief about VKYC and its process
    
    Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks:
    
    1. Customer verification
    2. 3 way Photo Verification
    3. Live location Check (Cx needs to be in India)
    4. Liveness Check
    
    Pre-VKYC contains following need to be managed steps:
    
    1. Pre-session messaging
    2. Device permission enablement and Instructions
    3. Consent for doing VKYC
    4. Scheduling
    5. Queuing
    
    During VKYC session following steps need to be completed:
    
    1. Security Questions
    2. Livininess Check
    3. PAN Capture
    4. Face Match
    5. Location Capture
    
    Post VKYC session following steps need to 
    
    1.  Based on Agent Marking the session as:
        1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review.
        2. Marking Session Failure: Customer needs to re-attempt VKYC.
        3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link
    2. Once the agent marks the session as a success, next is the Auditor Review:
        1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end
        2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC
        3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC

![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png)

As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process).

## Pre-VKYC

1. Initiation Page: 
    1. Pre-messaging: 
        1. Educate about VKYC
            1. Context Setting for the customer: 
                1. Mandatory Step by RBI
                2. Inform about the 3days rule
                    - What is the 3 days Rule?
                        
                        RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC
                        
            2. Instructions: 
                1. Having Pan Card Ready
                2. Having Stable Connection
                3. Enable Device Permission
            3. Positioning:
                1. Quick: Mention the time taken to complete (eg: <3mins)
                2. Build Trust: Data is 100% secure
    2. Device Permissions:
        1. Check and inform the customer to enable device permissions (SDK can access these device permissions)
        2. Enabling Permissions: 
            1. Triggers to receive permission and redirections to settings page 
            (incase of Android and iOS app) for enabling device permissions. 
            2. Pictorial steps for enabling device permissions before redirecting to the settings page
        3. Taking Consent: Include the Consent and the Terms and Conditions inside the T&C Checkbox before initiating the VKYC Session

Post the device permission checks, we initiate the VKYC SDK, 

→ Within the SDK, device permissions are checked again

→ After permission check, customer is placed in a queue awaiting connecting to the agent 

## Session Begins

Agent begins the VKYC session and takes all the necessary details from the customer as well as completes the checks which need to be done.

## Post Session (powered by webhooks)

1. Based on Agent Actions:
    1. Agent Success: The customer is taken to the disbursement/withdrawal page. The customer’s disbursement request is queued and waiting Auditor’s Approval.
    2. Agent Failure: The customer is requested to re-try the VKYC again. Also, showcase the rejection reason. Support Intervention.
    3. Incomplete: The customer is requested to re-try VKYC as it was incomplete. Support Intervention.
2. Auditor Actions:
    1. Auditor Success: Customer’s disbursement is initiated
    2. Auditor Reopen: Customer’s disbursement request is cancelled and customer is requested for to redo VKYC along with the reason. 
    3. Auditor Failure: Customer’s disbursement request is cancelled and customer is requested for to redo VKYC along with the reason. 

- Benchmarking files
    
    https://www.figma.com/board/Fi6QBxflSIqwF0CaPxb5V6/VKYC-Benchmarking?node-id=8-555&t=o6plo7fgjzFcjWWW-0
    
    → [*VKYC Benchmarking Google Sheet*](https://docs.google.com/spreadsheets/d/12UHl8-WEQRQ0pReEviKGpeBuCWozk3MW87SqMt2S7nY/edit?usp=sharing)
    
- Brief Comparisons:
    
    Slice VKYC:
    
    1. Scheduling Available
    2. Extended Timings till 11pm 
    3. 2 security questions
    4. Selfie assist with circle marked on screen to place the face
    5. No requirement to show the physical Pan Card
    6. Process completed under 1minute
    
    LazyPay:
    
    1. Gives option to do KYC + Selfie (liveliness check)
    2. Scheduling available in slots: last slot 8pm - 9pm
    3. Extended working hours available
    
    Tata Capital LAMF:
    
    1. No Scheduling possible
    2. Agent availability: Working hours only 
    3. 3 basic questions asked
    4. PAN required to be shown
    
    Yes Bank Credit Card (ANQ):
    
    1. Need to show my pan card and signature on blank sheet
    2. Work Apps SDK Implemented
    3. Differentiator: The changing of camera to front to rear is controlled by the agent
- 
    
    
    | Name | Scheduling Available | Video Session Timings  | PAN Card Required on Call? | Number of Questions | Total Time Needed |
    | --- | --- | --- | --- | --- | --- |
    | Slice SFB | Yes |  | No | 2 | <1min |
    | LazyPay (PayU Finance) | Yes |  | Yes | 2 | 3-5mins |
    | Yes Bank CC (ANQ) | No | 8am - 8pm | Yes | 3 | 4-7mins |
    | Tata LAMF | No | 9am - 6pm | Yes | 3 |  |
    | Unity SFB FD (Stable Money) | Yes |  | Yes |  |  |
    | Navi | No | 8am - 11pm | No | 1 | < 2 mins |
    | CRED |  |  |  |  |  |
    | Fibe  |  |  |  |  |  |
    | Shivalik SFB FD (Super Money) | Yes |  | Yes | 3 |  |
    | Refyne | Yes | 8am - 11pm | No | 2 | <4 mins |