# Improving Mandate Conversions

: Parikshit Kumar
Created time: July 13, 2025 10:47 PM
Status: In progress
Last edited: March 17, 2026 4:46 PM

# What problem are we solving?

- **Drop offs** in API-based eNACH mandates (due to vendor, bank or customer issues).
- **Drop-offs during Digio SDK invocation** due to performance/UI issues or trust gap.
- **Lack of modern mandate options** like UPI Autopay, which offers faster setup and better UX.
- **Inflexibility in fallback options**, e.g., esign/physical not clearly surfaced or too complex.
- **No recovery mechanisms**: Failed mandates are not followed up with retries, reminders, or alternate suggestion
- Problem identification
    - Digio SDK does not get invoked when the user chooses to set up autopay
    - Digit SDK has an intermittent failure or there is a downtime.

# How do we measure success?

### L1 Metrics:

- Mandate Setup Conversion Rate
- eNACH Setup Success Rate
- UPI Mandate Conversion Rate

### L2 Metrics:

- Number of attempts per customer
- Retry Success Rate/Retry Recovery Rate for users who fail initially but complete later
- Average Time to Complete Mandate Setup
- % Drop after Mandate Setup

# What is the Solution?

### A. Mandate Method Expansion

- UPI Autopay Integration
- eNach Optimization
- Simplified Nach(To be explored)
- Fallback Hierarchy

### B. UX and UI Improvements

- Improve Mandate Selection Screen
- Provide Trust Signals

### C. Retry, Reminder and Recovery Engine

- Retry Logic
- Automated Nudges
- Partner Callback Triggers

### D. Personalisation and Routing Logic

- Bank Support Mapping
- Partner SDK Routing

# Solutions Detailing

## **Mandate Method Expansion**

### A. UPI Mandate Integration

[UPI Autopay ](UPI%20Autopay%20231e8d3af13a807d93a7ee2862162467.md)

### B. eNach Optimization

- Dynamic **mandate amount calculation** based on user-selected limit:

[NBFC NACH: Mandate Limit Change](NBFC%20NACH%20Mandate%20Limit%20Change%20202e8d3af13a8003868efd6ae04f263c.md)

- Error state management:

[Nach SR Optimizations](Improving%20Mandate%20Conversions/Nach%20SR%20Optimizations%2022fe8d3af13a80c9b8f3ed67d468b1df.md)

### C. Fallback Hierarchy

- API eNACH → UPI Autopay → esign NACH → Physical NACH
- Show only supported flows as per user’s bank

## **UX and UI Improvements**

### A. Improve Mandate Selection Screen

- Clearly explain all mandate options
- Show speed, success rate, and supported banks per method

### B. Provide Trust Signals

- Explain that mandate setup process is secure
- Provide tutorials, hints and information icons

## **Retry, Reminder and Recovery Engine**

### A. Retry Logic

- Enable **1-click retry** via deep links in push/SMS/email
- 

### B. Automated Nudges

- Setup multi-channel nudges (Push > SMS > WhatsApp > Email).
- Personalized messages

### C. Partner Callback Triggers

- Notify partners on failure and retry trigger points

## **Personalisation and Routing Logic**

### A. Bank Support Mapping

- Provide best available mandate method through a real time bank support

### B. Partner SDK Routing

- Different routing approaches based on channels and BRE

# Business Rule Engine

## OD Product(To be finalised)

- In case of OD product we debit the per month interest for the drawn facility and the charges on the facility(if any).
- Based on the data almost 99% of our users across multiple channels(B2C, B2B, B2B2C Channels) have a DP of less than or equal to 15 Lakhs. Based on the data we will have the below approach.
- Users with selected offer equal to or less than 5 lakhs should only be provided with the option to set up UPI mandates. If these users try and enhance their facility to more than 5 lakhs then a re-mandate should be done.
- Users with selected offer between 5 lakhs and 15 Lakhs should be provided with both the options of eNACH and UPI autopay with the recommended option being eNACH. If they try to enhance their facility then a re-mandate should be done.
- Users with selected offer greater than 15 lakhs should only be provided the option of setting up a NACH mandate.

## Term Loan(DSP 100%)(Pending)

- In case of Term Loan product, before the mandate setup process we will get to know the tenure for which the user is opting the Tranche for.
- If the EMI amount for the first tranche in such a case comes to be more than 15k then such a user will be provided with an option to only setup an eNACH mandate.
- If the EMI amount for the first tranche in such a case comes to be less than 15k then we will provide the option to the user to setup a UPI mandate with a Fall back of Nach Mandate. If such a user takes subsequent drawdowns from us then if the aggregated EMI amount

# Approach for Channels

*Based on the BRE there will be three different user personas:*

*User Persona 1: Will only be shown UPI mandate option**(We might not go ahead with this)***

*User Persona 2: Will be shown both options of UPI and Nach mandate*

*User Persona 3: Will only be shown Nach mandate option*

**Channelwise approach(Post BA verification):**

**B2C Organic:**

1. **Android and iOS:**
    
    A. User Persona 1: User will be shown the option to set up the mandate. Once they continue(Either Digio SDK/Our screens with PhonePe APIs) they will be able to set up the mandate through the Intent or the Collect flow.
    

