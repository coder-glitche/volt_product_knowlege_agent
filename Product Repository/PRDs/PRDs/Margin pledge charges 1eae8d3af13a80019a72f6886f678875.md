# Margin pledge charges

: Ameya Aglawe
Created time: May 5, 2025 8:45 AM
Status: Pending Review
Last edited: June 5, 2025 7:19 PM

# **What problem are we solving?**

- Currently, DSP Finance offers a maximum sanction limit of ₹2,00,00,000, allowing users to pledge collaterals post-account opening up to this limit (calculated as NAV × LTV × Units) to access credit.
- However, this leads to cost implications such as lien marking charges, ongoing tech maintenance, and operational overheads, which are not being recovered from users today. To address this and improve monetisation, we plan to introduce pledge invocation charges, applicable when users pledge additional securities to increase their credit limit.
- As of April 30, DSP Finance has processed 3,794 margin pledge requests without applying applicable charges, resulting in an estimated monthly revenue loss of approximately ₹5 lakhs.

---

# **How do we measure success?**

- Margin pledge charges contributing ₹5 lakhs to monthly revenue for DSP Finance
- Number of margin pledge requests as a percentage of loan account
- Add in more detail

---

# **How are others solving this problem?**

---

# **What is the solution?**

We will be applying margin pledge charges (Additional pledge charges) on the user’s loan account. Margin pledge charges will be applied. The same will be added in the product construct.

## User stories / User flow

- Margin Pledge Initiation
    - The user initiates a margin pledge request via the LSPs interface.
- Pledge Execution via DSP’s wrapper APIs
    - The LSP interface integrates with DSP’s wrapper APIs to:
        - Fetch mutual fund holdings.
        - Execute the pledge request for selected funds.
- Add Collateral Request Triggered by LSP
    - Upon successful pledge confirmation:
        - DSP receives the fund pledge information via the wrapper APIs.
        - LSP then triggers an Add Collateral request.
- Margin Pledge Charges Applied
    - Margin pledge charges are linked to the Add Collateral request.
    - Once the Add Collateral request is successfully processed:
        - In non-STP and STP flows, the margin pledge charges are posted to the customer’s loan account.
- User Communication
    - After charge posting:
        - Email comms are sent to the user, confirming that the margin pledge charges are posted

## Requirements

---

- Charge amount :
    - Additional pledge charges charges type (percentage or absolute) and the corresponding values (what percentage or what value) should be configurable at a sourcing channel level (product construct)
    - GST of 18% will be applied on top of the charge amount applied to the user’s loan account
    - For now the margin pledge charge amount will be the one mentioned in the agreement
    - charge_identifier of margin pledge charges will be MARGIN_PLEDGE_CHARGES
    - The margin pledge charges will be picked up from the loan contract
- Charge application :
    - Additional pledge charges will be applied on user initiated requests, that is for manual lodgements requests raised by the operations team, there will be no additional pledge charge application charge applied on the user’s loan account
    - Note : The backlog of margin pledges will be addressed via the charge application script. (for the margin pledges which have been completed before the deployment of this feature)
    - “The system will support LSP-level configuration to determine whether marginPledgeCharges should be accepted within the loan contract for each LSP.
- Charge collection :
    - Additional pledge charges will be collected via repayments made to the user’s loan account according to the predefined apportionment strategy -
        - Interest overdue → Charges overdue → Interest due → Charges due → Principal → Excess
