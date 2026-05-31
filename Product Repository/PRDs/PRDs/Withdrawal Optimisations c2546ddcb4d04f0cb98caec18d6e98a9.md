# Withdrawal Optimisations

: Ameya Aglawe
Created time: October 8, 2024 11:53 AM
Status: In progress
Last edited: October 17, 2024 4:45 PM

# **What problem are we solving?**

In a 15-day period, 2.84% of the 5130 disbursal requests were rejected, with 1.98% attributed to tech gaps within Volt app. The key problems to address are : 

- Customers see a higher limit on the app and request a bigger amount resulting in failures
- We use a higher limit in our DB which results in withdrawals getting rejected at lender’s end
- Customer raise support tickets and give poor reviews impacting our CSAT and retention
- We face challenges in acquiring new customers due to poor ratings on app
- We are checking the customer’s holding statement which creates issue in updating status

The above problems are faced due to below implantation.

1. When users complete the loan application and the loan account opening is still pending at the lender's end, the dashboard displays the sanctioned limit as available cash. In some cases, the sanctioned limit is set greater than actual DP due to operational adjustments (e.g., margin pledge). Users then request withdrawals of the full available cash (sanction limit). As a result, these withdrawal requests are later rejected when the DP is updated from the lender. 
2. When users complete the loan application and the loan account opening is still pending at the lender's end, and user comes to the manage limit page & taps on view details, then we sync DP/assets with getHoldingData API, which reflects as 0 in the getHoldingData API as the account is not yet opened at lenders end, as we sync our DP with it, DP at our end becomes equal to DP at lender’s end, basis this we mark the credit as active and process the disbursal request, but since the available amount for disbursement is still 0 (as loan account not created at lender’s end) the withdrawal gets rejected. 

---

# **How do we measure success?**

- Reduction in withdrawal rejections from 2.84% to 0.86%.

<aside>
💡

We want to reduce the rejection %age from 0.86% to 0.1% but we are blocked on lender

</aside>

---

# **How are others solving this problem?**

- Most LSPs maintain a limit at their end which is used to validate the request
- Most LSPs check the available limit with lender’s ensuring minimal failures

---

# **What is the solution?**

## Requirements overview (optional)

### User stories / User flow

1. User completes the application 
2. User lands on the dashboard 
3. User sees the available cash in the dashboard **(which is the sanction limit currently)** 
    - UI
        
        ![Screenshot 2024-10-11 at 10.07.40 AM.png](Withdrawal%20Optimisations/Screenshot_2024-10-11_at_10.07.40_AM.png)
        
4. User place a withdrawals request
5. User goes to the Manage limit screen and taps on view details 
    1. Get Holding data API is called and the assets are synced with the lender  (**In this process DP also gets synced with lender and becomes 0 as account is not yet created at lenders end)** 

## Tech Requirements

