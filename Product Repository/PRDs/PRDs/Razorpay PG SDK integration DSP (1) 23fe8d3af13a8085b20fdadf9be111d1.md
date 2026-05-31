# Razorpay PG SDK integration: DSP (1)

: Ameya Aglawe
Created time: July 29, 2025 2:16 PM
Status: Ready for Tech
Last edited: July 29, 2025 2:16 PM
Owner: Vaibhav Arora
Assignee: Vaibhav Arora

# **What problem are we solving?**

As an LSP we have integrated with lender repayments flow via web integrations where the repayment pages are loaded as screens (web-view) and open the URLs in the web-view (Android and iOS) or as tabs replacing Volt’s URL (Web). 

In parallel, we rely on backend for the status of the user sessions via deep checks. This process is not optimal and often causes the following issues:

1. Blank screen opens (link comes from backend via lenders) 
2. Delayed status (backend is dependent on lender for status, client application gets status from backend)
3. Web hook drops - Amount gets debited from the user’s account but we are not able to show the respective status of the transaction
4. Inconsistent experience - We are reliant on lender UIs as integrated flows which are often not designed for all devices (aspect ratios) leading to inconsistent experience for users

With SDK integrations on Android and iOS (Client side integration) since the client (FE application) will be invoking the checkout experience, we will be able to control the UI, get callback responses on FE directly, and customise the UI for the user to improve experience.

---

# **How do we measure success?**

| **Metric** | **Definition** | **Measurement Method** | Expectations |
| --- | --- | --- | --- |
| Transaction Success Rate | Percentage of successfully completed repayment transactions out of the total initiated transactions. | Payment gateway reports, backend logs, analytics tools | 97% or higher |
| User Drop-off Rate | Percentage of users who abandon the repayment process before completing the transaction. | Funnel analysis, session tracking | 3% or lower |
| Retry Rate | Percentage of transactions that required a retry due to temporary failures (e.g., network issues, timeouts). | Transaction logs, number of transactions in an order | 2-3% or lower |
| API Latency | Average response time of APIs involved in the repayment process (e.g., transaction initiation, status update, confirmation). | API monitoring tools, backend logs | < 500ms |
| Transaction confirmation TAT | TAT it takes for LSP to confirm the transaction to the user post signature confirmation | Logs, API monitoring tools, Amplitude events | 5 seconds or lower |

---

# **How are others solving this problem?**

![WhatsApp Image 2024-09-05 at 8.18.25 PM.jpeg](Razorpay%20PG%20SDK%20integration%20DSP/WhatsApp_Image_2024-09-05_at_8.18.25_PM.jpeg)

![WhatsApp Image 2024-09-05 at 8.18.27 PM (1).jpeg](Razorpay%20PG%20SDK%20integration%20DSP/WhatsApp_Image_2024-09-05_at_8.18.27_PM_(1).jpeg)

![WhatsApp Image 2024-09-05 at 8.18.26 PM (1).jpeg](Razorpay%20PG%20SDK%20integration%20DSP/WhatsApp_Image_2024-09-05_at_8.18.26_PM_(1).jpeg)

![WhatsApp Image 2024-09-05 at 8.18.27 PM.jpeg](Razorpay%20PG%20SDK%20integration%20DSP/WhatsApp_Image_2024-09-05_at_8.18.27_PM.jpeg)

![WhatsApp Image 2024-09-05 at 8.18.26 PM.jpeg](Razorpay%20PG%20SDK%20integration%20DSP/WhatsApp_Image_2024-09-05_at_8.18.26_PM.jpeg)

![WhatsApp Image 2024-09-05 at 8.20.00 PM.jpeg](Razorpay%20PG%20SDK%20integration%20DSP/WhatsApp_Image_2024-09-05_at_8.20.00_PM.jpeg)

![WhatsApp Image 2024-09-05 at 8.18.28 PM.jpeg](Razorpay%20PG%20SDK%20integration%20DSP/WhatsApp_Image_2024-09-05_at_8.18.28_PM.jpeg)

---

# **What is the solution?**

We will be integrating React Native SDK for Android and iOS to improve user experience while they make repayments as a client side integration with Volt.

