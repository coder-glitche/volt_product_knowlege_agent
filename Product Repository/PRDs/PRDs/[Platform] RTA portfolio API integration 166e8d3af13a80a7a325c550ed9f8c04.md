# [Platform] RTA portfolio API integration

: Vaibhav Arora
Created time: December 24, 2024 8:57 AM
Status: Done
Last edited: August 25, 2025 8:02 PM
Owner: Vaibhav Arora

# **What problem are we solving?**

As an NBFC that offers loans against mutual fund, we have the capability to let the user fetch their securities, select eligible funds and then allowing them to pledge the corresponding securities in the name of the NBFC. 

This allows the NBFC to give the corresponding limit to the user in return, which they can then use for a myriad of use cases.

Since mutual funds (now) are a digital security, and only the pledge (contract between NBFC and the investor) there are potential collateral/potential risks that can arise between the user pledging/invoking/revoking the securities and the NBFC handling them to give the user the corresponding drawing power.

<aside>
💡

Collateral risk: If securities more than what were pledged by the user in the name of the NBFC are lodged, user will be given additional drawing power corresponding to the securities and will accordingly be able to withdraw a higher amount

This introduces financial risk in recovery scenarios as the NBFC will not be able to recover the outstanding amounts by liquidating the corresponding securities in a scenario of default/shortfall

</aside>

<aside>
💡

Operational risk: If securities less than what were pledged (ISIN + Folio + Lien marking number) are lodged in the user’s loan account. We will not be able to lodge the additional (pending) securities again due to a global dedupe. It will also introduce compliance implications as RBI directs REs to un-pledge all securities within a span of 30 days (if they are pledged in the name of the entity but not attached to the loan account)

</aside>

<aside>
💡

User experience: If securities that were unlodged and were not actually unmarked for the user, it can ruin the experience of the user as their DP would get reduced while they will also not be able to redeem their holdings (most of these scenarios are time sensitive for the user)

</aside>

---

# **How do we measure success?**

This is a collateral risk problem statement, any failure here opens up financial risk for the organisation and hence is important to solve for, following are the metrics that should be tracked.

