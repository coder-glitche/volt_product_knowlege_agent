# LSP Focused VKYC Journey Alignment

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

As an NBFC, our control is limited over the Pre-VKYC  and Post-VKYC user experience. 
Following are the steps of a VKYC journey which we govern:

## Journey Flow:

### Pre-VKYC Session:

1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP)
    - What is the 3 days Rule?
        
        RBI mandates VKYC be completed within 3 days from completing e-KYC.
        If the customer does not, lender will need to initiate the e-kyc flow before initiating VKYC
        
2. Device Permission Check, Instructions, and Consent: 
    1. Device Permissions: 
        1. We check the permissions enabled for our LSP’s application; our environment is a wrapper SDK which relies on these device permissions
        2. If any one of the permissions are disabled, the wrapper SDK triggers the device OS permissions to enable permissions for the LSP’s application.
    2. Instructions:
        1. We inform the need for:
            1. Original PAN Card
            2. Device Permissions (Camera, Microphone and Location)
            3. Stable Internet Connection
    3. Consent: 
        1. Wrapping the consent and permissions for V-KYC into T&C checkbox
        
3. Queuing:
    
    2a. Content and Screen Elements:
    
    1. Need an engaging element to reduce customer drop-off → having a countdown timer from 30s. If the timer ends, we showcase the position of the customer in the queue.
    2. Repeat the instructions while the customer waits in the queue
    3. Comforting copy on the screen 
    4. Large indicative animation (green tick) and messaging just before connecting with the agent
    
    2a. NBFC Queuing Process:
    
    1. Set agent availability: 9AM - 7PM | Monday - Saturday
    2. Agents are assigned the cases on a round-robin basis
    3. Maintain queuing time of under 30s for Cx
    

### During VKYC Session

1. Quick and to-the-point interactions
2. Steps required to be completed by the agent:
    1. Customer’s Original PAN Card :
        - Agent request the customer to have their PAN Card handy
    2. Check livliness of the customer: 
        - Agent requests the customer to recite the OTP on the screen
    3. Customer Verification: 
        - Completed by asking 1 security question
    4. PAN Verification:
        - Customer is requested to place the PAN Card flat (or held in their hand)
    5. Photo Verification:
        - User is requested to place their face within a well marked oval
        - Agent checks for a 3-way face-match between the selfie, Customer’s photo on their Aadhaar Card and Customer’s photo on their PAN Card
    6. Location Verification:
        - Agent captures the location of the customer using customer’s device GPS
    
    The Agent marks the VKYC Session as:
    
    1. Success: The customer’s VKYC session gets pushed to the auditor’s queue. Webhooks to inform the LSP; LSP can complete the application further (or better take the withdrawal request and queue the request on their end) 
    2. Failure: The customer will need to re-attempt VKYC. Webhooks to inform the LSP that the VKYC Session was a failure along with the reason.
    3. Incomplete: The customer will need to resume VKYC using the same link; Webhook to the LSPs with the reason
    
    ### Post VKYC Session
    
    The Auditor marks the VKYC session:
    
    1. Success: The VKYC has been successful for the customer; LSP can proceed with the next steps.
    2. Failure/Re-open: The customer will need to re-initate a VKYC for the customer; webhook to the LSP to inform the VKYC session has been marked failure/re-opened along with the reason.
    

Along with the above functionalities, we need to provide the LSP error messages to make sure the LSP and the customer are well informed.