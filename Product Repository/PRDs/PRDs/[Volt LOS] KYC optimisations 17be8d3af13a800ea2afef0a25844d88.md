# [Volt LOS] KYC optimisations

: Saksham Srivastava
Created time: January 14, 2025 7:30 PM
Status: Not started
Last edited: March 19, 2025 12:54 PM

# **What problem are we solving?**

Currently for customers to complete KYC on Volt Money, across lenders we only have one KYC mechanism - Digilocker. 

Key pain points of customers on the KYC step - 

1. Frequent Digilocker downtime - 2 major outages/week. Customer conversion on KYC falls to zero during such downtimes, no backup flows for KYC implemented here. 
2. Friction for the customer to complete the KYC journey - 
    1. Customers have to input their complete Aadhaar number, DL PIN, Aadhaar OTP to complete KYC. 
    2. Partners when completing KYC of the customers need them to share Aadhaar OTP and DL PIN to complete KYC of the customer. 

~20% customers drop off from the Digilocker step in the application. 

Only ~48% of customers (out of customers who complete KYC) complete Digilocker step in under 5 mins. 

---

# **How do we measure success?**

- Reduce drop-off from the KYC step to < 10%.
- > 70% of the customers should be able to complete KYC in less than 5 mins.

---

# **How are others solving this problem?**

Industry standard for the KYC conversion rate is ~75%

- Navi
    1. CKYC is found for 90% of the customers and for 90% out of these customers it passes validations. ~20% customer go through the OKYC flow. 
    2. OKYC flow provider - Digitap. Customer has to enter Captcha, Aadhaar is entered on Digitap UI. 
    3. Overall conversion of 75%(D1 conversion 60%, D7 conversion 75%). Step wise success percentage don’t know current. 
        
        ![mermaid-diagram-2025-01-20-161123.svg](%5BVolt%20LOS%5D%20KYC%20optimisations/mermaid-diagram-2025-01-20-161123.svg)
        
- Cred
    1. Cred has 6-7 lenders each one of them have their own KYC flows. Some have their own stacks which they want LSPs to integrate some allow LSP to do KYC and push documents. 
    2. ~50% of the customers have Digilocker account.
    3. Depending on the lender the KYC conversion is between 50-80%. 
    4. EKYC is limited KYC, lending limit is ₹60k
    5. OKYC flow might go down in near future, Digilocker should be there.
    6. Recent cases of DL outage were because of DL issues and not UIDAI issues. OKYC flow is was working.
    7. Suggests the vanila digilocker flow as after March 2024, opening a DL account does not require you to enter aadhaar which means. DL accounts can be there which don’t have Aadhaar in them. These account are called empty accounts, 1-1.5% cases in Cred. 
    8. In addition to the Navi checks, he mentioned to verify Father’s name as well.
    
    ![IMG_4567.HEIC](%5BVolt%20LOS%5D%20KYC%20optimisations/IMG_4567.heic)
    
- Groww
    1. Connected with the investments product onboarding person, credit team uses their KYC stack only. Mandate credit team have built themselves. 
    2. Only PAN (number) verification through NSDL. Partial verification.
    3. Digilocker - Aadhaar pulled
    4. Complete PAN verification through NSDL - this twice verification costs more but provides better customer experience
    5. In case DL is down, customer flows to manual document upload. These documents are manually verified. 
    6. Very small percentage people go to this flow (same as DL downtime)
    7. Not comfortable with sharing conversion numbers
- Cashe
    - Earlier:
        - CKYC first, then OKYC.
        - Conversion number: Won’t be able to disclose
    - Current:
        - Only digilocker, done upfront in the journey. Both PAN and Aadhaar documents are pulled.
        - PAN verification done through NSDL before DL. If they are unable to pull PAN from DL, they move past.
        - CashE compliance called out CKYC and OKYC non compliant. CKYC - RBI had called CKYC unreliable, OKYC - Non compliant because of scrapping.
        - They do VKYC for cases where the loan amount in more the ₹50k
        - Conversion number: “It’s not bad” 10% down after moving to Digilocker

---

# **What is the solution?**

TL;DR 

- Introduce multiple methods of KYC for DSP Fin customers.
- Build an orchestration among these KYC methods for the customer. In case customer is unable to complete KYC through one method because of user issues or downtime, they should be redirected to the fallback method(s) of KYC.

What counts as KYC for our customer?

- Compliance (CDD) requirements
    
    Obtain the following - 
    
    1. Aadhaar number 
        1. Proof of possession of Aadhaar(current), OVD, or equivalent e-document. Will have to do Digital KYC in this case. 
        2. the KYC Identifier with an explicit consent to download records from CKYCR
    2. the Permanent Account Number or the equivalent e-document thereof. This needs to be verified from the issuing authority. 
- POI/POA requirements
    - POI : PAN will always be the POI.
    - POA: Aadhaar is the primary POA currently.
    - Have to check the linkage between POI and POA.
- Different KYC methods + pros/cons
    
    
    | **Method** | **Pros** | **Cons** |
    | --- | --- | --- |
    | Digilocker | - If PAN document is fetched, it serves as PAN verification and POI-POA | - Frequent downtimes
    - High friction for the customer to input details  |
    | CKYC | - No customer intervention required to complete KYC | - Junk data 
    - Have to build validations to understand sanctity of the data  |
    | OKYC | - Easier than digilocker to verify Aadhaar | - Might be “non compliant” as per few players and providers
    - Delays in Aadhaar OTP being sent to customers 
    - UIDAI downtimes
    - Have to mask the Aadhaar in DB  |
    | OCR |  | - No way to properly verify Aadhaar. 
    - Have to mask the document before storing |
- Plan
    
    

Phase 1 - 

1. Check if the customer already has a digilocker account or not. 
2. If the customer has a DL account, flow the customer to the Meri Pehchaan PIN-less login flow 
3. If the customer does not have a DL account, the customer will be directed to the current Digilocker Aadhaar login flow. 

Items to get clarity on - 

1. As per Decentro, if customer has not accessed Digilocker in the last one year. We won’t be able to get Aadhaar of the customer through the Meri pehchaan flow. Decentro has handled this case, they trigger the main Digilocker flow for such customers again. Have to get clarity from Digio here. 
2. Can the PIN-less login checkbox be removed from Meri Pehchaan UI. Decentro mentioned that this can be done. Have to get clarity from Digio. 
3. Customer sign-up flow in Meri Pehchaan is not ideal. Have to avoid this flow for customers. 

![image.png](%5BVolt%20LOS%5D%20KYC%20optimisations/image.png)

## Requirements overview (optional)

## User stories / User flow

## Requirements

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

Meeting with Decentro - 15th Jan 

- 15-20% failures in sending OTP
- 100% Captcha breaking
- They purge the Aadhaar. Aadhaar pass through, have to solve for storing in our DB
- 2 PDF versions - letterhead, another is a customised one
- OCR and Image quality check can be
- Download throttling, warm up numbers
- CKYC whole stack will live on our servers
- Address check from delivery aggregator
- Webview
- For customers who have not opened Digilocker
- Pin less box can be removed
- Consent reinforcement
- TTL - Time to live older than a year then UI stream will flow to the old a

[https://digilocker.meripehchaan.gov.in/signup/](https://digilocker.meripehchaan.gov.in/signup/) - Meri pehchaan digilocker signup flow