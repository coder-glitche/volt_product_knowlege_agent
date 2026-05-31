# User Story template

# Guidelines

**How should user stories be written?**

- Each user story should be atomic — focus on one activity or action.
    - One feature needs to have multiple user stories for each activity.
    - For the UPI mandate registration feature, this will be:
        - Context page.
        - Mandate registration page.
        - UPI registration (TPAP).
        - Post-registration confirmation.
        - Retry or fallback, if required.
- Each user story should be written from a user/customer perspective.
    - Users can be internal users like sales, support, or operations OR
    - User can be customer OR
    - User can be a partner (B2B or LSP)
- User stories should document key scenarios and how they will be handled from a UI/UX perspective.
    - For the UPI mandate feature, this will be:
        - Mandate registration is pending due to user inactivity.
        - Mandate registration failure due to user error.
        - Mandate registration failure due to technical issues.
        - Mandate registration success.
        - Delayed confirmation handling.

# Template

Below is a template for User Stories.

- **User Story ID**: this is a unique identifier in a PRD that is linked to a user story. This can be alphanumeric like U1 or US1, etc.
- **User Story**: this will be a 1-2 liner that will talk about the user story in question. This will mention what the user is setting out to achieve.
- **User requirements**: this will be the detailed requirements, by building which, the user will be able to achieve the requirement.

# Example

Below is a list of User Stories keeping UPI mandate registration as an example.

- **U1**: As a customer, I want to know why a recurring debit needs to be setup so that I can move forward with setting up a mandate.
    
    **Flow**: Once the customer has completed the bank account verification step and the bank is verified, the customer is presented a screen to setup a auto-debit (mandate).
    
    **Success criteria**: The customer should be able to understand the rationale for an auto-debit and move forward in the journey.
    
    **Requirement**: Below are the requirements for this page.
    
    - Once the user lands on this page, the user should be conveyed that Volt will setup a mandate to debit the monthly interest.
    - This will be a common page that will cover both NACH and UPI mandate.
    - This page will describe that customer’s bank account will be debited automatically and not require the customer to pay.
    - This page will also show that the customer has the option to setup a recurring debit using NACH or UPI.
    - The customer is displayed their debit date, which is 7th of every month.
    - When the customer clicks on Proceed after choosing the mandate method type, an Amplitude event will be fired
    - This page will be white-labelled or in the color scheme of the partners for Volt B2B partners.
    - This page will mention the last 4 digits of the bank account against which the mandate needs to be setup using UPI or NACH.
- **U2**: As a lender, I want only a specific set of customers to setup mandate through UPI so that we can recover our dues to cover out exposure.
    
    **Flow**: Once the customer has completed the bank account verification step and the customer has selected the offer at the offer page.
    
    **Success criteria**: The customer should be able to view UPI and NACH mandate option if eligible or view only NACH if not eligible for UPI.
    
    **Requirement**: Below are the requirements for this logic.
    
    - The customer chooses the offer at the offer page step and Volt stores the amount in the DB.
    - If the amount is ≤ 3L, the customer is eligible for UPI mandate for the OD offering.
    - If the amount is >3L, the customer can setup a mandate using NACH only.
- **U3**: As a lender, I want to decide the mandate amount logic so that the customer sees the relevant amount on the UI.
    
    **Flow**: Once the customer has completed the bank account verification step and the customer has selected the offer at the offer page.
    
    **Success criteria**: The customer should be able to view UPI and NACH mandate option with the relevant limit amount.
    
    **Requirement**: Below are the requirements for this logic.
    
    - If the customer chooses UPI as the option, the mandate amount will be setup for 15K only. DSP can present the mandate multiple times to recover upto 1L/day.
    - If the customer chooses NACH as the option, the mandate amount will be the same as the offer amount.
    - For NACH, the registration amount will be capped to 10L irrespective of the offer selected by the customer/MFD.
- **U4**: As a customer, I want to setup a recurring debit using UPI mandate.
    
    **Flow**: Once the customer has read the mandate education page and has chosen to setup a mandate using UPI and have my dues auto-debited from my account.
    
    **Success criteria**: The customer should be able to understand the rationale for an auto-debit and move forward in the journey.
    
    **Requirement**: Below are the requirements for this page.
    
    - Once the customer has chosen to setup a mandate using UPI, the customer can see specific options. This page is rendered when Digio SDK is invoked.
    - Digio checks the device type from which the SDK is being invoked
    - The customer should see the below options on a mobile.
        - Intent flow
        - Collect flow
    - The customer should see the below options on a desktop.
        - QR flow
        - Collect flow
    - The customer enters their VPA for collect flow OR
    - The customer scans the QR from a TPAP (PhonePe, GPay, etc) OR
    - The customer clicks on the intent link and is redirected to a TPAP (PhonePe, GPay, etc).
    - The customer completes the authorization using MPIN on the TPAP.
    - 1 INR is debited from the customer’s bank account.
    - Digio redirects the customer to DSP, which redirects the customer to Volt UI with the terminal status.
- **U5**: As a customer, I want to know what to do if the status of UPI mandate registration has failed.
- **U6**: As a customer, I want to move forward if my UPI mandate has been registered successfully.
- **U7**: As a customer, I want to know what to do if the status of UPI mandate registration isn’t updated.
- **U8**: As a customer, I should be able to exit UPI mandate and setup a mandate with NACH due to any issues.