# NBFC: Capturing Additional details post KYC

: Gautam Mahesh
Created time: June 12, 2025 3:13 PM
Status: Ready for Tech
Last edited: July 11, 2025 12:42 PM
Owner: Gautam Mahesh

# **What problem are we solving?**

Few LSPs integrating with our stack do not capture all the necessary ‘Additional Details’ or ‘declarations’ required by DSP to process the loan. In such cases, LSPs expect the DSP to collect these details directly from the customer.

---

# **How do we measure success?**

DSP Coverage of Missing Mandatory Fields: We must ensure that 100% of applications from LSPs (excluding Volt) have all mandatory additional details/declarations captured at the DSP end if not provided by the LSP.

**Adoption Metric:** Percentage of LSPs relying on DSP to capture one or more of the additional details/declarations.

---

# **How are others solving this problem?**

There are other lenders like IDFC which ask the customers for the  details fetched from Digilocker eg: Dependent’s name and their relationship with the customer. A sample SS is attached below.

![Screenshot 2025-05-11 at 8.28.58 PM.png](NBFC%20Capturing%20Additional%20details%20post%20KYC/Screenshot_2025-05-11_at_8.28.58_PM.png)

---

# **What is the solution?**

## Requirements

FE Requirements: 

- LSP initiates KYC using the Init KYC API
- DSP creates a Digilocker link with a redirection URL
- DSP shares the link with the LSP
- Customer clicks on the link and is redirected to Digilocker
- Customer completes the Digilocker journey through Digio
- Digio redirects the customer to the DSP URL passed in the request
- Customer is shown below items on an UI which is rendered on DSP’s end
    
    Below is the complete list of fields that can appear on this UI. The visibility of each field is configurable based on the LSP’s ability to furnish the corresponding data.
    
    - Full Name of customer
        - To be pre-filled from Digilocker if available/found
        - Can be edited
        - Basic regex checks to be configured here and appropriate messaging to be shown(”Pls enter your full name/Pls enter a valid name”)
    - DOB
        - To be pre-filled from Digilocker if available/found
        - Can be edited
        - Basic regex checks to be configured here (Please enter a valid DOB)
    - Address
        - To be pre-filled from Digilocker
        - Cannot be edited
    - Father’s  first and last name: To be entered by the customer
        - Basic regex checks to be configured here (eg: Please enter the full name of father)
    - ‘Purpose of Loan ‘ dropdown
        - To be selected by the customer
        - Following are the options to be supported
            - Personal
            - Business
            - Investments
            - Emergency
    - Display the pre-checked ‘Indian resident declaration’ checkbox: “I confirm that I am a resident individual”
    - Display the pre-checked  ‘PA=CA’ declaration checkbox : “I confirm that my current address is same as permanent address as shown above”
- Customer confirms that their details are correct and confirms the same by clicking on ‘Confirm’ CTA
- The customer is redirected to the page of LSP to complete the next steps (Selfie or Bank Account step)

Note: 

- This is only for Digilocker as of now. We will use the same intermediate page to capture the customer’s details when the CKYC flow goes live
- The customer should not be allowed to proceed if any of the applicable fields are left blank (field applicability is based on the configuration for the respective sourcing partner).

BE

- The redirection URL currently sent to Digio needs to be replaced with the DSP URL, so that the customer is taken to DSP’s ‘Additional Details’ page.
- Once the customer completes this page, DSP will redirect them back to the LSP journey.
- Since DSP is collecting the fields that LSPs are unable to capture, those specific fields can be omitted by the LSP in the ‘Save Additional Details’ API. Depending on the sourcing channel, we should mark these fields as optional in the API. However, all mandatory fields must be available before proceeding with agreement generation

---

# **Design**

Create an intermediate page that captures all the above details including the messaging and alerting.

Figma link : https://www.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-Ad-Hoc-tasks?node-id=363-1466&t=JZWA42oUXJpsKmf7-0

---

# **Analytics**

Below are the metrics we will track.

- Number of customers who landed on UI - Amplitude to be configured
- Number of customers who filled out the details and continued - Amplitude/DB
- Field level analytics for all field that requires explicit entry or support edit

---

# **Timeline/Release Planning**

This will be rolled out across phases.

- LSPs like PhonePe will be enabled on this flow
- Subsequent LSPs who will not be capturing required details

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Inform LSPs about the change
- [ ]  Business
    - [ ]  
- [ ]  Design
    - [ ]  Create intermediate page

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