# MFC Pledge (revocation & invocation)

: Ameya Aglawe
Created time: July 2, 2025 9:49 AM
Status: Pending Review
Last edited: July 4, 2025 7:04 PM

# **What problem are we solving?**

---

- **Multiple OTP Friction**: Users currently need to enter two separate OTPs when pledging mutual fund units - one for CAMS RTA and another for KFIN RTA if their portfolio spans across both RTAs. The dual OTP process creates friction in the loan origination journey, potentially leading to higher drop-off rates during pledge process
- **Complex Integration Overhead**: LSPs must maintain separate API integrations with both CAMS and KFIN RTAs, leading to:
    - Duplicate development effort
    - Multiple credential management
    - Inconsistent error handling across RTAs
    - Managing different API formats, authentication mechanisms, and response structures across RTAs
- **Poor User Experience**: The dual OTP process creates friction in the loan origination journey, potentially leading to:
    - Higher drop-off rates during pledge process
    - Confused users questioning why multiple OTPs are needed
    - Longer transaction completion times

# **How do we measure success?**

---

- Number of successful MFC Pledge request
- Number of successful MFC Invoke/Revoke request

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements

---

- Shifting to MFC Pledge from RTA Pledge will have impact on things
    - API calls during pledge, invocation, revocation
    - Reconciliation (there won’t be any change required here as the CAMS and KFIN will continue to flow in the respective RTA reports), so the reconcilliation process would happen as it is.

## API Flows

The following will be the flow and sequence of API calls - 

- Submit a pledge request
    - validateLien request
        
        ```jsx
        {
          "reqId": "597810",
          "pan": "ALNPR6026P",
          "pekrn": "",
          "mobile": "9884174067",
          "email": "",
          "clientId": "ranjani",
          "clientRefNo": "2702112024112308",
          "lenderCode": "mfcl_001",
          "data": [
            {
              "schemeDetails": [
                {
                  "amc": "H",
                  "amcname": "MFHMF Test AMC",
                  "folio": "17063708",
                  "isin": "INF179K01608",
                  "itemNo": "",
                  "schemeCode": "02",
                  "schemeName": "",
                  "schemeType": "",
                  "lienUnits": "5"
                },
                {
                  "amc": "RMF",
                  "amcname": "Nippon India Mutual Fund",
                  "folio": "4092217783",
                  "isin": "INF204K01XO1",
                  "itemNo": "",
                  "schemeCode": "BFAGG",
                  "schemeName": "",
                  "schemeType": "",
                  "lienUnits": "5"
                }
              ]
            }
          ]
        }
        
        ```
        
    - validateLien response
        
        ```jsx
        {
          "reqId": "2526580",
          "pan": "ALNPR6026P",
          "pekrn": "",
          "mobile": "9884174067",
          "email": "",
          "clientId": "ranjani",
          "lenderCode": "mfcl_001",
          "pending": [],
          "errors": [],
          "success": [
            {
              "rtaName": "CAMS",
              "lienRefNo": "30344",
              "schemeDetails": [
                {
                  "amc": "H",
                  "folio": "17063708",
                  "schemeName": "",
                  "isin": "INF179K01608",
                  "itemNo": "",
                  "lienUnits": "5",
                  "remarks": ""
                }
              ]
            },
            {
              "rtaName": "KFin",
              "lienRefNo": "8844969",
              "schemeDetails": [
                {
                  "amc": "RMF",
                  "folio": "4092217783",
                  "schemeName": "NIPPON INDIA BANKING & FINANCIAL SERVICES FUND",
                  "isin": "INF204K01XO1",
                  "itemNo": "",
                  "lienUnits": "5"
                }
              ]
            }
          ],
          "validateId": "2526580"
        }
        
        ```
        
    - submitLien request
        
        ```jsx
        {
          "reqId": "2526580",
          "pan": "ALNPR6026P",
          "pekrn": "",
          "mobile": "9884174067",
          "email": "",
          "clientRefNo": "2702112024112308",
          "clientId": "ranjani",
          "lenderCode": "mfcl_001",
          "data": [
            {
              "rtaName": "CAMS",
              "lienRefNo": "30344",
              "schemeDetails": [
                {
                  "amc": "H",
                  "folio": "17063708",
                  "schemeName": "",
                  "isin": "INF179K01608",
                  "itemNo": "",
                  "lienUnits": "5",
                  "remarks": ""
                }
              ]
            },
            {
              "rtaName": "KFin",
              "lienRefNo": "8844969",
              "schemeDetails": [
                {
                  "amc": "RMF",
                  "folio": "4092217783",
                  "schemeName": "NIPPON INDIA BANKING & FINANCIAL SERVICES FUND",
                  "isin": "INF204K01XO1",
                  "itemNo": "",
                  "lienUnits": "5"
                }
              ]
            }
          ]
        }
        
        ```
        
    - submitLien response
        
        ```jsx
        {
          "reqId": 2526581,
          "otpRef": "ebdbad1c-25cd006026bc0a305af09266b0",
          "userSubjectReference": "",
          "clientRefNo": "2702112024112308"
        }
        
        ```
        
