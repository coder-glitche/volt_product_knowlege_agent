# Cashfree PG integration

: Ameya Aglawe
Created time: July 18, 2025 2:40 PM
Status: Pending Review
Last edited: August 5, 2025 3:56 PM

# **What problem are we solving?**

---

- Our current payment infrastructure depends entirely on Razorpay as the sole gateway for processing repayment transactions. This creates a critical single point of failure - if Razorpay experiences service disruptions, our entire repayment collection system becomes unavailable (users are not comfortable with VA payments), directly impacting cash flow and customer experience.
- Several of our partner LSPs are hesitant or unwilling to implement Cashfree PG integration due to various business considerations, including competitive concerns and strategic partnerships.

# **How do we measure success?**

---

| **Metric** | **Definition** | **Measurement Method** | Expectations |
| --- | --- | --- | --- |
| Transaction Success Rate | Percentage of successfully completed repayment transactions out of the total initiated transactions. | Payment gateway reports, backend logs, analytics tools | 97% or higher |
| User Drop-off Rate | Percentage of users who abandon the repayment process before completing the transaction. | Funnel analysis, session tracking | 3% or lower |
| Retry Rate | Percentage of transactions that required a retry due to temporary failures (e.g., network issues, timeouts). | Transaction logs, number of transactions in an order | 2-3% or lower |
| API Latency | Average response time of APIs involved in the repayment process (e.g., transaction initiation, status update, confirmation). | API monitoring tools, backend logs | < 500ms |
| Transaction confirmation TAT | TAT it takes for LSP to confirm the transaction to the user post signature confirmation | Logs, API monitoring tools, Amplitude events | 5 seconds or lower |

# **How are others solving this problem?**

---

- Leading fintech companies like PayU, Paytm, and PhonePe implement **multi-gateway architectures** with automatic failover mechanisms, routing transactions through backup payment processors when primary gateways experience downtime.
- Enterprise payment platforms use **smart routing algorithms** that dynamically distribute transaction load across multiple payment gateways based on success rates, cost optimisation, and real-time availability.
- Companies like Stripe and Square have built **unified payment orchestration platforms** that aggregate multiple payment processors behind a single API, allowing merchants to access multiple gateways without complex integrations

# **What is the solution?**

## Requirements overview (optional)

- **System Configuration & Communication**
    - Configure payment order expiration timeframes
    - Define transaction completion timeout parameters
    - Implement automated notification systems for payment status updates
- **Core API Development**
    - Develop order creation and payment link generation endpoints
    - Build order status retrieval functionality
    - Implement payment transaction query capabilities
    - Establish web hook handlers for real-time payment notifications
    - Modify existing Finflux repayment payIN API infrastructure to support new gateway
    - Create a createOrderAPI for payTM
- **Reconciliation**
    - Setting up transaction report
    - Setting up settlement recon report

## User stories / User flow

## Requirements

---

- **Configurations**
    
    
    | Parameter  | Value |
    | --- | --- |
    | Order expiry time  | 15 mins |
    | Transaction completion time | 12 mins  |
- **Notifications**
    
    
    | Emails  | Sent to  |
    | --- | --- |
    | Transaction, refund, settlement, emails, | nodalofficer@dspfin.com |
    | Dispute, risk emails | nodalofficer@dspfin.com, gautam.mahesh@dspfin.com |
