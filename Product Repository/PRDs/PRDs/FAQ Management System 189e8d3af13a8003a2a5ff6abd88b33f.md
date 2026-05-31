# FAQ Management System

: Ranjan kumar Singh
Created time: January 28, 2025 2:07 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# FAQ Management System PRD

## 1. Problem Statement

We need a flexible FAQ management system that allows:

- Dynamic content updates without code deployment
- Categorized display of FAQs
- Multi-language support
- Easy maintenance by non-technical teams

## 2. Goals & Success Metrics

### Primary Goals

- Reduce customer support tickets volume by 30%

### Success Metrics

- FAQ usage analytics
    - Improve FAQ content quality through user feedback
    - Identify gaps in documentation/support
    - Increase user satisfaction
    - Track FAQ effectiveness
- Reduction in support tickets

## 3. Technical Requirements

### 3.1 Content Management

```sql
Table: faq_content
- id (PK)
- category_id (FK)
- question
- answer
- language_code
- status (ACTIVE/INACTIVE)
- created_at
- updated_at
- last_updated_by

```

### 3.2 Category Management

```sql
Table: faq_categories
- id (PK)
- name
- description
- display_order
- status
- parent_category_id (for sub-categories)

```

### 3.3 Language Support

```sql
Table: supported_languages
- language_code (PK)
- language_name
- status
- rtl_support

```

## 4. Feature Requirements

### 4.1 Admin Panel Features

1. Content Management
    - CRUD operations for FAQs
    - Version history
2. Category Management
    - Create/edit categories: should be able to create the new FAQ category
    - Reorder categories : Should be able to set the order of category and will be shown on UI in same order
    - Category status toggle: Show hide on UI
3. Language Management
    - Add new languages
    - Translation management
    - Default language setting

### 4.2 User Interface Features

1. FAQ Display
    - Categorized view
    - Search functionality
    - Language selector
2. Navigation
    - Category filters
    - Breadcrumb navigation
    - Back to top button
3. Content Features
    - Rich text support
    - Image/video embedding
    - Link handling

## 5. API Structure

### 5.1 Content APIs

```json
GET /api/v1/faqs
{
  "category": "withdrawal",
  "language": "hi",
  "search": "optional_search_term"
}

Response:
{
  "category": {
    "id": "withdrawal",
    "name": "Withdrawal",
    "faqs": [
      {
        "id": "w1",
        "question": "When will I receive funds?",
        "answer": "During banking hours...",
        "last_updated": "timestamp",
        "last_updated_by": "Ranjan kumar singh"
      }
    ]
  }
}

```

### 5.2 Admin APIs

```json
POST /api/v1/admin/faqs
{
  "question": {
    "en": "English question",
    "hi": "Hindi question"
  },
  "answer": {
    "en": "English answer",
    "hi": "Hindi answer"
  },
  "category_id": "withdrawal",
  "status": "ACTIVE"
}

```

## 6. Content Update Workflow

1. Content Creation
    
    ```mermaid
    graph TD
    A[Create Content] --> B[Add Translations]
    B --> C[Preview]
    C --> D[Publish]
    
    ```
    
2. Content Update
    
    ```mermaid
    graph TD
    A[Edit Content] --> B[Update Translations]
    B --> C[Review Changes]
    C --> D[Publish Updates]
    
    ```
    

## 7. Language Implementation

### 7.1 Supported Languages (Phase 1)

- English (Default)
- Hindi

### 7.2 Translation Process

1. Base content in English
2. Translation management system
3. Review process
4. Publish workflow

## 8. Analytics Requirements

### 8.1 Track

- Most viewed FAQs
- Search terms
- Language preferences
- Time spent on FAQ
- Feedback ratings
    - Feedback rating requirements
        
        ### 1.1 Purpose
        
        To implement a feedback system that allows users to indicate whether FAQ answers were helpful (thumbs up/down), enabling continuous improvement of FAQ content and user experience.
        
        ### 1.2 Business Goals
        
        - Improve FAQ content quality through user feedback
        - Identify gaps in documentation/support
        - Reduce support ticket volume
        - Increase user satisfaction
        - Track FAQ effectiveness
        
        ## 2. Technical Architecture
        
        ### 2.1 Database Schema
        
        ```json
        -- Main FAQ table
        CREATE TABLE faqs (
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            category VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            status ENUM('active', 'inactive', 'draft') DEFAULT 'active'
        );
        
        -- Feedback table
        CREATE TABLE faq_feedback (
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            faq_id BIGINT NOT NULL,
            is_helpful BOOLEAN NOT NULL,
            user_identifier VARCHAR(255),
            session_id VARCHAR(255),
            device_id VARCHAR(255),
            ip_address VARCHAR(45),
            platform VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            comments TEXT,
            FOREIGN KEY (faq_id) REFERENCES faqs(id)
        );
        
        -- Analytics table for aggregated metrics
        CREATE TABLE faq_analytics (
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            faq_id BIGINT NOT NULL,
            total_views INT DEFAULT 0,
            helpful_count INT DEFAULT 0,
            not_helpful_count INT DEFAULT 0,
            last_calculated_at TIMESTAMP,
            FOREIGN KEY (faq_id) REFERENCES faqs(id)
        );
        ```
        
        ## 3. Features & Requirements
        
        ### 3.1 User Interface
        
        1. Feedback Collection
            - Simple thumbs up/down buttons below each FAQ
            - Optional comment field appears after thumbs down
            - Clear visual feedback on button press
            - Disable buttons after voting
        2. UI States
            - Default state: Both buttons enabled
            - Voted state: Selected button highlighted, both disabled
            - Loading state: Visual indicator during API call
            - Error state: Error message with retry option
        
        ### 3.2 API Endpoints
        
        ### Submit Feedback
        
        ```json
        POST /api/v1/faq-feedback
        Request:
        {
            faqId: number,
            isHelpful: boolean,
            sessionId: string,
            deviceId?: string,
            comments?: string
        }
        
        Response:
        {
            success: boolean,
            message: string,
            feedbackId: number
        }
        ```
        
        Get Feedback Stats
        
        ```json
        GET /api/v1/faq/{faqId}/stats
        Response:
        {
            totalVotes: number,
            helpfulPercentage: number,
            helpfulCount: number,
            notHelpfulCount: number,
            lastUpdated: string
        }
        ```
        

## Amplitude events:

| Journey | User action | Event name | Event property | Expected value | User property |
| --- | --- | --- | --- | --- | --- |
| User lands on my account page | User click on Help and Support CTA | HELP_AND_SUPPORT_BUTTON_CLICKED | source | lms/los |  |
|  | User lands on help and support landing page | HELP_AND_SUPPORT_PAGE_VIEWED |  |  |  |
|  | User selects category to get the help with | HELP_AND_SUPPORT_CATEGORY_SELECTED | category | cash_withdrawal / repayments / interest_and_charges / collateral / service_request |  |
|  | User selected FAQ after selecting the category | FAQ_SELECTED | question | How to withdraw funds? |  |
|  | User click on Yes/No button on FAQ content page | FAQ_QUERY_RESOLVED | result | Yes/No |  |
|  |  |  | question | How to withdraw funds? |  |
|  | User selected NO and share feedback | FAQ_NO_REASON | remarks | {{Feedback written by user after selecting no}} |  |
|  | When user click CTA “Proceed to close account” on foreclosure FAQ content page | PROCEED_TO_CLOSE_LOAN_BUTTON_CLICKED |  |  |  |