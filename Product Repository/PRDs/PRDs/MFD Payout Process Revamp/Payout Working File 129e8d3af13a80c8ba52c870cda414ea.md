# Payout Working File

Errors earliar

- We Currently don’t provide visibilty to MFD partner on there accrued balance( AP account data) to the MFD causing confusion between Payable and actual transaction. This is Due the way we have report format is configured
- We are taking ad hoc payout request without proper recon process , this causes issues downstream. This is due to lack of visibility internally
- We receive GST issues as Customer  raise   wrong invoices, This is because we don’t provide GST tax invoice to the partners
- We get calls to get the visibility on the Payouts status and Ledger, as we don’t share the data before actual payout. as engineering  uploads the data once a month
- We have recon issues and Payout delays due to Commercial file changing and analytics need to debug the issues the commercial changes. This was just 10 applications in September - need to review previous months’ data.
- We are unable to keep a upto date transactions table due to poor server infra at the lenders end. our transaction table is a month out of date
- We need to streamline GST and TDS filing
- We Don’t have a way to handle MFD ‘s without added bank account . ~~accrue payouts to a MFD~~

list , journey , use case 

## Meeting notes

- customer - cashback-
    - previously
- partner
- platform

customer cashback 

Base rate - 10.49% , volt base rate - 9.95, —>9.99—> 10.49

march 2022. —>23—>24 

<may 1st 9.99

9.99 -ROI  base rate - 10.49%. 0.5 % cashback 

on may 1 we changed the base rate for the customer to 10.49% 

cusotmer cashback , 

partner to partner Selfline 

partner payout - MFD 

- Volt empaneeled MFD  - MFD direct
- through Software, redvisison or invest well, assest plus , zfunds , - MFD software
- affiliates, - Ytbers ,

- Partner payout
    - apps like phonepe , jupiter, niyo, part+
    - 

Money is calculated on the Principal outstanding , monthly average 

daily average, payout is calculated 

customer wise average POS, eod, for debit-credit 

sharing percentage with partners - 

1. customer —> loan —> 
    1. credit to borrower 
    2. Credit to partner 
    3. Credit to platform 
2. partner - volt- 
3. upfront - one time payment,  rs 200 for opening a account 
4. trail income - 0.5 % into POS
5. category —> upfront and trainl 
6. frequency one-time, monthly , reason for payment 

- there is a a default rate
- dynamic  trail (agreement rate -volt base rate)*70%
- dynamic one time (aggreement PF - Volt base rate )*50%
- partner negotiations → we need to 90% , partner negotiate ,
- sheet  is maintained , where RM is negotiated list to puneet’s sheet ,
- sharing percentage  of negotiation in trail and upfront dynamic commintion

- Marketing - Diwali, etc offers , take rs 6000 offer is made 3 cusotmer etc .
- negotiation -credit partner , - negotions on this base rate of o.5% and rs 200 base
- commercial deals

Calculations {

Platforms 

- commercial bases
- they have logic of changing everything

- UI with all the parameter
- with bharat pe , - commercial is on sanctioned amount
    - take cusotmer sanction amount and POS, (SLAB)
    - there are slabs of eg 2 cr

special rules 

- if all the POS combined for all cusotmers then >10cr then the rate will be 0.55 step up

redvision - platfrom , 

- MFD gets 0.5 and rs 200
- commercial is 50 Cr give 0.1 , 50-60cr give 0.2 %

}

Calculation 

- transaction level data
- Live transaction data is not available
- a email send to tech for the updation of the transaction table ,

eg naman has done 10 transaction today then we don’t store the data , because we are not able to store the data in miles 

- miles is slow to send us data
- recon takes time , with bugs and fixes
- transsaction table to know POS

Deviations on the 4-5 cases on the Commercail 

transaction 

TDS - Rs 14,250> payout , then we deduct 5 % of the payout amounts

GST - APR- jun- July , 
GST valid , 18% extra send 

partner account table , we have GST , check is on 15 digit number 

we have  GST for 140 customer out of 2500

there could be partner without GST raising invoice  we have no way to check 

there could be MFD with invalid or wrong GST number getting paid 18% 

- execution -
    - Partner account , bank account , HSBC,
    - we don’t very bank account in the system we run offline penny drop. to check the bank account ,
    - we sent the money to the verified bank account ,
    - HSBC need 48 hr to get back on the status ,
    - We can get success full through HSBC API , instantly instead
