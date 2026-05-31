# Post loan Status APIs for MFD SaaS Partner Platform. Shortfall, Interest, Renewal

: Naman Agarwal
Created time: October 22, 2024 6:54 PM
Status: Done
Last edited: February 14, 2025 12:59 PM

# Product Requirements Document (PRD)

[API doc ](Post%20loan%20Status%20APIs%20for%20MFD%20SaaS%20Partner%20Platfor/API%20doc%20198e8d3af13a80b995eecf251432a056.md)

## **Project Title:**

**Development of External APIs for MFD Dashboard Integration**

---

## **1. Introduction**

This document outlines the requirements for developing a set of External APIs intended for MFD  platforms like redvision. These APIs will enable MFD partners to integrate with our system, allowing them to create comprehensive dashboards that provide essential customer data and financial metrics. The goal is to facilitate seamless data exchange, enhancing the operational efficiency and decision-making capabilities of our MFD partners

---

## **2. Objective**

To develop a suite of External APIs that replicate the functionalities of existing Internal APIs, providing MFD platforms with secure and efficient access to customer data related to active customers, shortfalls, interest dues, and renewals. These APIs will empower MFD partners to build detailed dashboards, enabling better management and support of their customer base.

---

## **3. Target Audience**

- **Primary Users:**
    - **MFD Platform Developers:** Responsible for integrating the External APIs into their dashboards.
    - **MFD Operations Teams:** Utilize the dashboards for monitoring and managing customer data.
- **Stakeholders:**
    - **Product Management Team**
    - **Development Team**
    - QA
    - **MFD SAAS Partners**

---

## **4. Scope**

### **In-Scope:**

- Development of four External APIs:
    1. **Get Active Customers**
    2. **Get Shortfall Details**
    3. **Get Interest Due Details**
    4. **Get Renewal Details**
- Documentation and specifications for each API.
- Implementation of business logic within each API.
- Security measures for data protection.

### **Out-of-Scope:**

- Development of UI components for MFD dashboards.
- Integration of common headers and authentication mechanisms (handled separately).

---

## **5. API Specifications**

### **5.1. Get Active Customers**

### **Endpoint:**

```
GET /v1/partner/platform/las/partner/{partnerAccountId}/activeCustomers?pageNumber={pageNumber}
```

### **Description:**

Retrieves a paginated list of active customers associated with a specific partner account. This API provides detailed customer information, including credit details and pledged portfolio items, enabling MFD partners to manage and support their active clientele effectively.

### **Parameters:**

- **Path Parameters:**
    - `partnerAccountId` (string, **required**): Unique identifier for the partner account.
- **Query Parameters:**
    - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve.

### **Response Payload:**

```json
{
  "activeCustomerDetails": [
    {
      "mobileNumber": "+919876501234",
      "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7",
      "email": "dummy@voltmoney.in",
      "pan": "AUWPA7175L",
      "dob": "30-03-1988",
      "creditDetails": {
        "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7",
        "creditType": "OVERDRAFT",
        "lenderCreditId": "9911725722",
        "lenderName": "Bajaj",
        "totalCreditAmount": 332300,
        "availableCreditAmount": 282300,
        "principalOutStandingAmount": 50000,
        "currentApplicableInterestRate": 9.95,
        "pledgedPortfolioAmount": 738723,
        "overUtilizationAmount": 0,
        "chargesDueAmount": null,
        "creditStatus": "ACTIVE",
        "processingCharges": 999,
        "interestDueAmount": null,
        "interestDueDate": "2023-05-07",
        "renewalDate": "2024-05-06 16:51:16.133",
        "pledgedPortfolioItems": [
          {
            "assetRepository": "KARVY",
            "amcName": null,
            "amcCode": null,
            "folioNo": "9048897656",
            "schemeCode": null,
            "schemeName": null,
            "isinNo": "INF846K01859",
            "schemeType": null,
            "totalAvailableUnits": 6371.203
          },
          {
            "assetRepository": "KARVY",
            "amcName": null,
            "amcCode": null,
            "folioNo": "7042093481",
            "schemeCode": null,
            "schemeName": null,
            "isinNo": "INF769K01010",
            "schemeType": null,
            "totalAvailableUnits": 1939.585
          },
          {
            "assetRepository": "KARVY",
            "amcName": null,
            "amcCode": null,
            "folioNo": "3002703269",
            "schemeCode": null,
            "schemeName": null,
            "isinNo": "INF843K01047",
            "schemeType": null,
            "totalAvailableUnits": 2816.244
          }
        ]
      }
    }
    // ... up to 20 customers per page
  ],
  "currentPageNumber": "1",
  "totalPages": "50"
}

```

