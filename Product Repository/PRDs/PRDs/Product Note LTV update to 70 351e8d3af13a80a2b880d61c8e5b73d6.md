# Product Note : LTV update to 70

: Ameya Aglawe
Created time: April 29, 2026 11:53 AM
Status: Not started
Last edited: May 12, 2026 10:39 AM

---

# **1. Problem Statement**

---

## **2. Objective**

---

## **3. Scope**

---

- LTV update task
    - Finflux
        - Multiple approved script management
        - Validations
        - Any sort of handling
    - Fenix
        - Multiple approved scripts handling
        - Risk and RMS validations required
        - Impact of all collateral transactions
            - Collateral addition
            - Collateral removal
            - Collateral invocation
        - Shortfall handling
        - Communications and statements
        - ROI auditing
        - Current offer visibility for NBFC and LSPs
    - Volt
        - Journey
            - Enhancement (Fetch/Pledge/Offer/Agreement)
            - Nudges
        - B2B2C & B2C
            - PF/ROI changes
                - Journey
                - Admin actions (PF increase to work out of the box)
            - Payout
- Scope reduction
    - Loan offer
    - PF/ROI
    - Contract level
    - Volt UI

---

- Nudge
- Current limit
- Updated Limit
- Current ROI
- New ROI
- LTV update charges
- KFS/Agreement

- Task name - Service request approval
    - Left panel
        - Request details
            - Request ID
            - Service request type : Limit enhancement
            - Requested on
            - Current collateral limit
            - Additional collateral limit
            - Updated collateral limit
            - Limit enhancement charges
            - AMC charges
            - Substatus
            - Maker name
            - Maker remark
            - Maker created on
        - Collateral details
            - ISIN
            - Asset type
            - Collateral sub type
            - Folio
            - Value
            - Existing limit
            - New limit
    - Right panel
        - Client details
        - Loan details
            - With loan contract
        - Transactions
        - Collaterals
            - Collaterals with details (LTV)
        - Loan kit
            - KFS
            - Agreement
- Generate offer what happens?
    - Request - FXLAN (with collateral details)
    - Response
        - Funds with higher LTV
        - Limit enhancement charge ranges
        - AMC charge ranges
        - ROI ranges
- Accept offer
    - Request - Fund with LTV, charges & ROI details
    - Response - Offer ID

- Service request and collateral addition in parallel, what validations to happen