- Check the status of pledge transaction request
    - Request
        
        ```jsx
        {
          "clientRefNo": "test_cs_01",
          "reqId": "2212_003"
        }
        ```
        
    - Response
        
        ```jsx
        {
          "pan": "EFNPXXXXXR",
          "pekrn": "",
          "mobile": "8015933245",
          "email": "",
          "requests": [
            {
              "reqId": 2489560,
              "status": "COMPLETED",
              "requestTime": "2023-11-15 12:40:09.859",
              "requestType": "SUBMIT_LIEN",
              "requestTypeDesc": "Submit Lien to RTA",
              "rtaResponse": {
                "success": [
                  {
                    "schemeDetails": [
                      {
                        "amc": "T",
                        "folio": "3688619",
                        "schemeName": "",
                        "isin": "INF277K014C0",
                        "itemNo": "8620727865",
                        "lienUnits": "1",
                        "lienSubRefNo": "23136",
                        "entryDateTime": "15-Nov-2023 12:11:11",
                        "message": "",
                        "techMessage": "",
                        "transactionStatus": "Lien marked successfully."
                      }
                    ],
                    "completionTime": "2023-11-15 12:45:11.614",
                    "code": "200",
                    "reqType": "LM",
                    "lienRefNo": "27168",
                    "rtaName": "CAMS",
                    "reqId": "445801136"
                  }
                ]
              },
              "completionTime": "2023-11-15 12:45:11.718"
            }
          ]
        }
        
        ```
        
- During lodgement reconcile whether the pledge funds are still pledge against DSP
    - Request
        
        ```jsx
        {
          "reqId": "597810",
          "pekrn": "",
          "mobile": "9239874560",
          "pan": "AQQPS7576R",
          "email": "",
          "clientId": "ranjani",
          "clientRefNo": "2afmlfflpoppd2dsl08",
          "lenderCode": "mfcl_001"
        }
        ```
        
    - Response
        
        ```jsx
        {
          "reqId": "2945483",
          "pan": "AQQPS7576R",
          "pekrn": "",
          "email": "",
          "mobile": "9239874560",
          "clientId": "ranjani",
          "clientName": "",
          "lenderCode": "mfcl_001",
          "data": [
            {
              "rtaName": "CAMS",
              "lienRefNo": "44648",
              "amc": "H",
              "folio": "17081138",
              "schemeName": "MTOGT / HDFC Corp. Bond Fund-Direct-GR",
              "isin": "INF179K01XD8",
              "lienHoldUnits": "0",
              "lienSubRefNo": "199529",
              "TotalLienUnits": "5",
              "schemeCode": "MTOGT"
            },
            {
              "rtaName": "KFIN",
              "lienRefNo": "7016627",
              "amc": "117",
              "folio": "730249464",
              "schemeName": "Mirae Asset Large Cap Fund  Direct Plan - Growth",
              "isin": "INF769K01AX2",
              "lienHoldUnits": "1",
              "schemeCode": "IOD1",
              "lienSubRefNo": "186961373"
            }
          ]
        }
        
        ```
        
