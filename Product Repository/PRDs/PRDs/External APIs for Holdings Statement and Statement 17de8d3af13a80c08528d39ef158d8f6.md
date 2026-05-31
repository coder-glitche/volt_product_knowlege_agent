# External APIs for Holdings Statement and Statement of Accounts (SOA)

: Naman Agarwal
Created time: January 16, 2025 7:49 PM
Status: In progress
Last edited: January 16, 2025 7:53 PM

External APIs for Holdings Statement and Statement of Accounts (SOA)

---

## 1. Introduction

This document outlines the requirements for developing external APIs that will provide Holding Statements and Statement of Accounts (SOA) to MFD partners. These APIs will enable partners to access comprehensive financial statements and holdings data for their customers, enhancing transparency and operational efficiency.

## 2. Objective

To develop robust external APIs that provide detailed holdings statements and transaction histories, allowing MFD partners to:

- Access real-time holdings data
- Retrieve historical transaction statements
- Generate comprehensive financial reports
- Support customer portfolio management

## 3. Target Audience

### Primary Users

- MFD Platform Developers
- MFD Operations Teams
- MFDs

## 4. Scope

### In-Scope

- Development of two primary APIs:
    1. Get Holdings Statement API
    2. Get Statement of Accounts (SOA) API
- Documentation and specifications
- Data validation and error handling
- Integration with existing systems like Invest well dashboard

### 

## 5. API Specifications

### 5.1. Get Holdings Statement API

### Endpoint

```
GET /v1/partners/{partnerAccountId}/holdings?date={date}

```

### Description

Retrieves a comprehensive holdings statement for a specific date, showing all active mutual fund investments and their current values.

### Parameters

- **Path Parameters:**
    - `partnerAccountId` (string, required): Unique identifier for the partner account
- **Query Parameters:**
    - `date` (string, optional, format: YYYY-MM-DD): Date for which holdings are requested. Defaults to current date

### Response Payload

```json
{
  "holdingsStatement": {
    "statementDate": "2025-01-16",
    "customerDetails": {
      "name": "Shubham Kapoor",
      "accountNumber": "30345",
      "pan": "AUWPA7175L"
    },
    "holdings": [
      {
        "folioNumber": "1041038180",
        "schemeName": "Aditya Birla Sun Life Flexi Cap Fund",
        "isinCode": "INF209K01AJ8",
        "units": 22.7620,
        "navValue": 1670.00,
        "currentValue": 38021.64,
        "lienMarked": true,
        "lienQuantity": 22.7620,
        "lienMarkingDate": "2024-09-14"
      }
    ],
    "summaryMetrics": {
      "totalPortfolioValue": 2454930.52,
      "totalLienMarkedValue": 801000.00,
      "availableValue": 1653930.52
    }
  }
}

```

### 5.2. Get Statement of Accounts (SOA) API

### Endpoint

```
GET /v1/partners/{partnerAccountId}/soa?startDate={startDate}&endDate={endDate}

```

### Description

Retrieves a detailed statement of accounts showing all transactions within the specified date range.

### Parameters

- **Path Parameters:**
    - `partnerAccountId` (string, required): Unique identifier for the partner account
- **Query Parameters:**
    - `startDate` (string, required, format: YYYY-MM-DD): Start date for the statement period
    - `endDate` (string, required, format: YYYY-MM-DD): End date for the statement period

### Response Payload

```json
{
  "statementOfAccounts": {
    "periodStart": "2024-07-01",
    "periodEnd": "2025-01-16",
    "customerDetails": {
      "name": "Shubham Kapoor",
      "accountNumber": "30345",
      "pan": "AUWPA7175L"
    },
    "transactions": [
      {
        "date": "2024-07-02",
        "transactionType": "DEBIT",
        "description": "Processing Fee",
        "amount": 1355.82,
        "balance": 1705.82
      }
    ],
    "summaryMetrics": {
      "openingBalance": 0.00,
      "closingBalance": 107487.00,
      "totalDebits": 801000.00,
      "totalCredits": 693513.00
    }
  }
}

```

## 6. Business Logic

### Holdings Statement

- Calculate current portfolio value using latest NAV
- Track lien marking status and quantities
- Compute available balance after lien
- Handle multiple folios per scheme
- Update values daily based on NAV changes

### Statement of Accounts

- Track all financial transactions
- Calculate running balances
- Categorize transaction types
- Handle multiple transaction dates
- Support date range queries
- Maintain audit trail

## 

## 7. Error Handling

### Standard HTTP Status Codes

- 200: Successful request
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 429: Too many requests
- 500: Internal server error

### Error Response Format

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {
      "field": "Additional error context"
    }
  }
}

```

## 

## 8. Documentation Requirements

- API specifications (Swagger/OpenAPI)
- Integration guide
- Sample requests and responses
- Error code reference
- Testing guidelines
- Security implementation guide

## 9. Success Criteria

- All APIs fully functional and documented
- Performance metrics met
- Security requirements implemented
- Partner integration successful
- Zero critical bugs
- Documentation complete
- Testing passed

---

# Development Checklist

## Holdings Statement API

- [ ]  Implement GET endpoint
- [ ]  Add portfolio calculation logic
- [ ]  Implement lien tracking
- [ ]  Add NAV updates
- [ ]  Implement data validation
- [ ]  Add error handling
- [ ]  Implement caching
- [ ]  Add security measures
- [ ]  Create documentation
- [ ]  Perform testing

## Statement of Accounts API

- [ ]  Implement GET endpoint
- [ ]  Add transaction tracking
- [ ]  Implement balance calculation
- [ ]  Add date range filtering
- [ ]  Implement data validation
- [ ]  Add error handling
- [ ]  Implement caching
- [ ]  Add security measures
- [ ]  Create documentation
- [ ]  Perform testing