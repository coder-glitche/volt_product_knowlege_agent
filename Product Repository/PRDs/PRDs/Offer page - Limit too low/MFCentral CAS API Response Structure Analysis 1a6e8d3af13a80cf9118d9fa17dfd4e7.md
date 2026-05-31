# MFCentral CAS API Response Structure Analysis

## Top-Level Structure

```json
{
  "reqId": "string",           // Request identifier
  "pan": "string",             // PAN number of the investor
  "pekrn": "string",           // PEKRN (optional identifier)
  "mobile": "string",          // Mobile number with country code
  "email": "string",           // Email address (optional)
  "data": [                    // Array of fund house holdings
    {
      "summary": [...],        // Summary data for this fund house
      "schemes": [...]         // Array of schemes under this fund house
    },
    // Additional fund houses...
  ],
  "portfolio": [               // Overall portfolio summary
    {
      // Non-demat holdings summary
    },
    {
      // Demat holdings summary
    }
  ],
  "investorDetails": {         // Investor information
    // Address and contact details
  },
  "statementHoldingFilter": "string" // Filter applied (e.g., "NON-ZERO")
}

```

## Fund House Data Structure

Each element in the `data` array represents holdings from a single AMC:

```json
{
  "summary": [
    {
      "amc": "string",              // AMC code
      "amcName": "string",          // AMC full name
      "isDemat": "string",          // "Y" or "N" for demat status
      "currentMktValue": "number",  // Current market value
      "costValue": "number",        // Total investment amount
      "gainLoss": "number",         // Profit/loss amount
      "gainLossPercentage": "number" // Profit/loss percentage
    }
  ],
  "schemes": [
    {
      // Detailed information for each scheme
    }
    // Additional schemes...
  ]
}

```

## Scheme-Level Structure

Each scheme contains detailed investment information:

```json
{
  "amc": "string",                  // AMC code
  "amcName": "string",              // AMC full name
  "folio": "string",                // Folio number
  "investorName": "string",         // Investor name
  "age": number,                    // Investor age
  "mobile": "string",               // Registered mobile
  "email": "string",                // Registered email
  "taxStatus": "string",            // Tax status code
  "modeOfHolding": "string",        // Single, Joint, etc.
  "transactionSource": "string",    // Source of transaction (BSE, etc.)
  "schemeCode": "string",           // Unique scheme identifier
  "schemeName": "string",           // Complete scheme name
  "idcwChangeAllowed": "string",    // Income Distribution Change allowed flag
  "schemeOption": "string",         // Growth, IDCW, etc.
  "assetType": "string",            // EQUITY, DEBT, etc.
  "schemeType": "string",           // Classification
  "nav": "number/string",           // Current NAV
  "navDate": "string",              // NAV as of date
  "closingBalance": "number/string", // Total units held
  "availableUnits": "number/string", // Redeemable units
  "availableAmount": "number/string", // Value of available units
  "currentMktValue": "number/string", // Total current value
  "costValue": "number/string",      // Total investment amount
  "gainLoss": "number/string",       // Profit/loss amount
  "gainLossPercentage": "number/string", // Profit/loss percentage
  "isDemat": "string",               // "Y" or "N"
  "lienUnitsFlag": "string",         // "Y" or "N"
  "decimalUnits": number,            // Decimal places for units
  "decimalAmount": number,           // Decimal places for amounts
  "decimalNav": number,              // Decimal places for NAV
  "brokerCode": "string",            // Distributor ARN code
  "brokerName": "string",            // Distributor name
  "isin": "string",                  // International Securities ID
  "purAllow": "string",              // Purchase allowed flag
  "redAllow": "string",              // Redemption allowed flag
  "swtAllow": "string",              // Switch allowed flag
  "sipAllow": "string",              // SIP allowed flag
  "stpAllow": "string",              // STP allowed flag
  "swpAllow": "string",              // SWP allowed flag
  "planMode": "string",              // REGULAR or DIRECT
  "dpId": "string",                  // Depository participant ID
  "mobileRelationship": "string",    // Mobile relationship code
  "emailRelationship": "string",     // Email relationship code
  "newFolio": "string",              // "Y" or "N"
  "nomineeStatus": "string",         // "Y" or "N"
  "validPan": "string",              // "Y" or "N"
  "kycStatus": "string",             // KYC status code
  "lienEligibleUnits": "number/string", // Units eligible for lien
  "bank": {                          // Bank account details
    "accountNo": "string",
    "accountType": "string",
    "name": "string",
    "branch": "string",
    "city": "string",
    "pincode": "string",
    "micr": "string",
    "ifsc": "string",
    "neftifsc": "string"
  },
  "rtaName": "string"                // RTA name (CAMS or KFIN)
}

```

## Portfolio Summary Structure

The portfolio section provides an aggregate view:

```json
[
  {
    "currentMktValue": "string",      // Total non-demat value
    "costValue": "string",            // Total non-demat cost
    "gainLoss": "string",             // Total non-demat P/L
    "gainLossPercentage": "string",   // Total non-demat P/L %
    "isDemat": "N"                    // Non-demat indicator
  },
  {
    "currentMktValue": "string",      // Total demat value
    "costValue": "string",            // Total demat cost
    "gainLoss": "string",             // Total demat P/L
    "gainLossPercentage": "string",   // Total demat P/L %
    "isDemat": "Y"                    // Demat indicator
  }
]

```

## Investor Details Structure

```json
{
  "address": {
    "line1": "string",
    "line2": "string",
    "line3": "string",
    "state": "string",
    "pincode": number,
    "country": "string",
    "city": "string"
  },
  "email": "string",
  "mobile": "string",
  "investorName": "string"
}

```

# Example Data

## Top-Level Structure

```json
{
  "reqId": "879239409",
  "pan": "ACXPS5634D",
  "pekrn": "",
  "mobile": "+918401827921",
  "email": "",
  "data": [
    // Array of fund house data (examples below)
  ],
  "portfolio": [
    {
      "currentMktValue": "214476.49",
      "costValue": "190495.71",
      "gainLoss": "23980.78",
      "gainLossPercentage": "12.59",
      "isDemat": "N"
    },
    {
      "currentMktValue": "0.00",
      "costValue": "0.00",
      "gainLoss": "0.00",
      "gainLossPercentage": "0.00",
      "isDemat": "Y"
    }
  ],
  "investorDetails": {
    "address": {
      "line1": "301,CHINTAMANI APT,SHANKHESHWAR",
      "line2": "COMPLEX,KAILASH NAGAR,SAGRAMPURA",
      "line3": "",
      "state": "GUJARAT",
      "pincode": 395002,
      "country": "INDIA",
      "city": "SURAT"
    },
    "email": "shahhitesh5412@gmail.com",
    "mobile": "8401827921",
    "investorName": "JYOTI HITESH SHAH"
  },
  "statementHoldingFilter": "NON-ZERO"
}

```

## Fund House Data Examples

### Example 1: Franklin Templeton Mutual Fund

```json
{
  "summary": [
    {
      "amc": "FTI",
      "amcName": "Franklin Templeton Mutual Fund",
      "isDemat": "N",
      "currentMktValue": "30219.65",
      "costValue": "26000.00",
      "gainLoss": "4219.65",
      "gainLossPercentage": "16.23"
    }
  ],
  "schemes": [
    {
      "amc": "FTI",
      "amcName": "Franklin Templeton Mutual Fund",
      "folio": "33622087",
      "investorName": "Jyoti Hitesh Shah",
      "age": 50,
      "mobile": "+918401827921",
      "email": "shahhitesh5412@gmail.com",
      "taxStatus": "01",
      "modeOfHolding": "Single",
      "transactionSource": "BSE",
      "schemeCode": "219",
      "schemeName": "Franklin India Smaller Companies Fund - Growth",
      "idcwChangeAllowed": "False",
      "schemeOption": "Growth",
      "assetType": "EQUITY",
      "schemeType": "Equity(G)",
      "nav": "154.5509",
      "navDate": "12-Feb-2025",
      "closingBalance": "195.53",
      "availableUnits": "0.001",
      "availableAmount": "0.15",
      "currentMktValue": "30219.65",
      "costValue": "26000.00",
      "gainLoss": "4219.65",
      "gainLossPercentage": "16.23",
      "isDemat": "N",
      "lienUnitsFlag": "Y",
      "decimalUnits": 3,
      "decimalAmount": 2,
      "decimalNav": 4,
      "brokerCode": "ARN-0155",
      "brokerName": "NJ INDIAINVEST PVT LTD",
      "isin": "INF090I01569",
      "purAllow": "Y",
      "redAllow": "Y",
      "swtAllow": "Y",
      "sipAllow": "Y",
      "stpAllow": "Y",
      "swpAllow": "Y",
      "planMode": "R",
      "dpId": "",
      "mobileRelationship": "SE",
      "emailRelationship": "SP",
      "newFolio": "N",
      "nomineeStatus": "Y",
      "validPan": "Y",
      "kycStatus": "3",
      "lienEligibleUnits": "0.001",
      "bank": {
        "accountNo": "110004104281",
        "accountType": "SB",
        "name": "CANARA BANK",
        "branch": "SURAT NANPURA II",
        "city": "SURAT",
        "pincode": "",
        "micr": "",
        "ifsc": "CNRB0017176",
        "neftifsc": "CNRB0017176"
      },
      "rtaName": "CAMS"
    }
  ]
}

```

