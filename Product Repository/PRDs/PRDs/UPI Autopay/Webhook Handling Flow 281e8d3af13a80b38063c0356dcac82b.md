# Webhook Handling Flow

## What problem are we solving?

Currently, during UPI mandate setup via Digio, we incorrectly treat Auth webhooks (Auth Success / Auth Failure) as the final mandate status. This causes:

- False positives (e.g., Auth Success but later Auto Debit(Rs 1) fails).
- Customers setting mandate on a different bank account, than the registered one, move ahead in the journey but mandate gets revoked later due to TPV failure.
- Inconsistent mandate states that require manual Ops intervention.

---

## How do we measure success?

- % reduction in Ops tickets related to mandate status mismatch.
- TAT for mandate setup
- L2 Metric: % of users completing the application without getting stuck due to mandate issues.

---

## What is the solution?

### Flow Updates

**Mandate Initiation**

- User lands on Volt mandate setup screen post bank account verification.
- Mandate status field needs to be added on this screen as shown below. 
If the mandate setup is not initiated then this status will be shown as “Not registered”
If the mandate setup is in the pending state then this status will be shown as “In Progress”
If the mandate setup fails then this status will be shown as “Failed”
If the mandate setup is successful then this status will be shown as “Success”

![Screenshot 2025-10-08 at 10.44.30 AM.png](Webhook%20Handling%20Flow/Screenshot_2025-10-08_at_10.44.30_AM.png)

- When the user clicks on the Setup mandate tab they will be redirected to the DSP screen.
- This DSP screen theme needs to be the Volt app theme the pallete for which is provided in the Figma design.
- On the DSP screen, user will be provided with the option of selecting between UPI and Nach mandate type.
- For B2C users UPI mandate(UPI Autopay) needs to be the ‘recommended’ mandate type.
- For B2B2C users Nach mandate(Bank Autopay) needs to be the ‘recommended’ mandate type.
- If the user clicks on Nach and proceeds then the flow will be same as currently in Nach mandate setup. We need to ensure that the mandate status is displayed on the Volt screen based on the status of the nach mandate.
- If the user clicks on UPI mandate and proceeds then the user is redirected to the Digio screen for the mandate setup.
- On the Digio screen user will be able to select from any of the following modes: Intent, Collect and QR scan
- When a user selects from any of the mode for UPI mandate setup they will be landing on the UPI app wherein to approve/authorize the mandate the user will enter the UPI Pin. If the UPI Pin is entered correctly then the mandate is approved/authorized. Now a Rs 1 auto-debit will happen from the user’s bank account to register the mandate successfully.
- If the user opted the mandate setup through the Intent mode then they will be redirected automatically to the Digio screen and will be shown ‘Authorization successful’ and will be redirected back to the DSP screen.
- If the user opted the mandate setup through the Collect/QR mode then they will manually come back to the Digio screen and will be shown ‘Authorization successful’ and will be redirected back to the DSP screen.

Please refer to the following Figma link for reference: https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=4-10&p=f&t=UYK3pHOy2gMgdbGI-0

**Auth Webhook Handling**

Below are the two auth webhooks which we receive from Digio for UPI mandate setup:
1. [UPI.MNDT.AUTHSUCCESS](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtauthsuccess): This webhook is received when the user enters the correct UPI PIN and approves/authorizes the mandate.
2. [UPI.MNDT.AUTHFAIL](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtauthfail): This webhook is received when the user enters incorrect PIN for mandate authorization.

- In the above cases when the user enters the correct UPI PIN and approves the mandate we will be getting an **Auth Success webhook**. This webhook is currently treated as the Terminal webhook for UPI mandate registration success. We need to make changes in order to mark the mandate status as Pending/In Progress when this webhook is received as this is an intermediate status webhook and not a terminal status one.
- In the above cases when the user enters incorrect UPI PIN then we will be getting an **Auth Failed webhook**. This webhook is currently treated as the Terminal webhook for UPI mandate registration failure. We need to make changes in order to mark the mandate status as Pending when this webhook is received as this is an intermediate status webhook and not a terminal status one. In this case user will land on the Digio screen and will be able to either re-attempt the mandate setup from Digio or they can manually come back to the DSP screen.
- In case the user either gets automatically redirected or they manually get back to the DSP screen before any of the Auth Webhooks are received then we need to show the user an In-Progress screen(Will be discussed later in this prd).

