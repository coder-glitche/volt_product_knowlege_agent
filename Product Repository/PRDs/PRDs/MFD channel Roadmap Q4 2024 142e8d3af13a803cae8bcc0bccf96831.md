# MFD channel Roadmap Q4 2024

: Naman Agarwal
Created time: November 18, 2024 10:32 AM
Status: Not started
Last edited: December 23, 2024 4:13 PM

[Kapture CX](MFD%20channel%20Roadmap%20Q4%202024/Kapture%20CX%20165e8d3af13a8003a45be22c5308f5ea.md)

Questions To ask?

- For growth in MFD channel is a Lack of market? Lack of information ? lack of distribution?
    - what is our current per MFD application per month count
    - What is possible application per month count . AKA we get all the LAMF business form the the MFD
        - How many MFD are aware of the LAMF solution ?
        - How many MFD have given  a LAMF before?
        - How many customers come to MFD for a Liquidity need ?
- How many Applications are completed without assistance in the current journey
    - What the major hold up and issues that require manual intervention ?
    - What is the resolution to these issues ?
        - Sales based
        - Product based
- How many applications require servicing requests ?
    - What are the issues ?
    - What is their resolution
        - support based
        - Product based
- What is the performance of the sales driven Workflows /solutions ?
    - Sales efficiency metrics
    - Inbound
    - Outbound
- What is the performance of the Product driven solutions ?
    - Product metrics

LAMF sales 

- Unaware
- Problem Aware
- Solution Aware
- Product Aware

MFD channel System design 

Current problems 

- 

North star is AUM with check of cost 

number of MFDs * activity of the MFDs

Acquisition

Activation

Retention 

Revenue

| Acquisition
 | Top of the funnel  |
| --- | --- |
|  |  |
| Activation
 |  |
| Retention |  |
| Revenue |  |

User stories

1. MFD hears about the volt money 
2. MFD registers on volt platform or tries Volt on partner platform 
3. MFD creates application for the customers 
4. MFD services the customers 
5. MFD get the payout for the business they bring 

Creating applications for customers require -  Volt product , if there is a issue then reach out to servicing 

Communications 

Resolutions 

CRM

# Marketing

- Not in scope in this qtr

# Platfroms

## Volt Platforms

- Identify Key usage patterns ( Funnels)
- Identify the Key challenges in volt MFD dashboard and MFD app
- Prioritise solutions

Partner B2B Platforms

- Maintain the Funnels provided to partners
    - Partner will not be able to provide us with the status on the funnels from there side , we have to build solution to catch and identify the issues partners are facing
        - Talk to Partner MFD is they raise issues
        - Add Logs and tests in SDKs to proactively

### CRM

orient LSQ to AUM 

- Find and solve misalignments
    - Mis-allocated leads
    - Incomplete information in leads
    - wrong info in the leads
    - Team incentives misalignement

Tasks to solve the LSQ alignment 

- Solve all types of mis allocations -
    - Automated MFD to RM mapping - 100% mapping of the MFDs to RMs
        - VOLT  (pre, post activation)
        - Partner - Redvision
    - Correct channel attribution
        - B2C to B2B2C
            - Understand and solve the root cause of the borrower going to wrong platforms
            - Pass data to LSQ in cases the lead channel is changed from Admin actions
    - Correct Lead status
        - Lead status  mismatch between LSQ and DB
        - Lead Status mis configuration in LSQ and DB (portfolio pledge)
    - Backfilling data
        - MFD details for Leads (B2b2c, redivision)
        
    
    ### Communications
    
    - Track Responsiveness - @Tushar Luthra
        - Whatsapp
            - Move to Wati with better Analytics and automated chatbots from Periskope
            - Get the responsiveness tracking on wati
        - Call
            - Reduce missed calls (Runo, LSQ activity linking )
    - Improve responsiveness
        - Set up chatbot for common queries
    
    ### Resolution
    
    - Track Resolution TAT and breakup of tickets
        - Create tickets for Partner requests for all issues, and servicing
        - 100% disposition for the Calls and Whatsapp. once we know what the partners are reaching out for then we can mandate which requests should go in tickets
        - Search and finalise a ticketing system
            - sync with Tushar to understand Zendesk Whatsapp
        - Label and track tickets and establish ticket category based TaT
        - Provide the TaT to the partner
    - Reduce issues
        - List the issues and prioritise the solutions
    

MFD channel 

Acquisition 

Activation 

## Retention

Value provided to the user

- Benefits
- Cost
    
    

Served by RMs 

- Responsiveness
    - Customer faces issues or have a query
        - Knowable issues
    - Customer reaches out
    - Customer receives communication back
    
- Resolution
- Base product performance

Questions?

Market 

- what are AUM wise distribution of MFDs 1,50,00 ?
- What the platforms MFD uses?
- What are different categories of MFDs? what is their persona?
- What are the channels to reach MFDs ?
- What device MFD mostly use , desktop vs Mobile ?

How can we best segment MFDs ?

|  | low volume | High volume |
| --- | --- | --- |
| HNI |  |  |
| LNI |  |  |

Type of MFD 

- Individual practice
- Corporate MFD
- Partnerships
- **National distributors**
- **Independent financial advisors**

What is the list of platforms Volt is available on ?

What are the number of Impressions we have on these platorms?

- How many registed MFD?
- How many activated MFD?
- TAT to activate MFD?’
- TAT to complete loan application from Offer selection
- TAT to complete loan application from Registration of customers
- Number of customer registed per MFD?
- Number of Customer Check limit per MFD?
- Number of Eligible customer per MFD?

Attribution of 

- the Impressions to Registration
- Registration to Credit limit fetch
- Credit Limit to offer
- Offer to KYC
- KYC to BAV
- Multiple BAV customer , i.e why they have to change the bank account , TAT to change the bank account
- Mandate step
- Disbursement issues

common complains of MFDs ?

reason for churn ?

Here's a concise list of distinct LSQ bugs and requirements from the document:

Bugs:

- Incorrect mapping of LSQ pledge steps (MF_Pledge vs Asset_Pledge)
- B2B2C leads incorrectly tagged as B2C in LSQ
- User stage incorrectly updating post loan completion
- Incorrect stage updates in LSQ for completed loans
- MFD status not updating properly
- Enhancement application status not updating
- Name not flowing into LSQ when MFC is fetched and dropped off

New Requirements/Product Scoping:

- Backfilling of LSQ B2B Platform MFD data
- Stickiness tracking for B2B Platform MFD & RM
- BOTFU leads assignment workflow changes
- Different disposition structure for B2C & B2B2C teams
- Multiple disposition tracking for multiple calls
- Different opportunity types (Renewal, Enhancement, New)
- User activity tracking from Web/App to LSQ
- Data sanity improvements for RedVision MFDs
- Inbound call tracking as sales touch
- Lead conversion stickiness to stage
- Lead reconciliation between DB and LSQ
- Alert system for critical issues

#