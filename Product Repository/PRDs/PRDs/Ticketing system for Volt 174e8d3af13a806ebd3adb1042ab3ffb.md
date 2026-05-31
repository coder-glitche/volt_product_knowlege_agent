# Ticketing system for Volt

: Naman Agarwal
Created time: January 7, 2025 7:07 PM
Status: In progress
Last edited: February 19, 2025 3:20 PM

# **Problem Statement:**

Volt intent to provide best in class support to the Partners and customer. Due to the Nature of product being the Credit application, significant amount of support is needed to provided to the Users

To scale efficiently we need to Move more applications to Zero touch and and Handle the support Requests that we do get more efficient. 

Applications successful  = With + without assist = Count * Cost 

Current Support team are facing following challenges 

Borrower

- Long wait times for the agents to get back
- Chat support

- visibility
    - we don’t have rich visibility on the Ongoing calls and messages to the Agents. We would like to How many query of a particular issue was received and can we solve it through product.
    - RMs and agents have to provide context in sending the client Between RMs or on Leave
    - We would have a data on the issues raised by a particular customer or to maintain history of support

- If the support request is not OPS or Tech realted then taking followup
- High Inbound Traffic :- Agents are move from call to call and saving
- Lack of a single source of truth for customer issues.
- Inconsistent tracking across calls, WhatsApp, and emails.
- Unrecorded issues, especially from phone calls.
- No SLA tracking or identification of common problems.

**Key Requirements:**

- **Mandatory Ticketing**: Every interaction (calls, WhatsApp, emails) must generate a ticket.
- **Ticket Details**: Include customer phone, partner/platform ID, creator ID, issue category, description, channel, owner, status, and resolution notes.
- **Workflow Needs**:
    - Easy ticket creation and search by phone number.
    - Visibility into all tickets per customer/issue.
    - Strong APIs and customizable workflows.
- **Tool Integration**: Must work with Exotell, WABA, email, Slack, and the customer database.

**Goals:**

- Achieve 100% ticketing for all interactions.
- Track and measure issue resolution times (SLAs).
- Identify bottlenecks and common problems.
- Prevent any customer issue from being overlooked.

The Workflows that need to be enabled 

- Grouping of users
- 

Page-nation for the pending and completed application 

The Filter for the lead stage to be added 

Add filters in the pending application

User stories 

- Customer will call us
- customer is routed to a agent - How is this routing setup?
- Agent takes notes on the call
    - Dispostion form
    - Issue details
- Basis issue of the ticket the ticket is processed
- The resolution is communicated

Requirement from the Ticketing system 

Grouping 

- Should be able to make agent groups
- should be able to add customer/MFD into a group
- Should have group of 1000+ for the MFD list
- Should have the Ability to assign customer groups to agent groups
- Should be able to make 500 + groups
- Should be able to make 500+ logics of assignment

Call handling - 100% dispostion of Calls

- Initiate calls from the desk
- Inbound call handling
    - Save call details
    - automatically open dispostion from
    - Save missed call tickets
    - Ticket should open up a form for the user to fill
- Create tickets for the missed calls

Workflows 

- Reminders based on ticket status and time passed on a stage
- Escalation if the ticket has not been closed within a specified time

Ticket object 

- the Ticket should know when it was created by who and store changes made
- we should be able to add forms to ticket
- the Data of the form should flow when pulling the tickets
- the changes made should be in ledger form not overideable
- Add stages in Tickets

Forms 

- Easy to create and customisable forms

Analytics 

- send the ticket data with the ticket form data
    - We need to be able to set l1, l2, l3
    - and track the instances
- Calculate send-backs on the tickets
- TAT solution basis tags and filter
- Open, Pending, Closed.

- Assignment logic ability, Like round robin , and backup assignment
- 
- Integration with Exotell
- Integration with

Zendesk and jira issues 

Collect requirements from everyone to prepare the ticketing system 

Sales manager 

Agent Workflow 

1. Customer Contact 
    1. How is the contact received?
        1. Call
            1. Inbound
            2. Outbound
        2. Whatsapp
            1. central 
            2. Personalised 
        3. Email
2. Where can Agent see the Contact? 
    1. Exotel
    2. WATI 
    3. Periskope
    4. Gmail
3. What is the type of request ?
    1. Question, process related understanding 
    2. Problem faced, Deviation from the Process
    3. Order status, - Provide the status of the activity to the caller
4. How do we resolve the Request?
    1. Question: Answer the question / refer & share documentation / send request to Different individual
    2. Problem faced: Note the problem and Investigate the Problem. 
        1. Prepare the Customer data facing the issue 
        2. Mark the ticket or the issue in issue Buckets 
        3. Refer to the SOP of the Issue category mentioned
        4. Add details about  the problem as per customer 
        5. Ask clarifying questions to the user about the issues 
        6. Actions as per SOP
            1. Raise OPS/tech tickets 
            2. Use ADMIN actions to resolve the issues 
        7. Confirm with user is the problem is solved or Follow up 
        8. Close the Ticket 
    3. Order status 
        1. Create ticket with issues categories
        2. check for the SOP against the issue category 
        3. Check the relevant details in the retool and self close
        4. If the Details are Offline then Raise it to OPS to get it from Lenders
        5. Set up followup and mention TAT to use.
        6. close the ticket with the Information
