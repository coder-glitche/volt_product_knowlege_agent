# Pledged portfolio API (KFIN)

: Vaibhav Arora
Created time: December 11, 2024 11:42 AM
Status: Done
Last edited: February 1, 2025 1:21 PM

### **Purpose**

The API enables a lender to request detailed information about an investor's mutual fund folios that are pledged as collateral. It provides insights into folio numbers, pledged units, ISINs, and related details.

---

### **Request Method**

**POST** `/PortfolioRequest`

---

### **Request Headers**

| **Name** | **Type** | **Description** | **Default Value** |
| --- | --- | --- | --- |
| `CLIENT` | string (header) | Client Header | XXXXXX |
| `CLIENT-ID` | string (header) | Client ID Header | XXXX |
| `CLIENT-SECRET` | string (header) | Client Secret Header | XXX |
| `Content-Type` | string (header) | Content Type | application/json |

---

### **Request Body**

The body accepts a JSON object containing:

```json
json
Copy code
{
  "PortfolioRequest": {
    "InvPan": "ABC123",       // Investor PAN
    "RequestID": "123",       // Unique Request ID
    "AgentCode": "ABC123"     // Agent Code
  }
}

```

---

### **Response**

### **Success (Code: 0)**

Returns detailed data for pledged mutual fund units. Example:

```json
json
Copy code
{
  "Dtinformation": [
    { "Return_Code": 0, "Return_Msg": "Success" }
  ],
  "DtData": [
    {
      "RequestID": "123",
      "InvestorPAN": "ABC123",
      "InvestorName": "ABC",
      "FolioNo": "123",
      "ISIN": "ABC123",
      "LienMarkedUnits": 0.1,
      "CurrentNAV": 0.1,
      "CurrentValue": "0",
      ...
    }
  ]
}

```

### **Failure (Code: -100)**

Returns a message if the data does not exist. Example:

```json
json
Copy code
{
  "Dtinformation": [
    { "Return_Code": 0, "Return_Msg": "Data Does not exist" }
  ]
}
```

---

### **Key Features**

- **Parameters:** Accepts investor PAN, request ID, and agent code.
- **Output Details:** Comprehensive folio and pledged unit details like:
    - Folio number
    - Pledged units and amount
    - NAV and current value
    - Investor and lender information
- **Error Handling:** Indicates when no data is found.

This API is primarily intended for lenders to access mutual fund collateral data securely and efficiently.