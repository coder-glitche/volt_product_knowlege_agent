# Multi Drawdown Term Loan: LMS Requirements

: Gautam Mahesh
Created time: June 4, 2025 11:20 AM
Status: In progress
Last edited: October 30, 2025 2:56 PM
Owner: Parikshit Kumar

# **What problem are we solving?**

The existing OD-based Loan Against Mutual Funds (LAMF) product does not align with the repayment expectations and financial behavior of a large segment of customers. These users are more familiar with **structured EMI-based repayment formats**, as seen in personal loans, home loans, and auto loans. As a result, product comprehension, drawdown confidence, and repayment discipline are negatively impacted when only an OD line is offered.

This gap is particularly visible in:

- Low drawdown rates from sanctioned limits
- Confusion around usage-based interest calculation
- Hesitation in using OD due to ballooned principal repayment at the end

---

# **How do we measure success?**

## Product Metrics

### L1

- % of users who get the first drawdown
- % of users opting for a subsequent drawdown
- Mandate Presentation SR(First and subsequent presentations)

### **Business Metrics (LOS)**

- Daily total disbursals trend WOW, MOM, QOQ, YOY. This will be across all LSPs as well as LSP-wise distribution.
- LSP-wise distribution of loan applications initiated across OD and Term Loan products(SD&MD)

---

# **How are others solving this problem?**

NA

---

---

# What is the Solution?

Product Overview

We propose a **term-loan-style wrapper** on top of the facility construct to match user expectations and drive better usage. The solution involves:

- **Offering a familiar term-loan onboarding flow** for the first drawdown.
- **Enabling multiple drawdowns** from the same facility, with flexibility in amount and tenure.
- **Allowing re-borrowing** once limits are replenished through repayment.
- **Positioning the product clearly as “term loans with flexibility”**

This hybrid approach is designed to increase adoption, improve credit utilization, and grow customer LTV.

**Product Technical Construct**

A **line-backed, multi-drawdown term loan**, where:

- **Both loan and tranche constructs are exposed to the LSP**.
- DSP manages the **loan** as the credit container; **each tranche** is a separate drawdown linked to it.
- Multiple **active tranches** can exist simultaneously, each with its own amount, tenure, and repayment.
- On full **repayment of a tranche,** the loan limit is replenished, enabling **re-borrowing**.

This enables:

- A **term-loan-style UX** for each drawdown.
- Centralised collateral management via the loan with clear LSP visibility into both loan and tranche lifecycles.

# Requirements/User Flow

### Disbursement

**Overview**

The system supports drawdowns under a sanctioned facility, which we will refer to as Loan. Each drawdown is treated as a separate term loan instance with its own principal, schedule, ledger and we will refer to each of this term loan instance as a Tranche. 

[Term Loan: Disbursement](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Disbursement%20284e8d3af13a80038bfad3626adc9db2.md)

### Repayments

**Overview**

Once the user opts for a Term Loan product and had taken either single or multiple drawdowns/tranche, corresponding to each drawdown/tranche there will be a repayment/EMI schedule which will be generated. Based on the schedules repayment will be done by the user. There are multiple ways in which repayments can be done. Below are the different ways detailed out:

[Term Loan: Mandate Repayments](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Mandate%20Repayments%2024ce8d3af13a80208366c26e4b7ce3bb.md)

[Term Loan: Manual Repayments(PG)](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Manual%20Repayments(PG)%20249e8d3af13a80f99221fdbe69247b6f.md)

[Term Loan: Manual Repayments(VA)](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Manual%20Repayments(VA)%2024ee8d3af13a80e0a482d98f10281889.md)

[Term Loan: Foreclosure](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Foreclosure%20242e8d3af13a807ca29efce9aab8e150.md)

[Term Loan: Prepayments and Excess Handling](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Prepayments%20and%20Excess%20Handling%20260e8d3af13a800e871fe8e18392f88a.md)

[Term Loan: Sell off](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Sell%20off%20260e8d3af13a80eda1bff2779bca7eed.md)

[Term Loan: Charges](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Charges%20260e8d3af13a805d91d4f44f8e8aeff4.md)

[Term Loan: Apportionment Logic](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Apportionment%20Logic%20284e8d3af13a80d48381ef0e3d6de944.md)

[Term Loan: Excess Handling and Refund](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Excess%20Handling%20and%20Refund%2028ce8d3af13a80039847db947b0af212.md)

**Part Payments**

Not in V0

[Term Loan: DPD handling](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20DPD%20handling%20265e8d3af13a80e0bca0d0c413febd89.md)

[Term Loan: Unpledging](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Unpledging%20284e8d3af13a8008a8e8ffbfb03282d7.md)

[Term Loan: Unpledge Eligibility API(Post loan creation)](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Unpledge%20Eligibility%20API(Post%20loan%20creat%20287e8d3af13a80be80dcf142c7e0d4db.md)

### Statements

[Term Loan: Customer Statements](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Customer%20Statements%20265e8d3af13a80fab4b9caf8b3a2b4a9.md)

### Communication

[Term Loan: Communications](Multi%20Drawdown%20Term%20Loan%20LMS%20Requirements/Term%20Loan%20Communications%20265e8d3af13a80189253ca2b6508ccef.md)

### 

**Cool-off period(Not in V0)**

- This is the period post drawdown when the user will be able to cancel the loan without incurring any penalty for the same if they decide that they don’t want to go ahead with it.
- We have a cool-off period of 3 days/72 hours and if users cancel the loan in this period then we recover the pro-rata interest and pro-rata processing fee.
- CRED at their end has a cool-off period of only 24 hours. Their proposal was DSP should also keep the cool-off period as 24 hours and for the rest of the period the charges and interest needs to be handled offline in the commercials.
- In case of a single Tranche if user decides to pay during the cool-off period then we will be cancelling the Tranche but we won’t be unpledging the collaterals upto a certain period. The time period needs to be finalised by business.
- In case multiple tranches are active and user takes a fresh drawdown then decided to pay in cool-off for this fresh drawdown then this Tranche will be cancelled but the other Tranches will still remain active.
- In case of Tranche cancellation in cool-off period the pro-rata charge and interest will be adjusted from the amount which the user needs to pay back and accordingly the user makes the payment.
- Once the payment is received against the cool-off cancellation we will be posting the adjusted payment, closing the Tranche and mark it as *cool-off cancellation(Need to understand the current handling to decide on this)*.

---

# **Design**

---

# **Analytics**

---

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