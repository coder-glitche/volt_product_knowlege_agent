# [Platform] Disbursement optimisation to handle cross billing cycle reversals

Last Edited: May 6, 2025 7:03 AM
PRD Owner: Vaibhav Arora
Status: Completed

# **What problem are we solving?**

As an NBFC one of the core aspects is to handle disbursements. Disbursement as a request as primarily two main components:

- Payout from the source bank account to the beneficiary bank account
- Posting of the transaction in the loan account of the user

While it seems pretty straightforward, there are multiple aspects that affect this workflow:

- Charge posting and knock off from disbursement requests
- Disbursement reversals

More about payouts:

Now payouts primarily have two cycles, debit cycle where the money is debited from the source bank account (NBFC bank account), and credit cycle where the amount is credited to the beneficiary bank account (Customer bank account).

There are types of payouts that any entity can make:

- IMPS (near instant) has a limit of 5 lakhs
- RTGS (real time) one to one settlements available 24/7 without limits
- NEFT (processed in blocks/batches of 30 minutes) available 24/7 without limits

We are currently using IMPS and RTGS (IMPS below 5 lakhs and RTGS above 5 lakhs for payouts).

We post the transaction in the loan account of the user post debit cycle success, which essentially means that the amount has been debited from our account. However payouts can still fail post debit success. 

While we have handled the corresponding reversals, when the payout is reversed, the charge knock off entry and the corresponding payout is reversed) however there is one scenario where our handling breaks (which is what we will solve via this requirement).

If a payout is made in billing cycle 1, and when the billing cycle changes when the payout is reversed, we are unable to reverse the knock off entry corresponding to the disbursal.

Which essentially means, that NBFC recognises income (charge knock off) which it has not collected.

---

# **How do we measure success?**

- Number of disbursements that reverse between two billing cycles
- Number of charge knock offs that are not reversed as their corresponding payouts were reversed

---

# **How are others solving this problem?**

NA

---

# **What is the solution?**

When a payout for a disbursement request placed in the previous billing cycle with a successful SOA posting in the previous billing cycle fails in the next billing cycle.

Change 1: Instead of reversing the payout as well as the corresponding knock off entry, we will be doing a partial return of the SOA posting.

Change 2: When a user places a withdrawal request, as a part of the workflow, we first knock off the charges, and then initiate the payout (sometimes it takes time for us to get confirmation on the payout cycle and the debit cycle in itself can fail) can cause similar instances as described in the problem statement where we are unable to reverse the charge knock off transaction post billing cycle

Scenario 1:

Processing fees applied on 31st March 2025 for account opening of Rs 1,000

- Processing fee is posted in the loan account creating a charge due of Rs 1,000

User placed a disbursement request of Rs 10,000 on 31st March post account opening and amount is successfully debited from the NBFC bank account

- Charge knock off transaction is placed clearing the charge due (reducing it by Rs 1000)
- SOA posting is done to increase principal outstanding by Rs 10,000

Credit cycle for the corresponding payout fails on the first (Cashfree confirmation) on the 1st of April:

- SOA posting is reversed with Finflux’s partial return API for an amount (Disbursement request - Charge knock off amount) in this case for Rs 9,000

Scenario 2:

Processing fees applied on 31st March 2025 for account opening of Rs 1,000

- Processing fee is posted in the loan account creating a charge due of Rs 1,000

User placed a disbursement request of Rs 10,000 on 31st March post account opening and amount however the payout goes in a pending state 

- Please note that we will not place charge knock off entry till we get a success state (payout initiated successfully) from Cashfree

![image.png](%5BPlatform%5D%20Disbursement%20optimisation%20to%20handle%20cro/image.png)

## User stories / User flow

Previous flow (Debit success):

- User places a disbursement request
- Outstanding charges if any are knocked off and deducted from the requested amount and net amount is disbursed in their bank account
- Charge due reduces to zero, and POS increases with amount equal to requested amount
- If payout fails, SOA posting is reversed POS reduces to zero and charge due increases back to the initial due amount

Previous flow (Debit pending):

