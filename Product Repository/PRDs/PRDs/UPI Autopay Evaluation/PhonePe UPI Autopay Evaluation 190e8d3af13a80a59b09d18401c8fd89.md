# PhonePe UPI Autopay Evaluation

API Documentation & Integration - [Link](https://developer.phonepe.com/v1/reference/subscription-v2-authorization)

**List of APIs**

1. Authorization API
    1. This API is used to generate the auth token to access the rest of the APIs.
    2. The auth token is valid for 1 hour.
    3. If the auth token is re-generated within 1 hour, the old token will not expire.
- Request
    
    ```json
    curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=' \
    --data-urlencode 'client_version=1' \
    --data-urlencode 'client_secret=' \
    --data-urlencode 'grant_type='
    ```
    
- Response
    
    ```json
    {
        "access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q",
        "encrypted_access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q",
        "expires_in": 3600,
        "issued_at": 1738669002,
        "expires_at": 1738672602,
        "session_expires_at": 1738672602,
        "token_type": "O-Bearer"
    }
    ```
    

1. Validate VPA API
    1. This API is used to validate the user's VPA.
    2. Returns, valid & name of the user.
    3. We should ask PhonePe team to share the bank account number & IFSC associated with this VPA. This will help us to limit mandate registration only on verified bank accounts.
- Request
    
    ```json
    {
        "type": "VPA",
        "vpa": "nihaltest1@ybl"
    }
    ```
    
- Response
    
    ```json
    {
        "valid": true,
        "name": "<Name of User>"
    }
    ```
    

1. Intent
    1. This API is used to create the intent link for autopay.
    2. amount - this parameter defines the amount to be deducted at the time of registration.
    3. maxAmount - this amount defines the maximum amount the mandate is registering for.
    4. Android - Generic intent URI will be provided.
    5. iOS - Tpap specfic URI will be generated. Only Gpay, PhonePe & Paytm is supported. This will be a drawback as we can’t give users the power to choose the app.
- Request
    
    ```json
    {
       "merchantOrderId": "MOTEST5",
       "amount": 300,
       "expireAt": 1709058548000,
       "paymentFlow": {
           "type": "SUBSCRIPTION_SETUP",
           "merchantSubscriptionId": "MSTEST5",
           "authWorkflowType": "TRANSACTION",
           "amountType": "FIXED",
           "maxAmount": 2000,
           "frequency": "ON_DEMAND",
           "expireAt": 1737278524000,
           "paymentMode": {
               "type": "UPI_INTENT",
               "targetApp": "com.phonepe.app"
           }
       },
        "deviceContext" : {
            "deviceOS" : "ANDROID"
        }
    }
    ```
    
- Response
    
    ```json
    {
        "orderId": "OMO2502041725138147510236",
        "state": "PENDING",
        "intentUrl": "ppesim://mandate?pa=VOLTMONEYUAT@ybl&pn=SUBSCRIBEMID&am=300&mam=&tr=OM2502041725138157510738&utm_campaign=SUBSCRIBE_AUTH&utm_medium=VOLTMONEYUAT&utm_source=OM2502041725138157510738"
    }
    ```
    

1. Collect
    1. This API is used to send the collect request for mandate setup.
    2. In collect request, all the VPAs are supported. Even Gpay, SuperMoney VPAs are supported.
- Request Body
    
    ```json
    {
       "merchantOrderId": "MOTEST6",
       "amount": 200,
       "expireAt": 1709058548000,
       "paymentFlow": {
           "type": "SUBSCRIPTION_SETUP",
           "merchantSubscriptionId": "MSTEST6",
           "authWorkflowType": "TRANSACTION",
           "amountType": "VARIABLE",
           "maxAmount": 2000,
           "frequency": "ON_DEMAND",
           "expireAt": 1737278524000,
           "paymentMode": {
               "type": "UPI_COLLECT",
               "details": {
                   "type": "VPA",
                   "vpa": "nihaltest1@ybl"
               }
           }
       }
    }
    ```
    
- Response
    
    ```json
    {
        "orderId": "OMO2502041727154877510267",
        "state": "PENDING"
    }
    ```
    

1. Subscription Order Status
    1. This API is used check the status of the mandate transaction.
- Response
    
    ```json
    {
        "merchantId": "VOLTMONEYUAT",
        "merchantOrderId": "MOTEST5",
        "orderId": "OMO2502041725138147510236",
        "state": "COMPLETED",
        "amount": 300,
        "expireAt": 1709058548000,
        "paymentFlow": {
            "type": "SUBSCRIPTION_SETUP",
            "merchantSubscriptionId": "MSTEST5",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 2000,
            "frequency": "ON_DEMAND",
            "expireAt": 1709058548000,
            "subscriptionId": "OMS2502041725138157510035"
        },
        "paymentDetails": [
            {
                "transactionId": "OM2502041725138157510738",
                "paymentMode": "UPI_INTENT",
                "timestamp": 1738671606532,
                "amount": 300,
                "state": "COMPLETED",
                "instrument": {
                    "type": "ACCOUNT",
                    "maskedAccountNumber": "XXXXXXX20000",
                    "ifsc": "PPTA0000000",
                    "accountHolderName": "PPTA0000000",
                    "accountType": "SAVINGS"
                },
                "rail": {
                    "type": "UPI",
                    "utr": "402920414278",
                    "vpa": "8668594479@ybl",
                    "umn": "5e0bb6dfccf14cc1bbaf87fae06c3bbf@ybl"
                }
            }
        ]
    }
    ```
    

1. Subscription Status
    1. This API is used to get the latest status of the mandate.
- Response
    
    ```json
    {
        "merchantSubscriptionId": "MOTEST6",
        "subscriptionId": "OMS2502041727154887510928",
        "state": "CANCELLED",
        "authWorkflowType": "TRANSACTION",
        "amountType": "VARIABLE",
        "maxAmount": 2000,
        "frequency": "ON_DEMAND",
        "expireAt": 1709058548000,
        "pauseStartDate": null,
        "pauseEndDate": null
    }
    ```
    

1. PDN
    1. This API is used to trigger the PDN for registered VPA.
    2. There is no API which says, whether the PDN is success/ not.
- Request
    
    ```json
    {
     "merchantOrderId": "MOPDN-2",
     "amount": 300,
     "expireAt": 1738576000,
     "paymentFlow": {
       "type": "SUBSCRIPTION_REDEMPTION",
       "merchantSubscriptionId": "OMO2502041725138147510236",
       "redemptionRetryStrategy": "STANDARD",
       "autoDebit": true
     }
    }
    ```
    
- Response
    
    ```json
    {
        "orderId": "OMO2502041740029327510770",
        "state": "NOTIFICATION_IN_PROGRESS",
        "expireAt": 1738576000
    }
    ```
    

1. Redemption - Execute
    1. This API is used to execute the mandate.
    2. This needs to be called post PDN is called & 24hrs passed.
    3. Amount will be debited instantaneously.
    - Request
        
        ```json
        {
            "merchantOrderId": "OMO2502041801304337510249"
        }
        ```
        
    - Response
        
        ```json
        {
            "state" : "PENDING",
            "transactionId": "OM1234"
        }
        ```
        
    
2. Redemption Order - Status
    1. This API is used to check the status of the redemption.
- Response
    
    ```json
    {
        "merchantId": "VOLTMONEYUAT",
        "merchantOrderId": "MOPDN-4",
        "orderId": "OMO2502041802526797510282",
        "state": "COMPLETED",
        "amount": 300,
        "expireAt": 1738576000,
        "paymentFlow": {
            "type": "SUBSCRIPTION_REDEMPTION",
            "merchantSubscriptionId": "OMO2502041725138147510236",
            "redemptionRetryStrategy": "STANDARD",
            "autoDebit": true,
            "notifiedAt": 1738672377897,
            "validAfter": 1738845177897,
            "validUpto": 1738576000
        },
        "paymentDetails": [
            {
                "transactionId": "OM2502041802526807510746",
                "paymentMode": "UPI_AUTO_PAY",
                "timestamp": 1738672377897,
                "amount": 300,
                "state": "COMPLETED",
                "instrument": {
                    "type": "ACCOUNT",
                    "accountType": "SOD"
                },
                "rail": {
                    "type": "UPI",
                    "utr": "402920414278",
                    "umn": "5e0bb6dfccf14cc1bbaf87fae06c3bbf@ybl"
                },
                "responseCode": "COMPLETED"
            }
        ]
    }
    ```
    

1. Subscription Cancel
    1. This API is used to cancel the mandate from lender side.
    2. Active mandates & pending mandates can be cancelled via this API.
    3. Empty response body.
- Request
    
    ```json
    No response body. Only status code 204 will be sent.
    ```
    

1. Merchant Callbacks
- Redemption Status
    
    ```json
    {
      "type": "SUBSCRIPTION_NOTIFICATION_COMPLETED/SUBSCRIPTION_NOTIFICATION_FAILED",
      "payload": {
        "merchantId": "SWIGGY8",
        "merchantOrderId": "MO1708797962855",
        "orderId": "OMO12344",
        "amount": 100,
        "state": "NOTIFIED",
        "expireAt": 1620891733101,
        "paymentFlow": {
          "type": "SUBSCRIPTION_REDEMPTION",
          "merchantSubscriptionId": "MS121312",
          "redemptionRetryStrategy": "CUSTOM",
          "autoDebit": true,
          "validAfter": "1628229131000",
          "validUpto": "1628574731000",
          "notifiedAt": "1622539751586"
        }
      }
    }
    ```
    
- Redemption State
    
    ```json
    {
      "type": "SUBSCRIPTION_REDEMPTION_ORDER_COMPLETED/SUBSCRIPTION_REDEMPTION_ORDER_FAILED",
      "payload": {
       "merchantId": "SWIGGY8",
        "merchantOrderId": "MO1708797962855"
        "orderId": "OMO12344",
        "state": "COMPLETED",
        "amount": 100,
       "expireAt": 1620891733101,
        "paymentFlow": {
          "type": "SUBSCRIPTION_REDEMPTION",
          "merchantSubscriptionId": "MS121312",
          "redemptionRetryStrategy": "CUSTOM",
          "autoDebit": true,
          "validAfter": "1628229131000",
          "validUpto": "1628574731000",
          "notifiedAt": "1622539751586"
        },
        "errorCode": <PRESENT ONLY IF STATE IS FAILED>
        "detailedErrorCode": <PRESENT ONLY IF STATE IS FAILED>  
        "paymentDetails": [
            {
                "amount": 100
                "paymentMode": "UPI_AUTO_PAY",
                "timestamp": 1620891733101      
                "transactionId": "OM124",
                "state": "COMPLETED", // FAILED, PENDING
                "rail": {
                    "type": "UPI",
                    "utr": "2",
                    "vpa": "abcd@ybl",
                    "umn": "544fcc8819d04cb08e26faa1fb07eee7@ybl"
                },
                "instrument": {
                    "type": "ACCOUNT",
                    "maskedAccountNumber": "XXX2312",
                    "ifsc": "VISA",
                    "accountHolderName": "Venkat",
                    "accountType": "SAVINGS"
                },
                "errorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
               "detailedErrorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
            }
        ]
      }
    }
    ```
    
- Redemption - Attempt
    
    ```json
    {
      "type": "SUBSCRIPTION_REDEMPTION_TRANSACTION_COMPLETED/SUBSCRIPTION_REDEMPTION_TRANSACTION_FAILED",
      "payload": {
       "merchantId": "SWIGGY8",
        "merchantOrderId": "MO1708797962855"
        "orderId": "OMO12344",
        "state": "PENDING",
        "amount": 100,
       "expireAt": 1620891733101,
        "paymentFlow": {
          "type": "SUBSCRIPTION_REDEMPTION",
          "merchantSubscriptionId": "MS121312",
          "redemptionRetryStrategy": "CUSTOM",
          "autoDebit": true,
          "validAfter": "1628229131000",
          "validUpto": "1628574731000",
          "notifiedAt": "1622539751586"
        },
        "errorCode": <PRESENT ONLY IF STATE IS FAILED>
        "detailedErrorCode": <PRESENT ONLY IF STATE IS FAILED>  
        "paymentDetails": [
            {
                "amount": 100
                "paymentMode": "UPI_AUTO_PAY",
                "timestamp": 1620891733101      
                "transactionId": "OM124",
                "state": "COMPLETED", // FAILED, PENDING
                "rail": {
                    "type": "UPI",
                    "utr": "2",
                    "vpa": "abcd@ybl",
                    "umn": "544fcc8819d04cb08e26faa1fb07eee7@ybl"
                },
                "instrument": {
                    "type": "ACCOUNT",
                    "maskedAccountNumber": "XXX2312",
                    "ifsc": "VISA",
                    "accountHolderName": "Venkat",
                    "accountType": "SAVINGS"
                },
                "errorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
               "detailedErrorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
            }
        ]
      }
    }
    ```
    

1. Subscription Callbacks

There is no callback for “Expired” mandates.

- Unpaused
    
    ```json
    {
        "type": "SUBSCRIPTION_UNPAUSED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "ACTIVE",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": null,
            "pauseEndDate": null
        }
    }
    ```
    
- Paused
    
    ```json
    {
        "type": "SUBSCRIPTION_PAUSED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "PAUSED",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": 1708798426196,
            "pauseEndDate": 1708885799000
        }
    }
    ```
    
- Revoked
    
    ```json
    {
        "type": "SUBSCRIPTION_REVOKED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "REVOKED",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": 1708798426196,
            "pauseEndDate": 1708885799000
        }
    }
    ```
    
- Cancelled
    
    ```json
    {
        "type": "SUBSCRIPTION_CANCELLED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "CANCELLED",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": 1708798426196,
            "pauseEndDate": 1708885799000
        }
    }
    ```
    

## Available SDKs for Autopay

SDKs are not benchmarked

1. Java SDK
2. Python SDK

## Functionality & Features

- Authentication & Authorization
    - Secure auth token generation with a 1-hour validity.
    - Regenerating a token invalidates the previous one.
- User Verification & Validation
    - Validate VPA to check if it exists and retrieve the associated name.
    - Need to request bank details (account number & IFSC) for stronger validation.
- Subscription Setup & Payment Initiation
    - Intent-Based Setup:
        - Generates an intent URI for UPI-based mandate registration.
        - Limited app support for iOS (only GPay, PhonePe & Paytm).
    - Collect Request Setup:
        - Allows mandate registration via a collect request.
        - Supports all VPAs, including third-party apps.
    - QR Code Setup:
        - Allows mandate registration by scanning the QR code.
        - There is no API directly exposed, however we need to convert the intent URL.
- Subscription Status & Order Management
    - Retrieve mandate status (active, pending, canceled, revoked).
    - Check transaction status in real-time.
- Payment Execution & Recurring Payments
    - PDN (Pre-Debit Notification):
        - Notifies about an upcoming debit but lacks a success confirmation API.
    - Redemption Execution:
        - Mandate execution post PDN notification (requires a 24-hour wait).
        - Supports auto-debit.
- Merchant Callbacks & Notifications
    - Real-time webhook notifications for:
        - Subscription setup completion.
        - Payment status updates.
        - Subscription state changes (paused, resumed, revoked, canceled).
- Subscription Lifecycle Management
    - Pause & Resume: Allows temporary suspension of mandates.
    - Cancellation & Revocation: Merchants can cancel active & pending mandates.
- API Response Time
    - All the APIs have less than 50 - 100ms in TAT. Tested only on UAT.
    - However, we can expect 100- 150ms in TAT on production.