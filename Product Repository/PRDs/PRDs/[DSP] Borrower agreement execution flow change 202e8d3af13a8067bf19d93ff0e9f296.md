# [DSP] Borrower agreement execution flow change

: Saksham Srivastava
Created time: May 29, 2025 4:47 PM
Status: Ready for Tech
Last edited: July 21, 2025 2:52 PM

# **What problem are we solving?**

Making sure the agreement execution happens in the newly aligned order

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

Following would be the flow of agreement execution. The following order is a chronological and should be followed exactly. 

1. **Loan Application Received**
    - As soon as LSP triggers the generate KFS API, DSP should send an “Application received” email to the customer.
    - **Variables required:** date, name of the applicant, oppId, product name (Loan against mutual funds), timestamp of KFS generation.
    - **Sendgrid template ID**: d-6cdebdd4d34f4dbf97397458cd803b20
    - List and format of data sent in mail:
        
        "date":"24-10-2024",
        "oppId":"OPP6916467173",
        "customerName":"Saksham Srivastava",
        "[supportEmail":"support@dspfin.com](mailto:supportEmail%22:%22support@dspfin.com)",
        "product":"Loan against mutual funds",
        "supportNumber":"+91 96117 49097",
        "timestamp":"09-Dec-2024 03:36 PM"
        
        Following is SS of the Email communication: 
        
        ![image.png](%5BDSP%5D%20Borrower%20agreement%20execution%20flow%20change/image.png)
        
2. **Display KFS in LSP App**
    
    The Key Facts Statement (KFS) is shown to the customer within the LSP app interface.
    
3. **Customer Acknowledges KFS**
    
    The customer reviews and acknowledges the KFS. We store the timestamp of this KFS acceptance.
    
4. **Generate Unsigned Agreement D1**
    
    An unsigned agreement document (referred to as D1) is generated.
    
5. **Present D1 to Customer**
    
    D1 is presented to the customer inside the LSP app so they can sign it.
    
6. **Customer Signs D1**
    
    The customer signs D1; we capture and store the timestamp of their signature on D1.
    
7. **Generate Unsigned Agreement D2**
    
    A new unsigned version of the agreement (referred to as D2) is generated. Here previously we were completing the execution of D1 (DSP copy) before generating the customer copy of agreement. Now we will need to generate, sign and send D2 to customer before stamping. 
    
8. **DSP Signs D2**
    
    DSP signs on D2.
    
9. **Send D2 & Welcome Email to Customer**
    
    D2 is sent to the customer along with the loan account opening/welcome email. This email along with current attachments will also include:
    
    - A separate unsigned copy of the KFS document
    
    [Standalone KFS template.docx](%5BDSP%5D%20Borrower%20agreement%20execution%20flow%20change/Standalone_KFS_template.docx)
    
    - The customer’s KFS acknowledgement timestamp (from step 3)
    - The customer’s D1 signature timestamp (from step 6)
    
    The welcome mail will be sent as sent right now, ie, after creation of FXLAN. 
    
    Updated sendgrid template: d-f57d8c5d41da4e839c33f57dfc86f2a4
    
    List and format of data sent in email: 
    
    "date":"24-10-2024",
    "clientId":"FXCID453242",
    "lan":"FXLAN3453443",
    "customerName":"Vaibhav Arora",
    "customerFirstName":"Vaibhav",
    "[supportEmail":"support@dspfin.com](mailto:supportEmail%22:%22support@dspfin.com)",
    "creditLimit":"Rs 2,00,00,000",
    "supportNumber":"+91 96117 49097",
    "kfsTtimestamp":"09-Dec-2024 03:36 PM",
    "custSignTimestamp":"09-Dec-2024 03:39 PM"
    
    Following is the SS for updated mail. 
    
    ![image.png](%5BDSP%5D%20Borrower%20agreement%20execution%20flow%20change/image%201.png)
    
10. **Affix Stamp to D1**
    
    We affix the stamp to D1 (from step 6).
    
11. **DSP signs & Stores Stamped D1**
    
    DSP signs the stamped D1 and stores it as the final executed agreement.
    

---

# **Design**

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