### Example 2: Kotak Mutual Fund

```json
{
  "summary": [
    {
      "amc": "K",
      "amcName": "Kotak Mutual Fund",
      "isDemat": "N",
      "currentMktValue": "58615.52",
      "costValue": "48000.00",
      "gainLoss": "10615.52",
      "gainLossPercentage": "22.12"
    }
  ],
  "schemes": [
    {
      "amc": "K",
      "amcName": "Kotak Mutual Fund",
      "folio": "11563631",
      "investorName": "Jyoti Hitesh Shah",
      "age": 50,
      "mobile": "+918401827921",
      "email": "shahhitesh5412@gmail.com",
      "taxStatus": "01",
      "modeOfHolding": "Single",
      "transactionSource": "BSE",
      "schemeCode": "123",
      "schemeName": "Kotak Emerging Equity Fund-Growth (Regular Plan)",
      "idcwChangeAllowed": "False",
      "schemeOption": "Growth",
      "assetType": "EQUITY",
      "schemeType": "Equity(G)",
      "nav": "116.794",
      "navDate": "12-Feb-2025",
      "closingBalance": "501.87",
      "availableUnits": "0.001",
      "availableAmount": "0.12",
      "currentMktValue": "58615.52",
      "costValue": "48000.00",
      "gainLoss": "10615.52",
      "gainLossPercentage": "22.12",
      "isDemat": "N",
      "lienUnitsFlag": "Y",
      "decimalUnits": 3,
      "decimalAmount": 2,
      "decimalNav": 3,
      "brokerCode": "ARN-0155",
      "brokerName": "NJ IndiaInvest Pvt Ltd",
      "isin": "INF174K01DS9",
      "purAllow": "Y",
      "redAllow": "Y",
      "swtAllow": "Y",
      "sipAllow": "Y",
      "stpAllow": "Y",
      "swpAllow": "Y",
      "planMode": "R",
      "dpId": "",
      "mobileRelationship": "SE",
      "emailRelationship": "SP",
      "newFolio": "N",
      "nomineeStatus": "Y",
      "validPan": "Y",
      "kycStatus": "3",
      "lienEligibleUnits": "0.001",
      "bank": {
        "accountNo": "110004104281",
        "accountType": "SB",
        "name": "CANARA BANK",
        "branch": "SURAT NANPURA II",
        "city": "SURAT",
        "pincode": "",
        "micr": "",
        "ifsc": "CNRB0017176",
        "neftifsc": "CNRB0017176"
      },
      "rtaName": "CAMS"
    }
  ]
}

```

### Example 3: SBI Mutual Fund

```json
{
  "summary": [
    {
      "amc": "L",
      "amcName": "SBI Mutual Fund",
      "isDemat": "N",
      "currentMktValue": "28804.80",
      "costValue": "28000.00",
      "gainLoss": "804.80",
      "gainLossPercentage": "2.87"
    }
  ],
  "schemes": [
    {
      "amc": "L",
      "amcName": "SBI Mutual Fund",
      "folio": "35366107",
      "investorName": "Jyoti Hitesh Shah",
      "age": 50,
      "mobile": "+918401827921",
      "email": "shahhitesh5412@gmail.com",
      "taxStatus": "01",
      "modeOfHolding": "Single",
      "transactionSource": "BSE",
      "schemeCode": "017G",
      "schemeName": "SBI Large & Midcap Fund Regular Growth",
      "idcwChangeAllowed": "False",
      "schemeOption": "Growth",
      "assetType": "EQUITY",
      "schemeType": "Equity(G)",
      "nav": "559.8927",
      "navDate": "12-Feb-2025",
      "closingBalance": "51.45",
      "availableUnits": "0.001",
      "availableAmount": "0.56",
      "currentMktValue": "28804.80",
      "costValue": "28000.00",
      "gainLoss": "804.80",
      "gainLossPercentage": "2.87",
      "isDemat": "N",
      "lienUnitsFlag": "Y",
      "decimalUnits": 3,
      "decimalAmount": 2,
      "decimalNav": 4,
      "brokerCode": "ARN0155",
      "brokerName": "NJ Indiainvest Pvt Ltd",
      "isin": "INF200K01305",
      "purAllow": "Y",
      "redAllow": "Y",
      "swtAllow": "Y",
      "sipAllow": "Y",
      "stpAllow": "Y",
      "swpAllow": "Y",
      "planMode": "R",
      "dpId": "",
      "mobileRelationship": "SE",
      "emailRelationship": "SP",
      "newFolio": "N",
      "nomineeStatus": "Y",
      "validPan": "Y",
      "kycStatus": "3",
      "lienEligibleUnits": "0.001",
      "bank": {
        "accountNo": "110004104281",
        "accountType": "SB",
        "name": "CANARA BANK",
        "branch": "SURAT NANPURA II",
        "city": "SURAT",
        "pincode": "",
        "micr": "",
        "ifsc": "CNRB0017176",
        "neftifsc": "CNRB0017176"
      },
      "rtaName": "CAMS"
    }
  ]
}

```

