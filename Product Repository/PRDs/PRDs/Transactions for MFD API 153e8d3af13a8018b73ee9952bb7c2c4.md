# Transactions for MFD API

: Naman Agarwal
Created time: December 5, 2024 12:29 PM
Status: In progress
Last edited: January 16, 2025 7:45 PM

# PRD: Partner-Level Transaction API

## Overview

New API endpoint to provide aggregated transaction data at partner level for all customers under a specific partner to address transaction duplication issues.

## Business Context

- Need to provide accurate transactions to partner MFDs
- Currently experiencing transaction duplication issues
- Need consolidated partner-level view instead of customer-level only
- Support platforms with multiple partners and customers

We recreate our transaction Db with different txn ID every day.

Redvision does not have a sophisticated dedupe check , causing transactions to get duplicated multiple time ~avg 2.7 time , highest 28+ count. https://voltmoney.atlassian.net/browse/VSSB-398

This is a major escalations from the redvision, as the daily transaction sync with the with redvision will be unfeasible they requested partner level API to full from our DB.

## API Specification

### Endpoint

`GET /v1/partner/platform/transactions`

### Headers

| Header | Description | Required | Example |
| --- | --- | --- | --- |
| X-AppPlatform | Platform identifier | Yes | FUNDS_INDIA |
| requestReferenceId | Unique request ID | Yes | b2595c8c-a163-4072 |
| Content-Type | Content type | Yes | application/json |

### Request Parameters

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| fromDate | String | Yes | Start date | "2024-01-01" |
| toDate | String | Yes | End date | "2024-01-31" |
| volt_Partner_id | String | Yes | Partner identifier | "PARTNER123" |
| format | String | No | Response format | "JSON" |

### Response Structure

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| status | String | Yes | Response status (SUCCESS/ERROR) |
| partnerDetails.partnerId | String | Yes | Unique partner identifier |
| partnerDetails.partnerName | String | Yes | Partner name |
| partnerDetails.totalCustomers | Number | Yes | Total customers count |
| transactions[].transactionId | String | Yes | Unique transaction ID |
| transactions[].voltcustomerCode | String | Yes | Customer identifier |
| transactions[].description | String | Yes | Transaction description |
| transactions[].amount | Number | Yes | Transaction amount |
| transactions[].transactionStatus | String | Yes | SETTLED/PENDING_SETTLEMENT |
| transactions[].transactionType | String | Yes | CREDIT/DEBIT |
| transactions[].settledOn | Number | Yes | Settlement timestamp |
| transactions[].createdOn | Number | Yes | Creation timestamp |
| transactions[].lastUpdatedOn | Number | Yes | Last update timestamp |
| transactions[].UTR | String | No | Unique Transaction Reference |

## Key Requirements

- Prevent duplicate transactions
- Support date range filtering
- Include all transaction types and statuses
- Include customer identification in transactions
- Track UTR for transaction reconciliation

##