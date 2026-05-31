# PRD - GST Invoice and Payout statement creation and approval

Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on  a regular basis. 

high level MFD GST invoice flow 

- Volt Calculate accurate base Payouts
- Generate GST Invoice
- Send GST tax Invoice to partner
- Get approval from Partner over Email
- Pay GST invoices
- Handle issue if mentioned
- Close the GST for the month.

## Phase 1 - Development needed

### Tech

- Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why.
- Generate Invoice creation
    - Fix Invoice templates (Payout + GSTN) + recon templates
    - Generation bulk Invoices
- Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this )
- Storing the Invoices and consent agasint Accounts payable and payments
    - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers

### Business

- Process to Verify GSTN (manual)
- Process to collect / modify Bank accounts with maintained records
- Process to take approvals for Payouts and GSTN
- Process for tracking and storing issues in Payouts
- Process for triggering reconciliation payouts and communications
- Process for sharing GST data with Jars
- Process for updating reconciled payouts with Ledgers
- Process for approval of the Reconciled payouts

## Phase 2

- Role based access and dashboard for MFD, Admin and others.

## User flows

### Registration

- MFD need to Register and be activated with us to be eligible for a payout
- MFD need to provide there bank account and GSTN
    - Take it on UI , partner dashboard
    - Take it over Email
- We need to Verify Bank account and GSTN -
- For Bank account verification
    - Get the bank account data from partner Database
    - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account
    - We verify the bank account with Penny drop
    - We request to avoid joint accounts
