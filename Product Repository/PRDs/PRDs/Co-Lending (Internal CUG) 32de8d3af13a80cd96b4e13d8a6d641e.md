# Co-Lending (Internal CUG)

: Priyamvada S
Created time: March 24, 2026 11:58 AM
Status: Not started
Last edited: April 26, 2026 4:37 PM

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

Step 1: Entry points (No change)

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
- 

Step 3: Loan Offer Confirmation (No change)

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
    - PAN available via Digilocker
    - Annual income >3L
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

Step 9: Email verification (no change)

Step 9: Loan contract

BE

- DSP API to render  KFS & Agreement of ‘TCL-DSP’ colender cohort in the redirection journey

Step 10: Submit Opportunity

BE

For ‘DSP-TCL’ cohort, following changes are required:

Pre-workflow validations

- Client dedupe : TCL ‘Dedupe +Risk’ wrapper API to be called in addition to DSP dedupe
- Sourcing channel validation: All ‘TCL-DSP’ co-lender applications to go via NSTP

On receiving the NSTP application, Ops will trigger VKYC workflow from Hyperverge dashboard and on successful VKYC, Ops to approve application & VKYC status/data to get updated in DSP BE

Post NSTP approval, initiate CLAW workflow with following additional requirements:

- Lead, Opportunity & Webtop ID creation
- Upload f[ollowing documents](https://docs.google.com/spreadsheets/d/1Jzbf4iQq3naCVnrIzG_gEXlGZoPjzzw1/edit?usp=drive_web&ouid=116325890390285274812&rtpof=true) to the webtop
- Agreement singing workflow to contain 2 DSC based signing (one by DSP & one by DSP on behalf of tata) and one clickwrap signing (by user). Please find below the signing order
    1. Customer signature
    2. DSP Signature
    3. DSP Signature on behalf of TCL
    4. Customer gets a lender signed copy of the agreement
    5. Stamp paper is affixed
    6. On stamp paper - DSP Signature and / or DSP Signature on behalf of TCL

## CC & Ops

-Ops to trigger the VKYC workflow from Hyperverge dashboard & approve the NSTP application

---

# **Design**

Internal CUG: 

---

# **Analytics**

---

# Open points (Tata)

DSP & Colender logo on offer page

Additional details -PWD requirement

T~~ata documents~~

CC requirements

Agreement signing

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

-Opporutnity created willhavea contract type in our DB to idenitfy the subseuqnet colending apis

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes