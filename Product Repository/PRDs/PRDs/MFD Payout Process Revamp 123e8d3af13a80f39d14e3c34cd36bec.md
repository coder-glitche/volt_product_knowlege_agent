# MFD Payout Process Revamp

: Gautam Mahesh
Created time: October 18, 2024 5:52 PM
Status: In progress
Last edited: March 7, 2025 1:51 PM
Owner: Naman Agarwal

# **What problem are we solving?**

[**VOLT MFD Payout Process Overview**](MFD%20Payout%20Process%20Revamp/VOLT%20MFD%20Payout%20Process%20Overview%20129e8d3af13a80f0a322dd388f71d70c.md)

[Payout Working File](MFD%20Payout%20Process%20Revamp/Payout%20Working%20File%20129e8d3af13a80c8ba52c870cda414ea.md)

[PRD - GST Invoice and Payout statement creation and approval ](MFD%20Payout%20Process%20Revamp/PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an%2012ee8d3af13a80189662fc13cfe7d2a1.md) 

[Process note Payouts ](MFD%20Payout%20Process%20Revamp/Process%20note%20Payouts%2013be8d3af13a80d58fbaf763902d7ca0.md)

[Payouts Phase 2 ](MFD%20Payout%20Process%20Revamp/Payouts%20Phase%202%20149e8d3af13a80bdb2f2cf6c1b703c32.md)

[Bulk Email Sender Setup Guide](MFD%20Payout%20Process%20Revamp/Bulk%20Email%20Sender%20Setup%20Guide%2014ae8d3af13a8091889eccaec480fbee.md)

[Volt MFD Payout & GST Invoice Process](MFD%20Payout%20Process%20Revamp/Volt%20MFD%20Payout%20&%20GST%20Invoice%20Process%2014be8d3af13a808e9ef3f61a1a7659dc.md)

[MFD Accounts Payable ](MFD%20Payout%20Process%20Revamp/MFD%20Accounts%20Payable%2017de8d3af13a801392a7ee2993b23be8.md)

[Notes <>Bharat](MFD%20Payout%20Process%20Revamp/Notes%20Bharat%20185e8d3af13a802292e6e8f1e6878432.md)

## Major issues Identified

- We Don’t send GST invoices to MFDs this leads to ad-hoc payments, accounting issues , and incorrect payouts and fillings leading to MFD complains from the top MFDs
- Current Payout Reports to MFDs are not easy to read by majority of the MFD. This lead to customer calls to understand the Payouts.
- We track Partner Accounts payable on a monthly table level we don’t calculate on a global basis this leads to Customer with new bank accounts to not have a payout from previous months as we don’t run a all time query.
- Currently we don’t process payouts on a partner accounts payable level, making the calculations for GST and TDS tough, and at glance state of the partner accounts payable we have to run a query
- There is accounting issues for ~2% of the partners due to accounting issues. partner comes to know about then during 26AS filing
- We don’t have a overall visibility on support provided to MFD partner for payouts , L1, L2, L3 issues and there status.
- We have a recon issues due to current Commercials excel file
- Older Ad hoc payouts are harder to track-down, and are on multiple files and emails
- Current process to check Correct GSTN is =15char , need to check gov website

| Feature  | Current  | Proposed |
| --- | --- | --- |
| Application data  | DB | No change |
| Transaction data | DB | No change |
| Principle Outstanding | google sheets  | DB |
| Partner Commercials  | google sheets  | DB |
| Payout ledger table  | google sheets  | DB |
| Account Payable (AP) | - | DB |
| Base Payout calculations  | google sheets  | DB |
| GST calculations | google sheets  | DB |
| TDS calculations  | google sheets  | DB |
| Payout Invoice | google sheets  | DB |
| GST Invoice | - | DB |
| GST Tax Filling  | google sheets  | DB |
| TDS filling  | google sheets  | DB |
| Bank account data | Check  | DB |
| Payout File to Bank | Excel | API |
| Payout payment status data | statement  | API |
| Reconciliation and UTR backfill | google sheets  | DB |

### MFD/Partner

- MFDs expect to get paid on time, (not a issue, MFD get paid on 10th)
    - Issues arise when bank accounts are not updated
    - we calculate the payouts from the date of new bank account addition. This causes issues in arrears
- MFD expects to get paid  accurately , as per the agreed upon commercials.
    - Sometimes ~2%, marketing offer payout are missed. these get highlighted when tax filling
    - Mismatch between 26AS and actual payment made to MFD , likely internal accounting errors