- User places a disbursement request
- Outstanding charges if any are knocked off and a payout is created
    - Payout goes to a success state (debit success): Same as above
    - Payout goes to a failed state (Charge knock off transaction is reversed (**billing cycle change leads to failure of reversal**)

New flow (when billing cycle does not change) - Same as existing/previous flow (debit success)

- User places a disbursement request
- Outstanding charges if any are deducted from the requested amount and net amount is disbursed in their bank account
- Charge due reduces to zero, and POS increases with amount equal to requested amount
- If payout fails, SOA posting is reversed POS reduces to zero and charge due increases back to the initial due amount

New flow (When billing cycle changes) (Debit pending):

- User places a disbursement request
- **Payout is created first and charges are not knocked off till we get a success state from Cashfree**
    - Payout goes to a success state, charges are knocked off and POS is posted to loan account
    - Payout goes to a failed state, disbursement is marked as failed (user is notified to request again)

New flow (when billing cycle changes) (Debit success):

- User places a disbursement request
- Outstanding charges if any are knocked off and deducted from the requested amount and net amount is disbursed in their bank account
- Charge due reduces to zero, and POS increases with amount equal to requested amount
- If payout fails, SOA posting is reversed with partial amount equal to requested amount - charges knocked off

<aside>
🚨

Please note: When payout will be reversed, user will still have a principal outstanding equal to the processing fee (since now charge due is converted to POS)

</aside>

## Requirements

Finflux partial return API integration

API Curl:

```json
curl 'https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/revolving-credit-lines/000004148/transactions/bd1117e4-5afc-46a5-aca1-9a30de0e054a/partial-return' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'authorization: Bearer AKQmO6CCjAUbcCarfqPPxjnre_w' \
  -H $'content-security-policy: default-src \'self\'' \
  -H 'content-type: application/json' \
  -H 'hashed-request-body: UMG1VCxjtXNU/a50Fy/ZqeE2Nmrl15u7GEMbiCx0ZWcrNfW7V+1Kz3YV8ikSP7Xx2pZZqVMcWPvlxyONBSMTsO30dFUOIB+sQZ9mrOP1tRPJ4YxrLbI359waXqhrycATmWXWp2MeUPHq/4YzvHqL06FI9NWHmkr6w8eKpmUUQ67ybUhL7YJIUc4XVaqqT1tRw6v3+QW5nG/KxpMkv5Diq1zuq+eBaWCTYe69kvfk4YQkCo25KIhXc01IOFfuy7vXz2CCkIVpp0KLV6H7n1c9USixD0ssk18akRl3bFC1U0Npt0+zXxbpssy3U87HtEG4nI3N2wWo/IvuKX61jSto8Q==' \
  -H 'origin: https://uat-voltmoney.finfluxtrial.io' \
  -H 'priority: u=1, i' \
  -H 'referer: https://uat-voltmoney.finfluxtrial.io/customers/1077/credit-line/000004148' \
  -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  --data-raw '{"amount":500,"notes":"Check"}'
```

**Reversal transaction reference ID:**

For current reversals, a reference ID for the corresponding return transaction of payout is sent as per the following logic:

Example: If the disbursement request ID for the initially raised request by the customer was DR134252432 the transaction ID for the reversal of the corresponding transaction would be DR134252432R.

<aside>
🚨

Please note: This implementation and the logic will remain the same for reversals within the same billing cycle

</aside>

Partial disbursement reversals (Disbursement reversals with a billing cycle change) will follow the following logic:

Example: If the disbursement request ID for the initially raised request by the customer was DR134252432 the transaction ID for the reversal of the corresponding transaction would be DR134252432P (Where P signifies partial return).

**Enrichments:**

We will be passing the following enrichments in the partial return of the disbursement request:

Enrichment1: DRID of the disbursement reversed for the transaction

Enrichment2: CKOID (Knock off transaction ID of the charge knocked off with the disbursement)

**Transaction remarks:**

We will be passing the following transaction remarks for the transaction:

Partial amount reversed for loan account number: {{FXLAN}} against withdrawal posted on {{Disbursement requested date}}

**Accounting:**

This release will have an accounting impact as the charges due are being capitalised and are being collected as income despite the payout being reversed (partially).

Accounting team will need ways to recognise such scenarios so that they can identify and account them accordingly:

- Accounting team will be able to identify the same transactions by the external ID (Should start with DR and end with P)
- Accounting team will be able to identify the reversed disbursement (DR ID in enrichment1 and the charge knock off transaction (CKO ID) from the transaction remarks of the payout return transaction.)

Operations reconciliation team:

- Operations team will use the same markers defined above to identify and accordingly reconcile transactions for internal reference

LSP communication:

- LSPs will be notified on these scenarios via the disbursement reversal webhook.
- We will be introducing a new status for disbursals (terminal state) called partially_reversed and will introduce a new parameter which can be used for internal and external reference called reversed_amount
- LSPs will be able to gauge what amount was reversed based on the requested amount and reversed amount parameter and can rely on the partial_reversed status for reelvant communication to the user.

```json
Enter webhook for withdrawal reversed here
```

---

# **Design**

NA

---

# **Analytics**

- Number of disbursements that reverse between two billing cycles
- Number of charge knock offs that are not reversed as their corresponding payouts were reversed

---

# **Timeline/Release Planning**

- To be picked in April A sprint
- PRD kickoff date: 31st March 2025
- ETA from engineering team: Pending

---

# **Go to market**

- LSP notification for upcoming changes and requirements alignment (Pending)
- External dependencies with Finflux (NA)
- NBFC Finance team alignment on change (Initiated)

## Marketing

## Ops & Sales training

- Pending

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