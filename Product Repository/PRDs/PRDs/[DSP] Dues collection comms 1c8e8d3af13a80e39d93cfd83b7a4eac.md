# [DSP] Dues collection comms

: Ameya Aglawe
Created time: April 1, 2025 3:29 PM
Status: Done
Last edited: August 22, 2025 3:28 PM

# **What problem are we solving?**

- Currently DSP is not sending collection related communications to the user -
    - ***Poor customer experience :*** This leads to user being unaware of the due dates, leading to them missing the payments, incurring bounce/penal charges
    - ***Business risk :*** This puts DSP finance (as an NBFC) at an compliance risk, as it is mandatory for NBFCs to send collections related communications to the user as per RBI regulations

---

# **How do we measure success?**

- Decrease in % mandate failures due to insufficient balance
- Decrease in % of loan accounts with over dues
- Reduction in % of portfolio sell-offs due to non repayment of dues
- Reduction in # of customer queries to DSP Finance support team & sourcing channels’ support team

---

# **How are others solving this problem?**

---

- TCL comms on mandate (Only SMS comms, no emails)
- Groww’s SIP reminders
- AMCs’ comms on successful SIP transactions

![image.png](%5BDSP%5D%20Dues%20collection%20comms/image.png)

![Screenshot 2025-04-08 at 4.07.00 PM.png](%5BDSP%5D%20Dues%20collection%20comms/Screenshot_2025-04-08_at_4.07.00_PM.png)

![Screenshot 2025-04-08 at 4.07.40 PM.png](%5BDSP%5D%20Dues%20collection%20comms/Screenshot_2025-04-08_at_4.07.40_PM.png)

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

- The flow for dues collection comms will be of 2 types -
    - Sync : Comms will get automatically triggered due to occurrence of an event
    - Bulk : Comms will go through maker-checker, where DSP Ops will review and approve the comms file, once they tap on “Approve” only then the comms will get triggered to the customers.
- Auto-debit reminder & auto debit failed comms will be triggered in sync
    - **Sync**
        - The auto-debit reminder comms will be triggered when the DSP Ops approves the mandate presentation file on due date - 1
        - The auto-debit failed comms will be triggered as we get the status of auto-debit collection
    - **Bulk**
        - The due reminder comms on 1st, 4th & 7th
        - The overdue comms will be triggered on 8th & a 3 day interval from 8th
        - DSP Ops will check the respective task and approve
            - *Due reminder*
                - On 1st
                    - Trigger time : 8 AM
                    - Task type : Holding & account statements with due notification
                    - Report fields
                        
                        
                        | fenixLoanAccountId | clientId | customerName | supportEmail | supportNumber | loanStatus | interest_and_charges_due | due_date | drawingPower | availableLimit | sanctionedLimit | soaFileName | soaFile | holdingStatementFileName | holdingFile |
                        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
                - On 4th & 7th
                    - Trigger time : 8 AM
                    - Task type : Due reminder
                    - Report fields
                        
                        
                        | fenixLoanAccountId | clientId | customerName | supportEmail | supportNumber | loanStatus | due_amount | due_date | interest_due | charges_due | overdue | sourcing_channel |
                        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
            - *Overdue reminder*
                - Trigger time : Every week once from 8 & coming at 8 AM
                - Task type : Overdue reminder
                - Report fields
                    
                    
                    | fenixLoanAccountId | clientId | customerName | supportEmail | supportNumber | loanStatus | overdue | due_date | interest_overdue | charges_overdue | sourcing_channel |
                    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
            - *Dues received*
                - Trigger time : Every week once from 8 & coming at 8 AM
                - Task type : Interest received comms
                - Report fields
                    
                    
                    | fenixLoanAccountId | clientId | customerName | supportEmail | supportNumber | loanStatus | due_amount | due_date | interest_due | charges_due | overdue |
                    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        - Once approved, the comms will be sent to the users

## Requirements

---

**Email communications -** 

