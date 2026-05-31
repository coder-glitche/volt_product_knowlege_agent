# Command Centre design requirements

: Vaibhav Arora
Created time: July 11, 2024 10:17 AM
Status: In progress
Last edited: August 13, 2024 7:21 PM

Problem statement: User should be able to navigate between different interfaces/utilities on the platform

**Possible interfaces:** 

- Side navigation panel (Left) [Example: Material.io](https://m3.material.io/)
- Top navigation bar [Example: Apple](https://www.apple.com/)
- Drop down menu Example: Trello
- Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility)
- Card based notifications https://trello.com/u/vaibhavarora56/boards

**Utilities between which the user will be able to navigate:**

Tasks - All tasks tracking and assignment

Search (Client/Application/Credit) - Application level search

Notifications

NBFC dashboard: SLA tracking

Internal user management and access control

Analytics dashboard

Following are details of each section:

- Search requirements
    - Search
        - Ops agent should be able to search clients basis the following parameters:
            - Search customer
                - Name (Partial match)
                - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user)
                - Client ID (Exact match)
                - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user)
            - Search line
                - Line ID (Loan account number)
                - Client ID (Exact match)
                - Bank account number (To identify lines to which disbursements were made)
                - Transaction ID
            - Search loan application
                - Application ID (Exact match)
                - Mobile Number (Exact match)
        - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. 
        
        If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input)
        - The result screen should include the following parameters in order:
            - Client
                - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk)
                - Client Name (Name of the client)
                - Client Mobile (Mobile number of the client)
                - Client Email address (Hyperlinked for one click communication capabilities)
                - Last 4 digits of Aadhaar for the client
                - Client creation date (DD-MM-YYYY)
                - Client status (Active, Pending - in tab format)
            - Line
                - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk)
                - Product name (Loan against mutual fund)
                - Drawing power
                - Available limit
                - Principal outstanding
                - Interest due
                - Interest accrued
                - Charges due
                - Rate of interest
                - Tenure
                - Line activation date
                - Line status
            - Application
                - Application ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk)
                - Application type
                - Eligible limit
                - Pledged limit
                - Customer name
                - Product name
                - Current step
                - Application start date
                - Status
        - Result table should be clickable - Could be highlighted on hover to indicate the ops agent that they can go forward
        - To handle multiple pages:
            - Result should be paginated, and ops agent should be able to toggle how many results do they want to load in the first stage, by default the 10 results will be shown to the ops agent)
- Active Clients tab requirements
    - Active Clients
        - Ops agent should be able to track active clients (latest to last via this inteface. The UI should be similar to the search results page)
            - Parameters:
                - Status
                - Customer ID
                - Customer name
                - Mobile number
                - Email address
                - Created date
- Active lines requirements
    - ⁠Search loan results
        - Loan status
        - Loan ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk)
        - Customer name (Customer name should be highlighted to direct user to the client page)
        - Product name (Loan against mutual fund)
        - Drawing power
        - Available limit
        - Principal outstanding
        - Interest due
        - Interest accrued
        - Charges due
        - Rate of interest
        - Loan expiry date
        - Loan activation date
- Active applications requirements
    - Active Applications (Same as results page): Rows should highlight on hover
        - Status
        - Application ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk)
        - Product name
        - Application type (Consider clubbing of product name and application type - pill/tags)
        - Current step (color marked)
        - Customer name
        - Eligible limit
        - Pledged limit
        - Application start date
- Reports module requirements - Deprioritised
    - Reports
        
        ![Untitled](Command%20Centre%20design%20requirements/Untitled.png)
        
        ![Screenshot 2024-07-26 at 8.53.46 AM.png](Command%20Centre%20design%20requirements/Screenshot_2024-07-26_at_8.53.46_AM.png)
        
        ![Untitled](Command%20Centre%20design%20requirements/Untitled%201.png)
        
        - Report discovery:
            - Report discovery can either be in a list view or a tab view as shown in references above.
            - On clicking a left panel should open up which will ask for required parameters to run the report. For example for the holding data reconciliation report, user will be able to add the time frame (Date picker) and select RTA (CAMS/Karvy/All) to create a report
        - Reports and bulk actions section will help the ops agent generate and download various reports to assist them in NBFC operations. Reports will be classified into the following categories
        - Report download:
            - Reports will be heavy and may take time to generate, post generation user should be able to download the previously generated report via UI in the report history tab.
            - User will only see history of reports generated by them
        - Reconciliation reports
            - Holding data reconciliation report
                - Ops agent will be able to select the timeframe of pledged assets in the report
                - Ops agent will be able to filter the report basis RTAs (CAMS/Karvy)
                - Ops agent will see the option to download the report, report can be directly downloaded to the user’s system.
            - Withdrawal reconciliation report
                - Ops agent will be able to select the timeframe of of transactions in the report
                - Ops agent will see the option to download the report, report can be directly downloaded to the user’s system. (Excel file download)
            - Repayment reconciliation report
                - Ops agent will be able to select the timeframe of of transactions in the report
                - Ops agent will see the option to download the report, report can be directly downloaded to the user’s system. (Excel file download)
        - Utility reports
            - Mandate presentation file (Ops agent will be able to generate the mandate presentation file for the NBFC)
            - Margin report (Ops agent will be able to generate a margin risk report where all clients under risk will get populated with the respective shortfall details)
        - Management reports
            - Active client list (Client level)
            - Active lines list (Line level)
            - Active line summary (NBFC level)
        - Accounting reports: (Can use finflux UI to generate these reports)
            - Trail balance report
            - Balance sheet
            - Income statement
            - Journal entry details
            - General ledger