- **API integrations**
    - create order
        - Request
            
            ```jsx
            {
              "order_currency": "INR",
              "order_amount": 10.34,
              "customer_details": {
                "customer_id": "7112AAA812234",
                "customer_phone": "9898989898"
              }
            }
            ```
            
        - Response
            
            ```jsx
            {
              "cf_order_id": "2149460581",
              "created_at": "2023-08-11T18:02:46+05:30",
              "customer_details": {
                "customer_id": "409128494",
                "customer_name": "Johmn Doe",
                "customer_email": "pmlpayme@ntsas.com",
                "customer_phone": "9876543210",
                "customer_uid": "54deabb4-ba45-4a60-9e6a-9c016fe7ab10"
              },
              "entity": "order",
              "order_amount": 22,
              "payment_session_id": "session_a1VXIPJo8kh7IBigVXX8LgTMupQW_cu25FS8KwLwQLOmiHqbBxq5UhEilrhbDSKKHA6UAuOj9506aaHNlFAHEqYrHSEl9AVtYQN9LIIc4vkH",
              "order_currency": "INR",
              "order_expiry_time": "2023-09-09T18:02:46+05:30",
              "order_id": "order_3242Tq4Edj9CC5RDcMeobmJOWOBJij",
              "order_meta": {
                "return_url": "https://www.cashfree.com/devstudio/thankyou",
                "payment_methods": "cc",
                "notify_url": "https://example.com/cf_notify",
                "payment_methods_filters": {
                  "method": {
                    "action": "ALLOW",
                    "values": [
                      "debit_card",
                      "credit_card",
                      "credit_card_emi",
                      "debit_card_emi"
                    ]
                  },
                  "filters": {
                    "card_bins": {
                      "action": "ALLOW",
                      "values": [
                        441144,
                        554455
                      ]
                    },
                    "card_schemes": {
                      "action": "ALLOW",
                      "values": [
                        "VISA",
                        "MASTERCARD"
                      ]
                    },
                    "card_suffix": {
                      "action": "ALLOW",
                      "values": [
                        4433,
                        8910
                      ]
                    },
                    "card_emi_bins": {
                      "action": "ALLOW",
                      "values": [
                        441144,
                        554455
                      ]
                    },
                    "card_emi_schemes": {
                      "action": "ALLOW",
                      "values": [
                        "VISA",
                        "MASTERCARD"
                      ]
                    },
                    "card_emi_suffix": {
                      "action": "ALLOW",
                      "values": [
                        4433,
                        8910
                      ]
                    }
                  }
                }
              },
              "order_note": "some order note LIST",
              "order_splits": [],
              "order_status": "ACTIVE",
              "order_tags": {
                "name": "John",
                "age": "19"
              },
              "terminal_data": null,
              "cart_details": {
                "cart_id": "1"
              }
            }
            ```
            
    - create payment link
        - Request
            
            ```jsx
            {
              "customer_details": {
                "customer_email": "john@cashfree.com",
                "customer_name": "John Doe",
                "customer_phone": "9999999999"
              },
              "link_amount": 100,
              "link_auto_reminders": true,
              "link_currency": "INR",
              "link_expiry_time": "2021-10-14T15:04:05+05:30",
              "link_id": "my_link_id",
              "link_meta": {
                "notify_url": "https://ee08e626ecd88c61c85f5c69c0418cb5.m.pipedream.net",
                "return_url": "https://www.cashfree.com/devstudio/thankyou",
                "upi_intent": false
              },
              "link_minimum_partial_amount": 20,
              "link_notes": {
                "key_1": "value_1",
                "key_2": "value_2"
              },
              "link_notify": {
                "send_email": true,
                "send_sms": false
              },
              "link_partial_payments": true,
              "link_purpose": "Payment for PlayStation 11",
              "order_splits": [
                {
                  "vendor_id": "Jane",
                  "amount": 1.45,
                  "tags": {
                    "address": "Hyderabad"
                  }
                },
                {
                  "vendor_id": "Barbie",
                  "amount": 3.45,
                  "tags": {
                    "address": "Bengaluru, India"
                  }
                }
              ]
            }
            ```
            
        - Response
            
            ```jsx
            {
              "cf_link_id": "1996567",
              "link_id": "my_link_id",
              "link_status": "ACTIVE",
              "link_currency": "INR",
              "link_amount": 100,
              "link_amount_paid": 0,
              "link_partial_payments": true,
              "link_minimum_partial_amount": 20,
              "link_purpose": "Payment for PlayStation 11",
              "link_created_at": "2021-09-30T17:05:01+05:30",
              "customer_details": {
                "customer_name": "John Doe",
                "customer_phone": "9999999999",
                "customer_email": "john@example.com"
              },
              "link_meta": {
                "notify_url": "https://ee08e626ecd88c61c85f5c69c0418cb5.m.pipedream.net",
                "upi_intent": false,
                "return_url": "https://www.cashfree.com/devstudio/thankyou"
              },
              "link_url": "https://payments-test.cashfree.com/links/o1tf1nvcvjhg",
              "link_expiry_time": "2021-10-14T15:04:05+05:30",
              "link_notes": {
                "key_1": "value_1",
                "key_2": "value_2"
              },
              "link_auto_reminders": true,
              "link_qrcode": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUAAAAFAAQMAAAD3XjfpAAAABlBMVEX///8AAABVwtN+AAAC9ElEQVR4nOyaPY7jMAyFn6HCpY7go/hmkXIzH0VHUOlC8Fvw0c4kM4PFFltJJjDAQPnSEPx5JIPbbrvttv9rC82mPW7gvnDasT5ZkSZyS/ZR6xLMANaJFQLJuj5J5mkHHgaMDpJlNfeROzAZFE4/PgKZOwZfoWTggchsDrvBd7DNZeW/+LEHUDmzY7Wn1aNHORO335JrNPBVcVPYl+2Y6/pssSS9/F6aOwDdLq9smLkBsUCl9aeNB6riymMzNwujI9QlW11hw/Lmx47AJVNBY16Zi71Ydy1JFTXU4UEGlvWYSfsGgbghXOn2HkGdgcCymdJS9GCu66HXmVtqsQwOvoSo/tnswbovLZ6mFpnHBpccTLHaPGMq5QBWKznZOpN9PbUeQcCdUV1mmFfkHmqcI4nBweZt2Ifc031SbEifrbgnMClndg8aWknJ1l5cpLlgHRp0OaZ5xiY4qRQPI5Our3mmO7Cs3L37mhp1SaYBNtRP9wwJnsll84zWYTmwJO5qOCV1CdpoT9pQkkykWWuResdccY22A4NIZIGmF2i4qesRXLBbcpWvNtwTuDCc7SWf0tTay6LVZ3ovpKOClkYHbHrZsU575LOddfiBD2XfFdhMhJozgo31NsXBFem35BoSlPjY9LkJdswkWywJEmmfWdgPeMqt64akQtr0Gj8XgKOCvubxjehmfszXaD992wH0AyL5BGZ9xqIHkU+eihRX9xkX9C2fSzKVFJtXouSITitvS8AhwSzBLm2mM6RmGoDaJfMtHvsC1YavzbD344pXxR0eNG1m8jx5yVHFNT9GBU/uEnSzDMnNSq8KLaATG0L9OiyOCfoFUn5sM7fj2gy/ztLoEtS12f6yqshc8Qj13AKFd202KHheIF2bQWseFkxKrrp8/6VLV+Au8cFNqYJYkrXZZ4s/f98zJEiPFd3gU9PPdij1/rEO6whUzsxnmug24gez6DkzOPiquAg+ztEX57rK1+WX0twBeNttt932d/sTAAD//zUdVfZhwUvzAAAAAElFTkSuQmCC",
              "link_notify": {
                "send_sms": false,
                "send_email": true
              },
              "order_splits": [
                {
                  "vendor_id": "Jane",
                  "percentage": 10,
                  "tags": {
                    "address": "Hyderabad"
                  }
                },
                {
                  "vendor_id": "Barbie",
                  "percentage": 50,
                  "tags": {
                    "address": "Bengaluru, India"
                  }
                }
              ]
            }
            ```
            
    - get order
        - Request
            
            ```jsx
            
            https://sandbox.cashfree.com/pg/orders/{order_id}
            ```
            
        - Response
            
            ```jsx
            {
              "cf_order_id": "2149460581",
              "created_at": "2023-08-11T18:02:46+05:30",
              "customer_details": {
                "customer_id": "409128494",
                "customer_name": "Johmn Doe",
                "customer_email": "pmlpayme@ntsas.com",
                "customer_phone": "9876543210",
                "customer_uid": "54deabb4-ba45-4a60-9e6a-9c016fe7ab10"
              },
              "entity": "order",
              "order_amount": 22,
              "payment_session_id": "session_a1VXIPJo8kh7IBigVXX8LgTMupQW_cu25FS8KwLwQLOmiHqbBxq5UhEilrhbDSKKHA6UAuOj9506aaHNlFAHEqYrHSEl9AVtYQN9LIIc4vkH",
              "order_currency": "INR",
              "order_expiry_time": "2023-09-09T18:02:46+05:30",
              "order_id": "order_3242Tq4Edj9CC5RDcMeobmJOWOBJij",
              "order_meta": {
                "return_url": "https://www.cashfree.com/devstudio/thankyou",
                "payment_methods": "cc",
                "notify_url": "https://example.com/cf_notify",
                "payment_methods_filters": {
                  "method": {
                    "action": "ALLOW",
                    "values": [
                      "debit_card",
                      "credit_card",
                      "credit_card_emi",
                      "debit_card_emi"
                    ]
                  },
                  "filters": {
                    "card_bins": {
                      "action": "ALLOW",
                      "values": [
                        441144,
                        554455
                      ]
                    },
                    "card_schemes": {
                      "action": "ALLOW",
                      "values": [
                        "VISA",
                        "MASTERCARD"
                      ]
                    },
                    "card_suffix": {
                      "action": "ALLOW",
                      "values": [
                        4433,
                        8910
                      ]
                    },
                    "card_emi_bins": {
                      "action": "ALLOW",
                      "values": [
                        441144,
                        554455
                      ]
                    },
                    "card_emi_schemes": {
                      "action": "ALLOW",
                      "values": [
                        "VISA",
                        "MASTERCARD"
                      ]
                    },
                    "card_emi_suffix": {
                      "action": "ALLOW",
                      "values": [
                        4433,
                        8910
                      ]
                    }
                  }
                }
              },
              "order_note": "some order note LIST",
              "order_splits": [],
              "order_status": "ACTIVE",
              "order_tags": {
                "name": "John",
                "age": "19"
              },
              "terminal_data": null,
              "cart_details": {
                "cart_id": "1"
              }
            }
            ```
            
    - get payments
        - Request
            
            ```jsx
            https://sandbox.cashfree.com/pg/orders/{order_id}/payments
            ```
            
        - Response
            
            ```jsx
            [
              {
                "cf_payment_id": "12376123",
                "order_id": "order_8123",
                "entity": "payment",
                "payment_currency": "INR",
                "error_details": null,
                "order_amount": 10.01,
                "order_currency": "INR",
                "is_captured": true,
                "payment_group": "upi",
                "authorization": {
                  "action": "CAPTURE",
                  "status": "PENDING",
                  "captured_amount": 100,
                  "start_time": "2022-02-09T18:04:34+05:30",
                  "end_time": "2022-02-19T18:04:34+05:30",
                  "approve_by": "2022-02-09T18:04:34+05:30",
                  "action_reference": "6595231908096894505959",
                  "action_time": "2022-08-03T16:09:51"
                },
                "payment_method": {
                  "upi": {
                    "channel": "collect",
                    "upi_id": "rohit@xcxcx",
                    "upi_payer_ifsc": "AXL1234",
                    "upi_payer_account_number": "XXXXXXX6024"
                  }
                },
                "payment_amount": 10.01,
                "payment_time": "2021-07-23T12:15:06+05:30",
                "payment_completion_time": "2021-07-23T12:18:59+05:30",
                "payment_status": "SUCCESS",
                "payment_message": "Transaction successful",
                "bank_reference": "P78112898712",
                "auth_id": "A898101",
                "international_payment": {
                  "international": false
                },
                "payment_gateway_details": {
                  "gateway_name": "CASHFREE",
                  "gateway_order_id": "1234421ABD",
                  "gateway_payment_id": "XABDJ2213",
                  "gateway_order_reference_id": "BDIWO233",
                  "gateway_settlement": "cashfree",
                  "gateway_reference_name": ""
                }
              },
              {
                "cf_payment_id": "12376124",
                "order_id": "order_8123",
                "entity": "payment",
                "payment_currency": "INR",
                "error_details": {
                  "error_code": "TRANSACTION_DECLINED",
                  "error_description": "issuer bank or payment service provider declined the transaction",
                  "error_reason": "auth_declined",
                  "error_source": "customer"
                },
                "order_amount": 10.01,
                "order_currency": "INR",
                "is_captured": true,
                "payment_group": "credit_card",
                "authorization": null,
                "payment_method": {
                  "card": {
                    "channel": "link",
                    "card_number": "xxxxxx1111"
                  }
                },
                "payment_amount": 10.01,
                "payment_time": "2021-07-23T12:15:06+05:30",
                "payment_completion_time": "2021-07-23T12:18:59+05:30",
                "payment_status": "FAILED",
                "payment_message": "Transaction failed",
                "bank_reference": "P78112898712",
                "auth_id": "A898101",
                "international_payment": {
                  "international": false
                },
                "payment_gateway_details": {
                  "gateway_name": "CASHFREE",
                  "gateway_order_id": "1234421ABD",
                  "gateway_payment_id": "XABDJ2213",
                  "gateway_order_reference_id": "BDIWO233",
                  "gateway_settlement": "cashfree",
                  "gateway_reference_name": ""
                }
              },
              {
                "cf_payment_id": "12376152",
                "order_id": "order_8125",
                "entity": "payment",
                "payment_currency": "USD",
                "error_details": {
                  "error_code": "TRANSACTION_DECLINED",
                  "error_description": "issuer bank or payment service provider declined the transaction",
                  "error_reason": "auth_declined",
                  "error_source": "customer"
                },
                "order_amount": 100,
                "order_currency": "INR",
                "is_captured": true,
                "payment_group": "credit_card",
                "authorization": null,
                "payment_method": {
                  "card": {
                    "channel": "link",
                    "card_number": "xxxxxx1111"
                  }
                },
                "payment_amount": 1.25,
                "payment_time": "2021-07-23T12:15:06+05:30",
                "payment_completion_time": "2021-07-23T12:18:59+05:30",
                "payment_status": "FAILED",
                "payment_message": "Transaction failed",
                "bank_reference": "P78112812312",
                "auth_id": "A851201",
                "international_payment": {
                  "international": true
                },
                "payment_gateway_details": {
                  "gateway_name": "CASHFREE",
                  "gateway_order_id": "3462421ABD",
                  "gateway_payment_id": "XAUIH2213",
                  "gateway_order_reference_id": "ZD5WO253",
                  "gateway_settlement": "cashfree",
                  "gateway_reference_name": ""
                }
              }
            ]
            ```
            
    - Web hooks
        - Web hooks will be handled for -
            - Successful transaction
            - Failure transaction
            - Refunded transaction
    - Finflux repayment payIN API
        - Note
            - Our existing architecture uses a generic "Payment_Gateway" identifier for paymentType since we currently operate with a single payment processor. However, as we expand our payment ecosystem to include multiple gateways such as Cashfree and incorporate repayments from PhonePe_PG, we need to implement more granular payment source identification.
            - The updated paymentType parameter will now accept specific gateway identifiers: "RAZORPAY", "CASHFREE", and "PHONEPE_PG" to accurately track and categorize repayments based on their originating payment platform.
        - Request
            
            ```jsx
            {
                "amount": 10,
                "transactionTime": 1721820134000,
                "paymentDetails": {
                    **"paymentType": ""**
                },
                "transactionProcessingStrategy" : "default_T"
            }
            ```
            
        - Response
            
            ```jsx
            {
                "transactionId": "6458a88b-c817-46e4-8fac-57a6b2ef0404",
                "accountNumber": "000000049",
                "amount": 10,
                "tags": [],
                "transactionTime": 1721820134000,
                "transactionAdditionalDetails": {},
                "paymentDetails": {
                    "paymentType": ""
                },
                "subLimitDetails": [],
                "isOriginalTransactionConvertedToEmi": false,
                "isCreditLineTransaction": true
            }
            ```
            
    - createOrder for LSPs (payTM specific)
        - Note
            - As per alignment with PayTM team, PayTM will create order/payment link at their end using DSPs credentials, and through an API (provided by DSP to PayTM), payTM will share the order_id of transaction. DSP will then poll the status of the API and if the status is successful DSP itself will post the repayment.
        - Request
            
            ```jsx
            {
                loanAccountId : "FXLAN345678"
                repayment_type : ""
                orderId : "wvhowiehgowihfgefion_2312490hgw"
                
            } 
            ```
            
        - Response
            - Same as the current response object of createOrder API

- **Reconciliation**
    - Daily at 6 AM we will receive reconciliation reports from Cashfree through SFTP
    - There will be 2 reports which will be used in daily reconciliation
        - Transaction report - This contains transaction level details like Transaction ID, order ID, transaction UTR number, timestamp of transaction
        - Settlement report - This contains all the payments, refunds, disputes, adjustments and settlement details of each transaction with transaction UTR number and settlement UTR number
        - Note - transaction UTR number field will be primarily used to create mapping between the Transaction report and the Settlement report for reconciliation. Additionally fields like Order ID/Merchant Reference ID and Reference ID/CashFree Reference ID can also be used to create mapping.
    - Transaction report -
    
    [Transaction Report Aug 5 2025.csv](Cashfree%20PG%20integration/Transaction_Report_Aug_5_2025.csv)
    
    - Settlement recon report -
    
    [Settlement Recon Report Aug 5 2025.csv](Cashfree%20PG%20integration/Settlement_Recon_Report_Aug_5_2025.csv)
    

# **Design**

---

# **Analytics**

---

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