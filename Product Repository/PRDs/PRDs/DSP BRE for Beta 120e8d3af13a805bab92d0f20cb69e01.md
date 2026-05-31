# DSP BRE for Beta

: Saksham Srivastava
Created time: October 15, 2024 5:40 PM
Status: Pending Review
Last edited: October 28, 2024 10:53 AM
Owner: Gautam Mahesh

# **What problem are we solving?**

Currently, customers can avail a loan from Volt app or web through DSP only through whitelisting or URL based parameters. This will not be possible to handle in the beta stage as we need to route applications real-time to DSP.

In addition, the segment where the credit limit offered by Volt is between 10K and 25K is ~12% of the total eligible applications which isn’t catered to by our other lenders, Bajaj and Tata. This opens up a new set of customers for us to acquire and eventual enhance from a limit perspective. 

---

# **How do we measure success?**

- Increase in offer generation numbers by at least 450bps
- Increase in sanction numbers by at least 320bps (~28% drop-off)
- Sanction value/month to increase by at least 40L
- Number of customers to increase by atleast 6 per day for 10K - 25K segment

---

# **How are others solving this problem?**

- Enable customers who have credit limit less than ₹25k but more than ₹10k by changing the minimum eligible amount. (subsequent phases)
- Build a generic backend BRE or eligibility check API for LSPs to consume from their backend (recommended) or UI (subsequent phases)

---

# **What is the solution?**

## Requirements Overview

We are splitting the DSP BRE changes into 3 phases broadly. T

- Phase 1/Beta: add the DSP BRE to cater to B2B2C (MFD) channels
- Phase 2: add the DSP BRE to cater to B2B2C (MFD) channels and platforms
- Phase 3: add the DSP BRE to cater to B2C (web & app) channel and B2B2C (MFD) channels and platforms
- Phase 4: add the DSP BRE to cater to B2B platforms

This document lays out the BRE For Phase 1/Beta only. Subsequent phases will have their own BREs.

<aside>
💡

The detailed break-downs for Phase 2, 3, 4 will be covered separately

</aside>

## Requirements Overview (Phase 1)

1. The minimum eligible limit for customers to avail volt credit limit will continue to be ₹25k. This number might reduce further as we go, especially when we open up the B2C channel.
2. The maximum eligible limit for customers will be set at 2CR for now and will be increased as we go.
3. All customers with eligible credit limit above ₹25k should be assigned DSP lender as per one of the below rules.
    1. Applications coming from whitelisted MFDs
    2. %age of applications coming from whitelisted MFDs
4. Add configuration parameters for BRE which can be used like.
    1. Partner (MFD) using the partner code for whitelisting
    2. %age of the applications coming from a MFD to be routed to DSP

**Out of scope**: Build an eligibility check API which can be consumed by not just Volt but other LSPs who will be going live with our APIs

## User Flow (Phase 1)

**Pre-requisite**: Product/Biz will share the list of MFDs to be whitelisted for DSP.

1. Customer’s application is started through the MFD dashboard and the MFD fetches the funds CAMS or KFin or both.
2. LSP checks if the MFD is whitelisted for DSP. If DSP isn’t configured, then Bajaj or TATA is allocated as per the appropriate BRE.
3. LSP configures TATA as the default lender to fetch funds, etc.
4. LSP provides the limit basis the LTV configured at LSP’s end and derives the complete offer amount.
    1. >2CR: the BRE will allocate the customer to BFL or TCL as per the %age
    2. ≤ 2CR and ≥25K : the BRE runs keeping DSP, BFL and TCL as lender as per the %age configured
    3. 10K - 25K: LSP rejects the customer for now
    4. <10K: LSP rejects the customer
5. LSP informs the customer on UI that its not eligible if the credit limit is <10K. This will be messaged something like ‘We regret to inform you that you aren’t eligible for a loan at this stage.’
6. If the customer is eligible with DSP, they proceed with the offer screen (Select credit limit) on the LSP UI.
7. If the eligible lender allocated as per the BRE is BFL or TCL, the flow will continue to next step on the offer screen (Select credit limit) on the LSP UI.

### Rules (Phase 1)

Below are the BRE rules for DSP in the beta stage.

| **Parameter** | **Value** | **Comments** |
| --- | --- | --- |
| Credit limit (Drawing Power) | ≥ 25000 AND ≤ 2,00,00,000 |  |
| Funds whitelisted | As per the DSP approved list | To be uploaded |
| Channel | MFD |  |
| Split on B2C | 0% |  |
| B2B partners | 0% | Not to be enabled for any B2B partner as of now |
| MFD list | 50% of applications | List of MFDs who are whitelisted to be shared |
| MFD platforms | 0% | Not to be enabled for any MFD platform as of now |

<aside>
💡

Remove the lender name on Retool till the lender BRE allocation is completed

</aside>

---

# **Design**

Some cosmetic changes are to be done at our end to handle the amount logic on LSP UI. Nothing on DSP backend.

---

# **Analytics**

Below are the numbers to be captured.

- Number of applications approved by DSP in <25K (drawing power) bracket
- Number of loans opened for DSP in <25K (drawing power) bracket
- Number of sanctions for DSP in <25K (drawing power) bracket
- Number of customers who accept the offer
- Average offer value of customers

---

# **Timeline/Release Planning**

[BRE Phase 2++ Items](DSP%20BRE%20for%20Beta/BRE%20Phase%202++%20Items%20129e8d3af13a807f955ce11760258c42.md)

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Train the Ops team around change in minimum loan amount logic
- [ ]  Business
    - [ ]  Inform business team about changes to the minimum threshold logic
- [x]  Design

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

Data distribution for eligible limit: https://docs.google.com/spreadsheets/d/1XqSC2PravuhEaL7u2as1XZnaV1lFaJt0eduD1FCUMKA/edit?usp=sharing

## Meeting notes

@Gautam Mahesh : Had discussed this with Arpit. The only risk scenario that I can think of here: 

1. customer who is started application with another partner let’s say jupiter with an eligbile credit limit of 25k, would be assigned jupiter platform. 
2. Now this user sold some of his mutual fund and his eligible credit limit is 15k, 
3. this user check limit from Volt Website, we will show them the limit and make the user go ahead in the application,
4. later in the application user will see that he is not eligible since his eligible credit limit is lower than 25k.