### **Purpose of Data Fields:**

- **Customer Identification:**
    - `mobileNumber`, `email`, `pan`, `dob`: Essential for identifying and contacting the customer.
    - `voltCustomerCode`: Unique internal code for customer tracking.
- **Credit Details:**
    - `creditId`, `creditStatus`, `lendingPartnerId`, etc.: Provide comprehensive information about the customer's credit status and history, enabling MFD partners to assess creditworthiness and manage loans effectively.
- **Partner Information:**
    - `partnerAccountId`, `partnerName`, `partnerCode`, etc.: Ensures data is accurately associated with the correct MFD partner for tailored support.

---

### **5.2. Get Shortfall Details**

### **Endpoint:**

```
GET /v1/partners/{partnerAccountId}/shortfall?pageNumber={pageNumber}

```

### **Description:**

Retrieves a paginated list of customers experiencing shortfalls. A shortfall occurs when the Mutual Fund (MF) pledged collateral is lower than the disbursed loan amount, triggering specific actions to manage the deficit.

### **Parameters:**

- **Path Parameters:**
    - `partnerAccountId` (string, **required**): Unique identifier for the partner account.
- **Query Parameters:**
    - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve.

### **Response Payload:**

```json
{
  "shortfallDetails": [
    {
      "creditId": "8a800c4991a2837b0191a42e70d7320b",
      "lender": "Tata",
      "lenderCreditId": "31087",
      "lenderLoanAccountNumber": "28543",
      "accountHolderName": "Yuvraj Rajput",
      "accountHolderPhoneNumber": "919755419488",
      "accountHolderEmail": "rajputyuvraj484@gmail.com",
      "shortfallAmount": 4776,
      "dueAmount": 4776, // 
      "agingDays": 6,
      "status": "Open" // Possible values: Open, Cleared, Selloff Initiated
    }
    // ... up to 20 shortfall records per page
  ],
  "currentPageNumber": "1",
  "totalPages": "10"
}

```

### **Purpose of Data Fields:**

- **Shortfall Identification:**
    - `shortfallAmount`, `dueAmount`: Quantify the deficit that needs to be addressed.
    - `agingDays`: Tracks how long the shortfall has been open, ensuring timely resolution.
- **Customer and Credit Information:**
    - `creditId`, `lenderCreditId`, `lenderLoanAccountNumber`: Unique identifiers for tracking specific credit instances.
    - `accountHolderName`, `accountHolderPhoneNumber`, `accountHolderEmail`: Facilitate direct communication with the customer.
- **Partner and Platform Details:**
    - `partnerName`, `partnerEmail`, `partnerPhoneNumber`: Ensure that the data is correctly associated with the MFD partner responsible for managing the shortfall.
    - `platformName`: Identifies the platform through which the customer is engaged.
- **Status Tracking:**
    - `status`: Indicates the current state of the shortfall, enabling MFD partners to take appropriate actions such as initiating selloffs or marking shortfalls as cleared.

### **Business Logic:**

- **Shortfall Occurrence:**
    
    Triggered when the Loan-to-Value (LTV) ratio falls below 50% due to a decrease in the MF pledged collateral value.
    
