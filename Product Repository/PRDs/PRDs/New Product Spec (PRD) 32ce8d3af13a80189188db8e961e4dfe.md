# New Product Spec (PRD)

: Priyamvada S
Created time: March 23, 2026 3:10 PM
Status: Not started
Last edited: March 24, 2026 11:57 AM

# **What problem are we solving?**

-

---

# **How do we measure success?**

-

---

# **How are others solving this problem?**

-

---

# **What is the solution?**

## Internal CUG (V0)

## *User cohort*

 A small no of users (’PAN ‘+ ‘Mob No’) will be whitelisted for the  ‘DSP-TCL’ co lending journey in Volt B2C app .

## *User journey*

Described below are the key steps in the co-lending user journey 

Step 1: Entry points (App/Webapp/Website)

![image.png](New%20Product%20Spec%20(PRD)%2032ce-4dfe/image.png)

FE

- User enters & verifies mob no with OTP
- User enters PAN no > Hits ‘Check eligibility’ >Fetch triggered

BE

- Volt hits  RTA Fetch APIs for fetching MFs

Step 2: MF Fetch & Offer generation

FE

- User enters CAMS OTP >Views fetched portfolio & eligible limit
- User hits ‘Get more portfolio’> Enters KFIN OTP> Views updated portfolio & eligible limit

BE

- On Volt receiving the fetched funds, it hits DSP to get the { ‘Approved fund list’ , ‘LTV’, NAV & units}
- DSP checks if ‘Override Lender assignment BRE’ flag is set to ‘True’ for user ‘PAN & mob’ combo
    - If ‘true’, DSP assigns lender= ‘DSP-TCL’ to user & share DSP-TCL’ approved fund list & LTV,
    - If ‘false’, defaults to lender=’DSP’ & shares DSP’s approved fund list & LTV
- On receiving above info, Volt generates ‘ eligible limit’ internally for the fetched  funds (for CAMS first and further ‘CAMS +KFIN’ ,if applicable )  based on the business config

Step 3: Loan Offer Confirmation (No change)

FE

- User views the eligible →Proceeds to select specific loan amount →Lands on the loan offer page

BE

- Volt hits DSP Client dedupe API → On success, Volt hits DSP Opportunity creation API

Step 3: KYC (including Hard BRE check)

FE 

User hits ‘Proceed with Digilocker’ > Lands on Digio DL  flow>Completes Digilocker flow

BE

- Volt hits DSP ‘KYC Init’ API >DSP returns DL url
- On receiving ‘Success’ from Digio> DSP triggers ‘Lender assignment BRE’ which runs the following checks in the below order:
    - Age: 21-65
    - AML/PEP: Trackwizz
    - CB: >=650
    - Tata ‘Dedupe + Risk’ api
    - If all conditions met, continue with ‘lender’ cohort=’TCL-DSP’ .
        - Note: In this case, offer will still be of the ‘TCL-DSP’ co-lending cohort
    - If any of the above conditions fail, BRE fallbacks to default lender assignment of ‘DSP’ provided below conditions
        - Age: 21-65
        - AML/PEP: If there is a hit, then moved to ‘Deviation’ flow

Note: ‘Lender assignment’ needs to be completed at DSP BE before Volt can proceed with the next step 

Step 4: Photo verification (No change)

Step 5: Additional details (TBC)

FE

- Volt needs to capture additional declaration from user that they are not physically disabled (pre-checked )
    - Note : Above is applicable only for “DSP-TCL’ cohort

BE

- DSP API to start capturing the consent,IP & timestamp of the additional  ‘Not PWD’ declaration

Step 6: Bank a/c verification(No change)

Step 7: Mandate set up (No change)

Step 8: Pledging 

FE (No change)

BE

- DSP API to use ‘TCL’ pledge credentials in MFC pledge wrapper API for ‘TCL-DSP’ colender cohort

Step 9: Loan contract

FE (No change)

BE

- DSP API to render  KFS & Agreement of ‘TCL-DSP’ colender cohort

Step 10: Submit Opportunity

BE

- Volt hits DSP ‘Submit opportunity’ API
- DSP performs the following checks

## 

---

# **Design**

Internal CUG: 

---

# **Analytics**

---

# Open points (Tata)

DSP & Colender logo on offer page

Additional details -PWD requirement

CC requirements

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