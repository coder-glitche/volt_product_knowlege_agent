# Repayment flow for DSP

: Vaibhav Arora
Created time: November 7, 2024 8:13 AM
Status: Pending Review
Last edited: November 11, 2024 8:01 PM

# **What problem are we solving?**

We offer three payment methods for a user to be able to make a repayment towards their loan via Razorpay:

- UPI
- Debits cards (Rupay)
- Net banking

For net banking, Razorpay assists us with partnering with different banks so that they can offer net banking as a service with our sponsor bank (Yes bank). Currently we are only utilising Razorpay integration as an LSP (via Volt) and do not have a repayment flow on the DSP website. 

To enable large banks like SBI, HDFC, ICICI, IDFC bank, we need to have a repayment flow on the DSP website to meet compliance requirements.

---

# **How do we measure success?**

- Get primary banks to offer net banking via our payment gateway service to users

---

# **How are others solving this problem?**

- BFL and TCL allows users to log in on their website where it shows all products taken by the user at a client level (even with LSPs like Volt/Stable money) and lets users make repayments towards the products
- Few lenders like BOB have product specific pages to allow users to make repayments where they have to add their loan account details/credit card number, post which an OTP is triggered to their registered mobile / email address

![Screenshot 2024-11-07 at 8.24.20 AM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_8.24.20_AM.png)

![Screenshot 2024-11-07 at 8.25.29 AM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_8.25.29_AM.png)

![Screenshot 2024-11-07 at 8.25.45 AM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_8.25.45_AM.png)

![Screenshot 2024-11-07 at 8.28.08 AM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_8.28.08_AM.png)

![Screenshot 2024-11-07 at 8.28.52 AM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_8.28.52_AM.png)

![Screenshot 2024-11-07 at 8.29.02 AM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_8.29.02_AM.png)

![Screenshot 2024-11-07 at 8.29.14 AM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_8.29.14_AM.png)

---

# **What is the solution?**

We will build an intermediate repayment flow for users to be able to make a repayment on their loan account on the DSP landing page (to showcase to Banking partners) 

## User stories / User flow

**High level flow:**

![image.png](Repayment%20flow%20for%20DSP/image.png)

## Requirements:

We will be building the repayment flow via the [DSP Finance landing page](https://dspfin.com/)

- Once the user lands on the DSP finance landing page, user will be able to select an option to repay their existing loan (in the footer)
- Once they click on the option, they will be redirected to a new page, where the user will be able to enter their loan account number and registered mobile number (with the loan address)
- If the mobile number and email address is valid, user will be taken to the loan repayment page otherwise they will be shown a validation error
    - Error message: Invalid details, please enter the correct details and try again
- On success user will be able to see the name associated with the account as well as the total oustanding amount
- User will not be able to place a repayment more than their total outstanding amount.
    - Error message: Please enter an amount equal or lower than the total outstanding amount
- Upon entering the amount, we will invoke the payment link for the user, basis the repayment made by the user their are three scenarios:
    - User cancels the payment:
        - Transaction cancelled, please try again
    - User completes the payment
        - Transaction successful, it will be posted in your loan account within 1 working day
        (We need a transaction success screen) 
        should show following details:
        Transaction amount 
        Payout ID (user should be able to copy it)
        Transaction date time 
        Should have CTA (go back) - will take them back to the DSP landing page)
    - Transaction fails for the user
    - Transaction failed, please try again. If any amount was debited from your account, it will be refunded back within 2-3 business days.
- After the transaction is successful, user will be shown the status of the transaction

**Wireframes:**

![Screenshot 2024-11-07 at 3.03.40 PM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_3.03.40_PM.png)

![Screenshot 2024-11-07 at 3.03.47 PM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_3.03.47_PM.png)

![Screenshot 2024-11-07 at 3.03.51 PM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_3.03.51_PM.png)

![Screenshot 2024-11-07 at 3.03.56 PM.png](Repayment%20flow%20for%20DSP/Screenshot_2024-11-07_at_3.03.56_PM.png)

---

# **Design**

[https://www.figma.com/design/woUrOqqLZscVNYcxjBHzG0/DSP-Finance-brand?node-id=322-2294&node-type=canvas&t=fUQ6S8NESqUvTY1J-0](https://www.figma.com/design/woUrOqqLZscVNYcxjBHzG0/DSP-Finance-brand?node-id=322-2294&node-type=canvas&t=fUQ6S8NESqUvTY1J-0)

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