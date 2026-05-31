# Dues Comms Updation

: Yogesh D
Created time: April 10, 2026 12:07 PM
Status: Not started
Last edited: May 15, 2026 4:30 PM

# What problem are we solving?

- Current SMS templates for due reminders, auto-debit alerts, overdue notices lack transparency, as they omit specific charges like collateral sell-off charges and fail to disclose the exact amounts for penal and dishonour charges.
- RBI guidelines require explicit disclosure of all applicable charges and reasons in all such communications.
- This gap creates a risk of non-compliance with RBI transparency and disclosure norms

# How do we measure success?

- **Send accuracy** — 100% of scheduled due communications utilize the newly updated, regulatory compliant DLT templates.
- **Log coverage** — 100% of records logged with per-record dispatch status for compliance audit, proving customers were notified of potential charges.
- **Regulatory Compliance** — Zero audit observations regarding the non-communication of penal charges during the loan repayment cycle.

# What is the solution?

## Overview

- Scheduled communication jobs will be updated to new DLT-approved templates that list all applicable charges (including collateral sell-off) while referencing the "as per KFS" clause  instead of mentioning the amount being levied against each of the charges, ensuring Compliance-aligned transparency.
- why "as per KFS" and no mention of exact charges.
    - KFS has clear disclosure of all charges and their value which satisfies the regulatory requirement of DSP letting users know the charges and their amount.
    - Charges like collateral sell off charges don’t have an exact amount example
        - 0.25% of the proceeds received + 18% GST
           -Maximum 1999 (excl. GST) will be charged in case securities
             are sold to recover dues.
           -Maximum 999 (excl. GST) will be charged in case security
             sell-off is requested by the customer
    - charges may change but this approach will still ensure we are regulatory compliant and not having to make changes to templates every time.
    - Repetitive mention of charges and their amount across overdue comms will be unnecessary example charges like Dishonour charges are levied only once a month but mentioned in every template.

## In Scope

- Migrating the existing communication events to the newly drafted SMS templates.
- Dynamo DB logging at a per-record level for all outcomes (success, failure) to maintain a compliance audit trail.

## Communication Specification

### Channel

- SMS
- Email

### Updated Comms

- SMS DSP