- **Resolution Timeline:**
    - **7 Days:** The shortfall must be cleared within this period.
    - **Recovery:** If the portfolio value recovers, the shortfall status is updated to "Cleared."
    - **User Intervention:** If the user adds funds to cover the shortfall, selloffs are prevented.
    - **Persistent Shortfall:** If unresolved after 7 days, the system initiates a selloff, updating the status to "Selloff Initiated."

---

### **5.3. Get Interest Due Details**

### **Endpoint:**

```
GET /v1/partners/{partnerAccountId}/interestDue?pageNumber={pageNumber}

```

### **Description:**

Retrieves a paginated list of customers with pending interest payments. This API assists MFD partners in managing and tracking interest dues effectively.

### **Parameters:**

- **Path Parameters:**
    - `partnerAccountId` (string, **required**): Unique identifier for the partner account.
- **Query Parameters:**
    - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve.

### **Response Payload:**

```json
{
  "interestDueDetails": [
    {
      "creditId": "8a8010c48c3d694f018c3e9ff0f50476",
      "lender": "Bajaj",
      "lenderCreditId": "V402ALAS00133257",
      "lenderAccountNumber": "168804",
      "customerName": "SIVA PARVATHI ANUMOLU",
      "customerPhoneNumber": "919492267529",
      "customerEmail": "sivaparvathi.anumolu@gmail.com",
      "interestAmount": 444,
      "totalDues": 444,
      "interestPaymentStatus": "paid",
      "interestDueDate": "2023-05-07"
    },
  
    // ... up to 20 interest due records per page
  ],
  "currentPageNumber": 1,
  "totalPages": 5
}

```

### **Purpose of Data Fields:**

- **Interest Identification:**
    - `interestAmount`, `penalCharges`, `bounceCharges`, `totalDues`: Financial details essential for tracking the total amount owed by the customer.
- **Mandate Information:**
    - `mandateRegistrationStatus`, `mandatePresentationStatus`, `mandatePresentationDate`, `mandateFailureReason`: Indicates the status of the mandate required for automated interest payments, ensuring compliance and facilitating smooth transactions.
- **Customer and Credit Information:**
    - `creditId`, `lenderCreditId`, `lenderAccountNumber`: Unique identifiers for tracking specific credit instances.
    - `customerName`, `customerPhoneNumber`, `customerEmail`: Essential for identifying and contacting the customer regarding their interest dues.
- **Partner and Platform Details:**
    - `partnerType`, `partnerName`, `partnerPhoneNumber`, `partnerEmail`: Ensures that the data is accurately associated with the correct MFD partner for targeted support and communication.
- **Status Tracking:**
    - `interestPaymentStatus`: Indicates whether the interest has been paid, aiding in monitoring and follow-up actions.
    - `interestDueDate`: Specifies the deadline for interest payment, enabling timely reminders and actions.

### **Business Logic:**

- **Interest Due Management:**
    
    Tracks customers who have pending interest payments to ensure timely collections and maintain financial health.
    
- **Mandate Status Monitoring:**
    
    Ensures that mandates for automatic interest payments are registered and functioning correctly to minimize manual intervention.
    
- **Due Date Enforcement:**
    
    Helps MFD partners in reminding customers about upcoming or overdue interest payments, facilitating proactive management.
    

---

### **5.4. Get Renewal Details**

### **Endpoint:**

```
GET /v1/partners/{partnerAccountId}/renewal?pageNumber={pageNumber}

```

### **Description:**

Retrieves a paginated list of customers pending renewal for their loans. This API assists MFD partners in managing and tracking the renewal processes to prevent loan defaults.

### **Parameters:**

- **Path Parameters:**
    - `partnerAccountId` (string, **required**): Unique identifier for the partner account.
- **Query Parameters:**
    - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve.

### **Response Payload:**