### Example 4: Motilal Oswal Mutual Fund

```json
{
  "summary": [
    {
      "amc": "127",
      "amcName": "MOTILAL OSWAL MUTUAL FUND",
      "currentMktValue": 22844.53,
      "costValue": 20999.02,
      "gainLoss": 1845.51,
      "gainLossPercentage": 8.8,
      "isDemat": "N"
    }
  ],
  "schemes": [
    {
      "amc": "127",
      "amcName": "MOTILAL OSWAL MUTUAL FUND",
      "folio": "91040425012",
      "investorName": "JYOTI HITESH SHAH",
      "age": 50,
      "mobile": "8401827921",
      "email": "shahhitesh5412@gmail.com",
      "taxStatus": "01",
      "modeOfHolding": "SINGLE",
      "transactionSource": "",
      "schemeCode": "FMGP",
      "schemeName": "Motilal Oswal Midcap Fund - Regular Plan Growth",
      "schemeOption": "GROWTH",
      "idcwChangeAllowed": "False",
      "assetType": "EQUITY",
      "schemeType": "EQUITY",
      "nav": 93.2289,
      "navDate": "12-Feb-2025",
      "closingBalance": 245.037,
      "availableUnits": 245.037,
      "lienEligibleUnits": 0.017,
      "availableAmount": 22844.53,
      "currentMktValue": 22844.53,
      "costValue": 20999.02,
      "gainLoss": 1845.51,
      "gainLossPercentage": 8.8,
      "lienUnitsFlag": "Y",
      "isin": "INF247L01411",
      "brokerCode": "ARN-0155",
      "brokerName": "NJ IndiaInvest Pvt Ltd",
      "decimalUnits": 3,
      "decimalAmount": 2,
      "decimalNav": 4,
      "isDemat": "N",
      "purAllow": "Y",
      "redAllow": "Y",
      "swtAllow": "Y",
      "sipAllow": "Y",
      "stpAllow": "Y",
      "swpAllow": "Y",
      "planMode": "REGULAR",
      "dpId": "",
      "rtaName": "KFIN",
      "nomineeStatus": "Y",
      "kycStatus": "02",
      "bank": {
        "accountNo": "110004104281",
        "accountType": "SAVING",
        "name": "CANARA BANK",
        "branch": "",
        "city": "SURAT",
        "pincode": "",
        "micr": "0",
        "ifsc": "CNRB0017176",
        "neftIfsc": "CNRB0017176"
      }
    }
  ]
}

```

### Example 5: Nippon India Mutual Fund