| **Event Trigger** | **Event Type** | **Existing DLT Template ID** | Existing Body Template | **New DLT Template ID** | **SMS Body Template** | Ghupshup_body | **Comments** | Tech template name |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2nd & 4th | Payment reminder | 1107175524057331890 | Rs. {#var#} due on {#var#} for your loan account {#var#}. Pay via {#var#} on or before {#var#} to avoid dishonor and penal charges - DSP FINANCE | 1107177729308956175 | Rs. {due_amount} due on {due_date} for your loan account {lan}. Pay via {sourcing_channel} on or before {due_date} to avoid levy of dishonor and penal charges as per KFS - DSPFIN | Rs. {#var#} due on {#var#} for your loan account {#var#}. Pay via {#var#} on or before {#var#} to avoid levy of dishonor and penal charges as per KFS - DSPFIN | Ready for tech

DONE | `DUES_REMINDER` |
| 6th | Auto-debit notification | 1107175524068439010 | Auto-debit of Rs. {#var#} will be attempted on {#var#} from bank account XXXX{#var#} for your loan account {#var#}. Maintain sufficient balance to avoid dishonor and penal charges - DSPFIN | 1107177641869597857 | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from bank account XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid levy of dishonor and penal charges as per KFS - DSPFIN | Auto-debit of Rs. {#var#} will be attempted on {#var#} from bank account XXXX{#var#} for your loan account {#var#}. Maintain sufficient balance to avoid levy of dishonor and penal charges as per KFS - DSPFIN | Ready for tech

DONE | `DUES_REMINDER_MANDATE_REGISTERED` |
| 7th | Auto-debit failed | 1107175524102388351 | Auto-debit attempt on your loan account {#var#} failed on {#var#}. Repay Rs. {#var#} via  {#var#} to avoid dishonor and penal charges - DSP FINANCE | 1107177642013675910 | Auto-debit attempt on your loan account {lan} failed on {due_date}. Repay Rs {due_amount} via {sourcing_channel} to avoid levy of dishonour and penal charges as per KFS - DSPFIN | Auto-debit attempt on your loan account {#var#} failed on {#var#}. Repay Rs. {#var#} via {#var#} to avoid levy of dishonor and penal charges as per KFS - DSPFIN | 
RE REGISTER DIS AND ADD RS. | `AUTO_DEBIT_FAILED` |
| 8th, 11th, 14th, 17th | Overdue | 1107175525443527157 | Rs. {#var#} overdue on your loan account {#var#}. Pay via {#var#} before 20th of the month to avoid collateral sell-off. Dishonor and penal charges applicable - DSP FINANCE | 1107177642029565871 | Rs. {due_amount} overdue on your loan account {lan}. Pay via {sourcing_channel} before the 20th to avoid collateral sell-off. Penal, & collateral sell-off charges applicable as per KFS - DSPFIN | Rs. {#var#} overdue on your loan account {#var#}. Pay via {#var#} before 20th of the month to avoid collateral sell-off. Penal & collateral sell-off charges applicable as per KFS - DSPFIN | comma

Reregister | `OVER_DUES_REMINDER` |
| 19th | Second Auto-debit notification | 1107175524142410806 | Auto-debit of Rs. {#var#} will be attempted on {#var#} from XXXX{#var#} for your loan account {#var#}. Maintain sufficient balance to avoid collateral sell-off - DSP FINANCE | 1107177642053845728 | Auto-debit of Rs. {due_amount} will be attempted on {due_date} from bank account XXXX{account_last4digits} for your loan account {lan}. Maintain sufficient balance to avoid collateral sell-off & levy of collateral sell-off charges as per KFS - DSPFIN | Auto-debit of Rs. {#var#} will be attempted on {#var#} from bank account XXXX{#var#} for your loan account {#var#}. Maintain sufficient balance to avoid collateral sell-off & levy of collateral sell-off charges as per KFS - DSPFIN | Ready for tech | `AUTO_DEBIT_REMINDER_FOR_SECOND_MANDATE` |
|  | SHORTFALL | 1107176588248414267 | Dear {#var#}, your loan account {#var#} has a shortfall of Rs {#var#} due to a fall in portfolio value. Please repay or pledge additional securities by {#var#} to avoid sell-off. Repay on the DSP Finance app: {#var#} - DSPFIN | 1107177850837027115 | {#lan#} has a shortfall of Rs.{#shorfall_amount#}. Repay or pledge additional securities by {due_date} to avoid selloff & levy of collateral addition/sell off charges as per KFS - DSPFIN | Dear {#alphanumeric#}, {#alphanumeric#} has a shortfall of Rs.{#alphanumeric#}. Repay or pledge additional securities by {#alphanumeric#} to avoid selloff & levy of collateral addition/sell off charges as per KFS - DSPFIN | Reregister. | `SHORTFALL_DUE_REMINDER` |
|  | WELCOME_LETTER | 1107176657577870667 | Congratulations {#var#}! Your Loan Against Securities account with DSP Finance, {#var#}, is now active with Credit Limit: Rs {#var#}.View your welcome document on the DSP Finance app: {#var#} - DSPFIN | 1107177338768331025 | Congratulations {customer_name}! Your Loan Against Securities account with DSP Finance, {Loan_account}, is now active with Credit Facility: Rs {credit limit amount}.View your welcome document on the DSP Finance app: {dsp_app_url} | Congratulations {#var#}! Your Loan Against Securities account with DSP Finance, {#var#}, is now active with Credit Facility: Rs {#var#}. View your welcome document on the DSP Finance app: {#var#} - DSPFIN | Re register. | `WELCOME_KIT` |
|  | HOLDING_STATEMENT | 1107176587809007297 | {#var#}Your Loan Against Mutual Funds statement dated {#var#} is available for download here: {#var#}. For support, contact: {#var#}  - DSPFIN | 1107177850689505583 | Dear {#customer_name#}, statements dated {#date#} for Loan Against Mutual Funds {#lan#} is available for download here: {#var#}.- DSPFIN | Dear {#var#}, statements dated {#var#} for Loan Against Mutual Funds {lan} is available for download here: {#var#}.- DSPFIN | Ready for tech
new comms 
NOT PICKED | `SOA_AND_HOLDING_STATEMENT` |
|  | COLLATERAL_ADDITION_CONFIRMATION | 1107176587956577738 | Dear {#var#}, your collateral addition request for your DSP Finance loan has been processed successfully. View updated collateral details on the DSP Finance app: {#var#} - DSPFIN | 1107177339199310507 | Dear {#customer_name#}, your collateral addition request for your DSP Finance Loan {#lan#} has been processed successfully. View updated collateral details on the DSP Finance app: {#dspfin.com#} - DSPFIN | Dear {#var#}, your collateral addition request for your DSP Finance Loan {#var#} has been processed successfully. View updated collateral details on the DSP Finance app: {#var#} - DSPFIN | Re register | `ADD_COLLATERAL_SUCCESS` |
|  | COLLATERAL_RELEASE_CONFIRMATION | 1107176587959190438 | Dear {#var#}, your collateral release request for your DSP Finance loan has been processed successfully. View updated collateral details on the DSP Finance app: {#var#} - DSPFIN | 1107177339192555890 | Dear {#customer_name#}, your collateral release request for your DSP Finance Loan {#lan#} has been processed successfully. View updated collateral details on the DSP Finance app: {#dspfin.com#} - DSPFIN | Dear {#var#}, your collateral release request for your DSP Finance Loan {#var#} has been processed successfully. View updated collateral details on the DSP Finance app: {#var#} - DSPFIN | Re register | `RELEASE_COLLATERAL_SUCCESS` |
|  | LOAN_CLOSURE_CONFIRMATION | 1107176588244217596 | Dear {#var#}, your Loan Against Mutual Funds is closed successfully. All pledged collateral has been released. Your No Dues Certificate is ready. View on the DSP Finance app: {#var#} - DSPFIN |  | Dear {#customer_name#}, your Loan Against Mutual Funds {#lan#} is closed successfully. All pledged collateral has been released. Your No Dues Certificate is ready. View on the DSP Finance app: {#dspfin.com#} - DSPFIN | Dear {#var#}, your Loan Against Mutual Funds {#var#} is closed successfully. All pledged collateral has been released. Your No Dues Certificate is ready. View on the DSP Finance app: {#var#} - DSPFIN | Re register | `NO_DUES_AND_CLOSURE_CERTIFICATE` |
|  | **DUES_REMINDER_MANDATE_NOT_REGISTERED** |  | Rs. {dueAmount} due on {dueDate} for your loan account {fenixLoanAccountId}. Pay via " + "{sourcingChannel} on or before {dueDate} to avoid dishonor and penal charges - DSP FINANCE" |  | Rs. {due_amount} due on {due_date} for your
loan account {lan}. Pay via
{sourcing_channel} on or before
{due_date} to avoid levy of dishonor and
penal charges as per KFS - DSPFIN | Rs. {due_amount} due on {due_date} for your
loan account {lan}. Pay via
{sourcing_channel} on or before
{due_date} to avoid levy of dishonor and
penal charges as per KFS - DSPFIN | DONE | `DUES_REMINDER_MANDATE_NOT_REGISTERED` |
|  | AUTO_DEBIT_REMINDER |  |  |  |  | Auto-debit of Rs. {#var#} will be attempted on {#var#} from bank account XXXX{#var#} for your loan account {#var#}. Maintain sufficient balance to avoid levy of dishonor and penal charges as per KFS - DSPFIN |  | `AUTO_DEBIT_REMINDER` |
- SMS Volt

| **Event Trigger** | **Event Type** | **Existing DLT Template ID** | Existing Body Template | **New DLT Template ID** | **UPDATED SMS Body Template** | **Comments** | config |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | credit_line_approved | 1107177210976900189 | Your VoltMoney credit line of {#numeric#} is approved.  Access funds anytime. Pay interest only on usage.    Complete application: {#url#} -VOLT | 1107177857554681535 | Your VoltMoney credit facility of Rs.{#numeric#} with {#alphanumeric#} is approved. Access funds anytime. Pay interest only on usage. Complete application: {#url#} -VOLT | check gp |  |
|  | las_shortfall_reminder | 1107176673331091218 | URGENT - Rs. {#var#} shortfall in your loan against share ({#var#}). Repay shortfall amount within {#var#} days to avoid security sell-off. -VOLT | 1107177865714517409 | URGENT - Rs. {#alphanumeric#} shortfall in your loan against share {#alphanumeric#} with {#alphanumeric#}. Repay shortfall amount within {#numeric#} days to avoid security sell-off and levy of collateral sell-off charges as per KFS.-VOLT | check vil
register for dsp and non dsp |  |
|  | FIRST_INTEREST_DUE_MANDATE_REGISTERED | 1107174601396149942 | {#var#} month statement generated Amt due: Rs. {#var#} Auto-debit date: {#var#} from XXXX{#var#} Maintain enough balance to avoid bounce charges -VOLT | 1107177857600422734 | {#var#} month statement generated Amt due: Rs. {#var#} Auto-debit date: {#var#} from XXXX{#var#} Maintain enough balance to avoid levy of bounce charges as per KFS by {#alphanumeric#} -VOLT | check gp | Interest repayment |
|  | mobile_number_update_otp_verification | 1107173434413767950 | {#var#} is the OTP to update registered mobile number. It is valid for 15 minutes.   - VOLT | 1107177858422036344 | {#alphanumeric#} is the OTP to update the registered mobile number for Loan {#alphanumeric#} with {#alphanumeric#}. It is valid for 15 minutes. -VOLT | check gp |  |
|  | auto-debit | 1107173331868790368 | Loan Against Mutual Funds Auto-debit date: {#var#} Amt: Rs. {#var#} Ensure balance in acc. xxx{#var#} to avoid bounce - VOLT Money | 1107177857663767305 | Loan Against Mutual Funds having {#alphanumeric#} with {#alphanumeric#} Auto-debit date: {#alphanumeric#} Amt: Rs. {#alphanumeric#} Ensure balance in your registered account xxxx{#alphanumeric#} to avoid levy of bounce charges as per KFS -VOLT | check gp |  |
|  | mandate_registration | 1107173229211971758 | Register your mandate for auto-debit of your monthly interest for your Loan Against Mutual Funds on the Volt Money app: {#var#} -VOLT | 1107177858286346660 | Register your mandate for auto-debit of your monthly interest for your Loan Against Mutual Funds having {#alphanumeric#} with {#alphanumeric#} on the Volt Money app: {#url#} -VOLT | check gp |  |
|  | Loan_confirmation_T1 | 1107172742063596784 | {#var#} is the OTP to confirm your Mutual Fund loan account closure request via TATA NEU -VOLT | 1107177865586117145 | {#alphanumeric#} is the OTP to confirm your Loan account against Mutual Funds {#alphanumeric#} closure request via TATA NEU -VOLT | check vil |  |
|  | Security_Unpledge_T1 | 1107172742049709881 | {#var#} is the confirmation number for your security unpledge request via TATA NEU -VOLT | 1107177858313771052 | {#alphanumeric#} is the confirmation number for your security unpledge request for loan {#alphanumeric#} with {#alphanumeric#} -VOLT | check gp |  |
| done | Disbursal OTP | 1107166902697405016 | {#var#} is the OTP to withdraw Rs.{#var#} to your account ending {#var#}. It is valid for {#var#} minutes. -VOLT | 1107177865487807290 | {#alphanumeric#} is the OTP to withdraw Rs.{#alphanumeric#} from your loan {#alphanumeric#} with {#alphanumeric#} to your account ending xxxx{#alphanumeric#}. It is valid for {#alphanumeric#} minutes. -VOLT | check vil
register for lark | withdrawal comm config |
|  | LoginTNEU | 1107172741896591684 | {#var#} is the OTP to withdraw Rs.{#var#} to your account ending {#var#}. It is valid for 15 minutes. - TATA NEU -VOLT |  | {#alphanumeric#} is the OTP to withdraw Rs.{#alphanumeric#} from your {#alphanumeric#} with {#alphanumeric#} to your account ending {#alphanumeric#}. It is valid for 15 minutes. - TATA NEU -VOLT | Check with tech is it used |  |
|  | 20230320_SMS2 | 1107167896178739639 | Avoid redeeming your client's MF for short-term funds! Volt money offers quick mutual fund loans. click here: {#var#}{#var#} - VOLT -VOLT |  | Avoid redeeming your client's MF for short-term funds! Volt money in association with its lending partners offers loan against mutual funds. click here: {#url#} -VOLT | Check with tech is it used |  |
| done | LAMF_shortfall |  |  |  |  |  | shortfallcomm |
|  | credit_line_closure_OTP |  |  |  |  |  | foreclosure |
- EMAIL (OD and Term Loan)
- We are supposed to add APR in Statement of Account the corresponding sendgrid Template ID is shared. In the Attached SOA pdf we are supposed to add the APR of the customer
- APR to be fetched from kfs_details data table in fenix-los

| SOA email | Sendgrid template ID |
| --- | --- |
| Term Loan | d-ff2455b081fa4f7384fccdd207a7d40b |
| OD loan |  |
| Loan Against Share | d-57b26afe5c4d430494d423c4c940151f |

# Happy Path

- The daily comms job executes as usual.
- System retrieves the newly updated regulatory DLT template mapped to that event and event day.
- System constructs the SMS body by substituting the dynamic variables (Amount, Dates, Account No, Links) into the template.
- SMS is dispatched to the customer's registered mobile number via the primary SMS gateway.
- Dispatch result (success) is logged to Dynamo DB at the per-record level, serving as proof of regulatory compliance that the customer was informed of the penal charges as per KFS.

# Open Items / Checklist

- DLT Registration — Register the 5 new/updated templates on the DLT portal and obtain the new Template IDs.