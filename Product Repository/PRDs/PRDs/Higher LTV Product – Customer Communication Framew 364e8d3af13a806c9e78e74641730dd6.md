# Higher LTV Product – Customer Communication Framework

: Ameya Aglawe
Created time: May 18, 2026 10:02 AM
Status: Pending Review
Last edited: May 23, 2026 9:07 PM

# Background

As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings.

Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements:

1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow.
2. Customers must be notified once their revised credit limit is successfully updated.
3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey.

---

# Proposed Solution

## 1. NBFC (DSP) Communications

From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow.

The communication will serve the following purposes:

- Inform customers regarding successful limit enhancement
- Share revised loan documentation for customer reference
- Ensure regulatory and audit compliance for executed agreements

### Communication Channels

- Email
- SMS

---

### DSP Email Communication

| Field | Details |
| --- | --- |
| Communication Trigger | Successful completion of LTV update flow |
| Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement |
| Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 |
| Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit |
| Attachments | Loan kit (KFS + Amendment) |

---

### DSP SMS Communication

| Field | Details |
| --- | --- |
| Communication Trigger | Successful completion of LTV update flow |
| Purpose | Notify customer regarding successful credit limit enhancement |
| Template ID | 1107177910598106787 |
| Tempalte Name | LTV_Update_Limit_enhancement_V2 |
| Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} |
| VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} |

---

# 2. LSP (Volt) Communications

From the LSP side, communications will focus on:

- Promoting the Higher LTV offering to eligible customers
- Providing request status updates during the LTV enhancement journey
- Improving customer awareness and feature adoption

### Communication Channels

- In-app banners
- Email
- SMS

---

## Promotion Strategy

Volt will use contextual in-app banners and campaign placements to promote the Higher LTV feature to eligible customers.

- The banners shall communicate:
    - Availability of enhanced credit limit
    - Limited-period or eligible-offer messaging
    - Simplified customer journey with minimal action required
- Banner presentation logic:
    - Banner should be shown to all Volt user unless -
        - A service request for the loan account is already in progress
        - Difference in DP by shifting to higher LTV product < Rs 10,000
        - The loan account is already on the higher LTV product

---

## Status Notification Framework

Volt will send transactional communications during key stages of the LTV enhancement flow.

Indicative statuses include:

- Request Initiated
- Request Successful
- Request Failed

---

### Volt Email Communications

| Field | Details |
| --- | --- |
| Communication Trigger | Request placed |
| Purpose | Keep customer informed that the limit increase request is placed |
| Template ID | d-2402ff0e00ee4ad9a1a013219dba06b0 |
| Variables | lenderLogoUrl, customername, lan, existing_credit_limit, additional_credit_limit, updated_credit_limit, supportEmail, contactnumber |

| Field | Details |
| --- | --- |
| Communication Trigger | Request successful |
| Purpose | Keep customer informed that the limit increase request is processed successfully |
| Template ID | d-aa69c9c04f6040aea53b6afbd3188cf7 |
| Variables | lenderLogoUrl, customername, lan, existing_credit_limit, additional_credit_limit, updated_credit_limit, supportEmail, contactnumber |

| Field | Details |
| --- | --- |
| Communication Trigger | Request failed |
| Purpose | Keep customer informed that the limit increase request is failed |
| Template ID | d-6d3e6e5c71ce4b8a97570a9dc326d936 |
| Variables | lenderLogoUrl, customername, lan, existing_credit_limit, additional_credit_limit, updated_credit_limit, supportEmail, contactnumber |

---

### Volt SMS Communications

| Field | Details |
| --- | --- |
| Communication Trigger | Request placed |
| Purpose | Keep customer informed that the limit increase request is placed |
| Template ID | 1107177909347828148 |
| Template Name | line_increase_ltv_update_request_placed |
| Copy | Your request to increase the credit limit to Rs {{updated_credit_limit}} for loan account {{lan}} has been received and is currently under progress.  |
| VilPower Copy | Your request to increase the credit limit to Rs {#alphanumeric#} for loan account {#alphanumeric#} has been received and is currently under progress. -VOLT |

| Field | Details |
| --- | --- |
| Communication Trigger | Request successful |
| Purpose | Keep customer informed that the limit increase request is processed successfully |
| Template ID | 1107177909389013184 |
| Template Name | line_increase_ltv_update_request_successful |
| Copy | Congratulations, your credit limit has been successfully updated to Rs {{updated_crediit_limit}} for loan account {{lan}}.  |
| VilPower Copy | Congratulations, your credit limit has been successfully updated to Rs {#alphanumeric#} for loan account {#alphanumeric#}. -VOLT |

| Field | Details |
| --- | --- |
| Communication Trigger | Request failed |
| Purpose | Keep customer informed that the limit increase request is failed |
| Template ID | 1107177909400234566 |
| Template Name | line_increase_ltv_update_request_failed |
| Copy | We were unable to process your credit limit increase request for loan account {{lan}} this time. Please try again later through the Volt Money app. |
| VilPower Copy | We were unable to process your credit limit increase request for loan account {#alphanumeric#} this time. Please try again later through the Volt Money app. -VOLT |

---

# Summary

| Entity | Communication Purpose | Channels |
| --- | --- | --- |
| DSP (NBFC) | Regulatory/customer confirmation post successful enhancement | Email, SMS |
| Volt (LSP) | Feature promotion and customer journey status updates | Banner, Email, SMS |