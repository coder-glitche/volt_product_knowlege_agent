# [Platform] Unpledging of unlinked funds bulk approval

: Vaibhav Arora
Created time: February 26, 2025 7:53 AM
Status: Pending Review
Last edited: March 5, 2025 10:35 AM

# **What problem are we solving?**

There can arise scenarios where the user pledges securities with the NBFC and changes their mind and does not end up taking a loan with the NBFC. 

As per an RBI regulation, the REs are supposed to release all the original movable / immovable property documents and remove charges registered with any registry within a period of 30 days after full repayment/ settlement of the loan account. ([Link](https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=12535&utm_source=chatgpt.com))

While the regulation does not explicitly mention the scenario where the loan is not taken by the customer, in principal the NBFC should comply with regulations and unpledge all pledged securities by the customers within 30 days of pledging (if the loan is not taken by the user.

There are multiple challenges and risks that may arise due to this:

- Collateral risk: Unpledged securities can be lodged against an loan if necessary validations and checks are not placed in the system.
- Compliance risk: Any delays can raise to the customer escalating to the regulatory bodies
- Customer experience risk: This seriously impacts the customer experience as if the customer decides to redeem securities instead of pledging to get a loan or decides to go ahead with another lender, they will not be able to do so till the lien from the securities is not removed
- 

Following are problems that arise due to this problem statement:

- Lack of visibility to LSP and end customer (On dropping off, there is limited visibility for the LSPs as well as the customers on the status of lien marking on their securities)
- DSP operations team are not able to process such requests at the moment and resort to reaching the tech ops team for manually un-pledging these securities.
- Since these transactions are processed manually and pass through multiple stakeholders across teams, a lot of risk for  incorrect lodgement/compliance are introduced which can have direct financial implication for the NBFC

---

# **How do we measure success?**

- Number of opportunities suspended post pledging of collaterals
- TAT taken for NBFC to release funds (Time difference between date of lien marking and date of unpledging)

---

# **How are others solving this problem?**

BFL and TCL manage these processes operationally and rely on the NBFC to share the information with them to unpledge securities of the user. 

TCL team manages lien marking date and the status of lodgement for all collaterals with ageing (Current date - date of lodgement). Securities pledged before 30 days are unpledged for the users.

---

# **What is the solution?**

We will be making a bulk operations maker, which will allow the NBFC operations agent to upload a file (at a security / ISIN / Lien reference number level). 

Bulk (file based) checker task for validation of the bulk unpledging file by the operations team (Manual verification of the initially lodged file)

NBFC currently supports unpledging requests only at a loan account level, a loan account is created only when the origination process (loan application) is completed by the user. We will be creating an opportunity level unpledging workflow (using step functions) to support the complete unpledging process.

Each bulk maker job (like bulk lodgement) will create independent unpledging requests at an opportunity level, these independent requests will be present in the applications section with the title “Unpledge collateral”. (Non STP: Will go through checker approval)

Referencing and analytics of bulk files uploaded by the operations team (Will be visible to the checker agent while approving independent opportunity level unpledging

Validations (Regex based) in the maker and checker bulk based file task)

NBFC will building multiple systemic checks to mitigate all risks for the organisation:

- Opportunity suspension: Whenever a request is created, an independent checker task at an opportunity level will be created (please note that the operations team will be sharing the corresponding opportunity ID with the collateral details for unpledging)
- Lien reference number for CAMS and KFIN reference number for KFIN will be blacklisted (in collateral dedupe) to ensure the same securities are not pledged against a different opportunity for the same customer (by the same/different LSP)
- Pledge verification before unpledging using lien status and portfolio APIs
- PAN dedupe: Unpledging requests against PANs which are associated with an active loan account will be rejected and not processed via this maker

## User stories / User flow

User comes to one of the associated LSPs for a loan against securities:

1. LSP creates opportunity for the user
2. User application steps (not mandatory) (bank verification / mandate registration / KYC) with the LSP and pledges securities
3. User drops off and does not complete their application

Now two scenarios can arise post the above three steps:

- User requests the LSP to unpledge funds
- NBFC reconciles unlinked securities over 20 days, and shares an update with LSP to either complete the application or process the corresponding unmarking

In both scenarios, the NBFC operations team will be able to upload a bulk file of securities at an ISIN Folio level to unpledge securities for the user.

<aside>
⚠️

Please note: Current scope only covers unpledging of securities and managing corresponding risk. Coordination with LSPs for completing applications and maintaining corresponding ageing for unlinked funds will be done operationally

</aside>

## Requirements

Bulk file based maker:

Operations agent will be able to upload a bulk unpledging file on the command centre in the NBFC operations section (NBFC operations section will be renamed to ops and mandate presentation section will be moved to an independent section in the side navigation panel) 

- File will have the following parameters (Each row will describe one ISIN + Folio + Lien ref combination:
    - Opportunity ID: Opportunity ID of customer which has to be suspended
    - PAN: PAN number of the user whose securities are being unpledged
    - ISIN: Unique security identification number of the mutual fund that has to be unpledged
    - Folio Number: Unique Folio of the user whose mutual fund has to be unpledged
    - Units: Number of units that have to be unpledged
    - Lien reference number / KFIn reference number: Request reference number from the RTAs
    - Lien marking number / IHNO: Transaction reference number for the RTAs
- File will go through the following Regex based validations and validations before creating independent unpledging tasks:
    - Regex check for investor PAN
    - Internal dedupe for file (Same ISIN + Folio + RRN should not repeat within the file)
    - Number of records check (We will be placing an initial limit of 100 records that can be unpledged at once with the RTAs.
    - Regex check for opportunity
    - Regex check for ISIN
- Response file:
    - Response file will have all the parameters of the request file along with two additional statuses:
        - Request status: Accepted / Rejected
        - Rejection reason:
            - PAN regex failed
            - Duplicate record (For duplicate file entries)
            - Number of records more than the prescribed limit (100 records)
            - Invalid opportunity ID (OppID regex)
            - Invalid ISIN (ISIN regex)
- Response file will then be approved via checker in a checker task (Bulk file approval)
- Post approval independent unpledging requests will be created at an opportunity level (Has to be batched via BE)
- Reference of the file name and the task ID (of the maker of bulk file processing) should be stored against each unpledging request so that the analytics team can build the corresponding analytics on top of it

---

# **Design**

[https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=576-6955&t=GdEt4WEnlYxPwmFn-4](https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=576-6955&t=GdEt4WEnlYxPwmFn-4)

---

# **Analytics**

- File based analytics (Each unpledging request will have a reference to the task) Operations team should be able to track the following file based metrics:
    - Number of unpledging requests in file
    - Status level distribution (unpledging) for each task/file uploaded
        - Number of unpledging request accepted
        - Number of unpledging request rejected
        - Number of unpledging request failed (before checker creation)
        - Number of unpledging request successfully processed
- Number of files processed
- TAT to process a file (maker submitted to checker approved)
- TAT for individual unpledging request (Started on and completed on)

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