- Communication & visibility
    - To DSP Ops
        - For N-STP lodgements : Under the request details section in add collateral task
            
            ![Screenshot 2025-05-05 at 4.59.26 PM.png](Margin%20pledge%20charges%201eae-8875/Screenshot_2025-05-05_at_4.59.26_PM.png)
            
        - For all lodgements (N-STP/STP) : Loan account → Holding details → Collateral transaction → Tap on 3 dot button → View addition detail → (Margin pledge charges, Request remarks, Completed on)
            
            ![Screenshot 2025-05-09 at 4.39.14 PM.png](Margin%20pledge%20charges%201eae-8875/Screenshot_2025-05-09_at_4.39.14_PM.png)
            
    - To LSPs
        - Pre facto
            - Description : We will provide an API to the LSPs to get a latest due charges as of latest timestamp (when the API is hit)
            - Request
                
                ```jsx
                GET /api/loan/fees-and-charges?loanAccountNumber=LN12345678
                ```
                
            - Response
                
                ```jsx
                {
                  "processingFee": {
                    "amount": "299.00",
                    "currency": "INR"
                  },
                  "marginPledgeCharge": {
                    "amount": "100.00",
                    "currency": "INR"
                  },
                  "pledgeInvocationCharge": {
                    "amount": "150.00",
                    "currency": "INR"
                  },
                  "dishonourCharge": {
                    "amount": "250.00",
                    "currency": "INR"
                  },
                  "effectiveTimestamp": "2025-05-09T10:30:00Z"
                }
                
                ```
                
        - Post facto
            - Description : We will provide add an additional field in the add_collateral API response which will mention the marginPledgeCharges applied with the add_collateral request (the value of the field will be 0 if no marginPledgeCharges are applied)
            - Add collateral API response
                
                ```jsx
                {
                  "fenixLoanAccountId": "FXLAN48398934",
                  "processingType": "DIGITAL",
                  "requestSource": "SYSTEM",
                  "associatedCollaterals": [
                    {
                      "isin": "INF209K01BT5",
                      "folio": "12345434",
                      "camsLienMarkingNumber": "3190117804",
                      "camsLienRefNumber": "TLGskdgtR6",
                      "kfinSessionId": null,
                      "kfinIhno": null,
                      "kfinLienRefNumber": null,
                      "modeOfHolding": "SINGLE_HOLDING",
                      "units": 100,
                      "overriddenLTV": null,
                      "ownersClientId": [
                        "FXCID52125727"
                      ],
                      "status": "LODGED",
                      "collateralRepository": "CAMS",
                      "collateralType": "MUTUAL_FUNDS",
                      "collateralSubType": "EQUITY",
                      "statusNotes": "LODGEMENT_SUCCESS"
                    }
                  ],
                  "status": "SUCCESS",
                  "associatedCharges": 
                		  {
                			  "marginPledgeCharge": "799",
                  }
                  "statusNotes": "Collateral lodged successfully.",
                  "makerNotes": null,
                  "requestedOn": 1731174364417,
                  "lastUpdatedOn": 1731174377988,
                  "completedOn": 1731174377986,
                  "addCollateralsRequestId": "ACRID2397966669"
                }
                ```
                
    - DSP customers (not in current scope)
        - Existing margin pledges
            - Template ID : d-9d06163cf44e4defb71eebd2bb8d05a4
            - Template variables
            
            ```jsx
            {
                "date":"24-10-2024",
                 "clientId":"FXCID453242",
                 "lan":"FXLAN3453443",
                 "customerName":"Vaibhav Arora",
                 "margin_pledge_charges":"33",
                 "supportEmail":"support@dspfin.com",
                 "supportNumber":"+91 96117 49097",
                  "rows": [
               
                { "folio": "2423432", "isin": "ISIN24324", "schemeName": "HDFC Smart Equity", "quantity": "45.678" , "value": "₹500.65"},
                { "folio": "2423432", "isin": "ISIN24324", "schemeName": "HDFC Smart Equity", "quantity": "45.678" , "value": "₹500.65"},
                { "folio": "2423432", "isin": "ISIN24324", "schemeName": "HDFC Smart Equity", "quantity": "45.678" , "value": "₹500.65"},
                { "folio": "2423432", "isin": "ISIN24324", "schemeName": "HDFC Smart Equity", "quantity": "45.678" , "value": "₹500.65"},
                { "folio": "2423432", "isin": "ISIN24324", "schemeName": "HDFC Smart Equity", "quantity": "45.678" , "value": "₹500.65"}
              ]
                
            }
            ```
            
            - Trigger event : Once margin pledge charges are posted in the user’s loan account
            - This would be a one time email communication for users who have done margin pledging, if user has done multiple margin pledges then we would communicate the total amount of margin pledge charges which have been posted
        - Upcoming margin pledges
            - Email communications will be triggered once the margin pledge charges are posted
                - Template ID : d-83caec3d165f4f709980abdc8b6e42f3
                - Trigger event : Once margin pledge charges are posted in the user’s loan account
- **Push LSPs to raise a single lodgement request - What to do here? - Ask Keyur to raise this requirement to Groww**

# **Design**

---

# **Analytics**

---

- Number of additional pledges post loan account creation
- Number of additional pledge charges posted to loan account

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

- Currenltly in margin pledge flow opportunity id is being pushed and not loan account
- What if LSP sends a lodgement request separately for CAMS & Kfin?
- Capability to skip, add, waive margin pledge charges - not required as of now
- Questions -
    - What should be the amount? Agreement
    - Will a checker task be created for all margin pledge linked add collateral request? Should a different task be created for charge approval or it can be clubbed with the lodgement?
    - Enhancement linked or add collateral linked
        - If add collateral based flow is done, communication about charges to LSP is required? Yes, webhook can be sent, can be informed in lodgement response
        - What we can’t take is customer is willing to pay the charge? - Good to have
- Questions -
    - Will the charges be knocked off from following withdrawal?

- Add collateral request API based how to communicate to LSP? In the API response of add collateral
- Store the charges
- Get applicable charges to a loan account
    - All types of charges
- Holding → add collateral request → transaction
- Once opportunity is complete it should be closed, pledge (margin pledge) should be then linked to FXLAN & not opportunity
- Will GST be applicable? Yes

- Mail Adarsh on requirement - Done
    - JV & Finflux
- Pre facto and post facto data - Done (just close whether pledge_invocation & security_invocation charges are same or not)
- **Push LSPs to raise a single lodgement request - What to do here?**
- Make the charge input from LSPs configurable - Done
- Two touch points command centre
    - add collateral request - Done
    - holding details - Done

- Finflux
    - Event
        - Workflow : add collateral
            - How would we differentiate between a normal add collateral & bulk lodgement?
        - Trigger : 2nd successful add collateral request for a loan account
    - Charge Code