```json
"renewalDetails": [
    {
      "creditId": "8a8016b98b72edd5018b75553fdd0096",
      "lender": "Bajaj",
      "lenderCreditId": "V402LAS00122678",
      "lenderLoanAccountNumber": "165693",
      "customerName": "VIJAYALAXMI BURA",
      "customerPhoneNumber": "919160045552",
      "customerEmail": "prakash9959968055@gmail.com",
      "pos": 0, // pos -> principle outstanding
      "dueDate": "2024-10-31"
    },
  
    // ... up to 20 renewal records per page
  ],
  "currentPageNumber": 1,
  "totalPages": 3
}

```

### **Purpose of Data Fields:**

- **Renewal Identification:**
    - `creditId`, `lenderCreditId`, `lenderLoanAccountNumber`: Unique identifiers for tracking specific credit instances requiring renewal.
- **Customer Information:**
    - `customerName`, `customerPhoneNumber`, `customerEmail`: Essential for identifying and contacting the customer regarding their loan renewal.
- **Borrower Details:**
    - `firstCoBorrower`, `secondCoBorrower`: Information about additional borrowers, if any, facilitating comprehensive renewal management.
- **Partner and Platform Details:**
    - `partnerName`, `partnerEmail`, `partnerPhoneNumber`: Ensures accurate association with the correct MFD partner responsible for managing the renewal.
    - `platformName`, `partnerAccountType`: Provides context about the platform and account type, aiding in tailored support.
- **Financial Information:**
    - `pos`: Point of Sale amount or related financial metric pertinent to the renewal process.
    - `dueDate`: Specifies the deadline for loan renewal, enabling timely reminders and actions.
- **Status Tracking:**
    - `status`: Indicates the current state of the renewal process (e.g., "Renewal done", "Not done - move to collections"), guiding necessary follow-up actions.
    - `owner`: Identifies the team member responsible for managing the renewal.
    - `mfdStatus`, `customerStatus`: Reflects the statuses from both the MFD and customer perspectives.
    - `nextFollowupDate`: Schedules future interactions if needed.
    - `alternateContactNumber`: Provides an alternative means of communication.
    - `cxComment`, `mfdComment`: Allows for contextual notes related to the renewal process.

### **Business Logic:**

- **Renewal Tracking:**
    
    Monitors loans approaching their renewal dates to ensure timely actions, reducing the risk of loan defaults.
    
- **Status Management:**
    - **"Renewal done":** Indicates successful renewal, allowing partners to update records accordingly.
    - **"Not done - move to collections":** Triggers collection actions if renewal is not completed by the due date.
    - **"Renewal application done":** Confirms that the renewal application has been submitted, prompting any necessary follow-ups.

---

## **6. Data Fields and Descriptions**

Detailed descriptions of all data fields used across the APIs have been provided within each API's response payload section. These fields are crucial for accurately representing customer and financial information, facilitating effective management by MFD partners.

---

## **7. Business Logic Integration**

Each API incorporates specific business logic tailored to the operational needs of MFD partners:

- **Shortfall Management:**
    
    Automates the identification and resolution of shortfalls, enforcing a 7-day clearance period with predefined actions based on the shortfall's status.
    
- **Interest Due Management:**
    
    Tracks pending interest payments, ensuring mandates are in place and payments are made on time to maintain financial stability.
    
- **Renewal Management:**
    
    Monitors upcoming loan renewals, automating follow-up actions and status updates to prevent defaults and ensure seamless loan continuations.
    

---

## **8. Success and Error Responses**

Each API will adhere to standard HTTP status codes to indicate the success or failure of requests:

- **Success Responses:**
    - `200 OK`: Request was successful, and the response payload contains the requested data.
- **Error Responses:**
    - `400 Bad Request`: The request was invalid or cannot be served. The exact error should be explained in the response.
    - `401 Unauthorized`: Authentication failed or user does not have permissions for the desired action.
    - `403 Forbidden`: Authentication succeeded but authenticated user does not have access to the requested resource.
    - `404 Not Found`: The requested resource could not be found.
    - `500 Internal Server Error`: An unexpected condition was encountered.

**Note:** Error responses will include a descriptive message to aid in troubleshooting but will not expose sensitive system details.

---

## **9. Timeline/Milestones**