- Partner 1 , settlemeted, [artner 2 non settleed
- Marketing message -  to MFD , with Payout mtds, gst ,
- MFD wants ledger of from which cusotmer they made money
- we send this ledge for evrry cusotmer MFD and send to dashbaord

- transaction issues
    - Miles performance
    - Data sanity issues
    - credits table - Live POS table
    - transaction table
    - 

- Calculate delay , payout dealy , transaction table delay , later on transaction table delay
- payout have completed , partner wants to see the details of how it is calcuated
- where to raise TDS and GST invoices
- details are missing in ledger, for GST and we hide the ledge formMFD employees
- empanelled
- if MFD has not taken payout by not adding bank then how do manage it
- biggest problem , - bank account number change handling
- GSTN check  API for tax validation
- who has empanelled GSTN belong this MFD or not
- 

- MFD commercials update (Slab wise payout) currently we do not process it
- If MFD has not updated bank account, the old payouts are not released unless highlighted by MFD or volt internal team
- GST is a pain point where MFD shares teh invoice basis the payout Volt makes and then volt manually verifies the gst details which is very much prone to error.
- Quaterly or yearly ledger for MFDs
- how do we create Quarterly ledger , Payout dashboard  a google file .
- RCA of previous payouts ,
- GST number - option on partner payouts
- do we check the bank acocunt belong to the MFD
- Payout , wrong calcualtion ,
- low visibility
- communication amount was wrong
- negotion request on base rates

- GST filing was wrong  why ??
- why we don’t get the UTR together with ledger
- 
- 
- 

| Step | Stakeholder | Data Source | Timeline | Current Challenges |
| --- | --- | --- | --- | --- |
| Capture MFD Commercials | Finops, MFD | Excel Sheets, Emails | Ongoing | - Commercials are scattered across excel sheets and emails<br>- Difficult to track and update dynamic rates, slabs, and special arrangements<br>- No differentiation between MFD types in current process |
| Capture Application Details | Finops | LOS (Loan Origination System), Excel Sheets | Ongoing | - Commercial deviations stored in excel sheets, not linked to LOS<br>- POS data not fetched daily, leading to payout errors |
| Perform Payout Calculations | Finops | Excel Sheets, Disparate SQL Queries | 1st-2nd | - Payout calculations done manually in excel<br>- Complex slab-based payouts prone to errors<br>- Calculations based on outdated POS data from previous month |
| Review Payouts | Finops | Excel Sheets | 3rd-4th | - No user-friendly interface for reviewing and approving payouts<br>- Manual comparisons and verifications time-consuming |
| Generate Invoice | Finops | Excel Sheets, Word Documents | 5th | - Invoices manually generated and shared with partners<br>- No itemized breakdown of payouts in invoices |
| Confirm Invoice | MFD | Emails | 6th-8th | - Invoice confirmation done over emails, difficult to track<br>- No reminders or notifications for pending confirmations |
| Raise Discrepancies | MFD | Emails, Phone Calls | 9th-10th | - Discrepancies raised over emails and calls, hard to keep track<br>- No centralized system to log and monitor discrepancies |
| Resolve Discrepancies | Finops | Emails, Excel Sheets | 11th-12th | - Discrepancy resolution done over emails, no SLAs maintained<br>- Resolutions not properly communicated to partners |
| Process Payouts | Finops | Bank Portal, Excel Sheets | 13th-14th | - Payout file generated manually and uploaded to bank portal<br>- No penny drop validation before processing payouts<br>- Payouts not put on hold if bank details are missing<br>- Same bank account used for payout and ops |
| File TDS and GST | Finops | Excel Sheets | 13th-17th | - TDS and GST calculations done manually based on payout data<br>- No automated integration with government filing systems |
| View Earnings and Deductions | MFD | Emails, Excel Sheets | 15th | - No self-serve earnings dashboard for partners<br>- Partners have to rely on emailed excel sheets for earnings data<br>- TDS, GST deductions not clearly displayed |
| Settle Unprocessed Payouts | Finops | Excel Sheets, Emails | 16th-18th | - No auto-retry mechanism for bounced payouts<br>- Partners not notified proactively to update bank details for pending payouts |
| Handle Queries and Disputes | Finops, MFD | Emails, Phone Calls | Ongoing | - Query resolution done over emails and calls, no SLAs maintained<br>- Partners not given timely updates on resolution status |

1. Reliance on manual data entry and excel sheets for storing critical data
2. Lack of integration between systems leading to data discrepancies and delays
3. Manual payout calculations prone to errors, especially for complex slab-based payouts
4. Absence of user-friendly interfaces for key tasks like payout review and discrepancy management
5. Communication gaps and lack of structured workflows for invoice confirmation and query resolution
6. Missing validation checks and segregation of duties in payout processing
7. Manual tax calculations and lack of integration with government filing systems
8. Poor visibility for partners on their earnings, deductions, and payout status
9. Inefficient handling of bounced payouts and missing bank details
10. No defined SLAs for query resolution and partner communication

Addressing these challenges would require a combination of system integrations, process automations, and workflow enhancements across the payout value chain.

- payed on two level
    - One time payment  - Part of processing fees (PF)
    - Trail payments - montly accrued (% over Principle outstanding(POS))
    
    - Offer payments
- how will customer confirm gst,
- Checker maker process
- JARS payout software , Payout confirmation
- 

GSt issues 

- volt payout
- net payout

Bharat lamba -  notes 

- Payouts
    - individual partners 2500
    - 90% of does not have GST
    - 10 % of them have GST

there income is dependent  on the upfront trail , offer payment 

TDS payment , and then we GST, unless we receive a Invoice from them

No problems are in Calculation by 4-5 th 

We then send Manually we send comms not a issues ATM 

We don’t have tracking or check for the GST 

1. we want to MFD to get the GST invoice received signed by then, First our CA has to sign off on the GST invoice then we payout 
2. We have dashboard in excel to track the payouts 
3. Comms could be automations from operational to automation 
4. automated Payouts
5. we want send a statement
6. we need to might the excel readability 
7. 

- partners, isseus
- - payout GST,
- Transparency
- Sales - tools LSQ, Zendesk , too many channels, need something onmi channels

For 10x

- Servicing ,
- bank account updated after 1 month after subsequent month of calculation
- Joint account , HSBC , - Bank account name , settle , fail 4-5 month