- Number of lodgements where lodged units ≠ pledged units (Higher introduces financial risk, lower introduces operational risk)
- Number of revocations failed due to unit mismatch (more units were unpledged than what was

---

# **How are others solving this problem?**

- BFL is integrated with the lien status API which gives transaction level information (not live information) and have an approval mechanism where the operations team validates lodgement and rejects if not found pledged in the NBFC transaction report
- TCL uses a T+1 reconciliation mechanism and limits the user’s withdrawal to 10,00,000 for STP to control risk

---

# **What is the solution?**

We will be integrating with portfolio APIs of the RTAs for three core collateral transactions in our system to validate the requests synchronously.

- Lodgement
- Revocation
- Invocation

The APIs give response at a combination of an ISIN + Folio + Lien marking number

KFIN Request body:

```json
{
"PortfolioLienRequest": {
"InvPan": "AECPC9871K",
"RequestID": "5000061609",
"AgentCode": "ANJ4718979"
}
}
```

KFIN API (Sample response):

```json
{
    "Dtinformation": [
        {
            "Return_Code": 0,
            "Return_Msg": "Success"
        }
    ],
    "DtData": [
        {
            "RequestID": "200003152175",
            "AgentCode": "ATE4719997",
            "mode": "Pledged",
            "InvestorPAN": "CLFPA9890J",
            "InvestorName": "Vaibhav Arora",
            "InvestorMobile": "9818794003",
            "InvestorEmail": "vaibhavarora144@gmail.com",
            "LenderName": "DSP Finance Private Limited",
            "LienReferenceNumber": 239329463,
            "AmcCode": "117",
            "FolioNo": "79970716793",
            "scheme": "MC",
            "Pln": "RG",
            "SchemeCode": "MCRG",
            "SchemeName": "Mirae Asset Midcap Fund  Regular Plan",
            "ISIN": "INF769K01EY2",
            "AssetCategory": "EQUITY",
            "AssetSubCategory": "EQUITY",
            "LienMarkedUnits": 211.919,
            "LienAmount": "7705.375",
            "CurrentUnits": 211.919,
            "CurrentNAV": 36.36,
            "CurrentValue": "7705.375",
            "ihno": 239329463,
            "KfinRefno": "3234898",
            "AgentCode1": "ATE4719997"
        },
        {
            "RequestID": "200003152175",
            "AgentCode": "ATE4719997",
            "mode": "Pledged",
            "InvestorPAN": "CLFPA9890J",
            "InvestorName": "Vaibhav Arora",
            "InvestorMobile": "9818794003",
            "InvestorEmail": "vaibhavarora144@gmail.com",
            "LenderName": "DSP Finance Private Limited",
            "LienReferenceNumber": 431895940,
            "AmcCode": "118",
            "FolioNo": "91019060043",
            "scheme": "SC",
            "Pln": "RG",
            "SchemeCode": "SCRG",
            "SchemeName": "Edelweiss Small Cap Fund  Regular Plan Growth",
            "ISIN": "INF754K01JJ4",
            "AssetCategory": "EQUITY",
            "AssetSubCategory": "EQUITY FUND",
            "LienMarkedUnits": 138.237,
            "LienAmount": "6455.668",
            "CurrentUnits": 138.237,
            "CurrentNAV": 46.7,
            "CurrentValue": "6455.668",
            "ihno": 431895940,
            "KfinRefno": "3234898",
            "AgentCode1": "ATE4719997"
        },
        {
            "RequestID": "200003152175",
            "AgentCode": "ATE4719997",
            "mode": "Pledged",
            "InvestorPAN": "CLFPA9890J",
            "InvestorName": "Vaibhav Arora",
            "InvestorMobile": "9818794003",
            "InvestorEmail": "vaibhavarora144@gmail.com",
            "LenderName": "DSP Finance Private Limited",
            "LienReferenceNumber": 289439717,
            "AmcCode": "128",
            "FolioNo": "910111587585",
            "scheme": "SC",
            "Pln": "DG",
            "SchemeCode": "SCDG",
            "SchemeName": "Axis Small Cap Fund  Direct Growth",
            "ISIN": "INF846K01K35",
            "AssetCategory": "EQUITY",
            "AssetSubCategory": "Equity",
            "LienMarkedUnits": 441.216,
            "LienAmount": "55734.405",
            "CurrentUnits": 801.248,
            "CurrentNAV": 126.32,
            "CurrentValue": "101213.647",
            "ihno": 289439717,
            "KfinRefno": "3411384",
            "AgentCode1": "ATE4719997"
        },
        {
            "RequestID": "200003152175",
            "AgentCode": "ATE4719997",
            "mode": "Pledged",
            "InvestorPAN": "CLFPA9890J",
            "InvestorName": "Vaibhav Arora",
            "InvestorMobile": "9818794003",
            "InvestorEmail": "vaibhavarora144@gmail.com",
            "LenderName": "DSP Finance Private Limited",
            "LienReferenceNumber": 289994416,
            "AmcCode": "128",
            "FolioNo": "910111587585",
            "scheme": "SC",
            "Pln": "DG",
            "SchemeCode": "SCDG",
            "SchemeName": "Axis Small Cap Fund  Direct Growth",
            "ISIN": "INF846K01K35",
            "AssetCategory": "EQUITY",
            "AssetSubCategory": "Equity",
            "LienMarkedUnits": 182.957,
            "LienAmount": "23111.128",
            "CurrentUnits": 801.248,
            "CurrentNAV": 126.32,
            "CurrentValue": "101213.647",
            "ihno": 289994416,
            "KfinRefno": "3234898",
            "AgentCode1": "ATE4719997"
        },
        {
            "RequestID": "200003152175",
            "AgentCode": "ATE4719997",
            "mode": "Pledged",
            "InvestorPAN": "CLFPA9890J",
            "InvestorName": "Vaibhav Arora",
            "InvestorMobile": "9818794003",
            "InvestorEmail": "vaibhavarora144@gmail.com",
            "LenderName": "DSP Finance Private Limited",
            "LienReferenceNumber": 1007796012,
            "AmcCode": "166",
            "FolioNo": "51013347075",
            "scheme": "IB",
            "Pln": "DG",
            "SchemeCode": "IBDG",
            "SchemeName": "quant Small Cap Fund  Direct Plan Growth",
            "ISIN": "INF966L01689",
            "AssetCategory": "EQUITY",
            "AssetSubCategory": "EQUITY",
            "LienMarkedUnits": 7.649,
            "LienAmount": "2240.316",
            "CurrentUnits": 7.649,
            "CurrentNAV": 292.89,
            "CurrentValue": "2240.316",
            "ihno": 1007796012,
            "KfinRefno": "3234898",
            "AgentCode1": "ATE4719997"
        }
    ]
}
```

CAMS Request body:

```json
{
    "consolidatelienstatus": {
        "fromDate": "18-Dec-2024",
        "clientid": "LAMF-TDSPPLL",
        "toDate": "23-Dec-2024",
        "pan": "AKOPV5352L"
    }
}
```

Sample CAMS response:

```json
{
  "consolidatelienstatus": {
    "fromDate": "18-Dec-2024", - Optional
    "clientid": "LAMF-TDSPPLL",
    "toDate": "23-Dec-2024", - Optional
    "pan": "AKOPV5352L",
    "schemedetails": [
      {
        "amccode": "H",
        "amcname": "HDFC Mutual Fund",
        "platformclientid": "",
        "email": "",
        "mobileno": "9538630710",
        "taxno": "AKOPV5352L",
        "invname": "JUDDJSUPVKAH",
        "folio": "17073508",
        "schemename": "INNPT / HDFC Index Fund-NIFTY 50 Plan - Direct Plan",
        "schemecode": "INNPT",
        "isinno": "INF179K01WM1",
        "lienunit": "10.117",
        "remainingunits": "10.117",
        "lienmarkno": "198424",
        "institution": "DSP FINANCE PRIVATE LIMITED",
        "markeddate": "20-Dec-2024 20:12:59",
        "lienrefno": "42709",
        "initiateddate": "20-Dec-2024 20:15:26",
        "lienmarkstatus": "SUCCESS"
      },
      {
        "amccode": "H",
        "amcname": "HDFC Mutual Fund",
        "platformclientid": "",
        "email": "",
        "mobileno": "9538630710",
        "taxno": "AKOPV5352L",
        "invname": "XCZYEIJZVFJY",
        "folio": "17057381",
        "schemename": "ACGPG / HDFC Small Cap Fund - Regular Plan - Growth Plan",
        "schemecode": "ACGPG",
        "isinno": "INF179KA1RZ8",
        "lienunit": "100.123",
        "remainingunits": "100.123",
        "lienmarkno": "",
        "institution": "DSP FINANCE PRIVATE LIMITED",
        "markeddate": "20-Dec-2024 16:08:42",
        "lienrefno": "42699",
        "initiateddate": "",
        "lienmarkstatus": "FAILURE"
      },
      {
        "amccode": "H",
        "amcname": "HDFC Mutual Fund",
        "platformclientid": "",
        "email": "",
        "mobileno": "9538630710",
        "taxno": "AKOPV5352L",
        "invname": "JUDDJSUPVKAH",
        "folio": "17073508",
        "schemename": "INNPT / HDFC Index Fund-NIFTY 50 Plan - Direct Plan",
        "schemecode": "INNPT",
        "isinno": "INF179K01WM1",
        "lienunit": "10.117",
        "remainingunits": "10.117",
        "lienmarkno": "",
        "institution": "DSP FINANCE PRIVATE LIMITED",
        "markeddate": "20-Dec-2024 20:08:33",
        "lienrefno": "42708",
        "initiateddate": "",
        "lienmarkstatus": "FAILURE"
      },
      {
        "amccode": "P",
        "amcname": "ICICI Prudential Mutual Fund",
        "platformclientid": "",
        "email": "",
        "mobileno": "9538630710",
        "taxno": "AKOPV5352L",
        "invname": "LKMEIRBRUMKY",
        "folio": "15713057",
        "schemename": "8130 / ICICI Prudential Regular Gold Savings Fund (FOF) - Direct Plan - Growth",
        "schemecode": "8130",
        "isinno": "INF109K01U92",
        "lienunit": "100.1",
        "remainingunits": "100.1",
        "lienmarkno": "",
        "institution": "DSP FINANCE PRIVATE LIMITED",
        "markeddate": "19-Dec-2024 18:55:00",
        "lienrefno": "42631",
        "initiateddate": "",
        "lienmarkstatus": "FAILURE"
      },
      {
        "amccode": "H",
        "amcname": "HDFC Mutual Fund",
        "platformclientid": "",
        "email": "",
        "mobileno": "9538630710",
        "taxno": "AKOPV5352L",
        "invname": "JUDDJSUPVKAH",
        "folio": "17073508",
        "schemename": "INNPT / HDFC Index Fund-NIFTY 50 Plan - Direct Plan",
        "schemecode": "INNPT",
        "isinno": "INF179K01WM1",
        "lienunit": "100.123",
        "remainingunits": "64.883",
        "lienmarkno": "198423",
        "institution": "DSP FINANCE PRIVATE LIMITED",
        "markeddate": "20-Dec-2024 19:06:34",
        "lienrefno": "42707",
        "initiateddate": "20-Dec-2024 19:08:49",
        "lienmarkstatus": "SUCCESS"
      }
    ]
  },
  "status": "SUCCESS",
  "message": "SUCCESS"
}
```

## Requirements overview (optional)

1. Context
    - We define uniqueness of a collateral transaction basis three parameters:
        - ISIN
        - Folio
        - Lien reference number (CAMS/KFIN)
    - One transaction has all three. For CAMS and KFIN unit management is done at a transaction level, that is:
        - If 100 units were marked in two transactions:
            - 40 units in transaction 1 (ISIN 1 + Folio Number 1 + ILien reference number)
            - 60 units in transaction 2 (ISIN 1 + Folio Number 1+Lien reference number)
        - We will not be able to revoke 100 units at once, it will have to be done at a transaction level, as the unit balance (check API response) with the RTAs is managed at a transaction level
        - This introduces a lot of complexity (Portfolio APIs will help us achieve the same easily.

Problems being solved:

- Pre-lodgement validation
- Revocation units validation + distribution at a transaction level
- Invocation units validation + distribution at a transaction level
- LM hold/LM pending handling for (KFIN + CAMS) - Asynchronous handling
- Multiple lien marking in one session for same ISIN + Folio combination failure handling
1. Lodgement:

When we hit the API for lien marking we will get a request success response post which we need to hit the lien status API to confirm the lien marking of the assets.

We can get the following status from the RTAs :

    1. Success / LM Success
    2. Pending (LM hold / LM pending)
    3. Failure
    
    A request can fail or be successful from a pending state.
    
- Before lodging units, make API calls to both RTAs (CAMS and KFIN)
1. KFIN Validation:
    - Call KFIN Portfolio API with required parameters
    - Extract LienMarkedUnits from response for each ISIN + Folio + Lien marking number combination
    - Compare with initial pledged units
    - Flag if `LienMarkedUnits < Initial Pledged Units`
2. CAMS Validation:
    - Call CAMS Portfolio API with parameters
    - From response, check `lienunit` and `remainingunits` for each combination
    - Compare with initial pledged units
    - Flag if `remainingunits < Initial Pledged Units`

Scenario 1;

Lodgement is above 10 lakhs, it will go through the approval flow:
Collateral value above 10 lakh, lodgement approval required for loan account number: [Loan account number]

Scenario 2:

If we get success for all funds, and lodgement is happening the same day as lien marking we will (<10,00,000) the lodgement (and passes the portfolio API validation) will be approved automatically without approval with the following remark: 

“Collateral addition auto-approved via STP flow for loan account number”: [Loan account number]

Scenario 3: 

If we get pending/failure status for any one of the funds, in the lodgement request, the request will automatically become non STP and will need a description.

Lien marking in pending state, approval required for loan account number: [Loan account number]

<aside>
💡

Operations agent will be able to partially approve securities that is, they will be able to select securities that have been marked by the RTAs and will be able to lodge them at a sub task level.

A task will be in a partial completion state till all securities are either accepted or rejected successfully, if accepted, the user will get the corresponding DP in their loan account.

Operations agent will be able to track the open request on the command centre as its type will now change from collateral addition approval to partial collateral addition approval

</aside>

1. Revocation and invocation:

A revocation/invocation request is when a user requests a partial or complete release/redemption of their securities. In this scenario, the held/marked securities by the NBFC are released/invoked via the RTA APIs. 

We hit the revoke validate API to ensure that the revocation request raised is validated and correspondingly an approval task is created for the operations team.

We will be integrating the portfolio API before hitting the revocation request API to ensure that the user has enough securities lien marked before proceeding to revoking.

1. KFIN Validation:

- Call KFIN Portfolio API with required parameters
- Extract LienMarkedUnits from response for each ISIN + Folio + Lien marking number combination
- Distribute number of units across ih number of transaction.
    - For example, if within the same loan account the same ISIN folio combination was marked and lodged twice they would be like:
        - 40 units in transaction 1 (ISIN 1 + Folio Number 1 + Ih Number 1)
        - 60 units in transaction 2 (ISIN 1 + Folio Number 1+ Ih number 2)
    - Now if I were to revoke 50 securities I would have to do either of the two:
        - Revoke/invoke securities from transaction 2: 50 out of the 60 marked securities
        - Revoke/invoke 40 from transaction 1: 40 out of 40 and 10 from transaction 2: 10 out of 60.
        - Our revocation request logic should optimise for minimum number of transactions for a ISIN folio combination to optimise for request failure.
1. CAMS Validation:
- Call CAMS Portfolio API with required parameters
- Extract LienMarkedUnits from response for each ISIN + Folio + Lien marking number combination
- Distribute number of units across lien reference number of transaction.
    - For example, if within the same loan account the same ISIN folio combination was marked and lodged twice they would be like:
        - 40 units in transaction 1 (ISIN 1 + Folio Number 1 + Lien reference number 1)
        - 60 units in transaction 2 (ISIN 1 + Folio Number 1+ Lien reference number 2)
    - Now if I were to revoke 50 securities I would have to do either of the two:
        - Revoke/invoke securities from transaction 2: 50 out of the 60 marked securities
        - Revoke/invoke 40 from transaction 1: 40 out of 40 and 10 from transaction 2: 10 out of 60.
        - Our revocation request logic should optimise for minimum number of transactions for a ISIN folio combination to optimise for request failure.

```json
Lien revoke validate API response
{
"revocvalidate": {
"reqrefno": "12000",
"lienrefno": "1806",
"pan": "ABCDE1234F",
"regemailid": "sathyav@abc.com",

"mobile": "",
"clientid": "xxxxx",
"requestip": "192.168.21.1",
"schemedetails": [{

"amccode": "TEST",
"folio": "3973186",
"schemecode": "ICFD",
"schemename": "Tata India Fund Regular Plan Dividend",
"isinno": "INF277K012",
"schemetype": "Equity",
"schemecategory": "0",
"lienunit": "2",
"revocationunit": "2",
"lienmarkno": "12343",
"remarks": "SUCCESS"
}
],
"message": "SUCCESS",
"revoctoken": "64"
}
}
```

## User stories / User flow

Lodgement:

![image.png](%5BPlatform%5D%20RTA%20portfolio%20API%20integration/image.png)

Invocation/Revocation:

![image.png](%5BPlatform%5D%20RTA%20portfolio%20API%20integration/image%201.png)

---

# **Design**

@Karuna Sankolli we need to handle partial approval for lodgement. Have described the PS above. Can we come up with iterations.

---

# **Analytics**

- Request logging of portfolio APIs.
- Number of lodgement requests rejected due to portfolio API validation

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