B. User Persona 2: We can directly show users two different options of Nach and UPI(Accordingly the DC/NB option appears in Nach & Intent/Collect options appear in UPI) or we can show them the option of setup mandate by either of the three modes: UPI ID, Debit Card and Net Banking(If user selects DC or NB then the Nach flow will be triggered if UPI is selected then the Intent/Collect option will be shown to the user.

C. User Persona 3: Flow remains as is

1. **Web:**
    
    A. User Persona 1: User will be shown the option to set up the mandate. Once they continue(Either Digio SDK/Our screens with PhonePe APIs) they will be able to set up the mandate through the QR or the Collect flow.
    

B. User Persona 2: We can directly show users two different options of Nach and UPI(Accordingly the DC/NB option appears in Nach & QR/Collect options appear in UPI) or we can show them the option of setup mandate by either of the three modes: UPI ID, Debit Card and Net Banking(If user selects DC or NB then the Nach flow will be triggered if UPI is selected then the QR/Collect option will be shown to the user.

C. User Persona 3: Flow remains as is

**Volt B2B:**

1. **Redirection Flow(App):**
    
    A. User Persona 1: User will be shown the option to set up the mandate. Once they continue(Either Digio SDK/Our screens with PhonePe APIs) they will be able to set up the mandate through the Intent(Deep linking if possible) or the Collect flow.
    

B. User Persona 2: We can directly show users two different options of Nach and UPI(Accordingly the DC/NB option appears in Nach & Intent(Deep linking if possible)/Collect options appear in UPI) or we can show them the option of setup mandate by either of the three modes: UPI ID, Debit Card and Net Banking(If user selects DC or NB then the Nach flow will be triggered if UPI is selected then the Intent(Deep linking if possible)/Collect option will be shown to the user.

C. User Persona 3: Flow remains as is

1. **SSO Flow:**

A. User Persona 1: User will be shown the option to set up the mandate. Once they continue(Either Digio SDK/Our screens with PhonePe APIs) they will be able to set up the mandate through the Intent or the Collect flow.

B. User Persona 2: We can directly show users two different options of Nach and UPI(Accordingly the DC/NB option appears in Nach & Intent/Collect options appear in UPI) or we can show them the option of setup mandate by either of the three modes: UPI ID, Debit Card and Net Banking(If user selects DC or NB then the Nach flow will be triggered if UPI is selected then the Intent/Collect option will be shown to the user.

C. User Persona 3: Flow remains as is

1. **Volt SDK(App):**

A. User Persona 1: User will be shown the option to set up the mandate. Once they continue(Either Digio SDK/Screens with PhonePe APIs) they will be able to set up the mandate through the Intent or the Collect flow.

B. User Persona 2: We can directly show users two different options of Nach and UPI(Accordingly the DC/NB option appears in Nach & Intent/Collect options appear in UPI) or we can show them the option of setup mandate by either of the three modes: UPI ID, Debit Card and Net Banking(If user selects DC or NB then the Nach flow will be triggered if UPI is selected then the Intent/Collect option will be shown to the user.

C. User Persona 3: Flow remains as is

1. **Volt SDK(Web):**

A. User Persona 1: User will be shown the option to set up the mandate. Once they continue(Either Digio SDK/Our screens with PhonePe APIs) they will be able to set up the mandate through the QR or the Collect flow.

B. User Persona 2: We can directly show users two different options of Nach and UPI(Accordingly the DC/NB option appears in Nach & QR/Collect options appear in UPI) or we can show them the option of setup mandate by either of the three modes: UPI ID, Debit Card and Net Banking(If user selects DC or NB then the Nach flow will be triggered if UPI is selected then the QR/Collect option will be shown to the user.

C. User Persona 3: Flow remains as is

**B2B2C:**

A. User Persona 1: RMs will be shown the option to set up the mandate for the user. Once they continue(Either Digio SDK/Our screens with PhonePe APIs) they will be able to set up the mandate for the user by either generating the QR for the user and sending it to them to scan and setup or through the collect flow.

B. User Persona 2: We can directly show RMs two different options of Nach and UPI(Accordingly the DC/NB option appears in Nach & QR/Collect options appear in UPI) or we can show them the option of setup mandate by either of the three modes: UPI ID, Debit Card and Net Banking(If RM selects based on user consent DC or NB then the Nach flow will be triggered if UPI is selected then the QR/Collect option will be shown to the RM.

C. User Persona 3: Flow remains as is

# How are others solving this problem?

| **Organizations** | **Mandate Types** | **Approach** | **Success Rates**  |
| --- | --- | --- | --- |
| CRED | Nach, UPI(Launched 1 month back) | - Based on the Loan amount user gets the option of either Nach or UPI with an alternative of Nach | - Nach Registration SR: 85%
- UPI(with Nach as alternative) Registration SR: 94%
- Nach Presentation SR:
- UPI Presentation SR(1st Debit): 
- UPI Presentation SR(2nd Debit): |
| Navi |  |  |  |
|  |  |  |  |