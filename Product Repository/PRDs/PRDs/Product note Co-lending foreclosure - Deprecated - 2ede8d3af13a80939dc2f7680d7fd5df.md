# Product note: Co-lending foreclosure - Deprecated - ignore

: Ranjan kumar Singh
Created time: January 19, 2026 1:40 PM
Status: In progress
Last edited: March 15, 2026 8:49 PM
Owner: Lalit Bihani

## **Background and Context**

- **Who is facing the problem**
    - Customers foreclosing co-lended loan.
    - DSP Operations, Vol and DSP Support, Tech Ops teams handling servicing
    - TCL NBFC operations and finance teams managing their loan books
- **What is the challenge / what is broken today**
    - In a co-lending setup, a single customer loan is split across **two NBFCs (DSP 10%, TCL 90%)**
    - Customers expect a **single foreclosure action**, while lenders require **independent loan closure and settlement**
    - Without a clearly designed orchestration:
        - Foreclosures risk becoming partially completed
            - Example: Foreclosure can partially succeed—closing one lender’s loan while the other remains open—and if collateral is released at that point, one lender is left with an unsecured loan, which is a major regulatory risk.
        - Ops teams face manual reconciliation and escalations
- **Why is it important / what is impacted**
    - Foreclosure is a **high-trust moment** in secured lending
    - Any error directly impacts:
        - Customer trust and NPS
        - Regulatory compliance around pledge release
        - DSP’s credibility as the servicing NBFC
    - As co-lending is a **new product vertical**, getting this wrong early creates long-term operational debt.

---

## **1. Problem scope**

### In scope

- Designing a **safe and consistent foreclosure experience** for co-lended LAMF loans
- Ensuring customers interact with **only one loan experience**, despite multiple lender loans
- Enabling DSP to **orchestrate foreclosure end-to-end** while respecting lender-level closures
- Validations and error handling
- CC Maker checker for foreclosure processing
- Foreclosure repayment settlement(handling of accrued amount and excess management) and accounting

**Primary users**

- Retail customers foreclosing co-lended loans

**Secondary users**

- DSP operations and DSP Finance team
- Volt sales and support teams
- Volt Tech Ops
- TCL NBFC Ops & Finance teams

### Out of scope

- Payouts

---

## **2. Success Criteria**

- 
    
    ### Primary outcomes
    
    - Customers can foreclose co-lended loans through **one clear and predictable flow**
    - Repayments are getting posted without and disputes, All three loans are getting closed, collaterals are getting released and NOC is provided to the users.
    - Minimal manual intervention for standard foreclosure cases
    
    ### Key success metrics
    
    - Foreclosure completion success rate ≥ **99%**
    - Average foreclosure TAT ≤ **1 business day**
    - Ops/manual intervention rate ≤ **5% of cases**
    
    ### Post-launch good state
    
    - Foreclosure journey live and stable
    - Virtual loan(loan 100%) acts as **single source of truth** for servicing
    - Clear operational SOPs for edge cases
    - 0 disputes/error reported in accounting of repayments at TCL and DSP end
    
    ### Guardrail metrics
    
    - No increase in customer complaints post foreclosure
    - No settlement mismatches between DSP and TCL
    - No increase in MF unpledge failure rate

---

## **3. Solution Scope**

### Solution overview

- 
    - Implement a **DSP-orchestrated foreclosure flow** where customers act on a **virtual 100% loan**, while DSP coordinates closure of:
        - DSP’s 10% loan
        - TCL’s 90% loan
    - The solution prioritizes **correct sequencing and atomic closure.**

### Detailed solution scope:

- 
    - **User-level capabilities**
        - View consolidated foreclosure amount (100%) along with breakups
        - Make a single foreclosure payment
        - Track foreclosure status (“In progress”, “Closed”)
        - Receive one closure confirmation
    - **System-level capabilities**
        - Fetch foreclosure amounts independently from DSP LMS and TCL LMS
        - Aggregate amounts at the virtual loan level, LSP will use existing foreclosure details API to fetch the foreclosure details.
        - Post repayment based on the defined repayment allocation logic
        - Trigger un-lien and un-lodgement of collateral once net dues is cleared
        - Un-lien will be handled by DSP
    - **Core happy path**
        - User initiates foreclosure
        - DSP fetches lender-level foreclosure dues
        - User pays consolidated amount
        - DSP settles DSP loan and requests TCL loan closure
        - Both loans marked closed
        - MF collateral unpledged
        - Virtual loan(loan 100%) marked closed
    - **Key edge cases handled**
        - TCL closure delay → loan remains “Foreclosure in progress”
        - Payment success but lender closure pending/Failed
        - MF unpledge failure → ops retry, customer sees no error
        - Lender system downtime
        - Excess handling in case of repayment amount which is not due, like accrued amount repayment will become excess, in case of foreclosure repayment we will require to post the accrued amount to make it due and to avoid the refunds.

---

## **5.  High level s***ystem, user or process flow*

- 
    - Cover the overview of the process or the journey
    - Include error cases or edge cases (Optional)

---

## **6.  Appendix (Optional)**

### Benchmarking:

### User feedback / Calling:

Meeting Notes

- Foreclosure simulation API
- EOD behaviour
- Foreclosure API and its validation
- Accrue interest posting API

Understanding on DRPS

-