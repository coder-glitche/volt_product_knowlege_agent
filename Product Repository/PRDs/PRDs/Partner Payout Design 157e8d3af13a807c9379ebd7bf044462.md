# Partner Payout Design

: Naman Agarwal
Created time: December 9, 2024 3:08 PM
Status: In progress
Last edited: December 23, 2024 3:44 PM

We need to update the design of the our Payout comms 

1. Payout Bank account and email collection mail , 
2. Payout commission statement for the month mail 
3. Payout GST invoice mail 
4. Commission statement invoice 
5. GST invoice

Redesign needs to 

- Align with volt design language
- Have clear Information Hierarchy

- Payout Bank account and GSTn collection mail
    1. 
    
    ### Email Subject
    
    **Optional Update: Bank Account & GST Details - Volt Money Partner**
    
    ---
    
    ### Email Body
    
    **Dear {{name}},**
    
    We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed.
    
    **Why Update?**
    
    Keeping your information accurate helps:
    
    - Process payouts smoothly
    - Ensure compliance with GST guidelines (if applicable)
    
    **How to Update:**
    
    1. Log in to your **Partner Dashboard** [Insert Dashboard Link].
    2. Navigate to the **Account Details** section.
    3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary.
    
    If your details are already accurate, you don’t need to do anything further.
    
    For your convenience, we’ve included a step-by-step guide with screenshots to assist you.
    
    **Need Assistance?**
    
    Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support.
    
    We appreciate your continued partnership with Volt Money.
    
    Warm regards,
    
    The Volt Money Team
    
- Payout commission statement for the month mail
    
    ---
    
    ### Monthly Payout Statement Template (For Partners With GSTN)
    
    **Subject:** Payout Statement for {{month}} - {{name}}
    
    **Body:**
    
    Dear {{name}},
    
    We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}:
    
    - **Total Income:** Rs. {{total_income}}
    - **TDS Deducted:** Rs. {{tds_amount}}
    - **Net Payout:** Rs. {{net_payout}}
    
    Your payout has been processed and credited to the following account:
    
    **Account Number:** ****{{number}}
    
    Additionally, the GST receipt for this transaction has been sent separately to your registered email address.
    
    You can view a detailed earnings breakdown in the **Earnings** section of your dashboard.
    
    For any assistance, feel free to contact us at **+91 96117 49295**.
    
    Thank you for partnering with Volt Money.
    
    Warm regards,
    
    The Volt Money Team
    
    ---
    
    ### Monthly Payout Statement Template (For Partners Without GSTN)
    
    **Subject:** Payout Statement for {{month}} - {{name}}
    
    **Body:**
    
    Dear {{name}},
    
    We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}:
    
    - **Total Income:** Rs. {{total_income}}
    - **TDS Deducted:** Rs. {{tds_amount}}
    - **Net Payout:** Rs. {{net_payout}}
    
    Your payout has been processed and credited to the following account:
    
    **Account Number:** ****{{number}}
    
    You can view a detailed earnings breakdown in the **Earnings** section of your dashboard.
    
    For any assistance, feel free to contact us at **+91 96117 49295**.
    
    Thank you for partnering with Volt Money.
    
    Warm regards,
    
    The Volt Money Team
    
    ---
    
    ### Key Notes:
    
    1. **Variables for Dynamic Content**
        - {{name}}, {{month}}, {{total_income}}, {{tds_amount}}, {{net_payout}}, {{number}}
    2. **GST Receipt Information**
        - Include this line only for partners with GSTN:
        “Additionally, the GST receipt for this transaction has been sent separately to your registered email address.”
    3. **Formatting Guidelines**
        - Ensure all monetary values use proper formatting with thousand separators (e.g., Rs. 1,00,000).
        - Display month in its full format (e.g., "December 2024").
    4. **WhatsApp Integration (Optional)**
        - Use template names aligned with the email type (e.g., `payout_gst_tds_v3_final3`).
        - Suggested CTAs:
            - “View Dashboard”
            - “Request Callback”
    
    **Action step:** Ensure the email templates are updated in your communication platform, and test both versions to confirm all variables populate correctly.
    
    ```jsx
    
    ---
    
    ### Monthly Payout Statement Template (For Partners With GSTN)
    
    **Subject:** Payout Statement for {{month}} - {{name}}
    
    **Body:**
    
    Dear {{name}},
    
    We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}:
    
    - **Total Income:** Rs. {{total_income}}  
    - **TDS Deducted:** Rs. {{tds_amount}}  
    - **Net Payout:** Rs. {{net_payout}}  
    
    Your payout has been processed and credited to the following account:  
    **Account Number:** ****{{number}}
    
    Additionally, the GST receipt for this transaction has been sent separately to your registered email address.
    
    You can view a detailed earnings breakdown in the **Earnings** section of your dashboard.  
    
    For any assistance, feel free to contact us at **+91 96117 49295**.  
    
    Thank you for partnering with Volt Money.  
    
    Warm regards,  
    The Volt Money Team  
    
    ---
    
    ### Monthly Payout Statement Template (For Partners Without GSTN)
    
    **Subject:** Payout Statement for {{month}} - {{name}}
    
    **Body:**
    
    Dear {{name}},
    
    We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}:
    
    - **Total Income:** Rs. {{total_income}}  
    - **TDS Deducted:** Rs. {{tds_amount}}  
    - **Net Payout:** Rs. {{net_payout}}  
    
    Your payout has been processed and credited to the following account:  
    **Account Number:** ****{{number}}
    
    You can view a detailed earnings breakdown in the **Earnings** section of your dashboard.  
    
    For any assistance, feel free to contact us at **+91 96117 49295**.  
    
    Thank you for partnering with Volt Money.  
    
    Warm regards,  
    The Volt Money Team  
    
    ---
    
    ### Key Notes:
    1. **Variables for Dynamic Content**  
       - {{name}}, {{month}}, {{total_income}}, {{tds_amount}}, {{net_payout}}, {{number}}  
    
    2. **GST Receipt Information**  
       - Include this line only for partners with GSTN:  
         “Additionally, the GST receipt for this transaction has been sent separately to your registered email address.”  
    
    3. **Formatting Guidelines**  
       - Ensure all monetary values use proper formatting with thousand separators (e.g., Rs. 1,00,000).  
       - Display month in its full format (e.g., "December 2024").  
    
    4. **WhatsApp Integration (Optional)**  
       - Use template names aligned with the email type (e.g., `payout_gst_tds_v3_final3`).  
       - Suggested CTAs:  
         - “View Dashboard”  
         - “Request Callback”  
    
    **Action step:** Ensure the email templates are updated in your communication platform, and test both versions to confirm all variables populate correctly.
    ```
    

1. Payout GST invoice mail 
2. Commission statement invoice 
    1. Monthly invoice of commission 
    2. 
3. GST invoice