# Capital gains tax calculator

: Saksham Srivastava
Created time: February 26, 2024 9:40 AM
Status: In progress
Last edited: March 15, 2024 6:49 PM
Owner: Saksham Srivastava
Tasks: Capital gains tax calculator (https://app.notion.com/p/Capital-gains-tax-calculator-4dd246a5559842fcaf9d701b6a9168a7?pvs=21)
Due Date: 08/03/2024

# **What problem are we solving?**

1. Users currently don’t have a resource readily available that helps them calculate and create a consolidated MF capital gains/losses report from all their brokers. 
2. Users also don’t know how much tax they will have to pay on these gains due to complex categorisations of these gains. 
3. MFD users similarly don’t have a resource readily available where they can create a consolidated capital gains statement for their clients.  

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

1. Create a report/statement generator that enables users to download a report that gives them a consolidated understanding of their MF capital gains. 
2. We will also build a summary in UI that gives them approximate understanding of how much tax they will have to pay in different categories of capital gain/losses. 

## Requirements overview (optional)

Requirements 

1. Entry point from the website top nav. (https://app.amplitude.com/analytics/volt-hq/chart/new/f3bf19rh)
    1. Merge the partner and integrate with us, into partner with us and when the user hovers over it, it can expand into - “For Mutual fund distributors” and “App and platform integrations”
    2. Include a new section Calculators, with a tag of “new”. Hovering over this should show “Capital gains tax statement”. For mobile in the hamburger menu this will show as just as “Capital gains tax statement”. 
2. Main report/calculator iframe.
    1. User input
        1. Input fields to enter PAN and mobile number. Subtext: “We need PAN to calculate your Capital gains”.  
        2. Dropdown to select FY. We will give two choices for now, “Current financial year” and “Previous financial year”. Corresponding date range will be shown in UI.
        3. CTA: “Generate statement”. 
    2. Summary output
        1. Heading: “Capital gains statement is here for PAN: KHUPS6329M”. This will have a CTA to edit details.
        2. Dropdown to select: “Current financial year” and “Previous financial year.”
        3. A section which shows what dates the financial year corresponds to.
        4.  There will be two sections of the report. Equity and Non-equity.
            1. Equity
                
                
                |  | Numbers | tooltip | Calculation |
                | --- | --- | --- | --- |
                | Long term capital gain | {Corresponding CG of the user} | For holding period of more than a year on equity focused mutual funds. Upto ₹1 lac per year is tax exempted.  | add all **data.schemeDetails[].longTermWithoutIndexation** where **data.transactionDetails[].assetClass: "EQUITY"** |
                | Tax% | 10% | Excludes cess and surcharges. |  |
                | Short term capital gain | {Corresponding CG of the user} | For holding period of less than a year on equity focused mutual funds. | add all **data.schemeDetails[].shortTerm** where **data.transactionDetails[].assetClass: "EQUITY"** |
                | Tax% | 15% | Excludes cess and surcharges. |  |
                |  |  |  |  |
                |  |  |  |  |
            2. Non-equity
            
            |  | Numbers | tooltip |  |
            | --- | --- | --- | --- |
            | Long term capital gain (with indexation) | {Corresponding CG of the user} | For holding period of more than 3 years on debt (units purchased before 1st Apr 2023) or debt oriented hybrid funds.  | add all **data.schemeDetails[].longTermWithIndexation** where **data.transactionDetails[].assetClass ≠ "EQUITY"** |
            | Tax% | 20% | Indexation benefits allow investors to adjust the cost of investment for inflation with the help of a price index.  |  |
            | Capital gains taxed as per income tax slab rates | {Corresponding CG of the user} | 1. Holding period of less than 3 years on debt (units purchased before 1st Apr 2023) or debt oriented hybrid funds. 
            2. Regardless of holding period on debt mutual fund units bought after 1st Apr 2023.  | add all **data.schemeDetails[].shortTerm** and **data.schemeDetails[].longTermWithoutIndexation** where **data.transactionDetails[].assetClass ≠ "EQUITY"** |
    3. Report generation:
        1. Excel CGS report to be generated. Mapping from JSON response is shared here:  
        
        [cgs_sample.xlsx](Capital%20gains%20tax%20calculator/cgs_sample.xlsx)
        
        1. Sample CGS report generated from MFC is here: 
        
        [MFC CGS.xlsx](Capital%20gains%20tax%20calculator/MFC_CGS.xlsx)
        
        1. Naming of the statement: 
    4. Scenarios of output:
        1. Both equity and non equity investments: Show both the sections of the report completely even when one row is zero. 
        2. Either equity or Non-equity: Show the relevant section with details and non relevant section with “You have no capital gains on non-equity mutual funds in financial year 2023-24.”
        3. No capital gains: Show text: “You have no capital gains on mutual funds in financial year 2023-24.”
3. Landing page.
    1. FAQs section. Heading “FAQs on capital gains statement”. 
    
    [FAQs on CGS landing page](Capital%20gains%20tax%20calculator/FAQs%20on%20CGS%20landing%20page%2059d1ff432a6a4b51bf79e0a707328bd1.md)
    
4. Data use cases:
    1. A lead should be created for a user who generates the report. CGS JSON will be stored against it. 
    2. In case of lead generated from partner dashboard the partner should be associated with the lead.
    3. Lead should have the following data
        1. PAN
        2. Number
        3. CGS JSON
        4. CGS year
        5. MFD partner (NA If not applicable)
    4. Once the lead is created an activity should be posted to LSQ with the above details. 
    5. Operations team should be able to view the CGS statement of the user with PAN and Phone number in admin dashboard. 

## User stories / User flow

UI

1. Users should be able to access the landing page for CGS from the main website landing page.
2. Users should be able to enter PAN, mobile and financial year to generate the CGS on the landing page.
3. Users should see a section on the landing page which educates them about the benefits of generating CGS from Volt.
4. Users should see a section on homepage that answers their FAQs regarding how to use the CGS and how taxation on mutual funds work. 
5. Users should be able to enter OTP received from MFC (generated after PAN, Phone and FY input).
6. Users should see a loading screen while we are fetching response from MFC and generating the CGS.
7. Users should see a summary of capital gains on equity and non-equity mutual funds. This summary will also include the tax% that the user has to pay in all taxation cases. 
8. Users should see tooltips against all the row items that need explanation. 
9. Users should be able to edit details on the summary page, this will take them back to the input form with pre-filled data. 
10. Users should be able to change the financial year (in a dropdown) this will retrigger the OTP for the user and they should be able to enter it. Users should see the date range corresponding to the FY selected. Current financial year will be from 1st April 2023 to {TODAY}. 
11. Users should see a section which prompts user to download the detailed report. This section will also educate the user what type of detailed information they can expect from the CGS report.

Report generation + Summary calculations

1. Users should see the summary section, which is calculated from the CGS JSON received from MFC.
2. Users should be able to download the detailed report. 

## Requirements

---

# **Design**

Figma link: [https://www.figma.com/file/d1yj53GJC9DCA78Fh0tQeg/Marketing-(investor)?type=design&node-id=993-5193&mode=design&t=KElx2L8WIzye03VF-4](https://www.figma.com/file/d1yj53GJC9DCA78Fh0tQeg/Marketing-(investor)?type=design&node-id=993-5193&mode=design&t=KElx2L8WIzye03VF-4)

---

# **Analytics**

Amplitude events:

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
    - [ ]  Partner dashboard design
    - [ ]  Name of the statement
    - [ ]  Entry point finalise
    - [ ]  Copy everywhere finalise
    - [ ]  FAQ copy finalise
    
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

### FAQs in CGS page

![Untitled](Capital%20gains%20tax%20calculator/Untitled.png)

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes

- Meeting with Ankit - 24th Feb
    - API Docs don’t contain the meaning of various parameters.
    - Sell and purchase shared in the same response, check the API response properly.
- API Understanding use case, key user needs, and benchmarking
    - UAT response for Lalit’s PAN:
        
        "reqId": "2522008-471678192",
        "pan": "BBKPB6083L",
        "pekrn": "",
        "email": "",
        "mobile": "9820167354",
        "fromDate": "01-Apr-2022",
        "toDate": "31-Mar-2023",
        "data": [
        {
        "transactionDetails": [
        {
        "amc": "H",
        "amcName": "MFHMF Test Fund",
        "folio": "17085094",
        "schemeName": "INF179K01608/HDFC Flexi Cap Fund - Regular Plan - Growth ",
        "desc": "Purchase",
        "date": "17-Jul-2019",
        "units": "1034.894",
        "amount": "1000000.000",
        "price": "966.292",
        "stt": 10,
        "desc_1": "Redemption ",
        "date_1": "24-May-2022",
        "purhUnit": "1463.407",
        "redUnits": "1034.894",
        "unitCost": "683.337",
        "indexedCost": "749.543",
        "grandfatheredUnits(As On 31/01/2018)": "0.000",
        "grandfatheredNAV(As On 31/01/2018)": "0.000",
        "grandfatheredMarketValue(As On 31/01/2018 )": "0.000",
        "shortTerm": "0.000",
        "taxPerc": "0.000",
        "taxDeduct": "0.000",
        "taxSurcharge": "0.000",
        "assetClass": "EQUITY",
        "name": "Value Research",
        "status": "Individual",
        "pan": "BBKPB6083L",
        "guardianPan": "BBKPB6083L",
        "longTermWithoutIndex": "0.000",
        "longTermWithIndex": "224312.591"
        }
        ],
        "summaryDetails": [
        {
        "Sno": "1",
        "summaryOfCapitalGains": "Full Value Consideration",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        },
        {
        "Sno": "2",
        "summaryOfCapitalGains": "Cost of Acquisition",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        },
        {
        "Sno": "3",
        "summaryOfCapitalGains": "Short Term Capital Gain/Loss",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        },
        {
        "Sno": "4",
        "summaryOfCapitalGains": "Fair Market Value Of capital asset as per section 55(2)(ac)",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        },
        {
        "Sno": "5",
        "summaryOfCapitalGains": "Full Value Consideration",
        "01/04 to 15/06": "1000000.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "1000000.000"
        },
        {
        "Sno": "6",
        "summaryOfCapitalGains": "Cost of Acquisition",
        "01/04 to 15/06": "775697.203",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "775697.203"
        },
        {
        "Sno": "7",
        "summaryOfCapitalGains": "LongTermWithIndex-CapitalGain/Loss",
        "01/04 to 15/06": "224312.591",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "224312.591"
        },
        {
        "Sno": "8",
        "summaryOfCapitalGains": "Fair Market Value Of capital asset as per section 55(2)(ac)",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        },
        {
        "Sno": "9",
        "summaryOfCapitalGains": "Full Value Consideration",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        },
        {
        "Sno": "10",
        "summaryOfCapitalGains": "Cost of Acquisition",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        },
        {
        "Sno": "11",
        "summaryOfCapitalGains": "LongTermWithOutIndex-CapitalGain/Loss",
        "01/04 to 15/06": "0.000",
        "16/06 to 15/09": "0.000",
        "16/09 to 15/12": "0.000",
        "16/12 to 15/03": "0.000",
        "16/03 to 31/03": "0.000",
        "total": "0.000"
        }
        ],
        "schemeDetails": [
        {
        "schemeName(Redeem/Switchout)": "INF179K01608/HDFC Flexi Cap Fund - Regular Plan - Growth Equity(G)",
        "totalCount": 1,
        "totalAmount": "1000000.000",
        "totalCost": "707181.361",
        "indexedCost": "749.543",
        "marketValue( As On 31/01/2018)": "0.000",
        "shortTerm": "0.000",
        "longTermWithIndex": "224312.591",
        "longTermWithoutIndexation": "0.000",
        "tds": "0.000"
        }
        ],
        "staticDetails": [
        {
        "invName": "Value Research",
        "address1": "Address1 of Folio: 17085094",
        "address2": "Address2 of Folio: 17085094",
        "address3": "Address3 of Folio: 17085094",
        "city": "Mumbai",
        "state": "MA",
        "pinCode": "400053",
        "pan": "BBKPB6083L"
        }
        ]
        }
        ],
        "Return_Code": 400,
        "Return_Message": "******No data found***"
        }
        
    - Understanding
        - The API gives transaction level data, where in each transaction purchase, and redemption(switchout) is shared in one response.
        - The response can be segregated into three section:
            - Summary: Gives an overall understanding of STCG and LTCG.
            - Scheme level summary: Gives an scheme level understanding of STCG and LTCG.
            - Transaction details: This in one section gives purchase and redemption (or Switchout) for a particular fund. All the purchases and redemptions linked to a folio are shown here. Subsequent corresponding description and dates are as desc_1, date_1, etc. The sample response is of one purchase and redemption, structure of SIPs with multiple purchase and redemption will be harder to understand. Handling this structure will be a pain.
        - Below is from the MFD platform recording. The below information is shown by the “transactionDetails” section of the API response.
        
        ![Untitled](Capital%20gains%20tax%20calculator/Untitled%201.png)
        
        ![Untitled](Capital%20gains%20tax%20calculator/Untitled%202.png)
        
        - transactionDetails vs what it means: Apart from the obvious, stating what the other params mean in the response.
        
        | param | what it means | questions |
        | --- | --- | --- |
        | amount | amount redeemed (price*units) | How will this look like when multiple redemptions purchases? |
        | units | total units redeemed | How will this look like when multiple redemptions purchases? |
        | price | price of unit redeemed | How will this look like when multiple redemptions purchases? |
        | purhUnit | # units purchased  | How will this look like when multiple purchases? |
        | redUnits | # units redeemed | How will this look like when multiple redemptions? |
        | unitCost | actual cost per unit when purchased. Cost of acquisition.  | How will this look like when multiple purchases? |
        | indexedCost | inflation adjusted cost of unit when purchased. Indexed cost of acquisition. [CII for the year of sale ÷ CII for the year of purchase (or CII for 2001–02, whichever is earliest)] x unitCost | How will this look like when multiple purchases? |
        | grandfatheredUnits(As On 31/01/2018) | units that will be considered grandfathered on cut off date |  |
        | grandfatheredNAV(As On 31/01/2018) | NAV of grandfathered unit on cutoff date |  |
        | grandfatheredMarketValue(As On 31/01/2018 ) | = [grandfatheredUnits * grandfatheredNAV] |  |
        | taxPerc, taxDeduct, taxSurcharge |  | Are these for STCG only? How will we handle all the cases where taxation is marginal |
        | assetClass | Equity, hybrid or Debt | Want to check cases of other two.  |
        | longTermWithoutIndex |  | Which one to show |
        | longTermWithIndex |  | Which one to show |
    - Cases to check
        
        Cases we want to check responses for:
        
        1. Debt: Sell units are a mix of debt bought before and after the 1st April 2023. 
        2. Debt: Funds that potentially are considered hybrid post 1st April 2023.
        3. The summary still shows Short term and long term, but for debt long/short doesn’t matter anymore. How is that counted still?
    - Excel mapping, shared by Dhruv.
        
        [cgs_sample.xlsx](Capital%20gains%20tax%20calculator/cgs_sample%201.xlsx)
        
    - Use case: An understanding from Yogendra (Bharat connected) + YT comments
        - There are two major buckets of use cases:
            - Before selling a mutual fund: Understanding how much tax the user will have to pay in case they sell their mutual funds, understand what is the category of a particular MF
            - After selling a mutual fund: Getting a report to send to their CA(Very high for our TG, they ask their MFD for this report and sent it to their CA), understanding how to fill ITR themselves (user need hand holding for this)
        - In debt cases, the taxation is marginal. How we help user in that case?
        - We can use this data to show them savings: This can be the difference of STCG and LTCG or just the tax amount, some sort of tax regret calculation.
- MF Taxation understanding:
    
    ![Untitled](Capital%20gains%20tax%20calculator/Untitled%203.png)
    
    - Grandfathering: The process of excluding current programs, policies, or advantages from new rules or adjustments to the budget is called grandfathering in budgeting. In his 2018-2019 Union Budget Speech, the then Finance Minister, Mr. Arun Jaitley presented the new provisions related to long-term capital gains (LTCG) tax. In the budget speech, he stated that the government would tax long-term capital gains exceeding 1 lakh rupees at a rate of 10% without providing indexation benefits. However, he added that all gains up to 31 January 2018 would be ‘grandfathered’.
    
    ![Untitled](Capital%20gains%20tax%20calculator/Untitled%204.png)
    
    - Indexation from Debt funds was removed on 1st April 2023, this will be applicable to funds bought after this date, unlike the grandfathering clause.
    - Tax is calculated on MFs in FIFO basis, this is important question for people who do SIP.
    - STT: securities transaction tax
    - Long-term capital loss will only be adjusted towards long-term capital gains. However, **a short-term capital loss can be set off against both long-term capital gains and short-term capital gain**
    - Sources:
        - [https://www.etmoney.com/learn/mutual-funds/taxation-in-mutual-funds/#:~:text=Taxation on Debt Funds&text=Hence%2C any types of gains,April 2023 are taxed differently](https://www.etmoney.com/learn/mutual-funds/taxation-in-mutual-funds/#:~:text=Taxation%20on%20Debt%20Funds&text=Hence%2C%20any%20types%20of%20gains,April%202023%20are%20taxed%20differently).
        - [https://www.tataaia.com/blogs/life-insurance/grandfathering-rules-and-provisions.html#:~:text=In simple terms%2C investments made,at a prior%2C lower rate](https://www.tataaia.com/blogs/life-insurance/grandfathering-rules-and-provisions.html#:~:text=In%20simple%20terms%2C%20investments%20made,at%20a%20prior%2C%20lower%20rate).
        - [https://www.youtube.com/watch?v=lnMUAJOgBoM&ab_channel=YadnyaInvestmentAcademy](https://www.youtube.com/watch?v=lnMUAJOgBoM&ab_channel=YadnyaInvestmentAcademy)
        - [https://www.youtube.com/watch?v=CqCGr4G73fw&ab_channel=FinancialPlanningAcademy(FPA)](https://www.youtube.com/watch?v=CqCGr4G73fw&ab_channel=FinancialPlanningAcademy%28FPA%29)
        - [https://margcompusoft.com/m/section-55-2-ac-of-the-income-tax-act/#:~:text=Valuation of asset%3A The value,previous owner of the asset](https://margcompusoft.com/m/section-55-2-ac-of-the-income-tax-act/#:~:text=Valuation%20of%20asset%3A%20The%20value,previous%20owner%20of%20the%20asset).
- UI/UX
    - User flow:
        
        User visits the CGS landing page → User enters PAN → User enters mobile number → User enters OTP → User sees the summary data for the current financial year by default, user can change the FY from a dropdown → User sees fund level data and all transactions → User downloads/shares excel, PDF of the report 
        
    - Use cases to solve for:
        - User when comes to the website should be able to navigate to the calculator. It should attract attention but not away from check eligibility.
        - User should understand that is only for mutual funds and not for stocks or other assets.
        - User should understand that this not a calculator but a report.
        - User should know the benefits of fetching CGS from Volt.
            - Completely free!
            - One stop solution. Not broker specific.
            - Fast and accurate!
            - Detailed folio/transaction level understanding
            - In partnership with/powered by MF central
        - User should be able to select for which financial year do they want to check. This will be done along with date ranges
        - User should see a summary of Capital gains tax
        - User should see a detailed scheme wise view of the CG
        - Use should understand what terms like grandfathered unit etc mean.
        - User should have information on how the CG is calculated on mutual funds.
        - User should have a basic understanding on how to use the Volt CGS report.
    - Design requirement:
        - Changes in top nav on the website to include a new section for resources. This will house blogs and calculators.
        - Landing page for calculator [https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/ae4a091b4](https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/ae4a091b4)
            - Main calculator input fields. This will be in the interface where user interacts with our calculator.
            - 3 USP of volt CGS calculator. This will be outside the calculator/report interface.
            - FAQ section. This will be outside the calculator/report interface.
        - Summary page [https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/a38739487](https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/a38739487)
        - Scheme level page
        - Transaction level page
        - Report PDF design?
    - 
    
    [Capital gains statements UI requirements for Yusuf](Capital%20gains%20tax%20calculator/Capital%20gains%20statements%20UI%20requirements%20for%20Yusuf%202b411bb216db4be98e46b5e44a562bb0.md)
    
- Discussion with Lalit - 28th Feb
    - Use case of report is strong. Could not validate the use case of a calculator.
    - API is giving gains and not tax
    - We can take what is the tax slab for the user and calculate the tax accordingly.
- Other resources
    
    [Saksham CGS report](Capital%20gains%20tax%20calculator/cgs_detailed_report_2024_02_26_094745.xlsx)
    
    [UI benchmarking for CGS](Capital%20gains%20tax%20calculator/UI%20benchmarking%20for%20CGS%208d90ec21047b442e961273e9c802f710.md)
    
    https://drive.google.com/file/d/1T9FLeS-lJcM2XSRfqLCz0wC7sHKNg8ZK/view?usp=drive_link : Capital gains - MFD platform recording
    
    [Capital gains IFA Now - YT Demo SS](Capital%20gains%20tax%20calculator/Screenshot_2024-02-26_at_12.32.55_PM.png)
    
    [Capital gains - MFC document download page](Capital%20gains%20tax%20calculator/Screenshot_2024-02-26_at_9.46.36_AM.png)
    
    https://drive.google.com/file/d/1RVDIhAQTJyX-z8GyEOlT3oDTzlgvL3nh/view?usp=drive_link : MFC CGS API Doc
    
    [https://www.youtube.com/watch?v=SjJ8xYRcRaw&ab_channel=CARachanaPhadkeRanade](https://www.youtube.com/watch?v=SjJ8xYRcRaw&ab_channel=CARachanaPhadkeRanade): Grandfathering explanation
    
    [Saksham CAMS CGS.pdf](Capital%20gains%20tax%20calculator/Saksham_CAMS_CGS.pdf)
    

---