**Terminal Webhooks**

Below are the terminal webhooks which we receive from Digio for UPI mandate setup:

1.  [UPI.MNDT.AUTO.DEBIT.SUCCESS](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtautodebitsuccess): This webhook is the Terminal Mandate registration success webhook.
2. [UPI.MNDT.AUTO.DEBIT.FAILURE](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtautodebitfailure): This webhook is a Terminal Mandate registration failure webhook.
3. [UPI.MNDT.REVOKED](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtrevoked): This webhook is a Terminal Mandate registration failure webhook. This webhook is triggered by Digio when the mandate setup was attempted in a different bank account than the registered bank account.
4. [UPI.MNDT.REGISTER.FAILURE](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtregisterfailure): This webhook is a Terminal Mandate registration failure webhook. This is triggered by Digio when the “Revoked” status is not received by Digio from the PSP app within 5 mins from “Auth Success Webhook”.

**Terminal Webhooks Handling**

- **Auth Success flow**: If we receive an Auth Success Webhook from Digio then we will mark the Mandate status as Pending. Post the reception of this webhook we can receive the following terminal webhooks:

1. [UPI.MNDT.AUTO.DEBIT.SUCCESS](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtautodebitsuccess): Once this webhook is received only then we need to mark the status of the Mandate setup as successful.
2. [UPI.MNDT.AUTO.DEBIT.FAILURE](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtautodebitfailure): Once this webhook is received then we need to mark the status of the Mandate setup as Failed.
3. [UPI.MNDT.REVOKED](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtrevoked): Once this webhook is received then we need to mark the status of the Mandate setup as Failed.
4. [UPI.MNDT.REGISTER.FAILURE](https://documentation.digio.in/digicollect/nach/nach_registration/#upimndtregisterfailure): Once this webhook is received then we need to mark the status of the Mandate setup as Failed.

Any of the above Terminal webhooks can be received with a delay post the reception of the Auth success webhook. **We need to keep the user on the In-Progress screen until one of the above Terminal webhooks is received.** This will block the customer from moving ahead in the journey without having a successful mandate setup with us.
- **Auth Fail flow**: If we receive an Auth Failed Webhook from Digio then we will mark the Mandate status as Pending. There will be multiple scenarios in this case:

1. User retries the mandate setup from the Digio screen itself. In this case, for the same mandate request we will be receiving Auth success webhook as well if user successfully approves/authorizes the mandate by entering the correct UPI PIN. Here, we need to follow the same process as discussed in the above ‘Auth Success flow’ pointer.

2. User retries the mandate setup from the Digio screen itself but we don’t receive any webhook response from Digio by the time user lands back on the DSP screen. In this case we need to make the user wait on the In Progress screen until we receive a webhook response from Digio. 
- If we receive an Auth success webhook in few seconds then we need to make the user wait a bit longer on the In Progress screen until the terminal status webhook is received. 
- If we receive another Auth fail response from Digio then we fail the mandate and let the user retry the mandate setup .
- If we don’t receive any auth webhook from Digio then we will make the customer wait on the In Progress screen for 15 seconds then fail the mandate setup and ask the user to retry. In the backend if we receive a terminal success webhook response for the initial request then we will trigger the mandate cancellation api to cancel the mandate.

3. User does not retry the mandate setup through Digio screen and lands back on the DSP screen, then we will make the customer wait on the In Progress screen for 15 seconds then fail the mandate setup and ask the user to retry. In the backend if we receive a terminal success webhook response for the initial request then we will trigger the mandate cancellation api to cancel the mandate.

### In Progress Screen

- This screen will be a waiting screen which will be shown to the customer when the terminal status of mandate setup is not received from Digio.
- This screen will have the components in Volt’s theme.
- If the customer presses the device back button while being on the In Progress screen then the customer will land on Volt’s Setup Mandate screen and the status of the mandate will be shown as ‘In Progress’. Here the user will only have the option to go back to the Homepage. Customer won’t be able to move ahead in the journey until the terminal status of the Mandate setup is received from Digio. Please refer to the below screen for reference:

![Screenshot 2025-10-29 at 11.06.21 AM.png](Webhook%20Handling%20Flow/Screenshot_2025-10-29_at_11.06.21_AM.png)

---