5. How to assign the ticket to the others?
    1. The Agent should be able to send the ticket to the other Groups 
    2. 
    
    AMRIT
    
    - Ticking system should be able to Notification on Email or slack
    - ticket assigment to same team members
        - Incases of leave , or other issues
    - the Ticket should be able to handle the Data of the cases like opening account , like adding documents , and long details
    - The Ticket should be able to be closed by the issues themselfs
    
    somesh 
    
    - Issues missing in the service form, Others option , ( challange here if we enable other that there will be issues with lazy marking , if not given then the issues will be miscategorised )
    - Option to Reopen ticket . currently ops can close the ticket that was opened by RMs
    - There is a communication gap
    - Mis mapping of tickets , allow user to reassign tickets
    
    Vishal
    
    - Notification & drop-down, auto self assignment when creating tickets
    
    Mansi
    
    - Auto escalations in cases of No response
    - Nested ticket as the tickets are assigned to lender.
    - DSP to increase Sanction Limit ability to the Agents
    - VTS-8852 for the Tata repayment issues
    - What happens if the Tickets are raised and need follow - up
    - Rm - support Rm , context . contact on the
    
    Kanto heath - had a inhouse chatbot 
    
    - Hubspot , - create ticket for the each issues
    - TAT based escalation
    - Auto email based on sheet
    
    B2c call support team 
    
    - Notification on the Update or edit of  a ticket,
    - Are notes visible for all the customer?
    - Fresh-desk , incoming call ticket,
        - Dispostion ,
        - notes
        - Customer support group , assign the Tickets to group
    - Disposition time after call to fill the disposition before next call
    - Tickets merge for the customer calls , as there could be multiple calls for the for the same issues
    - Automated Number based actions to the RMs, where they can enter number and the communications can be send with the required information
    - 
    
    Global 
    
    - Require Ticket ID to Open Retool /Appsmith  to have the tracking
    - Flag a ticket for your manager to review in cases of Lack of support
    - Tickets getting deleted - should not be allowed
    - Tickets to be assigned to Group , not individual
    
    ## 
    
    - **Problem 1- High inbounds- Call & chat**
        - Why this is high?- *We need telemetry to understand the Daily breakup of issues and volume to respond accordingly*
            - Customer reaches out for multiple queries & issues?  - *Reach out of same customer for multiple issues, reach out of multiple customer For same issue.*
                - Why cant we productize it? - Need clear problem statement and Volume to prioritise a product solve where ever possible
                    - Because we don’t know The reasons of user reaching out to us?
                        - Why? - *Because we are not marking Dispostion and Inquery details on the associated with the C*all
                            - Because we are not storing dispositions of inbound calls in our system - *No aligned process as of Now to store dispostion, Process of storing not efficient from a agent perspective*
                
    - Problem 2- My Support team spends a lot of time just solving the tickets.
    Eg. AHT of an inbound call is 6 min - *What does does this time Involve? ( Call duration, query handling …) . the Agent tries to solve the issue on call, as they would receive the next call immediately and they cannot process the Earlier call query. we need to add visibility for the issues and how are they solved by agents to reduce the AHT, which is Call duration.*
        - Why this is high?
            - Because team efforts goes into A) Understanding issue B) Identifying root cause - Current process is the User sees the Incoming call number on Exotell, and search Retool for the Information.
                - Why it takes time here?
                    - Juggles with multiple tools
                        - Retool- To understand customer history— Copy paste number
                        - Takes time to go through specific part in Retool to find the document to cross check: - *Retool /appsmith can be configured to provide the most referred data first to reduce the time, To create a flowchart /waterfall of user information in terms of releveance to support*
                        - Then checks Zendesk to check if issue is raised already :- *IF we can have a ticketing tool for the Incoming call and the Individual view and history comes up that could save time*
                        - If not, then raises ticket or does follow up on existing ticket - *Ticketing tool should track TAT and provide the ability to take followups , Current escalation and followups are on Mail, slack other channels and are harder to track to understand the Time required for a agent to solve or get resolution of a ticket*
            - **Best case scenario**
                - Call comes up
                - Pop up opens in Support tool which contains all information of user history (Similar to of Retool)
                - Also contains past interactions just to check if this customer is calling for the first time or is following up on his issue (Data to be triangulated via exotel, wati & email) —> Omnichannel context building
                - Also contains existing ticket raised for this customer & the update on this. SO that the agent can provide instant update to the customer & provide accurate ETA
                - Support tool should also contain guide to troubleshoot the customer
                    - For eg. When customer called he was at Mandate
                    - So troubleshoot guide should be visible in front of the agent, which they can read & solve the problem—> Kind of a decision tree
                    
            
            ## MFDs
            
            **Problem**
            
            - RM is not able to track all the issues raised with respect to their MFDs as the knowledge is still stored only in Whatsapp chats :- *The Inquiries need to passed to the ticketing tool by the agent from call and WA, the Ticketing tool should enable the Different persona of the Users, For a MFD we should have linked customers and the tickets could be linked to both MFD and browser.*  What is the Ideal workflow for a agent to pass this information , how can it be automated to an extent. explore with the vendors
            - Zendesk ticket is raised from customer POV & not MFD/Partner POV
                - As in tagging of MFD should be there so that RM can track all issues of his 500 MFDs allocated - *Tickets should be able to associated to multiple customers*
            
            - **Best case scenario**
                - RM can view all tickets of his MFDs in one place - *We need ablity to create custom view basis filters on the tickets for  the Agent*
                - Also track multiple tickets of 1 MFD
                - All issues whether its new customer, existing or even his payout should be into this one tool only to track & manage