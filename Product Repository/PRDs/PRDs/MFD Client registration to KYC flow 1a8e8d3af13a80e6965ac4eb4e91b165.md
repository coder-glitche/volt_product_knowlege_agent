# MFD Client registration to KYC flow

: Naman Agarwal
Created time: February 28, 2025 12:28 PM
Status: In progress
Last edited: May 28, 2025 12:45 PM

### **Overview**

The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves:

1. **Registering the customer**
2. **Fetching details of their mutual funds**
3. **Calculating the credit limit**
4. **Presenting a loan offer**

The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates.

## **Objective**

- **Increase conversion** from registration to application creation.
- **Optimise the top-of-funnel (TOFU) experience** before the KYC stage.

## **Current vs. Proposed Journey**

| **Current Journey** | **Proposed Journey** |
| --- | --- |
| Add phone number | Add phone number |
| OTP | Add PAN number |
| Email | MFC summary fetch OTP |
| Email SSO or OTP | Offer page |
| PAN |  |
| DOB |  |
| Verify PAN |  |
| Fetch |  |
| OTP |  |
| Unlock limit |  |
| Set limit |  |
| Offer page |  |

## **Issues in the Current Process**

## Client Registration issues

1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. 

![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png)

1. The Email is not Pre-Filled if the MFD has MFC fetched for the client
2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email.
3. We want to remove the Page of email selector and move to the add email screen 
    1. Text “Add client email ID”
4. MFD add their own email in the E-Mail step as it is not explicitly called out.
5. MFDs have to fetch the Limit again after fetching in the Check limit section.

## Offer page issues

1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption.
2. **Customer misconception** that the limit shown is deducted from their mutual funds.
3. **Fear of entire limit being disbursed** instead of flexible withdrawals.
4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien.
5. **Limited understanding of Credit Line or Overdraft (OD) accounts.**
6. **Confusion about interest rates**—reducing vs. flat rate.
7. **Processing fees (PF) issues** for smaller ticket loans.
8. **Unfavourable tenure**—customers may not want a fixed 3-year loan.

## **Proposed Solutions**

1. **Decouple credit limit from mutual fund visibility**
    - Customers assume funds will be sold to get a limit.
    - Background processing will improve conversion and reduce customer concerns/inbound calls.
2. **Focus on what customers care about—credit limit**
    - If the limit is attractive and meets their needs, they are more likely to proceed.

### **User Insights & Concerns**

### **Customer 1**

- Felt the app looked amateurish and untrustworthy.
- Found the service good but needed more clarity on the loan process.

### **Customer 2 (Ashish)**

- Discovered Volt through blogs and articles.
- Had no major issues but wanted to understand **payment terms & schedule**.

### **Customer 3**

- Had concerns about:
    - **Loan disbursement process**
    - **Unpledging charges**
    - **Fixed 3-year tenure**
    - **Processing fee (₹1,499)—one-time or per withdrawal?**

## **Next Steps**

- Improve UI/UX to enhance trust and credibility.
- Communicate loan disbursement flexibility and repayment options clearly.
- Address key customer concerns proactively in FAQs and onboarding flow

---

##