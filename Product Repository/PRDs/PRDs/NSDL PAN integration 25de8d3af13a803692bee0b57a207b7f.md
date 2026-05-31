# NSDL PAN integration

: Devansh Kar
Created time: August 28, 2025 4:44 PM
Status: Not started
Last edited: April 29, 2026 5:11 PM

# **What problem are we solving?**

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

- Provide an option to LSPs to complete KYC of customers in DSP UI. The complete KYC including NSDL PAN verification + documents pull + selfie match will be orchestrated in DSP UI reducing effort required from LSPs to integrate KYC. This will include Digilocker and CKYC as methods of document download,
- Provide APIs to LSPs to complete *KYC for customers (*NSDL PAN verification + documents pull + selfie match*)*. This will give LSPs the flexibility to build their own UI and experience for completing KYC for customers.
- Ensure *regulatory compliance* and *improve success rates* by making the KYC journey simpler and clearer for end users.

## Requirements

NSDL PAN verification
**Note: 
1.** This is not implemented in the current version as we dont  have the NSDL integration done yet. This will be picked up post NSDL onboarding is done. **** 
2. PAN verification in the current flow will be done via Signzy at the end of successful KYC verification. 

1. Flow #1: 
    1. Customer will see the form to enter Name and DOB. 
    2. Post filling the details, NSDL PAN verification API will be triggered. 
        
        [NSDL PAN Verification API _ HyperVerge.pdf](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/NSDL_PAN_Verification_API___HyperVerge.pdf)
        
    3. Success criteria for PAN verification - all of the below should be satisfied. If PAN verification is successful, LSP will be sent PAN verification successful webhook. 
        1. panStatus: “EXISTING AND VALID”
        2. name: "MATCHING"
        3. dateOfBirth: "MATCHING" or “NOT-MATCHING”
        4. aadhaarSeedingStatus: "Y"
        
        <aside>
        💡
        
        - Name needs to be exactly matching as PAN is the POI for loan application. The name of the applicant in our application should be the exact legal name.
        - DOB does not need to match exactly. We only need to validate if the age of the customer is between 18 and 70 years. This can be checked from the DOB that comes in the CKYC download or from digilocker (as per the current process).
        </aside>
        
    4. PAN number should be in the format  **XXXPX1234X.** 4th letter of the PAN should be “P” to indicate that the PAN belongs to an individual. If this requirement is not matched return error `“PAN in opportunity does not belong to an individual”` to LSPs in a webhook.  PAN verification API should not be triggered in this case. This error will result in KYC failure. 
    5. In case panStatus ≠ EXISTING AND VALID, “PAN entered is not a valid PAN” error will be shown to the customer in UI and given as a webhook to LSP as well. This error will result in KYC failure. 
    6. In case aadhaarSeedingStatus ≠ Y, “PAN is not linked to Aadhaar” error will be shown to the customer in UI and given as a webhook to LSP as well. This error will result in KYC failure. 
    7. Customers can trigger PAN verification thrice. After 3 tries in 15 mins. “Maximum attempts reached for PAN verification” error will be shown to the customer in UI and given as a webhook to LSP as well. The number of retries and the cooldown time should be in a config that can be changed later. 
2. Flow #2: 
    1. DSP will perform NSDL PAN verification check before rendering sending the KYC link. 
    2. Once PAN verification is successful, KYC link will be sent to LSP along with PAN verification successful webhook. Selfie capture UI should be shown to the user, skipping the PAN verification UI. 
    3. In case PAN verification fails as per success criteria mentioned [here.](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)%20189e8d3af13a803aa872e67345979451.md) Error messages mentioned in point d, e, f, and g of flow #1 will be shared with LSP. These errors will result in KYC failure. 
3. Flow #3:
    1. LSP will hit the KYC init API, DSP will internally hit PAN verification API.
    2. If PAN verification is successful, a success callback will be given to LSP. 
    3. In case any error mentioned in point d, e, f, and g of flow #1 occur, corresponding error message will be shared with LSP. These errors will result in KYC failure. 

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