- For GSTN verification
    - currently there is only char = 15 check , We need to verify GSTN from [gov.in](http://gov.in)
    - https://services.gst.gov.in/services/searchtp
    - For we have 140 GST partners , we can do verification manually and update in the sheet -Business team
    - IF GSTN  is not verified we trigger a E- Mail

Now we should have correct GSTN and bank account for the MFD partner 

### Payout

- Payout calculations
    - MFD will be eligible for the commercials agreed
    - GSTN registered MFD are eligible for GSTN invoice and payout
    - Payout >15,000 will incur TDS.
- Payout Invoice genration
    - Analytics team will generate correct payout and GST calculations
    - Analytics will verify Bank account and GSTN / receive verification
    - Analytics team will Create Invoices Payout and GSTN
    - Analytics team will Update the ledger with Invoices against them
    - Analytics team will help business team resolve any query customer raise

### Acknowledgment

- We would communicate the Payout with MFD partner over E-mail and Dashboard (phase-2)
- We will communicate
    - If we need the GSTN or Bank account
        - Template 1 for the registration
    - If we need confirmation on payout
        - Template 2 for Payout statement
        - Google form form for confirmation and issues collection
    - If we need confirmation on the GSTN
        - Template 3 that contains GSTN
        - Google form form for confirmation and issues collection

### Reconciliation

- The processed payout could have three states
    - Not processed
        - Bank account verification failed
        - GSTN verification failed
    - Payout confirmed and GST Tax invoice confirmed
        - Great!, update it in ledger
    - Payout confirmed but issues in GST Tax invoice
        - Read the issue in google sheets
        - Add the issue in google sheets if coming from other channels
        - Provide update and resolution or status in the sheet
        - IF payout changes are required then follow Issues handling of payouts
        - Communicate back over email with the MFD

### JTBD

- MFD
    - MFD need to register and activate
    - MFD needs to provide correct Bank account and GSTN details
- Analytics team
    - Create correct Payout and GST payout files
    - Check and flag incorrect / missing Bank accounts
    - Check and Flag incorrect /missing GSTN accounts
    - Consume /update / and store changes in Bank accounts and GSTN
- Business team
    - Trigger /confirm Emails and Payouts
    - Collect bank account Change requests in a File and provide to analytics
    - Collect GSTN update requests in a file and provide to analytics
    - Verify all new  GSTN  on gov portal and send status  to analytics.
    - Coordinate any issues mentioned by MFD partner
    - Email to MFD partners for missing and update bank account and GSTN, we can trigger the email to all MFDs
- Tech
    - Custom google form for the customer
- Issues handling of the Payouts
    - Collect issues
    - RCA issues
    - Solve issue
    - Calculate correct payout Balance
    - Update File for the changes and reasons
    - Get approval
    - Trigger corrected payouts with Balance invoices and same google form

Questions 

How do we ensure correct data when our tables are on a month level ? how important is this disc with puneet, and ops 

How do we create Invoice ?  -  List down what we want we want to do on a journey level / Zoho / tradeoffs buil d vs buy.

What should be the formant of invoice ? standard format 

what is considered a invoice confirmation ? 

- Establish google flow , 10 x volumes

what are legal terms we need to add to the invoice sign off ?

- talk to anant (jars) and Bharat

Do we want to send invoice on Email or create in dashboard as well?

In email can we get the issues through google form for now?

<aside>
💡

- Should we send different emails for payout and GSTN ?
- should we pay the GST for the current month of the till date? require data teams bandwidth.
- who will trigger invoice send
- 

</aside>

We can share on the Email , which we have to , and then develop the dashboard as well

https://forms.gle/GEe7LXUBC2izeNR58

How do we 

Invoice management 

- Create invoice
- Send invoice
- Confirm invoice
- store invoice
- update invoice
- Fetch invoice

Ref 

Storage costs and estimations - Not a significant cost 

[Cost estimates ](PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an/Cost%20estimates%2012ee8d3af13a80df856ded05b206dc19.md)

[Detailed JTBD](PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an/Detailed%20JTBD%2012ee8d3af13a80b3b5e7eb6a74c71b31.md)

Build vs Buy Decision pending , collect information on the Solutions in the market - Recommendation- Build as no solution provide Issue handling and we need to build the rest of infra anyways 

[Build vs Buy ](PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an/Build%20vs%20Buy%2012ee8d3af13a804abd37eb5e4fcd3acc.md)

Next Steps

- Connect with Puneet to understand Invoice creation in template
- Get confirmation on the GST invoice and Statement template.
- Highlight any blockers , send to development
- 

Admin actions will the tools for uploading the file for the data , take admin access reference

- Email Template confirmation
- GST invoice
- Statement Confirmation
- Admin actions UI and flow
- Sheet template

Development steps 

- Email template
    - Provide Bank account and GSTN
    - Payout only
    - Payout [GST](PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an/GST%20136e8d3af13a8043b670f3cc28d3b882.md)

Questions 

- What should happen if the customer does not send response? should we pay payout and not GST ?
- do we want to send out the Email for updating bank account and GSTN
- 
- 

[payout Email ](PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an/payout%20Email%20136e8d3af13a807b8c25ef55e07dae61.md)

Volt Admin pannel 

- Trigger Partner Payout
- approved names -with phone numbers
    - OTP
- upload confirmed table
    - Rename the table to last  month payout file  maintain proper naming convention
- Show Previously uploaded list
- Provide Email status and

Excel file template 

- Partner ID
- Partner Name
- GST applicable?
- Gst Invoice
- Payout invoice

On 1st of the month we send the Email to MFDs which Don’t have bank account 

We can also sent one time E-mail to collect the GSTN from MFDs 

We will verify the GSTNs off all the MFDs 

we will verify the Bank Accounts using Penny-drop

We will get the Payout calculation sheet by 5th By Puneet 

Business will verify the calculation and provide Approval 

The Approved list will be communicated through Email to MFD using Mail Moto by Labdhi

We will have two different Emails one for Payout Commission , one of Payout commission + GST Invoice. 

We will get the approval back on the Form Sheets and issues will be handled by Nitesh 

we will consider the Confirmed on the Commission statement by Default

We will not trigger a GST payout until Getting confirmation on the GST Invoice. 

we can consider the Google Form confirmation  as E-sign (confirming with CA)

[Invoice format_GST.xlsx](PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an/Invoice_format_GST.xlsx)

[https://app.notion.com](https://app.notion.com)

[https://docs.google.com/spreadsheets/d/1LTOr0jyY1pmB8h4RJCO-8IZNgCzoIkOB/edit?usp=sharing&ouid=104935226601455395779&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1LTOr0jyY1pmB8h4RJCO-8IZNgCzoIkOB/edit?usp=sharing&ouid=104935226601455395779&rtpof=true&sd=true)