**Documentation:**

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/) (Android)

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/) (iOS)

## User stories / User flow

### Configuration

Below are the items configured at Razorpay’s end.

- Supported payment methods
    - UPI
    - Netbanking
    - Debit Card
- Ordering of payment methods
    - UPI (flat charge for NBFC)
    - Netbanking (flat charge for NBFC)
    - Debit Card (%age of transaction value for NBFC)
- Logo of DSP
- Settlement bank account

### User Journey

Below is the user flow on the app/web.

- User initiates the repayment request on Volt’s app
- 

![image.png](Razorpay%20PG%20SDK%20integration%20DSP/image.png)

### Settlements

Razorpay will be settling to our underlying bank account on a T+n (where n = 1 or the next working day). 

## Requirements

**Input parameters**

| Parameter name | Mandatory | Parameter type | Description | Value |
| --- | --- | --- | --- | --- |
| key | Yes | String | To be generated from Rzp dashboard | TBD |
| Amount | Yes | Integer | Amount selected by the user on client application in the smallest currency sub-unit. For example, if the amount to be charged is ₹299.00, then pass 29900 | Amount in paisa*100 |
| Currency | Yes | String | Currency of amount | INR. Hardcoded |
| Name | Yes | String | Name of the business | DSP Finance Pvt Ltd |
| image | No | String | Public hosted URL of Volt logo | Hardcoded |
| pre-fill | No | JSON object | JSON object with pre-filled values to improve user payment experience | name: User name (Can be pre-filled in case of card payments)

contact: + {country code}{phone number}

email: {email of the user}

payment method: pre-selected payment method for ease of payment:

For payment: Below 50k pass upi above 50k, pass netbanking

"bank_account": {
"beneficiary_name": "Gaurav Kumar",
"account_number": "1121431121541121",
"account_type": "savings",
"ifsc_code": "HDFC0000001"
} |
| Theme | No | JSON object | JSON object to pass theme and backdrop colors | color: Volt primary color hexcode (string)

Backdrop: Volt secondary color hexcode  (string)

(B2B white labelling controlled) |
| Modal | No | JSON object | JS configurations to control the behaviour of SDK | backdropclose: (boolean) false

Indicates whether clicking the translucent blank space outside the Checkout form should close the form.

escape: (boolean)
false

Controls exit content does not close on pressing back

handleback: (boolean)
false

confirm close: (boolean)
true

opens confirmation dialog when user tries to close checkout

ondismiss: (function)

Calls a function when user dismisses the checkout page (to handle user abandonment on checkout screens)

animation: true

Adds a loader animation before checkout page is loaded for the user
 |
| callback_url  ❌ | No  | string | To send callback | We will not be integrating callback flow and instead will be capturing header values and handling redirection since failure callbacks are not passed in the callback flow |
| customer_id | No | string | Send unique identifiers for customers to load saved cards in subsequent payments | Client ID of the customer |
| remember customer | No | boolean | Send a flag to load previously saved cards for the user | True |
| timeout  | No | integer | Send timeout in seconds | User payment (not order) will terminate and a new payment will get initiated. (Should be 10 minutes) |
| readonly | No | Boolean | Makes few parameters read only and blocks editing | Make phone email and name as read only parameters |
| hidden | No | JSON object | JSON object for additional features | allowrotation: false (boolean)

Blocks rotation of checkout screen

retry: (object)
(enabled: true
max count: 4 - recommended by Rzp)