- Task manager module requirements
    - Task manager
        - User will be able to do tasks related to NBFC operations through this module. Tasks will be divided into two types:
            - Create request
                - Will have input parameters that the ops agent will have to enter to create the request
                - Input parameters can be consumed in following ways:
                    - Radio buttons
                    - Checkboxes
                    - String input (text box)
                    - Number input (text box)
                    - Drop downs with pre-filled options
                - Will need error states to show validations and failures to the user for invalid requests
                    - Snack bar error (feedback error post submission of maker)
                    - Alert dialogs
                    - Field highlighting with red
                - Will need an interface to show data as per the request made to the user so that they can make the right choice (Need steppers to validate information entered by the ops agent)
            - Approve request
                - User will be able to perform multiple actions on a approve request:
                    - View request (necessary parameters against each request will be shown to the ops agent
                    - Approve request (Approving the request will update the status of the request. This should change the status of the request and should show a confirmation modal to the user (”Are you sure you want to approve this request?”)
                    - Reject request (Ops agent can reject approval requests) Similar handling with a confirmation modal needs to be done here
        - Tasks will be divided into following categories (Can be tabs within the tasks section, each tab will contain two big CTAs (Create a request/Approve a request)
        
        Create a request will open a form where the user will be able to select the type of request basis the section they are in
        
        Approve a request will take the user to the specific section where approve requests will be shown to the user for approval
        
        ):
            - Loan application
            - Loan servicing
            - Client management - To be moved to line/application
            - Admin (remove tabs add column value)
        - Following tasks will be present in each category:
            - Application management
                - Credit approval (Approve request)
                    - @Saksham Srivastava can you add requirements for UI
            - Line management
                - Create requests:
                    - Line operations
                        - Freeze line
                            - Input parameters: Line ID (numeric)
                            - Output parameters: Client name, Line activation date, Sanction limit, Drawing power, Total outstanding, Principal outstanding, Interest outstanding, Charges outstanding, Accrued interest, Line activation date, Line expiry date, Line status 
                            
                            (Reference to the line details page which the user can open in a new tab should be added)
                            
                            (Re-evaluate sectioning)
                            
                            - Action: Freeze line (CTA)
                        - Refund interest
                            - Input parameters: Line ID
                            - Output parameters: Client name, Line activation date, Sanction limit, Drawing power, Total outstanding, Principal outstanding, Interest outstanding, Charges outstanding, Accrued interest, Line activation date, Line expiry date, Line status  
                            
                            (Reference to the line details page which the user can open in a new tab should be added)
                            - Action: Collect amount to be refunded in an input, Refund interest (CTA)
                        - Update sanction limit
                            - Input parameters: Line ID
                            - Output parameters: Client name, Line activation date, Sanction limit, Drawing power, Total outstanding, Principal outstanding, Interest outstanding, Charges outstanding, Accrued interest, Line activation date, Line expiry date, Line status  
                            
                            (Reference to the line details page which the user can open in a new tab should be added)
                            - Action: Collect amount to be refunded in an input, Refund interest (CTA)
                        - Update tenure
                            - Input parameters: Line ID
                            - Output parameters: Client name, Line activation date, Sanction limit, Drawing power, Total outstanding, Principal outstanding, Interest outstanding, Charges outstanding, Accrued interest, Line activation date, Line expiry date, Line status  
                            
                            (Reference to the line details page which the user can open in a new tab should be added)
                            - Action: Updated sanction limit input, Update Sanction limit (CTA)
                        - Manually post interest for line
                            - Input parameters: Line ID
                            - Output parameters: Client name, Line activation date, Sanction limit, Drawing power, Total outstanding, Principal outstanding, Interest outstanding, Charges outstanding, Accrued interest, Line activation date, Line expiry date, Line status 
                            
                            (Reference to the line details page which the user can open in a new tab should be added)
                            - Action:  Post accrued interest (CTA)
                        - Close line:
                            - Input parameters: Line ID
                            - Output parameters: Client name, Line activation date, Sanction limit, Drawing power, Total outstanding, Principal outstanding, Interest outstanding, Charges outstanding, Accrued interest, Line activation date, Line expiry date, Line status 
                            
                            (Reference to the line details page which the user can open in a new tab should be added)
                            - Action:  Close line (CTA)
                    - Transaction operations
                        - Place withdrawal
                            - Input parameters: Line ID
                            - Output parameters: Client name, Line activation date, Sanction limit, Drawing power, Total outstanding, Principal outstanding, Interest outstanding, Charges outstanding, Accrued interest, Line activation date, Line expiry date, Line status 
                            
                            (Reference to the line details page which the user can open in a new tab should be added)
                            - Action:
                                - Withdrawal input form:
                                    - Withdrawal amount
                                    - Withdrawal date
                                    - Payment type (Online transfer / Adjustment)
                                    - UTR (only if payment type is online transfer)
                                    - Remarks/Notes
                        - Add repayment
                        - Undo withdrawal
                        - Reverse repayment
                        - Reverse charges
                        - Post charges
                    - Collateral operations
                        - Add collateral
                        - Remove collateral
                        - Sell-off of collateral
                - Approve requests
                    - Transaction operations
                        - Approve withdrawal
                        - Approve repayment
                        - Approve withdrawal undo
                        - Approve repayment reversal
                        - Approve charges reversal
                        - Approve charges posting
                    - Collateral operations
                        - Approve collateral addition
                        - Approve collateral removal
                        - Approve collateral sell-off
                    - Line operations
                        - Approve sanction limit update
                        - Approve tenure update
                        - Approve interest posting
                        - Approve interest refund
                        - Approve line closure
            - Client management
                - Create requests
                    - Update mobile number
                    - Update email address
                    - Update bank account
                    - Update mandate details
                - Approve requests
                    - Approve mobile update
                    - Approve email address update
                    - Approve bank account update
                    - Approve mandate details update
            - NBFC management
                - Create requests
                    - Update IFSC master
                    - Update approved collateral list
                    - Generate withdrawal reconciliation file
                    - Generate repayment reconciliation file
                    - Generate collateral reconciliation file
                - Approve requests
                    - Approve IFSC master update
                    - Approve collateral master update
- Profile module requirements
    - Profile
        - Profile section of the user will give user information regarding their role and will allow the user to log out from the service dashboard. This will be a small pop up on the top right section of the command centre.
        - Upon clicking user will see the following details:
            - User name
            - User email address
            - User current role
            - Log out option for the command centre
- Notifications module requirements
    - ⁠Notifications
        - Notifications tab will help user take action or get notified on different events that happen against their request (V1):
        
        There can be CTAs on notifications, user will be able to mark notifications as read or not read as a high level configuration. By default latest 20 notifications (Read and unread will be visible to the user). On scrolling more notifications will automatically load.
        
        User will be able to see the time and date of the notifications, there should be a visual distinction and sectioning between read and not read notifications
        
        If there are not read notifications, user should be able to see a red dot on the notifications button
            - Type of events:
                - Approval of maker request made by the user
                    - Withdrawal request for <customer name> and LAN 104567  is approved
                    - Repayment reversal for <customer name and LAN 34232 is approved
                - Rejection of maker request made by the user
                    - Withdrawal request for <customer name> and LAN 104567 was rejected with note: “Invalid UTR”
                    - Repayment request for <customer name> and LAN 34322 was rejected with note: “Incorrect details.”
                - Report generation completion requested by the user
                    - Withdrawal reconciliation report is now ready for download
                    - Repayment reconciliation report is now ready for download
                    - Collateral reconciiliation report is now ready for download
                - General utility based notifications:
                    - Mandate presentation reminders
                    - Reconciliation reminders
- Side modal module requirements
    - ⁠Side modal - Here the only requirement should be to come up with references
        - Use cases:
            - Maker checker (Task details)
            - Line actions:
                - Freeze line
                - Manual withdrawal request
                - Withdrawal reversal request
                - Repayment reversal request
                - Interest update request
                - Charges posting request
            - Client actions:
                - Update client details (Mobile/Email/Bank account)
            - Application details
                - Approve credit referral request
        
        ![Untitled](Command%20Centre%20design%20requirements/Untitled%202.png)
        
- Landing page module requirements
- Login page module requirements
- Client details page
- Line details page
- Application details page