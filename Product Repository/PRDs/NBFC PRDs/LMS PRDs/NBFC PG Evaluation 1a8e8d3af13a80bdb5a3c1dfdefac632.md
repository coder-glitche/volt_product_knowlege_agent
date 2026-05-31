# NBFC PG Evaluation

Last Edited: April 8, 2025 1:06 PM
PRD Owner: Surya Ganesh

# Evaluation Criteria

## Business Criteria

| Parameter | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) |
| --- | --- | --- | --- | --- |
| Same day Settlements | No | No | No | No |
| UPI Commercials |  |  |  |  |
| Netbanking Commercials |  |  |  |  |
| VISA Commercials |  |  |  |  |
| Mastercard Commercials |  |  |  |  |
|  |  |  |  |  |

## Product Criteria

| Parameter | Priority | RazorPay | PhonePe | PayU + HDFC | Easebuzz |
| --- | --- | --- | --- | --- | --- |
| No user login (OTP) | High | No | Available (Standard checkout flow doesn't require user login) |  |  |
| Transaction level control on payment methods | High |  | Available (Can specify payment instruments in the payment initiation request) |  |  |
| Transaction level control on card networks | High |  | Available (Can filter specific card networks in payment instruments) |  |  |
| Customer name at transaction level | High |  |  |  |  |
| Backend callback post transaction level | High |  | Available (Via callbackUrl parameter in payment request) |  |  |
| Ability to whitelist multiple URLs | High |  | Available (Can configure multiple callback and redirect URLs) |  |  |
| White-labelling of checkout | High |  | Limited (PhonePe branded checkout but some customization options) |  |  |
| Error codes and reasons at transaction level | High |  | Available (Detailed error codes in status responses) |  |  |
| Settlement webhook | Medium |  | Available (Supports settlement notifications) |  |  |
| TPV check for UPI transactions | High |  | Available (Transaction status API provides verification) |  |  |
| TPV check for DC transactions | High |  | Available (Transaction status API provides verification) |  |  |
| TPV check for Netbanking transactions | High |  | Available (Transaction status API provides verification) |  |  |

## Operations Criteria

| Parameter | Priority | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) |
| --- | --- | --- | --- | --- | --- |
| Settlement timeline | High | No |  |  |  |
| SFTP based reports | High |  |  |  |  |
| Transaction MIS | High |  |  |  |  |
| Settlement MIS | High |  |  |  |  |
| Fee reconciliation | High |  |  |  |  |
|  | High |  |  |  |  |
|  |  |  |  |  |  |

## Tech Criteria

| Parameter | Priority | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) |
| --- | --- | --- | --- | --- | --- |
| Ease of integration | High | No |  |  |  |
| Documentation simplicity | High |  |  |  |  |
| Android SDK | High |  |  |  |  |
| iOS SDK | High |  |  |  |  |
| Web SDK | High |  |  |  |  |
|  | High |  |  |  |  |
|  |  |  |  |  |   |

## Evaluation

[PhonePe PG Evaluation](NBFC%20PG%20Evaluation/PhonePe%20PG%20Evaluation%201a8e8d3af13a80a7a82ad46ce300b9f8.md)

[PayU PG Evaluation](NBFC%20PG%20Evaluation/PayU%20PG%20Evaluation%201a8e8d3af13a80b2a91af5ad7f1462e8.md)

[Easebuzz PG Evaluation](NBFC%20PG%20Evaluation/Easebuzz%20PG%20Evaluation%201a8e8d3af13a80f494c8ec54aa7c5bf0.md)

[Razorpay PG Evaluation](NBFC%20PG%20Evaluation/Razorpay%20PG%20Evaluation%201a8e8d3af13a80cb907cce8d29a4f26b.md)