Config (object)
(Payment methods config

Ordering of payments:
UPI
Netbanking 
Card

Hide all remaining payment options from the user

https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/configure-payment-methods/sample-code/#show-only-a-certain-payment-method-on-checkout |
| send_sms_hash | Yes |  |  |  |

### Payment selection BRE (To be passed in checkout configurations)

| **Amount** | **Scenario** | **Default payment method** |
| --- | --- | --- |
| <50,000 |  | UPI |
| >50,000 |  | Net Banking |
|  |  | Debit card |

[Screenshot 2024-09-05 at 5.53.49 PM.png](Razorpay%20PG%20SDK%20integration%20DSP/Screenshot_2024-09-05_at_5.53.49_PM.png)

![image.png](Razorpay%20PG%20SDK%20integration%20DSP/image%201.png)

Payment method analysis:

UPI Intent:

```r
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>phonepe</string>
    <string>paytmmp</string>
    <string>credpay</string>
    <string>freecharge</string>
    <string>in.fampay.app</string>
    <string>bhim</string>
          <string>amazonpay</string>
          <string>payzapp</string>
          <string>jupiter</string>
          <string>icici</string>
          <string>sbiyono</string>
          <string>myjio</string>
          <string>bobupi</string>
          <string>shriramone</string>
          <string>indusmobile</string>
          <string>whatsapp</string>
</array>
```

Status handling:
On receiving the header value, FE will call the backend deep check API (Volt backend) to get the status of the transaction. 

Flow of information:

User completes transaction → Razorpay sends web hook to Fenix BE → Fenix BE sends status to Volt BE → Volt FE polls Volt BE API for status of the transaction

<aside>
⚠️

Need to ensure that this flow of information does not introduce a lag for the user

</aside>

---

Success callback:

```sql
{
  "razorpay_payment_id": "pay_29QQoUBi66xm2f",
  "razorpay_order_id": "order_9A33XWu170gUtm",
  "razorpay_signature": "9ef4dffbfd84f1318f6739a3ce19f9d85851857ae648f114332d8401e0949a3d"
}
```

Failure callback

```sql

rzp1.on('payment.failed', function (response){
    alert(response.error.code);
    alert(response.error.description);
    alert(response.error.source);
    alert(response.error.step);
    alert(response.error.reason);
    alert(response.error.metadata.order_id);
    alert(response.error.metadata.payment_id);
}
```

Signature verification:

All callbacks from the SDK are validated via a signature (passed in success callback) to ensure the payment was actually completed by the user:

To create a signature use the following steps:

- Create a signature
    - Order ID (received from client application from backend while creating checkout)
    - Razorpay payment id (Success callback)
    - key_secret
    - Create a pipe separated string and use the SHA256 algorithm to create an HMAC hex
        
        ```sql
        generated_signature = hmac_sha256(order_id + "|" + razorpay_payment_id, secret);
        
          if (generated_signature == razorpay_signature) {
            payment is successful
          }
        ```
        
- Validate the above signature with signature received in success callback

Error message handling;

```sql
Sample error response:
{
  "error": {
    "code": "BAD_REQUEST_ERROR",
    "description": "Authentication failed due to incorrect otp",
    "field": null,
    "source": "customer",
    "step": "payment_authentication",
    "reason": "invalid_otp",
    "metadata": {
      "payment_id": "pay_EDNBKIP31Y4jl8",
      "order_id": "order_DBJKIP31Y4jl8"
    }
  }
}
```

Response parameters:

| Parameter name | Type | Description |
| --- | --- | --- |
| code | string | Enum for type of error |
| Description | string | Description of error  |
| field | string | Name of the field is passed if a specific filed is passed incorrectly |
| reason | string | readable reason for failure of payment |
| metadata | object | meta data for the payment (payment id and order id) |

### Out of Scope

[https://razorpay.com/docs/errors/payment-methods/list/](https://razorpay.com/docs/errors/payment-methods/list/)
(Different error messages and their respective handling: Like mandate can be done)

---

# **Design**

[https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=6272-6648&node-type=SECTION&t=H8wc8fnpYa867OEL-0](https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=6272-6648&node-type=SECTION&t=H8wc8fnpYa867OEL-0)

---

# **Analytics**

We will need to capture the below items.

- Payment method at order level
- Error code at order/transaction level
- Network (VISA/Master/Rupay) for Debit card at order level
- Bank names (Netbanking) of repayment
- UPI ID of the payer
- Timestamp of invocation of SDK
- Timestamp of redirection of SDK

---

# **Timeline/Release Planning**

---

# **Go to market**

NA

## Marketing

NA

## Ops & Sales training

- Training to be setup for support teams
- Training to be setup for operations teams from a reconciliation perspective

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes