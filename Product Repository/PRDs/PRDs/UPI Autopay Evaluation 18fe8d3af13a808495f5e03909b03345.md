# UPI Autopay Evaluation

: Nihal Simha M S
Created time: February 3, 2025 3:30 PM
Status: In progress
Last edited: February 12, 2025 6:14 PM

# Overview

UPI Autopay is a digital payment solution introduced by NPCI to enable seamless, recurring payments through Unified Payments Interface (UPI). It allows users to set up automatic debits for subscriptions, EMIs, utility bills, insurance, and other recurring expenses without manual intervention.

Merchants can integrate UPI Autopay to ensure frictionless collections, improve customer retention, and reduce payment failures.

Key evaluation criteria include commercials, performance metrics, ease of integration, reconciliation processes, and support availability. Comparison across providers like PhonePe and Razorpay helps determine the best solution based on reliability, cost, and performance.

# PhonePe Evaluation Report

[PhonePe UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/PhonePe%20UPI%20Autopay%20Evaluation%20190e8d3af13a80a59b09d18401c8fd89.md)

| **Criteria** | **Priority** | **Expectations** | **Comments** |
| --- | --- | --- | --- |
| Commercials for registration | High |  | Need to confirm |
| Commercials for presentation | High |  | Need to confirm |
| Settlement timelines | High | T+0 / T+1 | Needs confirmation |
| Registration API performance | High | 95p TAT < 100ms | Not explicitly stated in docs, need benchmarks |
| Pre-debit API performance | High | 95p TAT < 100ms | Needs performance validation |
| Presentation API performance | High | 95p TAT < 100ms | Needs performance validation |
| Ease of integration | High | Yes (2 weeks - 2 devs) | APIs are well-defined, should be achievable |
| Post-integration support | High | PhonePe support required | Need clarity on support SLAs |
| SDKs available | High | Java, Python | APIs are also available |
| Registration modes | High | - Intent  - QR  - Collect | Intent and Collect supported, QR we need to convert |
| Debit & Pre-debit orchestration | High | Managed by PhonePe & Merchant can also handle | APIs allow merchant to trigger debit |
| Registration Error Codes | High | Not provided in documentation | Need list from PhonePe |
| Pre-debit Error Codes | High | Not provided in documentation | Need list from PhonePe |
| Presentation Error Codes | High | Not provided in documentation | Need list from PhonePe |
| Transaction reconciliation | High | MIS reports for presentation |  |
| Settlement reconciliation | High | MIS reports for settlement |  |
| Registration reconciliation | High | MIS reports for registration |  |
| Mandate Expiry Handling | High | Notifications before expiry & expired | Not available. |
| Mandate Pause & Resume | High | APIs to pause & resume mandates | Not available. Need confirmation from PhonePe. |
| Multi-TPAP Support | High | Support for multiple PSPs | Android - Yes
iOS - Only Gpay, Paytm & Phonepe |
| Refund & Chargeback Handling | High | Process for disputes & refunds | Need clarity on TAT and escalation |
| Auto-Debit Failure Handling | High | Retry mechanism & fallback options | Need confirmation on auto-retry policy |
| Custom Notifications & Alerts | Medium | Webhooks | Need to validate available event webhooks |

# Razorpay Evaluation Report

[Razorpay UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/Razorpay%20UPI%20Autopay%20Evaluation%20190e8d3af13a80b69d76c6a0f92093d5.md)

|  | Priority | PhonePe | Razorpay |
| --- | --- | --- | --- |
| Commercials for registration | High |  |  |
| Commercials for presentation | High |  |  |
| Settlement timelines | High |  |  |
| Acquirer Bank (SRs) | High |  |  |
| Registration performance | High |  |  |
| Pre-debit performance | High |  |  |
| Presentation performance | High |  |  |
| Ease of integration | High |  |  |
| Post-integration support | High |  |  |
| SDKs available | High |  |  |
| Registration modes | High |  |  |
| Debit & Pre-debit orchestration | High |  |  |
| Registration Error Codes | High |  |  |
| Pre-debit Error Codes | High |  |  |
| Presentation Error Codes | High |  |  |
| Transaction reconciliation | High |  |  |
| Settlement reconciliation | High |  |  |

# Takeaways