- Submit revocation/invocation request
    - validateLienInvokeRevoke API request
        
        ```jsx
        {
          "lenderCode": "mfcl_001",
          "clientId": "ranjani",
          "clientRefNo": "677756qdp74698421",
          "email": "",
          "mobile": "9239874560",
          "pan": "AQQPS7576R",
          "pekrn": "",
          "reqId": "",
          "data": [
            {
              "lienRefNo": "51387",
              "invokeRevokeType": "R",
              "invokeRevokeToken": "",
              "rtaName": "CAMS",
              "schemeDetails": [
                {
                  "amc": "H",
                  "folio": "17057225",
                  "isin": "INF179K01830",
                  "lienUnits": "0.1",
                  "lienSubRefNo": "203903"
                }
              ]
            },
            {
              "lienRefNo": "2110597",
              "invokeRevokeType": "R",
              "invokeRevokeToken": "",
              "rtaName": "KFIN",
              "schemeDetails": [
                {
                  "amc": "101",
                  "folio": "1071636311",
                  "isin": "INF760K01274",
                  "lienUnits": "0.1",
                  "lienSubRefNo": "609223307"
                }
              ]
            }
          ]
        }
        
        ```
        
    - validateLienInvokeRevoke API response
        
        ```jsx
        {
          "reqId": "2945193",
          "pan": "AQQPS7576R",
          "pekrn": "",
          "mobile": "9239874560",
          "email": "",
          "clientId": "ranjani",
          "lenderCode": "mfc_001",
          "pending": [],
          "errors": [],
          "success": [
            {
              "rtaName": "CAMS",
              "invokeRevokeType": "R",
              "lienInvRevRefNo": "51387",
              "invokeRevokeToken": "4934",
              "schemeDetails": [
                {
                  "amc": "H",
                  "folio": "17057225",
                  "schemeName": "",
                  "isin": "INF179K01830",
                  "itemNo": "",
                  "lienUnits": "0.1",
                  "lienSubRefNo": "203903",
                  "remarks": ""
                }
              ]
            },
            {
              "rtaName": "KFIN",
              "lienRefNo": "2110597",
              "lienInvRevRefNo": "2110597",
              "invokeRevokeToken": "",
              "invokeRevokeType": "R",
              "schemeDetails": [
                {
                  "amc": "101",
                  "folio": "1071636311",
                  "schemeName": "",
                  "isin": "INF760K01274",
                  "lienUnits": "0.1",
                  "lienSubRefNo": "609223307",
                  "entryDateTime": "",
                  "remarks": "Valid Folio",
                  "transactionStatus": "Folio Validated Successfully"
                }
              ]
            }
          ],
          "validateId": "2945193"
        }
        
        ```
        
    - submitLienInvokeRevoke API request
        
        ```jsx
        {
          "reqId": "2945473",
          "pan": "AQQPS7576R",
          "pekrn": "",
          "mobile": "9239874560",
          "email": "",
          "clientId": "dspfinance",
          "lenderCode": "mfc_dspfinance",
          "clientRefNo": "67tyqdfp74698421",
          "data": [
            {
              "rtaName": "CAMS",
              "invokeRevokeType": "R",
              "lienRefNo": "51387",
              "invokeRevokeToken": "4938",
              "schemeDetails": [
                {
                  "amc": "H",
                  "folio": "17057225",
                  "schemeName": "",
                  "isin": "INF179K01830",
                  "itemNo": "",
                  "lienUnits": "0.1",
                  "lienSubRefNo": "203903",
                  "remarks": ""
                }
              ]
            },
            {
              "rtaName": "KFIN",
              "lienRefNo": "2110597",
              "lienInvRevRefNo": "2110597",
              "invokeRevokeToken": "",
              "invokeRevokeType": "R",
              "schemeDetails": [
                {
                  "amc": "101",
                  "folio": "1071636311",
                  "schemeName": "",
                  "isin": "INF760K01274",
                  "lienUnits": "0.1",
                  "lienSubRefNo": "609223307",
                  "entryDateTime": "",
                  "remarks": "Valid Folio",
                  "transactionStatus": "Folio Validated Successfully"
                }
              ]
            }
          ]
        }
        
        ```
        
    - submitLienInvokeRevoke API response
        
        ```jsx
        {
          "reqId": "2609854"
        }
        ```
        
- Check the status of revocation/invocation transaction request using the transaction status API

## Following are the details on where we would fetch the details of the different API and their request bodies 

1. Pledge request

### 1.1 validateLien API

**Purpose**: Validate portfolio for lien marking
**URL**: `<baseURL>/api/client/V1/validatelien`

**Key Request Parameters**:

- `clientRefNo`: Unique reference (max 30 chars)
- `pan` or `pekrn`: Investor identification
- `mobile` or `email`: Contact (either one required)
- `clientId`: MFC client ID
- `lenderCode`: Lender identification
- `data[]`: Array of schemes to pledge
    - `amc`: AMC code
    - `folio`: Folio number
    - `isin`: Scheme ISIN
    - `lienUnits`: Units to pledge

**Response**:

- `reqId`: Use in subsequent calls
- `success[]`: Valid schemes with `lienRefNo`
- `errors[]`: Invalid schemes with error details

### 1.2 submitLien API

**Purpose**: Submit validated lien request and trigger OTP
**URL**: `<baseURL>/api/client/V1/submitlien`

**Key Request Parameters**:

- `reqId`: From validateLien response
- Same investor details as validateLien
- `data[]`: Include `rtaName` and `lienRefNo` from validateLien success response

**Response**:

- `reqId`: For OTP validation
- `otpRef`: OTP reference
- `clientRefNo`: Reference number

### 1.3 Status Checking

### getTransactionStatus API

**Purpose**: Check transaction completion and get lienSubRefNo
**URL**: `<baseURL>/api/client/V1/getTransactionStatus`

**Request Parameters**:

- `reqId`: From submit API response
- `clientRefNo`: Original reference

**Response Statuses**:

- `COMPLETED`: Transaction successful, contains `lienSubRefNo`
- `ERROR`: Transaction failed with error details
- `PENDING`: Still processing

**Critical Response Fields**:

- `lienRefNo`: RTA level reference
- `lienSubRefNo`: Fund level reference (required for invoke/revoke)

### 1.4 Reconciliation

### lienCheck API

**Purpose**: Check transaction completion and get lienSubRefNo
**URL**: `<baseURL>/api/client/V1/getTransactionStatus`

**Request Parameters**:

- `reqId`: From submit API response
- `clientRefNo`: Original reference
- `mobile` : User’s mobile
- `pan` : User’s PAN
- `clientId` : Lender credentials
- `lender_code`: Lender credentials

**Response Statuses**:

- `COMPLETED`: Transaction successful, contains `lienSubRefNo`
- `ERROR`: Transaction failed with error details
- `PENDING`: Still processing

**Critical Response Fields**:

- `lienRefNo`: RTA level reference
- `lienSubRefNo`: Fund level reference (required for invoke/revoke)

## 2. Invoke/Revoke

### 2.1 validateLienInvokeRevoke API

**Purpose**: Validate invoke/revoke request
**URL**: `<baseURL>/api/client/V1/validatelieninvokerevoke`

**Key Request Parameters**:

- `invokeRevokeType`: "I" for invoke, "R" for revoke
- `lienRefNo`: From original pledge
- `lienSubRefNo`: From getTransactionStatus response
- Same scheme details as original pledge

**Response**:

- `reqId`: For submit API
- `invokeRevokeToken`: Required for submit (CAMS only)

### 2.2 submitLienInvokeRevoke API

**Purpose**: Submit invoke/revoke request
**URL**: `<baseURL>/api/client/V1/submitlieninvokerevoke`

**Key Request Parameters**:

- `reqId`: From validate response
- `invokeRevokeToken`: From validate response (if provided)
- Same data structure as validate request

**Response**:

- `reqId`: For status checking

### 2.3 Status Checking

### getTransactionStatus API

**Purpose**: Check transaction completion and get lienSubRefNo
**URL**: `<baseURL>/api/client/V1/getTransactionStatus`

**Request Parameters**:

- `reqId`: From submit API response
- `clientRefNo`: Original reference

**Response Statuses**:

- `COMPLETED`: Transaction successful, contains `lienSubRefNo`
- `ERROR`: Transaction failed with error details
- `PENDING`: Still processing

**Critical Response Fields**:

- `lienRefNo`: RTA level reference
- `lienSubRefNo`: Fund level reference (required for invoke/revoke)

****

---

**TLDR :** 

1. The MFC Pledge flow consists of three types of transactions: pledge, invocation, and revocation. Invocation and revocation share the same APIs and overall flow. The process starts with initiating a pledge, followed by checking the status of that pledge to retrieve a `lienSubRefNo`, which is then used to either invoke or revoke the pledge.
2. The pledge process involves two APIs: `validateLien`, which returns a `reqID`, and `submitLien`, which uses this `reqID` in its request body. After submitting the lien, the status of the transaction can be checked using the `getTransactionStatus` API, which takes the `reqID` and `clientSubRefNo` as inputs. This API returns the status of the request (completed, error, or pending) - attaching the response structure [here](https://docs.google.com/document/d/1NiIxYn0CE4Qm35lr4zwyP1zIaKRkw_I-HnFy-iN9D84/edit?usp=sharing). If the transaction is completed, it provides a `lienRefNo` at the RTA level and a `lienSubRefNo` at the fund level.
3. To perform an invocation or revocation, the `lienSubRefNo` obtained earlier is used. This process also involves two APIs: `validateLienInvokeRevoke`, which returns a new `reqID`, and `submitLienInvokeRevoke`, which uses that `reqID` in its request body.
4. In case of partial invocation/revocation the lienSubRefNo against the fund would change, we will have to fetch the latest lienSubRefNo against a particular fund from the get transaction status API or lien check API. 

---

# **Design**

---

# **Analytics**

---

1. Discuss with Vaibhav 

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

- Existing Finflux fields changes
    - pledgeSource (MFC, KFIN, CAMS)
- Jugaad