- We will send collections related email notifications to the both mandate registered & not registered DSP Finance customers. Please find the detailed comms PRD with respective templates of each of the above scenarios [here](https://docs.google.com/document/d/1g5knedV_KqNbe5KEiv06adhD2k6MVf21cYC1HlximMY/edit?usp=sharing). Following is the comms plan with triggers -
    
    
    | Phase | Mandate registration status  | Purpose | Trigger | Comms type | Occurrence |
    | --- | --- | --- | --- | --- | --- |
    | Phase 1 | Status agnostic | Dues notification  | 1st of every month : when the DSP Ops approve the statements comms checker task  | Bulk  | One time/month |
    | Phase 1 | Registered  | Auto debited reminder | Due date - 1 : when DSP Ops approves the mandate presentation file  | Sync | One time |
    | Phase 1 | Registered  | Mandate attempt failed | Due date : when we get mandate status from Digio APIs | Sync  | One time |
    | Phase 1 | Not registered | Dues payment reminder  | Due date - 3 & Due date : when the DSP Ops approve the dues reminder comms checker task  | Bulk  | One time |
    | Phase 1 | Status agnostic  | Dues received  | Due date  | Bulk  | One time |
    | Phase 1  | Status agnostic | Dues overdue  | Due date + 1 : when the DSP Ops approve the overdue reminder comms checker task  | Bulk  | Multiple times |
    | Phase 2  | Status agnostic | Portfolio sell-off  | Date of invocation initiation | Sync  | One time |
- Overdues
    - Overdue calculation methodology:
        - overdue = interest_due + overdue (previous) + charges_due
    - Communication cadence for overdue accounts:
        - Overdue payment notifications will be triggered automatically every 3 days
        - First notification sent on day after due date (Due date + 1)
        - Subsequent reminders on 3-day intervals (e.g., 8th, 11th, 14th day after original due date)
            - We will send create the comms jobs one day prior if the scheduled date lies outside the business hour
    - Overdue communication cycle continues until payment is received or 20th of the due month
- Two different holding & account statement for 1st of every month
    - No Dues → Template ID :  d-ff2455b081fa4f7384fccdd207a7d40b
    - Dues present → Template ID : d-ea740018f0ad44be8d0b4cf35d96346f
- Update in the holdings & statements format for showing dues
    - Current
        
        ![Screenshot 2025-04-01 at 5.57.49 PM.png](%5BDSP%5D%20Dues%20collection%20comms/Screenshot_2025-04-01_at_5.57.49_PM.png)
        
    - New
        - Here we will change the date range of interest due in case of an overdue.
            - Lets say there is an overdue interest of Dec, then in the account & holding statement of Feb 1 we will keep the date range of interest due as “Due from 01 December to 31 January”
- Comms ****
    - To be sent for all the LSPs (Groww, INDMoney, Yenmo)- **Aligned with Keyur**
    - Please note that the name of the sourcing channels stored in the DB will changed a little to send in comms
        
        
        | Name of sourcing channel in DB | Name of sourcing channel to be sent in comms |
        | --- | --- |
        | VOLT_MONEY | Volt Money |
        | GROWW | Groww Credit  |
        | INDMONEY | INDMoney |
- Web-hooks
    - LSPs → Groww, INDMoney, Yenmo
    - Trigger → Calling of Sendgrid APIs
    - Fields → Variables set for the Sendgrid templates
- We will not be showing sell off dates in any communications - Aligned with Nishant
- Overdue API curl (use Finflux loan account number in the end point)
    
    ```jsx
    curl --location 'https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/revolving-credit-lines/000004196/bill-overdues' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer eClwBKK6ukwBhuO4aYU9fShfc6M'
    ```
    

**SMS communications -** 

- Flow
    - SMS communications will follow the same workflow as email communications for dues collection, including frequency, triggers, and approval process.
- API integration
    - SMS vendor : Gupshup
    - API details
        - Auth
            - userid : 2000247728
                - password : YGxXWvnW
        - POST
            - Request
                
                ```jsx
                {
                  "userid": "20000XXXXX",
                  "password": "XXXXXX",
                  "send_to": "919XXXXXXXXX",
                  "msg": "Dear Abc, This is testing",
                  "method": "sendMessage",
                  "msg_type": "text",
                  "format": "json",
                  "auth_scheme": "plain",
                  "v": 1.1
                }
                ```
                
            - Response
                
                ```jsx
                
                ```
                
        - GET
            - Request
                
                ```jsx
                curl --request GET \
                     --url http://enterprise.smsgupshup.com/GatewayAPI/rest
                ```
                
            - Response
    - Status handling
        - Web-hooks
            - Following are the fields that would populate in the web hook body
                - externalId - Unique ID for each message.
                - deliveredTS - Time of delivery of message as LONG number.
                - status - Final status of the message, possible values are SUCCESS, FAILURE or UNKNOWN.
                - phoneNo - Phone number of the receiver.
                - cause - This is the response you will get depending on the status. Various statuses and their explanation are below.
                - Errorcode – Error code assigned to a different failure cause.
                    
                    
                    | **Error Code** | **Error Name** | **Description** |
                    | --- | --- | --- |
                    | 1 | ABSENT_SUBSCRIBER | When the service provider fails to reach the member/subscriber, thisvalue is passed. |
                    | 2 | CALL_BARRED | Subscribers have some kind of call barring activity on the number due to which messages from unknown sources are blocked. |
                    | 3 | UNKNOWN_SUBSCRIBER | Unknown/invalid number. |
                    | 4 | SERVICE_DOWN | Operator service is temporarily down. |
                    | 5 | SYSTEM_FAILURE | Failure due to a problem in the Operator’s systems (Originating orDestination Operator). |
                    | 6 | DND_FAIL | The number is either in DND or Blocked due to being in DND or a complaint. |
                    | 7 | BLOCKED |  |
                    | 8 | DND_TIMEOUT | The latest DND status is not available in time for the message to be sent. (Max 1 day). |
                    | 9 | OUTSIDE_WORKING_HOURS | Message sending is outside mentioned working hours. |
                    | 00a, 14, 15, 16, 17, 18, 19, 01a, 01b, 01c, 20, 24 | OTHER | Messages that are sent but can not be delivered for reasons that don’t fall under any mentioned category. |
                    | 00b | BLOCKED_MASK | Mask is blocked by SMS GupShup. |
                    | 00c | SMSCTIMEDOUT |  |
                    | 00d | CANCEL_CAUSEID |  |
                    | 00e | CANCEL_SCHEDULE |  |
                    | 10 | DEFERRED |  |
                    | 11 | INBOXFULL |  |
                    | 12 | CONGESTION |  |
                    | 13 | NO_ACK_FROM_OPERATOR |  |
                    | 22 | BLOCKED_FOR_USER |  |
                    | 23 | UNKNOWN_SUBSCRIBER |  |
                    | 038 | MSG_DOES_NOT_MATCH_TEMPLATE | The template passed in the message content does not match with dltTemplateId uploaded offline in the system. |
                - No of frags – one message (fragment) is of 160 characters. Number of charactert states the total count offragments.
                - Mask – Sender ID sent with the sms.
    - DSP SMS copy : Please refer to [this](https://docs.google.com/document/d/1pA-wZuRMg_2gg0DvlnK20c8Hr5dA7NYtR4uQ3MyTVZs/edit?usp=sharing) document for templates and template ID
        
        
        | **Time**  | Event | Type | Optimised Copy  | Copy |
        | --- | --- | --- | --- | --- |
        | 2nd  | Payment reminder | Bulk | Rs. {due_amount} for your loan account {lan} due on {due_date}. Pay via {sourcing_channel} by {due_date} to avoid dishonor and penal charges - DSPFIN | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid dishonor and penal charges or repay early via the {sourcing_channel} - DSPFIN |
        | 4th  | Payment reminder | Bulk  | Rs. {due_amount} for your loan account {lan} due on {due_date}. Pay via {sourcing_channel} by {due_date} to avoid dishonor and penal charges - DSPFIN | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid dishonor and penal charges or repay early via the {sourcing_channel} - DSPFIN |
        | 6th  | Auto-debit notification | Sync | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid dishonor and penal charges - DSPFIN | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid dishonor and penal charges - DSPFIN |
        | 7th  | Mandate Success | Sync | Dues of ₹{due_amount} have been successfully collected for your loan account {lan} on {due_date} - DSPFIN | Dues of ₹{due_amount} have been successfully collected for your loan account {lan} on {due_date} - DSPFIN |
        | 7th  | Mandate Failed | Sync | Auto-debit attempt on your loan account {lan} failed on {due_date}. Repay ₹{due_amount} via {sourcing_channel} to avoid dishonor and penal charges - DSPFIN | Auto-debit attempt on your loan account {lan} failed on {due_date}. Repay ₹{due_amount} via {sourcing_channel} to avoid dishonor and penal charges - DSPFIN |
        | 8th/11th/14th/17th | Overdue | Bulk  | Rs. {due_amount} OVERDUE on your loan account {lan}. Pay via {sourcing_channel} app before the 20th to avoid collateral sell-off. Dishonor and penal charges applicable. - DSPFIN | Rs. {due_amount} OVERDUE on your loan account {lan}. Pay via {sourcing_channel} app before the 20th to avoid collateral sell-off. Dishonor and penal charges applicable. - DSPFIN |
        | 19th | Auto-debit notification | Sync | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid collateral sell-off - DSPFIN | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid collateral sell-off - DSPFIN |
        | 21st  | Collateral sell-off  | Sync | Collateral sell-off of {sell_off_units} units for ISIN {isin} has been initiated for your loan account {lan} - DSPFIN | Collateral sell-off of {sell_off_units} units for ISIN {isin} has been initiated for your loan account {lan} - DSPFIN |
    - **Note : The SMS should be triggered strictly between 9:00 AM and 9:00 PM (as outside these timings gupshup does not allowed to send SMS)**
        
        ![Screenshot 2025-08-20 at 4.12.36 PM.png](%5BDSP%5D%20Dues%20collection%20comms/Screenshot_2025-08-20_at_4.12.36_PM.png)
        

# **Design**

---

# **Analytics**

---

- Number of comms sent of each comm type (send by NBFC)
    - Number of comms delivered (This will be tracked on sendgrid)
    - Open rate of comms (This will be tracked on sendgrid)

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes

1. Problem for DSP Ops 
2. Takes 9 hours to generate all reports 
3. Summary API bulk → Gives outstanding dues 
4. Statements are currently password protected
    1. Link can be password protected
    2. Can directly be downloaded but the documented will be password protected 
5. Expiry time can be set up for s3 links 

- Can make the same comms for both dues & non-dues for 1st of the month reminder
- Bank name cannot be shown  - Taking from LSPs during bank verification, is there an approved list? - Bank verification records - Unique banks
- Stack rank of the phase 1 comms
- Platform team will have to pick up changes in the holding statement/might not be possible - Already in place
- LSP level files should be sent based on comms type instead of web-hooks
- Not required —
    - To check the overdue API - Done
    - Can we give nudge to the user to register mandate while giving them payment reminders - Check with Vaibhav/Nishant
- **Confirm with Vaibhav if we should send the overdue comms daily**

- 13 June - Change in comms schedule as currently we cannot differentiate between mandate registered and non mandate registered users
    - 1st & 4th - Payment reminders
    - 6th - Auto debit notification
    - 7th - Failed & Success status of dues
    - 8th - overdue comms with business hours check until initiation of next business cycle or clearing of dues
- Volt SMS copy
    
    
    | Event  | Copy  |
    | --- | --- |
    | 1st MR | {due_interest_month} month statement generated Amt due: Rs. {due_amount} Auto-debit date: {due_date} from XXXX{account_last4digits} Maintain sufficient balance to avoid bounce charges - VOLT |
    | 1st MNR | {due_interest_month} month statement generated Amt due: Rs.{due_amount} Due date: {due_date} Pay now or before the due date to avoid penal charges - VOLT |
    | 6th MR | {due_interest_month} Month Interest Due Reminder Amount Due: Rs. {due_amount} Auto-debit Date: TOMORROW from XXXX{account_last4digits} Maintain sufficient balance to avoid bounce charges - VOLT |
    | 6th MNR | {due_interest_month} Month Interest Due Reminder Due Amount: Rs.{due_amount} Due Date: TOMORROW Pay now to avoid penal charges. - VOLT |
    | 7th MR | {due_interest_month} Month Interest Due Reminder Amount Due: Rs. {due_amount} Auto-debit Date: TOMORROW from XXXX{account_last4digits} Maintain sufficient balance to avoid bounce charges - VOLT |
    | 7th MNR | {due_interest_month} Month Interest Due Reminder Due Amount: Rs.{due_amount} Due Date: TOMORROW Pay now to avoid penal charges. - VOLT |
    | Overdue | {due_interest_month} Month Interest Overdue Reminder Payment of Rs. {due_amount} is OVERDUE Make payment before {lender_sell_off_date} to avoid security sell-off - VOLT |
- SMS copy
    - Payment reminders
        
        ```jsx
        {due_interest_month} month statement generated Amt due: Rs. {due_amount} Auto-debit date: {due_date} from XXXX{account_last4digits} Maintain sufficient balance to avoid dishonor charges or repay early via the {{sourcing_channel}} app - DSPFIN
        ```
        
    - Auto-debit notification
        
        ```jsx
        {due_interest_month} month statement generated Amt due: Rs. {due_amount} Auto-debit date: {due_date} from XXXX{account_last4digits} Maintain sufficient balance to avoid dishonor charges or repay early via the {{sourcing_channel}} app - DSPFIN
        ```
        
    - Auto-debit status
        - Success
            
            ```jsx
            Dear Customer, your loan account dues of ₹{{due_amount}} have been successfully collected
            ```
            
        - Failed
    - Overdue
        
        ```jsx
        {due_interest_month} Month Interest Overdue Reminder Payment of Rs. {due_amount} is OVERDUE Make payment before {lender_sell_off_date} to avoid security sell-off - DSPFIN
        ```
        
    - Sell-off