```json
{
  "summary": [
    {
      "amc": "RMF",
      "amcName": "NIPPON INDIA MUTUAL FUND",
      "currentMktValue": 73991.99,
      "costValue": 67496.69,
      "gainLoss": 6495.3,
      "gainLossPercentage": 9.6,
      "isDemat": "N"
    }
  ],
  "schemes": [
    {
      "amc": "RMF",
      "amcName": "NIPPON INDIA MUTUAL FUND",
      "folio": "477274856236",
      "investorName": "JYOTI HITESH SHAH",
      "age": 50,
      "mobile": "8401827921",
      "email": "shahhitesh5412@gmail.com",
      "taxStatus": "01",
      "modeOfHolding": "SINGLE",
      "transactionSource": "",
      "schemeCode": "LCGP",
      "schemeName": "NIPPON INDIA FLEXI CAP FUND - GROWTH PLAN",
      "schemeOption": "GROWTH",
      "idcwChangeAllowed": "False",
      "assetType": "EQUITY",
      "schemeType": "EQUITY",
      "nav": 15.0491,
      "navDate": "12-Feb-2025",
      "closingBalance": 3647.292,
      "availableUnits": 3647.292,
      "lienEligibleUnits": 0.012,
      "availableAmount": 54888.46,
      "currentMktValue": 54888.46,
      "costValue": 47997.6,
      "gainLoss": 6890.86,
      "gainLossPercentage": 14.4,
      "lienUnitsFlag": "Y",
      "isin": "INF204KC1097",
      "brokerCode": "ARN-0155",
      "brokerName": "NJ IndiaInvest Pvt Ltd",
      "decimalUnits": 3,
      "decimalAmount": 2,
      "decimalNav": 4,
      "isDemat": "N",
      "purAllow": "Y",
      "redAllow": "Y",
      "swtAllow": "Y",
      "sipAllow": "Y",
      "stpAllow": "Y",
      "swpAllow": "Y",
      "planMode": "REGULAR",
      "dpId": "",
      "rtaName": "KFIN",
      "nomineeStatus": "Y",
      "kycStatus": "02",
      "bank": {
        "accountNo": "110004104281",
        "accountType": "SAVING",
        "name": "CANARA BANK",
        "branch": "",
        "city": "SURAT",
        "pincode": "",
        "micr": "0",
        "ifsc": "CNRB0017176",
        "neftIfsc": "CNRB0017176"
      }
    },
    {
      "amc": "RMF",
      "amcName": "NIPPON INDIA MUTUAL FUND",
      "folio": "477274856236",
      "investorName": "JYOTI HITESH SHAH",
      "age": 50,
      "mobile": "8401827921",
      "email": "shahhitesh5412@gmail.com",
      "taxStatus": "01",
      "modeOfHolding": "SINGLE",
      "transactionSource": "",
      "schemeCode": "SCGP",
      "schemeName": "NIPPON INDIA SMALL CAP FUND - GROWTH PLAN GROWTH OPTION",
      "schemeOption": "GROWTH",
      "idcwChangeAllowed": "False",
      "assetType": "EQUITY",
      "schemeType": "EQUITY",
      "nav": 150.1118,
      "navDate": "12-Feb-2025",
      "closingBalance": 127.262,
      "availableUnits": 127.262,
      "lienEligibleUnits": 0.012,
      "availableAmount": 19103.53,
      "currentMktValue": 19103.53,
      "costValue": 19499.09,
      "gainLoss": -395.56,
      "gainLossPercentage": -2,
      "lienUnitsFlag": "Y",
      "isin": "INF204K01HY3",
      "brokerCode": "ARN-0155",
      "brokerName": "NJ IndiaInvest Pvt Ltd",
      "decimalUnits": 3,
      "decimalAmount": 2,
      "decimalNav": 4,
      "isDemat": "N",
      "purAllow": "N",
      "redAllow": "Y",
      "swtAllow": "N",
      "sipAllow": "Y",
      "stpAllow": "Y",
      "swpAllow": "Y",
      "planMode": "Regular",
      "dpId": "",
      "rtaName": "KFIN",
      "nomineeStatus": "Y",
      "kycStatus": "02",
      "bank": {
        "accountNo": "110004104281",
        "accountType": "SAVING",
        "name": "CANARA BANK",
        "branch": "",
        "city": "SURAT",
        "pincode": "",
        "micr": "0",
        "ifsc": "CNRB0017176",
        "neftIfsc": "CNRB0017176"
      }
    }
  ]
}

```

## Key Observations about the API Structure

1. **RTA Differences**: Note that schemes from CAMS (Franklin Templeton, Kotak, SBI) and KFIN (Motilal Oswal, Nippon India) have slight differences in their data structure and field formats.
2. **Type Inconsistency**: Some fields appear as strings in some AMCs and as numbers in others (e.g., currentMktValue, nav).
3. **Format Variations**: Fields like mobile number have different formats (with/without country code).
4. **Field Availability**: Some fields are present in some schemes but not others.
5. **Case Variations**: Field values like "SINGLE" vs "Single" vary between RTAs.
6. **Plan Mode Representation**: "R" vs "REGULAR" for regular plans.

This comprehensive structure provides a consolidated view of an investor's mutual fund holdings across multiple AMCs and RTAs in India, making it a valuable resource for financial planning and portfolio analysis.