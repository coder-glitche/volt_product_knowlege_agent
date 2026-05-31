# Current State: Kyc

> Auto-generated from 49 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Bajaj PAN verification API
**Status:** Not started | **Last edited:** September 19, 2024 6:26 PM

**Problem:**
are we solving?**

Currently Bajaj KYC fails for the following cases:

1. Full name (First, middle and last) is not shared / shared incorrectly in the KYC pod request. 
2. PAN is not already fetched in Digilocker

---

**Solution:**
?**

---

## #2 — User getting stuck at KYC verification step in cas
**Status:** On Hold | **Last edited:** October 7, 2024 5:01 PM

**Problem:**
are we solving?**

In the applications in which we are not able to fetch PAN details, the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

**Solution:**
?**

- User completes the KYC screen :
    - We get “POV=null” in the getkycdetails response.
    - Then we will not keep the user stuck at this step, and allow them to move to the next “bank account” step.
    - Then we will enable the user to add supporting documents in the documents section
- When the issue is of mis-match, we will enable the 1st applicant to the add additional documents screen, where we will make the user attach the :
    - PAN signed document
- Once the user has uploaded the document, these documents will be sent in BAJAJ account creation mail, **(with remarks)**
    - **Remarks : “PAN for the customer was not fetched from Digilocker, hence attaching the self attested PAN of the user”**
    - Add Pratik, Sheetal & Parul in cc
        - Pratik :  [pratik.bagul@bajajfin

---

## #3 — [Lending stack] KYC Flow
**Status:** Not started | **Last edited:** October 11, 2024 4:17 PM

**Problem:**
are we solving?**

Complete KYC of the customer for DSP lender. For completing a successful CDD, following are the requirements as per regulations.

1. Proof of possession of Aadhaar number.
2. Verified E-document of Aadhaar (to be used as proof of address)
3. PAN should be verified fro mt hte issuing authority. 
4. PAN details/document (to be used as proof of identity). 

---

**Solution:**
?**

---

## #4 — KYC Risk Status (NBFC Platform)
**Status:** Done | **Last edited:** November 12, 2024 6:05 PM

**Problem:**
are we solving?**

KYC risk status needs to be maintained against each client in the NBFC to maintain appropriate risk classification of customers in the LMS as well as in NBFC.

RBI requires us to maintain risk status for each customer under CDD and EDD measures, for all non face to face account based relationship openings, customer should be classified as high risk. 

For customers classified as high risk, their KYC should be evaluated every 2 years, (Re-KYC) unless a face to face KYC or VCIP is formed for the customer. 

To comply with the same, we need a method to store and display the KYC

**Solution:**
?**

Maintain KYC status and KYC expiry date (2 years post account opening) in LMS as well as internal storage at a client level. 

We will be storing the details at a client level in Finflux (datatables - clientkycdetails) and internally in Finflux against client ID.

The same will be visible for the operations and risk teams on the command centre on the client details and KYC details page

---

---

## #5 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #6 — NSDL PAN Verification — Non-STP Rejection Handling
**Status:** Not started | **Last edited:** May 28, 2026 3:16 PM

**Solution:**
?**

---

## #7 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #8 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #9 — [Volt LSP] Integrating DSP KYC
**Status:** Not started | **Last edited:** March 3, 2025 2:38 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #10 — [Volt LOS] KYC optimisations
**Status:** Not started | **Last edited:** March 19, 2025 12:54 PM

**Problem:**
are we solving?**

Currently for customers to complete KYC on Volt Money, across lenders we only have one KYC mechanism - Digilocker. 

Key pain points of customers on the KYC step - 

1. Frequent Digilocker downtime - 2 major outages/week. Customer conversion on KYC falls to zero during such downtimes, no backup flows for KYC implemented here. 
2. Friction for the customer to complete the KYC journey - 
    1. Customers have to input their complete Aadhaar number, DL PIN, Aadhaar OTP to complete KYC. 
    2. Partners when completing KYC of the customers need them to share Aadhaar OTP and DL P

**Solution:**
?**

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
    - P

---

## #11 — Bajaj KYC Coborrower enhancement and renewal
**Status:** Not started | **Last edited:** June 5, 2024 1:29 PM

**Problem:**
are we solving?**

1. Currently users with joint holdings can not do KYC.
2. Customer with Bajaj lender will not be able to enhance or renew their line. 

---

**Solution:**
?**

---

## #12 — Aadhaar QR scan
**Status:** Not started | **Last edited:** June 26, 2025 11:33 AM

# Aadhaar QR scan 1. Perfios Walk-through completed: SDK includes: 1. Scan QR (scanner) 2. Upload QR 3. Fetches and displays the data 4. To verify the email and phone, the customer has to enter email and phone Steps: 1. Scan QR/ Upload QR 2. Perfios de-codes the data on the QR 3. Fetches the data from UIDAI 4. Verify the email and phone Downside of SDK: Cannot be used for web-app (MFD portal) Perfios gave a walk through for the OCR KYC Plus: 1. Upload the Aadhaar 2. Scans the QR itself 3. Gives the address as the outputD 1. Bureau ID gave the following demo: 1. Upload the Aadhaar QR of the customer 2. It provides: 1. Adhaar last 4 digits 2. careOf 3. District 4. DOB 5. gender 6. location 7. landmark 8. mobile number registered? 9. email registered? 10. name of the customer 11. signature base64 12. state 13. street 14. sub district But when I gave it my black and white aadhaar and another coloured aadhaar card photo, they could not process it. They provide an API based solution thus it can be used across for web-app and mobile-app usage.

---

## #13 — Addition of City-State to CKYC Request in Decentro
**Status:** In progress | **Last edited:** June 18, 2025 6:10 PM

**Problem:**
are we solving?**

The Central Registry of Securitisation Asset Reconstruction and Security Interest (CERSAI) manages the centralized CKYC database. 

CKYCRR (CKYC Registry) maintains a master pincode list that works differently from the standard India Post directory. Here's how:

Source and Updates

- CKYCRR sources its pincode data from India Post (.csv file)
- Updates occur every 6 months
- Requires 3 weeks notice to Reporting Entities for implementation

Note: city and district are used through out the PRD inter-changeably. 

How the Master List Works

The CKYC Master List follows a specif

**Solution:**
?**

The solution has been presented in the notice provided by CERSAI published on 31st Jan 2025:
[**Notice by CERSAI](https://www.ckycindia.in/ckyc/assets/doc/4838-Rejection_in_upload_of_KYC_records_due_to_mismatch_of_PIN.pdf)**
The notice recognised the problem and gave the solution of passing the state and the city (which have been part of the request body but was not added before as they were optional). CERSAI will accept the city-state pair and process the documents if the pincode is missing.

This ensures no rejection from CERSAI’s  as well as 3rd Party Service Provider’s side due to the pincode missing with the CKYC Master Pincode List.

---

## #14 — [DSP] NSDL PAN Verification alignment
**Status:** Not started | **Last edited:** June 13, 2025 11:59 AM

**Problem:**
are we solving?**

As per RBI’s KYC guidelines, if as an RE we are obtaining PAN of the customer the same should be verified from the issuing authority (as per point 10(j) of Chapter III in the RBI KYC [Masterdirections](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566)). This means that PAN should be verified via the NSDL PAN verification API. 

![image.png](%5BDSP%5D%20NSDL%20PAN%20Verification%20alignment/image.png)

Currently we are not integrated with the NSDL PAN verification API, which makes us non-compliant. We need to plan and align on how to integrate NSDL PAN verifi

**Solution:**
?**

Understanding of the regulation - 

Where PAN is obtained, the same shall be verified from the verification facility of the issuing authority. 

“Verification facility of the issuing authority” makes it very clear that the PAN obtained should be verified by NDSL. 

We currently obtain PAN of the customer either from Digilocker or get it verified via PAN verification API provided by Signzy

- PAN document obtained from Digilocker is an e-document that NSDL (or UTIITSL) has already cryptographically signed and published. Does obtaining this document suffices the “verification facility of the issuing authority”? This is not clear.
    - Digio mentions that this suffices the compliance requirement.
    - Protean mentions that this does NOT suffice the compliance requirement.
    - Hyperve

---

## #15 — Tata Video KYC Integration V0
**Status:** In progress | **Last edited:** July 3, 2025 10:08 AM

**Problem:**
are we solving?**

Tata Capital mandated the VKYC process to be completed for each new customer from 1st April 2025. With larger vision and deeper potential partnerships in the horizon, restarting the business with Tata Capital is required.

To do so, we need to implement Tata  Capital’s VKYC in our journey flow.

---

**Solution:**
?**

Implementation of VKYC will cause significant rise in the drop-offs. With alignment from Tata, we can open the account without the customer completing the VKYC but it is mandatory for the customer to complete VKYC before raising a disbursement request.

For the initial launch (and till we observe stabilized funnels) we would be involving our Support team to help customers before and after (in cases of rejection/incomplete VKYC) with clear instructions and hand holding.

This is for the V0 launch only.

 

Note:

Tata’s Business Hour: 9AM - 6pm

[Activation: LSQ Task Creation](Tata%20Video%20KYC%20Integration%20V0/Activation%20LSQ%20Task%20Creation%20224e8d3af13a80c982dacebab3d9b6b0.md)

---

## #16 — NBFC Capturing Additional details post KYC
**Status:** Ready for Tech | **Last edited:** July 11, 2025 12:42 PM

**Problem:**
are we solving?**

Few LSPs integrating with our stack do not capture all the necessary ‘Additional Details’ or ‘declarations’ required by DSP to process the loan. In such cases, LSPs expect the DSP to collect these details directly from the customer.

---

**Solution:**
?**

---

## #17 — CKYC Upload for DSP
**Status:** In progress | **Last edited:** January 22, 2025 6:39 PM

**Problem:**
are we solving?**

- Manual effort in retrieving and matching data
    - CKYC is a manual process for a lot of banks where KYC records are manually updated and then converted into consumable format by Cersai.
- Prone to errors which might result in borrowers’ records getting updated incorrectly
    - Due to the manual nature of flows, the process is error prone and has an impact on user’s KYC data saved with Cersai (which may be used by other lenders) and may impact user experience
- Upload involves processing/accessing a lot of PII & KYC data of borrowers
    - A lot of PII information and KY

**Solution:**
?**

We will be building a file generator for ops team which will generate the CKYC reporting file (as per the guidelines of RBI) which can be uploaded directly to the SFTP portal by Cersai.

---

## #18 — [Platform] Photo verification and liveliness check
**Status:** Done | **Last edited:** January 21, 2025 7:21 AM

**Problem:**
are we solving?**

It is important to ensure that the user who is going through the application journey submits there own verification documents and details (POA, POI and bank account). 

There are multiple checks in place currently in the system that ensure that:

- Customer Aadhaar PAN seeding check
- Selfie/Photo verification (not liveliness check) with their Aadhaar
- Name verification with bank account (Aadhaar/PAN)

Despite these checks, we have seen cases in the past when operating as an LSP where users were able to bypass this check by clicking a screenshot/someone else’s photograph in

**Solution:**
?**

We will be integrating with Hyperverge’s photo verification and liveliness check stack where the photo will be first matched and then will be checked by a model which verifies if it was a live photograph or a picture of a picture

---

## #19 — CKYC (Decentro) API integration
**Status:** Done | **Last edited:** February 20, 2025 5:27 PM

**Problem:**
are we solving?**

- Manual effort in retrieving and matching data
    - CKYC is a manual process for a lot of banks where KYC records are manually updated and then converted into consumable format by Cersai.
- Prone to errors which might result in borrowers’ records getting updated incorrectly
    - Due to the manual nature of flows, the process is error prone and has an impact on user’s KYC data saved with Cersai (which may be used by other lenders) and may impact user experience
- Upload involves processing/accessing a lot of PII & KYC data of borrowers
    - A lot of PII information and KY

**Solution:**
?**

We will be integrating with Decentro’s upload API to push CKYC data to Cersai.

[Documentation](https://docs.decentro.tech/reference/kyc-and-onboarding-api-reference-identities-ckyc-services-upload-individuals)

API request sections:

| **Parameter** | **Type** | **Number of entries per API call** | **Mandatory** | **Definition** |
| --- | --- | --- | --- | --- |
| `name` | String | One | Yes. Hardcoded | The name of the employee who has done the KYC verification and is performing the CKYC upload.  |
| `designation` | String | One | Yes. | The designation of the employee who is performing the CKYC upload. |
| `kyc_declaration_place` | String | One | Yes. Hardcoded | The place of declaration or verification of the KYC documents. |
| `employee_code` | String | One | Yes. Hardcoded | The

---

## #20 — [Platform] Liveliness check
**Status:** In progress | **Last edited:** December 26, 2024 2:13 PM

**Problem:**
are we solving?**

Users can pledge their collateral using our platform and can get a loan within 5 minutes. The process is completely digital and can be done via just an application or website.

To ensure fair use of our product, there are certain checks that need to be in place to avoid frauds for un-willing / unaware users. 

The same is proposed by RBI in their guidelines:

<aside>
💡

The RE must ensure that the Live photograph of the customer is taken by the authorized officer and the same photograph is embedded in the Customer Application Form (CAF). Further, the system Application of th

**Solution:**
?**

We will be integrating with Digio’s passive liveliness check API which uses a base64 to identify the following checks:

- If there is a person in the image
- If the shared photograph is a live photo

What is a live photo?
When a customer clicks there photograph while actually being there in front of the lens - it is considered as a live photo. 

What is not a live photo?

- Photograph of a passport size picture
- Photograph of a screen (picture of person)
- Photograph of a person on a video call

---

## #21 — [Volt LSP] Liveliness check
**Status:** Not started | **Last edited:** December 23, 2024 8:08 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #22 — Volt LSP PAN verification
**Status:** Not started | **Last edited:** December 13, 2024 3:02 PM

**Problem:**
are we solving?**

A high number of customers are currently facing issues with Decentro PAN verification step on the LSP, this need to be solved.

---

**Solution:**
?**

---

## #23 — VKYC for DSP and Co-Lending
**Status:** In progress | **Last edited:** August 19, 2025 7:01 PM

# VKYC for DSP and Co-Lending [LSP Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/LSP%20Focused%20VKYC%20Journey%20Alignment%20238e8d3af13a80cd80c6f64c76ab3aed.md) [Volt Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/Volt%20Focused%20VKYC%20Journey%20Alignment%20216e8d3af13a801bbba2eb686074c82b.csv) [VKYC: Vendor Evaluation](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Vendor%20Evaluation%20217e8d3af13a80dfb53bed7d04c1e7f3.md) [VKYC: Regulatory Understanding](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Regulatory%20Understanding%20217e8d3af13a809f88e9f173d73f3d5a.md) [Discussion with Rohan (Groww)](VKYC%20for%20DSP%20and%20Co-Lending/Discussion%20with%20Rohan%20(Groww)%20254e8d3af13a8085a070ce018cec0f02.md)

---

## #24 — [DSP] KYC v2 (including CKYC)
**Status:** Ready for Tech | **Last edited:** August 13, 2025 12:55 PM

**Problem:**
are we solving?**

Currently for customers to complete KYC on DSP, they only have one KYC mechanism - Digilocker. 

Key pain points of customers on the KYC step - 

1. Frequent Digilocker downtime - 2 major outages/week. Customer conversion on KYC falls to zero during such downtimes, no backup flows for KYC implemented here. 
2. Friction for the customer to complete the KYC journey - 
    1. Customers have to input their complete Aadhaar number, DL PIN, Aadhaar OTP to complete KYC. 
    2. Partners when completing KYC of the customers need them to share Aadhaar OTP and DL PIN to complete KYC o

**Solution:**
?**

---

## #25 — Product note NSDL PAN Verification
**Status:** In progress | **Last edited:** April 7, 2026 3:21 PM

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users
- Ensuring all the various sources [Digilocker, LSP, CKYC, etc.] through which DSP is obtaining the PAN related details (PAN number, PAN Name, and PAN DoB) must be verified via NSDL as a part of compliance and KYC.
- Verification with Primary source for KYC being Digilocker.
-

# Product note: NSDL PAN Verification ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? As per RBI’s KYC guidelines, if as an RE we are obtaining PAN of the customer the same should be verified from the issuing authority (as per point 10(j) of Chapter III in the RBI KYC [Masterdirections](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566)). This means that PAN should be verified via the NSDL PAN verification API. ![image.png](%5BDSP%5D%20NSDL%20PAN%20Verification%20alignment/image.png) With the current sources for obtaining PAN that we use in the KYC journey 1. Digilocker PAN 2. If Digilocker PAN is not fetched, we use Signzy enrichment API for verification Currently we are not integrated with the NSDL PAN verification API for verifying PAN details, which makes us non-compliant. Also, even in cases where we are able to receive PAN document from Digilocker that also needs to be verified from NSDL which is the verification facility of the issuing authority as users can also directly update/ renew PAN with ITDB and records might not be synced with Digio. The interval/ frequency when digilocker updates the new PAN when a user renews it is also uncertain. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users - Ensuring all the various sources [Digilocker, LSP, CKYC, etc.] through which DSP is obtaining the PAN related details (PAN number, PAN Name, and PAN DoB) must be verified via NSDL as a part of compliance and KYC. - Verification with Primary source for KYC being Digilocker. - Fallback for Consuming Name from Decentro PAN API for Volt flows in order to use it for NSDL PAN Verification in the fallback flows (Volt) - ~~Downstream changes in th e agreement name and DoB.~~ ### Out of scope - - Call out on items out of scope - Rationale for exclusion - --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics (Conversion rate / Error rate / TAT) - Define post launch good state (Expected behaviour / uptime / SR) - Guardrail metrics (Metrics that should not degrade) - 100% compliance in terms of verifying Proof of identity in KYC

---

## #26 — Bajaj KYC Pod Requirements
**Status:** Not started | **Last edited:** April 4, 2024 1:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #27 — VKYC Integration PRD
**Status:** In progress | **Last edited:** April 23, 2026 9:30 AM

**Problem:**
are we solving?**

We need to implement a regulatory-compliant, secure, and operationally resilient agent-assisted Video KYC(vKYC) process for LAMF customers that:

- Ensures completion within RBI-prescribed timelines (72-hour KYC window)
- Handles real-world Internet instability (call drops, reconnects)
- Maintains audit-grade recording integrity
- Enables structured governance via agent and auditor layers
- Enforces geo-validation (India-only compliance)
- Provides tamper-proof audit trails
- Prevents fraud via face match and SOP-based verification

Without this system:

- VKYC may breach re

**Solution:**
?

We will implement a DSP-orchestrated, Hyperverge-powered, DSP agent-assisted vKYC lifecycle with the following pillars:

---

## #28 — CKYC Comms for Regulatory Compliance
**Status:** Done | **Last edited:** April 17, 2026 2:41 PM

**Problem:**
are we solving?

- Currently, DSP Finance (via Decentro) will search for an existing CKYC record in the CERSAI registry (using PAN) → if found, it downloads the data, compares it, and uploads any updates → if not found, it creates a new CKYC record.
- Regulatory compliance mandates that customers be notified when a CKYC record is created by DSP Finance.
- Currently, there is no automated mechanism to trigger an acknowledgement SMS to customers upon CKYC ID creation.
- Without this flow, DSP Finance risks non-compliance with RBI regulatory notification norms.

---

**Solution:**
?

**In scope:**
- Automated SMS trigger inline within the Decentro web-hook processing flow
- Per-record eligibility check (status == COMPLETED AND ckycReferenceId == null)
- Customer phone number resolution from internal system using fxcid_key
- Dynamo DB logging at per-record level for all outcomes (success, failure)
- Trigger Condition Logic
    - When Decentro’s bulk CKYC web-hook is received, the system insp

---

## #29 — KYC & Mandate Workflow PRD
**Status:** Done | **Last edited:** April 14, 2025 7:17 PM

**Problem:**
are we solving?**

1. LSPs currently need to integrate with third-party SDKs to complete the KYC and mandate steps. Integrating two separate SDKs is cumbersome, fails to establish a high standard for DSP, and raises compliance concerns when DSP credentials are shared with LSPs for SDK invocation.
2. Alternatively, LSPs can initiate the Digilocker/mandate step via a web URL, which opens in a web view belonging to a third-party provider. DSP has no control over the session, screens, or analytics on what step user dropped.
3. The go-live TAT for LSPs increases due to third-party SDK integrations,

**Solution:**
?**

We are introducing fully customizable, DSP-managed user screens to deliver a seamless, compliant, and consistent user experience. These screens will allow LSPs to customize themes and branding to align with their specific requirements.

This solution eliminates the reliance on third-party SDKs, reduces integration complexity, and accelerates the go-live process.

Additionally, LSPs can enable or disable specific modules, or manage them independently through backend APIs:

1. **KYC Module**:
    - Mandatory for all LSPs and cannot be skipped or disabled.
2. **Photo Verification**:
    - Optional module; LSPs can choose to disable it and handle verification via backend APIs.
3. **Additional Data Collection**:
    - Optional module; LSPs can disable it and manage the data collection proc

---

## #30 — CKYC Internal Report
**Status:** Not started | **Last edited:** April 10, 2025 2:50 PM

**Problem:**
are we solving?**

The Central Registry of Securitisation Asset Reconstruction and Security Interest (CERSAI) manages the centralized CKYC database for customer KYC verification. Currently, our team lacks visibility into the performance metrics of CKYC application submissions, including success rates, failure reasons, and backlog status.

There is a need for comprehensive monitoring and reporting on CKYC applications to:

1. Track submission success rates
2. Identify common failure reasons
3. Monitor backlogs
4. Analyze trends in application processing
5. Provide actionable insights for proces

**Solution:**
?**

The solution is to develop comprehensive dashboards that provide visibility into CKYC application metrics. These dashboards will track submissions, success rates, failure reasons, and backlogs.

---

## #31 — CKYC Flow integration
**Status:** Ready for kickoff | **Last edited:** Unknown

# CKYC Flow integration Charter: LOS Pod # Context [[Lending stack] KYC Flow](../PRDs/PRDs/%5BLending%20stack%5D%20KYC%20Flow%20f322514482d7490dbcf3675515b16276.md) # Process - [x] Map flow - [x] Scope out screens - [x] Benchmarking on flows # Figma xhttps://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3740-1840&t=182AaW1ur1jUPPnI-11 https://www.figma.com/design/khuVsTb01ruke7QxxOuCYR/Animation?node-id=4-1425&t=xNwnuqSfvRvHUnP7-11

---

## #32 — CKYC New flow
**Status:** Ready for kickoff | **Last edited:** Unknown

# CKYC New flow Charter: LOS Pod Priority: P0 Task type: Sprint # Context Need to work on creating a loader for CKYC flow which would last 10-12s # Process - [x] Selfie screen illustrations - [x] Wireframes for loader - [ ] Final Design # Figma https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=5170-7847&t=zvlUVrpOudLY6mV1-11

---

## #33 — API details
**Status:** Unknown | **Last edited:** Unknown

# API details This API documentation outlines various attributes in both the **Request Header** and **Request Body** sections. Below, I will explain each attribute in both sections for a better understanding. ### Request Header Attributes 1. **Ocp-Apim-Subscription-Key** (String, Mandatory): - A unique subscription key required for accessing the API. This is a static key that needs to be obtained from the APIM Gateway authority. 2. **MOAuthorization** (String, Mandatory): - A dynamic authorization token (Mauth Token) that must be obtained and passed. This is managed by the respective authority and is not required if the request is initiated from an SFDC channel. 3. **Content-Type** (String, Mandatory): - Default value is `"application/json"`. It specifies the format of the data being sent. 4. **Authorization** (String, Mandatory): - An authorization token, typically OAuth2, used for accessing the API securely. ### Request Body Attributes 1. **XML_PACKET** (String, Optional): - Specifies whether CKYC XML Data will be included in the response. Default value is 'Y'. Possible values: - `'Y'`: XML Data will be included. - `'N'`: Only extracted fields will be returned. 2. **BITLY** (String, Optional): - Indicates whether a URL will be sent in the response or through SMS. Default value is 'N'. Possible values: - `'N'`: URL will be included in the response. - `'Y'`: URL will be sent via SMS. 3. **SOURCE_REQUEST_TIME** (String, Mandatory): - The timestamp of the request in the format `YYYY-MM-DD HH:MM:SS`. 4. **PROCESS_MODE** (String, Mandatory): - Indicates the mode of the process. Possible values: - `'UI'`: For user interface modes such as CKYC, OKYC. - `'API'`: Applicable when KYC Mode is CKYC. 5. **SOURCE_REQUEST_ID** (String, Mandatory): - A unique ID to identify the source channel request. 6. **APPLICATION_ID** (String, Optional): - A unique Application ID of the sourcing channel. 7. **CHANNEL_KEY** (String, Mandatory): - A static key that identifies the sourcing channel, obtained during the initial setup. 8. **CUSTOMER_ID** (String, Optional): - The customer identifier. 9. **POI_TYPE** (String, Optional): - Proof of Identity Type. Possible values include PAN, PASSPORT, UID, etc. 10. **POI_NO** (String, Optional): - The corresponding number for the specified POI type. 11. **DOB** (String, Mandatory): - Customer's Date of Birth in the format `YYYY-MM-DD`. 12. **CUSTOMER_TYPE** (String, Optional): - Customer type for reporting purposes. Possible values: New, Existing. 13. **FORCE_REFRESH_FLAG** (String, Optional): - Indicates whether to bypass the KYC search for an existing customer. Possible values: 'Y', 'N'. 14. **GENDER** (String, Optional): - Customer gender. Mandatory

---

## #34 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #35 — SDK
**Status:** Unknown | **Last edited:** Unknown

# SDK - JS sdk - IOS sdk - Android SDK - RN sdk - partner mobile APP, web , PLJ - Iframe - webhook for partner , v-kyc done or not to partners - API exposed, Get application status , KYC done , bifurcation -

---

## #36 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #37 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #38 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #39 — Activation LSQ Task Creation
**Status:** Unknown | **Last edited:** Unknown

# Activation: LSQ Task Creation Flow: 1. Link generated gets generated and sent to the MFD over whatsapp 2. Task gets published in LSQ 3. RMs follow the tasks for calling and supporting the MFD with the VKYC flow and the link

---

## #40 — Discussion with Rohan (Groww)
**Status:** Unknown | **Last edited:** Unknown

# Discussion with Rohan (Groww) 1. Building in-house after 1 year of operations is recommendable instead of building it in-house from the start 2. VideoSDK has good solution for the video session. 3. Groww built all the in-house cause they were aiming for 4. Hyperverge gives a high amount of false negatives 5. Initially: Success rate → 80% and VKYC completion rate → 70% 6. After spending 2 quarters improving on the Vkyc stack, Success rate → 95% and VKYC completion rate → 80% 7. It is important to store the data correctly and in a reproducible manner. 8. IDfy and Digio are recommended VKYC solution providers 9. Digio uses VideoSDK for their video stack - confirmed 10.

---

## #41 — LSP Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# LSP Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an NBFC, our control is limited over the Pre-VKYC and Post-VKYC user experience. Following are the steps of a VKYC journey which we govern: ## Journey Flow: ### Pre-VKYC Session: 1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP) - What is the 3 days Rule? RBI mandates VKYC be completed within 3 days from completing e-KYC. If the customer does not, lender will need to initiate the e-kyc flow

---

## #42 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #43 — Name
**Status:** Unknown | **Last edited:** Unknown

# Name Column 1: Does it check if the permissions are given? Column 2: Switch On Permission automatically/guide the customer? Column 3: Is Scheduling Available? Column 4: Configure communications for scheduled customers? Column 5: Is Digi Locker Integrated? Column 6: Is Pan Required? Column 7: Does Dashboard have Analytics Available?

---

## #44 — VKYC Vendor Evaluation
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Vendor Evaluation # Evaluation Criteria # Vendor List List of vendors. - Hyperverge - Demo completed (SDK) - IDFy - Perfios - Signzy - Demo Complete (API driven) - Digio - Demo Completed - AuthBridge - Demo Completed - Pixl - Demo not Completed - KYC Hub - Demo Completed # Evaluation ## Summary [Untitled](VKYC%20Vendor%20Evaluation/Untitled%20216e8d3af13a80248558f522cbf900a8.csv) ## Hyperverge ## IDFy ## Perfios

---

## #45 — Volt Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# Volt Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process). ## Pre-VKYC 1. Initiation Page: 1. Pre-messaging: 1. Educate about VKYC 1. Context Setting for the customer: 1. Mandatory Step by RBI 2. Inform about the 3days rule - What is the 3 days Rule? RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC

---

## #46 — CKYC OTP verify error cases
**Status:** Unknown | **Last edited:** Unknown

# CKYC OTP verify error cases | **Case description** | **Condition** | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | Customer enters wrong OTP | | | | | Resend tried by customer before 90 secs | | | | | Exceeded OTP verify attempts | | | | | | | | |

---

## #47 — CKYC S&D error handling
**Status:** Unknown | **Last edited:** Unknown

# CKYC S&D error handling | **Case description** | CKYC terminal status | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | PAN or Mobile number do not match with the records in Cersai. | | | | | Mobile number doesn’t match | | | | | Mobile number doesn’t exist | | | | | Customer doesn’t exist in CKYCRR | | | |

---

## #48 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements - Complete journey in DSP theme - Do we need a new anchor page on the Volt side? - What will happen in case customer drops off and starts the KYC journey again? - What will happen if the user faces an error in KYC? - Include an optional “Secondary logo”. This will be configured for each LSP - How can we make sure customers enter PAN details as per PAN only? - Add digilocker screens as well in the flow, this will be added in case CKYC fetch is failed - Do we need the KYC successful bottom sheet **Wed 19th March, 2025** - [x] Two sections one for Volt and another for DSP - [x] DSP will have a header as well, LSPs can pass a parameter to show or hide the header - [x] Primary, secondary, tertiary colour change option @Karuna Sankolli - [x] Retry KYC screen, this will be from Volt Side @Karuna Sankolli - [x] Secondary logo pendikng @Karuna Sankolli - [x] Rethink retake selfie flow @Karuna Sankolli - [ ] What will Volt header show when the DSP KYC is in progress @Saksham Srivastava - [ ] Deviation flow will be there or not? @Saksham Srivastava - [x] Jupiter colors @Saksham Srivastava

---

## #49 — NSDL error messaging
**Status:** Unknown | **Last edited:** Unknown

# NSDL error messaging | **Case description** | **Condition** | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | NSDL returns name not matching | | | | | NSDL returns DOB not matching | | | | | NSDL returns | | | |