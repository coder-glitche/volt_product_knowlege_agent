# [B2B2C] GST payouts and reconciliation optimisation

: Ameya Aglawe
Created time: November 13, 2025 8:18 PM
Status: In progress
Last edited: March 19, 2026 5:03 PM

# **What problem are we solving?**

---

- Currently processing of payouts is handled manually by the business and finance team end to end, this takes up a lot of bandwidth as the payouts involve multiple back & forth for approvals till the final payment processing takes place.
- Processing GST payouts takes more than 60% of overall payout processing of the business team, as it involves manually reconciling invoices of more than 600 partners monthly, reconciling the status of the GST payout and co-ordinating with marketing team to ensure timely communications

# **How do we measure success?**

---

- Man-hours spent on entire GST lifecycle workflow goes down to 2 hours monthly
- Number of partners who claim GST goes up from 600 to 2000 within 2 months of feature launch
- Errors in reconciliation go down to zero

# **How are others solving this problem?**

---

- Asset plus
    
    ![Screenshot 2025-11-24 at 2.49.15 PM.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/Screenshot_2025-11-24_at_2.49.15_PM.png)
    

![Screenshot 2025-11-24 at 2.49.47 PM.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/Screenshot_2025-11-24_at_2.49.47_PM.png)

![Screenshot 2025-11-24 at 2.50.27 PM.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/Screenshot_2025-11-24_at_2.50.27_PM.png)

# **What is the solution?**

---

### Overview

---

- **Following is the existing end to end monthly Net payouts & GST payouts lifecycle -**
    - Tech team prepares partner level payout sheet
    - Payout sheet goes for approval to business team
    - Business team approves and share the sheet with analytics team
    - Analytics team generates a master sheet with
        - Payout details sheet (business team)
            - Base payout amount
            - TDS amount
            - GST amount
        - Base payout communications sheet (business/marketing team)
        - GST payout communications sheet  (business/marketing team)
        - Payments bulk upload sheet (finance team)
        - Finance team processes the bulk payouts and shares HSBC file with business team for recon
        - Based on the recon file business/marketing team initiate base payout communications to the partners
        - Within next 5 days GST invoices from the partners are collected via google forms and Finance team processes the GST payout & shares HSBC file with business team for recon
        - Based on the recon file business/marketing team initiate GST payout communications to the partners

