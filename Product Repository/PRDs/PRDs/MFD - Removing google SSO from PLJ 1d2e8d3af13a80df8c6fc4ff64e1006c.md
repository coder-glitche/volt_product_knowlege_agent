# MFD - Removing google SSO from PLJ

: Naman Agarwal
Created time: April 11, 2025 6:08 PM
Status: Ready for Tech
Last edited: April 22, 2025 10:53 AM

Problem statement

1. The **Email field is not Pre-filled** even when the MFD has already fetched the MFC for the client.
2. **Email verification via Google SSO** doesn’t work well for the MFD channel—Google pulls the MFD's email from the device instead of the client’s.
    
    ![Screenshot 2025-04-11 at 1.31.35 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.35_PM.png)
    

- MFDs often manually enter their email in the **“Continue with other email”** option, leading to operational effort to remove the Email.

![Screenshot 2025-04-11 at 1.31.44 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.44_PM.png)

## **Proposed Solution:**

**After customer registration (Name + Mobile Number + OTP):**

1. The MFD lands on the **Customer Registered** screen.
2. The screen gives two options:
    - Learn how to **create an application** on the Partner Portal, or
    - **Share a link** with the customer.
3. If the MFD chooses **“Continue creating customer application”**:
    - The flow will continue to the next application journey step skipping the App homepage as the intended action at this step is to complete the application.
    - The Data like Email ID and Fetched portfolio will be Pre-filled if the MFC has been previously fetched for the customer
    - If the MFD needs to access the App home page then they can go back on the application process using the top ← arrow on the top left.
    

Text changes on the verify Email step 
” The provided email will be used by lenders as the Client’s registered Email for all communications “

### Key Changes from the Current Flow

1. **Skip the email selector page** — go directly to the “Add Email” screen.
2. **Show the client’s name** clearly to ensure the email being entered is for the right person.
3. **Include a note** saying the email will be used by lenders for important updates.
4. **Update the header** to: “Add client’s email.”
5. **Streamline the journey** by removing extra steps and taking MFDs directly to the email input screen.