- MFD want to know the breakup of the Payout and GST TAX invoices that are easy to read
    - For Tax Filling purposed MFD want invoices
        - We currently don’t provide GST invoice , 110 MFDs
        - MFD routinely raise GST on NET amount instead of correct Gross amount. Invoice problems are limited to the GST MFDS
- MFD wants to highlight any discrepancies and get them resolved quickly.
    - We don’t have a tracking of the issues raised on a aggregate level
    - RM don’t have understanding of the GST calculation and hence cant help MFDs
    - ~minor issues are solved with a day, major issues take weeks as we need to connect with CAs to resolve the issue
- MFD want Volt to take care of the Tax filling etc accurately.
    - only issues are calculations errors
- MFD want to have a similar payout process as best AMCs they have worked with in there experience.

### Business team

- Business team want to provide great service to the MFDs and want to solve there Payout problems.
    - MFD faces Payment-Related Issues (based on daily [escalations](https://docs.google.com/spreadsheets/d/1FF-0Zuu5uP0xHgk3sarZbZocrtQFkwHyfip7FQbp2eY/edit?usp=sharing) )
        - Payout delays or non-receipt / Credited  - unavailability of BA, and Older payment don’t get processed
        - GST payment and invoice concerns -  payment amount issues, MFD has to raise invoice offline
        - Cash back (0.5%) not received - For old customers, accounting  error RCA needed
        - Processing fee refunds:- Self line - Case is from different number, for family
- Business team wants accurate payouts to the MFDs and to provide them with accurate Invoices for Payout and GST.
    - Currently we don’t generate GST invoices for MFDs. We need to CA approved invoices to GST MFDs
    - Non GST MFD have mentioned the Lack of readability of report we provide maybe moving to the AP Statements.
    - We need Sign off from Partner on the Invoices
    - Our TDS and GST calculation is not 100% correct - accounting issues
        - total payout 14,250 starts TDS , MFD understanding issues
        
        |  | TDS | Payout  |
        | --- | --- | --- |
        | 5000 | 0 | 5000 |
        | 5000 | 0 | 5000 |
        | 5000 | 750 | 4250 |
- Accounting issues
    - Upfront payments not received 02e8186d-a814-4eae-bd34-0a4b70d341b6

![image (4).png](MFD%20Payout%20Process%20Revamp/image_(4).png)

- Business team want to have overview to see a partners payout detailed status and history of payouts , Issues tracking and resolutions to resolve MFD tickets effectively.
    - Business team  currently handle and approve Payouts on Ad-hoc requests from MFDs
        - We currently do not have any way to track Ad hoc transactions,
        - OLD transactions Email , sheets  etc . not reconned.
    - We track Payout basis bank account and HSBC confirmation
        - It takes 48 Hrs to get statement from HSBC. we send communication to MFD whose transactions have failed as we don’t get to know beforehand
    - Tracking payouts is a manual process
- Business team want status summary of the all payouts and where are they struck and have issues.
    - Manual check of the issues

### Accounting team

- Accounting want to have a consistent and accurate ledger with Invoices against every transaction
    - We don’t have a Ledger with transactions with invoices, We don’t have a way to generate invoices on demand
- Accounting team want to track the reason of each payment in detail
- Accounting team want to regularise and close all the payments
- Accounting Team want to have a MFD based accounts payable
- 

### Payment ops

- Payment ops want to have accurate bank accounts of the customers
    - no problem sending file to HSBC

### Analytics team

- Need a accurate source data tables at the time of start of the month process
- Need time-source data on the commercials for accurate reconciliation
- Need to know Offline payouts against partners to Recon
- There are Old transactions we no source to Recon
- Need to have updated formats for the Invoices to send
- Have to create monthly files ,
- partner payout —> status —>success—>marketing message—>if you want to get GST then fill the google form—> MFD fills form
- Now contains few issues in the process
    - MFD fills previous months GST invoices in the current month.
    - MFD has correct GSTIN number, analytics has no method to verify this
    - Reporting the paid GST to Jars (CA firm) is tough to maintain (as no exact detail of month wise payout)
    - Their 20% of the partner who raises incorrect GST,
        - Ideally GST should be calculated on Payout Amount.
        - We pay MFD Amount which is (Payout Amount - TDS),
    
    Example: 
    
    **GST Issues**
    
    1. Month 1, MFD received payout of 5000 for month `Aug 2024`, and eligible for GST 900,
    2. Now we send messaging to fill the google form to claim GST.
    3. He fills the google form, and fills also add GST for previous months (Feb, Mar, Apr)
    4. Here, we are unable to classifiy which is the exact GST amount for the Aug 2024.
    5. Messaging is unclear to partner about which amount to raise GST on (Payout Amount or TDS Accounted Amount).
    6. Once they raise this amount its difficult to cross the exact gst amount to be paid
    7. Once the Incorrect Gst has been Paid to the government , then it irresible and partner have tax issues 
    8. Once GST is paid, mapping & storing in your database is tough to handle.

---

**HSBC Transaction Status:** 

1. transaction recon- manual process 48 
2. Recon process for old transactions 

**Partner customer attribution**

- Customer which does MFC fetch from partner link but created account directly
- Analytics map their partner - customer but changing in `PROD` database every month
- As this is a critical process this should be handled in a Ad-hoc manner.

**Consolidated place to enter Commercials/ Rate change** https://docs.google.com/spreadsheets/d/1z4sn7BSduzEEt6HAIpZXTJWbd3S2Sfh2_cgn6NcxW3s/edit?usp=sharing

**Bank Account Verification** 

1. Currently Analytics store and does penny drop for new bank / updated bank accounts and store in Google Sheets
    1. Total partner bank accounts are 3500, of which every month thier are 40-50 new bank accounts / bank account changes happens
    2. https://docs.google.com/spreadsheets/d/1oG573MD1bXiTAhKzt9AJ_JP2G8t_ifM_nW6i1GhWoGc/edit?gid=638303458#gid=638303458

**Marketing Comms:**

- Currently Marketing comms is handled in a mannual fashion Analytics make a mannual file send to Labdhi (Marketing) he uploads to wati for comms
- here their are many a times issues with amount that is shared to MFD & Comms Timings
- https://docs.google.com/spreadsheets/d/1RDgsU3YYXxqllhZopHY7Bc99nqSWAbEKH0pkoe_1a-4/edit?usp=sharing

**Reporting (Earning Report / Payout dashboard / Platform brokerage reports):** 

1. Earning report acts a ledger for partner earnings - this is calculated manually and uploaded on S3.
    
    [cd89ec14-503d-4656-b00f-81c6512574ef.xlsx](MFD%20Payout%20Process%20Revamp/cd89ec14-503d-4656-b00f-81c6512574ef.xlsx)
    
2. Payouts dashboard is internal tool, to get the details of partner and their respective payouts
    1. https://docs.google.com/spreadsheets/d/18Zf_H4BNUEfY4LSBARGNGOBQc1pjw_Z4smfzxKM2020/edit?gid=1271729655#gid=1271729655
3. Platform brokerage reports: for all the external platforms we share a sheet that contains summary of the their sharing & customers 
    
    :: https://docs.google.com/spreadsheets/d/1wLcqbNrxJPmVmQvUu7fpBQ2bdmsioE3abV4pPkzOzDc/edit?gid=1887240370#gid=1887240370
    

Resources: 

1. https://docs.google.com/document/d/1S4d3hz0OUZnV1osqYfdvRyD8MbWp5LgElifzzg0tOQI/edit?tab=t.0#heading=h.ndewm9pzlkw1
2. 

### Tech team

- Tech team need to provide the accurate data tables to the the Analytics team, These table creation and updation is dependent on lender infra.

### Support team - RMs

- As a RM i prefer to help new customer complete the applications instead of MFD payout issues of MFDs
    - Currently 2-3 days are taken up for payout issues and resolution and have to deal with angry MFDs
    - RMs can Provide assistance on GST invoice directly have to involve business team and CA to resolve with very high TAT.

| Stage | Activity | Gap in System | Issues |
| --- | --- | --- | --- |
| MFD Onboarding | Capturing commercial b/w MFD and Volt | Not captured in the DB as of now | - Commercials are captured in a excel sheet by RMs maintained by Puneet
- Need a better ways to document, as Dynamic rates, base rates for one-time and trail are different and changes from time to time
- ~~there are slabs for some partners
- there three types of MFD-direct, MFD-software, Affiliates.
- to be checked how commercials are closed~~  |
| MFD Onboarding | Capturing MFD’s bank account | Captured. Updated bank account? | - Bank account verification before payout using pennydrop
- HSBC takes two day to tell us if Bank account does not exist 
- MFD changing bank account is not handled
- How to store money till user add there bank account 
- Do not allow international bank account  |
| Application | Capturing commercials at application level | Not captured in the DB as of now | - RMs capture in sheets
- the transactions made by user is stored in tranasaction table which is not updated on a daily basis , to not overload Miles
- we need upto date POS sheet everyday |
| Application | Calculating payout at application level | Not captured in the DB as of now | - we store transaction data in disbursement table and in repayment table but not in transaction table on a daily basis . transaction table is updated monthly from lender’s data due to inability of lenders to provide capable infra |
| End of Month | Calculating overall calculations (month level) + TDS and GST calculation | Not captured in the DB as of now | - It takes 18 hrs to build the transaction table from the Lenders data. Ops start the process in parallel for both lenders 
- Transaction table reconned can be provided by 2nd of the month 
- the POS is calculated by analytics offline 
- the transactions made by user is stored in transaction table which is not updated on a daily basis , to not overload Miles
- build own tables then recon with lender
 |
| Servicing | Visibility of earnings to MFD | To be checked | - Earning are not visible to MFD and are not clear, on a transaction and ledger basis 
- We need to provide better comms and in dashboard experience  |
| Servicing | Invoice confirmation from MFD | To be checked | - Improve Invoice experience 
- Invoice format should be cover the ledger of what is breakup of the payment  |
| Servicing | Show TDS and GST details to MFD | To be checked | - Calculate correct TDS and GST,
- collect and validate GSTN 
- Verify bank account  |
| Payout | Payout earnings to MFD (1st cut) |  |  |
| Payout | Payout earnings to MFD (2nd cut or differences) |  | - we don’t keep track of MFD GST payouts if a MFD requests outside of the system
- there is no validation of GSTN
there is no validation of bank account  |
| Payout | Reconciliation of MFD payout transactions |  | - we need a tracking of MFD payouts, which MFD is pending , which MFD raised request, which MFD need bank acccount change and GSTN approved  |
| Payout | Offline payouts to be avoided | Pause all offline payouts on demand. All payouts to happen through system | - no tracking or SOP for ad hoc payments 
- SOP needed for change in commercial - application level , Gst invoice , TDS, bank account change , payouts 

 |
| Payout | Separate bank account for payouts | Single bank account being used for all transactions | - get a new bank account dedicated to MFD payouts  |
| Taxation | Filing of TDS | Needs to be handled offline | - collect files needed for CA |
| Taxation | Filing of GST | Needs to be handled offline | - collect files needed for CA |

---

# **How do we measure success?**

- GST invoice related

---

# **How are others solving this problem?**

Below is the way most lenders handle the payouts flow.

- All commercials between the MFD and lender to be in the system
- Any commercial deviations at an application level to be stored in the system
- MFD or DSA can view the accrued earnings on the dashboard
- System calculates the payouts basis certain set of parameters
- Operations team reviews the payout calculations
- Invoice is generated by the system on the dashboard by 5th
- MFD confirms the invoice is accurate or raises an issue
- Finops team settles the payouts to MFDs by 10th which are confirmed
- MFDs raise any discrepancies to Volt by 15th
- Any payouts which weren’t processed is settled in the subsequent cycle on 20th
- TDS is deducted from the payouts by the system itself
- GST invoice is shared with the MFD
- MFD can view their earnings, TDS deductions, GST calculations, etc on dashboard
- Volt’s accounting team(jars) files TDS and GST as per cycle

Flow wise , 

---

# **What is the solution?**

## Requirements overview

### Phase 1

**Objective**: To ensure reduction in support related calls and issues, which will improve satisfaction and retention. This will drive growth.

- GST and Payout Invoice Creation and MFD approval flow

[PRD - GST Invoice and Payout statement creation and approval ](MFD%20Payout%20Process%20Revamp/PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an%2012ee8d3af13a80189662fc13cfe7d2a1.md)

- Analytics to pivot to partner and add balance in the ledger, this will enable us to send the Receipts
- Receipts can be shared on the MFD dashboard with approval and issues taken
- We will capture the ad hoc Payout Req in a Dashboard. This is a major issue to create accurate tables
- Full Dashboard and Payout flow can be built  process can be
- For Recon purposes the flow is required

### Phase 2

**Objective**: To ensure reduction in internal man-hours for reconciliation and payouts. This will improve partner satisfaction and drive retention.

### Phase 3

**Objective**: To ensure industry-best MFD and agent channel experience. This will help us acquire more MFDs/ IFAs with very low cost.