- **Following is the new flow -**
    - Partner comes to the dashboard and visits the earning section
    - They find 2 tabs in the earning sections
        - Payout details (customer can check monthly net payout details)
            - Payout details tab view
                
                
                | Month | Gross payout | TDS (i) | Net Payout (i) | Status | UTR |
                | --- | --- | --- | --- | --- | --- |
                | January 2025 |  |  |  | Payment settled |  |
                | February 2025 |  |  |  |  |  |
                | March 2025 |  |  |  |  |  |
                | April 2025 |  |  |  |  |  |
                | May 2025 |  |  |  |  |  |
                | June 2025 |  |  |  |  |  |
        - GST details (customer can check monthly GST payout details)
            - GST details tab view
                
                
                | Month | Gross payout  | GST payout (i) | Status | UTR | Actions |
                | --- | --- | --- | --- | --- | --- |
                | January 2025 |  |  |  |  |  |
                | February 2025 |  |  |  |  |  |
                | March 2025 |  |  |  |  |  |
                | April 2025 |  |  |  |  |  |
                | May 2025 |  |  |  |  |  |
                | June 2025 |  |  |  |  |  |
            - GST payout status
                - Expired (i)
                - Invoice pending (i)
                - Payout processing (i)
                - Settled (i)
            - GST actions
                - Enter invoice details
                    - Partner enters details required for invoice generation
                        - GSTIN number
                            - Pre-filling
                                - GSTIN number would be pre-filled if the system already has GSTIN mapped with the partner
                            - Regex checks
                                - We will implement regex validation here to ensure entered GSTIN number is not entirely incorrect (will have to implement here as well as in the entry point i.e account details)
                                - List of regex checks
                                    - GSTIN number must be of 15 characters
                                    - First 2 characters must be of digits (this is the [state code](https://tallysolutions.com/gst/gst-state-code-list/))
                                    - 3th, 4th, 5th, 6th, 7th characters must be letters
                                    - 8th, 9th, 10th, 11th characters must be numbers
                                    - 12th character must be a letter
                                    - 14th character must be letter Z
                                - If the value inputted by the user fails any of the regex checks we throw an error and ask the user to enter a valid GSTIN number
                        - Invoice number
                        - Company name
                            - Pre-filled if present in the system
                - Review invoice preforma
                    - PFA the Invoice preforma format
                        - If same state then CGST and SGST - [Format](https://docs.google.com/document/d/1wiV9AvAKjgnSDKBIv-u_nM5PJIOd97Gz8R1ch7S7kF8/edit?tab=t.0)
                        - If different state then IGST - [Format](https://docs.google.com/document/d/1rSnW12PKODipgD8BfNikxwcpMSVCD0iy8AXNG2kWE8A/edit?tab=t.0)
                        - Note - State identification of the partner will happen based on the first two characters of the GSTIN number. Refer to the master here.
                - Sign invoice via OTP exchange
                - Download invoice (once the invoice is signed)
                    - PFA the Invoice format
                        - If same state then CGST and SGST - [Format](https://docs.google.com/document/d/1mG5ZlJiVcmc5BpvvJWgHJJMz0q41a_kaTRJ302-X9UA/edit?tab=t.0)
                        - If different state then IGST - [Format](https://docs.google.com/document/d/1yZJ2TumnD2K4cgggqOU2cmH-rkDzM5thapf9aaxNfP4/edit?tab=t.0)
                        - Note - State identification of the partner will happen based on the first two characters of the GSTIN number. Refer to the master here.
    - Communications
        - Payout settled successfully
            - Whatsapp
                - Template ID
                    - volt_partner_payout_success_19_march
                - Copy
                    
                    ```jsx
                    Dear {{name}}
                    
                    Volt Money partner payout for the month of {{billing_payout_month_year}} is settled.
                    
                    Net Payout = Rs {{net_payout}}
                    Bank account number: xxxx{{last4digits_bank_account}}
                    
                    Visit Earnings section in the dashboard to get a detailed breakup and *sign GST invoice for this billing month before the end of the ongoing month.*
                    ```
                    
                - Variables
                    - {{partner_name}}
                    - {{billing_payout_month_year}}
                    - {{net_payout}}
                    - {{last4digits_bank_account}}
                    - {{payout_utr}}
                - Screenshot
                    
                    
                    ![Screenshot 2026-03-19 at 4.26.17 PM.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/Screenshot_2026-03-19_at_4.26.17_PM.png)
                    
                    ![Screenshot 2026-03-19 at 4.26.31 PM.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/Screenshot_2026-03-19_at_4.26.31_PM.png)
                    
            - SMS
                - Template ID
                    - 1107177391863829737
                - Copy
                    - Payout of Rs {#alphanumeric#} for {#alphanumeric#} settled in bank account xxxx{#numeric#}. Check Earnings & sign GST invoice before end of the month from Volt Partner dashboard.
        - GST invoice signed and submitted successfully
            - Email
                - Template ID
                    
                    ```jsx
                    d-7f89b021d73647be81cf1d885f244722
                    ```
                    
                - Copy
                    
                    ```jsx
                    <!DOCTYPE html>
                    
                    <head>
                    <meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
                    </head>
                    <html xmlns:th="http://www.thymeleaf.org" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
                    <head>
                    <!--[if gte mso 9]>
                        <xml>
                            <o:OfficeDocumentSettings>
                                <o:AllowPNG/>
                                <o:PixelsPerInch>96</o:PixelsPerInch>
                            </o:OfficeDocumentSettings>
                        </xml>
                        <![endif]-->
                    <title>Volt</title>
                    <meta name="viewport" content="initial-scale=1.0,width=device-width"/>
                    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
                    <meta name="ROBOTS" content="NOINDEX, NOFOLLOW"/>
                    <meta name="referrer" content="no-referrer"/>
                    <style type="text/css">
                    span.MsoHyperlink {
                        mso-style-priority: 99;
                        color: inherit;
                    }
                    span.MsoHyperlinkFollowed {
                        mso-style-priority: 99;
                        color: inherit;
                    }
                    a[href^=tel] {
                        color: inherit;
                        text-decoration: none;
                    }
                    a[x-apple-data-detectors] {
                        color: inherit !important;
                        text-decoration: none !important;
                        font-size: inherit !important;
                        font-family: inherit !important;
                        font-weight: inherit !important;
                        line-height: inherit !important;
                    }
                    #MessageViewBody a {
                        color: inherit;
                        text-decoration: none;
                        font-size: inherit;
                        font-family: inherit;
                        font-weight: inherit;
                        line-height: inherit;
                    }
                    #outlook a {
                        padding: 0;
                    }
                    body {
                        margin: 0 !important;
                        padding: 0 !important;
                        -webkit-text-size-adjust: 100% !important;
                        -ms-text-size-adjust: 100% !important;
                        -webkit-font-smoothing: antialiased !important;
                    }
                    img {
                        outline: none;
                        text-decoration: none;
                        -ms-interpolation-mode: bicubic;
                    }
                    a img {
                        border: none;
                    }
                    p {
                        margin: 1em 0;
                    }
                    table td {
                        border-collapse: collapse;
                    }
                    table th {
                        margin: 0 !important;
                        padding: 0 !important;
                        vertical-align: top;
                        font-weight: normal;
                    }
                    .ReadMsgBody {
                        width: 100%;
                    }
                    .ExternalClass {
                        width: 100%;
                    }
                    .ExternalClass * {
                        line-height: 100%;
                    }
                    #backgroundTable {
                        margin: 0;
                        padding: 0;
                        width: 100% !important;
                        line-height: 100% !important;
                    }
                    [owa] .foo {
                        background: none !important;
                    }
                    div, button {
                        margin: 0 !important;
                        padding: 0 !important;
                        display: block !important;
                    }
                    td a {
                        color: inherit;
                        text-decoration: underline;
                    }
                    
                    @media only screen and (min-device-width: 320px) and (max-device-width: 1024px) {
                    a[href^="tel"], a[href^="sms"], a {
                        color: inherit;
                        cursor: default;
                        text-decoration: none;
                    }
                    }
                    
                    @media only screen and (min-device-width: 768px) and (max-device-width: 1024px) {
                    body {
                        min-width: 100% !important;
                    }
                    }
                    
                    @media only screen and (max-width:480px), (max-device-width:480px) {
                    .h {
                        display: none !important;
                    }
                    .wFull {
                        width: 320px !important;
                        height: auto !important;
                        max-width: 100% !important;
                    }
                    .noBG {
                        background: none !important;
                    }
                    .mob-img {
                        width: 100% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-40 {
                        width: 40% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-25 {
                        width: 20% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-75 {
                        width: 75% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-85 {
                        width: 85% !important;
                        max-width: 100% !important;
                    }
                    .mob-logo {
                        width: 90% !important;
                    }
                    }
                    </style>
                    </head>
                    <img height="0" width="0" alt="" src="https://mcusercontent.com/4be6dced2f8f027c9d1b68acc/images/3fd93179-53a2-84dc-8349-f3e994749ed3.png"/>
                    <body topmargin="0" bottommargin="0" leftmargin="0" rightmargin="0" bgcolor="#ffffff" style="background-color:#f9f9f9;">
                    
                    <!-- End of DoubleClick Floodlight Tag: Please do not remove --> 
                    <!-- framework start -->
                    <table width="100%" cellpadding="0" cellspacing="0" align="center" border="0" style="table-layout: fixed; margin: 0 auto; max-width: 600px;" bgcolor="#ffffff">
                      <tbody>
                        <!--Header Starts-->
                        
                        <tr>
                          <td width="100%" align="center" valign="middle" style="background-color: #f9f9f9; padding: 20px 0 20px 0;"><table width="100%">
                              <tr>
                                <td align="left"><a href="https://voltmoney.in/" target="_blank"><img class="" align="center" alt=""
                                                                                                              src="https://volt-images.s3.ap-south-1.amazonaws.com/volt-website-header.png"
                                                                                                              width="80"
                                                                                                              style="padding-bottom: 0;display: inline !important;vertical-align: bottom;border: 0;height: auto;outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;"></a></td>
                                <!--<td width="300"><table width="100%" cellpadding="0" cellspacing="0">-->
                                <!--    <tr>-->
                                <!--      <td width="100%">&nbsp;</td>-->
                                <!--      <td width="100%" align="right" valign="middle" style="font-family: sans-serif;border-left: 2px solid #E4E7EC;border-top: 2px solid #E4E7EC;border-bottom: 2px solid #E4E7EC;background-color: #ffffff;font-size:12px;color: #667085;padding: 4px 10px 5px 10px;">Lending&nbsp;partner </td>-->
                                <!--      <td width="100%" align="right" style="font-family: sans-serif;border-left: 2px solid #E4E7EC;border-top: 2px solid #E4E7EC;border-bottom: 2px solid #E4E7EC;border-right: 2px solid #E4E7EC;background-color: #ffffff; padding: 4px 10px 5px 10px; "><a href="https://voltmoney.in/" style="font-family: sans-serif;text-decoration:none;color:blue;display:inline-block;width:auto;" target="_blank">-->
                                <!--        <img src= {{lenderLogoUrl}} alt="" width="98" style="vertical-align:middle;" border="0" /></a></td>-->
                                <!--    </tr>-->
                                <!--  </table></td>-->
                              </tr>
                            </table></td>
                        </tr>
                        <!--Header Ends--> 
                        <!--Body Starts-->
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 30px 20px 20px 20px;" valign="middle">Dear {{partnername}}, <br>
                            <br>
                             The GST invoice for the {{GST_payout_month_year}} month has been successfully signed. GST payout for the {{GST_payout_month_year}} month will be credited to your registered bank account within the next 30 days.<br><br>
                            
                            The GST invoice has been attached in the mail for your reference. <br><br>
                            For more details you can visit the GST payout details in the earnings section on the Volt Money partner dashboard.
                            </td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:14px; color:#000000; line-heighthttps://mc.sendgrid.com/dynamic-templates:1.5;padding: 10px 20px 20px 20px;" valign="middle"><div align="center" style="padding-top:15px;"><a href="https://voltmoney.in/partner/customer?activeIndexTab=shortfall"
                                                                                 style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#1434cb;border-radius:40px;width:auto;width:auto;border-top:1px solid #1434cb;border-right:1px solid #1434cb;border-bottom:1px solid #1434cb;border-left:1px solid #1434cb;font-family:'Open Sans',Helvetica,Arial,sans-serif;text-align:center;word-break:keep-all"
                                                                                 target="_blank"><span style="padding:10px 80px;font-size:16px;display:inline-block;"> <span
                                        style="font-size:16px;line-height:2"><strong>Check GST payout details</strong> </span> </span></a> </div></td>
                        </tr>
                        <tr>
                        
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 30px 20px 20px 20px;" valign="middle">
                            
                           
                           For any query, feedback or support, call us or whatsapp us at {{contactnumber}}.
                           
                            </td>
                        </tr>
                        
                          <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 20px 20px 20px 20px" valign="middle">Regards,<br>
                            Team Volt Money </td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:14px; color:#000000; line-height:1.5;padding: 10px 20px 0px 20px" valign="middle"><table>
                              <tr>
                                <td width="500" style="border-top: solid 1px #e4e4e4;">&nbsp;</td>
                              </tr>
                            </table></td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:16px; color: grey; line-height:1.5;padding: 10px 20px 5px 20px" valign="middle"><b>For any query or feedback</b></td>
                        </tr>
                        <tr>
                          <td align="center"><table width="100%" class="wFull">
                              <tr>
                                <td align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="mailto:{{supportEmail}}"
                                                                                                                                     style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;padding:10px 20px 8px;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                     target="_blank"><img alt="" height="40"
                                                                                                                                                          src="https://res.cloudinary.com/mailmodo/image/upload/v1681577521/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/65dba85f62b5150a8501ad105faa0fb0_xgkvyz.png"
                                                                                                                                                          style="vertical-align:middle;padding:0px 15px 0px 0; color: blue;"/>{{supportEmail}}</a></td>
                                <td align="center" style="text-align:center;width:auto; padding-left: 5px;" valign="top"><a href="https://wa.me/{{contactnumber}}"
                                                                                                                                    style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;padding:10px 20px 8px;color:blue;display:inline-block;border-radius:4px;width:auto;"
                                                                                                                                    target="_blank"><img alt="" height="40"
                                                                                                                                                         src="https://res.cloudinary.com/mailmodo/image/upload/v1681577540/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/b57baeef65dd7087c9563a38fe9a3ef2_yt9mbf.png"
                                                                                                                                                         style="vertical-align:middle;padding:0px 15px 0px 0"/>{{contactnumber}}</a></td>
                              </tr>
                            </table>
                            <br></td>
                        </tr>
                        <!--Body Ends till CTA--> 
                        <!--Footer Starts-->
                        <tr>
                          <td width="100%" align="center" valign="middle" style="background-color: #f9f9f9; padding: 10px 0 10px 0;">&nbsp;</td>
                        </tr>
                        <tr>
                          <td align="center" style="background-color: #f9f9f9;"><table width="100%" class="wFull">
                              <tr>
                                <td width="200">&nbsp;</td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="https://www.instagram.com/voltmoney_in/"
                                                                                                                                                style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                                target="_blank"><img alt="" height="40"
                                                                                                                                                                     src="https://res.cloudinary.com/mailmodo/image/upload/v1681577581/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/58b3f5b46d62f088c43d38fba50d1f6f_tahbl6.png"
                                                                                                                                                                     style="vertical-align:middle;padding:0px 0px 0px 0; color: blue;"/></a></td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="https://www.linkedin.com/company/voltmoney/"
                                                                                                                                                style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                                target="_blank"><img alt="" height="40"
                                                                                                                                                                     src="https://res.cloudinary.com/mailmodo/image/upload/v1681577562/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/7b08e28696aa5485e0bcead19d23e8c6_jgxqwh.png"
                                                                                                                                                                     style="vertical-align:middle;padding:0px 0px 0px 0; color: blue;"/></a></td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="https://twitter.com/voltmoney_in"
                                                                                                                                                style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                                target="_blank"><img alt="" height="40"
                                                                                                                                                                     src="https://res.cloudinary.com/mailmodo/image/upload/v1681577571/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/0e1bd2da691ad4e8ed716827f8c9ed8f_kg4yrk.png"
                                                                                                                                                                     style="vertical-align:middle;padding:0px 0px 0px 0; color: blue;"/></a></td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-left: 5px;" valign="top"><a href="https://www.youtube.com/@voltmoney"
                                                                                                                                               style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto;"
                                                                                                                                               target="_blank"><img alt="" height="40"
                                                                                                                                                                    src="https://res.cloudinary.com/mailmodo/image/upload/v1681577531/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/853ce334a5fa846493dc6668f4731010_hsuko6.png"
                                                                                                                                                                    style="vertical-align:middle;padding:0px 0px 0px 0"/></a></td>
                                <td width="200">&nbsp;</td>
                              </tr>
                            </table></td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:12px; color:#000000; line-height:1.5;padding: 20px 30px 30px 30px; background-color: #f9f9f9;" valign="middle"><br>
                            <center>
                              <span style="color: grey;"> Ground Floor, EBC Space 3 166, 19th Main Rd, Sector 4, HSR Layout Bengaluru, Karnataka 560102</span><br>
                              <br>
                              <a href="https://voltmoney.in/privacy/" style="color: grey;">Privacy</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="https://voltmoney.in/about" style="color: grey;">About Us</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="https://voltmoney.in/" style="color: grey;">Visit website</a>
                            </center></td>
                        </tr>
                        <!--Footer Ends-->
                        
                      </tbody>
                    </table>
                    <!-- framework end --><!--android gmail zoom fix--> 
                    <!--/android gmail zoom fix--><!-- android yahoo fix-->
                    <table class="h" cellSpacing="0" cellPadding="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td align="center" style="FONT-SIZE: 1px; LINE-HEIGHT: 1px" height="1"><unsubscribe><!--[if !mso 9]><!--><img
                                        style="DISPLAY: block;" border="0" src="https://mcusercontent.com/4be6dced2f8f027c9d1b68acc/images/3fd93179-53a2-84dc-8349-f3e994749ed3.png" width="600"
                                        height="1"><!--<![endif]--></unsubscribe></td>
                        </tr>
                      </tbody>
                    </table>
                    <!--/android yahoo fix-->
                    </body>
                    </html>
                    ```
                    
                - Variables
                    
                    ```jsx
                    {
                    	"partnername": "Shivansh",
                    	"GST_payout_month_year" : "October-2025",
                    	"supportEmail": "support@voltmoney.in",
                    	"contactnumber": "+919611749097", 
                    	"date" : "23-Nov-2025"
                    }
                    ```
                    
                - Screenshot
                    
                    ![image.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/image.png)
                    
                - GST invoice should be attached
            - Whatsapp
                - Template ID
                    
                    ```jsx
                    gst_invoice_signed_successfully
                    ```
                    
                - Copy
                    
                    ```jsx
                    Hi {{partner_name}}
                    
                    Your GST invoice for {{GST_payout_month_year}} has been successfully submitted and shared to you over your registered email ID.
                    
                    GST payout for {{GST_payout_month_year}} will be settled in your registered bank account within the next 30 days. 
                    
                    For any queries, feel free to reach out.
                    ```
                    
                - Variables
                    - {{partner_name}}
                    - {{GST_payout_month_year}}
                - Screenshot
                    
                    ![Screenshot 2025-11-24 at 3.49.42 PM.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/Screenshot_2025-11-24_at_3.49.42_PM.png)
                    
        - GST payout settled successfully
            - Email
                - Template ID
                    
                    ```jsx
                    d-15cb8e5ab71a435c8a7de01028a7f36e
                    ```
                    
                - Copy
                    
                    ```jsx
                    <!DOCTYPE html>
                    
                    <head>
                    <meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
                    </head>
                    <html xmlns:th="http://www.thymeleaf.org" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
                    <head>
                    <!--[if gte mso 9]>
                        <xml>
                            <o:OfficeDocumentSettings>
                                <o:AllowPNG/>
                                <o:PixelsPerInch>96</o:PixelsPerInch>
                            </o:OfficeDocumentSettings>
                        </xml>
                        <![endif]-->
                    <title>Volt</title>
                    <meta name="viewport" content="initial-scale=1.0,width=device-width"/>
                    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
                    <meta name="ROBOTS" content="NOINDEX, NOFOLLOW"/>
                    <meta name="referrer" content="no-referrer"/>
                    <style type="text/css">
                    span.MsoHyperlink {
                        mso-style-priority: 99;
                        color: inherit;
                    }
                    span.MsoHyperlinkFollowed {
                        mso-style-priority: 99;
                        color: inherit;
                    }
                    a[href^=tel] {
                        color: inherit;
                        text-decoration: none;
                    }
                    a[x-apple-data-detectors] {
                        color: inherit !important;
                        text-decoration: none !important;
                        font-size: inherit !important;
                        font-family: inherit !important;
                        font-weight: inherit !important;
                        line-height: inherit !important;
                    }
                    #MessageViewBody a {
                        color: inherit;
                        text-decoration: none;
                        font-size: inherit;
                        font-family: inherit;
                        font-weight: inherit;
                        line-height: inherit;
                    }
                    #outlook a {
                        padding: 0;
                    }
                    body {
                        margin: 0 !important;
                        padding: 0 !important;
                        -webkit-text-size-adjust: 100% !important;
                        -ms-text-size-adjust: 100% !important;
                        -webkit-font-smoothing: antialiased !important;
                    }
                    img {
                        outline: none;
                        text-decoration: none;
                        -ms-interpolation-mode: bicubic;
                    }
                    a img {
                        border: none;
                    }
                    p {
                        margin: 1em 0;
                    }
                    table td {
                        border-collapse: collapse;
                    }
                    table th {
                        margin: 0 !important;
                        padding: 0 !important;
                        vertical-align: top;
                        font-weight: normal;
                    }
                    .ReadMsgBody {
                        width: 100%;
                    }
                    .ExternalClass {
                        width: 100%;
                    }
                    .ExternalClass * {
                        line-height: 100%;
                    }
                    #backgroundTable {
                        margin: 0;
                        padding: 0;
                        width: 100% !important;
                        line-height: 100% !important;
                    }
                    [owa] .foo {
                        background: none !important;
                    }
                    div, button {
                        margin: 0 !important;
                        padding: 0 !important;
                        display: block !important;
                    }
                    td a {
                        color: inherit;
                        text-decoration: underline;
                    }
                    
                    @media only screen and (min-device-width: 320px) and (max-device-width: 1024px) {
                    a[href^="tel"], a[href^="sms"], a {
                        color: inherit;
                        cursor: default;
                        text-decoration: none;
                    }
                    }
                    
                    @media only screen and (min-device-width: 768px) and (max-device-width: 1024px) {
                    body {
                        min-width: 100% !important;
                    }
                    }
                    
                    @media only screen and (max-width:480px), (max-device-width:480px) {
                    .h {
                        display: none !important;
                    }
                    .wFull {
                        width: 320px !important;
                        height: auto !important;
                        max-width: 100% !important;
                    }
                    .noBG {
                        background: none !important;
                    }
                    .mob-img {
                        width: 100% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-40 {
                        width: 40% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-25 {
                        width: 20% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-75 {
                        width: 75% !important;
                        max-width: 100% !important;
                    }
                    .mob-img-85 {
                        width: 85% !important;
                        max-width: 100% !important;
                    }
                    .mob-logo {
                        width: 90% !important;
                    }
                    }
                    </style>
                    </head>
                    <img height="0" width="0" alt="" src="https://mcusercontent.com/4be6dced2f8f027c9d1b68acc/images/3fd93179-53a2-84dc-8349-f3e994749ed3.png"/>
                    <body topmargin="0" bottommargin="0" leftmargin="0" rightmargin="0" bgcolor="#ffffff" style="background-color:#f9f9f9;">
                    
                    <!-- End of DoubleClick Floodlight Tag: Please do not remove --> 
                    <!-- framework start -->
                    <table width="100%" cellpadding="0" cellspacing="0" align="center" border="0" style="table-layout: fixed; margin: 0 auto; max-width: 600px;" bgcolor="#ffffff">
                      <tbody>
                        <!--Header Starts-->
                        
                        <tr>
                          <td width="100%" align="center" valign="middle" style="background-color: #f9f9f9; padding: 20px 0 20px 0;"><table width="100%">
                              <tr>
                                <td align="left"><a href="https://voltmoney.in/" target="_blank"><img class="" align="center" alt=""
                                                                                                              src="https://volt-images.s3.ap-south-1.amazonaws.com/volt-website-header.png"
                                                                                                              width="80"
                                                                                                              style="padding-bottom: 0;display: inline !important;vertical-align: bottom;border: 0;height: auto;outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;"></a></td>
                                <!--<td width="300"><table width="100%" cellpadding="0" cellspacing="0">-->
                                <!--    <tr>-->
                                <!--      <td width="100%">&nbsp;</td>-->
                                <!--      <td width="100%" align="right" valign="middle" style="font-family: sans-serif;border-left: 2px solid #E4E7EC;border-top: 2px solid #E4E7EC;border-bottom: 2px solid #E4E7EC;background-color: #ffffff;font-size:12px;color: #667085;padding: 4px 10px 5px 10px;">Lending&nbsp;partner </td>-->
                                <!--      <td width="100%" align="right" style="font-family: sans-serif;border-left: 2px solid #E4E7EC;border-top: 2px solid #E4E7EC;border-bottom: 2px solid #E4E7EC;border-right: 2px solid #E4E7EC;background-color: #ffffff; padding: 4px 10px 5px 10px; "><a href="https://voltmoney.in/" style="font-family: sans-serif;text-decoration:none;color:blue;display:inline-block;width:auto;" target="_blank">-->
                                <!--        <img src= {{lenderLogoUrl}} alt="" width="98" style="vertical-align:middle;" border="0" /></a></td>-->
                                <!--    </tr>-->
                                <!--  </table></td>-->
                              </tr>
                            </table></td>
                        </tr>
                        <!--Header Ends--> 
                        <!--Body Starts-->
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 30px 20px 20px 20px;" valign="middle">Dear {{partnername}}, <br>
                            <br>
                             The GST payout for {{GST_payout_month_year}} has been successfully credited to your registered bank account.<br><br>
                            
                    <table style="border-collapse: collapse; margin-top: 10px;"> <tr> <td style="padding: 8px 12px; border: 1px solid #ddd;">GST Payout Amount</td> <td style="padding: 8px 12px; border: 1px solid #ddd;">₹{{GST_payout_amount}}</td> </tr> <tr> <td style="padding: 8px 12px; border: 1px solid #ddd;">Registered Bank Account</td> <td style="padding: 8px 12px; border: 1px solid #ddd;">{{bank_account_number}}</td> </tr> <tr> <td style="padding: 8px 12px; border: 1px solid #ddd;">IFSC Code</td> <td style="padding: 8px 12px; border: 1px solid #ddd;">{{ifsc_code}}</td> </tr> <tr> <td style="padding: 8px 12px; border: 1px solid #ddd;">UTR Number</td> <td style="padding: 8px 12px; border: 1px solid #ddd;">{{utr_number}}</td> </tr> </table><br>
                    
                            For more details you can visit the GST payout details in the earnings section on the Volt Money partner dashboard.
                            </td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:14px; color:#000000; line-heighthttps://mc.sendgrid.com/dynamic-templates:1.5;padding: 10px 20px 20px 20px;" valign="middle"><div align="center" style="padding-top:15px;"><a href="https://voltmoney.in/partner/customer?activeIndexTab=shortfall"
                                                                                 style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#1434cb;border-radius:40px;width:auto;width:auto;border-top:1px solid #1434cb;border-right:1px solid #1434cb;border-bottom:1px solid #1434cb;border-left:1px solid #1434cb;font-family:'Open Sans',Helvetica,Arial,sans-serif;text-align:center;word-break:keep-all"
                                                                                 target="_blank"><span style="padding:10px 80px;font-size:16px;display:inline-block;"> <span
                                        style="font-size:16px;line-height:2"><strong>Check GST payout details</strong> </span> </span></a> </div></td>
                        </tr>
                        <tr>
                        
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 30px 20px 20px 20px;" valign="middle">
                            
                           
                           For any query, feedback or support, call us or whatsapp us at {{contact_number}}.
                           
                            </td>
                        </tr>
                        
                          <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 20px 20px 20px 20px" valign="middle">Regards,<br>
                            Team {{brandname}} </td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:14px; color:#000000; line-height:1.5;padding: 10px 20px 0px 20px" valign="middle"><table>
                              <tr>
                                <td width="500" style="border-top: solid 1px #e4e4e4;">&nbsp;</td>
                              </tr>
                            </table></td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:16px; color: grey; line-height:1.5;padding: 10px 20px 5px 20px" valign="middle"><b>For any query or feedback</b></td>
                        </tr>
                        <tr>
                          <td align="center"><table width="100%" class="wFull">
                              <tr>
                                <td align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="mailto:{{supportEmail}}"
                                                                                                                                     style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;padding:10px 20px 8px;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                     target="_blank"><img alt="" height="40"
                                                                                                                                                          src="https://res.cloudinary.com/mailmodo/image/upload/v1681577521/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/65dba85f62b5150a8501ad105faa0fb0_xgkvyz.png"
                                                                                                                                                          style="vertical-align:middle;padding:0px 15px 0px 0; color: blue;"/>{{supportEmail}}</a></td>
                                <td align="center" style="text-align:center;width:auto; padding-left: 5px;" valign="top"><a href="https://wa.me/{{contactnumber}}"
                                                                                                                                    style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;padding:10px 20px 8px;color:blue;display:inline-block;border-radius:4px;width:auto;"
                                                                                                                                    target="_blank"><img alt="" height="40"
                                                                                                                                                         src="https://res.cloudinary.com/mailmodo/image/upload/v1681577540/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/b57baeef65dd7087c9563a38fe9a3ef2_yt9mbf.png"
                                                                                                                                                         style="vertical-align:middle;padding:0px 15px 0px 0"/>{{contactnumber}}</a></td>
                              </tr>
                            </table>
                            <br></td>
                        </tr>
                        <!--Body Ends till CTA--> 
                        <!--Footer Starts-->
                        <tr>
                          <td width="100%" align="center" valign="middle" style="background-color: #f9f9f9; padding: 10px 0 10px 0;">&nbsp;</td>
                        </tr>
                        <tr>
                          <td align="center" style="background-color: #f9f9f9;"><table width="100%" class="wFull">
                              <tr>
                                <td width="200">&nbsp;</td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="https://www.instagram.com/voltmoney_in/"
                                                                                                                                                style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                                target="_blank"><img alt="" height="40"
                                                                                                                                                                     src="https://res.cloudinary.com/mailmodo/image/upload/v1681577581/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/58b3f5b46d62f088c43d38fba50d1f6f_tahbl6.png"
                                                                                                                                                                     style="vertical-align:middle;padding:0px 0px 0px 0; color: blue;"/></a></td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="https://www.linkedin.com/company/voltmoney/"
                                                                                                                                                style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                                target="_blank"><img alt="" height="40"
                                                                                                                                                                     src="https://res.cloudinary.com/mailmodo/image/upload/v1681577562/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/7b08e28696aa5485e0bcead19d23e8c6_jgxqwh.png"
                                                                                                                                                                     style="vertical-align:middle;padding:0px 0px 0px 0; color: blue;"/></a></td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-right: 5px;" valign="top"><a href="https://twitter.com/voltmoney_in"
                                                                                                                                                style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto"
                                                                                                                                                target="_blank"><img alt="" height="40"
                                                                                                                                                                     src="https://res.cloudinary.com/mailmodo/image/upload/v1681577571/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/0e1bd2da691ad4e8ed716827f8c9ed8f_kg4yrk.png"
                                                                                                                                                                     style="vertical-align:middle;padding:0px 0px 0px 0; color: blue;"/></a></td>
                                <td width="40" align="center" style="text-align:center;width:auto; padding-left: 5px;" valign="top"><a href="https://www.youtube.com/@voltmoney"
                                                                                                                                               style="background:#FFFFFF;font-family: sans-serif;font-size:16px;line-height:19px;text-decoration:none;color:blue;display:inline-block;border-radius:4px;width:auto;"
                                                                                                                                               target="_blank"><img alt="" height="40"
                                                                                                                                                                    src="https://res.cloudinary.com/mailmodo/image/upload/v1681577531/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/853ce334a5fa846493dc6668f4731010_hsuko6.png"
                                                                                                                                                                    style="vertical-align:middle;padding:0px 0px 0px 0"/></a></td>
                                <td width="200">&nbsp;</td>
                              </tr>
                            </table></td>
                        </tr>
                        <tr>
                          <td align="left" style="font-family: sans-serif; font-size:12px; color:#000000; line-height:1.5;padding: 20px 30px 30px 30px; background-color: #f9f9f9;" valign="middle"><br>
                            <center>
                              <span style="color: grey;"> Ground Floor, EBC Space 3 166, 19th Main Rd, Sector 4, HSR Layout Bengaluru, Karnataka 560102</span><br>
                              <br>
                              <a href="https://voltmoney.in/privacy/" style="color: grey;">Privacy</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="https://voltmoney.in/about" style="color: grey;">About Us</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="https://voltmoney.in/" style="color: grey;">Visit website</a>
                            </center></td>
                        </tr>
                        <!--Footer Ends-->
                        
                      </tbody>
                    </table>
                    <!-- framework end --><!--android gmail zoom fix--> 
                    <!--/android gmail zoom fix--><!-- android yahoo fix-->
                    <table class="h" cellSpacing="0" cellPadding="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td align="center" style="FONT-SIZE: 1px; LINE-HEIGHT: 1px" height="1"><unsubscribe><!--[if !mso 9]><!--><img
                                        style="DISPLAY: block;" border="0" src="https://mcusercontent.com/4be6dced2f8f027c9d1b68acc/images/3fd93179-53a2-84dc-8349-f3e994749ed3.png" width="600"
                                        height="1"><!--<![endif]--></unsubscribe></td>
                        </tr>
                      </tbody>
                    </table>
                    <!--/android yahoo fix-->
                    </body>
                    </html>
                    ```
                    
                - Variables
                    
                    ```jsx
                    {
                        
                        "partnername" : "Shivansh",
                        "GST_payout_month_year" : "October",
                        "GST_payout_amount" :"40000",
                        "bank_account_number" :"1237958038",
                        "ifsc_code" :"HDFC1279420",
                        "utr_number" : "YESB57901248912",
                        "contact_number" : "+914801244532",
                        "supportEmail" : "shivansh.singh@voltmoney.in"
                    }
                    ```
                    
                - Screenshot
                    
                    ![image.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/image%201.png)
                    
            - Whatsapp
                - Template ID
                    
                    ```jsx
                    gst_payout_processed_successfully
                    ```
                    
                - Copy
                    
                    ```jsx
                    Hi {{partner_name}},
                    
                    GST payout for {{GST_payout_month_year}} has been successfully settled and credited.
                    
                    *GST Payout Details* - 
                    Amount : ₹{{GST_payout_amount}}
                    Bank Account : xxxx{{last4_digits_account_number}}
                    UTR Number : {{UTR}}
                    
                    For any support, feel free to reach out.
                    ```
                    
                - Variables
                    - {{partner_name}}
                    - {{GST_payout_month_year}}
                    - {{GST_payout_amount}}
                    - {{last4_digits_account_number}}
                    - {{UTR}}
                - Screenshot
                    
                    ![Screenshot 2025-11-24 at 3.48.40 PM.png](%5BB2B2C%5D%20GST%20payouts%20and%20reconciliation%20optimisatio/Screenshot_2025-11-24_at_3.48.40_PM.png)
                    
    - GST payout reconciliation
        - Finance/Business team will update the status of the GST payout using an admin action
        - Sheet will contain the following details Partner account ID, GST payout ID, UTR and GST status
    - User education (information icons)
        - TDS (2% TDS is applied once total gross payout exceeds ₹19,600 as per Volt internal policy)
        - GST (GST payout is calculated as 18% of gross payout)
        - Status in GST details
            - Claim expired (payout claims of only current financial year can be processed)
            - Invoice pending (submit invoice to receive payout)
            - Processing payout (payout will be released within 30 days post invoice submission date)
            - Payout settled
    - GST payout table details for DB
        - Partner Account ID
        - GST Payout ID
        - GST Invoice ID (Invoice reference number)
        - GST billing Month
        - Gross payout Amount
        - GST Payout Amount
        - Created On
        - Last Updated On
        - Status
            - EXPIRED
            - PENDING_INVOICE_SIGN
            - PENDING_PAYOUT_INITIATION
            - PAYMENT_SETTLED
        - Invoice Received On
        - Invoice Link
        - Invoice Number
        - GSTIN
        - Company Name
        - IP Address
        - UTR
    - **Additional requirement**
        - To make the earnings section access authentication based for partners - [PRD](https://docs.google.com/document/d/1k34Wq6xaQAgXKVoYKge5_R5sGKeTcD7liaTAbiaZ01w/edit?usp=sharing)
- **Backfilling of GST payout details -**
    - We will update the GST payout details of the current financial year
        - Marked the current financial year GST payouts as settled for the ones present in the sheet
        - GST Master :
        
        [https://docs.google.com/spreadsheets/d/1ySNkmx-EZswjZgtBuX6xjHYrZuBYdQcFzMAVEdQ-e3o/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1ySNkmx-EZswjZgtBuX6xjHYrZuBYdQcFzMAVEdQ-e3o/edit?gid=0#gid=0)
        

# **Design**

---

- https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/MFD-partner-flow?node-id=6602-57467&p=f&t=xMDlTSP8f9beb4hF-0

# **Analytics**

---

- Monthly GST payout details

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

Note - 

- GST present v/s not present handling
    - Backfill all GST payout for present GSTIN to success
    - Escalations to be handled on a case by case basis
- Have to call out in designs that OTP consent is a signature etc.
- What is TDS and what is GST education information
- Payout section visibility (Validation of making it visible for the current financial year)
- Auto populate
    - GSTIN number
    - Company name
- Email of the invoice generated is sent to the partner once the invoice is generated and download invoice option in the section
- GST BE Payout table
    - GST Payout ID
    - GST Invoice ID
    - Total income
    - GST payout amount
    - created_on
    - last_updated_on
    - Status
    - invoice received on
    - invoice link
    - Invoice number
    - GSTIN
    - Company name
    - IP address
    - UTR
    - Partner account ID
    - GST payout billing month
- Status
    - Expired
    - Invoice signature pending
    - Invoice under review
    - Payout settled
- TDS and GST amount informations (Rs 14,700)
- Email send to partner for MFD
- What is TDS and what is GST education information

- Status
    - Claim expired (payout claims of only current financial year can be processed)
    - Invoice submission pending (submit invoice to receive payout)
    - Invoice submitted (payout will be released within 30 days post invoice submission date)
    - Payment settled
    
    - TDS (2% TDS is applied once total gross payout exceeds ₹19,600 as per Volt internal policy)
    - GST (GST payout is calculated as 18% of gross payout)
    - Net payout (Gross payout - TDS)