| Milestone | Description | Completion Date |
| --- | --- | --- |
| **PRD Approval** | Finalize and approve the PRD |  |
| **API Design Completion** | Detailed API design and data modeling |  |
| **Development Phase** | Coding of the APIs |  |
| **Internal Testing** | Quality Assurance and functional testing |  |
|  |  |  |

**Note:** Specific dates to be determined based on project kickoff and resource availability.

---

## **11. Acceptance Criteria**

- **Functionality:**
    - Each API must return the correct data as per the specifications.
    - Pagination must work correctly, returning accurate `currentPageNumber` and `totalPages`.
- **Performance:**
    - APIs should respond within acceptable time frames (e.g., < 500ms for successful requests).
- **Security:**
    - Only authenticated and authorized requests should access the APIs.
    - Sensitive data must be encrypted in transit.
- **Reliability:**
    - APIs should have high uptime (e.g., 99.9% availability).
- **Documentation:**
    - Comprehensive and clear documentation must be available for all APIs.
- **Error Handling:**
    - APIs must return appropriate error messages and status codes for various failure scenarios.

---

## **12. Appendices/References**

- **Internal API Documentation:** Reference to existing internal APIs for data consistency. [https://api.staging.voltmoney.in/swagger-ui/index.html#/Partner reporting/getShortfallDueUsingPOST](https://api.staging.voltmoney.in/swagger-ui/index.html#/Partner%20reporting/getShortfallDueUsingPOST)
- **Data Models:** Detailed schemas for customer, shortfall, interest due, and renewal data.
- **Security Guidelines:** OAuth 2.0 implementation and data protection standards.
- **API Documentation Tools:** Links to Swagger/Postman documentation guides. [https://documenter.getpostman.com/view/22301608/2s93eYTrMd#fb823457-4ca2-4854-9923-b277b6d3abb7](https://documenter.getpostman.com/view/22301608/2s93eYTrMd#fb823457-4ca2-4854-9923-b277b6d3abb7)

---

# Summary

This PRD provides a comprehensive blueprint for developing External APIs tailored for MFD platforms to create effective dashboards. By outlining the endpoints, data structures, business logic, and acceptance criteria, developers are equipped with clear guidance to implement the required functionalities. Emphasizing simplicity and relevance, the APIs focus on delivering essential customer and financial data, ensuring that MFD partners can manage their operations efficiently and securely.

# Development and Testing Checklist

## Get Active Customers API

| Development Task | Test Requirement | Dev ✓ | ✓ |
| --- | --- | --- | --- |
| Implement GET endpoint `/v1/partner/platform/las/partner/{partnerAccountId}/activeCustomers` | Verify endpoint accessibility and correct HTTP method | □ | □ |
| Add pagination logic with default page size of 20 | Test different page numbers and verify correct data segmentation | □ | □ |
| Implement customer data retrieval with all required fields | Validate all fields present in response: mobile, email, PAN, DOB | □ | □ |
| Add credit details calculation logic | Verify credit amounts, interest rates, and status accuracy | □ | □ |
| Implement pledged portfolio items aggregation | Check portfolio items list completeness and accuracy | □ | □ |
| Add data validation for required fields | Test with missing/invalid fields | □ | □ |
| Implement error handling for invalid partnerAccountId | Verify 404 response for non-existent partner | □ | □ |

## Get Shortfall Details API

| Development Task | Test Requirement | Dev ✓ | QA ✓ |
| --- | --- | --- | --- |
| Implement GET endpoint `/v1/partners/{partnerAccountId}/shortfall` | Verify endpoint accessibility | □ | □ |
| Add shortfall calculation logic | Test shortfall amount calculation accuracy | □ | □ |
| Implement aging days calculation | Verify correct aging days computation | □ | □ |
| Add status transition logic (Open → Cleared → Selloff) | Test all status transitions | □ | □ |
| Implement 7-day resolution timer | Verify timer accuracy and triggers | □ | □ |
| Add selloff initiation logic | Test automatic selloff after 7 days | □ | □ |
| Implement pagination for shortfall records | Verify page size and navigation | □ | □ |

## Get Interest Due Details API

| Development Task | Test Requirement | Dev ✓ | QA ✓ |
| --- | --- | --- | --- |
| Implement GET endpoint `/v1/partners/{partnerAccountId}/interestDue` | Verify endpoint accessibility | □ | □ |
| Add interest calculation logic | Test interest amount accuracy | □ | □ |
| Implement due date tracking | Verify due date accuracy and updates | □ | □ |
| Add mandate status tracking | Test all mandate status scenarios | □ | □ |
| Implement payment status updates | Verify payment status changes | □ | □ |
| Add total dues calculation | Test total dues computation | □ | □ |
| Implement pagination for interest records | Verify pagination functionality | □ | □ |

## Get Renewal Details API

| Development Task | Test Requirement | Dev ✓ | QA ✓ |
| --- | --- | --- | --- |
| Implement GET endpoint `/v1/partners/{partnerAccountId}/renewal` | Verify endpoint accessibility | □ | □ |
| Add renewal date tracking | Test renewal date accuracy | □ | □ |
| Implement lender-specific logic (Bajaj/Tata) | Verify different lender flows | □ | □ |
| Add POS (Principal Outstanding) calculation | Test POS calculation accuracy | □ | □ |
| Implement status management | Verify all status transitions | □ | □ |
| Add follow-up date tracking | Test follow-up date functionality | □ | □ |
| Implement pagination for renewal records | Verify pagination works correctly | □ | □ |

## Common Implementation Requirements

| Development Task | Test Requirement | Dev ✓ | QA ✓ |
| --- | --- | --- | --- |
| Implement OAuth 2.0 authentication | Test authentication flow and token handling | □ | □ |
| rate limit | Verify rate limit enforcement | □ | □ |
| Implement error handling | Test all error scenarios and messages | □ | □ |
| Add request validation | Verify input validation and error responses | □ | □ |
| Implement logging | Check log entries for all operations | □ | □ |
| Add monitoring metrics | Verify metric collection | □ | □ |
| Implement caching strategy | Test cache hit/miss scenarios | □ | □ |

## Security Requirements

| Development Task | Test Requirement | Dev ✓ | QA ✓ |
| --- | --- | --- | --- |
| Implement data encryption | Verify data encryption in transit | □ | □ |
| Add input sanitization | Test against injection attacks | □ | □ |
| Implement XSS protection | Verify XSS prevention | □ | □ |
| Add CSRF protection | Test CSRF token handling | □ | □ |
| Implement role-based access | Verify permission enforcement | □ | □ |
| Add security headers | Check security header presence | □ | □ |
| Implement audit logging | Verify audit trail completeness | □ | □ |

## Documentation Requirements

| Development Task | Test Requirement | Dev ✓ | QA ✓ |
| --- | --- | --- | --- |
| Create API documentation | Verify documentation accuracy | □ | □ |
| Add code comments | Check code documentation | □ | □ |
| Create example requests/responses | Test example validity | □ | □ |
| Document error codes | Verify error documentation | □ | □ |
| Add integration guide | Test integration instructions | □ | □ |
| Create postman collection | Verify postman collection works | □ | □ |
| Add swagger documentation | Test swagger UI functionality | □ | □ |

### Usage Instructions:

1. Developers should check off tasks in the "Dev ✓" column as they complete them
2. QA should verify each task and check off in the "QA ✓" column
3. Any failed tests should be marked with an "✗" and documented
4. Additional notes or issues can be added below each section as needed

### Definition of Done:

- All checkboxes in both the Dev and QA columns are checked
- No critical or high-severity bugs remain
- All performance metrics meet the requirements
- Documentation is complete and accurate
- Code review has been completed
- All tests are passing in a staging environment

Active customers 

- Customer identification
- Customer Credit status
- Customer available credit

Renewal 

- bjaja
    - App
- tata
    - Support -  message