- **Problem 1 : Showing sanction limit as available cash in the dashboard**
- Solution -  We will show min (sanction limit, DP) as available cash in the dashboard.
- where DP = summation of NAVxLTVxUnitsPledgedf
- **Problem 2 : Syncing DP**
- Solution - We will sync assets via the GetHoldingData API only if the credit status is "APPROVED_NOT_DISBURSED", "ACTIVE", "PENDING_CLOSURE". If credit is not in the 3 mentioned statuses, we will not call (sync assets) the GetHoldingData API.
    - getHoldingData API
        - Request
            
            ```jsx
            [
            {
                "NonPOAHoldingPledge": [
                    {
                        "InputFieldType": "LoanAccountID",
                        "InputFieldValue": "187678",
                        "RequestID": "-1mhwvgrlut2e7--1nunz1vi6yjzy",
                        "UserName": "APIVLT76"
                    }
                ]
            }
            ]
            ```
            
        - Response
            
            ```jsx
            {
                "NonPOAPledgeHoldingData": [
                    {
                        "LoanAccount": "187678",
                        "InputFieldType": "LoanAccountID",
                        "InputFieldValue": "187678",
                        "SecurityKey": "89849",
                        "ScripName": "SBI Contra Direct-G",
                        "ISIN_AMFI": "INF200K01RA0",
                        "AMFI": "119835",
                        "TotalQty": "125.3260",
                        "AllowableQty": "125.3260",
                        "MarketRate": "426.38",
                        "DPofSecurity": "26719.00",
                        "RecordStatus": null,
                        "Remarks": null,
                        "PledgeType": "LIEN",
                        "PledgeFolioDetails": [
                            {
                                "InputFieldValue": "187678",
                                "SecurityKey": "89849",
                                "ScripName": "SBI Contra Direct-G",
                                "ISIN_AMFI": "INF200K01RA0",
                                "AMFI": "119835",
                                "PledgeQty": "125.3260",
                                "Pledge_FolioNo": "38061111",
                                "DPID": null,
                                "ClientID": null,
                                "PledgerName": null,
                                "PledgeeDPId": null,
                                "PledgeeClientId": null
                            }
                        ]
                    },
                    {
                        "LoanAccount": "187678",
                        "InputFieldType": "LoanAccountID",
                        "InputFieldValue": "187678",
                        "SecurityKey": "95989",
                        "ScripName": "HDFC Mid-Cap Opportunities Direct-G",
                        "ISIN_AMFI": "INF179K01XQ0",
                        "AMFI": "118989",
                        "TotalQty": "245.7750",
                        "AllowableQty": "245.7750",
                        "MarketRate": "209.00",
                        "DPofSecurity": "25683.00",
                        "RecordStatus": null,
                        "Remarks": null,
                        "PledgeType": "LIEN",
                        "PledgeFolioDetails": [
                            {
                                "InputFieldValue": "187678",
                                "SecurityKey": "95989",
                                "ScripName": "HDFC Mid-Cap Opportunities Direct-G",
                                "ISIN_AMFI": "INF179K01XQ0",
                                "AMFI": "118989",
                                "PledgeQty": "245.7750",
                                "Pledge_FolioNo": "30743822",
                                "DPID": null,
                                "ClientID": null,
                                "PledgerName": null,
                                "PledgeeDPId": null,
                                "PledgeeClientId": null
                            }
                        ]
                    },
                    {
                        "LoanAccount": "187678",
                        "InputFieldType": "LoanAccountID",
                        "InputFieldValue": "187678",
                        "SecurityKey": "113996",
                        "ScripName": "SBI Multi Asset Allocation Direct-G",
                        "ISIN_AMFI": "INF200K01TZ3",
                        "AMFI": "119843",
                        "TotalQty": "842.0380",
                        "AllowableQty": "842.0380",
                        "MarketRate": "61.94",
                        "DPofSecurity": "26076.00",
                        "RecordStatus": null,
                        "Remarks": null,
                        "PledgeType": "LIEN",
                        "PledgeFolioDetails": [
                            {
                                "InputFieldValue": "187678",
                                "SecurityKey": "113996",
                                "ScripName": "SBI Multi Asset Allocation Direct-G",
                                "ISIN_AMFI": "INF200K01TZ3",
                                "AMFI": "119843",
                                "PledgeQty": "842.0380",
                                "Pledge_FolioNo": "38061111",
                                "DPID": null,
                                "ClientID": null,
                                "PledgerName": null,
                                "PledgeeDPId": null,
                                "PledgeeClientId": null
                            }
                        ]
                    },
                    {
                        "LoanAccount": "187678",
                        "InputFieldType": "LoanAccountID",
                        "InputFieldValue": "187678",
                        "SecurityKey": "125774",
                        "ScripName": "HDFC NIFTY Next 50 Index Direct-G",
                        "ISIN_AMFI": "INF179KC1BQ9",
                        "AMFI": "149288",
                        "TotalQty": "4660.1770",
                        "AllowableQty": "4660.1770",
                        "MarketRate": "17.67",
                        "DPofSecurity": "41168.00",
                        "RecordStatus": null,
                        "Remarks": null,
                        "PledgeType": "LIEN",
                        "PledgeFolioDetails": [
                            {
                                "InputFieldValue": "187678",
                                "SecurityKey": "125774",
                                "ScripName": "HDFC NIFTY Next 50 Index Direct-G",
                                "ISIN_AMFI": "INF179KC1BQ9",
                                "AMFI": "149288",
                                "PledgeQty": "4660.1770",
                                "Pledge_FolioNo": "30743822",
                                "DPID": null,
                                "ClientID": null,
                                "PledgerName": null,
                                "PledgeeDPId": null,
                                "PledgeeClientId": null
                            }
                        ]
                    },
                    {
                        "LoanAccount": "187678",
                        "InputFieldType": "LoanAccountID",
                        "InputFieldValue": "187678",
                        "SecurityKey": "128397",
                        "ScripName": "HDFC NIFTY Smallcap 250 Index Direct-G",
                        "ISIN_AMFI": "INF179KC1GE4",
                        "AMFI": "151727",
                        "TotalQty": "3695.8990",
                        "AllowableQty": "3695.8990",
                        "MarketRate": "19.73",
                        "DPofSecurity": "36465.00",
                        "RecordStatus": null,
                        "Remarks": null,
                        "PledgeType": "LIEN",
                        "PledgeFolioDetails": [
                            {
                                "InputFieldValue": "187678",
                                "SecurityKey": "128397",
                                "ScripName": "HDFC NIFTY Smallcap 250 Index Direct-G",
                                "ISIN_AMFI": "INF179KC1GE4",
                                "AMFI": "151727",
                                "PledgeQty": "3695.8990",
                                "Pledge_FolioNo": "30743822",
                                "DPID": null,
                                "ClientID": null,
                                "PledgerName": null,
                                "PledgeeDPId": null,
                                "PledgeeClientId": null
                            }
                        ]
                    }
                ],
                "status": {
                    "Status": "Success",
                    "Code": "01",
                    "Remarks": ""
                }
            }
            ```
            

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