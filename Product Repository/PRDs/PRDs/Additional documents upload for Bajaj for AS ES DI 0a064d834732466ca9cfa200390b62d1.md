# Additional documents upload for Bajaj for AS / ES DIY document creation + Line enhancement

: Vaibhav Arora
Created time: March 12, 2024 8:48 AM
Status: Ready for Tech
Last edited: September 20, 2024 3:06 PM
Owner: Vaibhav Arora

# **What problem are we solving?**

We are solving for autofilling these documents for the user and integrating them in the journey to improve the loan booking experience of joint holders of mutual funds.

Broadly, there are two ways to own a mutual fund:

1. Individual ownership (single account holder)
2. Joint ownership
    1. Joint (Approval of both parties is required) (2 account holders)
    2. Anyone or survivor (AS) (anyone can manage the account without seeking the other person’s approval) (up to 3 account holders)
    3. Either or survivor (ES) (both can manage the account without seeking other’s approval) (two account holders)

<aside>
🔢 5% of all applications have joint holdings and 9% of all credits have joint [accounts](https://docs.google.com/spreadsheets/d/1UqFxl7gpgHuGPBk_0jPACHKxF1Cy1LnUkfubxXMRA64/edit#gid=391672949)

</aside>

We also have a use case of unifying lines for our users, where individual holdings are combined under a loan account, and secondary borrowers are added as additional security providers.

Problem overview:

- Current process does not support uploading of documents on UI
- Ops team have to manually share and coordinate with customers for documents
- Documents are error prone - Ops team fill them on behalf of the customers and get them signed

---

# **How do we measure success?**

- Loan application TAT for joint account holders (from credit line generation to unlocking credit limit)
    - Time stamp of application creation and credit creation

---

# **How are others solving this problem?**

![Untitled](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Untitled.png)

![Untitled](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Untitled%201.png)

---

# **What is the solution?**

We will be recreating digital versions of forms (Update)

For the scope of first development we are only picking co-borrower and addendum form:

[Bajaj ECS Mandate.pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Bajaj_ECS_Mandate.pdf)

[coborrower.pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/coborrower.pdf)

[_ADDENDUM SAMPLE new new (1) (1).pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/_ADDENDUM_SAMPLE_new_new_(1)_(1).pdf)

[__CO APPLICANT FORM SAMPLE.pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/__CO_APPLICANT_FORM_SAMPLE.pdf)

Self attested PAN (photo of the document signed by the user)

Self attested Aadhaar (photo of the document signed by the user)

```html
<!DOCTYPE html>

<head>
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
</head>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<!--[if gte mso 9]>
<xml>
 <o:OfficeDocumentSettings>
  <o:AllowPNG/>
  <o:PixelsPerInch>96</o:PixelsPerInch>
 </o:OfficeDocumentSettings>
</xml>
<![endif]-->
<title></title>
<meta name="viewport" content="initial-scale=1.0,width=device-width" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="ROBOTS" content="NOINDEX, NOFOLLOW" />
<meta name="referrer" content="no-referrer" />
<style type="text/css">
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
.mob-img-95 {
    width: 95% !important;
    max-width: 100% !important;
}
}
</style>
</head>
<img height="0" width="0" alt="" src="https://mcusercontent.com/4be6dced2f8f027c9d1b68acc/images/3fd93179-53a2-84dc-8349-f3e994749ed3.png"/>
<body topmargin="0" bottommargin="0" leftmargin="0" rightmargin="0" bgcolor="#ffffff" style="background-color:#f9f9f9;">

<!-- End of DoubleClick Floodlight Tag: Please do not remove --> 
<!-- framework start -->
<table width="100%" cellpadding="0" cellspacing="0" align="center" border="0" style="table-layout: fixed; margin: 0 auto; max-width: 600px;" bgcolor="#ffffff">
  
  <!--Header Starts-->
  
  <tr>
    <td align="center" style="font-family: sans-serif; font-size:10px; color:#000000; line-height:1.5;padding: 20px 5px 0px 5px; background-color: #FFFFFF; border-collapse: collapse;" valign="middle"><a href="#" target="_blank"><img class="mob-img" src="https://res.cloudinary.com/mailmodo/image/upload/v1713169958/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/f33bd0c64f95d69e99c5140c8ae37faf_urfomr.jpg" width="600" style="display: block;" alt=""></a></td>
  </tr>
  <!--Header Ends--> 
  <!--Body Starts-->
  
  <tr>
    <td width="100%" align="left" style="font-family: calibri; font-size:9px; color:#808080; line-height:1.7; padding: 0px 20px 0px 20px" valign="top"><table width="100%" style="border-spacing: 0; border-collapse: collapse; margin-right: auto;">
        <tr style="height: 0px;">
          <td  style="padding: 5px 5px 5px 0px;  vertical-align: top; width: 65px; font-size: 9px;" valign="top"><strong>Name (same as OVD)*</strong></td>
          <td  style="padding: 5px 5px 5px 5px;  vertical-align: top; width: 65px;font-size: 9px; " valign="top"><hr>
            <strong>Prefix</strong></td>
          <td  style="padding: 5px 5px 5px 5px;  vertical-align: top; width: 65px;font-size: 9px;" valign="top"><hr>
            <strong>First Name</strong></td>
          <td  style="padding: 5px 5px 5px 5px; vertical-align: top; width: 65px;font-size: 9px;" valign="top"><hr>
            <strong>Middle Name</strong></td>
          <td  style="padding: 5px 5px 5px 5px; vertical-align: top; width: 65px;font-size: 9px;" valign="top"><hr>
            <strong>Last Name</strong></td>
        </tr>
        <tr style="height: 0px;">
          <td  style="padding: 5px 5px 5px 0px;  vertical-align: top; width: 65px; font-size: 9px;" valign="top"><strong>Father/Spouse/Mother name*</strong></td>
          <td  style="padding: 5px 5px 5px 5px;  vertical-align: top; width: 65px;font-size: 9px;" valign="top"><hr>
            <strong>Prefix</strong></td>
          <td  style="padding: 5px 5px 5px 5px;  vertical-align: top; width: 65px;font-size: 9px;" valign="top"><hr>
            <strong>First Name</strong></td>
          <td  style="padding: 5px 5px 5px 5px;  vertical-align: top; width: 65px;font-size: 9px;" valign="top"><hr>
            <strong>Middle Name</strong></td>
          <td  style="padding: 5px 5px 5px 5px;  vertical-align: top; width: 65px;font-size: 9px;" valign="top"><hr>
            <strong>Last Name</strong></td>
        </tr>
      </table></td>
  </tr>
  <tr>
    <td align="center" style="font-family: sans-serif; font-size:10px; color:#000000; line-height:1.5;padding: 0px 0px 0px 0px; background-color: #FFFFFF; border-collapse: collapse;" valign="middle"><a href="#" target="_blank"><img class="mob-img" src="https://res.cloudinary.com/mailmodo/image/upload/v1713977085/editor/p/2c2b5e3c-a145-4baf-9ffa-e742927ed41b/5af909fe347e3ab575f33959835adfef_u5cclo.jpg" width="600" style="display: block;" alt=""></a></td>
  </tr>
  <tr>
    <td align="center" style="font-family: sans-serif; font-size:10px; color:#000000; line-height:1.5;padding: 0px 0px 0px 0px; background-color: #FFFFFF; border-collapse: collapse;" valign="middle"><a href="#" target="_blank"><img class="mob-img" src="https://volt-images.s3.ap-south-1.amazonaws.com/co_applicant_bottom.png" width="600" style="display: block;" alt=""></a></td>
  </tr>
  <!--Body Ends till CTA--> 
  <!--Footer Starts--> 
  
  <!--Footer Ends--> 
  
  <!-- framework end --><!--android gmail zoom fix--> 
  <!--/android gmail zoom fix--><!-- android yahoo fix-->
  
</table>
<!--/android yahoo fix-->
</body>
</html>
```

## Requirements overview

Co-applicant form fields:

[Form field values](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Form%20field%20values%207a94dfc8ac3b48608fe1939f9c1f7704.csv)

![Screenshot 2024-04-03 at 1.41.13 PM.png](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Screenshot_2024-04-03_at_1.41.13_PM.png)

Addendum: Comma separated names of borrower + coborrowers

![Untitled](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Untitled%202.png)

Addendum: Name of borrower (signed and delivered as a list)

![Untitled](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Untitled%203.png)

All borrowers name to be added here

![Untitled](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Untitled%204.png)

![Untitled](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Untitled%205.png)

## User stories / User flow

## Requirements

### Document creation

Four documents to be created in HTML with custom fields as described in table above:

- ECS Mandate form (out of scope)
- Coborrower form (pre-filled via code - Signed with self attested photo of the user)
- Addendum (Samples attached above) (pre-filled via code - Signed with self attested photo of the user)
- Self attested PAN document of the coborrower
- Self attested Aadhaar document of the user

Types of Document:

There are broadly two types of documents:

- Documents which are prefilled and created for the user to sign (Download option would be available for the user)
- Documents where the user has to print their own document and then upload it (Aadhaar and PAN) - Download option would not be available

Selected fields will be auto-filled with the user’s details (for the user to be able to download, sign and directly upload the document on UI

### Document upload on UI

- New screens on UI that will support document upload by the user
- Additional KYC step called “Documents” to be triggered via specific events defined in backend
- Post uploading the document user will be taken to a status screen which will only get updated and take the user to the dashboard if documents are approved via an admin action by operations team.
- Additional borrowers section (in terms of joint holding) will be added as a part of KYC
- Sample documents (to be uploaded on S3, links of which will be shared on UI for the user to see).

### Backend handling:

- Trigger events to be defined which will tell frontend to show additional step on KYC
    - Mandate skipped via admin action (trigger one) - Bajaj (will change basis new digio requirement) - Bajaj mandate not successful
    - Admin action to enable mandate document for the user
        - In case there are no co-applicants and this admin action is hit, documents page with just the mandate ECS form should be available for the user
        - Mandate ECS form will only be for the primary co-applicant form
        - Ops agent should be able to enable collection of document via admin action
        - Mandate ECS form to be sent as additional documents to ops for approval within the same workflow
        - Post approval additional documents should get automatically uploaded in the account opening, enhancement and renewal mail sent to Bajaj
    - Joint holding detected while fetch **and joint holding mutual funds are selected by the applicant in the credit limit** (Modeofholding in (AS ES or 4 (Karvy))
    - Line unified (Added application to primary application)
    - For line enhancement/margin pledge of existing cases with joint holding and
- Basis triggers we will tell frontend to load additional step in KYC for the user to complete
- Uploaded documents by the user will be sent as a mail on Ops email (ops email format)
- Post verification ops can forward it to Bajaj ops (if documents are correct), if documents are incorrect Ops will invoke an admin action which will take back the user to the documents screen for re - upload
- 
    - **(Admin action to skip document flow)
    (Admin action to take the user back to application flow - Reject selected documents)
    (Admin action to reject document)**

Cases where Document upload section has to be visible for the user
Current scope (User will see document upload for line enhancement and line renewal cases (since Bajaj needs re- KYC for all customers due to high risk classification)

| Flow | KYC Pod (old application) | Re-KYC required | Additional borrowers added | Documents available | New documents required | Expected handling |
| --- | --- | --- | --- | --- | --- | --- |
| Line enhancement/Line renewal | Yes | No | Yes | Yes | No | Show document upload flow (Addendum and coborrower form for new borrower) - Copy available coborrower form for existing coborrower |
| Line enhancement/Line renewal | Yes | No | No | Yes | No | Copy older documents - user should not see document upload flow |
| Line enhancement/Line renewal | Yes | No | Yes/No | No | Yes | Show UI flow to the user, user to upload documents again

(ops can skip documents if they are available) |
| Line enhancement/Line renewal | No | Yes | No | No | Yes/No dependent on availability | User should see document upload flow - Ops can skip on case to case basis |
| Line enhancement/Line renewal | No | Yes | Yes | No | No | User should see document flow |
| Recreate lender application | Yes | No | Yes/No | Yes | No | User should not see document flow |
| Recreate lender application | Yes | No | Yes/No | No | Yes | User should see document flow |
- **Admin action requirement 
Ops agent will be able to see all uploaded documents on UI via admin action and select documents which needs to be rejected for the user (status of rejected documents will change from uploaded to pending) - Documents will get deleted automatically for the user, user should still be able to download the sample and upload pending documents again.**
- We will only keep 2 states, uploaded and pending for the user and backend, once uploaded user can upload documents on both states
- Selection of rejected documents (selective upload of documents on UI) - Admin action

### Reporting and analytics:

- Audit log of new admin action that will send back the user to the document upload screen “REINITIATE_DOCUMENT_UPLOAD”
- Application created at, credit created at to measure turn around time for credit creation in joint holding accounts
- Number of validation cycles (document) - Document re-upload

### User communication:

- Users will be communicated on two steps:
    - When documents are uploaded:
        - Documents uploaded successfully! (Handled this via UI not required)
        Dear {{user_name}},
        
        Documents for your Volt Money credit line of ₹{{credit_line}} have been submitted successfully and are under approval.
        
        Please find the signed documents attached in the email.
        
        Regards,
        Team Volt
        d-b9c7b21b345a42e8a61b32b3fec26fff (template id for sendgrid)
    - Documents rejected:
    - (Subject): Your documents verification was rejected
        - Action required: Documents rejected!
        Dear {{user_name}}
        
        Documents submitted for your application for your Volt Money credit line of ₹{{credit_line}} were rejected.
        
        Please click here to submit the documents again, for any query or feedback, call us or WhatsApp us at +919611749097
        
        Regards,
        Team Volt
        
        d-eecf9108a5b54d06a6951e785bc85513
        - {{user_name}}: {{Primary_holder_name}}
        - {{credit_line}}: {{credit_line}}
        - sendername: Volt Money
        - Recipient: Customer email (user_email) (to), [vaibhav.arora@voltmoney.in](mailto:vaibhav.arora@voltmoney.in) (bcc)
        - "supportEmail": "[support@voltmoney.in](mailto:support@voltmoney.in)"
        - "contactnumber": "+919611749097”
        - {{lenderLogoUrl}}

### Ops notification

Ops will receive an email containing all the documents when a user submits additional documents for Bajaj: (Will be triggered even after retries)

Subject: Coborrower form and addendum for {{user_name}}

Email:

(Subject): Additional documents submitted by customer

Hi Team,

Please find the attached additional documents for the application of {{user_name}} with application id {{application_id}}.

Please approve the following documents and share with BFL team to complete application.

{{documents}}

Document name (Coborrower form - {{borrower_name}}) - Document Id

Document name (Coborrower form - {{borrower_name}}) - Document Id

Document name (Coborrower form - {{borrower_name}}) - Document Id

Document name (Addendum}) - Document Id

Regards,

Team Volt Money

d-bc596973f8e240eba349087e539f7d01

{{user_name}} - {{Primary_holder_name}}

{{application_id}} - {{application_id}}

Sender name: Volt operations

{{document_detail}} - Data of documents 

"supportEmail": "[support@voltmoney.in](mailto:support@voltmoney.in)"

"contactnumber": "+919611749097”

{{lenderLogoUrl}}

Recipients: [operations@voltmoney.in](mailto:operations@voltmoney.in) (to), [vaibhav.arora@voltmoney.in](mailto:vaibhav.arora@voltmoney.in) (bcc)

<aside>
⚠️ It is important to attach the documents in the email so that if approved, Volt operations team can forward the documents to BFL operations.

</aside>

### Bajaj comms

Bajaj receives three types of emails upon completing applications from Volt

1. Account opening email : New application
2. Line enhancement mail: Enhancement in sanction limit
3. Line renewal 

There may be co-applicants or additional documents required in each of the step, if the application contains additional documents signed by the user, the documents should be attached in the email for Bajaj to review post ops verification

Email format: Same as before with additional documents

Recipients (add): [operations@voltmoney.in](mailto:operations@voltmoney.in) (to), [vaibhav.arora@voltmoney.in](mailto:vaibhav.arora@voltmoney.in) (bcc)

### HTML Documents

[Coborrower_html.html](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Coborrower_html.html)

[ADDENDUM SAMPLE.html](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/ADDENDUM_SAMPLE.html)

### Amplitude events

[https://docs.google.com/spreadsheets/d/1mx2ktWwy3UkUFRtG7mVPxx9v4yN6beo5mbrM2E9ht28/edit#gid=0](https://docs.google.com/spreadsheets/d/1mx2ktWwy3UkUFRtG7mVPxx9v4yN6beo5mbrM2E9ht28/edit#gid=0)

---

# **Design**

[https://www.figma.com/file/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?type=design&node-id=6814%3A19436&mode=design&t=Bmh62FrYMIyTTOmF-1](https://www.figma.com/file/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?type=design&node-id=6814%3A19436&mode=design&t=Bmh62FrYMIyTTOmF-1)

---

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