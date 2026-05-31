# PhonePe PG Implementation

: Surya Ganesh
Created time: February 26, 2025 5:59 PM
Status: Not started
Last edited: February 28, 2025 3:28 PM

# **What problem are we solving?**

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

Authorisation:

This is used to authorise the subsequent API calls between the Merchant & PhonePe backend.

- **Request Headers**
    
    
    | **Header Name** | **Header Value** |
    | --- | --- |
    | `*Content-Type*` | application/x-www-form-urlencoded |
- Request Parameters
    
    
    | **Parameter Name** | **Description** |
    | --- | --- |
    | `*client_id*` | Client ID shared by PhonePe |
    | `*client_version*` | In case of **UAT**, client_version value should be 1.In case of **PROD**, use the value as received in credentials email. |
    | `*client_secret*` | Client secret shared by PhonePe |
    | `*grant_type*` | Value will be “client_credentials” |
- Request Body
    
    ```json
    {
    "client_id": "<your_client_id>",
    "client_version": 1,
    "client_secret": "<your_client_secret>",
    "grant_type": "client_credentials"
    }
    ```
    
- Documentation
    
    [https://developer.phonepe.com/v1/reference/authorization-standard-checkout/#Request-Details](https://developer.phonepe.com/v1/reference/authorization-standard-checkout/#Request-Details)
    
- End-point
    
    POST – [https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token](https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token)
    
- Response
    
    ```json
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzT24iOjE3MjA2MzUzMjE5OTYsIm1lcmNoYW50SWQiOiJWUlVBVCJ9.4YjYHI6Gy6gzOisD_628wfbaI46dMSc5T_0gZ2-SAJo",
        "encrypted_access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzT24iOjE3MjA2MzUzMjE5OTYsIm1lcmNoYW50SWQiOiJWUlVBVCJ9.4YjYHI6Gy6gzOisD_628wfbaI46dMSc5T_0gZ2-SAJo",
        "expires_in": null,
        "issued_at": 1706073005,
        "expires_at": 1706697605,
        "session_expires_at": 1706697605,
        "token_type": "O-Bearer"
    }
    ```
    

Initiate Payment:
This API is used to initiate the payment.

- Complete Host Details
    
    
    | **Environment** | **Http Method** | **Value** |
    | --- | --- | --- |
    | `UAT` | POST | **https://api-preprod.phonepe.com/apis/pg-sandbox/checkout/v2/pay** |
    | `PROD` | POST | **https://api.phonepe.com/apis/pg/checkout/v2/pay** |
- Request Headers
    
    ### Request Headers
    
    | **Header Name** | **Header Value** | **Description** |
    | --- | --- | --- |
    | `*Content-Type*` | **application/json** |  |
    | `*Authorization*` | **O-Bearer <access_token>** | Pass **`*access_token*`** received in [Authorization](https://developer.phonepe.com/v1/reference/authorization-standard-checkout/) call |
- Sample Request with Selected Instrument
    
    ```json
    {
        "merchantOrderId": "TX123456",
        "amount": 1000,
        "expireAfter": 1200,
        "metaInfo": {
            "udf1": "<additional-information-1>",
            "udf2": "<additional-information-2>",
            "udf3": "<additional-information-3>",
            "udf4": "<additional-information-4>",
            "udf5": "<additional-information-5>"
        },
        "paymentFlow": {
            "type": "PG_CHECKOUT",
            "message": "Payment message used for collect requests",
            "merchantUrls": {
                "redirectUrl": ""
            },
            "paymentModeConfig": {
                "enabledPaymentModes": [
                    {
                        "type": "UPI_INTENT"
                    },
                    {
                        "type": "UPI_COLLECT"
                    },
                    {
                        "type": "UPI_QR"
                    },
                    {
                        "type": "NET_BANKING"
                    },
                    {
                        "type": "CARD",
                        "cardTypes": [
                            "DEBIT_CARD",
                            "CREDIT_CARD"
                        ]
                    }
                ],
                "disabledPaymentModes": [
                    {
                        "type": "UPI_INTENT"
                    },
                    {
                        "type": "UPI_COLLECT"
                    },
                    {
                        "type": "UPI_QR"
                    },
                    {
                        "type": "NET_BANKING"
                    },
                    {
                        "type": "CARD",
                        "cardTypes": [
                            "DEBIT_CARD",
                            "CREDIT_CARD"
                        ]
                    }
                ]
            }
        }
    }
    ```
    

Important Notes

Either **enabledPaymentModes** or **disabledPaymentModes** is required, if both are present API will throw error.

- **paymentModeConfig**.**enabledPaymentModes**:This will ensure the list of Instruments passed within the “**enabledPaymentModes**” block will only be shown on the Checkout Page while all other enabled instruments at PhonePe end won’t be displayed.
- **paymentModeConfig**.**disabledPaymentModes**:This will ensure the list of Instruments passed within the “**disabledPaymentModes**” block will not be shown on the Checkout Page while all other enabled instruments at PhonePe end will be displayed.
- Special Case for the **CARD** instrument: Ensure to pass the **cardTypes** as well along with **type**.
    - If “**enabledPaymentModes.type**” = “CARD” but“**enabledPaymentModes.cardTypes**” is not passed, then the Card option will be displayed based on the instrument enabled at PhonePe’s end [CreditCard (and/or) Debit Card].
    - If “**enabledPaymentModes.type**” = “CARD” and“**enabledPaymentModes.cardTypes**” = [“DEBIT_CARD”] is passed, then the Debit Card option only will be allowed on the PhonePe checkout.
    - If “**disabledPaymentModes.type**” = “CARD” but“**disabledPaymentModes.cardTypes**” is not passed, then the Card option won’t be disabled and user will be displayed based on the instrument enabled at PhonePe’s end [CreditCard (and/or) Debit Card].
    - If “**disabledPaymentModes.type**” = “CARD” and“**disabledPaymentModes.cardTypes**” = [“DEBIT_CARD”] is passed, then the Debit Card option alone will be disabled on the PhonePe checkout.
    - If “**disabledPaymentModes.type**” = “CARD” and“**disabledPaymentModes.cardTypes**” = [“DEBIT_CARD”, “CREDIT_CARD”] is passed, only then both Debit Card and Credit Card will be disabled on the PhonePe checkout.
- Request Parameters
    
    
    | **Parameter Name** | **Data Type** | **Description** | **Mandatory (Yes/No)** | **Constraints** |
    | --- | --- | --- | --- | --- |
    | `*merchantOrderId*` | **STRING** | **Unique merchant order id generated by merchant** | **Yes** | **Max Length = 63 charactersNo Special characters allowed except underscore “_” and hyphen “-“** |
    | `*expireAfter*` | **LONG** | **Order expiry in seconds. If not passed, default value will be used.** | **No** | **Min Value = 300, Max Value = 3600** (in Seconds)**Default Value = 1200 Secs** (20 Mins) |
    | `*amount*` | **LONG** | **Order amount in paisa** | **Yes** | **Min Value = 100 (In paise)** |
    | `*metaInfo*` | **OBJECT** | **Merchant defined meta info to store additional information.same data will be returned in status and callback response** | **No** |  |
    | `*metaInfo.udf1-4*` | **STRING** | **Merchant defined additional information** | **No** | **Max length = 256 characters** |
    | `*paymentFlow*` | **OBJECT** | **Additional details required by this flow** | **Yes** |  |
    | `*paymentFlow.type*` | **STRING** | **Type of payment flow** | **Yes** | **Valued Allowed = [PG_CHECKOUT]** |
    | `*paymentFlow.message*` | **STRING** | **Payment message used for collect requests** | **No** |  |
    | `*paymentFlow.merchantUrls*` | **OBJECT** | **Object to store different merchant Urls** | **Yes** |  |
    | `*paymentFlow.merchantUrls.redirectUrl*` | **STRING** | **Url where user will be redirected after success/failed payment.** | **Yes** |  |
    | `*paymentModeConfig*` | **OBJECT** | **Additional details to display only the selected instruments** | **Optional** | Either **enabledPaymentModes** or **disabledPaymentModes** is required, if both are present API will throw error. |
- Sample CURL
    
    ```json
    curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/checkout/v2/pay' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: O-Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzT24iOjE3MTIyNTM2MjU2NDQsIm1lcmNoYW50SWQiOiJWMlNVQlVBVCJ9.7aVzYI_f_77-bBicEcRNuYx093b2wCsgl_WFNkKqAPY' \
    --data '{
      "merchantOrderId": "TX123rrty34432456",
      "amount": 1000,
      "paymentFlow": {
        "type": "PG_CHECKOUT",
        "message": "Payment message used for collect requests",
        "merchantUrls": {
          "redirectUrl": "https://www.xyz.com/PGIntegration/"
        }
      }
    }'
    ```
    
- Response Headers
    
    
    | **Header Name** | **Header Value** |
    | --- | --- |
    | `*Content-Type*` | application/json |
- Response Payload
    - Order created successfully (200)
        
        Http Response Code: 200
        
        ```json
        {
            "orderId": "OMO123456789",
            "state": "PENDING",
            "expireAt": 1703756259307,    
            "redirectUrl": "https://mercury-uat.phonepe.com/transact/uat_v2?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzT24iOjE3MjgyNTk1MzE0NzgsIm1lcmNoYW50SWQiOiJWUlVBVCIsIm1lcmNoYW50T3JkZXJJZCI6Ik1PLTlkMC1hNmMyYmY1ZWM4MmUifQ.Trj5fub__kJpQhzOlJttXl2UPruHE7fsbH5QWj-iy6E"
        }
        ```
        
    - Order with same merchant order id is already present and not in CREATED state (400)
        
        Http Response Code: 400
        
        ```json
        {
            "code": "BAD_REQUEST",
            "message": "Please check the inputs you have provided."
        }
        ```
        
    - Internal Server Error (500)
        
        Http Response code: 500
        
        ```json
        {
            "code": "INTERNAL_SERVER_ERROR",
            "message": "There is an error trying to process your transaction at the moment. Please try again in a while."
        }
        ```
        
    

[](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MjUgNDI1IiB4bWw6c3BhY2U9InByZXNlcnZlIj48cGF0aCBmaWxsPSIjMzIzMTM1IiBkPSJNMjEyLjUwMiA4NS4yMDhjNi44MzEgMCAxMi4zODkgNS41NTggMTIuMzg5IDEyLjM5MSAwIDYuODMxLTUuNTU4IDEyLjM4OS0xMi4zODkgMTIuMzg5LTYuODMxIDAtMTIuMzktNS41NTgtMTIuMzktMTIuMzg5IDAtNi44MzMgNS41NTktMTIuMzkxIDEyLjM5LTEyLjM5MXptLTQ2LjgxMyAyMzIuNzAzYzEuNzM2LjkxOCAzLjc3NCAxLjkyNiA2LjAxNSAzLjAzIDExLjk3NCA1LjkwOCAzMi4wMTQgMTUuNzk2IDMyLjAxNCAyNy42MzRhOC43ODMgOC43ODMgMCAwIDAgOC43ODQgOC43ODQgOC43ODMgOC43ODMgMCAwIDAgOC43ODMtOC43ODRjMC0xMS44NCAyMC4wNDQtMjEuNzI4IDMyLjAyMS0yNy42MzYgMi4yMzQtMS4xMDMgNC4yNzUtMi4xMTIgNi4wMDgtMy4wMjggMjcuMTYtMTQuMzY0IDQ1LjgxMy0zOS45NjggNTEuNTU0LTY5LjM3NmwxMy4yNTcgMTMuMjU3YTguNzU0IDguNzU0IDAgMCAwIDYuMjEgMi41NzMgOC43NSA4Ljc1IDAgMCAwIDYuMjEtMi41NzMgOC43OCA4Ljc4IDAgMCAwIDAtMTIuNDJsLTI2LjM0NC0yNi4zNDZhOC44NTkgOC44NTkgMCAwIDAtMS4zMzYtMS4wOThjLS4xMDMtLjA2OC0uMjE4LS4xMTEtLjMyMy0uMTc1YTguNjkyIDguNjkyIDAgMCAwLTEuMTg2LS42MzNjLS4xNTgtLjA2Ni0uMzI5LS4wOTYtLjQ5MS0uMTUzLS4zNzYtLjEzMS0uNzUtLjI2OS0xLjE0Ny0uMzQ4YTguNzMgOC43MyAwIDAgMC0zLjQ3MyAwYy0uMzYuMDcyLS42OTYuMi0xLjAzOC4zMTUtLjIuMDY3LS40MDkuMTA2LS42MDQuMTg3LS4zNjEuMTUxLS42OTMuMzUzLTEuMDI4LjU0OS0uMTU4LjA5Mi0uMzI5LjE1OS0uNDgxLjI2MWE4Ljc3IDguNzcgMCAwIDAtMS4yOTIgMS4wNmMtLjAxLjAwOS0uMDIxLjAxNS0uMDMuMDI0bC0yNi4zNTcgMjYuMzU1YTguNzgyIDguNzgyIDAgMCAwIDAgMTIuNDIyIDguNzggOC43OCAwIDAgMCAxMi40MiAwbDcuNDIxLTcuNDE5YTgyLjU3OSA4Mi41NzkgMCAwIDEtNDAuMTU2IDQ4LjAwOWMtMS42MDUuODQ5LTMuNDk2IDEuNzgxLTUuNTY4IDIuODAyLTcuMDY1IDMuNDg2LTE2LjI2NiA4LjA0Ny0yNC4yNDcgMTQuMDgzVjE1Ni41MTRoMjkuMTI2YTguNzgzIDguNzgzIDAgMCAwIDguNzgzLTguNzgzIDguNzgyIDguNzgyIDAgMCAwLTguNzgzLTguNzgzaC0yOS4xMjZ2LTEyLjcxM2MxMi4yNDQtMy43NjMgMjEuMTczLTE1LjE3MyAyMS4xNzMtMjguNjM2IDAtMTYuNTE4LTEzLjQ0LTI5Ljk1OC0yOS45NTYtMjkuOTU4LTE2LjUxNyAwLTI5Ljk1NiAxMy40NC0yOS45NTYgMjkuOTU4IDAgMTMuNDYzIDguOTI4IDI0Ljg3MyAyMS4xNzIgMjguNjM2djEyLjcxM2gtMjkuMTI1YTguNzgyIDguNzgyIDAgMCAwLTguNzg0IDguNzgzIDguNzgzIDguNzgzIDAgMCAwIDguNzg0IDguNzgzaDI5LjEyNXYxNjIuNzU0Yy03Ljk3OS02LjAzNC0xNy4xNzktMTAuNTk1LTI0LjI0My0xNC4wODEtMi4wNzItMS4wMjItMy45NjYtMS45NTQtNS41NzItMi44MDVhODIuNTcyIDgyLjU3MiAwIDAgMS00MC4xNTUtNDguMDA2bDcuNDE3IDcuNDE2YTguNzUgOC43NSAwIDAgMCA2LjIxIDIuNTczIDguNzU0IDguNzU0IDAgMCAwIDYuMjEtMi41NzMgOC43OCA4Ljc4IDAgMCAwIDAtMTIuNDJsLTI2LjM0NS0yNi4zNDZhOC44MSA4LjgxIDAgMCAwLTEuMzM2LTEuMDk4Yy0uMTAyLS4wNjgtLjIxOC0uMTExLS4zMjMtLjE3NWE4LjYyMiA4LjYyMiAwIDAgMC0xLjE4NS0uNjMzYy0uMTU5LS4wNjYtLjMzLS4wOTYtLjQ5Mi0uMTUzLS4zNzYtLjEzMS0uNzQ5LS4yNjktMS4xNDYtLjM0OGE4Ljc0OCA4Ljc0OCAwIDAgMC0zLjQ3NCAwYy0uMzYuMDcyLS42OTYuMi0xLjAzOC4zMTUtLjIuMDY3LS40MDkuMTA2LS42MDMuMTg3LS4zNjIuMTUxLS42OTQuMzUzLTEuMDI5LjU0OS0uMTU4LjA5Mi0uMzI4LjE1OS0uNDgxLjI2MWE4LjgyMyA4LjgyMyAwIDAgMC0xLjI5MiAxLjA2Yy0uMDA5LjAwOS0uMDIuMDE1LS4wMy4wMjRMODguNDU0IDI0OS4zN2MtMy40MyAzLjQzMS0zLjQzIDguOTkzIDAgMTIuNDIyYTguNzgxIDguNzgxIDAgMCAwIDEyLjQyMSAwbDEzLjI2LTEzLjI1OGM1Ljc0MSAyOS40MSAyNC4zOTQgNTUuMDE0IDUxLjU1NCA2OS4zNzd6Ii8+PC9zdmc+)

Order Status:

This API is used to check the payment status.

Note : It is recommended to rely on Server to server callback response, if not received then you can start calling the Order status API

- Host Details
    
    
    | **Environment** | **Http Method** | **Value** |
    | --- | --- | --- |
    | `UAT` | GET | **https://api-preprod.phonepe.com/apis/pg-sandbox** |
    | `PROD` | GET | **https://api.phonepe.com/apis/pg** |
- End-point
    
    **/checkout/v2/order/{merchantOrderId}/status** – Endpoint is common for UAT and Production.
    
- Complete Host Details
    
    
    | **Environment** | **Http Method** | **Value** |
    | --- | --- | --- |
    | `UAT` | GET | **https://api-preprod.phonepe.com/apis/pg-sandbox/checkout/v2/order/{merchantOrderId}/status** |
    | `PROD` | GET | **https://api.phonepe.com/apis/pg/checkout/v2/order/{merchantOrderId}/status** |
- Request Headers
    
    
    | **Header Name** | **Header Value** |
    | --- | --- |
    | `*Content-Type*` | **application/json** |
    | `*Authorization*` | **O-Bearer <access_token>** |
- Query Parameters
    
    Sample EndPoint Details with Query Parameters:
    
    /checkout/v2/order/{merchantOrderId}/status?details=false&errorContext=true
    
    | **Name** | **Description** |
    | --- | --- |
    | `*details*` | **true → return all attempt details under paymentDetails listfalse → return only latest attempt details under paymentDetails list** |
    | `*errorContext*` | **true → To receive the errorContext block with error details if the state is FAILED.false → If the errorContext block is not required.** |
    - Query the API with above details using HTTP GET method, below is the sample CURL for the same:
        
        ```jsx
        curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/checkout/v2/order/TX123rrty34432456/status?details=false' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: O-Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVzT24iOjE3MTIyNTM2MjU2NDQsIm1lcmNoYW50SWQiOiJWMlNVQlVBVCJ9.7aVzYI_f_77-bBicEcRNuYx093b2wCsgl_WFNkKqAPY'
        
        ```
        
        Sample response (with limited details as “detail=fails”)
        
        ```json
        {
            "orderId": "OMO2403282020198641071317",
            "state": "COMPLETED",
            "amount": 1000,
            "expireAt": 1711867462542,
            "paymentDetails": [
                {
                    "paymentMode": "UPI_QR",
                    "transactionId": "OM2403282020198651071949",
                    "timestamp": 1711694662542,
                    "amount": 1000,
                    "state": "COMPLETED",
                    "rail": {
                        "type": "UPI",
                        "utr": "<utr>",
                        "upiTransactionId": "<upiTransactionId>",
                        "vpa": "<vpa>"
                    },
                    "instrument": {
                        "type": "ACCOUNT",
                        "maskedAccountNumber": "<maskedAccountNumber>",
                        "accountType": "SAVINGS",
                        "accountHolderName": "<accountHolderName>"
                    }
                }
            ]
        }
        ```
        
- Response Details
    - Response Headers
        
        
        | **Header Name** | **Header Value** |
        | --- | --- |
        | `*Content-Type*` | application/json |
    - Order is completed and details = true (200)
        
        Http Response Code: 200
        
        ```json
        {
          "orderId": "OMO2407021511185686967711",
          "state": "COMPLETED",
          "amount": 1000,
          "payableAmount": 1000,
          "feeAmount": 0,
          "expireAt": 1719913878566,
          "metaInfo": {
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": ""
          },
          "paymentDetails": [
            {
              "transactionId": "OM2407021515097451914211",
              "paymentMode": "UPI_INTENT",
              "timestamp": 1719913509762,
              "amount": 1000,
              "payableAmount": 1000,
              "feeAmount": 0,
              "state": "COMPLETED",
              "rail": {
                "type": "UPI",
                "upiTransactionId": "upi12313",
                "vpa": "abcd@ybl"
              },
              "instrument": {
                "type": "ACCOUNT",
                "maskedAccountNumber": "XXXXXX5533",
                "accountType": "SAVINGS"
              },
              "splitInstruments": [
                {
                  "instrument": {
                    "type": "ACCOUNT",
                    "maskedAccountNumber": "XXXXXX5533",
                    "accountType": "SAVINGS"
                  },
                  "rail": {
                    "type": "UPI",
                    "utr": "455069731511",
                    "upiTransactionId": "YBL369f6d962de74c2680789bff8c11aec9",
                    "vpa": "abcd@ybl"
                  },
                  "amount": 1000
                }
              ]
            }
          ]
        }
        ```
        
    - No payment attempt is made for order (200)
        
        ```json
        {
            "orderId": "OMO2407111821482103732111",
            "state": "PENDING",
            "amount": 100,
            "expireAt": 1720702908208,
            "metaInfo": {
                "udf1": "<additional-information-1>",
                "udf2": "<additional-information-2>",
                "udf3": "<additional-information-3>",
                "udf4": "<additional-information-4>",
                "udf5": "<additional-information-5>"
            },
            "paymentDetails": []
        }
        ```
        
    - Order Failed (200)
        
        ```json
        {
            "orderId": "OMO2407121214395503786511",
            "state": "FAILED",
            "amount": 200,
            "expireAt": 1720767279548,
            "errorCode": "INVALID_MPIN",
            "detailedErrorCode": "ZM",
            "metaInfo": {
                "udf1": "<additional-information-1>",
                "udf2": "<additional-information-2>",
                "udf3": "<additional-information-3>",
                "udf4": "<additional-information-4>",
                "udf5": "<additional-information-5>"
            },
            "paymentDetails": [
                {
                    "transactionId": "OM2407121214579231302711",
                    "paymentMode": "UPI_COLLECT",
                    "timestamp": 1720766697944,
                    "amount": 200,
                    "payableAmount": 200,
                    "feeAmount": 0,
                    "state": "FAILED",
                    "errorCode": "INVALID_MPIN",
                    "detailedErrorCode": "ZM"
                }
            ],
            "errorContext": {
               "errorCode" : "INVALID_MPIN",
               "detailedErrorCode" : "ZM",
               "source" : "CUSTOMER",
               "stage" : "AUTHENTICATION",
               "description" : "Wrong MPIN was entered"
            }
        }
        ```
        
    - Invalid order ID
        
        ```json
        {
            "success": false,
            "code": "MERCHANT_ORDER_MAPPING_NOT_FOUND",
            "message": "No entry found for <Merchant Order Id>",
            "data": {}
        }
        ```
        
    
- Response Parameters
    
    
    | **Header Name** | **Data Type** | **Description** |
    | --- | --- | --- |
    | `*orderId*` | **String** | **PG generated internal order id** |
    | `*state*` | **String** | **State of order, Expected Values = [PENDING, FAILED, COMPLETED]Note**: Merchants should rely only on the “**state**” parameter for the Payment status confirmation. |
    | `*amount*` | **String** | **Order amount in paisa** |
    | `*expireAt*` | **Long** | **order expiry time in epoch** **(in milliseconds)** |
    | `*metaInfo*` | **Object** | **Merchant defined meta info passed at the time of order creation** |
    | `*paymentDetails*` | **List** | **Contain list of details of each payment attempt made corresponding to this order.** |
    | `*paymentDetails.paymentMode*` | **String** | **Mode of payment. Expected Values = [UPI_INTENT, UPI_COLLECT, UPI_QR, CARD, TOKEN, NET_BANKING]** |
    | `*paymentDetails.timestamp*` | **Long** | **Transaction attempt timestamp in epoch** **(in milliseconds)** |
    | `*paymentDetails.amount*` | **Long** | **Amount in paisa, corresponding to payment attempt** |
    | `*paymentDetails.transactionId*` | **String** | **internal transaction id for given payment attempt** |
    | `*paymentDetails.state*` | **String** | **Transaction attempt state. Expected Values = [PENDING, COMPLETED, FAILED]** |
    | `*paymentDetails.errorCode*` | **String** | **Error code (Only present when transaction state is failed)** |
    | `*paymentDetails.detailedErrorCode*` | **String** | **Detailed Error Code (Only present when transaction state is failed)** |
    | `*paymentDetails.rail*` | **String** | **Contains processing rail details under which payment attempt is made.** |
    | `*paymentDetails.rail.type*` | **String** | **Type of rail. Expected values = [UPI, PG]** |
    | `*paymentDetails.instrument*` | **String** | **Contains instrument details** |
    | `*paymentDetails.instrument.type*` | **String** | **Type of payment instrument. Expected values = [ACCOUNT,CREDIT_CARD, DEBIT_CARD,NET_BANKING]** |

Refund:

This API is used to initiate the refund.

POST – [https://api-preprod.phonepe.com/apis/pg-sandbox/payments/v2/refund](https://api-preprod.phonepe.com/apis/pg-sandbox/payments/v2/refund)

- Host Details
    
    
    | **Environment** | **Http Method** | **Value** |
    | --- | --- | --- |
    | `UAT` | POST | **https://api-preprod.phonepe.com/apis/pg-sandbox** |
    | `PROD` | POST | **https://api.phonepe.com/apis/pg** |
- Endpoint
    
    **/payments/v2/refund** – Endpoint is common for UAT and Production
    
- Complete Host Details
    
    
    | **Environment** | **Http Method** | **Value** |
    | --- | --- | --- |
    | `UAT` | POST | **https://api-preprod.phonepe.com/apis/pg-sandbox/payments/v2/refund** |
    | `PROD` | POST | **https://api.phonepe.com/apis/pg/payments/v2/refund** |
- Request Header
    
    
    | **Header Name** | **Header Value** |
    | --- | --- |
    | `*Content-Type*` | **application/json** |
    | `*Authorization*` | **O-Bearer <access_token>** |
- Request Parameter
    
    
    | **Parameter Name** | **Data Type** | **Mandatory(Y/N)** | **Description** | **Constraints** |
    | --- | --- | --- | --- | --- |
    | `*merchantRefundId*` | String | Yes | Unique merchant refund id generated by merchant. | Max Length = 63 characters |
    | `*originalMerchantOrderId*` | String | Yes | Original merchant order id against which refund is required. |  |
    | `*amount*` | Long | Yes | Amount in paisa to refund. | Min Value = 100 (In Paise) |
- Request Body
    
    ```json
    {
        "merchantRefundId": "Refund-id-12345",
        "originalMerchantOrderId": "Order-12345",
        "amount": 1234
    }
    ```
    
- Response
    - Response Field Details
        
        
        | **Field Name** | **Data Type** | **Description** |
        | --- | --- | --- |
        | `*refundId*` | **String** | **PG generated internal refund id** |
        | `*amount*` | **Long** | **Amount in paisa to refund** |
        | `*state*` | **String** | **refund state, expected value = PENDING** |
    - Refund initiated successfully
        
        ```json
        {
            "refundId": "OMRxxxxx"
            "amount": 1234,
            "state": "PENDING"
        }
        ```
        

Refund Status: 

This API is used to check the refund status.

## Requirements overview (optional)

## User stories / User flow

## Requirements

---

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

/