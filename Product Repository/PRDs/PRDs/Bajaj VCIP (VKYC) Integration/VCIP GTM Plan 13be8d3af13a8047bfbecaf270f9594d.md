# VCIP GTM Plan

- First to decide default : - what will happen if we don’t develop ?
    - to Schedule call with bajaj
    - They will start on 15th Nov
    - they have asked us for the Timelines
- IF we Decide to not build then what should happen
    - We should move out of Bajaj
    - We should move to Tata or DSP
        - Tata is p3 as the lien charges are high
        - DSP will take 1-2 months to be operational
- If we decide to build then what the flow should be ?
    - VCIP stop:- We can Block all the steps till V-kyc is Done
        - Safer and operationally less challenging, but higher dropoffs
    - VCIP end:- We can allow all the steps and V-kyc can be done last
        - Easier and recommended by Bajaj, But more customer complains and Higher operations cost
- To integrate the VCIP we need to make additions to the UI screens in Bajaj flow
    - Figma?
    - API integration, testing , and response handling.
    - Permissions handling
- Platform changes

| Platform  | Changes |  |
| --- | --- | --- |
| Web | New UI screens, chrome permissions, | API |
| Android/IOS | New UI screens , API, Permissions  |  |
| MFD Saas  |  |  |
| B2B |  |  |
| MFD  | Need to stop MFD and have a link that user can Open  |  |

| VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... |
| Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... |
- Tech side , most volume channels

- Step ID - Analytics , LSQ, DB, OPS
- SDK complatablity - Sagar
- Neo - Is oversees
- JS/React native SDK verison update required ?
- Android SDK New AAR file required?
- IOS SDK new Framework files required ?
- Webhook URL to send the Updated Status to the partner
- UI / Copy changes for the MFD on the Vkyc step
- Get application status new status
- enhance limit , account open ,
- operations handling of etb customer

Development scope 

- UI change-  Figma
- API integration and testing
- Response handling
- Web testing
- Partner platforms , SDKs testing

Flow is that it is a Single mandatory step after offer 

- Selects Bajaj for lender
- Digilocker KYC
- Basic information
- VCIP, with one CTA and get back when VCIP is complete
- rest of the Flow remains same

Having VCIP as Blocker for the User is easier to develop and And push to partners but will result in huge drop -off and lost clients 

What will be the VCIP development ?

- User would have to do VCIP for Bajaj. All partners , any amount. User will see VCIP as a new step in there loan journey.
- User will have to do video call with agent during the Working hours (9am to 6pm)
- VCIP will block the account creation in Bajaj?

Where the VCIP step be in the Bajaj Journey ?

- We can have VCIP to be the last step after agreement
    - Operationally challenging but we can focus on the Higher intend customers
- We can have VCIP after Digilocker
    - Simpler and consistent with KYC Step but Huge Drop off in the near top of the funnel.

What is required for VCIP tech development ?(phase 1): goal is to launch the VCIP

- VKYC Step creation and handling
- VKYC UI creation
- VKYC API integration and response handling
- Testing on the main platform
- Testing across B2b And B2b2c platforms

What is taken up in Phase 2? 

- Re-engagement strategy with communications and notifications
- VKYC parallel flow

What is required for VCIP Sales side ?

- We need to Focus on the getting the People across the VCIP step

What is required to be communicated to Partners ?

- the VCIP addition and the likely drop-off increase
- Issues with Un-lien for some customers and process to raise Un-lien
- And the required effort on sales

What is required from Operations ?

- Expect more Un-lien calls

Business trade-offs?

- Should we go for lower top of the funnel or higher operational costs?
- Are the customers to Pay the Un-lien charges in case of VCIP miss?
- Do we want to keep the the Instant Disbursal messaging for Bajaj?

Resource planning ?

To be decided 

List of Platforms? [https://docs.google.com/spreadsheets/d/1e0nrI65l0tXsHurtpZlv0b8jz4x2FHHzLNJcIxWemUs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1e0nrI65l0tXsHurtpZlv0b8jz4x2FHHzLNJcIxWemUs/edit?usp=sharing)

How will the new Flow work ?

- User complete the application exactly like current flow
- User  will have to complete the VCIP after the Mandate step
- Then user can raise a withdrawal request.
- MFD partner can share the V-KYC link to the borrowers

For Un-lien, User can use manage limits and un-pledge from there we will build a custom flow to collect Rs 450 fees from. customer who have Pledged assets but no Credit line open (>7 days)

- this flow can be trigger by support too